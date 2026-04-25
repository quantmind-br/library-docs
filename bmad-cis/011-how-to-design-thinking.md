---
title: Apply Design Thinking
url: https://cis-docs.bmad-method.org/how-to/design-thinking/
source: sitemap
fetched_at: 2026-04-08T11:33:51.785856299-03:00
rendered_js: false
word_count: 364
summary: This document outlines the design thinking workflow, guiding users through its five core phases—Empathize, Define, Ideate, Prototype, and Test—to create user-centered solutions for defined problems.
tags:
    - design-thinking
    - user-experience
    - problem-solving
    - prototyping
    - user-research
    - empathy
category: guide
---

Use the `design-thinking` workflow to create solutions deeply rooted in user needs through empathy, ideation, and rapid prototyping.

- Designing products or features for people
- Solving problems where user experience matters
- Starting from user research or empathy work
- Need to move from insights to testable prototypes
- Reimagining an existing experience

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- Pure technical problems without user interaction
- Infrastructure or backend-only concerns
- Timeframes don’t allow for user validation

Start a fresh chat and load the Design Thinking Coach:

### 2. Define Your Challenge

[Section titled “2. Define Your Challenge”](#2-define-your-challenge)

Maya will ask for your design challenge. Frame it around user needs:

**Good challenges:**

- “How might we help users feel more confident starting a new project?”
- “Redesign the checkout experience for mobile shoppers”
- “Help small business owners understand their cash flow”

**Less effective:**

- “Build a new dashboard” (solution-first)
- “Fix the slow API” (technical, not user-centered)

### 3. Journey Through the Five Phases

[Section titled “3. Journey Through the Five Phases”](#3-journey-through-the-five-phases)

Maya guides you through the complete design thinking process:

PhaseGoalWhat You Do**Empathize**Understand usersShare insights, create personas, map empathy**Define**Frame the problemCraft POV statements, ask “How Might We”**Ideate**Generate solutionsDiverge wildly, then converge on promising concepts**Prototype**Make it tangibleCreate rough artifacts that convey the idea**Test**Validate with usersPlan how to get real feedback

### 4. Apply Design Methods

[Section titled “4. Apply Design Methods”](#4-apply-design-methods)

At each phase, Maya selects appropriate methods from her design-methods library:

- **Empathize**: User interviews, empathy mapping, journey maps
- **Define**: POV madlibs, “How Might We” framing, problem statements
- **Ideate**: Brainstorming, sketching, storyboarding
- **Prototype**: Paper prototypes, role-play, Wizard of Oz
- **Test**: Usability testing plans, feedback capture templates

Output saved to `_bmad-output/design-thinking-{date}.md`:

SectionContents**Design Challenge**Your framed opportunity**Point of View**User-centered problem statement**User Insights**Empathy findings and personas**How Might We Questions**Reframed problem as opportunity**Solution Concepts**Generated ideas with rationales**Prototype Designs**Testable artifacts and mockups**Test Plan**How to validate with real users**Iteration Roadmap**Next steps based on learning

```text

You: /cis-design-thinking
Maya: 🎨 Tell me about your design challenge, friend.
Who are the humans we're designing with?
You: We need to redesign onboarding for our analytics tool.
Users are dropping out during setup.
Maya: Ah, first impressions! Let's start with empathy.
What do we know about these humans?
You: [Share user research, pain points]
Maya: [Guides through empathy mapping]
Now let's craft our Point of View...
"New analysts need to feel capable, not confused"
[Frames How Might We questions]
[Generates solution concepts]
[Creates low-fidelity prototype]
[Plans validation approach]
```

After design thinking:

- Use **storytelling** (`/cis-storytelling`) to craft user narratives
- Apply **innovation strategy** (`/cis-innovation-strategy`) to assess business viability
- Run **brainstorming** (`/cis-brainstorm`) if you need more solution options

## Providing Context

[Section titled “Providing Context”](#providing-context)

For best results, provide user research via the `--data` flag:

```bash

workflowcis-design-thinking--data/path/to/user-research.md
```

Maya will use this context to ground the empathy and definition phases in real user insights.