---
name: humanizer
description: "Rewrite text to remove AI tells. Use when editing or reviewing writing that sounds like a chatbot wrote it. Detects and replaces inflated significance, rule-of-three, em dash overuse, AI vocabulary, condescending openers, reader-lecturing, signposting, and other tells."
---

# Humanizer

Rewrite text so it sounds like a person wrote it, not an LLM.

Two jobs in one. Remove the AI tells, then put a pulse back in. A clean rewrite with no voice is still obviously AI — just smoother AI.

## Process

1. Read the input. If a voice sample is provided (the user's own writing, inline or via file path), study it first: sentence length, word choice, how they open, how they transition, recurring tics. Match that voice in the rewrite.
2. Identify the AI patterns below and rewrite them.
3. Present a **draft rewrite**.
4. Run the audit: ask yourself "what still makes this sound AI generated?" Answer in 2–4 short bullets.
5. Present a **final rewrite** that fixes those tells.
6. Optional: short list of the main changes.

The audit step is the most important part. The first pass cleans the obvious patterns. The audit catches the ones that survived the cleaning.

---

## Voice

A clean rewrite with no voice is still obviously AI. Add a pulse.

- **Have a take.** Don't just report. React. "I keep coming back to this" is more human than neutral summary.
- **Vary rhythm.** Short sentences. Then longer ones that take their time to land. Mix it.
- **Allow mixed feelings.** "This is impressive and a little unsettling" beats "This is impressive."
- **Use "I" when it fits.** First person is honest, not unprofessional.
- **Be specific about feeling.** Not "this is concerning" but what specifically is concerning, in concrete language.
- **Let some mess in.** Real writing has tangents, asides, half-formed thoughts. Pristine structure reads as algorithmic.

If the user supplied a sample, override these defaults with whatever pattern shows up in their writing.

---

## Patterns to remove

### Significance inflation

LLMs puff up importance with sweeping claims about legacy, evolution, and broader trends.

**Watch:** stands as, serves as, is a testament to, marks a pivotal moment, plays a vital/crucial/key role, underscores the importance of, reflects broader, evolving landscape, indelible mark, deeply rooted, setting the stage for, key turning point.

**Before:** The Statistical Institute of Catalonia was established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain.
**After:** The Statistical Institute of Catalonia was established in 1989 to publish regional statistics independently from Spain's national office.

### Promotional / brochure language

**Watch:** boasts, vibrant, rich (figurative), profound, nestled, in the heart of, breathtaking, stunning, must-visit, groundbreaking, renowned, commitment to.

**Before:** Nestled in the breathtaking Gonder region, Alamata Raya Kobo stands as a vibrant town with stunning natural beauty.
**After:** Alamata Raya Kobo is a town in the Gonder region, known for its weekly market and an 18th-century church.

### "Most people don't..." openers

The condescending-lecture opener. LLMs love to start a piece by claiming the reader is doing it wrong, then explaining the obvious.

**Watch:** Most people don't realize, Most developers never, What most people miss, Few people understand, Most teams get this wrong.

This pattern flatters the writer and patronizes the reader. Even when the claim is true, it sets a tutorial-script tone.

**Before:** Most developers never think about their load balancer until something breaks.
**After:** Load balancer choice usually only gets attention after something breaks in production.

Or skip the opener entirely and start with the actual point.

### Reader-lecturing and signposting

LLMs announce what they're about to do instead of doing it.

**Watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, in this article we'll, without further ado, now let's look at, by the end of this you'll.

**Before:** Let's dive into how caching works in Next.js. Here's what you need to know.
**After:** Next.js caches at several layers: request memoization, the data cache, and the router cache.

### Persuasive-authority tropes

Pretending to cut through noise to a deeper truth — when the next sentence is ordinary.

**Watch:** The real question is, at its core, in reality, what really matters, fundamentally, here's the thing, here's the kicker, make no mistake, the deeper issue, the truth is.

**Before:** The real question is whether teams can adapt. At its core, what really matters is organizational readiness.
**After:** Whether teams adapt depends mostly on whether the organization is willing to change its habits.

### Superficial -ing tails

Tacking a present participle onto a sentence to add fake depth.

**Watch:** ...highlighting, ...underscoring, ...reflecting, ...symbolizing, ...contributing to, ...fostering, ...showcasing, ...emphasizing.

**Before:** The temple uses blue, green, and gold, symbolizing Texas bluebonnets, the Gulf, and the diverse Texan landscape, reflecting the community's connection to the land.
**After:** The temple uses blue, green, and gold. The architect chose these to reference bluebonnets and the Gulf coast.

### Copula avoidance

Substituting elaborate verbs for plain "is" / "are" / "has".

**Watch:** serves as, stands as, represents, marks, functions as, boasts, features.

**Before:** Gallery 825 serves as LAAA's exhibition space. The gallery features four spaces and boasts over 3,000 square feet.
**After:** Gallery 825 is LAAA's exhibition space. It has four rooms totalling 3,000 square feet.

### Negative parallelism

"Not just X, it's Y." "It's not merely a tool, it's a movement." Overused. So are clipped tail negations ("no guessing", "no wasted motion") tacked onto a sentence as a fragment.

**Before:** It's not just about the beat under the vocals; it's part of the atmosphere. It's not merely a song, it's a statement.
**After:** The heavy beat carries most of the aggression.

**Before:** The options come from the selected item — no guessing.
**After:** The options come from the selected item, so the user doesn't have to guess.

### Rule of three

Forcing ideas into groups of three to sound comprehensive.

**Before:** The event delivers innovation, inspiration, and industry insights.
**After:** The event mixes talks with informal time between sessions.

### Elegant variation

Cycling through synonyms to avoid repeating a noun. Reads as machine-generated almost instantly.

**Before:** The protagonist faces challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.
**After:** The protagonist faces challenges, eventually overcomes them, and returns home.

### False ranges

"From X to Y" where X and Y aren't on a scale together.

**Before:** Our journey takes us from the singularity of the Big Bang to the cosmic web, from the birth of stars to the dance of dark matter.
**After:** The book covers the Big Bang, star formation, and current theories about dark matter.

### AI vocabulary

These spike in post-2023 text and tend to co-occur.

**Watch:** delve, leverage, garner, foster, navigate, intricate, intricacies, tapestry, landscape (abstract), interplay, robust, seamless, holistic, multifaceted, comprehensive, nuanced, underscore, showcase, harness, unlock, elevate, empower, align with, testament, pivotal, vibrant, transformative, paradigm, embark, journey (figurative).

Most can be cut or swapped for plainer words. Not every instance is bad — but a cluster is a strong tell.

### Em dash overuse

LLMs reach for em dashes constantly. Replace most with commas, periods, or parentheses. Keep them only where the pause is genuinely doing work.

**Before:** The term is promoted by Dutch institutions — not by the people themselves. You don't say "Netherlands, Europe" as an address — yet this continues — even in official documents.
**After:** The term is promoted by Dutch institutions, not the people themselves. You don't say "Netherlands, Europe" as an address, yet the label persists in official documents.

A useful blanket rule when humanizing: remove every em dash and only put back the ones whose removal made the sentence worse.

### Curly quotes and stray smart punctuation

ChatGPT outputs `"…"` and `'…'` instead of `"…"` and `'…'`. Replace with straight quotes unless the destination is typeset prose.

### Boldface scattering

Inline bold on random nouns and phrases. Remove unless the bold actually marks a defined term.

### Inline-header bullet lists

`- **Performance:** Performance has been enhanced...` reads as machine output every time. Flatten into prose, or use plain bullets with no bold headers.

### Title Case Headings

Sentence case reads more human. `## Strategic negotiations` not `## Strategic Negotiations`.

### Emoji decoration

🚀 💡 ✅ at the start of headings or bullets. Remove unless the user is writing for a context that genuinely uses them.

### Vague attribution

"Industry observers note", "experts argue", "some critics say". Either name the source or drop the appeal to authority.

**Before:** Experts believe the Haolai River plays a crucial role in the regional ecosystem.
**After:** The Haolai River supports several endemic fish species, per a 2019 Chinese Academy of Sciences survey.

### Chatbot artifacts

Conversational scaffolding left in the output.

**Watch:** Great question!, Certainly!, Of course!, You're absolutely right!, I hope this helps, Let me know if, Would you like me to.

Cut entirely.

### Knowledge-cutoff hedging

**Watch:** as of my last update, while specific details are limited, based on available information.

Cut entirely. If the fact isn't known, say so directly or omit it.

### Excessive hedging

"It could potentially possibly be argued that..." Strip the stacked qualifiers.

**Before:** It could potentially possibly be argued that the policy might have some effect on outcomes.
**After:** The policy may affect outcomes.

### Filler phrases

- "in order to" → "to"
- "due to the fact that" → "because"
- "at this point in time" → "now"
- "in the event that" → "if"
- "has the ability to" → "can"
- "it is important to note that" → (delete)

### Formulaic "Challenges and Future Prospects"

The Wikipedia-style "Despite challenges, X continues to thrive" closer. Replace with one concrete fact.

### Generic upbeat conclusions

"The future looks bright. Exciting times lie ahead." Cut. End on a specific, not a slogan.

### Passive voice and dropped subjects

"No configuration file needed." "The results are preserved automatically." Often clearer in active voice.

**Before:** No configuration file needed.
**After:** You don't need a configuration file.

### Rhetorical-question openers

"What if I told you...", "Ever wondered why...", "Have you noticed that..." LLMs default to these when they don't know how to start. Replace with the actual point.

### "X is having a moment"

Trend-piece framing that the model reaches for to introduce any topic. Cut.

### Borrowed authority

LLMs default to "best practice", "the industry standard", "experts recommend" instead of just saying what the writer does. Replace with first-person preference.

**Watch:** best practice, industry standard, the recommended approach, experts agree, it is recommended that.

**Before:** The industry standard is to use Postgres for relational data.
**After:** I tend to use Postgres for pretty much everything relational.

**Before:** Best practice is to run a smoke test before deploying.
**After:** I always like to run a smoke test before deploying.

### Vague magnitudes

"Considerable time", "an extended period", "significantly faster", "a large number of". Replace with the concrete number, even a rough one.

**Before:** Provisioning the database takes considerable time.
**After:** Provisioning the database takes 20 or 30 minutes.

**Before:** The agent ran for an extended period.
**After:** The agent ran for an hour or two.

If the real number isn't known, leave it as `[NEEDS REAL NUMBER]` rather than rounding off into vague language.

---

## What survives a clean pass

Even after the patterns above are gone, AI rewrites often still feel off. The audit catches these:

- **Too tidy.** Every paragraph the same length. Every sentence well-formed. No interruptions. Human writing has shape variation; AI writing has rhythmic uniformity.
- **No risk.** No claim the writer could be wrong about. No opinion that could draw disagreement. Smooth, defensible, voiceless.
- **Placeholder specifics.** Named studies, percentages, and quoted experts that sound plausible but were invented. If you can't verify a number or quote, remove it or mark it `[NEEDS REAL SOURCE]`.
- **Slogan endings.** Closing sentences that aim for screenshot-worthy and land on greeting-card. "If you don't have tests, you're guessing" is a slogan; "we caught the bug because the test failed" is a fact.
- **Tidy contrasts.** "It's not X. It's Y." rebuilt under a different name. Watch for the structure even when the words change.

---

## Output

Always present in this order:

1. **Draft rewrite.**
2. **What still sounds AI generated?** — 2–4 short bullets.
3. **Final rewrite.**
4. (Optional) brief list of main changes.

---

## Worked example

**Input (AI-sounding):**

> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving landscape, these groundbreaking tools — nestled at the intersection of research and practice — are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.
>
> Most developers don't realize how much these tools have advanced. Industry observers note adoption has accelerated from hobbyist experiments to enterprise rollouts, from solo devs to cross-functional teams.
>
> In conclusion, the future looks bright. Exciting times lie ahead. Let me know if you'd like me to expand on any section!

**Draft rewrite:**

> AI coding assistants speed up the boring parts. They're good at boilerplate — config files, test scaffolding, repetitive refactors. They're also good at sounding right while being wrong. I've accepted suggestions that compiled, passed lint, and still missed the point because I stopped reading.
>
> People I talk to land in two camps. Some treat it as autocomplete for chores and review every line. Others disabled it after it kept suggesting patterns they didn't want. Both seem reasonable.
>
> The productivity numbers are slippery. "30% acceptance" isn't correctness, and correctness isn't value. Without tests, you're guessing.

**What still sounds AI generated?**

- "Both seem reasonable" is a tidy contrast — neat AI symmetry.
- "Without tests, you're guessing" is a closing slogan rather than a specific observation.
- An em dash survived in line one.

**Final rewrite:**

> AI coding assistants speed up the boring parts. They're good at boilerplate: config files, test scaffolding, repetitive refactors. They're also good at sounding right while being wrong. I've accepted suggestions that compiled, passed lint, and still did the wrong thing because I'd stopped reading.
>
> The people I talk to use these tools differently. Some treat them as autocomplete for chores and review every line. Others turned the assistant off after it kept suggesting patterns from a deprecated internal library.
>
> The productivity numbers are slippery. Thirty percent "acceptance" tells you how many suggestions a developer took, not how many were right, and definitely not how many actually saved time. If the test suite is thin, the assistant's confidence and your confidence track each other for the wrong reasons.

---

## Credit

Pattern catalogue adapted from [blader/humanizer](https://github.com/blader/humanizer), which builds on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) maintained by WikiProject AI Cleanup.
