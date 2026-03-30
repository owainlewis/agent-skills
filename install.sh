#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_SKILLS="$HOME/.claude/skills"

mkdir -p "$CLAUDE_SKILLS"

echo "Installing skills from $REPO_DIR/skills/"
echo ""

# Remove existing symlinks that point into this repo
for link in "$CLAUDE_SKILLS"/*/; do
    [ -L "${link%/}" ] && readlink "${link%/}" | grep -q "$REPO_DIR" && rm "${link%/}"
done

# Symlink each skill
for skill in "$REPO_DIR"/skills/*/; do
    name="$(basename "$skill")"
    target="$CLAUDE_SKILLS/$name"

    rm -rf "$target"
    ln -sf "$skill" "$target"
    echo "  OK  $name"
done

echo ""
echo "Done. $(ls -1d "$CLAUDE_SKILLS"/*/ 2>/dev/null | wc -l | tr -d ' ') skills installed to $CLAUDE_SKILLS"
echo ""
echo "Next steps:"
echo "  1. Open the SKILL.md files and replace [YOUR NAME], [YOUR URL] etc. with your details"
echo "  2. Add your own examples to the Examples sections"
echo "  3. Use /linkedin-post or /substack-notes in Claude Code"
