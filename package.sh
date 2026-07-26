#!/usr/bin/env bash
# package.sh — Regenerate esvg-dis.skill from the current repo state.
#
# Usage:
#   bash package.sh
#
# Output:
#   esvg-dis.skill (at the repo root)
#
# What's included: exactly the files SKILL.md depends on at runtime.
# What's excluded: git metadata, build artifacts, OS junk, docs-only
#   files (README, INSTALL, CONTRIBUTING, CHANGELOG, LICENSE, roadmap,
#   architecture-decisions, glossary) — these aren't loaded by the skill.
#
# Run this after any content change to workflow/, knowledge/, prompts/,
# integration/, playbooks/, state-templates/, skill/, or examples/.
# Commit the updated esvg-dis.skill alongside the content changes.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
OUTPUT="$REPO_ROOT/esvg-dis.skill"
TMPDIR_PKG="$REPO_ROOT/.pkg_tmp"

echo "[package] Building esvg-dis.skill from $REPO_ROOT"

# Clean up any previous temp dir
rm -rf "$TMPDIR_PKG"
mkdir -p "$TMPDIR_PKG"

# Copy SKILL.md to the root of the package (not inside skill/)
cp "$REPO_ROOT/skill/SKILL.md" "$TMPDIR_PKG/SKILL.md"

# Copy the bootstrap script to scripts/ (zip layout: one level below root)
mkdir -p "$TMPDIR_PKG/scripts"
cp "$REPO_ROOT/skill/scripts/bootstrap.py" "$TMPDIR_PKG/scripts/bootstrap.py"

# Copy operational directories
for dir in workflow knowledge prompts integration playbooks state-templates examples; do
  if [ -d "$REPO_ROOT/$dir" ]; then
    cp -r "$REPO_ROOT/$dir" "$TMPDIR_PKG/$dir"
  fi
done

# Remove OS/editor junk that may have crept in
find "$TMPDIR_PKG" -name ".DS_Store" -delete
find "$TMPDIR_PKG" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find "$TMPDIR_PKG" -name "*.pyc" -delete
find "$TMPDIR_PKG" -name "*.pyo" -delete
find "$TMPDIR_PKG" -name "Thumbs.db" -delete
find "$TMPDIR_PKG" -name ".gitkeep" -delete

# Build the zip from inside the temp dir so paths inside the zip are clean
(cd "$TMPDIR_PKG" && zip -r "$OUTPUT" . -x "*.DS_Store")

# Clean up
rm -rf "$TMPDIR_PKG"

echo "[package] Done → esvg-dis.skill ($(du -h "$OUTPUT" | cut -f1))"
echo "[package] Contents:"
unzip -l "$OUTPUT"
