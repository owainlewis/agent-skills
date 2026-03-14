#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_SKILLS="$HOME/.claude/skills"

mkdir -p "$CLAUDE_SKILLS"

echo "Installing skills from $REPO_DIR"

# Remove existing symlinks that point into this repo
for link in "$CLAUDE_SKILLS"/*/; do
    [ -L "${link%/}" ] && readlink "${link%/}" | grep -q "$REPO_DIR" && rm "${link%/}"
done

# Symlink each skill
for skill in "$REPO_DIR"/skills/*/; do
    name="$(basename "$skill")"
    target="$CLAUDE_SKILLS/$name"

    if [ -e "$target" ] && [ ! -L "$target" ]; then
        echo "  SKIP $name (non-symlink already exists)"
        continue
    fi

    ln -sf "$skill" "$target"
    echo "  OK   $name"
done

echo "Done. $(ls -1d "$CLAUDE_SKILLS"/*/ 2>/dev/null | wc -l | tr -d ' ') skills installed."
