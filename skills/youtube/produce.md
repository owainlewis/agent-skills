# Script Writing

**Goal:** Produce a single script file the creator can record from, section by section.

## Before starting, read:
- `reference/brand.md` — Voice and positioning
- `references/hooks.md` — Hook patterns and voice
- The project's `research.md` if it exists
- `reference/offers.md` — Only when writing the Outro/CTA

---

## Step 1: Title

The title is the single highest-leverage decision. It determines whether anyone clicks. Lock the title before writing anything else.

### Process

1. **Generate 15 title variations.** Go wide. Mix formats — questions, statements, contrarian takes, "How I..." framings, short punchy phrases. Don't self-edit during generation. **Include at least 3 personal/possessive variations** ("My...", "How I...") — these consistently outperform advice-style titles.
2. **Rate each title against the checklist** (see below). Score each criterion as pass/fail.
3. **Rank all 15.** Present the top 5 to the creator with a one-line note on why each works.
4. **Pick one.** The creator chooses. If nothing hits, generate another round.

### The Good Title Checklist

Every title must pass all four:

- **Is it short?** — Under 10 words. Ideally under 8. Every word must earn its place.
- **Is it bold?** — Does it make a claim or take a position? Bland descriptions don't get clicks.
- **Is it original?** — Search YouTube for the topic. If five other videos have a similar title, yours needs to be different.
- **Is it intriguing?** — Does it create a question in the viewer's mind? The title should open a loop the video closes.

### Title rules

- Lead with the viewer's problem or curiosity, not your achievement.
- Avoid generic modifiers: "complete guide", "full tutorial", "everything you need to know."
- Don't front-load with "How to" unless the rest is genuinely compelling.
- Contrarian titles ("You Don't Need X") work when you can back the claim.
- The title and thumbnail are a pair — the title doesn't need to say everything.

Present the top 5 titles to the creator. **Wait for a title choice before moving on.**

---

## Step 2: Brain Dump

Before writing anything, have a conversation with the creator. Ask these questions and let them think aloud. They may not know all the answers — that's fine. Work through it together.

**Questions to ask:**
1. What's this video about? Just talk me through it.
2. Why do you want to make this video right now? What's been on your mind?
3. Who is this for? What does the viewer already know, and what are they trying to figure out?
4. What's the one thing you want someone to walk away being able to do?
5. What's the common mistake or misconception you see around this topic?
6. Is there a demo or something you want to show? What does it look like?
7. Are you building this in a real project or a demo? Can you use your actual codebase?
8. What artifact could this video create? A repo, template, tool, or system someone could use?

Don't rush this. The creator's natural phrasing, observations, and opinions are the raw material for the hook and the entire script. Capture their exact words — the best lines will come from how they naturally talk about the topic, not from polishing their ideas into copy.

If the creator doesn't have clear answers, help them think through it. Suggest angles. Push back on ideas that feel weak. This is a collaborative conversation, not an interview.

---

## Step 3: Write the Plan

Using the brain dump, fill out the Plan. This is the filter — if it's weak, the video isn't ready.

- **Goal** — one sentence. What the viewer can DO after watching (not just understand).
- **The confusion** — what problem or misconception does this video cut through? If you can't name a specific confusion, the video doesn't need to exist.
- **Key points** — 3-4 things the video must deliver. Each one should change what the viewer is able to do.
- **CTA** — pick from `reference/offers.md`
- **Artifact** — what tangible thing does this video produce? (repo, template, open-source tool, named system, or none)
- **Tier** — Flagship (15-25 min, full process) or Short Tactical (3-8 min, lighter process)
- **Pillar / Length**

Present the Plan to the user. **Wait for approval before writing the script.**

---

## Step 4: Write the Script

The script has a fixed structure. Every video follows this shape:

```
HOOK → FRAMEWORK → APPLY (x2-3) → HONEST TAKE → OUTRO
```

That gives you **5-6 sections total**. The hook and outro are scripted. Everything else is key points you talk from.

### The key line

Before writing the script, ask: **is there one line that captures the whole video?** Not every video has one, but when it exists, it's the spine. Use it at up to three structural points — in the hook as a promise, in the middle as a reveal, and in the outro as a callback. Repetition of a strong line creates cohesion. A weak line repeated three times creates cringe. Only do this when the line earns it.

### The arc

The hook is short. The middle is the bulk of the video. The end is short. Think of it as: **setup → value → payoff → out.**

- **Setup (hook):** Deliver on the title promise in the first 15 seconds. Set up one or more payoffs that the video will deliver — leave the best for last.
- **Value (framework + apply):** Each section adds value through unique perspectives, real examples, and demos. No filler, no repetition. Every section must earn its place.
- **Payoff (honest take):** The most valuable insight comes at the end. This is the climax — the thing the viewer couldn't get from the title alone.
- **Out (outro):** End promptly after the payoff. Don't drag. CTA and done.

### Section types

**HOOK** (15-60 seconds, scripted)

The hook has three jobs: deliver on the title promise, set up the payoff, and tell the viewer what they'll learn.

