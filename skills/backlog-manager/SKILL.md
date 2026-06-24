---
name: backlog-manager
description: "Manage an engineering backlog for humans and AI agents: classify issues, improve issue quality, sync PR state, and label safe tickets for agent execution. Use when GitHub Issues, GitHub Projects, Linear, or an explicit local backlog path is the source of truth."
user-invocable: true
argument-hint: "<GitHub repo|GitHub Project URL|Linear board|local path>"
---

# Backlog Manager

Manage one backlog source of truth.
Classify issues, sync PR state, create evidence-backed maintenance issues, and report what changed.

Do not implement code.
Do not delete branches.
Do not invent tracker labels, statuses, or project policy.
When unattended, never wait for input; report blockers and exit.

## Sources

Use one source per run:

- GitHub Issues: named repo, or current repo when it has a GitHub remote and authenticated `gh`.
- GitHub Projects: user-provided project URL/path and `gh` access.
- Linear: user-provided team/project/board and available Linear connector.
- Local backlog file: only when the user names the path as source of truth.

Treat roadmap files, planning docs, README sections, and local ticket files as context unless explicitly chosen as the source.
Report drift between docs and tracker state.

## Labels

Use only this managed label set.
Leave all other labels alone.
Never remove or downgrade managed labels during classification.
PR sync may remove `agent:ready` when work is in progress or done.
If classification disagrees with an existing managed label, keep the label and report the disagreement.

Risk:

- `risk:low`: safe for agent execution when also `agent:ready`.
- `risk:medium`: may become agent-suitable later; no unattended execution.
- `risk:high`: human-led; agents may investigate or plan only.

Type:

- `type:bug`: incorrect behavior or regression.
- `type:feature`: new user-facing or developer-facing capability.
- `type:docs`: docs, examples, README, comments, links, written guidance.
- `type:test`: tests, coverage, fixtures, reliability.
- `type:refactor`: internal restructuring without behavior change.
- `type:chore`: dependencies, build scripts, CI, formatting, metadata, repo cleanup, tooling.

Routing:

- `agent:ready`: agent execution loop may pick up the issue.
- `needs:human`: human decision, clarification, or judgement required.

Do not create completion labels such as `agent:complete` or `agent:blocked` unless repo docs define them or the user asks.

## Routing

Add `agent:ready` only when all are true:

- `risk:low`
- scope is clear
- one-PR size
- expected output is clear
- verification is known
- no active linked work
- no product, UX, architecture, security, data, billing, auth, or deployment judgement

Good `agent:ready` work:

- docs updates
- broken links
- stale README commands
- simple tests
- lint or formatting fixes
- small repo chores
- simple CI command/config drift
- patch dependency upgrades with passing tests

Add `needs:human` when any are true:

- requirements or expected behavior are unclear
- bug lacks reproduction
- issue is too large for one PR
- product, UX, architecture, security, data, billing, auth, or deployment judgement is needed
- classification confidence is low
- previous agent attempt failed and next step is unclear

## Agent Assessment

Add/update only when classification, reasoning, or plan changed.

```md
## Agent Assessment

Risk: low | medium | high
Type: bug | feature | docs | test | refactor | chore
Agent-ready: yes | no

Reason:
<1-3 sentences.>

Suggested plan:
1. <small first step>
2. <small second step>
3. <verification step>
```

If human input is needed:

```md
Human needed:
<specific question or decision.>
```

## Workflow

### 1. Load Context And Source

Read repo instructions, README, contribution docs, issue templates, and local roadmap/backlog docs as context.
Resolve the single backlog source.
Stop if the source or required access is missing.

For GitHub Projects, load fields and status option IDs before edits.
Use existing status names.
Common mapping:

- `Todo`: open unstarted issue.
- `In Progress`: owned issue or active branch.
- `In Review`: open PR ready for review.
- `Done`: closed by merged PR.

Do not create project fields or statuses unless asked.

### 2. Ensure Labels

Create missing managed labels when supported.
If unavailable, report missing labels and continue.

GitHub colors:

- `risk:low`: `0E8A16`
- `risk:medium`: `FBCA04`
- `risk:high`: `B60205`
- `type:*`: `5319E7`
- `agent:*`: `1D76DB`
- `needs:human`: `D93F0B`

### 3. Classify Open Issues

Fetch title, body, labels, comments, status/project fields, and linked PRs.

For each open issue:

1. Add one `risk:*` if missing.
2. Add one `type:*` if missing.
3. If no routing label exists, add `agent:ready`, `needs:human`, or neither.
4. Keep existing managed labels.
5. Report label disagreements.
6. Add/update Agent Assessment only when changed.

Do not mark medium/high risk issues `agent:ready` unless the user asks for that policy.

