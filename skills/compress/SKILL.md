---
name: compress
description: "Simplifies skills, prompts, and agent instructions to their most basic useful form: load-bearing verbs, nouns, constraints, examples, and checks. Use when the user asks to compress, simplify, shorten, tighten, de-noop, remove noise, or trim a prompt, spec, plan, or skill file."
user-invocable: true
argument-hint: "<file path or pasted instruction>"
---

# Compress

Simplify skills, prompts, and instructions to the smallest text that still changes agent behavior.

Keep load-bearing words.
Cut noise.
Use dense command language.

## Process

1. Choose the target from `$ARGUMENTS`, a pasted instruction, or the named file.
2. Extract the behavior contract: actions, inputs, outputs, tools, files, checks, constraints, defaults, edge cases, and stop conditions.
3. For each sentence or bullet, run the output-change test: if removed, would the agent's output or process likely change?
4. Delete it when the answer is no.
5. Rewrite it when it points at a real requirement but uses vague language.
6. Prefer load-bearing verbs: build, update, remove, keep, inspect, verify, return, skip, ask, stop, fail, retry, cite, preserve.
7. Prefer specific nouns: file path, schema, command, tool, source, output format, test, threshold, owner, state, error, example.
8. Preserve behavior. Do not weaken rules to make the text shorter.
9. Cut:
   - baseline agent virtues, such as "be thorough", "write clean code", "use good judgment", "make it easy to read", or "write a good commit message"
   - quality adjectives without criteria, such as "robust", "polished", "detailed", "comprehensive", or "production-ready"
   - motivational language
   - throat-clearing, rationale, and backstory that do not alter the task
   - restated rules
   - overlapping instructions
   - padding phrases
   - obvious preamble
   - hedging that does not change behavior
   - examples that restate a rule without adding format or edge-case value
10. Keep:
   - commands and constraints
   - concrete success checks
   - concrete examples that show a required format or edge case
   - file paths, exact names, identifiers, commands, and schemas
   - instructions that came from previous failures
   - defaults that resolve real ambiguity
11. If asked to update a file, replace it with the simplified version. Otherwise return only the simplified instruction.

## Rewrite

Rewrite weak phrases into commands only when the context supports a concrete behavior.
Otherwise delete them.

- "Be thorough" becomes "Inspect open review threads, failing checks, and linked issues before reporting ready" only when those sources are in scope.
- "Make the commit message very detailed" becomes "Use a conventional commit subject and include a body with motivation, tests, and risk" only when that exact commit format matters.
- "Make the implementation easy to read" becomes "Keep parsing, validation, and rendering in separate functions" only when that boundary is relevant to the change.
- "Create a polished final answer" becomes "Report changed files and checks run" only when final-report evidence matters.

## Output Shape

Use the simplest structure that preserves behavior:

- imperative bullets for rules
- numbered steps for required order
- short prose for one connected idea
- examples only for exact format or edge cases

## Rules

- Return the simplified version only unless the user asks for commentary.
- Merge overlapping sections.
- State a general rule and its exception together.
- Do not drop a rule to hit a word count.
- Do not keep motivational or quality language unless it creates a concrete test, priority, or constraint.
- Replace vague quality language with a behavior-changing rule only when the original intent clearly requires it.
- If simplification changes likely agent behavior, restore the load-bearing instruction.
