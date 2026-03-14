# LinkedIn Post Examples

Real posts. These are the ground truth for voice, structure, pacing, and length. Study them before writing — match the tone, not the topic.

<example title="explainer — explain first, then why it matters">
OpenAI just quietly released a feature that could change how developers work.

It's called Automations and it's part of their coding tool, Codex.

Codex is an AI coding assistant. You give it a task in plain English — like "fix this bug" or "review this code" - and it does the work for you.

Automations take that one step further.

Instead of asking Codex to do something once, you can set it to run the same task on a schedule. Every morning. Every hour. Whatever you want.

You write a prompt. You pick a schedule. Codex runs it automatically in the background.

Here's a real example from their docs:

You tell Codex: "Look at my last 24 hours of code commits, find any bugs I introduced, and fix them."

It runs that every day. You wake up, open your inbox in the app, and the fixes are already there waiting for you to review.

That's a big deal. Here's why.

Automations allow you to replace complex automation tools with natural language and the intelligence of agents.

It takes you out of the loop and enables you to become much more effective.

It's a simple concept that scales incredibly well and unlocks new possibilities for using AI in your work or business.

A few things worth knowing:

It runs locally on your machine. Codex needs to be open, and your project files need to be on your computer.

Each run starts fresh. In Git projects, it creates a separate copy of your code so it doesn't mess with what you're working on.

I'd use this for automating anything that you'd normally have to manually prompt an agent to do.

If you're a developer or business owner, this is worth paying attention to.
</example>

<!--
WHY THIS EXAMPLE WORKS:
1. Explains what Codex IS before explaining what Automations do. Reader never feels lost.
2. Uses a concrete example ("look at my last 24 hours of commits") instead of abstract claims.
3. The "why it matters" section comes AFTER the reader already understands the feature.
4. No numbered list forced onto it — the structure follows the explanation naturally.
5. Practical details (runs locally, starts fresh) answer real questions without feeling like a spec sheet.

KEY PATTERN: Explain first. Assume the reader hasn't heard of the tool. Make them understand it before you tell them why they should care. Most posts do this backwards — they hype the impact before the reader even knows what the thing does.
-->

<example title="comparison — numbered sections with analogies">
Subagents vs agent teams explained:

Claude Code has two ways to coordinate work:

Here's when to use each.

Agent teams is a new feature for Claude Code that lets you run multiple Claude Code instances that can work together as a team.

Here's how teams differ from subagents.

1. Subagents are contractors

You tell one agent to delegate work. It hands tasks to workers. Workers complete them and report back.

The parent orchestrates everything. Workers never talk to each other.

Token efficient. Results get summarised back to the parent instead of keeping full context.

2. Agent teams are engineering squads

Each teammate is its own Claude Code session with its own context window.

They share a task list. They message each other directly. They self-coordinate.

A reviewer can read code and send notes straight to a working agent. No middleman copying context back and forth.

Best for: Work that spans layers. Frontend, backend, and tests that all need to move together. Long running sessions without human in the loop or cases where you'd normally copy context between sessions manually.

3. Token cost is real

Agent teams cost roughly 5x the tokens. Every teammate is a separate Claude instance.

You wouldn't use this for a bug fix.

But for a complex build where you'd otherwise be relaying messages between agents yourself, the saved time is worth it.

4. Teams challenge assumptions

One interesting thing is negotiation.

Backend and frontend agents can discuss or debate implementation details.

5. The ceiling is high

A researcher at Anthropic used 16 parallel Claude agents to build a C compiler in Rust - 100,000 lines of code, capable of compiling the Linux kernel.

The rule:

If tasks are independent and don't need coordination between workers, use subagents.

If workers need to talk to each other, not just report upward, use agent teams.
</example>

