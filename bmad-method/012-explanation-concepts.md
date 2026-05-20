---
title: Advanced Concepts and Techniques
url: https://docs.bmad-method.org//llms-full.txt
source: llms
fetched_at: 2026-05-19T08:33:05.038451722-03:00
rendered_js: false
summary: Advanced reasoning techniques including elicitation, adversarial review, and analysis-phase tools.
tags:
    - bmad-method
    - advanced-elicitation
    - adversarial-review
    - analysis
category: concept
optimized: true
optimized_at: 2026-05-19T11:33:05Z
word_count: 598
---
# Advanced Concepts and Techniques

Make the LLM reconsider what it just generated. You pick a reasoning method, it applies that method to its own output, you decide whether to keep the improvements.

## What is Advanced Elicitation?

A structured second pass. Instead of asking the AI to "try again" or "make it better," you select a specific reasoning method and the AI re-examines its own output through that lens.

The difference matters. Vague requests produce vague revisions. A named method forces a particular angle of attack, surfacing insights that a generic retry would miss.

## When to Use It

- After a workflow generates content and you want alternatives
- When output seems okay but you suspect there's more depth
- To stress-test assumptions or find weaknesses
- For high-stakes content where rethinking helps

Workflows offer advanced elicitation at decision points — after the LLM has generated something, you'll be asked if you want to run it.

## How It Works

1. LLM suggests 5 relevant methods for your content
2. You pick one (or reshuffle for different options)
3. Method is applied, improvements shown
4. Accept or discard, repeat or continue

## Built-in Methods

Dozens of reasoning methods are available. Examples:

- **Pre-mortem Analysis** — Assume the project already failed, work backward to find why
- **First Principles Thinking** — Strip away assumptions, rebuild from ground truth
- **Inversion** — Ask how to guarantee failure, then avoid those things
- **Red Team vs Blue Team** — Attack your own work, then defend it
- **Socratic Questioning** — Challenge every claim with "why?" and "how do you know?"
- **Constraint Removal** — Drop all constraints, see what changes, add them back selectively
- **Stakeholder Mapping** — Re-evaluate from each stakeholder's perspective
- **Analogical Reasoning** — Find parallels in other domains and apply their lessons

The AI picks the most relevant options for your content — you choose which to run.

> [!tip] Start Here
> Pre-mortem Analysis is a good first pick for any spec or plan. It consistently finds gaps that a standard review misses.

## Analysis Before Planning

The Analysis phase (Phase 1) helps you think clearly about your product before committing to building it. Every tool is optional, but skipping analysis entirely means your PRD is built on assumptions instead of insight.

### Why Analysis Before Planning?

A PRD answers "what should we build and why?" If you feed it vague thinking, you get a vague PRD — and every downstream document inherits that vagueness. Architecture built on a weak PRD makes wrong technical bets. Stories derived from weak architecture miss edge cases. The cost compounds.

Analysis tools make your PRD sharp. They attack the problem from different angles — creative exploration, market reality, customer clarity, feasibility — so that by the time you sit down with the PM agent, you know what you're building and for whom.

### Brainstorming

**What it is.** A facilitated creative session using proven ideation techniques. The AI acts as coach, pulling ideas out of you through structured exercises — not generating ideas for you.

**Why it's here.** Raw ideas need space to develop before they get locked into requirements. Brainstorming creates that space. It's especially valuable when you have a problem domain but no clear solution, or when you want to explore multiple directions before committing.

**When to use it.** You have a vague sense of what you want to build but haven't crystallized the concept. Or you have a concept but want to pressure-test it against alternatives.

See [Brainstorming](./brainstorming.md) for a deeper look.

####

#advanced-elicitation #adversarial-review #analysis
