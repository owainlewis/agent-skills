---
name: backlog-manager
description: "Manage an engineering backlog for humans and AI agents: classify issues, improve issue quality, sync PR state, and label safe tickets for agent execution. Use when GitHub Issues, GitHub Projects, Linear, or an explicit local backlog path is the source of truth."
user-invocable: true
argument-hint: "<dry-run|apply> backlog for <GitHub repo|GitHub Project URL|Linear board|local path>"
---

# Backlog Manager

Manage one backlog source of truth.
Default to `dry-run`.
Mutate trackers only when the user asks for `apply`.
When unattended, never wait for input; report blockers and exit.

Labels answer who may pick up work.
Statuses answer workflow state.
Use tracker status fields when available.

## Source Contract

Use exactly one source per run:

- GitHub Issues for a named repo when `gh` is installed and authenticated.
- GitHub Projects when the user provides a project URL/path and `gh` can access it.
- Linear when the user provides a team/project/board path and a Linear connector is available.
- Local backlog file only when the user provides the path and says it is the source of truth.

Default to GitHub Issues when the current repo has a GitHub remote and authenticated `gh`.
If no source can be resolved, ask for a backlog path/URL or missing setup.
Treat roadmap files, ticket files, planning docs, and README sections as context unless explicitly chosen as the source.

## Managed Labels

Do not invent labels unless asked.
Leave non-managed labels alone.
Do not remove or downgrade existing managed labels during classification.
Exception: PR sync may remove `agent:ready` when work is in progress or done.
If classification disagrees with an existing managed label, keep the label and report the disagreement.

Risk:

- `risk:low`: safe for agent execution when also `agent:ready`.
- `risk:medium`: may become agent-suitable later; no unattended execution by default.
- `risk:high`: human-led; agents may investigate or plan only.

Type:

- `type:bug`: incorrect behavior or regression.
- `type:feature`: new user-facing or developer-facing capability.
- `type:docs`: docs, examples, README, comments, links, or written guidance.
- `type:test`: test additions, fixes, coverage, fixtures, or reliability.
- `type:refactor`: internal restructuring without intended behavior change.
- `type:chore`: dependencies, build scripts, CI, formatting, metadata, repo cleanup, or tooling.

Routing:

- `agent:ready`: permission for an agent execution loop to pick up the issue.
- `needs:human`: human decision, clarification, or judgement required.

Do not create completion labels such as `agent:complete` or `agent:blocked` unless repo docs define them or the user asks.

## Routing Rules

Add `agent:ready` only when all are true:

- `risk:low`
- scope is clear
- one-PR size
- expected output is clear
- verification is known
- no product, UX, architecture, security, data, billing, auth, or deployment judgement
- no active linked work

Good low-risk examples:

- docs updates
- broken links
- stale README commands
- simple test additions
- lint or formatting fixes
- small repo chores
- simple CI command/config drift
- patch dependency upgrades with passing tests

Add `needs:human` when any are true:

- requirements or expected behavior are unclear
- reproduction is missing for a real bug
- issue is too large for one PR
- product, UX, architecture, security, data, billing, auth, or deployment judgement is needed
- classification confidence is low
- previous agent attempt failed and next step is unclear

Risk:

- `risk:low`: small, bounded, clear verification, low blast radius.
- `risk:medium`: may be agent-suitable later; needs more confidence, tests, or close review.
- `risk:high`: unattended execution could create product, security, operational, or data risk; add `needs:human` unless human-owned.

## Agent Assessment

Put reasoning in the issue body or a comment.
Update only when classification, reasoning, or plan changes.

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

If input is needed:

```md
Human needed:
<specific question or decision.>
```

## Workflow

### 1. Load Context

Read:

- `AGENTS.md`
- `CLAUDE.md`
- README files
- contribution/development docs
- issue templates
- local roadmap/backlog docs as context only

Use context for risk and assessments.
Do not invent project policy.
Report drift between docs and tracker state.

### 2. Resolve Source

Use the user-named source.
Otherwise use GitHub Issues only when `gh` is installed, authenticated, and the current directory has a GitHub remote.
Do not infer Linear, GitHub Projects, or local backlogs from vague references.

For GitHub Projects, load fields and status option IDs before mutating.
Map existing status options, commonly:

- `Todo`: open unstarted issues.
- `In Progress`: owned issue or active branch.
- `In Review`: open PR ready for review.
- `Done`: closed by merged PR.

Do not create project fields or statuses unless asked.

### 3. Ensure Labels

In `dry-run`, report missing labels.
In `apply`, create missing labels when supported.

GitHub colors:

- `risk:low`: `0E8A16`
- `risk:medium`: `FBCA04`
- `risk:high`: `B60205`
- `type:*`: `5319E7`
- `agent:*`: `1D76DB`
- `needs:human`: `D93F0B`

