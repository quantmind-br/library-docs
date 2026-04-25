---
title: Set up a Unity project with BMGD
url: https://game-dev-studio-docs.bmad-method.org/how-to/setup-unity/
source: sitemap
fetched_at: 2026-04-08T11:34:04.599605319-03:00
rendered_js: false
word_count: 873
summary: This guide provides a step-by-step walkthrough detailing how to set up a complete Unity game project workflow using the specialized BMad Game Development (BMGD) methodology. It covers everything from initial project creation and context generation to developing technical architecture, writing design documents (GDD), and planning sprints.
tags:
    - unity
    - game-development
    - workflow
    - gdd
    - bmgd
    - setup-guide
category: guide
---

## Set up a Unity project with BMGD

[Section titled “Set up a Unity project with BMGD”](#set-up-a-unity-project-with-bmgd)

Configure a new Unity project with BMGD workflows for full production game development.

* * *

## When to Use This Guide

[Section titled “When to Use This Guide”](#when-to-use-this-guide)

- You’re starting a new Unity game project
- You want to use BMGD’s Full Production workflow
- You need formal documentation (GDD, architecture, sprint tracking)

* * *

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- You just want to prototype quickly — use [Quick Flow](https://game-dev-studio-docs.bmad-method.org/how-to/tutorials/first-game-project/) instead
- You’re using Unreal or Godot — see the setup guides for those engines
- You’re prototyping or doing a game jam — Quick Flow is faster

* * *

> **Before starting:**
> 
> - BMad Method installed with BMGD module enabled
> - Unity Hub and Unity 2022 LTS (or later) installed
> - Basic familiarity with Unity and C#
> - A game concept or idea you want to develop

* * *

### Step 1: Create your Unity project

[Section titled “Step 1: Create your Unity project”](#step-1-create-your-unity-project)

1. Open Unity Hub
2. Click **New Project**
3. Select the appropriate template for your game type:
   
   - **2D** → Core 2D
   - **3D** → 3D Core
   - **URP** → Universal Render Pipeline (recommended for most games)
   - **HDRP** → High Definition Render Pipeline (high-end visuals)
4. Name your project and choose a location
5. Click **Create Project**

### Step 2: Generate your project context

[Section titled “Step 2: Generate your project context”](#step-2-generate-your-project-context)

BMGD uses a `project-context.md` file to maintain consistency across all workflows.

In your BMad-enabled environment at the project root:

```plaintext

/bmgd-generate-project-context
```

This invokes the **Game Architect (Cloud Dragonborn)** to create a `project-context.md` file that includes:

- Project name and description
- Target platforms
- Engine and framework choices
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

Plan your Unity project structure and systems.

```plaintext

/bmgd-create-architecture
```

The **Game Architect (Cloud Dragonborn)** creates `architecture.md` with:

- Project structure (folders, naming conventions)
- System architecture (game loop, input, physics, networking)
- Unity-specific patterns (ScriptableObjects, events, object pooling)
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

- Implement story tasks with C# scripts
- Follow Unity best practices
- Write tests for your features
- Review code before marking complete

* * *

After completing this setup, you’ll have:

File/FolderPurpose`project-context.md`AI context for consistency across all BMGD workflows`game-brief.md`Your game’s vision and positioning`gdd.md`Complete game design document`architecture.md`Technical architecture and Unity-specific patterns`sprint-status.yaml`Sprint tracking with stories and progress`stories/`Folder containing individual story files

* * *

## Unity-Specific Considerations

[Section titled “Unity-Specific Considerations”](#unity-specific-considerations)

### Project Structure

[Section titled “Project Structure”](#project-structure)

BMGD recommends this Unity project structure:

```plaintext

Assets/
├── _Project/
│   ├── Scripts/
│   ├── Art/
│   ├── Audio/
│   └── Data/
├── Packages/
└── ProjectSettings/
```

### ScriptableObjects

[Section titled “ScriptableObjects”](#scriptableobjects)

Use ScriptableObjects for game data — the Game Architect will include this in your architecture:

- Game configuration
- Character stats
- Item definitions
- Level data

### Performance Budgets

[Section titled “Performance Budgets”](#performance-budgets)

Unity projects typically target:

- **60 FPS** for most platforms
- **30 FPS** for mobile (if targeting battery life)
- **120+ FPS** for VR/high-refresh gaming

Your `architecture.md` will specify your targets.

For Unity automated testing, the Game QA agent (GLaDOS) can help:

This sets up Unity Test Framework with:

- Edit Mode tests (logic without running the game)
- Play Mode tests (gameplay systems)
- Test assembly structure

* * *

> **Best Practice:** Always run `bmgd-generate-project-context` after creating a new Unity project. The `project-context.md` file is the “single source of truth” that all BMGD agents reference.

> **Avoid:** Don’t manually organize your Assets folder before running `bmgd-create-architecture`. Let the Game Architect define the structure first, then follow it consistently.

> **Remember:** Unity projects can get large quickly. Use the architecture document to keep your project organized as it grows.

* * *

MistakeSolutionSkipping project-context generationAlways generate `project-context.md` first — it guides all other workflowsChoosing the wrong Unity templateConsult the Game Architect if unsure — your engine choice affects architectureStarting implementation before GDDComplete the Design phase first — changes are cheaper before code is writtenIgnoring sprint planningEven solo projects benefit from story tracking — it keeps you focused on ship

* * *

- [**Quick Flow vs Full Production**](https://game-dev-studio-docs.bmad-method.org/how-to/explanation/quick-flow-vs-full/) — Understand both development approaches
- [**Set up Unreal with BMGD**](https://game-dev-studio-docs.bmad-method.org/how-to/setup-unity/setup-unreal/) — If you’re considering Unreal instead
- [**Run sprint planning**](https://game-dev-studio-docs.bmad-method.org/how-to/setup-unity/sprint-planning/) — When you’re ready to start building
- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/how-to/reference/agents/) — Learn about all 6 BMGD agents