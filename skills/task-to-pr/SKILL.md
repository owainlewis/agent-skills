---
name: task-to-pr
description: "Turns one or more tickets into draft PRs by running the full developer loop. Outer loop: for each ticket, prepare an isolated worktree and dispatch a worker. Inner loop: write code, add and run tests, run review subagents, open a draft PR. Use when the user asks to work through tickets, process agent-ready backlog items, run issues in parallel, or produce draft PRs for review."
user-invocable: true
argument-hint: "<issue reference, ticket list, backlog query, or parallel task set>"
---

# Task To PR

Turn tickets into draft PRs. Two loops, one skill:

- **Inner loop** (one ticket): write code, add and run tests, run subagents to review the work,
  open a draft PR.
- **Outer loop**: for each ticket, run the inner loop in its own worktree.

Use this when the user wants tickets worked through to draft PRs, especially in parallel. For one
ordinary coding task, code it directly unless the user asks for this loop.

## Outer Loop

### 1. Select Work

Read the requested tickets, source context, issue tracker context, and repo state. Classify tickets
as independent, dependent, conflicting, or unclear. Run independent tickets in parallel, run
dependent tickets in waves, sequence conflicting tickets, and stop on unclear acceptance criteria.

For dependent tickets, prefer stacked draft PRs when each ticket remains reviewable on its own. If
the tickets are really one feature or heavily overlap, ask whether to use one integration branch
and PR.

### 2. Prepare Worktrees

Inspect `git status`, current branch, remotes, and existing worktrees. For each unblocked ticket in
the current wave, derive a traceable branch name from the ticket ID and short task summary, then
create a separate worktree. Default to a sibling root such as `../<repo-name>-worktrees/<branch-name>`.

Use `git worktree add -b <branch> <path> <base>` for new branches. Reuse an existing worktree only
when it is for the same branch and clean.

For stacked PRs, base each dependent branch on its predecessor branch. For an integration PR, run
the dependent tickets sequentially in one integration worktree.

### 3. Dispatch Workers

A worker is any isolated agent context that can run the inner loop for one ticket. Use whatever the
host agent provides:

- Codex: spawn one thread per ticket.
- Claude Code: spawn one subagent per ticket, pointed at the ticket's worktree; run subagents in
  the background to parallelize a wave.
- No worker tools: run the inner loop yourself, sequentially, one ticket and worktree at a time.

Assume workers cannot be steered after launch. The packet must be self-contained: everything a
worker needs to finish, or fail cleanly, without asking questions. For an integration PR, start one
worker at a time in the integration worktree. Send each worker a compact packet:

```text
Ticket:
Source context:
Worktree:
Branch:
Base:
Acceptance criteria:
Verification:
PR target:
Pause after:
```

Each worker runs the inner loop for exactly one ticket and ends with a structured result: draft PR
URL, verification run, and review findings fixed, or the exact blocker. A worker that needs a
decision does not wait for an answer; it stops, reports the question, and the outer loop hands the
ticket off.

### 4. Hand Off Failures

When a worker gives up on a ticket, remove its `agent:ready` label, add `needs:human`, and leave an
issue comment explaining what went wrong, so the ticket lands with a human instead of being retried
on the next run.

### 5. Report

The run is complete when each selected ticket is blocked or has a draft PR. Report each ticket's
worker, worktree path, branch, commit, draft PR URL, verification, review findings fixed, and any
blocked or handed-off tickets.

## Inner Loop

Each worker owns exactly one ticket and runs these steps in its worktree.

### 1. Write Code

Make the smallest complete code change for the ticket. Use test-first work when the user asked for
it.

### 2. Add And Run Tests

Add or update tests that prove the change, then run the relevant test suite and verification
commands from the worker packet.

### 3. Review With Subagents

Request a code-review subagent when available. Fix valid findings that are in scope, rerun the
relevant checks, and stop on findings that require a human decision or source-context change.

### 4. Open A Draft PR

Stage only intended files, create one clear commit, push the branch, and open a draft PR with
available GitHub tools or `gh`. The PR body should include the ticket or source link, acceptance
criteria, verification run, review result, and anything not verified. If push or PR creation fails,
keep the branch local and report the exact missing remote, auth, command, or tool capability.

### 5. Pause

Stop at the draft PR. Do not merge, resolve GitHub review, fix CI, or start follow-up changes
unless explicitly asked.

## Rules

- The outer loop routes work; each worker runs the inner loop for one ticket.
- Use one worktree and branch per ticket, unless the user chose one integration branch.
- Parallelize only tickets that can be reviewed, merged, and reverted independently.
- Do not overwrite, discard, or stage unrelated uncommitted work.
- Do not invent issue tracker tickets or rewrite source context.
- Skip or stop dependent tickets when an earlier ticket fails or changes the source context.
- Judge review findings; do not blindly implement every comment.
- Open draft PRs only after verification ran, or clearly report what could not be verified.
- Pause at draft PRs; merging is out of scope.
