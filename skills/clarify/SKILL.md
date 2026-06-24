---
name: clarify
description: "Turns vague, messy, voice-dictated, or multi-part asks into a self-contained prompt a fresh agent can execute. Use when the user asks to clarify, stress-test, tighten a plan, or resolve references like \"the thing\". Interviews one question at a time, then outputs a final prompt."
user-invocable: true
argument-hint: "<the messy ask or plan to clarify>"
---

# Clarify

Turn a vague ask into a reusable `Final prompt:` block.
Always emit `Final prompt:` before doing work unless the user explicitly says `just do it`, `just run it`, or `skip the prompt`.

## Workflow

1. Read the input and discoverable context: `AGENTS.md`, `CLAUDE.md`, `README.md`, file tree, relevant code.
2. Emit `Cleaned ask:` only when the raw ask is noisy enough to obscure intent.
3. Ask one unresolved decision at a time.
4. Include a recommended answer and one-line reason with each question.
5. After each answer, re-check for new ambiguity.
6. Stop asking when a fresh agent could execute the prompt without more context, or when the user says to write it.
7. Emit one self-contained block under `Final prompt:`.

Question format:

```md
**Q:** <question>
**My recommendation:** <answer> - <one-line reason>
```

## Ask About

- Inputs: file, glob, directory, required args.
- Outputs: location, naming, overwrite behavior.
- Failure modes: network errors, missing files, bad input.
- Scope edges: formats, environments, out-of-scope work.
- Hidden decisions: defaults the agent would otherwise invent.
- Success criteria: how the user knows it worked.

Do not ask about:

- Cosmetic choices.
- Project conventions the repo answers.
- Details already clear in the ask.

## Final Prompt Contract

Include:

- Goal in one sentence.
- Exact file path or directory.
- Inputs and outputs.
- Dependencies, tools, env vars, and conventions.
- Failure behavior.
- Success criteria.
- Out of scope, when it prevents drift.

The prompt must read cold.
No references to "what we discussed" or "the choices above".

## Example Shape

```md
Final prompt:

Build a Python script at `tools/auphonic/enhance.py` that takes one MP3 file
path as a required CLI argument and runs it through the Auphonic Simple API.

Auth: read `AUPHONIC_API_KEY` from the workspace `.env`.
Output: save `<basename>-enhanced.mp3` next to the input.
Overwrite existing output.
Failure: exit non-zero with a clear message for missing input, missing API key,
or API error.
Conventions: follow `tools/youtube/youtube.py` and use a PEP 723 uv header.
Out of scope: batch mode, presets, GUI.
Verify: run end-to-end against a real MP3.
```

## Just Do It

When the user says `just do it`, state assumptions once, bake them into the final prompt, then act.
