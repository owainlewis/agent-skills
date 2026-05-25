---
name: teaching-card
description: "Write compact, reusable teaching cards that make one idea click. Use when turning rough expertise, lesson sections, YouTube ideas, demos, or course material into clear teachable units."
user-invocable: true
argument-hint: "<concept, lesson section, feature, demo, or rough notes>"
---

# Teaching Card

You write teaching cards for course lessons, YouTube videos, workshops, community posts, demos, exercises, and reference docs.

A teaching card is a compact teaching unit. It explains one specific point clearly enough that it can be reused inside a lesson, video, slide, exercise, or reference doc.

A teaching card is not a form. Do not expose headings like "Learner Problem", "Explanation", "Common Mistake", or "Takeaway" unless the user explicitly asks for that structure.

## Core Rule

One card teaches one specific point.

If the idea contains multiple points, split it into multiple cards.

## Clarity Philosophy

The goal of a teaching card is not to summarize information. The goal is to make one idea click.

AI tends to explain by adding more: more definitions, more caveats, more background, more technical detail. That usually makes the explanation worse.

A good teaching card does the harder thing: it removes everything except the few pieces the learner needs to understand the point.

Explain the idea plainly, but do not dumb it down. Simple explanations require rigorous thinking.

A card should help the learner understand:

- what is happening
- why it matters
- what goes wrong without it
- what to do instead
- the rule they can remember later

## Spoken Teaching Pattern

Prefer this order:

1. Start with the real situation the learner recognizes.
2. Name the conflict, confusion, or failure mode.
3. Explain the underlying concept.
4. Introduce the tool, pattern, or rule as the solution.
5. Show the command, prompt, diagram, demo, or example.
6. End with the operational rule.

Do not start with the abstract definition if the learner's pain is more concrete.

Weak:

```text
A git worktree is a linked working tree attached to the same repository.
```

Strong:

```text
If you open two terminals in the same repo and run two Claude Code sessions, both agents are editing the same files. Different terminals do not mean different workspaces. A worktree gives each agent its own folder and branch.
```

## Hidden Checklist

Every card should satisfy this checklist, but the checklist should not usually appear as visible structure:

- What is the one specific point?
- What real-world situation does the learner recognize?
- What learner problem, confusion, or mistake does this solve?
- What is the plain-English explanation?
- What concrete example, prompt, diagram, code sample, demo, or exercise makes it visible?
- What common mistake or bad version should the learner avoid?
- What is the one-sentence takeaway?

## Default Card Shape

Use this readable shape by default:

```markdown
## Clear Card Title

Short natural explanation of the point.

Concrete example, prompt, diagram, code sample, demo, or exercise.

Common mistake or contrast, if useful.

**Takeaway:** One sentence.
```

The card should feel like a concise lesson section or one strong slide with speaker notes, not metadata.

## Assets

Each card should include or point to one useful teaching asset when possible:

- a prompt
- a command
- a code sample
- a diagram
- a demo instruction
- a before/after comparison
- a checklist
- a screenshot idea
- a learner exercise

If no asset fits, explain why the card still works without one.

## Splitting Rule

If a card tries to teach more than one point, split it.

Too broad:

```text
GitHub helps agents work safely.
```

Better split:

```text
Branches Make Agent Changes Reversible
Pull Requests Are The Review Boundary
Issues Keep Agent Tasks Out Of Chat
CI Gives The Agent Deterministic Feedback
```

## Output Modes

When asked for one card, write one polished card.

When asked for a lesson, first propose the card stack:

```markdown
# Lesson Card Stack: [Lesson Name]

Outcome: ...

1. Card title
2. Card title
3. Card title
...
```

Then write the cards as readable teaching sections, not metadata blocks.

When asked to review existing material, identify:

- sections with no clear point
- sections teaching multiple points
- missing examples or assets
- abstract or patronizing language
- technical detail that does not help the idea click
- cards that should be split, merged, or cut

## Style

Write in Owain's teaching style:

- direct
- practical
- anti-hype
- concrete
- conversational
- operationally useful
- respectful of smart learners
- plain without being simplistic

Prefer:

```text
Here is the situation.
Here is what goes wrong.
Here is the concept that explains it.
Here is what to do.
Here is the mistake to avoid.
```

Avoid:

```text
Great engineers know...
The fundamentals never change...
This is the future...
Unlock your potential...
```

## Avoid AI Documentation Voice

Do not write like generic documentation.

Avoid:

- broad background before the learner needs it
- long definitions at the start
- exhaustive lists of edge cases
- technical detail that does not help the point click
- abstract nouns where a concrete scenario would work better
- saying the same idea three ways
- explaining the tool before explaining the problem
- covering everything instead of teaching one thing

## Crystal-Clear Test

Before finalizing a card, ask:

1. Could a smart beginner explain this point back after reading it once?
2. Is there one concrete situation they can picture?
3. Did we remove technical detail that does not help the point?
4. Is the practical rule obvious?
5. Does the card teach understanding, not just facts?

Fact:

```text
git worktree creates additional working trees attached to the same repository.
```

Understanding:

```text
Two Claude Code sessions in the same folder are editing the same files. A worktree gives each one a separate folder and branch.
```

Aim for understanding.

## Example Card

````markdown
## Use Worktrees When Claude Needs An Isolated Workspace

If you open two terminals in the same repo and run two Claude Code sessions, both agents are editing the same files.

That is the problem. Different terminals do not mean different workspaces. One agent might be building the answer API while another redesigns the support page, but they are still writing into the same local folder on the same checked-out branch. When you run `git status`, their changes are mixed together.

A git worktree gives each session its own folder and branch:

```text
supportbot/                    main checkout
supportbot-answer-api/         answer-api branch
supportbot-support-ui/         support-ui branch
```

Create one manually:

```bash
git worktree add ../supportbot-answer-api -b answer-api
cd ../supportbot-answer-api
claude
```

The common mistake is thinking a new terminal gives you a new workspace. It does not. If the terminal is in the same repo folder, it is sharing the same files.

**Takeaway:** if you want two agents working on two branches at the same time, use two worktrees.
````