<!--
WHY THIS EXAMPLE WORKS:
1. Hook from hooks.md — matches the "X vs Y explained" pattern. Performed well.
2. Analogies that click immediately — "contractors" vs "engineering squads." Reader gets the mental model before the technical detail.
3. Numbered sections earn their place — each one covers a distinct angle (what they are, cost, coordination, scale).
4. Concrete stat anchors it — "16 parallel Claude agents, 100,000 lines of code, C compiler in Rust." Specific, memorable, shareable.
5. Clean closing rule — simple if/then decision framework the reader can actually use.
6. Practical detail (5x token cost) shows honest trade-offs, not just selling the feature.

KEY PATTERN: When comparing two things, give each one an analogy first, then get into the details. The analogy does the heavy lifting — the reader understands the difference before they read a single technical sentence.
-->

<example title="setup walkthrough — hook with intrigue, then show the system">
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

Every fix is a bug your users never see, a vulnerability that gets closed before it's exploited, a breaking change caught before it hits production.

The real benefit isn't speed. It's that AI catches issues I would otherwise miss entirely.

The rule I use for what to automate:

if the task is repetitive, runs in the background, and is relatively safe for an AI to handle, it's a good candidate.

Other things this works for: dependency updates, documentation checks, release notes, security scanning, standup preparation.
</example>

<!--
WHY THIS EXAMPLE WORKS:
1. Three-line hook uses the visible fold perfectly — "I have two AI agents that run every single day. / One finds problems in my code. / The other fixes them." All three lines visible before "see more." Reader has to click.
2. Explains the tool immediately after the hook — doesn't assume the reader knows what Codex or Automations are.
3. Shows the specific setup (Automation 1, Automation 2) before explaining the benefit. Show first, explain second.
4. The turn: "The real benefit isn't speed. It's that AI catches issues I would otherwise miss entirely." Reframes from obvious benefit (fast) to non-obvious benefit (coverage).
5. Ends with a practical rule the reader can apply: "if the task is repetitive, runs in the background, and is relatively safe for an AI to handle."
6. List of other use cases at the end gives save-worthy value without forcing a numbered list.

KEY PATTERN: The 3-line hook creates a miniature story (characters + conflict + resolution) in the space before the fold. The reader sees agents, a problem, and a fix — all before clicking "see more." This drove 9 reposts.
-->

<example title="step-by-step">
If you want AI to write code like a senior engineer, learn these 5 steps:

There's a difference between vibe coding and AI driven engineering.

Vibe coding: Prompt. Ship. Pray.

AI engineering: Real design. Tasks. Code. Iterate. Review.

Same tools. Completely different outcomes.

I've been using Claude Code since it first released. One of the traps I fell into early was long-running sessions with no clear plan.

The AI would lose focus. Context would bloat. Code quality would drift.

These 5 steps fixed that:

1. Plan (technical spec)

Generate requirements, architecture, and edge cases into a design doc. Think upfront about what you're doing.

Architecture decisions last for years. Senior engineers spend time on design for good reason - building the wrong thing is 100x harder to fix than thinking it through upfront.

2. Break spec into tasks

Decompose the spec into small, independent tasks written specifically for agents to execute.

One task = one chat = clean context. The AI stays focused instead of drowning in complexity.

3. Review and iterate

First-pass AI code works but is usually messy. Ask: "How could we improve this code?"

Run a senior-level review for correctness, readability, and patterns.

4. Test

Untested code is a ticking time bomb. Tests also serve as documentation and success criteria for AI agents.

Generate tests for happy path, edge cases, and error handling.

5. Commit

Ask AI to write commit messages that explain WHY, not just WHAT.

Future you will search git blame at 2am. A good commit message is a gift to yourself.

The tools have changed. The fundamentals haven't.

What's your workflow?
</example>

<example title="listicle">
Building a startup is harder than most people can imagine.

15 lessons in the order I learned them:

I've built and sold multiple 8-figure businesses.

Each one taught me something the previous one couldn't.

Here's what nobody tells you:

1. Product comes before everything else

