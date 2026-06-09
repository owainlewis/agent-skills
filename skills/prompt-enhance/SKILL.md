---
name: prompt-enhance
description: "Rewrites a rough prompt, voice dump, or half-written instruction into a refined, agent-ready prompt. Use when the user asks to make a prompt better, enhance/refine a prompt, clean up instructions for an agent, or improve pasted prompt text. One-shot transformer; does not interview."
user-invocable: true
argument-hint: "<the text or draft prompt to refine>"
---

# Prompt Enhance

Take the input text and return a single refined prompt that a coding or knowledge agent can execute well. The job is craft applied to wording and structure — turn a messy, ambiguous, or contradictory ask into a clear, explicit, well-ordered instruction.

This is a **one-shot transformer**. It does not interview the user. It does not try to discover what the user "really wants" — that is `clarify`'s job. `prompt-enhance` takes the intent as given and makes the *prompt* better: clearer, more explicit, contradiction-free, properly scoped, and structured the way models follow best.

If you find yourself wanting to ask the user a question, you are reaching for `clarify`. Here, mark the gap in the output instead (see **Gaps**) and keep going.

## Workflow

1. **Read the input and the context it points at.** If it references a repo, files, or conventions, glance at them (`AGENTS.md`, `CLAUDE.md`, `README.md`, the relevant code). Resolve "the thing" / "that script" to real names where the context makes it unambiguous. Never invent specifics the input and context don't support — mark them as gaps instead.

2. **Diagnose what makes it a weak prompt.** Run it against the principles below: vague intent, buried goal, contradictions, missing scope, no output format, no success criteria, negative phrasing, instructions that rely on the model inferring scope, premature-stop scaffolding, irrelevant noise.

3. **Rewrite, applying the principles.** Produce one clean prompt. Preserve the user's intent exactly — sharpen the wording, never change what they asked for. Cut filler; keep substance. Density over length.

4. **Emit the refined prompt as the deliverable**, then a short note of what you changed and any gaps. Offer to run it or save it.

## Principles (the craft this skill applies)

Drawn from Anthropic's and OpenAI's prompting guidance. Apply the ones the input needs; don't bloat a prompt with structure it doesn't warrant.

- **Lead with the goal in one sentence.** What outcome, for whom, why. The first line should make the objective unmissable.
- **Be explicit, not implicit.** State the desired output, format, and constraints directly. Modern models follow instructions *literally* — they will not silently generalize. If something must apply broadly, say so ("every section, not just the first").
- **Kill contradictions.** Conflicting instructions are the most expensive defect in a prompt — the model burns effort reconciling them and picks unpredictably. Reconcile or drop the loser. If two requirements genuinely conflict, state the priority.
- **Scope it — in and out.** Say what's included and, when there's an obvious temptation, what's out of scope. Bound the inputs, the surface area, the formats.
- **Sequence when order matters.** Use a numbered list for steps that must happen in order or completely; prose for everything else.
- **Prefer positive instructions.** "Do X" steers better than "don't do Y". Show the wanted behavior rather than listing forbidden ones.
- **Add the context the model needs and no more.** Why the task exists, who consumes the output, which conventions/tools/patterns to follow. Cut backstory that doesn't change the work.
- **Specify the output contract.** Format, structure, length, where it goes, naming, overwrite behavior. If shape matters, give a tiny example or a schema.
- **State success criteria.** How the agent knows it's done and correct — tests pass, file exists, behavior observed.
- **Bias to action.** Tell the agent to proceed on reasonable assumptions rather than stopping to ask, unless genuinely blocked. Remove scaffolding that forces premature plans or status preambles.
- **Use a role only when it earns its place.** A one-line role/persona can focus tone and judgment; skip it for mechanical tasks.
- **Structure with light markup when the prompt mixes kinds of content.** When instructions, context, examples, and pasted input run together, separate them — headings or `<tags>` — so the agent can't confuse data for instructions. Don't tag a prompt that's already clear as prose.
- **Add examples when format or style must be exact.** One or two well-chosen examples steer output more reliably than description. Wrap them so they read as examples, not as the task.

## Gaps

When the input is missing something a strong prompt needs (a path, a success criterion, a choice between two reasonable options), do **not** ask. Either:

- fill it with a sensible default and record it under **Assumptions**, or
- if there's no safe default, leave an inline `[NEEDS: <what's missing>]` placeholder so the user can fill it in before running.

This is the line that keeps `prompt-enhance` one-shot. Questions belong to `clarify`.

## Output

Emit exactly this shape:

```
Refined prompt:

<the rewritten, self-contained prompt — reads cold, no references to "your input" or "above">

---
Changed: <one or two lines on the substantive improvements — e.g. resolved the contradiction between X and Y, added output path and success criteria, scoped out Z>
Assumptions: <defaults you baked in, if any — omit the line if none>
Gaps: <anything left as [NEEDS: …], if any — omit the line if none>
```

Then offer, in one line: run it now, save it (suggest `prompts/<slug>.md`), or stop.

## Example

Input:

> ok so i want like a script that pulls down the podcast episodes, mp3s, and uh transcribes them, use whisper i think, oh and don't make it slow, should probably cache stuff, put it somewhere sensible

Refined prompt:

```
Refined prompt:

Build a Python CLI script that downloads podcast episodes as MP3s and
transcribes each one with OpenAI Whisper.

Input: an RSS feed URL as a required argument.
Output: save each episode's MP3 and its transcript (`.txt`, same basename)
under `data/<podcast-slug>/`.
Caching: skip download and transcription for any episode whose output files
already exist, so re-runs are incremental.
Performance: download and transcribe concurrently across episodes.
Failure: exit non-zero with a clear message on a bad feed URL or a download
error; skip and log an individual episode that fails, then continue.
Success: running twice in a row does no redundant work and leaves one MP3 +
one transcript per episode.

Out of scope: a UI, speaker diarization, formats other than MP3.

---
Changed: turned "don't make it slow" into concrete concurrency + caching
requirements; gave the output a real location and naming scheme; added
per-episode failure handling and a success check.
Assumptions: RSS feed as the input source; local `data/` directory for output.
```

Run it now, save it to `prompts/podcast-transcribe.md`, or stop?