### 4. Classify Open Issues

Fetch title, body, labels, comments, status/project fields, and linked PRs.

For each open issue:

1. Add one `risk:*` label only if missing.
2. Add one `type:*` label only if missing.
3. If no routing label exists, add `agent:ready`, `needs:human`, or neither.
4. Keep existing managed labels; report disagreements.
5. Add/update Agent Assessment only when changed.
6. Use `needs:human` when confidence is low.

Do not mark medium/high risk issues `agent:ready` unless the user asks for that policy.

### 5. Sync Issue State With PRs

If linked PR is open:

- move issue to review state when status fields exist
- remove `agent:ready`
- comment only when adding missing PR link or verification summary

If linked PR is merged:

- remove `agent:ready`
- close the issue only when the PR clearly resolves it
- move project item to done when status fields exist
- keep audit labels and assessments

If linked PR is closed unmerged:

- remove `agent:ready`
- add `needs:human` when next step is unclear
- comment with known reason when available
- move status back only when tracker policy is clear

Do not infer completion from PR title or branch.
Check draft flag, mergeability, checks, review submissions, and unresolved threads.
Verify issue state and project item state agree after sync.

### 6. Sweep For Quality Drift

Run on full backlog reviews.
Create/propose tickets only for concrete evidence:

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

### 7. Create Candidate Issues

In `dry-run`, output candidates only:

```md
Candidate issue: <title>
Evidence:
- <file, command, PR, issue, or code reference>
Why it matters:
<short explanation>
Suggested fix:
<small reviewable fix>
Risk: low | medium | high
Type: bug | feature | docs | test | refactor | chore
Agent-ready: yes | no
Confidence: high | medium | low
Create issue: yes | no
```

In `apply`, create a new issue only with concrete evidence and high confidence.
Every created issue must include evidence, why it matters, suggested fix, and Agent Assessment.

### 8. Report Branch Cleanup Candidates

Report branches that are:

- merged into the default branch
- linked to closed issues or merged/closed PRs with no remaining work
- stale automation branches whose PR closed unmerged with no follow-up

Never delete branches from this skill.

### 9. Verify Apply Runs

After `apply`, verify:

- open issues have one managed `risk:*` and one managed `type:*`
- `agent:ready` without `risk:low`, or with `needs:human`, is flagged
- `risk:high` has `needs:human` unless a reason is recorded
- classified open issues have Agent Assessment
- sweep-created issues are deduplicated and evidence-backed
- open linked PRs map to review state when available
- merged linked PRs map to done state when available
- no closed issue remains active unless reported as tracker limitation or failed API update

For GitHub, prefer `gh issue list --json number,title,labels,body` over web UI checks.

### 10. Report

Include:

- tracker and mode
- steps run
- issues inspected
- labels created or missing
- issues changed
- `agent:ready` count
- `needs:human` count
- issues closed or synced from PR state
- sweep candidates found or created
- branch cleanup candidates
- verification result
- blockers and next action

## Scheduled Runs

Run the full loop: review backlog, label tickets, find drift, create/propose issues, sync ticket state, close completed tickets, report branch cleanup candidates, verify, report.

Cron prompts must include:

- repo/tracker
- source-of-truth rule
- allowed mutation policy
- create issues or propose only
- verification requirements
- delivery target

Default scheduled behavior must not merge PRs, publish releases, change secrets, spend money, delete branches, or make high-risk changes.

For GitHub Actions, copy this skill to `.claude/skills/backlog-manager/SKILL.md` and invoke with explicit mode.
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
$backlog-manager dry-run GitHub backlog for this repo
$backlog-manager apply full backlog loop for GitHub repo owainlewis/neo
$backlog-manager dry-run backlog for GitHub Project https://github.com/orgs/acme/projects/7
$backlog-manager dry-run Linear backlog for team ENG project Agentic Engineer
$backlog-manager dry-run backlog from ./BACKLOG.md as the source of truth
```

## Safety

- Default to `dry-run`.
- Mutate trackers only with `apply`.
- Never remove or downgrade existing managed labels during classification.
- PR sync may remove `agent:ready`.
- Do not add `agent:ready` to high-risk issues.
- Do not auto-close issues without linked merged PR evidence.
- Do not mark done while linked PR checks fail, are pending, or unresolved review threads remain actionable.
- Do not create speculative work.
- Do not implement code.
- Do not delete branches.
- When unsure, classify conservatively and add `needs:human`.

## Quality Bar

- Fixed label set used.
- Existing managed labels respected.
- Each classified issue has one risk and one type.
- `agent:ready` only on low-risk, clear, verifiable work.
- Human decisions routed through `needs:human`.
- Reasoning lives in Agent Assessment.
- Merged PR cleanup has evidence.
- Branch cleanup is report-only.
- Final report includes verification and next action.
