# Agent Skills for Claude Code

The exact Claude Code skills I use to create content for my business. Customizable for your voice, your audience, your links.

These are not toy prompts. Each skill includes real examples with annotations explaining why they work, proven hook patterns, writing frameworks, and quality constraints that make Claude produce genuinely good content.

## Skills

| Skill | What it does |
|-------|-------------|
| **linkedin-post** | Two-phase LinkedIn post writer. Generates hook options first, waits for your pick, then writes the full post with strategy, structure, and a CTA. |
| **substack-notes** | Short-form note writer. Follows a specific pattern: observation, friction, reframe. Under 150 words that land. |

## Quick Start

```bash
git clone https://github.com/owainlewis/agent-skills.git
cd agent-skills
./install.sh
```

Then customize:

1. Open `skills/linkedin-post/SKILL.md` and `skills/substack-notes/SKILL.md`
2. Replace `[YOUR NAME]`, `[YOUR TOPIC]`, `[YOUR URL]` placeholders with your details
3. Add your own best-performing posts to the Examples sections

Use in Claude Code:

```
/linkedin-post Why most AI agents never make it to production
/substack-notes The gap between building a demo and shipping to production
```

## How It Works

Each skill is a folder in `skills/` containing a single `SKILL.md` file. The install script symlinks these into `~/.claude/skills/` where Claude Code auto-discovers them.

The SKILL.md format:

```markdown
---
name: skill-name
description: "When to trigger this skill"
---

# Skill instructions, examples, and constraints go here
```

## Customization

Look for `<!-- CUSTOMIZE -->` comments and `[PLACEHOLDER]` markers in each SKILL.md. The main things to personalize:

- **CTAs** - your YouTube, newsletter, community links
- **Examples** - add your own best-performing posts (keep the "WHY THIS WORKS" annotations)
- **Name** - replace `[YOUR NAME]` with yours
- **Content buckets** - the linkedin-post skill works with any topic area

## Testing

Generate sample outputs to check skill quality:

```bash
./test.sh
```

This runs each skill with a sample topic and saves the output to `examples/`. Review manually to verify quality after making changes.

## Adding Your Own Skills

Create a new folder in `skills/` with a `SKILL.md` file following the frontmatter format above, then run `./install.sh` again.

## Structure

```
agent-skills/
  install.sh                    # Installs skills to ~/.claude/skills/
  test.sh                       # Generates sample outputs
  skills/
    linkedin-post/SKILL.md      # LinkedIn post writer
    substack-notes/SKILL.md     # Substack note writer
  examples/                     # Generated sample outputs (gitignored)
```

## Requirements

- [Claude Code](https://claude.ai/code) (requires Claude Pro, Max, or Team subscription)
