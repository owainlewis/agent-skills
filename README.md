# Agent Skills

> A small library of agent skills I use day to day. Install with one command.

## Skills

| Skill | What it does |
|---|---|
| `humanizer` | Rewrites text to remove AI tells (em dashes, "Most people don't…", significance inflation, signposting, etc.) and puts a voice back in. Runs a draft → audit → final pass. |
| `clarify` | Turns a vague ask or half-formed plan into a clean, self-contained prompt you can run anywhere. Interviews you one question at a time — with a recommended answer each time — then hands back the final prompt as the deliverable. Run it now, save it, or hand it to another agent. |
| `prompt-enhance` | Takes a draft prompt or messy text and rewrites it into a refined, agent-ready prompt using prompt-engineering best practice — explicit scope, no contradictions, output contract, success criteria. One-shot: it improves the prompt, it doesn't interview you (that's `clarify`). |
| `explain-visually` | Builds a beautiful HTML explanation of a repo, spec, PR, architecture, or concept so a smart beginner can understand and retell it. |
| `compress` | Compresses agent-facing instructions to the fewest words that preserve behavior, constraints, and clarity. |
| `teaching-card` | Turns rough expertise, lesson sections, YouTube ideas, or demos into compact teaching cards that make one specific idea click. |
| `teaching-doc` | Turns cards, rough notes, demos, or existing drafts into camera-readable Markdown lessons and YouTube companion docs with diagrams, prompts, code, and exercises. |

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
/prompt-enhance make this a better prompt: <paste your rough draft>
/explain-visually this repo
/compress skills/compress/SKILL.md
/teaching-card explain git worktrees for Claude Code users
/teaching-doc turn these notes into a YouTube companion doc about my multi-agent terminal setup
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
