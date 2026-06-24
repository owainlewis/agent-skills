---
name: explain-visually
description: "Creates a responsive HTML explainer with source-grounded copy, teaching diagrams, and browser-verified layout. Use when the user asks to visualize, diagram, or explain something as an HTML artifact."
user-invocable: true
argument-hint: "<repo, spec, PR, architecture, concept, or source material>"
---

# Explain Visually

Create a human-facing HTML artifact that explains one idea through source-grounded copy, teaching diagrams, and browser-verified layout.

## Workflow

### 1. Understand

- Read the source.
- Identify audience, core idea, moving parts, decisions, tradeoffs, and takeaway.
- Ground claims in source facts.
- Prefer concrete names, paths, commands, interfaces, examples, and observed behavior.
- Define jargon before using it.

### 2. Outline

Plan:

- core lesson
- why the old way fails
- new mental model
- how it works
- concrete example
- next action
- diagrams needed
- source facts used
- omissions

### 3. Build

- Create a responsive HTML explainer.
- Use Tailwind CSS via CDN.
- Use custom CSS only for fonts, theme tokens, diagrams, and small refinements.
- Use slide-like desktop sections and stacked mobile sections.
- Do not preserve fixed 16:9 on mobile.
- Use simple concrete titles.
- Use short explanatory copy.
- Use source-grounded statements, not slogans.
- Use SVG diagrams that teach the idea.
- Use responsive type, spacing, and visual hierarchy.
- Keep one idea per section.

### 4. Verify

Run `browser-verify`.
Check desktop and mobile.
Fix overflow, overlap, clipped text, unreadable scale, cramped spacing, and broken responsive layout.

## Style

- Body/UI font: Bricolage Grotesque.
- Display font: Instrument Serif.
- Palette: warm paper, dark ink, muted rust, restrained teal.
- Hero title: prefer `md:text-7xl`; avoid `lg:text-9xl` unless very short.
- Split content before cramming.
- Mobile: natural-height sections, single-column grids, compact display type, readable text, fitted diagrams.
- SVG labels: use `text-anchor`, `dominant-baseline`, explicit font sizes, and enough padding.

## Rules

- Explain, do not decorate.
- Teach before summarizing.
- First screen states the core lesson in plain language.
- Show at least one transformation: before/after, problem/solution, vague/clear, or hidden/visible.
- Give one reusable mental model.
- Include one concrete source example.
- End with the reader's next action.
- Use only source-supported factual claims.
- Center and contain diagram text.
- Do not use `overflow: hidden` to hide layout defects.
- The artifact fails if text overlaps, clips, or overflows.
