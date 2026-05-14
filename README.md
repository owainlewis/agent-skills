# Agent Skills

> A small library of agent skills I use day to day. Install with one command.

## Skills

| Skill | What it does |
|---|---|
| `humanizer` | Rewrites text to remove AI tells (em dashes, "Most people don't…", significance inflation, signposting, etc.) and puts a voice back in. Runs a draft → audit → final pass. |
| `clarify` | Turns a vague ask or half-formed plan into an unambiguous spec. Rewrites the ask if it's noisy, then interviews you one question at a time — with a recommended answer each time — until the intent is tight enough to execute. Stops you from shipping the wrong thing on a vague brief. |
| `explain-visually` | Builds a beautiful HTML explanation of a repo, spec, PR, architecture, or concept so a smart beginner can understand and retell it. |
| `compress` | Compresses agent-facing instructions to the fewest words that preserve behavior, constraints, and clarity. |

## Install

```bash
npx skills add owainlewis/agent-skills
```

Installs the skills into your agent (Claude Code, Codex, Cursor, and others supported by the [`skills`](https://www.npmjs.com/package/skills) CLI). Invoke by name (`explain-visually`, `compress`) or via your agent's skill picker.

## Update

```bash
npx skills update
```

## Use

In Claude Code:

```
/humanizer paste or path the text you want rewritten
/clarify build a thing that does X and also Y, you know
/explain-visually this repo
/compress skills/compress/SKILL.md
```

## Add your own skills

Create a folder in `skills/` with a `SKILL.md`:

```markdown
---
name: skill-name
description: "When to trigger this skill"
---

# Skill instructions
```

Fork the repo and point `npx skills add` at your fork to install your own set.

## Requirements

- [Claude Code](https://claude.ai/code), or another agent supported by the [`skills`](https://www.npmjs.com/package/skills) CLI.
