#!/usr/bin/env python3
"""
bootstrap.py — One-time state initialization for the
svg-design-intelligence-system skill (v1.1).

Detects whether the user's research log exists at ~/esvg-research/.
If not, creates it from the bundled template in state-templates/.

Idempotent — safe to call on every skill invocation. Returns early if
state already exists.

Usage:
    python3 bootstrap.py [--state-dir PATH] [--templates-dir PATH] [--quiet]

Default paths:
    state-dir:     ~/esvg-research
    templates-dir: auto-detected (supports both git-clone and .skill zip layouts)

Deliberately minimal compared to a full listing-tracking system — this
skill does design research and concept development, not published-
listing tracking, so it only needs a single research log, not a
multi-file database. See ../../documentation/architecture-decisions.md
for why this stays lightweight on purpose.
"""
import argparse
import shutil
import sys
from pathlib import Path


def find_default_templates_dir(script_dir: Path) -> Path:
    """Locate state-templates, handling two different install layouts.

    Git-clone layout:  repo/skill/scripts/bootstrap.py
                       repo/state-templates/esvg-research/   ← two levels up

    .skill zip layout: ~/.claude/skills/<name>/scripts/bootstrap.py
                       ~/.claude/skills/<name>/state-templates/esvg-research/ ← one level up

    Try one level up first (zip layout); fall back to two levels up (repo layout).
    """
    one_up = script_dir.parent / "state-templates" / "esvg-research"
    if one_up.exists():
        return one_up
    return script_dir.parent.parent / "state-templates" / "esvg-research"


def find_default_state_dir() -> Path:
    return Path.home() / "esvg-research"


def state_exists(state_dir: Path) -> bool:
    """State is considered to exist if research-log.md is present."""
    return (state_dir / "research-log.md").exists()


def bootstrap(state_dir: Path, templates_dir: Path, verbose: bool = True) -> dict:
    """Create state structure from templates. Idempotent."""
    result = {
        "state_dir": str(state_dir),
        "templates_dir": str(templates_dir),
        "already_existed": False,
        "files_created": [],
        "errors": [],
    }

    if state_exists(state_dir):
        result["already_existed"] = True
        if verbose:
            print(f"[bootstrap] State already exists at {state_dir} — no action.")
        return result

    if not templates_dir.exists():
        result["errors"].append(f"Templates dir not found: {templates_dir}")
        return result

    state_dir.mkdir(parents=True, exist_ok=True)
    if verbose:
        print(f"[bootstrap] Created state dir: {state_dir}")

    # Copy every entry from the template folder, skipping OS/editor junk
    # (.DS_Store, __pycache__, etc.) that shouldn't end up in the user's
    # state directory even if it accidentally got committed upstream.
    SKIP_NAMES = {".DS_Store", "__pycache__", "Thumbs.db", ".gitkeep"}
    for entry in templates_dir.iterdir():
        if entry.name in SKIP_NAMES or entry.name.startswith("."):
            continue
        target = state_dir / entry.name
        if target.exists():
            continue
        if entry.is_dir():
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
        result["files_created"].append(str(target.relative_to(state_dir)))
        if verbose:
            print(f"[bootstrap] Copied: {entry.name}")

    if verbose:
        print(f"[bootstrap] Done. {len(result['files_created'])} entries created.")
        print(f"[bootstrap] Your research log is ready at: {state_dir}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Bootstrap svg-design-intelligence-system skill state (v1.1).")
    parser.add_argument("--state-dir", type=Path, default=None,
                        help="Where to create state (default: ~/esvg-research)")
    parser.add_argument("--templates-dir", type=Path, default=None,
                        help="Source templates (default: ../../state-templates/esvg-research)")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    state_dir = args.state_dir or find_default_state_dir()
    templates_dir = args.templates_dir or find_default_templates_dir(script_dir)

    result = bootstrap(state_dir, templates_dir, verbose=not args.quiet)

    if result["errors"]:
        print(f"[bootstrap] Completed with {len(result['errors'])} error(s):", file=sys.stderr)
        for err in result["errors"]:
            print(f"  - {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
