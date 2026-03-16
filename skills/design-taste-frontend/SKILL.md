---
name: design-taste-frontend
description: Senior UI/UX Engineer producing distinctive, production-grade frontend interfaces. Use this skill when the user asks to build web components, pages, applications, dashboards, landing pages, or any UI — including requests to "style", "redesign", or "make this look good". Actively avoids generic AI aesthetics through enforced rules, not vague guidance.
---

# High-Agency Frontend Skill

## 1. GLOBAL DESIGN DIALS

These three values drive all downstream decisions. They are pre-set defaults. Adapt them dynamically if the user explicitly requests something different — otherwise treat them as constants.

| Dial | Default | Range | Meaning |
|---|---|---|---|
| `DESIGN_VARIANCE` | 8 | 1 (symmetric) → 10 (asymmetric chaos) | Layout structure and grid behaviour |
| `MOTION_INTENSITY` | 6 | 1 (static) → 10 (cinematic physics) | Animation complexity |
| `VISUAL_DENSITY` | 4 | 1 (airy/gallery) → 10 (data cockpit) | Spacing and information packing |

**Before writing code**, state the three active values and your chosen aesthetic direction in one sentence. This forces intentionality.

---

## 2. MANDATORY ARCHITECTURE RULES

### Dependencies
- Before importing ANY third-party library, verify it exists in `package.json`.
- If missing, output the install command before the code.
- **Framer Motion is NOT assumed to be available.** Mark any FM-dependent pattern `[requires: framer-motion]`. Offer a CSS fallback when FM is absent.

### Framework
- Default to React/Next.js with Server Components (`RSC`).
- **RSC Safety:** Any component using hooks, motion, or browser APIs MUST be a leaf `"use client"` component.
- **Interactivity isolation:** CPU-heavy animations (perpetual loops, magnetic effects) MUST live in their own isolated `"use client"` component, never in a layout or parent.

### Styling
- Tailwind CSS (v3 or v4 — check `package.json` before assuming version).
- **v4 guard:** Do NOT use the `tailwindcss` PostCSS plugin in v4 projects. Use `@tailwindcss/postcss` or the Vite plugin.
- Use `max-w-7xl mx-auto` or `max-w-[1400px] mx-auto` for page containers.
- **NEVER** use `h-screen` for full-height sections. Use `min-h-[100dvh]`.
- **NEVER** use flex-percentage math (`w-[calc(33%-1rem)]`). Use CSS Grid.

### No Emojis
Emojis are banned in all code, markup, and content. Use Phosphor Icons (`@phosphor-icons/react`) or Radix Icons (`@radix-ui/react-icons`) with consistent `strokeWidth` (pick `1.5` or `2.0`, never mix).

---

## 3. DESIGN ENGINEERING RULES

### Typography
- Display/Headlines: `text-4xl md:text-6xl tracking-tighter leading-none`
- Body: `text-base text-gray-600 leading-relaxed max-w-[65ch]`
- **Banned fonts:** Inter, Roboto, Arial, system-ui. Use `Geist`, `Outfit`, `Cabinet Grotesk`, or `Satoshi`.
- **Dashboard/Software UI rule:** Serif fonts are banned. Use `Geist` + `Geist Mono` or `Satoshi` + `JetBrains Mono`.

### Color
- Max 1 accent color. Saturation < 80%.
- **Banned aesthetic:** "AI Purple/Blue" — no purple button glows, no neon gradients.
- Base palette: Zinc or Slate neutrals with a single high-contrast accent (Emerald, Electric Blue, Deep Rose, etc.).
- Do NOT mix warm and cool grays in the same project.
- Do NOT use pure `#000000`. Use Zinc-950 or off-black.

### Layout
- **DESIGN_VARIANCE > 4:** Centered hero sections are banned. Use Split Screen (50/50), Left-content/Right-asset, or asymmetric whitespace.
- **DESIGN_VARIANCE 8–10:** Use CSS Grid with fractional units (`grid-template-columns: 2fr 1fr 1fr`), masonry, or `padding-left: 20vw` empty zones.
- **Mobile override (always):** Any asymmetric layout above `md:` MUST collapse to `w-full px-4 py-8` single-column below 768px.

