---
name: substack-notes
description: "Write 2-3 Substack notes — short standalone insights from a video. Use when the user wants to create Substack notes, write short-form content for Substack, or repurpose video content into micro-posts."
---

# Substack notes

Write Substack notes for: $ARGUMENTS

---

## What these are

Short, standalone insights pulled from a video. Each one should make sense on its own — a reader who never watches the video should still get value. Think of them as micro-observations, not previews.

---

## Constraints

- 2-3 notes per video
- Each note: 100-280 characters
- Plain text, no markdown, no hashtags
- End with a natural reference to the video

---

## Examples

<example>
Most engineers use AI agents one at a time. But the real leverage is running three agents that talk to each other — reviewer sends notes straight to the builder. I break this down in my new video.
</example>

<example>
AI doesn't know if your architecture is wrong. It will build exactly what you ask for, fast, in the wrong direction. By the time you realise, customers depend on it and it's almost impossible to reverse. Slow down on the decisions that are hard to undo.
</example>

<example>
AI can write your code in seconds, but it can't easily fix a bad database schema once it's live in production. A bad foundational architecture is almost impossible to reverse. Spend your time getting the foundation right.
</example>

<example>
I've been using a project board to manage my AI agents and it's working really well. Instead of prompting in the terminal, I put tasks on a board. The agents pick up tickets and open PRs. I explain the setup in my new video.
</example>

<example>
Two agents editing the same file will overwrite each other. No merge conflicts, no warnings. Last write wins. The fix is an ownership model — each agent owns specific files. I walk through this in my latest video.
</example>

---

## Output

Save to `workspace/projects/{slug}/substack-notes.md`.

Format each note with a blank line between them. Include character count for each note.