### 4. Sync PR State

Open linked PR:

- move issue to review state when available
- remove `agent:ready`
- comment only to add missing PR link or verification summary

Merged linked PR:

- remove `agent:ready`
- close issue only when the PR clearly resolves it
- move project item to done when available
- keep audit labels and assessments

Closed unmerged PR:

- remove `agent:ready`
- add `needs:human` when next step is unclear
- comment with known reason when available
- move status back only when tracker policy is clear

Never infer completion from PR title or branch.
Check draft flag, mergeability, checks, reviews, and unresolved threads.
Verify issue state and project item state agree after sync.

### 5. Sweep Drift And Create Issues

Create tickets only for concrete evidence:

- docs contradict tracker or code state
- local backlog/roadmap contradicts tracker
- broken Markdown links
- README/setup commands missing from scripts, CLI help, Makefile, or docs
- generated docs drift with documented check command
- bounded TODO/FIXME/HACK comments
- skipped tests or disabled checks that look accidental
- recent failed CI/check runs on default branch
- simple build/lint/config drift with clear verification

Do not create issues for speculative improvements, architecture rewrites, product ideas, or work needing business, UX, security, data, billing, auth, or deployment judgement.
Deduplicate against open and recently closed issues.

Create an issue only when evidence is concrete, confidence is high, and the fix is small.
Each created issue must include title, evidence, why it matters, suggested fix, risk, type, agent-ready status, and Agent Assessment.
Report skipped concerns with the missing condition.

### 6. Report Branch Cleanup

Report branches that are:

- merged into the default branch
- linked to closed issues or merged/closed PRs with no remaining work
- stale automation branches whose PR closed unmerged with no follow-up

Never delete branches.

### 7. Verify

Verify:

- open issues have one managed `risk:*` and one managed `type:*`
- `agent:ready` appears only with `risk:low` and not with `needs:human`
- `risk:high` has `needs:human` unless a reason is recorded
- classified open issues have Agent Assessment
- created issues are deduplicated and evidence-backed
- open linked PRs map to review state when available
- merged linked PRs map to done state when available
- no closed issue remains active unless reported as tracker limitation or failed API update

For GitHub, prefer `gh issue list --json number,title,labels,body` over web UI checks.

### 8. Report

Include:

- tracker
- steps run
- issues inspected
- labels created or missing
- issues changed
- `agent:ready` count
- `needs:human` count
- issues closed or synced from PR state
- issues created or skipped from drift sweep
- branch cleanup candidates
- verification result
- blockers and next action

## Scheduled Runs

Run the same workflow.
Prompt must include repo/tracker, source-of-truth rule, issue creation rules, verification requirements, and delivery target.

Scheduled runs must not merge PRs, publish releases, change secrets, spend money, delete branches, or make high-risk changes.
For GitHub Actions, copy this skill to `.claude/skills/backlog-manager/SKILL.md`.
Default `GITHUB_TOKEN` cannot edit user-level GitHub Projects; treat project mutations as report-only.

## GitHub Adapter

Use `gh` when available.

```bash
gh repo view --json nameWithOwner,url
gh label list --limit 200
gh label create "risk:low" --color "0E8A16" --description "Low-risk issue suitable for agent execution when agent-ready"
gh issue list --state open --limit 100 --json number,title,body,labels,url,createdAt,updatedAt,comments
gh issue edit <number> --add-label "risk:low,type:docs,agent:ready"
gh issue comment <number> --body-file <file>
gh issue close <number> --comment "Closed because linked PR <url> was merged."
gh project list --owner <owner>
gh project field-list <project-number> --owner <owner> --format json
gh project item-list <project-number> --owner <owner> --limit 200 --format json
gh project item-add <project-number> --owner <owner> --url <issue-or-pr-url> --format json
gh project item-edit --id <item-id> --project-id <project-id> --field-id <status-field-id> --single-select-option-id <option-id>
```

Use GraphQL or `gh pr list`/`gh pr view` for linked PRs.
Before retrying timed-out project writes, query item state to avoid duplicate comments or project items.

## Linear Adapter

Use Linear when requested and available.
Map labels directly: `risk:*`, `type:*`, `agent:ready`, `needs:human`.
Map issue status to existing workflow states.
Do not create new Linear statuses unless asked.
Use linked PR state when Linear and GitHub are connected.

## Invocations

```text
$backlog-manager GitHub backlog for this repo
$backlog-manager full backlog loop for GitHub repo owainlewis/neo
$backlog-manager backlog for GitHub Project https://github.com/orgs/acme/projects/7
$backlog-manager Linear backlog for team ENG project Agentic Engineer
$backlog-manager backlog from ./BACKLOG.md as the source of truth
```