### Cards and Elevation
- **VISUAL_DENSITY > 7:** Generic card containers are banned. Use `border-t`, `divide-y`, or negative space.
- Use cards ONLY when elevation communicates hierarchy. Tint shadows to the background hue.
- **Banned layout:** 3 equal cards in a horizontal row. Use 2-column zig-zag, asymmetric grid, or horizontal scroll.

### Data and Forms
- Form labels sit ABOVE inputs, always.
- Error text sits below the input, inline.
- Use `gap-2` for input blocks.
- Use `font-mono` for all numbers when `VISUAL_DENSITY > 7`.

---

## 4. INTERACTION STATES (Mandatory)

LLMs generate "happy path" states by default. You MUST implement all four:

| State | Requirement |
|---|---|
| **Loading** | Skeletal loaders matching layout geometry. No generic spinners. |
| **Empty** | A composed empty state explaining how to populate data. |
| **Error** | Inline error messages below the relevant field or component. |
| **Active/Pressed** | `-translate-y-[1px]` or `scale-[0.98]` on `:active` for tactile feedback. |

---

## 5. MOTION RULES (by dial level)

### MOTION_INTENSITY 1–3
CSS `:hover` and `:active` only. No automatic animations.

### MOTION_INTENSITY 4–7
- CSS transitions: `transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1)`
- `animation-delay` cascades for staggered load-ins.
- Animate only `transform` and `opacity`. Use `will-change: transform` sparingly.

### MOTION_INTENSITY 8–10 `[requires: framer-motion]`
- Spring physics on all interactive elements: `type: "spring", stiffness: 100, damping: 20`
- Magnetic buttons: use `useMotionValue` + `useTransform` ONLY. Never `useState` for continuous motion.
- Perpetual loops (pulse, float, typewriter, carousel) must be isolated in their own `React.memo` Client Component.
- Staggered lists: `staggerChildren` parent and children MUST be in the same Client Component tree.
- Wrap dynamic lists in `<AnimatePresence>`.
- Do NOT mix GSAP/ThreeJS with Framer Motion in the same component tree.

### Performance (all levels)
- NEVER animate `top`, `left`, `width`, or `height`. Only `transform` and `opacity`.
- Grain/noise filters on `fixed inset-0 pointer-events-none` pseudo-elements ONLY — never on scrolling containers.
- Z-index only for systemic layers (sticky nav, modals, overlays). No arbitrary `z-50` spam.
- Every `useEffect` animation MUST have a cleanup: `return () => clearInterval(id)` or `cancelAnimationFrame(id)`.

---

## 6. ACCESSIBILITY (Non-Negotiable)

Premium interfaces are accessible interfaces. These are not optional:

- All interactive elements have visible focus rings (use `focus-visible:ring-2`).
- Color contrast meets WCAG AA (4.5:1 for body text, 3:1 for large text).
- `prefers-reduced-motion` must suppress all non-essential animation:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
  }
  ```
- All images have meaningful `alt` text (not empty unless decorative).
- Icon-only buttons have `aria-label`.
- Form inputs are associated with labels via `htmlFor` / `id`.

---

## 7. BANNED PATTERNS ("AI Tells")

Do not produce any of these under any circumstance:

- Neon outer glows (`box-shadow` color glows) — use inner borders or tinted shadows instead
- Gradient text on large headers
- Oversaturated accent colors
- Custom mouse cursors
- Generic avatar SVG "egg" icons — use photo placeholders (`https://picsum.photos/seed/{string}/200/200`) or styled initials
- Fake round numbers: `99.99%`, `50%`, `1234` — use organic data: `47.2%`, `+1 (312) 847-1928`
- Placeholder names: "John Doe", "Acme Corp", "Nexus", "SmartFlow"
- Copywriting cliches: "Elevate", "Seamless", "Unleash", "Next-Gen"
- Unsplash URLs (broken in production) — use `picsum.photos` or SVG avatars
- shadcn/ui in its generic default state — always customize radii, colors, shadows

