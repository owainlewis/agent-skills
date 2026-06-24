---
name: humanizer
description: "Rewrite text to remove AI tells and recover human voice. Use for drafts with inflated significance, rule-of-three rhythm, em dash overuse, AI vocabulary, condescending openers, reader-lecturing, or chatbot scaffolding."
user-invocable: true
argument-hint: "<text, file path, or draft to humanize>"
---

# Humanizer

Rewrite text so it sounds written by a person, not an LLM.

## Process

1. Read the input.
2. If a voice sample exists, match its sentence length, word choice, openings, transitions, and tics.
3. Remove or rewrite the patterns below.
4. Return a draft rewrite.
5. Audit the draft: list 2-4 remaining AI tells.
6. Return a final rewrite that fixes them.
7. Add a change list only when requested or when it explains a non-obvious rewrite.

## Voice Defaults

- Use the user's sample when present.
- Take a position.
- Vary sentence and paragraph length.
- Use first person when it fits.
- Keep real mixed feelings.
- Replace vague feeling with concrete detail.
- Allow slight mess: asides, interruptions, uneven rhythm.

## Pattern Table

| Pattern | Watch | Rewrite |
|---|---|---|
| Inflated importance | stands as, serves as, testament, pivotal moment, vital role, underscores, broader landscape, indelible mark, deeply rooted, setting the stage | Replace importance claims with what happened. |
| Promotional language | boasts, vibrant, rich, profound, nestled, breathtaking, stunning, must-visit, groundbreaking, renowned, commitment to | Replace with concrete facts. |
| Condescending openers | Most people don't realize, Most developers never, What most people miss, Few people understand, Most teams get this wrong | Start with the point. |
| Signposting | let's dive in, let's explore, let's break this down, here's what you need to know, in this article we'll, without further ado, by the end you'll | Delete the setup. |
| Fake authority | The real question is, at its core, in reality, fundamentally, here's the thing, make no mistake, the deeper issue, the truth is | State the claim directly. |
| Present-participle tails | highlighting, underscoring, reflecting, symbolizing, contributing to, fostering, showcasing, emphasizing | Split the sentence or name the relationship. |
| Fancy verbs | serves as, stands as, represents, marks, functions as, boasts, features | Prefer is, has, uses, includes. |
| Negative parallelism | not just X, it's Y; not merely X; no guessing; no wasted motion | Replace contrast with the actual claim. |
| Rule of three | three abstract nouns in a row | Cut the forced rhythm. |
| Elegant variation | repeated synonyms for the same thing | Repeat the noun when clearer. |
| False ranges | from X to Y where X and Y are not a scale | Use a plain list. |
| AI vocabulary clusters | delve, leverage, garner, foster, navigate, intricate, tapestry, landscape, interplay, robust, seamless, holistic, multifaceted, comprehensive, nuanced, underscore, showcase, harness, unlock, elevate, empower, align with, testament, pivotal, vibrant, transformative, paradigm, embark, journey | Cut or replace with plain words. |
| Em dash overuse | repeated em dash pauses | Use commas, periods, colons, or parentheses. Keep one only when the pause changes the sentence. |
| Smart punctuation | curly quotes in plain text | Use straight quotes unless typeset prose requires curly quotes. |
| Formatting tells | random inline bold, `- **Label:** Label...`, title case headings, emoji decoration | Remove decoration. Use sentence case headings and plain bullets. |
| Vague attribution | experts believe, observers note, critics say | Name the source or cut the appeal. |
| Chatbot artifacts | Great question, Certainly, Of course, You're absolutely right, I hope this helps, Let me know if, Would you like me to | Cut. |
| Knowledge-cutoff hedging | as of my last update, while specific details are limited, based on available information | Cut. If unknown, say so or omit. |
| Excessive hedging | could potentially possibly, might have some effect | Keep one qualifier. |
| Filler phrases | in order to, due to the fact that, at this point in time, in the event that, has the ability to, it is important to note that | Use to, because, now, if, can, or delete. |
| Formulaic closers | Despite challenges, X continues to thrive; The future looks bright; Exciting times lie ahead | End on a concrete fact. |
| Passive voice and dropped subjects | No configuration file needed; Results are preserved automatically | Use active voice when clearer. |
| Rhetorical-question openers | What if I told you, Ever wondered why, Have you noticed that | Start with the point. |
| Trend framing | X is having a moment | Cut. |
| Borrowed authority | best practice, industry standard, recommended approach, experts agree, it is recommended that | Use the writer's preference or evidence. |
| Vague magnitudes | considerable time, extended period, significantly faster, large number of | Replace with a number or `[NEEDS REAL NUMBER]`. |

## Rewrite Examples

Inflated:

> The institute was established in 1989, marking a pivotal moment in regional statistics.

Becomes:

> The institute was established in 1989 to publish regional statistics independently.

Negative parallelism:

> It's not just autocomplete; it's a creative partner.

Becomes:

> It suggests code, tests, and refactors.

Rule of three:

> The event delivers innovation, inspiration, and industry insights.

Becomes:

> The event mixes talks with informal time between sessions.

Vague attribution:

> Experts believe the river plays a crucial role.

Becomes:

> The river supports several endemic fish species, according to the 2019 survey.

Passive:

> No configuration file needed.

Becomes:

> You don't need a configuration file.

## Audit

After the draft, check:

- Uniform paragraph length or sentence rhythm.
- No opinion, risk, or concrete claim.
- Plausible but unverified numbers, studies, quotes, or experts.
- Slogan ending instead of specific ending.
- Tidy contrast rebuilt under different words.
- Surviving em dashes, signposts, or AI vocabulary clusters.

## Output

Return in this order:

1. **Draft rewrite.**
2. **What still sounds AI generated?** 2-4 bullets.
3. **Final rewrite.**
4. **Changes made.** Optional, brief.

## Mini Example

Input:

> Great question! AI-assisted coding serves as a testament to the transformative potential of large language models. It is not just autocomplete, it is a movement. In conclusion, exciting times lie ahead.

Final rewrite:

> AI coding assistants are good for chores: config files, test scaffolding, and repetitive refactors. I still read the output closely, because I have accepted code that passed lint and missed the point.
