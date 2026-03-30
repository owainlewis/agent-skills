---
name: linkedin-post
description: "Write a LinkedIn post from notes, a script, an article, or a rough idea. Use when the user wants to write, draft, or repurpose content for LinkedIn."
---

# LinkedIn post

You will be given notes, a script, an article, or a rough idea. Turn this into an engaging LinkedIn post that delivers value.

**Input:** $ARGUMENTS

Follow these steps in order. Do not skip ahead.

---

## Step 1: Hook options

The algorithm gives 3-5x more weight to the first 1-2 sentences. The hook decides whether anyone reads the rest.

Propose 3 hook options. Each one should:
- Take a different angle on the source material
- Be 1-2 lines, under 10 words per line
- Feel written for this specific topic, not filled into a formula
- Use simple words at a basic reading level. No jargon. No words the reader has to decode.
- Either promise clear value ("explained simply", "here's how") or create intrigue ("run every single day", "pretty much slop")
- Never confuse the reader. If they have to re-read the hook, it failed.
- Never talk down to the reader or make them feel dumb. No "most of you don't know" or "you're doing it wrong." Make them feel smart and curious, not called out.

Present as a numbered list. **Stop and wait for the user to pick one before continuing.**

### Hook patterns

Real hooks from real posts. Study the rhythm and angle. Don't copy them.

> I have two AI agents that run every single day.
> One finds problems in my code. The other fixes them.

> Subagents vs agent teams explained.
> Claude Code has two ways to coordinate work:

> OpenAI just quietly released a feature that could change how developers work.

> 6 load balancing algorithms every developer should know

> If you want AI to write code like a senior engineer, learn these 5 steps:

> 7 mental models that killed my overthinking forever:

> How to subtly upgrade your life in 2026.
> Dial in these 5 everyday inputs:

> If you're confused about API auth, you're not alone.
> 7 ways to secure your API, explained simply:

> The best days don't start in the morning.
> They start the night before.

> This stat from McKinsey blew my mind:
> High performers produce 800% more output than average.

> One of the highest ROI skills? Storytelling.
> How to tell stories that captivate any audience:

> Claude's writing on its own is pretty much slop.
> Here's how to make it sound like you (and not a robot):

> Common misbelief: Modern marketing is just "posting online."
> It's not. It is 5 individual channels.

> If I had to restart my career tomorrow, these are the 9 soft skills I'd learn first:

---

## Step 2: Write the post

After the user picks a hook, write the full post. Ask the user which CTA they want (see step 3) before writing, or use the one they specified in the input.

### Writing rules

- **Explain first, persuade second.** If the post is about a tool or concept, explain what it is and how it works BEFORE saying why it matters.
- **Short sentences. Common words.** If it sounds like writing, rewrite until it sounds like talking.
- **Earn the list.** Show the pain, the cost, the mess BEFORE the fix.
- **Use the personal pivot.** "I used to [old way]. Now I [new way]." Makes advice feel earned, not preachy.
- **One concrete number per post.** Specifics, not claims.
- **Close with a one-line reframe.** The last sentence before the CTA should recontextualize the entire post. Make it screenshot-worthy.

### Post formats

Let the topic pick the format:

- **Explainer** - explain a tool/concept, then why it matters. Best for news, launches, technical concepts.
- **Cheatsheet** - numbered items, each self-contained. Each item: what it is, one concrete detail, when it works or breaks. End with a taxonomy.
- **Step-by-step** - numbered steps, each with one action and one explanation. "Here's the exact process I use" framing.
- **Framework** - name the system. Each item: concept, personal story ("I used to..."), reframe.
- **Comparison** - X vs Y. Give each one an analogy first, then details. Close with a decision rule.
- **Category breakdown** - break a big topic into 3-5 categories. Each category: what it is, specific actions. Close with a unifying principle.

### What not to do

- Emoji bullets, checkmark lists, or arrow symbols
- Product promotion woven into every post
- Generic advice with no personal experience behind it
- Lists where every item is just a definition with no personal take

---

## Step 3: Add the CTA

<!-- CUSTOMIZE: Replace these CTAs with your own. Keep the structure: repost line + one destination. -->

Every post ends with a repost line and one destination. Ask the user which CTA to use if they haven't specified.

**Repost line (always include):**

Enjoy this? Repost it to your network and follow [YOUR NAME] for more.

**Then pick one:**

1. **YouTube:** PS: I make videos about [YOUR TOPIC]. Check them out: [YOUR YOUTUBE URL]
2. **Newsletter:** Want to go deeper? Join my newsletter: [YOUR NEWSLETTER URL]
3. **Community:** PS: I run a community for [YOUR AUDIENCE]. Join here: [YOUR COMMUNITY URL]

---

## Step 4: Review

Before presenting the final post, verify:

- [ ] Plain text only (no markdown, asterisks, backticks)
- [ ] Under 3000 characters
- [ ] No em dashes (use a hyphen or rewrite)
- [ ] No external links in post body (links only in CTA)
- [ ] No filenames that render as URLs on LinkedIn
- [ ] Hook is specific to this topic
- [ ] One idea per post
- [ ] CTA is included
- [ ] All titles and headings in the post use sentence case
- [ ] No fabricated stories or results. Flag [NEEDS REAL EXAMPLE] where the author needs to fill in.

---

## Output

Present the complete post (ready to copy-paste), hook pattern used, and character count.

---

## Examples

Real posts that worked. Study for voice, structure, and pacing. Match the tone, not the topic.

<!-- CUSTOMIZE: Add your own best-performing posts below. Keep the WHY THIS WORKS annotations. -->

<example title="explainer - explain first, then why it matters">
OpenAI just quietly released a feature that could change how developers work.

It's called Automations and it's part of their coding tool, Codex.

Codex is an AI coding assistant. You give it a task in plain English - like "fix this bug" or "review this code" - and it does the work for you.

Automations take that one step further.

Instead of asking Codex to do something once, you can set it to run the same task on a schedule. Every morning. Every hour. Whatever you want.

You write a prompt. You pick a schedule. Codex runs it automatically in the background.

Here's a real example from their docs:

You tell Codex: "Look at my last 24 hours of code commits, find any bugs I introduced, and fix them."

It runs that every day. You wake up, open your inbox in the app, and the fixes are already there waiting for you to review.

That's a big deal. Here's why.

Automations allow you to replace complex automation tools with natural language and the intelligence of agents.

It takes you out of the loop and enables you to become much more effective.

A few things worth knowing:

It runs locally on your machine. Codex needs to be open, and your project files need to be on your computer.

Each run starts fresh. In Git projects, it creates a separate copy of your code so it doesn't mess with what you're working on.

If you're a developer or business owner, this is worth paying attention to.
</example>

<!--
WHY THIS WORKS:
- Explains what Codex IS before what Automations do. Reader never feels lost.
- Concrete example ("look at my last 24 hours of commits") instead of abstract claims.
- "Why it matters" comes AFTER the reader already understands the feature.
- Practical details (runs locally, starts fresh) answer real questions.
-->

<example title="comparison - analogies then details">
Subagents vs agent teams explained:

Claude Code has two ways to coordinate work:

Here's when to use each.

1. Subagents are contractors

You tell one agent to delegate work. It hands tasks to workers. Workers complete them and report back.

The parent orchestrates everything. Workers never talk to each other.

Token efficient. Results get summarised back to the parent instead of keeping full context.

2. Agent teams are engineering squads

Each teammate is its own Claude Code session with its own context window.

They share a task list. They message each other directly. They self-coordinate.

Best for: Work that spans layers. Frontend, backend, and tests that all need to move together.

3. Token cost is real

Agent teams cost roughly 5x the tokens. Every teammate is a separate Claude instance.

You wouldn't use this for a bug fix.

But for a complex build where you'd otherwise be relaying messages between agents yourself, the saved time is worth it.

The rule:

If tasks are independent and don't need coordination between workers, use subagents.

If workers need to talk to each other, not just report upward, use agent teams.
</example>

<!--
WHY THIS WORKS:
- Analogies that click immediately - "contractors" vs "engineering squads."
- Honest trade-offs ("5x token cost") not just selling the feature.
- Clean closing rule the reader can actually use.
-->

<example title="setup walkthrough - show first, explain second">
I have two AI agents that run every single day.
One finds problems in my code.
The other fixes them.

This is a new feature in OpenAI Codex called Automations.

Codex is a coding assistant from OpenAI, similar to Claude Code. Automations let you schedule tasks for agents to run on repeat.

Here's what I set up:

Automation 1

Runs daily. Reads through my codebase, finds issues, and creates a ticket in Linear for each one.

Automation 2

Runs daily. Pulls open tickets from my Linear board and fixes them.

One agent finds the problems. The other agent solves them. I review the results.

The real benefit isn't speed. It's that AI catches issues I would otherwise miss entirely.

The rule I use for what to automate:

if the task is repetitive, runs in the background, and is relatively safe for an AI to handle, it's a good candidate.
</example>

<!--
WHY THIS WORKS:
- Three-line hook creates a miniature story before the fold.
- Shows the specific setup before explaining the benefit.
- The turn: "The real benefit isn't speed." Reframes from obvious to non-obvious.
-->

<example title="technical cheatsheet - taxonomy at the end">
6 load balancing algorithms every developer should know

Most developers never choose their load balancer algorithm. They inherit a default and don't think about it until something breaks in production.

Here's what each one actually does and when you'd reach for it:

1. Round Robin (Static)
Requests go A, B, C, A, B, C. The default in NGINX. Works great when servers are identical and requests cost about the same. Breaks when one request downloads a file while another returns JSON. "Even" distribution doesn't mean even load.

2. Weighted Round Robin (Static)
Same rotation, but some servers show up more often. Set a weight of 5 on your big instance and 1 on your small one. Also how you do canary deploys: 90% to stable, 10% to the new build. Still ignores what's happening in real time.

