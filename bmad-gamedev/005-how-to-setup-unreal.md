---
title: Set up an Unreal project with BMGD
url: https://game-dev-studio-docs.bmad-method.org/how-to/setup-unreal/
source: sitemap
fetched_at: 2026-04-08T11:34:05.0604945-03:00
rendered_js: false
word_count: 916
summary: This guide details the comprehensive, multi-step process for setting up and structuring a full production game development workflow within Unreal Engine using the BMad Game Development (BMGD) system. It covers everything from initial project setup and context generation to designing mechanics, creating technical architectures, planning sprints, and finally implementing features.
tags:
    - unreal-engine
    - game-development-workflow
    - project-setup
    - gdd
    - architecture
    - bmgd
category: guide
---

## Set up an Unreal project with BMGD

[Section titled “Set up an Unreal project with BMGD”](#set-up-an-unreal-project-with-bmgd)

Configure a new Unreal project with BMGD workflows for full production game development.

* * *

## When to Use This Guide

[Section titled “When to Use This Guide”](#when-to-use-this-guide)

- You’re starting a new Unreal game project
- You want to use BMGD’s Full Production workflow
- You need formal documentation (GDD, architecture, sprint tracking)

* * *

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- You just want to prototype quickly — use [Quick Flow](https://game-dev-studio-docs.bmad-method.org/how-to/tutorials/first-game-project/) instead
- You’re using Unity or Godot — see the setup guides for those engines
- You’re prototyping or doing a game jam — Quick Flow is faster

* * *

> **Before starting:**
> 
> - BMad Method installed with BMGD module enabled
> - Unreal Engine 5.x installed
> - Basic familiarity with Unreal (Blueprints or C++)
> - A game concept or idea you want to develop

* * *

### Step 1: Create your Unreal project

[Section titled “Step 1: Create your Unreal project”](#step-1-create-your-unreal-project)

1. Open the **Epic Games Launcher**
2. Go to **Unreal Engine** tab
3. Click **Launch** to open Unreal Editor
4. In the Project Browser, click **Games** → **Next**
5. Select the appropriate template:
   
   - **Blank** — Start from scratch (most flexible)
   - **Third Person** — Character-based games
   - **First Person** — FPS/exploration games
   - **Top Down** — Strategy and arcade games
6. Choose **Blueprint** or **C++**
7. Name your project, choose a location, and click **Create**

### Step 2: Generate your project context

[Section titled “Step 2: Generate your project context”](#step-2-generate-your-project-context)

BMGD uses a `project-context.md` file to maintain consistency across all workflows.

In your BMad-enabled environment at the project root:

```plaintext

/bmgd-generate-project-context
```

This invokes the **Game Architect (Cloud Dragonborn)** to create a `project-context.md` file that includes:

- Project name and description
- Target platforms (PC, console, mobile)
- Engine and framework choices (Blueprint vs C++)
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

Plan your Unreal project structure and systems.

```plaintext

/bmgd-create-architecture
```

The **Game Architect (Cloud Dragonborn)** creates `architecture.md` with:

- Project structure (Content Browser organization)
- System architecture (game framework, replication, networking)
- Unreal-specific patterns (Components, Game Instances, Gameplay Abilities)
- Performance budgets and optimization strategy
- Asset pipeline and build configuration

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

- Implement story tasks in Blueprints or C++
- Follow Unreal best practices
- Write tests for your features
- Review code before marking complete

* * *

After completing this setup, you’ll have:

File/FolderPurpose`project-context.md`AI context for consistency across all BMGD workflows`game-brief.md`Your game’s vision and positioning`gdd.md`Complete game design document`architecture.md`Technical architecture and Unreal-specific patterns`sprint-status.yaml`Sprint tracking with stories and progress`stories/`Folder containing individual story files

* * *

## Unreal-Specific Considerations

[Section titled “Unreal-Specific Considerations”](#unreal-specific-considerations)

### Project Structure

[Section titled “Project Structure”](#project-structure)

BMGD recommends this Content Browser structure:

```plaintext

Content/
├── Game/
│   ├── Blueprints/
│   ├── Materials/
│   ├── Meshes/
│   ├── Textures/
│   ├── Audio/
│   └── UI/
├── Developers/
│   └── [YourName]/
└── Collections/
```

Your architecture should specify:

ApproachWhen to Use**Blueprints**Rapid prototyping, gameplay logic, designer-iterable systems**C++**Performance-critical systems, complex algorithms, platform-specific features**Mixed**C++ for systems, Blueprints for gameplay (common approach)

The Game Architect will recommend the right mix for your project.

### Performance Budgets

[Section titled “Performance Budgets”](#performance-budgets)

Unreal projects typically target:

- **60 FPS** for most console/PC games
- **30 FPS** for open-world games with high draw distance
- **120 FPS** for competitive shooters

Your `architecture.md` will specify frame time budgets (ms per frame).

For Unreal automated testing, the Game QA agent (GLaDOS) can help:

This sets up Unreal Automation System with:

- Unit tests (C++ and Blueprint function libraries)
- Functional tests (gameplay systems)
- Performance tests (frame rate, memory)

* * *

> **Best Practice:** Always run `bmgd-generate-project-context` after creating a new Unreal project. The `project-context.md` file is the “single source of truth” that all BMGD agents reference.

> **Avoid:** Don’t start with the First Person template if you’re making a third-person game. Choose the template closest to your final game — the Game Architect can advise if unsure.

> **Remember:** Unreal projects are larger than Unity projects. Clean up unused content early to keep your project manageable.

* * *

MistakeSolutionSkipping project-context generationAlways generate `project-context.md` first — it guides all other workflowsChoosing the wrong templateConsult the Game Architect — starting from Blank is often cleaner than refactoring a templateIgnoring Unreal’s project structureFollow Content Browser organization from your architecture — don’t create custom folder structuresNot using Unreal’s built-in systemsUse Gameplay Abilities, Gameplay Tags, and Data Assets — don’t reinvent the wheel

* * *

- [**Quick Flow vs Full Production**](https://game-dev-studio-docs.bmad-method.org/how-to/explanation/quick-flow-vs-full/) — Understand both development approaches
- [**Set up Unity with BMGD**](https://game-dev-studio-docs.bmad-method.org/how-to/setup-unreal/setup-unity/) — If you’re considering Unity instead
- [**Run sprint planning**](https://game-dev-studio-docs.bmad-method.org/how-to/setup-unreal/sprint-planning/) — When you’re ready to start building
- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/how-to/reference/agents/) — Learn about all 6 BMGD agents