**The first 15 seconds are critical.** The viewer clicked because of the title and thumbnail. Confirm they're in the right place immediately — the first sentence should validate what they clicked for. If you can show visual proof (a demo result, a before/after), do it here.

After the opener, set up the payoffs — what the viewer will get by the end. The best payoff should come last in the video, but the promise of it should be planted here. Then give the roadmap: one or two sentences listing what's coming so the viewer knows the video is worth their time.

Read `references/hooks.md` for the three-beat structure and framing options.

### Hook rules

**Start from the creator's own words.** Ask the creator to brain dump their thinking on the topic — what they've been noticing, why they care, what shift they're seeing. The best hooks come from tightening the creator's natural voice, not from generating polished copy. "I've been thinking about X" is more authentic than "I built an incredible X." The creator is sharing an insight, not performing a result.

**Script it line by line.** The creator reads this nearly verbatim on camera. Put a blank line between every sentence or thought so it's easy to read with natural pauses. No dense paragraphs.

**Clarity over cleverness.** The hook must make sense to someone who knows nothing about the topic yet. Every noun should be concrete. If you say "I'll break down the architecture" — of what? Say "I'll break down how these systems work" or "I'll show you the pattern behind all of them." The viewer should never feel lost or stupid in the first 30 seconds. If a sentence could mean two things, rewrite it until it can only mean one.

**Lead with outcome, not observation.** The first sentence should show the viewer what they'll be able to do, not describe a feeling or an abstract concept. "What if you could X?" or "I stopped doing X and started doing Y" beats "If you've been thinking about X" or "There's been a lot of hype around X." Concrete outcomes pull harder than observations.

**No desire-based openers.** Don't lead with "I built a system that does X amazing thing" or list impressive results. That's performance, not conversation. Lead with an observation or a thought — "I've been thinking about," "there's a pattern behind," "most of us are doing X but..." The creator is an engineer sharing what they've found, not a guru selling a dream.

**No cliche transitions.** Never use: "and here's the thing," "but here's where it gets interesting," "let's dive in," "it turns out," "spoiler alert." These are AI filler. Just state the next idea directly — it doesn't need a transition phrase.

