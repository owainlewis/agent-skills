# Agent Skills

> A small library of agent skills I use day to day. Install with one command.

## Skills

| Skill | What it does |
|---|---|
| `humanizer` | Rewrites text to remove AI tells (em dashes, "Most people don't…", significance inflation, signposting, etc.) and puts a voice back in. Runs a draft → audit → final pass. |
| `clarify` | Turns a vague ask or half-formed plan into a clean, self-contained prompt you can run anywhere. Interviews you one question at a time — with a recommended answer each time — then hands back the final prompt as the deliverable. Run it now, save it, or hand it to another agent. |
| `prompt-enhance` | Takes a draft prompt or messy text and rewrites it into a refined, agent-ready prompt using prompt-engineering best practice — explicit scope, no contradictions, output contract, success criteria. One-shot: it improves the prompt, it doesn't interview you (that's `clarify`). |
| `pr-review-loop` | Handles the GitHub PR review loop: re-reads live PR state, classifies human and bot feedback, fixes still-actionable findings, verifies checks, and reports merge readiness with evidence. |
| `backlog-manager` | Keeps a GitHub Issues or Linear backlog tidy: classifies risk/type, marks agent-ready work, adds issue assessments, and syncs issue state with linked PRs. |
| `task-to-pr` | Turns explicit ticket references into draft PRs by running the full developer loop: fetch the ticket, write code, add tests, review with subagents, fix issues, and open a PR. |
| `explain-visually` | Builds a beautiful HTML explanation of a repo, spec, PR, architecture, or concept so a smart beginner can understand and retell it. |
| `compress` | Compresses agent-facing instructions to the fewest words that preserve behavior, constraints, and clarity. |
| `feynman` | Writes a clear, well-structured explanation of a technical topic. Works as a course lesson, a reference for recording a YouTube video, or the basis for a newsletter. |

## Install

```bash
npx skills@latest add owainlewis/agent-skills
```

Installs the skills into your agent (Claude Code, Codex, Cursor, and others supported by the [`skills`](https://www.npmjs.com/package/skills) CLI). Invoke by name (`explain-visually`, `compress`) or via your agent's skill picker.

## Update

```bash
npx skills@latest update
```

## Use

In Claude Code:

```
/humanizer paste or path the text you want rewritten
/clarify build a thing that does X and also Y, you know
/prompt-enhance make this a better prompt: <paste your rough draft>
/pr-review-loop https://github.com/owner/repo/pull/123
/backlog-manager dry-run GitHub backlog for this repo
/task-to-pr JIRA-123
/task-to-pr LIN-123
/task-to-pr https://github.com/owner/repo/issues/456
/explain-visually this repo
/compress skills/compress/SKILL.md
/feynman agent memory
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

Fork the repo and point `npx skills@latest add` at your fork to install your own set.

## Requirements

- [Claude Code](https://claude.ai/code), or another agent supported by the [`skills`](https://www.npmjs.com/package/skills) CLI.

## Credits

The `humanizer` pattern catalogue is adapted from [blader/humanizer](https://github.com/blader/humanizer), which builds on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) maintained by WikiProject AI Cleanup.
