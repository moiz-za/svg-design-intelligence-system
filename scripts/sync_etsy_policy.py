#!/usr/bin/env python3
"""
Automated Etsy Policy & Engine Dual-Repo Sync Script
Synchronizes rulebooks between:
  - svg-design-intelligence-system (integration/etsy-seo-engine/)
  - etsy-seller-seo-system (skill/references/)

The seller repo is the policy source of truth. Prefer `--from-seller`
(one-way pull) over the default mtime-based bidirectional sync, which can
clobber a newer upstream release with stale local files. `--build` rebuilds
esvg-dis.skill with no cross-repo access.

Maintainer utility — not needed for normal skill usage. Auto-detects both repos
when cloned side by side; override locations with ESVG_REPO / SELLER_REPO env vars.
"""

import os
import sys
import shutil
import hashlib
import json
import zipfile
import argparse
from pathlib import Path

SELLER_REPO_DIRNAME = 'etsy-seller-seo-system'
ESVG_REPO_DIRNAME = 'svg-design-intelligence-system'


def _walk_up(start: Path, predicate):
    current = start.resolve()
    for candidate in [current] + list(current.parents):
        if predicate(candidate):
            return candidate
    return None


def detect_repos(script_path: Path):
    """Locate both repo roots from the script's own location.

    A seller repo has skill/references/ and no integration/etsy-seo-engine/;
    an ESVG repo has integration/etsy-seo-engine/. If only one is found, the
    other is looked up as a sibling directory.
    """
    p = script_path.resolve().parent
    esvg = _walk_up(p, lambda c: (c / 'integration' / 'etsy-seo-engine').is_dir())
    seller = _walk_up(p, lambda c: (c / 'skill' / 'references').is_dir()
                      and not (c / 'integration' / 'etsy-seo-engine').is_dir())
    if esvg is None and seller is not None:
        esvg = seller.parent / ESVG_REPO_DIRNAME
    if seller is None and esvg is not None:
        seller = esvg.parent / SELLER_REPO_DIRNAME
    return esvg, seller


_SCRIPT_PATH = Path(__file__).resolve()
_ESVG_FOUND, _SELLER_FOUND = detect_repos(_SCRIPT_PATH)
REPO_SELLER = Path(os.environ.get('SELLER_REPO')) if os.environ.get('SELLER_REPO') else _SELLER_FOUND
REPO_ESVG = Path(os.environ.get('ESVG_REPO')) if os.environ.get('ESVG_REPO') else _ESVG_FOUND

DIR_ESVG = REPO_ESVG / 'integration' / 'etsy-seo-engine' if REPO_ESVG else None
DIR_SELLER = REPO_SELLER / 'skill' / 'references' if REPO_SELLER else None

FILES_TO_SYNC = ['listing-guide.md', 'seo-guide.md', 'policies.md']
PLAYBOOKS = [
    'ab-testing.md', 'action-layer-pointers.md', 'ai-image-compliance.md',
    'conversion-floor.md', 'listing-health-score.md', 'platform-fit-check.md',
    'price-positioning.md', 'regional-handling.md',
    'search-intent-classification.md', 'trademark-stoplist.md', 'video-brief.md'
]

SKIP_NAMES = {'.DS_Store', '__pycache__', 'Thumbs.db', '.gitkeep'}


def get_hash(filepath):
    if not filepath.exists():
        return None
    return hashlib.md5(filepath.read_bytes()).hexdigest()


def get_mtime(filepath):
    if not filepath.exists():
        return 0
    return filepath.stat().st_mtime