**End with problem, promise, path.** The hook should close with a clear structure: the problem (what's confusing or missing), the promise (what the viewer will be able to do), and the path (how the video gets them there). "By the end of this video, you'll be able to..." is a strong closing pattern.

**FRAMEWORK** (2-3 minutes, key points)

Your mental model. The simple way to think about the topic. This is where you cut through the confusion named in the hook and give the viewer a clear lens.

This is NOT a definition section. Don't start with "so what is X?" Start with your way of thinking about it. The viewer came for your perspective, not a Wikipedia summary.

Write as key points the creator talks from, not verbatim script. Include what's on screen (diagram, code, terminal) for each point.

**APPLY sections** (2-4 minutes each, key points + demo notes)

Apply the framework to real examples. One concept per section. This is where the video earns its value — the viewer sees the framework in action.

2-3 Apply sections per video. Each one should:
- Introduce the specific thing you're applying the framework to
- Show it working (screen share, demo, real code)
- Connect back to the framework ("this is the X part of what I described earlier")

Write as key points + demo notes. Do not write verbatim narration — the creator talks through the demo naturally.

**HONEST TAKE** (1-2 minutes, key points)

What works. What doesn't. Where the limits are. This is the section most tech YouTubers skip, which is why it builds the most trust. Don't manufacture positivity. Say what you actually think.

**Contrarian threading:** The honest take doesn't have to be confined to this section. If the entire video's thesis IS the contrarian position (e.g., "you don't need X"), thread it from the hook through the end. The honest take then becomes the nuanced version — where the contrarian stance applies and where it breaks down. See `references/hooks.md` for the contrarian lead pattern.

Key points only. This should feel unscripted.

**OUTRO** (15-30 seconds, scripted)

CTA. Keep it short. One ask, not three. End promptly after the payoff — don't recap, don't ramble, don't add "one more thing." The honest take IS the climax. The outro is just the exit.

### Section format

Every section in the script follows this format:

```markdown
## {Type}: {Name}

**Record:** {talking head / screen share / split screen}
**Goal:** {one sentence — what the viewer gets from this section}

**Key points:**
- {point 1}
- {point 2}
- {point 3}

**On screen:** {what the viewer sees — diagram, code, terminal, etc.}

> Demo: {for screen share sections — what you do on screen, step by step}
> Key moment: {the single most important thing the viewer sees}
```

For the Hook and Outro only, replace key points with full scripted text.

### Timing guide

| Section | Duration |
|---|---|
| Hook | 30-60 seconds |
| Framework | 2-3 minutes |
| Apply (each) | 2-4 minutes |
| Honest Take | 1-2 minutes |
| Outro | 15-30 seconds |

A typical video: Hook (1 min) + Framework (3 min) + 3 Apply sections (3 min each) + Honest Take (1 min) + Outro (30 sec) = ~15 minutes.

---

## Making it valuable

These rules determine whether the video is worth watching or just another tutorial.

**Every section must change what the viewer can do.** Not just what they know — what they can do. "Now you understand what specs are" is knowledge. "Now you can write a spec that prevents an agent from guessing" is ability. If a section only adds knowledge, it needs a demo or example that converts it into ability.

**Start where the viewer's knowledge ends.** Don't explain what the viewer already knows. If the title says "spec-driven development," don't spend 2 minutes defining what a spec is — the viewer clicked because they already know roughly what it is. Start at the edge of their understanding and push forward.

**Your opinion is the value.** The viewer can read docs. They can watch five other videos. The thing they can't get anywhere else is your experience-informed take on what actually works. Lead with what you think. "I've tried three approaches and this is the one that stuck" is more valuable than "here are three approaches."

**One framework applied multiple times beats multiple frameworks explained once.** Depth over breadth. Show the same mental model working across different situations. The viewer remembers a framework they've seen applied three times. They forget three frameworks they've seen once.

**Cut anything the viewer could find in the docs.** If it's in the README, don't read it on camera. Show what the docs don't tell you — the workflow, the gotchas, the decisions you made and why.

**The demo is the proof.** Every claim needs a demo or a real example. "This is faster" — show it. "This produces better code" — show the code. If you can't demo a claim, either find a way or cut the claim.

---

## Output

Save to `workspace/projects/{slug}/script.md`. One file — Plan at the top, then all sections.

---

## Short Tactical Format

For 3-8 minute companion videos that keep the algorithm fed. These are focused, single-idea videos — no framework section, no multi-part apply sections. Use when the idea doesn't need 15 minutes to deliver.

### When to use

- The idea is one clear demo or take, not a multi-part breakdown
- Companion piece to a flagship video ("here's the quick version")
- Responding to news, a tool launch, or a trending topic quickly
- The creator says "this is a quick one" or the topic is narrow

### Process (lighter)

Skip the brain dump and formal plan. Go straight from title to script.

1. **Title** — Generate 10 variations (not 15). Same checklist. Pick one.
2. **Script** — Hook → Demo → Honest Take → Outro.

### Structure

```
HOOK → DEMO → HONEST TAKE → OUTRO
```

### Timing

| Section | Duration |
|---|---|
| Hook | 15-30 seconds |
| Demo | 2-5 minutes |
| Honest Take | 30-60 seconds |
| Outro | 15 seconds |

Total: 3-8 minutes.

### Section notes

- **Hook:** Same three-beat structure but tighter. 2-4 sentences. Get to the point fast.
- **Demo:** The bulk of the video. One thing shown well. Screen share with narration. Key points + demo notes, not verbatim script.
- **Honest Take:** Quick — what works, what doesn't. 2-3 bullet points.
- **Outro:** One sentence CTA. Done.

### Short Tactical Template

```markdown
# Script: {Title}

**Tier:** Short Tactical
**Goal:** {what the viewer can DO}
**Artifact:** {repo, template, or none}
**Length:** {X min}

---

## Hook

**Record:** talking head
{Scripted — 2-4 sentences. Validate the title, state what you'll show.}

---

## Demo: {What You're Showing}

**Record:** screen share
**Goal:** {the one thing the viewer learns}

**Key points:**
- {what you're showing}
- {the insight or takeaway}

> Demo: {step by step}
> Key moment: {the single most important thing}

---

## Honest Take

**Record:** talking head

**Key points:**
- {what works}
- {where the limits are}

---

## Outro

**Record:** talking head
{One sentence CTA.}
```

---

### Template

```markdown
# Script: {Title}

## Plan

**Goal:** {what the viewer can DO after watching}
**The confusion:** {what problem or misconception this cuts through}
**Key points:**
1. {point}
2. {point}
3. {point}
**CTA:** {from offers.md}
**Pillar:** {pillar} | **Length:** {X min}

---

## Hook

**Record:** talking head
**Goal:** Convince the viewer to stay. Name the problem, tell them what they'll learn.

{Scripted text — 4-8 sentences. First sentence validates the title. Last 1-2 sentences are the roadmap: what the video covers.}

---

## Framework: {Name}

**Record:** {talking head / screen share}
**Goal:** {the mental model the viewer walks away with}

**Key points:**
- {your way of thinking about this}
- {the key distinction or insight}
- {why this matters in practice}

**On screen:** {diagram, code, etc.}

---

## Apply: {Example 1}

**Record:** screen share
**Goal:** {what this example demonstrates}

**Key points:**
- {what you're showing}
- {how it connects to the framework}
- {the takeaway}

> Demo: {step by step what happens on screen}
> Key moment: {the most important thing the viewer sees}

---

## Apply: {Example 2}

{same format}

---

## Apply: {Example 3}

{same format — optional, include if the video needs it}

---

## Honest Take

**Record:** talking head
**Goal:** Build trust. Say what works and what doesn't.

**Key points:**
- {what works well}
- {where the limits are}
- {what you'd do differently or what's still unsolved}

---

## Outro

**Record:** talking head
**Goal:** CTA

{Scripted — 2-3 sentences. One ask.}
```
