---
title: Set up a Godot project with BMGD
url: https://game-dev-studio-docs.bmad-method.org/how-to/setup-godot/
source: sitemap
fetched_at: 2026-04-08T11:34:03.912013471-03:00
rendered_js: false
word_count: 900
summary: This guide outlines the step-by-step process for setting up a professional Godot game project using the BMGD (BMad Game Development) workflow. It details everything from initial project configuration and generating core documentation like the GDD and architecture, through to planning sprints and implementing features.
tags:
    - godot
    - game-development
    - bmgd
    - project-setup
    - gdd
    - workflow
category: guide
---

## Set up a Godot project with BMGD

[Section titled “Set up a Godot project with BMGD”](#set-up-a-godot-project-with-bmgd)

Configure a new Godot project with BMGD workflows for full production game development.

* * *

## When to Use This Guide

[Section titled “When to Use This Guide”](#when-to-use-this-guide)

- You’re starting a new Godot game project
- You want to use BMGD’s Full Production workflow
- You need formal documentation (GDD, architecture, sprint tracking)

* * *

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- You just want to prototype quickly — use [Quick Flow](https://game-dev-studio-docs.bmad-method.org/how-to/tutorials/first-game-project/) instead
- You’re using Unity or Unreal — see the setup guides for those engines
- You’re prototyping or doing a game jam — Quick Flow is faster

* * *

> **Before starting:**
> 
> - BMad Method installed with BMGD module enabled
> - Godot 4.2+ (recommended) or Godot 3.x installed
> - Basic familiarity with Godot and GDScript
> - A game concept or idea you want to develop

* * *

### Step 1: Create your Godot project

[Section titled “Step 1: Create your Godot project”](#step-1-create-your-godot-project)

1. Open **Godot Project Manager**
2. Click **New Project**
3. Browse to your desired folder location
4. Choose a renderer:
   
   - **Forward+** — Modern PBR, best for 3D games
   - **Mobile** — Optimized for mobile platforms
   - **Compatibility** — GLES2, for older hardware
5. Name your project folder
6. Click **Create & Edit**

### Step 2: Generate your project context

[Section titled “Step 2: Generate your project context”](#step-2-generate-your-project-context)

BMGD uses a `project-context.md` file to maintain consistency across all workflows.

In your BMad-enabled environment at the project root:

```plaintext

/bmgd-generate-project-context
```

This invokes the **Game Architect (Cloud Dragonborn)** to create a `project-context.md` file that includes:

- Project name and description
- Target platforms (PC, mobile, web)
- Engine version and renderer choice
- Performance budgets
- Critical technical decisions

### Step 3: Run the brainstorming workflow

[Section titled “Step 3: Run the brainstorming workflow”](#step-3-run-the-brainstorming-workflow)

Define your game concept with the Game Designer agent.

The **Game Designer (Samus Shepard)** will guide you through:

- Selecting and combining brainstorming techniques
- Generating and refining game ideas
- Choosing a concept to develop

### Step 4: Create your Game Brief

[Section titled “Step 4: Create your Game Brief”](#step-4-create-your-game-brief)

Capture your vision and positioning.

The Game Designer creates `game-brief.md` with:

- Game vision and elevator pitch
- Target audience and market positioning
- Platform and genre decisions
- Competitive analysis
- Art and audio direction

### Step 5: Design your game (GDD)

[Section titled “Step 5: Design your game (GDD)”](#step-5-design-your-game-gdd)

Create a comprehensive Game Design Document.

The Game Designer helps you:

- Select your game type from 24 available templates
- Define core gameplay mechanics
- Design progression systems
- Plan levels and content
- Specify art and audio requirements

Output: `gdd.md`

### Step 6: Create your technical architecture

[Section titled “Step 6: Create your technical architecture”](#step-6-create-your-technical-architecture)

Plan your Godot project structure and systems.

```plaintext

/bmgd-create-architecture
```

The **Game Architect (Cloud Dragonborn)** creates `architecture.md` with:

- Project structure (scenes, scripts, resources)
- System architecture (game loop, nodes, signals, autoloads)
- Godot-specific patterns (tree organization, resource management)
- Performance budgets and optimization strategy
- Export configurations and platform settings

### Step 7: Plan your first sprint

[Section titled “Step 7: Plan your first sprint”](#step-7-plan-your-first-sprint)

Ready to start building? Use the Game Scrum Master to plan your work.

The **Game Scrum Master (Max)** creates:

- `sprint-status.yaml` — Your sprint tracking file
- Stories from your GDD and Architecture
- Sprint goals and definition of done

### Step 8: Start implementing

[Section titled “Step 8: Start implementing”](#step-8-start-implementing)

Build features with the Game Developer agent.

```plaintext

/bmgd-dev-story [story-name]
```

The **Game Developer (Link Freeman)** helps you:

- Implement story tasks with GDScript
- Follow Godot best practices
- Write tests for your features
- Review code before marking complete

* * *

After completing this setup, you’ll have:

File/FolderPurpose`project-context.md`AI context for consistency across all BMGD workflows`game-brief.md`Your game’s vision and positioning`gdd.md`Complete game design document`architecture.md`Technical architecture and Godot-specific patterns`sprint-status.yaml`Sprint tracking with stories and progress`stories/`Folder containing individual story files

* * *

## Godot-Specific Considerations

[Section titled “Godot-Specific Considerations”](#godot-specific-considerations)

### Project Structure

[Section titled “Project Structure”](#project-structure)

BMGD recommends this Godot project structure:

```plaintext

res://
├── scenes/
│   ├── levels/
│   ├── characters/
│   ├── ui/
│   └── components/
├── scripts/
│   ├── autoload/
│   └── utils/
├── assets/
│   ├── art/
│   ├── audio/
│   └── data/
└── project.godot
```

### Scene Organization

[Section titled “Scene Organization”](#scene-organization)

Godot uses a tree of nodes. Your architecture should define:

- **Autoload Singletons** — Global managers (game state, audio, saves)
- **Scene Composition** — Reusable scenes (player, enemies, pickups)
- **Signal Patterns** — Decoupled communication between nodes

The Game Architect will specify these patterns in your `architecture.md`.

### Performance Budgets

[Section titled “Performance Budgets”](#performance-budgets)

Godot projects typically target:

- **60 FPS** for most games
- **30 FPS** for mobile with heavy computation
- **144+ FPS** for competitive games

Your `architecture.md` will specify frame time budgets.

For Godot automated testing, the Game QA agent (GLaDOS) can help:

This sets up GUT (Godot Unit Test) with:

- Unit tests (script logic without scenes)
- Integration tests (scene interactions)
- Test fixtures and test doubles

* * *

> **Best Practice:** Always run `bmgd-generate-project-context` after creating a new Godot project. The `project-context.md` file is the “single source of truth” that all BMGD agents reference.

> **Avoid:** Don’t create deeply nested scene trees. Godot’s scene system encourages composition — prefer many small scenes over one large scene.

> **Remember:** Godot uses GDScript (Python-like) by default. Your architecture should specify if you’re using C# or GDScript — both are supported but have different workflows.

* * *

MistakeSolutionSkipping project-context generationAlways generate `project-context.md` first — it guides all other workflowsCreating monolithic scenesBreak your game into reusable scene components — the Game Architect can help design thisNot using autoloads properlyKeep autoloads minimal — only use for true singletons (game state, save system)Mixing GDScript and C# arbitrarilyChoose one primary language and stick with it — mixing adds complexity without benefit

* * *

- [**Quick Flow vs Full Production**](https://game-dev-studio-docs.bmad-method.org/how-to/explanation/quick-flow-vs-full/) — Understand both development approaches
- [**Set up Unity with BMGD**](https://game-dev-studio-docs.bmad-method.org/how-to/setup-godot/setup-unity/) — If you’re considering Unity instead
- [**Run sprint planning**](https://game-dev-studio-docs.bmad-method.org/how-to/setup-godot/sprint-planning/) — When you’re ready to start building
- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/how-to/reference/agents/) — Learn about all 6 BMGD agents