def sync_files():
    print("🔄 --- AUTOMATED ETSY POLICY & ENGINE DUAL-REPO SYNC ---")
    if DIR_ESVG is None or not DIR_ESVG.exists():
        print(f"❌ ESVG repo not found (looked for sibling dir '{ESVG_REPO_DIRNAME}').")
        print("   Set ESVG_REPO env var or clone both repos side by side.")
        return False
    if DIR_SELLER is None or not DIR_SELLER.exists():
        print(f"⚠️ Standalone etsy-seller-seo-system repo not found (looked for sibling dir '{SELLER_REPO_DIRNAME}'). Skipping cross-repo sync.")
        return True

    synced_count = 0

    # Sync root files
    for filename in FILES_TO_SYNC:
        f_esvg = DIR_ESVG / filename
        f_seller = DIR_SELLER / filename

        h_esvg = get_hash(f_esvg)
        h_seller = get_hash(f_seller)

        if h_esvg != h_seller:
            m_esvg = get_mtime(f_esvg)
            m_seller = get_mtime(f_seller)

            if m_esvg > m_seller:
                print(f"  --> Copying newer {filename} from ESVG ➔ Etsy Seller SEO System")
                shutil.copy2(f_esvg, f_seller)
                synced_count += 1
            else:
                print(f"  <-- Copying newer {filename} from Etsy Seller SEO System ➔ ESVG")
                shutil.copy2(f_seller, f_esvg)
                synced_count += 1

    # Sync playbooks
    pb_esvg_dir = DIR_ESVG / 'playbooks'
    pb_seller_dir = DIR_SELLER / 'playbooks'

    pb_esvg_dir.mkdir(exist_ok=True)
    pb_seller_dir.mkdir(exist_ok=True)

    for filename in PLAYBOOKS:
        f_esvg = pb_esvg_dir / filename
        f_seller = pb_seller_dir / filename

        h_esvg = get_hash(f_esvg)
        h_seller = get_hash(f_seller)

        if h_esvg != h_seller:
            m_esvg = get_mtime(f_esvg)
            m_seller = get_mtime(f_seller)

            if m_esvg > m_seller:
                print(f"  --> Copying newer playbook {filename} from ESVG ➔ Etsy Seller SEO System")
                shutil.copy2(f_esvg, f_seller)
                synced_count += 1
            elif m_seller > m_esvg:
                print(f"  <-- Copying newer playbook {filename} from Etsy Seller SEO System ➔ ESVG")
                shutil.copy2(f_seller, f_esvg)
                synced_count += 1

    if synced_count == 0:
        print("✅ Both repositories are already 100% synchronized! Zero drift detected.")
    else:
        print(f"🎉 Successfully synchronized {synced_count} file(s) across both repositories!")
        rebuild_packages()

    return True


def pull_from_seller():
    """One-way sync: Etsy Seller SEO System ➔ ESVG integration/etsy-seo-engine/.

    Use this when the seller repo is the policy source of truth. It never
    writes to the seller repo, so newer local mtimes cannot clobber an
    upstream policy release.
    """
    print("⬅️ --- ONE-WAY POLICY PULL: Etsy Seller SEO System ➔ ESVG ---")
    if DIR_ESVG is None or not DIR_ESVG.exists():
        print(f"❌ ESVG repo not found (looked for '{DIR_ESVG}').")
        return False
    if DIR_SELLER is None or not DIR_SELLER.exists():
        print(f"❌ Etsy Seller SEO System not found (looked for sibling '{SELLER_REPO_DIRNAME}').")
        print("   Set SELLER_REPO env var or clone both repos side by side.")
        return False

    pulled = 0
    missing = []

    for filename in FILES_TO_SYNC:
        src = DIR_SELLER / filename
        dst = DIR_ESVG / filename
        if not src.exists():
            missing.append(filename)
            continue
        if get_hash(src) != get_hash(dst):
            shutil.copy2(src, dst)
            print(f"  <-- Pulled {filename} ➔ ESVG")
            pulled += 1

    pb_seller_dir = DIR_SELLER / 'playbooks'
    pb_esvg_dir = DIR_ESVG / 'playbooks'
    pb_esvg_dir.mkdir(exist_ok=True)

    for filename in PLAYBOOKS:
        src = pb_seller_dir / filename
        dst = pb_esvg_dir / filename
        if not src.exists():
            missing.append(f"playbooks/{filename}")
            continue
        if get_hash(src) != get_hash(dst):
            shutil.copy2(src, dst)
            print(f"  <-- Pulled playbook {filename} ➔ ESVG")
            pulled += 1

    if missing:
        print(f"⚠️ Not found in seller repo (skipped): {', '.join(missing)}")

    if pulled == 0:
        print("✅ ESVG already matches the seller repo rulebooks. Zero drift detected.")
    else:
        print(f"🎉 Pulled {pulled} file(s) from the seller repo.")
        rebuild_esvg_package()

    return True


ESVG_ARCHIVE_DIRS = ['workflow', 'knowledge', 'prompts', 'integration', 'playbooks', 'state-templates', 'examples']
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def _zip_member(z, fp, arcname):
    """Write one file with a fixed timestamp so archives are reproducible."""
    info = zipfile.ZipInfo(arcname, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, Path(fp).read_bytes())


