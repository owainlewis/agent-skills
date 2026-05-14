---
name: clarify
description: "Take a vague, messy, or multi-part user ask and turn it into an unambiguous spec before any work happens. Rewrite the ask if it's noisy, then interview the user one question at a time — walking down the decision tree, branching on each answer — until you could hand the final spec to a fresh agent and they'd build the right thing. Trigger eagerly: any voice-dictated input, filler-heavy prose, underspecified references (\"the thing\", \"that script\"), multi-part requests, or any plan the user wants stress-tested. Skip only for short, crisp, single-purpose prompts where the deliverable is obvious."
user-invocable: true
argument-hint: "<the messy ask or plan to clarify>"
---

# Clarify

The user dictates fast and brings half-formed plans. Your job is to turn what they actually meant into a spec tight enough that a fresh agent could implement it without further questions — and **not** to guess and ship the wrong thing.

This is the most important skill in the toolkit. Most failed agent work comes from acting on an unclear ask. Slow down here so the rest goes fast.

## Workflow

1. **Read the input.** Check the working directory and any obvious project conventions (`AGENTS.md`, `CLAUDE.md`, `README.md`, the file structure). Most ambiguity in a developer's ask is already answered by their codebase — never ask a question the code already answers.

2. **Rewrite the ask** (only if it's noisy enough to warrant it). Strip filler ("basically", "like", "obviously"), fix grammar, resolve obvious references. Preserve the user's intent exactly — do not expand scope or invent constraints. If the original is already crisp, skip this step. Show the cleaned version as a `Cleaned ask:` block, no commentary.

3. **Interview the user one question at a time.** Walk down the decision tree. For each unresolved decision, ask the question, recommend an answer with your reasoning, and wait. Each answer reshapes what comes next — the second question often only makes sense after the first is answered.

4. **Keep going until the spec is tight.** After each answer, check: did this expose new ambiguity? If yes, ask again. Stop only when you could write a one-paragraph spec a fresh agent could implement without further questions, or when the user says "just do it".

5. **Restate the final spec, then execute.** Brief one-paragraph summary of what you're about to build, then do it. No re-asking, no preamble.

## Rules for asking questions

**Ask one question at a time.** This is non-negotiable. Batching feels efficient but answers branch the tree — you cannot pre-compute the next three questions because question 2 depends on the answer to question 1. One question, one answer, then re-evaluate.

**Always recommend an answer.** Never present a question as a neutral menu and ask the user to choose. Have a take. Format:

> **Q:** \<the question\>
> **My recommendation:** \<your answer\> — \<one line of reasoning\>

If they accept, move on. If they push back, you've learned something the code didn't tell you.

**Check the codebase before asking.** If the answer is discoverable — file paths, naming conventions, framework defaults, existing patterns — go read. Don't ask the user to recite what you can find in 5 seconds. Ask only when the answer requires user intent or taste.

**Ask about what changes the deliverable.** Worth asking:
- Inputs (single file? glob? directory? required arg?)
- Outputs (where? what naming? overwrite behavior?)
- Failure modes (network errors, missing files, bad input)
- Scope edges (which formats, which environments, what's out of scope)
- Hidden decisions (anything where you'd otherwise pick a default — surface it)
- Success criteria (how does the user know it's done correctly?)

Not worth asking:
- Cosmetic choices (variable names, exact log wording)
- Things the project's existing conventions already settle
- Things the raw ask clearly answered, even if phrased messily

## When the user says "just do it"

Respect that immediately. State the assumptions you're making for the unresolved questions in one block, then execute. Don't keep grilling.

## What "tight enough to execute" looks like

Before you start work, you should be able to write something like:

> Building a Python script at `tools/auphonic/enhance.py` that takes one MP3 path as a CLI arg, uploads to the Auphonic Simple API using `AUPHONIC_API_KEY` from `.env`, polls until processing completes, and saves the result as `<basename>-enhanced.mp3` next to the input. No preset. Errors on missing file, surfaces API errors. Overwrites existing output silently.

If you can't write that paragraph yet, you have more questions to ask.
