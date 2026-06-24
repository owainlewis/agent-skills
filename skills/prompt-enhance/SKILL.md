---
name: prompt-enhance
description: "Rewrites a rough prompt, voice dump, or half-written instruction into an agent-ready prompt. Use when the user asks to make a prompt better, enhance/refine a prompt, clean up instructions for an agent, or improve pasted prompt text. One-shot transformer; does not interview."
user-invocable: true
argument-hint: "<the text or draft prompt to refine>"
---

# Prompt Enhance

Return one refined prompt a coding or knowledge agent can execute.
Do not interview.
When information is missing, use an assumption or `[NEEDS: ...]`.

## Workflow

1. Read the input and referenced context: repo, files, `AGENTS.md`, `CLAUDE.md`, `README.md`, relevant code.
2. Resolve unambiguous references such as "the thing" or "that script".
3. Identify defects: vague goal, buried intent, contradictions, missing scope, missing output format, missing success criteria, negative phrasing, premature-stop scaffolding, irrelevant noise.
4. Rewrite the prompt. Preserve intent. Remove filler. Keep substance.
5. Return the refined prompt, then `Changed`, `Assumptions`, and `Gaps` lines as needed.
6. Offer one action: run it now, save it to `prompts/<slug>.md`, or stop.

## Principles

- Lead with the goal in one sentence.
- State output, format, constraints, and scope directly.
- Resolve contradictions or state priority.
- Say what is in scope and what is out of scope.
- Use numbered steps only when order matters.
- Prefer positive instructions.
- Include only context that changes the work.
- Specify output contract: format, structure, length, path, naming, overwrite behavior.
- State success criteria: tests, files, observed behavior, or other proof.
- Tell the agent to proceed on reasonable assumptions unless genuinely blocked.
- Use a role only when it changes tone or judgment.
- Separate instructions, context, examples, and pasted input when they could be confused.
- Add examples only for exact format or style.

## Gaps

- Use a sensible default when safe. Record it under `Assumptions`.
- Use `[NEEDS: <missing detail>]` when no safe default exists.
- Do not ask questions. Use `clarify` for interviews.

## Output

```md
Refined prompt:

<rewritten, self-contained prompt that reads cold>

---
Changed: <substantive improvements>
Assumptions: <defaults baked in, omit if none>
Gaps: <remaining [NEEDS: ...] items, omit if none>
```

Then offer: run it now, save it to `prompts/<slug>.md`, or stop.

## Example

Input:

> script that pulls podcast mp3s and transcribes them, use whisper, don't make it slow, cache stuff somewhere sensible

Output:

```md
Refined prompt:

Build a Python CLI script that downloads podcast episodes from an RSS feed and transcribes each MP3 with OpenAI Whisper.

Input: RSS feed URL as a required argument.
Output: save each MP3 and transcript (`.txt`, same basename) under `data/<podcast-slug>/`.
Caching: skip any episode whose MP3 and transcript already exist.
Performance: download and transcribe episodes concurrently.
Failure: exit non-zero for a bad feed URL; skip and log individual episode failures.
Success: running twice performs no redundant downloads or transcriptions.
Out of scope: UI, speaker diarization, non-MP3 formats.

---
Changed: added input, output, caching, concurrency, failure handling, and success criteria.
Assumptions: RSS feed input; local `data/` output.
```
