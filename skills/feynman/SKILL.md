---
name: feynman
description: "Explains one technical theme as a teachable document with mechanism-first sections, examples, edge cases, and an exercise. Use when the user asks to explain, teach, or document a concept as a course lesson, YouTube reference, or newsletter basis."
user-invocable: true
argument-hint: "<topic>"
---

# Feynman

Write a document that teaches one technical theme through mechanisms, examples, edges, and an exercise.

## Rules

- Cover one coherent theme.
- If the topic is too broad, offer 2-4 narrower themes and ask the user to pick one.
- Open with an observation the reader recognises, not a definition.
- State the promise before details.
- At section level, state the point before explaining it.
- Explain the mechanism before naming the term.
- Give one plain mental-model sentence before formalism.
- Use one concrete example per section.
- Walk the example through before the general rule.
- When using an analogy, name where it breaks.
- Name unsolved, messy, or disputed edges.
- Close the obvious wrong conclusion.
- Use short sentences and common words.
- Cut sentences that sound profound but add no information.
- Put reference material, tables, cheat sheets, and syntax summaries in a separate document.

## Structure

```md
# [Title: claim or question]

[Opening: 2-4 sentences. Observation from the reader's experience.]

[Promise: what the reader will understand.]

## [Section title: specific claim]

[Point in one sentence.]
[One concrete example, walked through completely.]
[Code, command, prompt, or diagram only when it clarifies the idea.]

## [Next section]

## Putting it together

[Short scenario that uses the sections together.]

## Try it

[One exercise. Under ten minutes.]

[Closing sentence that earns the opening promise.]
```

## Narrowing Example

```md
"AI agents" is too broad. Pick one:

1. Agent memory: types, mechanics, when to use each
2. Tool calling: loop mechanics and tool design
3. Error handling: failures, recovery, avoiding hangs
```

## Mechanism Example

Weak: "This uses RAG to retrieve relevant context."

Strong: "RAG works in three steps. First, search stored documents for content relevant to the user's question. Second, paste that content into the prompt. Third, generate an answer using that information. The name is just the sequence: retrieve, augment, generate."

## Check

- Opening describes something recognisable.
- Promise appears before detail.
- Mechanism appears before term.
- Each section teaches one point with one example.
- Obvious wrong conclusion is closed.
- Analogy limits are named.
- Edges are named.
- `Putting it together` exists.
- Exercise exists.
