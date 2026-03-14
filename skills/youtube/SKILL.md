---
name: youtube
description: "Write a YouTube video script. Produces a plan and a script with a hook, framework, apply sections, honest take, and outro. Use when you're ready to plan and write a specific video."
---

# YouTube Script Writer

Turn a video idea into a script you can record section by section.

## Before starting, read:
- `reference/brand.md` — Voice and positioning
- `references/hooks.md` — Hook patterns and voice

## Two Tiers

Videos come in two tiers with different processes:

- **Flagship** (1/week target): Full 4-step process — title, brain dump, plan, script. 15-25 min. Structure: Hook → Framework → Apply (x2-3) → Honest Take → Outro.
- **Short Tactical** (2-3/week target): Lighter process — title and script only, skip brain dump and plan. 3-8 min. Structure: Hook → Demo → Honest Take → Outro.

Detect the tier from user input. If they say "quick video," "short one," or the topic is narrow/reactive, default to Short Tactical. If it's a deep topic, original framework, or multi-part demo, default to Flagship. If unclear, ask.

## Inputs

Required: A topic or video idea.

Optional (improve output if provided):
- Existing `research.md` from the youtube-research skill
- Reference material (docs, blog posts, changelogs)
- Specific demos or tools to show
- Target length

If the user has a `research.md`, use its gap analysis, key points, and recommended title as the foundation. If not, work directly from the topic.

## Process

Read `produce.md` (in this skill directory) for the full process.

### Flagship (full process)

1. **Title** — Generate 15 variations, rate against the checklist, present top 5. Lock the title first.
2. **Brain Dump** — Ask the creator questions, capture their natural voice and opinions.
3. **Plan** — Goal, confusion being solved, key points, CTA, artifact, tier. Present for approval.
4. **Script** — Fixed structure: Hook → Framework → Apply (x2-3) → Honest Take → Outro.

The hook and outro are scripted. Everything else is key points the creator talks from.

### Short Tactical (lighter process)

1. **Title** — Generate 10 variations, rate, pick one.
2. **Script** — Hook → Demo → Honest Take → Outro. No framework section, no multi-part apply.

## Output

Save to `workspace/projects/{slug}/script.md`. One file.
