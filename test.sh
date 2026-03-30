#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
EXAMPLES_DIR="$REPO_DIR/examples"

mkdir -p "$EXAMPLES_DIR"

echo "Generating sample outputs for each skill..."
echo ""

# LinkedIn Post
echo "--- linkedin-post ---"
claude -p --skill linkedin-post "Write a LinkedIn post about: Why most AI agents never make it to production" \
  > "$EXAMPLES_DIR/linkedin-post.md" 2>/dev/null
echo "  Saved to examples/linkedin-post.md"

# Substack Notes
echo "--- substack-notes ---"
claude -p --skill substack-notes "Write a Substack note about: The gap between demo and production in AI" \
  > "$EXAMPLES_DIR/substack-notes.md" 2>/dev/null
echo "  Saved to examples/substack-notes.md"

echo ""
echo "Done. Review the outputs in examples/ to check quality."
