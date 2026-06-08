---
name: pr-review-loop
description: "Handle a GitHub pull request review loop: inspect live PR state, classify human and bot feedback, fix only still-actionable findings, verify checks, and report merge readiness with evidence."
user-invocable: true
argument-hint: "<PR URL, number, branch, or current repository PR>"
---

# PR Review Loop

Use this when the user asks whether a PR is ready, says "fix the PR", "address review comments", "do the PR loop", "merge?", "safe?", or wants human/bot review feedback resolved before merging.

The job is independent validation, not agreement. Re-read the live PR state and decide from evidence.

## Workflow

1. Identify the PR from `$ARGUMENTS`, the current branch, or the repository's open PRs.
2. Inspect live state:
   - PR title, body, base/head branches, mergeability, changed files, and latest commits
   - check runs, required statuses, and failing or pending jobs
   - review submissions, unresolved threads, top-level comments, and bot comments
   - local working tree status
3. Classify feedback before editing:
   - `actionable`: still applies and should be fixed
   - `resolved`: already fixed or answered
   - `outdated`: attached to old code or obsolete context
   - `informational`: useful but not required for merge
   - `needs-human`: requires product, security, ownership, or risk acceptance
4. Patch only actionable findings. Keep changes narrow and consistent with the repo.
5. Run the smallest verification that proves the fixes, then broader tests when shared behavior, public APIs, security, or user-visible flows changed.
6. Re-check live PR state after pushing or after local fixes if not pushing.
7. Report merge readiness with evidence.

## Rules

- Do not rely on stale chat summaries. Inspect the PR again.
- Do not treat a resolved or outdated bot comment as current work.
- Do not mark a PR ready while required checks are failing or pending.
- Do not broaden scope because a bot suggested a nice-to-have refactor.
- Do not hide placeholders, skipped tests, partial fixes, or assumptions.
- Stop for human input if a finding requires authority the agent does not have.
- If you cannot access GitHub, say so and fall back to local branch, diff, and test evidence only.

## Report

Lead with the decision:

- `Ready`: all actionable feedback is resolved and required checks pass.
- `Not ready`: blockers remain.
- `Blocked`: missing access, missing environment, or human decision required.

Then include:

- PR inspected: number or URL
- Live state checked: reviews, threads/comments, checks, mergeability, working tree
- Changes made: concise bullets with files or areas
- Verification: commands run and results
- Remaining items: blockers, pending checks, human decisions, or risks

## Merge answer

When the user asks "merge?", answer directly:

- "Ready to merge" only when live evidence supports it.
- "Not yet" when checks are pending/failing, actionable feedback remains, or the fix is only partially verified.
- "I can't validate merge readiness" when GitHub state or required environment is unavailable.
