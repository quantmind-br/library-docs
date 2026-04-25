---
title: Quick Flow vs Full Production
url: https://game-dev-studio-docs.bmad-method.org/explanation/quick-flow-vs-full/
source: sitemap
fetched_at: 2026-04-08T11:34:00.881722198-03:00
rendered_js: false
word_count: 796
summary: 'This document explains the difference between two development methodologies offered by BMad Game Dev Studio: Quick Flow for rapid prototyping and Full Production for structured, long-term team projects. It guides users on when to use each method and how they can transition between them.'
tags:
    - game-development
    - quick-flow
    - full-production
    - prototyping
    - workflow
    - dev-methodology
category: guide
---

## Quick Flow vs Full Production

[Section titled “Quick Flow vs Full Production”](#quick-flow-vs-full-production)

BMad Game Dev Studio offers two development approaches. Understanding the difference helps you choose the right path for your project.

* * *

**Fast iteration for solo developers and small teams.**

Quick Flow is designed for rapid prototyping and quick iteration. It’s ideal when you want to test ideas fast or ship a small project quickly.

### When to Use Quick Flow

[Section titled “When to Use Quick Flow”](#when-to-use-quick-flow)

- You’re working **alone** or with a **tiny team**
- You want to **test a game mechanic** before committing
- You’re building a **small prototype** or game jam entry
- Speed matters more than comprehensive documentation
- You’re comfortable making decisions as you go

### What Quick Flow Looks Like

[Section titled “What Quick Flow Looks Like”](#what-quick-flow-looks-like)

```plaintext

Idea → Quick Prototype → Play → Iterate → Ship
```

**No lengthy planning phases.** You jump straight into building, test early, and refine based on what’s fun.

### The Quick Flow Workflow

[Section titled “The Quick Flow Workflow”](#the-quick-flow-workflow)

Quick Flow uses the **Game Solo Dev (Indie)** agent, who specializes in rapid development:

1. **Quick Prototype** — Define your core mechanic and generate a prototype structure
2. **Quick Dev** — Implement features directly with game-specific guidance
3. **Quick Spec** — Generate a technical spec when you need one (optional)

<!--THE END-->

- A playable prototype in **hours, not days**
- Minimal documentation (just what you need)
- Fast feedback loop with playtesting
- Flexibility to pivot based on what works

### When to Skip Quick Flow

[Section titled “When to Skip Quick Flow”](#when-to-skip-quick-flow)

- You have a **larger team** that needs coordination
- You’re working with **publishers or stakeholders** who require formal documentation
- The project needs to be **maintained long-term** by multiple developers
- You need to track **sprints, stories, and epics** formally

* * *

**Structured development for teams and long-term projects.**

Full Production follows a complete game development pipeline from concept through production. It’s ideal for larger projects and teams.

### When to Use Full Production

[Section titled “When to Use Full Production”](#when-to-use-full-production)

- You have a **team** with multiple disciplines (design, code, art)
- You need **formal documentation** for stakeholders or publishers
- The project will be **maintained or expanded** over time
- You want to track progress through **sprints and stories**
- You’re building something **larger than a prototype**

### What Full Production Looks Like

[Section titled “What Full Production Looks Like”](#what-full-production-looks-like)

```plaintext

Preproduction → Design → Technical → Production (sprints/stories)
```

**Each phase has specific workflows and artifacts.** Progress is tracked through sprints, stories, and retrospectives.

### The Full Production Workflow

[Section titled “The Full Production Workflow”](#the-full-production-workflow)

Full Production uses specialized agents for each phase:

PhaseAgentWorkflowsOutputs**Preproduction**Game Designerbrainstorm-game, game-briefgame-brief.md**Design**Game Designercreate-gdd, narrativegdd.md, narrative.md**Technical**Game Architectcreate-architecture, project-contextarchitecture.md, project-context.md**Production**Game Scrum Mastersprint-planning, create-storysprint-status.yaml, stories/**Implementation**Game Developerdev-story, code-reviewCompleted features**Testing**Game QAtest-framework, automateTest suites, test results

- **Complete documentation** — Game brief, GDD, architecture, technical specs
- **Sprint tracking** — sprint-status.yaml with stories, progress, and risks
- **Story management** — Clearly defined features with acceptance criteria
- **Project context** — AI-aware context file for consistency across all workflows
- **Retrospective process** — Continuous improvement for the team

### When to Skip Full Production

[Section titled “When to Skip Full Production”](#when-to-skip-full-production)

- You’re **working alone** and don’t need formal process
- You just want to **test an idea quickly**
- Documentation would **slow you down** more than it helps
- The project is a **one-off prototype** or experiment

* * *

## Comparison at a Glance

[Section titled “Comparison at a Glance”](#comparison-at-a-glance)

AspectQuick FlowFull Production**Team size**Solo or tiny teamAny size**Speed**Fast — prototype in hoursThorough — planning takes time**Documentation**Minimal (prototype spec)Comprehensive (brief, GDD, architecture)**Tracking**None (or informal)Sprints, stories, retrospectives**Agents involved**Game Solo Dev (Indie)All 6 agents as needed**Best for**Prototypes, jams, small projectsFull games, teams, publishers**Time to first playable**Hours to daysDays to weeks

* * *

## Can You Switch Between Paths?

[Section titled “Can You Switch Between Paths?”](#can-you-switch-between-paths)

**Yes.** Quick Flow and Full Production aren’t locked doors — they’re different approaches to the same goal.

### Quick Flow → Full Production

[Section titled “Quick Flow → Full Production”](#quick-flow--full-production)

Started with Quick Flow and now need more structure? No problem.

- Your prototype becomes the foundation for your **Game Brief**
- Iterate on your core mechanic in the **GDD phase**
- Use your prototype to inform the **Architecture**

The work you’ve done in Quick Flow informs the Full Production planning.

### Full Production → Quick Flow

[Section titled “Full Production → Quick Flow”](#full-production--quick-flow)

In the middle of Full Production but need to test something quickly?

- Use Indie’s **Quick Dev** workflow for rapid implementation
- Return to your **sprint planning** when ready

Full Production doesn’t forbid Quick Flow workflows — it provides structure around them.

* * *

## Making Your Choice

[Section titled “Making Your Choice”](#making-your-choice)

**Still unsure?** Start with Quick Flow.

Quick Flow gets you to a playable prototype faster. If your project grows, you can transition to Full Production with your prototype as the foundation.

**Remember:** A playable prototype beats a perfect design document. Test early, ship often.

* * *

- [**Your first game project with BMGD**](https://game-dev-studio-docs.bmad-method.org/explanation/tutorials/first-game-project/) — Try Quick Flow now
- [**Set up Unity with BMGD**](https://game-dev-studio-docs.bmad-method.org/explanation/how-to/setup-unity/) — Engine-specific Full Production setup
- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/explanation/reference/agents/) — Learn about all 6 BMGD agents