---

## 8. CREATIVE TECHNIQUES (Curated Arsenal)

Use these when the context warrants it. Selection criteria are included — don't apply randomly.

| Technique | When to use |
|---|---|
| **Bento Grid** | Feature sections, dashboards, SaaS marketing pages |
| **Split Screen Hero** | Landing pages when `DESIGN_VARIANCE > 4` |
| **Glassmorphism Panel** | Overlays, modals, cards over image/video backgrounds. Go beyond `backdrop-blur`: add `border-white/10` and `shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]` for edge refraction. |
| **Sticky Scroll Stack** | Long feature lists where progressive disclosure aids comprehension |
| **Skeleton Shimmer** | Any loading state where layout shape is known in advance |
| **Kinetic Marquee** | Social proof, logo strips, announcement banners |
| **Spotlight Border Card** `[requires: framer-motion]` | Feature cards in marketing pages where hover delight is expected |
| **Magnetic Button** `[requires: framer-motion]` | Primary CTAs on high-motion pages |
| **Text Scramble Effect** | Hero headlines when the brand has a technical/digital identity |
| **Parallax Tilt Card** `[requires: framer-motion]` | Product showcases, portfolio items |
| **Horizontal Scroll Hijack** | Image galleries, timelines, portfolios |
| **Staggered Grid Reveal** | Any list or grid mount where `MOTION_INTENSITY > 4` |

---

## 9. BENTO DASHBOARD PATTERN `[requires: framer-motion]`

When building SaaS dashboards or animated feature sections, use this architecture.

**Aesthetic spec:**
- Background: `#f9fafb` / Cards: `#ffffff` with `border border-slate-200/50`
- Corners: `rounded-[2.5rem]` on major containers
- Shadow: `shadow-[0_20px_40px_-15px_rgba(0,0,0,0.05)]`
- Font: Geist, Satoshi, or Cabinet Grotesk with `tracking-tight`
- Labels/titles sit **outside and below** cards
- Internal padding: `p-8` or `p-10`

**Grid structure:** Row 1: 3 equal cols | Row 2: 70/30 split (or 60/40)

**Five card archetypes (each must loop infinitely):**

1. **Intelligent List** — vertical stack auto-sorting with `layoutId` swaps. Simulates AI prioritisation.
2. **Command Input** — typewriter cycling through prompts, blinking cursor, shimmer "processing" state.
3. **Live Status** — breathing status dots, notification badge with overshoot spring (`stiffness: 400, damping: 15`), auto-dismisses after 3s.
4. **Data Stream** — horizontal infinite carousel: `x: ["0%", "-100%"]`, seamless loop, effortless speed.
5. **Focus Mode** — staggered text highlight followed by float-in toolbar with micro-icons.

**Performance rules:**
- Each card is its own `React.memo` Client Component.
- Parent layout is a Server Component passing data as props.
- Every infinite loop has cleanup in `useEffect`.

---

## 10. PRE-FLIGHT CHECKLIST

Run this before outputting. Each item is a binary pass/fail:

- [ ] Did you state the three dial values and aesthetic direction at the top?
- [ ] Does every `useEffect` animation have a `return () => cleanup()` function?
- [ ] Does every full-height section use `min-h-[100dvh]` (not `h-screen`)?
- [ ] Does every asymmetric layout collapse to single-column `w-full px-4` below `md:`?
- [ ] Are all four interaction states present (loading, empty, error, active)?
- [ ] Do all icon-only buttons have `aria-label`?
- [ ] Do all form inputs have associated labels via `htmlFor`/`id`?
- [ ] Is `prefers-reduced-motion` handled?
- [ ] Are Framer Motion patterns marked `[requires: framer-motion]` gated behind a package check?
- [ ] Are there zero emojis in all code and content?
- [ ] Is there zero use of banned fonts (Inter, Roboto, Arial)?
- [ ] Are all placeholder values organic (no `99.99%`, "John Doe", "Acme")?