def _expected_esvg_members():
    """Map archive member name -> source path for esvg-dis.skill."""
    members = {}
    skill_dir = REPO_ESVG / 'skill'
    members['SKILL.md'] = skill_dir / 'SKILL.md'
    bootstrap = skill_dir / 'scripts' / 'bootstrap.py'
    if bootstrap.exists():
        members['scripts/bootstrap.py'] = bootstrap

    for d in ESVG_ARCHIVE_DIRS:
        dp = REPO_ESVG / d
        if not dp.exists():
            continue
        for root, dirs, files in os.walk(dp):
            dirs.sort()
            for f in sorted(files):
                if f in SKIP_NAMES or f.endswith(('.pyc', '.pyo')):
                    continue
                fp = Path(root) / f
                members[str(fp.relative_to(REPO_ESVG))] = fp
    return members


def rebuild_seller_package():
    """Rebuild etsy-seller.skill — skill/ + state-templates/ (zip install layout)."""
    if REPO_SELLER is None:
        return
    output = REPO_SELLER / 'etsy-seller.skill'
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
        for base in [REPO_SELLER / 'skill', REPO_SELLER / 'state-templates']:
            if not base.exists():
                continue
            for root, dirs, files in os.walk(base):
                dirs.sort()
                for f in sorted(files):
                    fp = Path(root) / f
                    if f in SKIP_NAMES or f.endswith(('.pyc', '.pyo')):
                        continue
                    _zip_member(z, fp, str(fp.relative_to(REPO_SELLER / 'skill')))

    print(f"✅ Rebuilt etsy-seller.skill ({REPO_SELLER.name}: skill/ + state-templates/)")


def rebuild_esvg_package():
    """Rebuild esvg-dis.skill — full multi-folder layout matching the repo structure."""
    if REPO_ESVG is None:
        return
    output_esvg = REPO_ESVG / 'esvg-dis.skill'
    if output_esvg.exists():
        output_esvg.unlink()

    with zipfile.ZipFile(output_esvg, 'w', zipfile.ZIP_DEFLATED) as z:
        for arcname, fp in _expected_esvg_members().items():
            if not fp.exists():
                print(f"⚠️ Missing source file: {fp}")
                continue
            _zip_member(z, fp, arcname)

    print(f"✅ Rebuilt esvg-dis.skill ({REPO_ESVG.name}: full multi-folder layout)")


def check_esvg_archive():
    """Verify the committed esvg-dis.skill matches the repo tree.

    Compares member names and file bytes rather than raw zip bytes, so the
    check is stable across zlib/platform differences.
    """
    output = REPO_ESVG / 'esvg-dis.skill'
    if not output.exists():
        print(f"❌ {output.name} not found. Run: python3 scripts/sync_etsy_policy.py --build")
        return False

    expected = _expected_esvg_members()
    with zipfile.ZipFile(output) as z:
        actual = set(z.namelist())
        missing = sorted(set(expected) - actual)
        extra = sorted(actual - set(expected))
        changed = sorted(
            name for name in (set(expected) & actual)
            if z.read(name) != expected[name].read_bytes()
        )

    if not (missing or extra or changed):
        print(f"✅ {output.name} matches the repo tree ({len(expected)} entries).")
        return True

    if missing:
        print(f"❌ Missing from archive: {', '.join(missing)}")
    if extra:
        print(f"❌ Stale entries in archive: {', '.join(extra)}")
    if changed:
        print(f"❌ Out-of-date entries: {', '.join(changed)}")
    print("Run: python3 scripts/sync_etsy_policy.py --build  (then commit esvg-dis.skill)")
    return False


def rebuild_packages():
    print("📦 Rebuilding skill archives...")
    rebuild_seller_package()
    rebuild_esvg_package()


def main():
    parser = argparse.ArgumentParser(
        description="ESVG-DIS policy sync and packaged-skill build.")
    parser.add_argument(
        '--from-seller', action='store_true',
        help="One-way pull: Etsy Seller SEO System ➔ ESVG (recommended; never writes to the seller repo).")
    parser.add_argument(
        '--build', action='store_true',
        help="Rebuild esvg-dis.skill from the repo tree without any cross-repo sync.")
    parser.add_argument(
        '--check', action='store_true',
        help="Verify the committed esvg-dis.skill matches the repo tree (CI use).")
    args = parser.parse_args()

    if args.check:
        sys.exit(0 if check_esvg_archive() else 1)
    elif args.build:
        rebuild_esvg_package()
    elif args.from_seller:
        pull_from_seller()
    else:
        sync_files()


if __name__ == '__main__':
    main()
