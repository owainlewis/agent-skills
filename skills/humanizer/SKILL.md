---
name: humanizer
description: "Rewrite any kind of writing so it sounds clear, human, and plain. Use for landing pages, emails, docs, posts, scripts, lessons, prompts, and messages that contain AI slop, purple prose, cliches, em dashes, hype, vague claims, or over-polished language."
user-invocable: true
argument-hint: "<text, file path, or draft to humanize>"
---

# Humanizer

Rewrite writing so it sounds like a clear person wrote it.

Use this for any type of writing:

- landing pages
- sales copy
- emails
- docs
- course lessons
- scripts
- social posts
- prompts
- internal notes
- product copy

The goal is not casual.
The goal is clear.

Use simple words. Use concrete examples. Cut anything that sounds profound but does not say a real thing.

## Process

1. Read the input.
2. Work out what the writer is trying to say.
3. Remove AI slop, purple prose, cliches, and fake depth.
4. Rewrite in plain English.
5. Check the rewrite against the audit.
6. Return only what is useful.

## Voice Defaults

- Use the user's voice sample when present.
- Use short, normal words.
- Prefer concrete nouns: email, task, note, file, meeting, customer, invoice, reply.
- Prefer concrete verbs: get, make, ask, send, read, write, save, run, check.
- Use first person when it fits.
- Allow normal human rhythm. Not every sentence needs to be polished.
- Be direct, but not robotic.
- Keep the real opinion if there is one.
- If a claim is missing proof, soften it or mark it as unknown.

## Hard Rules

- No em dashes.
- No purple prose.
- No cliches.
- No slogan endings.
- No vague magic.
- No fake profundity.
- No inflated claims.
- No "stop X, start Y" copy unless it says something concrete.
- No "not just X, but Y" unless the contrast is genuinely useful.
- No "unlock", "elevate", "supercharge", "transform", "leverage", "seamless", "robust", "holistic", "game-changing", or similar filler.
- No "let's dive in", "here's the thing", "the real question is", "at its core", or "in today's fast-paced world".
- No invented numbers, proof, stories, or results.

## AI Slop Patterns

| Pattern | Watch for | Fix |
|---|---|---|
| Tidy contrast | Stop X. Start Y. Not just X, but Y. | Say the actual action or result. |
| Fake depth | The real shift is. The deeper truth is. At its core. | State the point in normal words. |
| Purple prose | profound, breathtaking, vibrant, rich, nestled, tapestry | Replace mood with facts. |
| Abstract nouns | transformation, potential, impact, alignment, innovation | Name the thing the reader can picture. |
| Vague magic | unlock, elevate, empower, supercharge, 10x | Say what changes in the user's day. |
| Marketing negation | Not a toy. Not a demo. Not a prompt pack. | Show what the person will have. |
| Grand claim | This changes everything. The future is here. | Make the claim smaller and specific. |
| Persona fog | AI operator, business OS, agentic workflow | Define it with examples or cut it. |
| Motivational rhythm | short punchy line, short punchy line, profound closer | Use natural sentences. |
| Empty outcome | save time, work smarter, get more done | Name the saved task or decision. |
| Condescending opener | Most people do not realize. What people miss. | Start with the point. |
| Chatbot scaffolding | Great question. Certainly. I hope this helps. | Cut it. |
| Fancy verb | serves as, stands as, represents, showcases | Use is, has, uses, shows. |
| Vague source | experts say, many believe, studies show | Name the source or cut it. |

## Plain English Tests

Before returning the rewrite, ask:

1. Can the reader picture the thing?
2. Does this say what they will have, do, see, or decide?
3. Would a smart 10-year-old understand it?
4. Would a real person say this out loud?
5. Did we replace vague value with a concrete example?
6. Is there any slogan rhythm left?
7. Are there any em dashes?

## Rewrite Examples

Bad:

> Stop prompting from scratch. Start delegating real work.

Better:

> Instead of explaining your whole situation every time, give the assistant a job: check my calendar, read my notes, draft the follow-up, and tell me what needs my attention.

Bad:

> Not a toy chatbot. Not another prompt pack. Not AI productivity tips.

Better:

> By the end, you will have an assistant running. You can message it. It can read your workspace. It can follow written skills. It can draft work for you to review.

Bad:

> Unlock the power of AI agents.

Better:

> Give the assistant one job, such as preparing your day each morning. Then give it the files, tools, and rules it needs to do that job without you explaining everything again.

Bad:

> This course transforms the way you work by helping you build an agentic operating system.

Better:

> This course helps you build an assistant that checks your calendar, reads your tasks, and gives you a short plan for the day.

Bad:

> The institute was established in 1989, marking a pivotal moment in regional statistics.

Better:

> The institute was established in 1989 to publish regional statistics independently.

## Output

Default output:

1. `Rewrite:` the improved text.
2. `Changed:` 2 to 4 short notes if useful.

When the user asks why something is bad, return:

1. `Pattern:` the main issue.
2. `Why it fails:` one plain sentence.
3. `Rewrite:` the improved text.

Keep the answer short unless the user asks for detail.
