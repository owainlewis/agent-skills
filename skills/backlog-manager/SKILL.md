---
name: backlog-manager
description: "Manage a software backlog by classifying issues, applying simple risk/type/agent labels, improving issue quality, and syncing issue state with linked pull requests. Use for GitHub Issues or Linear backlog grooming before agent execution loops."
user-invocable: true
argument-hint: "<dry-run|apply> <GitHub|Linear> backlog for <repo/team/project>"
---

# Backlog Manager

Keep a software backlog clean, classified, and ready for safe agent execution.

The goal is backlog management, not implementation. This skill labels issues, improves issue
quality, creates evidence-backed maintenance tickets when asked, and syncs issue state with linked
pull requests.

Default to `dry-run`. Only mutate GitHub, Linear, or another tracker when the user explicitly asks
for `apply`.

## Labels

Use this small fixed label set. Do not invent extra labels unless the user asks.

The skill owns only the labels listed below. Existing tracker labels such as `bug`, `enhancement`,
`documentation`, `exploration`, `good first issue`, or team-specific labels should be left alone
unless the user explicitly asks to normalize or remove legacy labels.

### Risk

- `risk:low` - Safe for agent execution when the issue is also `agent:ready`.
- `risk:medium` - Possibly agent-suitable later, but do not execute unattended by default.
- `risk:high` - Human-led. Agents may investigate or plan, but should not execute unattended.

### Type

- `type:bug` - Incorrect behavior or regression.
- `type:feature` - New user-facing or developer-facing capability.
- `type:docs` - Documentation, examples, README, comments, broken links, or written guidance.
- `type:test` - Test additions, test fixes, coverage, fixtures, or test reliability.
- `type:refactor` - Internal restructuring without intended behavior change.
- `type:chore` - Maintenance such as dependency upgrades, build scripts, CI config, formatting,
  package metadata, repo cleanup, or tool configuration.

### Agent Routing

- `agent:ready` - Permission for an execution loop to pick up the issue.
- `agent:blocked` - The agent cannot safely classify or progress the issue.
- `agent:complete` - Agent work produced the needed PR or the issue has been resolved.

### Human Input

- `needs:human` - A human decision, clarification, or judgement call is required.

## Risk Rules

Use `risk:low` for small, bounded changes with clear verification and low blast radius.

Good low-risk examples:
- docs updates
- broken links
- stale README commands
- simple test additions
- lint or formatting fixes
- small repo chores
- simple CI command/config drift
- patch dependency upgrades with passing tests

Only mark an issue `risk:low` when:
- scope is clear
- acceptance criteria can be inferred or written plainly
- likely change is small
- verification is available
- no product, security, data, billing, auth, or deployment decision is required

Use `risk:medium` when the change may be agent-suitable but needs more confidence, stronger tests,
or human review.

Medium-risk examples:
- user-facing bug fixes
- behavior changes with clear expected output
- multi-file refactors
- minor or major dependency upgrades
- framework/tooling migrations
- changes touching build or runtime behavior

Do not mark medium-risk issues `agent:ready` unless the user explicitly asks this workflow to
include medium-risk work.

Use `risk:high` when unattended execution could create meaningful product, security, operational,
or data risk.

High-risk examples:
- auth, permissions, secrets, or security-sensitive code
- billing, payments, subscriptions, or pricing
- data migrations or destructive data changes
- production deployment logic or infrastructure that can affect live systems
- vague feature requests
- broad architecture changes
- anything requiring product judgement

Add `needs:human` to high-risk issues unless they are already clearly human-owned.

## Agent Readiness

Only add `agent:ready` when all are true:
- risk is `risk:low`
- no human decision is needed
- the issue is small enough for one pull request
- the expected output is clear
- the likely verification step is known
- the issue is not already linked to an active PR

Add `needs:human` when:
- requirements are ambiguous
- expected behavior is unclear
- a reproduction is missing for a real bug
- the issue asks for a product, UX, architecture, security, data, or deployment decision
- the issue looks too large for one pull request

Add `agent:blocked` when:
- the tracker cannot be updated safely
- labels cannot be applied
- the issue cannot be classified with confidence
- a previous agent attempt failed and the next step is unclear

## Agent Assessment

Put reasoning in the issue body or a comment instead of creating more labels.

Add or update this block:

```md
## Agent Assessment

Risk: low | medium | high
Type: bug | feature | docs | test | refactor | chore
Agent-ready: yes | no

Reason:
<1-3 sentences explaining the classification.>

Suggested plan:
1. <small first step>
2. <small second step>
3. <verification step>
```

If human input is needed, include:

```md
Human needed:
<specific question or decision required before an agent can execute.>
```

## Workflow

### 1. Load Context

Read repository or workspace instructions first:
- `AGENTS.md`
- `CLAUDE.md`
- README files
- contribution/development docs
- issue templates

Use this context to classify risk and write issue assessments. Do not make up project policy.

### 2. Detect Tracker

Use the tracker the user names.

Otherwise:
- Use GitHub when `gh` is available and the current directory has a GitHub remote.
- Use Linear when the user asks for Linear and a Linear connector/tool is available.
- If no tracker can be accessed, stop with the exact missing setup.

