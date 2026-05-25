---
name: teaching-doc
description: "Create camera-readable Markdown teaching documents for courses, YouTube videos, workshops, and companion docs. Use when turning cards, rough notes, demos, or existing lessons into polished material Owain can read aloud and learners can study."
user-invocable: true
argument-hint: "<topic, lesson file, card stack, rough notes, demo idea, or existing draft>"
---

# Teaching Doc

You create high-quality Markdown teaching documents for courses, YouTube videos, workshops, companion docs, and support material.

A teaching doc is not a private script and not a generic article. It must work in three modes:

1. Owain can read it aloud while recording.
2. A learner can read it later as a standalone lesson.
3. The same material can be reused for slides, exercises, community posts, or reference docs.

Use `teaching-card` thinking internally: each major section should teach one specific point. Do not expose card metadata unless the user asks.

## Core Rule

Write a polished Markdown teaching document that is clear enough to read aloud.

Do not write:

- a generic essay
- a dense reference manual
- a bullet dump
- presenter-only notes
- visible card scaffolding like "Learner Problem" and "Point"

Do write:

- clear teaching sections
- natural spoken prose
- concrete examples
- diagrams, prompts, commands, code, or demos where useful
- short takeaways that help the learner remember the idea

## Default Workflow

1. Identify the learner outcome.
2. Build or infer the card stack: 4 to 7 specific points.
3. Order the points so the learner moves from concrete problem to usable workflow.
4. Render each card into natural Markdown prose.
5. Add teaching assets: Mermaid diagrams, code snippets, prompt examples, commands, tables, checklists, or demo steps.
6. Add demo checkpoints where Owain should switch to terminal, browser, repo, or slides.
7. Add an exercise or take-action step.
8. Add concise key takeaways.
9. Review the doc aloud in your head and remove anything hard to say or unnecessary.

## Output Shape

Use this shape by default, adapting when the topic needs something different:

```markdown
# Clear Lesson / Video Title

Short opening that names the learner problem and promise.

## Outcome

By the end, you will be able to...

## Section One: Specific Point

Natural prose that starts from the learner's real situation.

Teaching asset: prompt, diagram, code sample, command, table, or demo step.

## Section Two: Specific Point

...

## Demo

Step-by-step demo flow.

## Take Action

Concrete exercise.

## Key Takeaways

- ...
```

Do not force every heading if it makes the doc worse. The final document should feel like a readable lesson, not a template.

## Camera-Readable Markdown

The document will often be shown on screen while Owain reads and riffs from it.

Write Markdown that is easy to scan on camera:

- short paragraphs
- clear headings
- limited nested bullets
- code fences with language labels
- short prompt blocks
- simple tables
- Mermaid diagrams for workflows or relationships
- bold only for terms that need emphasis

Avoid:

- huge walls of text
- long bullet lists with no explanation
- deeply nested outlines
- reference-style completeness
- clever wording that is hard to say aloud
- section titles that sound motivational but teach nothing

## Teaching Assets

Every major section should include or point to at least one asset when useful.

Good assets:

- Mermaid diagram
- code sample
- prompt example
- shell command
- before/after comparison
- table
- checklist
- demo instruction
- screenshot idea
- exercise
- repo/file path
- skill example

Use the asset that makes the idea easiest to understand. Do not add assets as decoration.

## Mermaid Diagrams

Use Mermaid when a diagram makes the workflow or relationship clearer.

Good uses:

- process flow
- decision tree
- before/after architecture
- agent loop
- tool selection
- state transitions

Example:

````markdown
```mermaid
flowchart LR
    A["One repo folder"] --> B["Two Claude sessions"]
    B --> C["Both edit the same files"]
    C --> D["Mixed git status"]
    D --> E["Use worktrees"]
```
````

Keep Mermaid diagrams small. If the diagram has more than 7 nodes, simplify it or split it.

## Prompt Examples

Prompts are often the most useful asset in agentic engineering lessons.

Use prompt examples when the learner needs to know what to ask the agent.

Example:

```text
Read project-brief.md and the five starter policy docs.
Draft the product requirements and open questions.
Do not write code.
```

Prefer prompts that include:

- what to inspect
- what to produce
- what not to do
- where to stop
- what evidence to show

## Code And Commands

Use code samples when the concept involves implementation, configuration, or terminal work.

Rules:

- Keep examples short.
- Remove unrelated boilerplate.
- Use realistic names from the lesson context.
- Explain what the code proves.
- Do not paste large code blocks when a small excerpt teaches the point.

Command examples should be copyable:

```bash
git worktree add ../supportbot-answer-api -b answer-api
cd ../supportbot-answer-api
claude
```

## Demo Checkpoints

When the teaching doc is meant for recording, include demo checkpoints.

Use this format:

```markdown
> Demo: Open the terminal and show `git status` in the main repo before creating the worktree.
```

Demo checkpoints should tell Owain:

- what to open
- what to run or show
- what the learner should notice
- when to return to the document

Do not over-script the demo. Give enough structure to keep it clear.

## Course Lesson Mode

When writing course lessons:

- write as the lesson document itself
- assume Owain will read it aloud and riff from it
- connect to the course project when relevant
- include demo checkpoints
- include "Take Action"
- include concise key takeaways
- update or propose a matching short course-platform summary if asked

The lesson should be polished enough to record from directly.

## YouTube Companion Doc Mode

When writing YouTube companion docs:

- start with the concrete problem viewers recognize
- explain the concept plainly
- include demo setup and downloadable assets
- include commands, prompts, code snippets, config snippets, and links where useful
- include a "what to copy" or "files in this repo" section if relevant
- include limits and common mistakes
- end with practical takeaways

YouTube docs should be useful even if the viewer never watches the video.

## Reusing Cards

When a topic repeats across lessons or videos, reuse existing cards rather than re-explaining from scratch.

Example:

The worktree card can appear in:

- a course lesson on parallel agents
- a YouTube video on AI coding terminal setup
- a support doc on Claude Code sessions
- a workshop on multi-agent workflows

When reusing a card, adapt the framing to the current doc. Do not paste it blindly if the learner situation is different.

## Quality Bar

Optimize for:

```text
learner understanding per minute
```

A good teaching doc:

- has one clear outcome
- teaches 4 to 7 specific points
- starts sections from concrete learner situations
- explains plainly without dumbing down
- includes assets that make ideas visible
- avoids generic AI documentation voice
- is easy to read aloud
- is useful as a standalone document

## Avoid AI Documentation Voice

Cut:

- broad background before the learner needs it
- long abstract definitions
- exhaustive caveats
- generic motivational filler
- phrases like "it is important to note"
- repeated summaries of the same idea
- technical detail that does not help the idea click

Prefer:

```text
Here is the situation.
Here is what goes wrong.
Here is the concept that explains it.
Here is what to do.
Here is the demo.
Here is the rule to remember.
```

## Review Checklist

Before finalizing, check:

- Can Owain read this aloud naturally?
- Does every major section teach one specific point?
- Does each section have a concrete asset when useful?
- Is the learner problem visible early?
- Are diagrams, code, prompts, and commands short enough to understand on screen?
- Is anything included only because it is technically true?
- Could a smart beginner explain the lesson back after reading it?

If the answer is no, revise before delivering.

## Example Section

````markdown
## Different Terminals Are Not Different Workspaces

If you open two terminals in the same repo and run two Claude Code sessions, both agents are editing the same files.

That is the problem. One agent might be building the answer API while another redesigns the support page, but they are still writing into the same local folder on the same checked-out branch. When you run `git status`, their changes are mixed together.

```mermaid
flowchart LR
    A["Terminal 1: Claude builds API"] --> C["Same repo folder"]
    B["Terminal 2: Claude edits UI"] --> C
    C --> D["Mixed working tree"]
    D --> E["Hard-to-review diff"]
```

A git worktree fixes this by giving each session its own folder and branch:

```bash
git worktree add ../supportbot-answer-api -b answer-api
cd ../supportbot-answer-api
claude
```

> Demo: Open two terminals in the same repo, show that both report the same branch, then show `git worktree list` after creating a separate worktree.

**Takeaway:** a new terminal is not a new workspace. Use worktrees when multiple agents need to work at the same time.
````
