---
title: Develop an Innovation Strategy
url: https://cis-docs.bmad-method.org/how-to/innovation-strategy/
source: sitemap
fetched_at: 2026-04-08T11:33:53.140726701-03:00
rendered_js: false
word_count: 370
summary: This document outlines a systematic workflow, using various strategic frameworks like Blue Ocean Strategy and JTBD, designed to help users identify significant business disruption opportunities rather than mere feature improvements.
tags:
    - innovation-strategy
    - business-modeling
    - market-analysis
    - strategic-frameworks
    - disruption-opportunities
    - competitive-advantage
category: guide
---

Use the `innovation-strategy` workflow to identify disruption opportunities and architect business model innovation using proven strategic frameworks.

- Exploring new market opportunities or pivots
- Analyzing competitive threats and disruption potential
- Designing business models for new ventures
- Seeking sustainable competitive advantage
- Evaluating whether an idea has strategic merit

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- Incremental feature improvements (use brainstorming instead)
- Purely technical optimizations
- Well-established markets with clear rules

Start a fresh chat and load the Innovation Strategist:

### 2. Define Your Strategic Question

[Section titled “2. Define Your Strategic Question”](#2-define-your-strategic-question)

Victor will ask about your innovation challenge. Frame it strategically:

**Good strategic questions:**

- “Where are the disruption opportunities in our market?”
- “What business models could work for this idea?”
- “How can we create uncontested market space?”
- “What’s our sustainable competitive advantage?”

**Less effective:**

- “What features should we build?” (product strategy, not innovation strategy)
- “How do we beat competitor X?” (tactical, not strategic)

### 3. Analyze the Market Landscape

[Section titled “3. Analyze the Market Landscape”](#3-analyze-the-market-landscape)

Victor guides you through:

Analysis AreaWhat You’ll Explore**Market forces**Trends, shifts, emerging customer needs**Competitive dynamics**Who’s winning, why, and where gaps exist**Value chain**Where value is created and captured**Assumptions**Industry “rules” that might be broken

### 4. Apply Strategic Frameworks

[Section titled “4. Apply Strategic Frameworks”](#4-apply-strategic-frameworks)

Victor draws from his innovation-frameworks library:

FrameworkPurpose**Jobs-to-be-Done**Understand what customers actually hire products to do**Blue Ocean Strategy**Find uncontested market space**Disruptive Innovation**Identify low-end or new-market opportunities**Business Model Canvas**Design or reinvent your business model**Value Chain Analysis**Find where to capture value

### 5. Define Your Strategic Position

[Section titled “5. Define Your Strategic Position”](#5-define-your-strategic-position)

Based on analysis, Victor helps you articulate:

- **Innovation thesis** — Your core strategic bet
- **Business model** — How you’ll create and capture value
- **Moats** — Sustainable competitive advantages
- **Execution priorities** — What matters most

Output saved to `_bmad-output/innovation-strategy-{date}.md`:

SectionContents**Strategic Question**Your innovation challenge**Market Analysis**Forces, trends, competitive landscape**Jobs-to-be-Done**Unmet customer needs**Blue Ocean Opportunities**Uncontested market spaces**Business Model**Value proposition and capture mechanisms**Competitive Advantages**Defensible moats**Strategic Roadmap**Priorities and execution path

```text

You: /cis-innovation-strategy
Victor: What strategic opportunity are we exploring?
You: We want to disrupt the home security market.
Victor: Interesting. Let me ask: What job are people hiring
home security to do?
You: [Discuss customer needs, fears, motivations]
Victor: [Applies Jobs-to-be-Done analysis]
I see. The industry competes on features and price.
But the real job is "peace of mind, not surveillance."
What if we competed on reassurance instead?
You: [Explore blue ocean opportunities]
Victor: [Guides business model design]
Here's your advantage: You don't sell alarms.
You sell sleep. That's a different business model.
```

After innovation strategy:

- Use **brainstorming** (`/cis-brainstorm`) to generate execution ideas
- Apply **design thinking** (`/cis-design-thinking`) to shape user experience
- Run **storytelling** (`/cis-storytelling`) to craft your strategic narrative

## Providing Context

[Section titled “Providing Context”](#providing-context)

For best results, provide market analysis via the `--data` flag:

```bash

workflowcis-innovation-strategy--data/path/to/market-analysis.md
```

Victor will use this context to ground the strategic analysis in your market reality.