---
name: ia-format
description: "Format Markdown for iA Writer. Minimal, prose-first, almost no bold or italic."
user-invocable: true
argument-hint: "<file path or pasted text>"
---

# iA Format

Reformats Markdown so it reads well in iA Writer. iA Writer renders headings and prose beautifully; emphasis and decoration are noise.

## When to use

- Notes, scripts, briefs, posts, or reference docs read in iA Writer.
- Cleaning up agent-generated Markdown that overuses bold, italics, callouts, and rules.
- Any file under `context/`, `projects/`, `sops/`, or `scratch/` in this workspace.

## Process

1. Pick the target from `$ARGUMENTS`, a pasted block, or the named file.
2. Preserve meaning and structure. This is formatting, not rewriting.
3. Apply the rules below.
4. If a file path was given, overwrite it. Otherwise return the formatted text only.

## Rules

### Strip

- Bold (`**...**`) — remove unless it marks a true term-of-art definition.
- Italic (`*...*`, `_..._`) — remove unless it's a title, foreign word, or genuine stress that changes meaning.
- Blockquote callouts (`>`) used for emphasis — convert to plain prose. Keep blockquotes only for actual quotations.
- Horizontal rules (`---`) between sections — let headings do the work.
- Inline emoji and decorative symbols.
- Trailing labels like `**Why:**`, `**Note:**`, `**Critical:**` — fold into the sentence.
- "Bold-label + colon + text" bullets — rewrite as plain prose or a plain bullet.

### Keep

- Headings. Use `#`, `##`, `###`. One `#` per document.
- Lists, but only when the content is genuinely enumerable (steps, options, items). Convert decorative lists to prose.
- Code blocks and inline code for code, paths, commands, identifiers.
- Links in standard `[text](url)` form.
- Real quotations as blockquotes.

### Prose

- Prefer paragraphs over bullets when ideas connect.
- One blank line between paragraphs. Two blank lines before a new `##` section.
- Straight quotes (`"`, `'`), not curly.
- Em dash `—` with no surrounding spaces, or just use a comma or period.
- Sentence case for headings, not Title Case.

## Verification

- No bold or italic except where a rule above allows it.
- No `---` separators.
- Headings carry the structure; prose carries the content.
- Lists exist only where enumeration is real.
- Meaning unchanged.
