---
title: Getting Started with CIS
url: https://cis-docs.bmad-method.org/tutorials/getting-started/
source: sitemap
fetched_at: 2026-04-08T11:34:08.78476542-03:00
rendered_js: false
word_count: 888
summary: This document serves as a comprehensive guide detailing how to use the Creative Intelligence Suite (CIS) by walking through five specialized AI agents—including brainstorming, design thinking, innovation strategy, problem-solving, and storytelling—to facilitate structured creative workflows.
tags:
    - ai-workflow
    - creative-intelligence
    - design-thinking
    - problem-solving
    - innovation-strategy
    - guide
category: guide
---

Unlock creative breakthroughs using AI-powered workflows with specialized agents that guide you through ideation, design thinking, innovation strategy, and systematic problem-solving.

## What You’ll Learn

[Section titled “What You’ll Learn”](#what-youll-learn)

- Install and initialize Creative Intelligence Suite
- Run your first brainstorming session with Carson
- Use design thinking for human-centered solutions
- Apply innovation strategy to find market opportunities
- Solve complex problems with systematic analysis
- Craft compelling narratives with Sophia

## Understanding CIS

[Section titled “Understanding CIS”](#understanding-cis)

The Creative Intelligence Suite (CIS) extends BMad Method with tools for the fuzzy front-end of development—where ideas are born, problems are reframed, and solutions emerge through structured creativity.

### CIS Agents and Workflows

[Section titled “CIS Agents and Workflows”](#cis-agents-and-workflows)

AgentWorkflowPurpose**Carson**`brainstorming`Generate ideas using 36 techniques across 7 categories**Maya**`design-thinking`Human-centered design through 5 phases**Victor**`innovation-strategy`Identify disruption opportunities and business model innovation**Dr. Quinn**`problem-solving`Systematic problem diagnosis and root cause analysis**Sophia**`storytelling`Craft compelling narratives using 25 story frameworks**Caravaggio***(coming soon)*Structure persuasive presentations

SituationUse ThisStuck on a problem`/cis-problem-solving`Need fresh ideas`/cis-brainstorm`Designing for users`/cis-design-thinking`Finding market gaps`/cis-innovation-strategy`Telling your story`/cis-storytelling`

CIS installs as a module during BMad Method setup. If you haven’t installed BMad Method yet:

When prompted to select modules, choose **Creative Intelligence Suite**.

The installer adds CIS agents and workflows to your `_bmad/` folder.

## Step 1: Your First Brainstorming Session

[Section titled “Step 1: Your First Brainstorming Session”](#step-1-your-first-brainstorming-session)

Let’s start with the most popular workflow—brainstorming with Carson.

### Load the Brainstorming Coach

[Section titled “Load the Brainstorming Coach”](#load-the-brainstorming-coach)

In a fresh chat, load Carson:

Carson will ask what you want to brainstorm about. Provide a topic—anything from “improving user onboarding” to “new product ideas for pet owners.”

Carson guides you through:

1. **Topic exploration** — Understanding what you’re brainstorming
2. **Technique selection** — Choose from 36 techniques or let Carson recommend one
3. **Ideation** — Carson facilitates using “Yes, and…” methodology
4. **Idea capture** — Results saved to `_bmad-output/brainstorming-{date}.md`

```plaintext

You: /cis-brainstorm
Carson: What would you like to brainstorm about?
You: Ways to reduce user churn
Carson: Let's explore this! I recommend the SCAMPER technique...
[Guides you through 7 creative angles]
[Generates diverse, actionable ideas]
```

## Step 2: Human-Centered Design with Maya

[Section titled “Step 2: Human-Centered Design with Maya”](#step-2-human-centered-design-with-maya)

When you need to design solutions for real people, Maya’s design thinking workflow helps you empathize, define, ideate, prototype, and test.

### Load the Design Thinking Coach

[Section titled “Load the Design Thinking Coach”](#load-the-design-thinking-coach)

PhaseWhat Happens**Empathize**Understand user needs and pain points**Define**Frame the problem from user perspective**Ideate**Generate diverse solutions**Prototype**Create rapid testable artifacts**Test**Validate with real users

Output saved to `_bmad-output/design-thinking-{date}.md`:

- Design challenge statement and point-of-view
- User insights and empathy mapping
- “How Might We” questions
- Solution concepts with prototypes
- Test plans and iteration roadmap

## Step 3: Strategic Innovation with Victor

[Section titled “Step 3: Strategic Innovation with Victor”](#step-3-strategic-innovation-with-victor)

Victor helps you find disruption opportunities and business model innovation.

### Load the Innovation Strategist

[Section titled “Load the Innovation Strategist”](#load-the-innovation-strategist)

### Strategic Analysis

[Section titled “Strategic Analysis”](#strategic-analysis)

Victor guides you through:

1. **Market landscape** — Competitive dynamics and trends
2. **Jobs-to-be-Done** — What users are actually trying to accomplish
3. **Blue Ocean Strategy** — Find uncontested market space
4. **Business model innovation** — New ways to create and capture value

Output saved to `_bmad-output/innovation-strategy-{date}.md`:

- Market disruption analysis
- Innovation opportunity mapping
- Business model canvas alternatives
- Strategic priorities and implementation roadmap

## Step 4: Systematic Problem-Solving with Dr. Quinn

[Section titled “Step 4: Systematic Problem-Solving with Dr. Quinn”](#step-4-systematic-problem-solving-with-dr-quinn)

For complex, stubborn problems, Dr. Quinn applies systematic methodologies to find root causes and effective solutions.

### Load the Problem Solver

[Section titled “Load the Problem Solver”](#load-the-problem-solver)

### The Analytical Process

[Section titled “The Analytical Process”](#the-analytical-process)

Dr. Quinn treats problems like puzzles:

1. **Problem diagnosis** — Separate symptoms from root causes
2. **Framework selection** — TRIZ, Theory of Constraints, Five Whys, Systems Thinking
3. **Solution generation** — Multiple approaches evaluated
4. **Implementation planning** — Actionable steps with risk mitigation

Output saved to `_bmad-output/problem-solution-{date}.md`:

- Root cause analysis
- Solution evaluation matrix
- Implementation plan with metrics
- Risk mitigation strategies

## Step 5: Storytelling with Sophia

[Section titled “Step 5: Storytelling with Sophia”](#step-5-storytelling-with-sophia)

When you need to persuade, inspire, or connect, Sophia crafts compelling narratives.

### Load the Storyteller

[Section titled “Load the Storyteller”](#load-the-storyteller)

### Narrative Development

[Section titled “Narrative Development”](#narrative-development)

Sophia guides you through:

1. **Purpose definition** — What should the audience feel/think/do?
2. **Framework selection** — Hero’s Journey, Story Brand, Three-Act, and more
3. **Character development** — Relatable protagonists and authentic voice
4. **Narrative arc** — Tension, climax, and resolution
5. **Platform adaptation** — Tailored for your medium

Output saved to `_bmad-output/story-{date}.md`:

- Complete narrative with emotional beats
- Character development and dialogue
- Sensory details and vivid moments
- Platform-specific formatting

## What You’ve Accomplished

[Section titled “What You’ve Accomplished”](#what-youve-accomplished)

You’ve learned the foundation of creative intelligence with CIS:

- Installed CIS and explored all six agents
- Run a brainstorming session with Carson
- Applied design thinking with Maya
- Analyzed innovation opportunities with Victor
- Solved problems systematically with Dr. Quinn
- Crafted narratives with Sophia

Your `_bmad-output/` folder now contains:

```plaintext

your-project/
├── _bmad/
│   └── cis/                          # CIS agents and workflows
├── _bmad-output/
│   ├── brainstorming-{date}.md       # Your ideation session results
│   ├── design-thinking-{date}.md     # Human-centered design artifacts
│   ├── innovation-strategy-{date}.md # Strategic innovation roadmap
│   ├── problem-solution-{date}.md    # Root cause and solutions
│   └── story-{date}.md               # Your crafted narrative
└── ...
```

WorkflowCommandAgentPurpose`brainstorming``/cis-brainstorm`CarsonGenerate diverse ideas`design-thinking``/cis-design-thinking`MayaHuman-centered design`innovation-strategy``/cis-innovation-strategy`VictorStrategic innovation`problem-solving``/cis-problem-solving`Dr. QuinnRoot cause analysis`storytelling``/cis-storytelling`SophiaCraft compelling narratives

**How do I provide context to a workflow?**

Use the `--data` flag with a file path:

```bash

workflowcis-design-thinking--data/path/to/user-research.md
```

**Can I use multiple CIS workflows together?**

Yes. Start with brainstorming to generate options, then use design thinking to refine user-centered solutions, or innovation strategy to evaluate business potential.

**What’s the difference between problem-solving and design thinking?**

Design thinking focuses on user needs and rapid prototyping. Problem-solving applies analytical frameworks to find root causes and evaluate solutions systematically.

**Do I need to use all workflows?**

No. Each workflow stands alone. Use the ones that match your current challenge.

- **During workflows** — Agents guide you with questions and technique explanations
- **Community** — [Discord](https://discord.gg/gk8jAdXWmj) (#creative-intelligence-suite)
- **Issues** — [GitHub Issues](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues)

Ready to think differently? Start your first brainstorming session and discover where structured creativity can take you.