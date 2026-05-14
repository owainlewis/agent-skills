---
name: prompt-enhance
description: "Rewrite a vague, messy, or multi-part user prompt into a clean one — then grill the user with clarifying questions until the intent is unambiguous before executing. Trigger eagerly: any time the user's message is voice-dictated, contains filler words (\"basically\", \"like\", \"obviously\"), runs on without punctuation, has multiple loosely-connected parts, makes underspecified references (\"the thing\", \"that script\"), or leaves any decision the user did not explicitly make. Skip only for short, crisp, single-purpose prompts where the deliverable is obvious."
user-invocable: true
argument-hint: "<the messy prompt — usually the user's last message>"
---

# Prompt enhance

The user dictates fast and often sends prompts that are noisy, vague, or have hidden decisions baked in. Your job is to **turn that into an unambiguous spec before any work happens** — not to guess and ship the wrong thing.

## Workflow

1. **Rewrite the raw input** as a clean prompt addressed to yourself. Strip filler ("basically", "like", "so", "obviously"), fix grammar, resolve obvious references (e.g. "this repo" → the current working directory). Preserve the user's intent exactly — do not expand scope, invent constraints, or add requirements they did not state.

2. **Show the cleaned prompt to the user** in a `Cleaned prompt:` block. No preamble before it, no commentary after.

3. **Grill the user with clarifying questions until the prompt is fully unambiguous.** This is the most important step. After the cleaned prompt, list every unresolved question — one at a time or batched via `AskUserQuestion` (max 4 per round). After each round of answers, look again: did the new answers expose further ambiguity? Keep asking. Walk the tree. Do not stop questioning until you could hand the cleaned prompt + answers to a fresh agent and they would build the right thing on the first try.

4. **Execute the cleaned prompt** as if the user had typed it directly. Use the appropriate tools, skills, and project conventions. Do not re-state the prompt — just do it.

## What counts as "ambiguity worth asking about"

Ask when the answer would change the deliverable, the surface area, or the place the work lives. Examples:

- **Location / placement.** "Put it in the scripts folder" — but the project uses `tools/`. Ask which.
- **Inputs.** "Take an MP3" — single file, glob, directory? Required CLI arg, or default to a directory?
- **Outputs.** Where does the result go? What filename pattern? Overwrite if it exists?
- **Failure modes.** What should happen on network error, missing file, bad input?
- **Scope edges.** "Make it support uploads" — just MP3? Other formats? Size limits?
- **Hidden decisions.** Anything where you'd otherwise pick a default — surface it instead.
- **External dependencies.** "Use the API" — which auth flow, which endpoint, which version?
- **Success criteria.** How will the user know it's done correctly?

## What NOT to ask about

- Cosmetic choices the user clearly doesn't care about (variable names, exact wording of log lines).
- Things established by the project's existing conventions (read the codebase first).
- Things the raw prompt clearly answered, even if phrased messily.
- Don't ask 12 questions at once with no priority. Lead with the questions that most change the outcome.

## How to phrase the questions

- Prefer `AskUserQuestion` with concrete options when there's a finite set of reasonable answers — it's much faster than free-text for the user.
- For each option, include enough description that the user can pick without thinking.
- When you have a strong recommendation, put it first and mark it `(Recommended)`.
- Group related questions into one `AskUserQuestion` call (up to 4); don't drip them out one at a time when they could be answered together.

## When to stop asking

Stop only when:

- Every input, output, location, format, and edge case is pinned down, AND
- You can write a one-paragraph spec that a fresh agent could implement without further questions, AND
- The user has either answered the questions or explicitly said "use your judgement" for the remainder.

If the user pushes back ("just do it", "stop asking"), respect that — note the assumptions you're making and proceed.

## Final shape of your output before executing

```
Cleaned prompt:
<the rewritten prompt>

Open questions:
<AskUserQuestion call, or a numbered list if free-text is needed>
```

Then, after answers are resolved across however many rounds it takes, restate the final spec briefly and execute.
