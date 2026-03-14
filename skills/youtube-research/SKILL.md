---
name: youtube-research
description: "Research a YouTube video topic. Searches the competitive landscape, identifies your angle, generates data-informed titles, and recommends format and length. Use when brainstorming video ideas, researching a topic, or deciding what to make next."
---

# YouTube Research

Research a topic and find the angle that makes your video worth watching.

## Before starting, read:
- `references/title.md` — Title patterns and rules

## Tool

This skill has a Python script that queries the YouTube Data API v3.

```bash
# Search for videos on a topic
uv run youtube.py search "AI agents" --max 10

# Search recent videos only
uv run youtube.py search "AI agents" --max 10 --days 30

# Sort by view count
uv run youtube.py search "AI agents" --order view_count

# Get a creator's recent videos with outlier analysis
uv run youtube.py creator @mkbhd --days 90
```

Requires `YOUTUBE_API_KEY` environment variable.

## Inputs

Required: A topic or video idea from the user.

Optional:
- Reference material (docs, blog posts, changelogs)
- Specific demos or tools they plan to show
- Target audience level

## Process

### 1. Search YouTube

Use the script to find existing videos on this topic. Run 2-3 queries with different phrasings to get broad coverage.

```bash
uv run youtube.py search "topic phrase 1" --max 10
uv run youtube.py search "topic phrase 2" --max 10
```

### 2. Build Competitor Table

From the search results, select the top 5-8 most relevant videos:

```
| # | Title | Views | Channel | What They Covered | What They Missed |
|---|-------|-------|---------|-------------------|-----------------|
```

Look for outlier titles with unusually high views relative to the channel's size.

### 3. Analyze Top Creators

If a specific creator dominates the results, pull their channel to understand their patterns:

```bash
uv run youtube.py creator @channelhandle --days 90
```

Look at their outlier scores to see which titles and topics over-performed.

### 4. Identify the Gap

Find the angle that makes this video worth watching despite existing content. Common gap types:
- **Default approach everywhere** — Everyone teaches the same basic method. Show the production-ready version.
- **Unanswered question** — Competitors demo the happy path but skip failure cases, limitations, or real-world tradeoffs.
- **Unique advantage** — You have a workflow, result, or perspective nobody else has shared.
- **Outdated content** — The landscape changed and existing videos are stale.

State the gap in one sentence: "Every video on X covers Y, but nobody shows Z."

### 5. Key Points

List 3-5 key points the video should cover. Mark each as:

- **[TABLE STAKES]** — Must cover for completeness, but competitors already do this. Keep brief.
- **[DIFFERENTIATOR]** — This is the gap. This is why they watch YOUR video.

Order by viewer need, not by importance. Build from simple to complex.

### 6. Generate Title Options

Read `references/title.md` for the complete title SOP.

Write 5 title options informed by:
- Outlier data from the competitor table
- The psychological trigger that fits the gap
- The traffic source (browse, search, or both)

Recommend the strongest title with reasoning. Provide 2 backups.

### 7. Recommend Format and Length

Based on the topic and gap, recommend:
- **Format:** Workflow Demo, Conceptual Explainer, Feature Coverage, or Opinion/Analysis
- **Target length:** With reasoning

## Output

Present the research to the user. If they want it saved, write to `{slug}-research.md` in the current directory:

```markdown
# Research: {Topic}

## Competitor Analysis

{Competitor table}

### Outlier Titles
{Which titles over-performed and why}

### Creator Analysis
{If a creator was analyzed, key patterns from their channel}

## The Gap

{One sentence: what's missing from existing content}

## Key Points

1. [TABLE STAKES] {point}
2. [DIFFERENTIATOR] {point}

## Title Options

| # | Title | Pattern | Trigger | Notes |
|---|-------|---------|---------|-------|

**Recommended:** {title} — {reasoning}
**Backups:** {title}, {title}

## Format & Length

**Format:** {type}
**Target:** {X} minutes — {reasoning}
```