If you build something mediocre and market it well, you'll just burn cash on churn.
If you build something people love, they'll become your product champions.

2. Your network will carry you forward

I haven't built any of my businesses alone.
Every business I've scaled came from relationships built years before I needed them.

3. Founder-led personal brand is distribution

3M+ followers didn't happen to me overnight.
But when we launched Searchable, we had distribution to the exact people who needed it.

4. Speed is a competitive advantage

We hit $75K MRR in 20 days because we moved fast.
Ship, test, learn, iterate. No endless planning cycles.

5. Focus on pre-validated markets

We didn't invent AEO. We studied what was already working, took the best parts, and made it 10x better.
You don't have to completely reinvent the wheel to succeed.

6. Give away value for free

High-value free content is the best sales tool you have.
It gains trust at scale, and if done correctly, can convert highly.

7. Listen to the first 100 users obsessively

We gave beta access to 100 people in exchange for daily feedback.
Product-market fit doesn't happen by accident.
</example>

<example title="rule / declaration">
Rule for life:

You'll never be ready. Start anyway.

Over the years, I've learned you just need to get started.

What happens when you do?

1. Your first attempt is always going to be rough:

- You'll ship code that breaks production
- The client call could be a total disaster
- You'll price your work way too low

The second attempt will be better. The third better still.

2. Action reveals problems that planning can't.

As someone who overthinks a lot, I know you're far better off taking a small step - you'll learn faster that way.

Plans are useful, but real learning happens when you act.

3. You build confidence by doing, not by thinking things through.

Want to become a great software engineer? Write a lot of code. Build software.

Want to get better at sales? Do more sales calls.

The more you do things, the more your confidence grows.

4. Imposter syndrome is self awareness

Feel like an imposter? That's actually a great sign - you're self-aware enough to see the gaps in your abilities. When you can see the gaps, you can close them.

Don't worry about mistakes when you first start out.

Book the call.
Take on the project you're scared of.
Take your first sales call.
Have the conversation you're avoiding.

The only way to make progress is to start.
</example>

<example title="technical cheatsheet — 130 reposts, numbered list with personal takes">
6 Load Balancing Algorithms Every Developer Should Know

Most developers never choose their load balancer algorithm. They inherit a default and don't think about it until something breaks in production.

Here's what each one actually does and when you'd reach for it:

1. Round Robin (Static)
Requests go A, B, C, A, B, C. The default in NGINX. Works great when servers are identical and requests cost about the same. Breaks when one request downloads a file while another returns JSON. "Even" distribution doesn't mean even load.

2. Weighted Round Robin (Static)
Same rotation, but some servers show up more often. Set a weight of 5 on your big instance and 1 on your small one. Also how you do canary deploys: 90% to stable, 10% to the new build. Still ignores what's happening in real time.

3. Least Connections (Dynamic)
Instead of counting dealt cards, it watches who's still busy. A server stuck on a slow query stops getting new work automatically. The first dynamic algorithm most developers reach for. Great for WebSockets and streaming. HAProxy's default.

4. Least Response Time (Dynamic)
Sends traffic to whoever is answering fastest right now. What you use when user-perceived latency is the metric that matters. AWS ALB calls their version "least outstanding requests." Can oscillate though: everyone floods the fast host, it slows, traffic shifts, repeat.

5. P2C / Power of Two Choices (Distributed)
The algorithm quietly routing your Kubernetes traffic right now. Pick two random servers, send to whichever is less busy. Surprisingly, this is nearly as good as checking all of them. No herd stampede where every balancer picks the same "best" node. Default in Envoy, Istio, and most service meshes.

6. Consistent Hashing (Affinity)
Not about spreading load. About remembering where things go. User 42 always hits Server B. That's the point. Your memcached ring, your sharded database, your sticky sessions. Add a server and only its neighbors' keys move instead of reshuffling everything.

The progression:

Two static (Round Robin, Weighted RR)
Two dynamic (Least Connections, Least Response Time)
One distributed (P2C)
One affinity (Consistent Hashing)

Each one solves a different real problem. No filler.
</example>

<!--
WHY THIS EXAMPLE WORKS:
1. Hook declares the list count and audience upfront. "6 algorithms every developer should know" sets expectations immediately.
2. Setup earns the list: "Most developers never choose... they inherit a default." Reader thinks "that's me" and keeps reading.
3. Each item is self-contained: what it does, when it works, when it breaks. No item depends on reading another.
4. Concrete examples instead of definitions: "Requests go A, B, C, A, B, C" beats "distributes requests sequentially."
5. Personal voice woven in: "instead of counting dealt cards", "that's the point", "no filler." Not a textbook.
6. Clean taxonomy at the end (static/dynamic/distributed/affinity) gives the reader a framework to remember all six.
7. "Even distribution doesn't mean even load" is the kind of reframe that gets screenshots and reposts.

KEY PATTERN: Technical cheatsheet format. Each numbered item follows the same rhythm: what it does, one concrete detail, when it breaks or shines. The closing taxonomy turns a list into a mental model. 130 reposts.
-->

<example title="API patterns cheatsheet — numbered list with personal experience">
Six API patterns every software developer should know.

(Explained simply)

Here is what each one actually does and when it is the right call.

1. REST

Standard HTTP methods with stateless, cacheable, resource-based design. Client sends GET /users, server returns JSON.

Pretty much my default for most things (if it ain't broken ...).

Best fit: public APIs, CRUD apps, mobile backends.

2. GraphQL

Clients request exactly the data they need through a single endpoint. Typed schema prevents over-fetching. I haven't used this much personally but it solves a real problem when your frontend is stitching together five REST calls to render one page.

Best fit: complex frontends, mobile apps, data aggregation.

3. Webhooks

Reverse HTTP callbacks triggered by events. Your server registers a URL and gets notified automatically. Stripe fires an event, your server receives the payload.

Best fit: payment notifications, CI/CD, third-party integrations.

4. gRPC

Google's high-performance RPC using Protocol Buffers and HTTP/2 with bidirectional streaming. Binary format instead of JSON. Not something I reach for often, but at massive scale between internal services it makes a big difference.

Best fit: microservices, real-time streaming, polyglot systems.

5. WebSockets

Full-duplex communication over a persistent TCP connection. Both sides can send messages at any time.

Best fit: chat, live dashboards, multiplayer games, collaborative editors.

6. SSE

Server-Sent Events over a single HTTP connection. One-way stream from server to client. This is how most LLM APIs stream tokens back to you. I use SSE all the time when building AI applications. Simple, reliable, and works over standard HTTP.

Best fit: AI streaming, live feeds, notifications, stock tickers.

REST works well for CRUD. But if you need real-time data, WebSockets or SSE are built for that (e.g. AI apps where tokens stream to the user). If your frontend is hitting five endpoints to render one page, GraphQL solves that. If your services talk to each other millions of times per second, gRPC handles it at a fraction of the overhead.
</example>

<!--
WHY THIS EXAMPLE WORKS:
1. Same "N patterns every developer should know" hook format as the load balancer post. Proven structure.
2. Personal experience mixed into technical explanations: "Pretty much my default", "I haven't used this much personally", "I use SSE all the time." Makes it honest, not encyclopedic.
3. Each item has the same structure: what it is, one concrete example, best fit. Easy to scan.
4. Closing paragraph ties it together with decision logic: "if you need X, use Y." Gives the reader a decision framework, not just a list.
5. "(Explained simply)" in the hook sets the tone and lowers the barrier for non-expert readers.

KEY PATTERN: The personal asides ("I haven't used this much personally but...") build trust by admitting gaps. Readers share cheatsheets that feel honest over ones that feel like documentation.
-->
