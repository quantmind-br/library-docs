---
title: Craft a Compelling Story
url: https://cis-docs.bmad-method.org/how-to/storytelling/
source: sitemap
fetched_at: 2026-04-08T11:33:53.698440476-03:00
rendered_js: false
word_count: 402
summary: This document outlines a structured storytelling workflow designed to help users craft compelling narratives for various purposes, from pitch decks to marketing content. It guides the user through defining purpose, understanding their audience, selecting an appropriate narrative framework, crafting story elements, and adapting the final output for a specific platform.
tags:
    - storytelling
    - narrative-crafting
    - communication-strategy
    - audience-analysis
    - content-development
    - pitch-decks
category: guide
---

Use the `storytelling` workflow to craft compelling narratives using proven story frameworks, emotional psychology, and platform-specific adaptation.

- Creating product or brand narratives
- Writing pitch decks or investor presentations
- Developing user stories or case studies
- Communicating change or vision
- Crafting marketing content or campaigns

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- Purely technical documentation
- Simple factual reporting without narrative need
- Extremely short formats (headlines, taglines)

Start a fresh chat and load the Storyteller:

### 2. Define Your Story Purpose

[Section titled “2. Define Your Story Purpose”](#2-define-your-story-purpose)

Sophia will ask about your story. Be clear about intent:

**Good story purposes:**

- “Persuade investors that our market opportunity is massive”
- “Inspire employees to embrace a new direction”
- “Help users understand how our product changes their life”
- “Explain a complex technical concept in relatable terms”

**Less effective:**

- “Write about our product” (no clear purpose)
- “Tell our company story” (too vague)

### 3. Understand Your Audience

[Section titled “3. Understand Your Audience”](#3-understand-your-audience)

Sophia explores who you’re speaking with:

Audience QuestionWhy It Matters**Who are they?**Shapes language, tone, references**What do they believe now?**Identifies gap to bridge**What do you want them to feel?**Emotional journey design**What should they do?**Call to action clarity

### 4. Choose Your Framework

[Section titled “4. Choose Your Framework”](#4-choose-your-framework)

Sophia selects from 25 story frameworks:

FrameworkBest For**Hero’s Journey**Transformation, overcoming obstacles**StoryBrand**Customer-centric marketing**Three-Act Structure**Classic narrative arcs**Before-After-Bridge**Simple problem-solution stories**The Pixar Pitch**Emotional, character-driven narratives**Inverted Pyramid**News-style, impact-first

### 5. Craft Your Narrative

[Section titled “5. Craft Your Narrative”](#5-craft-your-narrative)

Sophia guides you through:

Story ElementWhat You’ll Create**Hook**Opening that grabs attention**Characters**Relatable protagonists and antagonists**Conflict**The problem or tension**Journey**The path through struggle**Resolution**The satisfying outcome**Transformation**How the world changed

### 6. Adapt to Platform

[Section titled “6. Adapt to Platform”](#6-adapt-to-platform)

Sophia tailors the story for where it will live:

- **Pitch deck** — Concise, slide-by-slide narrative
- **Blog post** — Scannable, with narrative arc
- **Video script** — Visual storytelling with dialogue
- **Social media** — Micro-narratives for feed format
- **Email** — Personal, direct storytelling

Output saved to `_bmad-output/story-{date}.md`:

SectionContents**Story Framework**Which structure was used and why**Audience Profile**Who the story is for**Emotional Arc**The journey you want them to feel**Complete Narrative**Full story with vivid details**Character Development**Voice, motivation, transformation**Platform Adaptation**Formatted for your chosen medium**Impact Plan**How to measure effectiveness

```text

You: /cis-storytelling
Sophia: 📖 Greetings, traveler. What tale shall we weave?
You: We need to tell our product story for a pitch deck.
Our app helps people manage anxiety.
Sophia: Ah, a noble quest. Tell me—who suffers from
this anxiety, and how does your solution become
the hero they've been waiting for?
You: [Explains user struggle and solution]
Sophia: [Selects Hero's Journey framework]
Let us craft your protagonist—someone whose
anxiety keeps them from living fully.
[Develops character and emotional stakes]
[Creates narrative arc with tension and release]
[Adapts story for pitch deck format—slide by slide]
```

After storytelling:

- Use **presentation design** (coming soon) to create visual decks
- Apply **innovation strategy** (`/cis-innovation-strategy`) to strengthen business narrative
- Use **brainstorming** (`/cis-brainstorm`) to generate story variations

## Providing Context

[Section titled “Providing Context”](#providing-context)

For best results, provide brand or product context via the `--data` flag:

```bash

workflowcis-storytelling--data/path/to/brand-guidelines.md
```

Sophia will use this context to maintain brand voice and consistency.