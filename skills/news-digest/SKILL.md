---
name: news-digest
description: "Research the last 7 days of AI coding tools and broader AI/LLM industry updates for a newsletter. Fans out parallel research agents per source, dedupes against a running log, and emits newsletter-ready entries. Use when the user wants to research recent AI/tech updates, build a weekly digest, or update the running newsletter log."
user-invocable: true
argument-hint: "[window e.g. 'last 7 days' | 'since 2026-05-18' | a topic to focus on]"
---

# News Digest

Research recent updates across AI coding tools and the broader AI/LLM industry, dedupe them against a persistent running log, and produce newsletter-ready entries. This skill is the *research engine* behind the newsletter — it gathers and structures material; it does not publish.

## Default behaviour

- **Window:** last 7 days, counting back from today. If the user passes an argument, honour it: a window (`last 14 days`), an explicit start (`since 2026-05-18`), or a topic to bias toward (`focus on agents`).
- **Scope:** everything in the source registry — AI coding tools *and* broader AI/LLM industry.
- **Output:** append a dated digest to the running log AND print a newsletter-ready draft in chat.

## Files & locations

All data lives under `~/news-digest/` (create it if missing — `mkdir -p ~/news-digest/log`):

- `~/news-digest/sources.md` — the editable source registry. Each `##` heading is one **bucket** = one parallel research agent. If this file does not exist, create it from the template at the bottom of this skill.
- `~/news-digest/log/LOG.md` — human-readable master index. One line per run.
- `~/news-digest/log/YYYY-MM-DD.md` — the dated digest for each run.
- `~/news-digest/log/seen-urls.txt` — dedup ledger, one canonical URL per line. This is the source of truth for "already covered."

## Procedure

1. **Set up.** Compute today's date and the window. Ensure `~/news-digest/log/` exists. If `sources.md` is missing, scaffold it from the template below and tell the user you did.

2. **Load the registry.** Read `~/news-digest/sources.md`. Each `##` bucket becomes one research agent.

3. **Load dedup state.** Read `~/news-digest/log/seen-urls.txt` (may be empty). These URLs are already covered — they must be dropped later.

4. **Fan out — parallel research.** Spawn one `general-purpose` subagent **per bucket**, all in a single message so they run concurrently (cap ~10 at once; if more buckets, batch). Give each the prompt template under "Research agent prompt" below, filled in with that bucket's name, its source URLs, today's date, and the window. Each agent returns a structured list of items — nothing else.

5. **Collect & dedupe.**
   - Merge all agents' items.
   - Drop any item whose URL is already in `seen-urls.txt`.
   - Drop any item dated outside the window.
   - Drop near-duplicates (same announcement reported by two sources) — keep the most primary/official URL.
   - If an item has no real, resolvable source URL, **drop it.** No URL, no entry.

6. **Write entries.** For every surviving item, write it in the **Item format** below. Group the draft by bucket/vendor, vendor headings in a sensible order (coding tools first, then broader industry).

7. **Persist.**
   - Write the full digest to `~/news-digest/log/YYYY-MM-DD.md` (front-matter line with date + item count, then the grouped entries).
   - Append every new item's canonical URL to `~/news-digest/log/seen-urls.txt`.
   - Prepend one line to `~/news-digest/log/LOG.md`: `- [YYYY-MM-DD](log/YYYY-MM-DD.md) — N items · <one-line headline of the biggest story>`.

8. **Report.** Print the draft in chat and state: window covered, buckets researched, items found, items kept after dedup, path to the dated file. If a bucket returned nothing, list it as "no updates" rather than omitting it — silence and failure look the same otherwise.

## Research agent prompt (template)

> You are researching recent product/industry updates for a newsletter. Today is **{TODAY}**. Only report items published/announced **within {WINDOW}** (on or after {START_DATE}).
>
> Bucket: **{BUCKET_NAME}**. Check these official/primary sources (you may follow links to other official pages from them, but do not wander to blogs/aggregators for the facts):
> {SOURCE_URLS}
>
> For each genuine update in the window, return:
> - `date` — publication/announcement date (YYYY-MM-DD)
> - `vendor` — the product/company
> - `title` — short, specific
> - `what` — 1–2 sentences: what it actually is/does
> - `why` — 1 sentence: why it matters / what it changes for users
> - `url` — the canonical official source URL
>
> Rules: Only real, dated, sourced items. Every item MUST have a working official URL. Do not speculate, do not pad, do not include anything outside the window. If a source has no qualifying updates, say so explicitly. Return ONLY the structured list — no preamble.

## Item format

Each entry in the digest and the chat draft uses exactly this structure:

```
### {Title}
`{YYYY-MM-DD} · {Vendor}`

**What is it?** {Plain explanation of the update — what shipped, what it does.}

**Why should I care?** {Why it matters, what it changes, who it affects, what it signals.}

**Find out more:** [{source label}]({url})
```

Keep "What is it?" factual and "Why should I care?" interpretive — that split is the whole value of the digest. One link is enough; add a second only if it adds something (e.g. official changelog + benchmark page).

## Guardrails

- **Verifiable or omitted.** Every entry carries a real source URL. If an agent can't produce one, the item does not ship. Never invent updates, dates, or version numbers.
- **Last-N-days discipline.** Respect the window strictly. A big launch from three weeks ago is not "this week's news."
- **Dedup is the log.** `seen-urls.txt` is what prevents repeating items across runs. Always read it before, always append to it after.
- **Parallel, not serial.** Buckets are independent — spawn them together. Keep their raw output in the subagents; only structured findings come back.
- **Editing sources is editing `~/news-digest/sources.md`.** To track/drop a product, the user edits that file — no need to touch this skill.

## Default `sources.md` template

If `~/news-digest/sources.md` does not exist, create it with this content:

```markdown
# News Digest — Source Registry

Each `##` heading is one bucket = one parallel research agent.
Add/remove products by editing this file. Prefer official changelogs, release
notes, and company blogs over aggregators.

## OpenAI Codex
- https://developers.openai.com/codex/changelog
- https://github.com/openai/codex/releases

## Anthropic Claude Code
- https://docs.claude.com/en/release-notes/claude-code
- https://github.com/anthropics/claude-code/releases

## Cursor
- https://cursor.com/changelog

## GitHub Copilot
- https://github.blog/changelog/label/copilot/

## Google Gemini (CLI & Code Assist)
- https://developers.google.com/gemini-code-assist/docs/release-notes
- https://github.com/google-gemini/gemini-cli/releases

## Other coding agents (Windsurf, Aider, Amp, Zed, Devin)
- https://windsurf.com/changelog
- https://aider.chat/HISTORY.html
- https://zed.dev/releases

## OpenAI — models & platform
- https://openai.com/news/
- https://developers.openai.com/api/docs/changelog

## Anthropic — models & platform
- https://www.anthropic.com/news
- https://docs.claude.com/en/release-notes/api

## Google DeepMind & Google AI
- https://blog.google/technology/ai/
- https://deepmind.google/discover/blog/

## Other labs (Meta, Mistral, xAI, DeepSeek, Qwen)
- https://mistral.ai/news/
- https://x.ai/news
```