### 3. Ensure Labels Exist

In `dry-run`, report missing labels.

In `apply`, create missing labels where the tracker supports it.

Recommended GitHub colors:
- `risk:low` - `0E8A16`
- `risk:medium` - `FBCA04`
- `risk:high` - `B60205`
- `type:*` - `5319E7`
- `agent:*` - `1D76DB`
- `needs:human` - `D93F0B`

### 4. Fetch Open Issues

Fetch open issues with title, body, labels, comments, status/project fields when available, and
linked pull requests when the tracker exposes them.

For GitHub, prefer `gh`. Use GraphQL when linked PR state matters.

### 5. Classify And Tidy Issues

For each open issue:
1. Assign exactly one managed `risk:*` label.
2. Assign exactly one managed `type:*` label.
3. Decide whether `agent:ready`, `agent:blocked`, `agent:complete`, or `needs:human` should change.
4. Add or update the Agent Assessment.
5. Avoid changing labels when confidence is low. Use `needs:human` and explain why.

### 6. Create Obvious Maintenance Issues

Only scan the repo and create new issues when the user asks for repo scanning.

Create a new issue only when there is concrete evidence of a real problem. If the concern is
plausible but not proven, mention it in the run report instead of creating a ticket.

Good candidates:
- broken docs links
- stale commands in README or setup docs
- TODO comments that describe clear work
- missing tests around small utility code
- simple CI/build script drift
- dependency upgrades that are clearly routine

Bad candidates:
- vague improvement ideas
- speculative refactors
- architecture rewrites
- product ideas
- anything requiring business, UX, security, data, or deployment judgement

Deduplicate before creating an issue.

Every agent-created issue must include:
- evidence, including file paths, commands, config keys, or code references
- why the problem matters
- a small suggested fix
- an Agent Assessment

Use this shape:

```md
## Evidence

- File: <path>
- Current state: <specific text, command, config, or code reference>
- Problem: <why this is wrong, stale, broken, or risky>

## Suggested fix

<small fix another agent or human can review>

## Agent Assessment

Risk: low | medium | high
Type: bug | feature | docs | test | refactor | chore
Agent-ready: yes | no
```

### 7. Sync Issue State With Pull Requests

Keep issue state aligned with linked PRs.

If a linked PR is open:
- move the issue to the tracker review state when status/project fields are available
- do not add `agent:complete` unless the workflow defines PR-open as complete

If a linked PR is merged:
- remove `agent:ready`
- add `agent:complete`
- close the issue when the PR clearly resolves it

If a linked PR is closed without merge:
- remove `agent:complete`
- add `agent:blocked`
- comment with the known reason when available

Do not close an issue unless the linked PR clearly resolves it.

### 8. Report

End with a compact summary:
- tracker used
- mode used
- number of issues inspected
- labels created or missing
- issues changed
- issues marked `agent:ready`
- issues marked `needs:human`
- issues closed or synced from PR state
- blockers and recommended next action

## GitHub Adapter

Use `gh` when available.

Useful commands:

```bash
gh repo view --json nameWithOwner,url
gh label list --limit 200
gh label create "risk:low" --color "0E8A16" --description "Low-risk issue suitable for agent execution when agent-ready"
gh issue list --state open --limit 100 --json number,title,body,labels,url,createdAt,updatedAt,comments
gh issue edit <number> --add-label "risk:low,type:docs,agent:ready"
gh issue comment <number> --body-file <file>
gh issue close <number> --comment "Closed because linked PR <url> was merged."
```

For linked PRs, use GraphQL or `gh pr list`/`gh pr view` as needed. Prefer exact linked PR data over
guessing from branch names or text search.

## Linear Adapter

Use Linear when the user asks for Linear and the connector/tool is available.

Map labels directly:
- `risk:*`
- `type:*`
- `agent:*`
- `needs:human`

Map issue status to the workspace's existing workflow states. Do not create new status states unless
the user asks.

When Linear and GitHub are connected, use linked PR state to update Linear issue status and labels.

## Example Invocations

```text
$backlog-manager dry-run GitHub backlog for this repo
$backlog-manager apply GitHub backlog labels and issue assessments for owainlewis/neo
$backlog-manager dry-run Linear backlog for the Agentic Engineer project
```

## Safety Rules

- Default to `dry-run`.
- Do not mutate trackers unless the user asks for `apply`.
- Do not add `agent:ready` to high-risk issues.
- Do not auto-close issues without clear linked merged PR evidence.
- Do not create speculative work.
- Do not use the backlog manager to implement code.
- When unsure, classify conservatively and ask for human input.

## Quality Bar

- [ ] Uses the small fixed label set.
- [ ] Each classified issue has one managed risk label and one managed type label.
- [ ] `agent:ready` only appears on low-risk, clear, verifiable work.
- [ ] Human decisions are routed through `needs:human`, not extra labels.
- [ ] Issue reasoning lives in Agent Assessment, not label sprawl.
- [ ] Merged PR cleanup only happens with clear evidence.
- [ ] Final report is concise and actionable.