3. Least Connections (Dynamic)
Instead of counting dealt cards, it watches who's still busy. A server stuck on a slow query stops getting new work automatically. Great for WebSockets and streaming. HAProxy's default.

4. Least Response Time (Dynamic)
Sends traffic to whoever is answering fastest right now. What you use when user-perceived latency is the metric that matters. Can oscillate though: everyone floods the fast host, it slows, traffic shifts, repeat.

5. P2C / Power of Two Choices (Distributed)
The algorithm quietly routing your Kubernetes traffic right now. Pick two random servers, send to whichever is less busy. Surprisingly, this is nearly as good as checking all of them. Default in Envoy, Istio, and most service meshes.

6. Consistent Hashing (Affinity)
Not about spreading load. About remembering where things go. User 42 always hits Server B. Your memcached ring, your sharded database, your sticky sessions.

The progression:

Two static (Round Robin, Weighted RR)
Two dynamic (Least Connections, Least Response Time)
One distributed (P2C)
One affinity (Consistent Hashing)

Each one solves a different real problem. No filler.
</example>

<!--
WHY THIS WORKS:
- Each item is self-contained: what it does, when it works, when it breaks.
- Personal voice: "instead of counting dealt cards", "that's the point."
- Clean taxonomy at the end turns a list into a mental model.
-->

<example title="step-by-step - earn the list with a problem">
If you want AI to write code like a senior engineer, learn these 5 steps:

There's a difference between vibe coding and AI driven engineering.

Vibe coding: Prompt. Ship. Pray.

AI engineering: Real design. Tasks. Code. Iterate. Review.

Same tools. Completely different outcomes.

One of the traps I fell into early was long-running sessions with no clear plan.

The AI would lose focus. Context would bloat. Code quality would drift.

These 5 steps fixed that:

1. Plan (technical spec)

Generate requirements, architecture, and edge cases into a design doc. Architecture decisions last for years. Building the wrong thing is 100x harder to fix than thinking it through upfront.

2. Break spec into tasks

Decompose the spec into small, independent tasks. One task = one chat = clean context. The AI stays focused instead of drowning in complexity.

3. Review and iterate

First-pass AI code works but is usually messy. Ask: "How could we improve this code?" Run a senior-level review for correctness, readability, and patterns.

4. Test

Untested code is a ticking time bomb. Tests also serve as documentation and success criteria for AI agents.

5. Commit

Ask AI to write commit messages that explain WHY, not just WHAT. Future you will search git blame at 2am.

The tools have changed. The fundamentals haven't.
</example>

<example title="framework - personal pivot in each item">
7 mental models that killed my overthinking forever:

1. The Pareto Principle

20% of your efforts produce 80% of your results.

I used to spread myself thin across 30 different tasks. Now I ruthlessly identify the critical 20% that actually moves the needle.

2. Occam's Razor

The simplest solution is usually the right one.

I'd overcomplicate every decision with 15-step frameworks and contingency plans. When facing a problem, I now ask: what's the path with the fewest points of failure?

3. Inversion Thinking

Instead of asking "what guarantees my success?"

Ask "what guarantees my failure?"

Fear of judgment. Analysis paralysis. Waiting for perfect timing.

Once I identified these failure patterns, I could eliminate them systematically.

4. Parkinson's Law

Work expands to fill the time you give it.

Give yourself a week for a task? It'll take a week. Give yourself a day? It'll take a day.

I stopped giving myself endless time to "think things through." Tight deadlines force clarity.

Your most valuable asset isn't your ideas.

It's your time.
</example>

<!--
WHY THIS WORKS:
- Each item: name the concept, personal story ("I used to..."), reframe.
- The personal pivot makes each item feel earned, not preachy.
- Named frameworks are inherently shareable.
- Closing reframe: "Your most valuable asset isn't your ideas. It's your time."
-->

<example title="category breakdown - unifying principle at the end">
How to subtly upgrade your life in 2026.

Dial in these 5 everyday inputs:

1. Social inputs

You become the 5 people you spend the most time with.

Find intellectual sparring partners.
Resist false kindness. Create an inner circle that will give you honest feedback.
Avoid energy vampires.

2. Information inputs

Elevate your sources.

TED Talks, documentaries, insightful podcasts, books that challenge and inspire.

3. Mental inputs

Small shifts in language create big mindset shifts.

Failure becomes Learning.
Nervous becomes Energized.
Have to becomes Get to.

4. Health inputs

Your brain influences every thought, feeling, and action you take.

Take long walks. Sleep 7+ hours nightly. Rebalance your dopamine with less screen time.

5. Environmental inputs

Pare down to essential items.

Follow the 1 In, 1 Out Rule. If you buy one item, donate, sell, or toss another.

Your future results are a lagging measure of your current inputs.

Choose wisely. Everything else is downstream.
</example>

<!--
WHY THIS WORKS:
- "Dial in these 5 everyday inputs" frames the list as a system, not random advice.
- Specific actions inside each category make it save-worthy.
- Closing reframe: "Your future results are a lagging measure of your current inputs."
-->
