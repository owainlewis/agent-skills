---
name: clarify
description: "Turn a vague, messy, or multi-part user ask into a clean, self-contained prompt that a fresh agent could execute without further questions. Interview the user one question at a time — walking down the decision tree, branching on each answer — until the prompt is tight, then output the final prompt as the deliverable. Trigger eagerly: any voice-dictated input, filler-heavy prose, underspecified references (\"the thing\", \"that script\"), multi-part requests, or any plan the user wants stress-tested. The skill itself can be skipped for trivial one-line requests where producing a prompt artifact would be pure ceremony — but once invoked, always produce the prompt, even if execution looks trivial."
user-invocable: true
argument-hint: "<the messy ask or plan to clarify>"
---

# Clarify

The user dictates fast and brings half-formed plans. Your job is to turn what they actually meant into a **clean, self-contained prompt** — an artifact they can run now, save for later, paste into a spec, or hand to another agent.

This skill produces a prompt. It does not (by default) execute that prompt. The output is the deliverable.

**Hard rule:** always emit the `Final prompt:` block before doing any work — even when the ask is already concrete enough that you could "just run it." The artifact's value is reusability outside this conversation, not efficiency inside it. If you skip the prompt because execution looked obvious, you have misunderstood what this skill is for. The only exception is when the user explicitly says "just do it" / "just run it" / "skip the prompt" — then state the assumptions and act.

This is the most important skill in the toolkit. Most failed agent work comes from acting on an unclear ask. Slow down here so the rest goes fast.

## Workflow

1. **Read the input and the codebase.** Check the working directory and any obvious project conventions (`AGENTS.md`, `CLAUDE.md`, `README.md`, the file structure). Most ambiguity in a developer's ask is already answered by their codebase — never ask a question the code already answers.

2. **Optionally restate the raw ask cleanly.** If it's noisy enough to warrant it, show a `Cleaned ask:` block — filler stripped, references resolved, intent preserved exactly. Skip this if the original is already crisp.

3. **Interview the user one question at a time.** Walk down the decision tree. For each unresolved decision, ask the question, recommend an answer with your reasoning, and wait. Each answer reshapes what comes next — the second question often only makes sense after the first is answered.

4. **Keep going until the prompt would be tight.** After each answer, check: did this expose new ambiguity? If yes, ask again. Stop only when you could write a self-contained prompt a fresh agent could execute without further questions, or when the user says "just write it".

5. **Produce the final prompt as the deliverable.** Output it as a single, self-contained block under a `Final prompt:` heading. The prompt must read cold — no references to "what we discussed" or "the choices above". A fresh agent receiving only this prompt must have everything they need.

6. **Ask what's next.** After the prompt, offer the three handoff options:
   - **Execute it now** in this session.
   - **Save it** to a file (suggest a path like `prompts/<slug>.md` or wherever the project keeps prompts).
   - **Stop** — the user will use the prompt elsewhere.

   Wait for the answer; don't pick a default.

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

## What the final prompt looks like

The final prompt is **self-contained and imperative** — addressed to whoever runs it (you in this session, a future agent, a teammate). It should include:

- **What to build, in one sentence.**
- **Where it lives** (exact file path or directory).
- **Inputs and outputs** (types, paths, naming conventions, overwrite behavior).
- **Dependencies and conventions** (which tools, which env vars, which existing patterns to follow).
- **Failure behavior** (what happens on bad input, network errors, missing files).
- **Success criteria** (how the agent knows it's done).
- **Anything out of scope**, if it's a likely temptation.

Example shape:

```
Final prompt:

Build a Python script at `tools/auphonic/enhance.py` that takes one MP3 file
path as a required CLI argument and runs it through the Auphonic Simple API
to produce an enhanced version.

Auth: read AUPHONIC_API_KEY from the workspace .env file.
Output: save the result next to the input as `<basename>-enhanced.mp3`.
Overwrite silently if the output already exists.
Failure: exit non-zero with a clear error message on missing input file,
missing API key, or API error.
Conventions: follow tools/youtube/youtube.py — uv inline-script header
(PEP 723) with dependencies declared in the script.

Out of scope: batch mode, presets, GUI. One file, one CLI invocation.

Test it end-to-end against a real MP3 once built.
```

If you can't write a paragraph like that yet, you have more questions to ask.

## When the user says "just do it" or "just write it"

Respect that immediately. State the assumptions you're making for the unresolved questions in one block, then produce the final prompt with those assumptions baked in. Don't keep grilling.
