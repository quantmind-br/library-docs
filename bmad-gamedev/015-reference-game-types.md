---
title: BMGD Game Types Reference
url: https://game-dev-studio-docs.bmad-method.org/reference/game-types/
source: sitemap
fetched_at: 2026-04-08T11:34:12.333708797-03:00
rendered_js: false
word_count: 498
summary: This document serves as a comprehensive reference guide detailing 24 distinct game type templates used within the BMGD GDD workflow, outlining key elements for genres ranging from platformers and shooters to RPGs and simulation games. It also explains how the Game Designer agent helps users select primary and secondary types when designing complex hybrid games.
tags:
    - bmgd-workflow
    - game-design-reference
    - game-types
    - gdd-templates
    - genre-guide
    - gameplay-systems
category: reference
---

## BMGD Game Types Reference

[Section titled “BMGD Game Types Reference”](#bmgd-game-types-reference)

BMGD’s GDD workflow includes 24 game type templates. Each template provides specialized guidance for designing that specific genre.

* * *

Game TypeDescriptionKey Elements**Action Platformer**Jump, run, and overcome obstaclesMovement system, combat, level design patterns, ability unlocks**Fighting**One-on-one combat between charactersMove sets, combo systems, balance, frame data**Shooter**Combat through projectilesWeapon systems, aim mechanics, enemy AI, level flow**Survival**Stay alive in a hostile environmentResource management, crafting, base building, threat systems

* * *

## Adventure & Exploration

[Section titled “Adventure & Exploration”](#adventure--exploration)

Game TypeDescriptionKey Elements**Adventure**Narrative-driven explorationStory structure, puzzles, environmental storytelling, progression**Metroidvania**Explore an interconnected world with ability-gated progressionMap design, ability gates, backtracking rewards, power curve**Horror**Evoke fear and tensionAtmosphere, threat design, resource scarcity, pacing**Visual Novel**Branching narrative with character focusStory branches, character arcs, dialogue systems, choices

* * *

## Strategy & Tactics

[Section titled “Strategy & Tactics”](#strategy--tactics)

Game TypeDescriptionKey Elements**Strategy**Real-time or turn-based resource and unit managementEconomy, tech trees, unit balance, map control**Turn-Based Tactics**Small-scale combat with positional strategyUnit abilities, cover systems, action economy, mission design**Tower Defense**Defend against waves of enemiesTower types, enemy variety, placement strategy, upgrade paths**MOBA**Team-based competitive combat with hero progressionHero design, laning, item systems, team synergy

* * *

## Role-Playing Games

[Section titled “Role-Playing Games”](#role-playing-games)

Game TypeDescriptionKey Elements**RPG**Character progression through story and combatCharacter builds, skill trees, equipment, encounter design**Roguelike**Procedural generation with permadeathRun structure, unlock persistence, balance across runs, item pools

* * *

## Simulation & Management

[Section titled “Simulation & Management”](#simulation--management)

Game TypeDescriptionKey Elements**Simulation**Model real-world systemsSystem depth, feedback loops, complexity management**Sandbox**Open-ended play with user creativityToolsets, creation tools, sharing systems, emergent gameplay**Idle/Incremental**Progress through automated systemsPrestige mechanics, balance curves, offline progression, unlock structure

* * *

Game TypeDescriptionKey Elements**Puzzle**Solve challenges using logicPuzzle mechanics, difficulty curve, hint systems, variety**Text-Based**Gameplay through prose inputParser design, world modeling, narrative integration, hint design

* * *

Game TypeDescriptionKey Elements**Sports**Simulate competitive sportsSport rules, player stats, team AI, progression**Racing**Compete to finish firstTrack design, vehicle physics, handling feel, progression

* * *

Game TypeDescriptionKey Elements**Card Game**Gameplay through card mechanicsCard design, deck building, RNG management, meta evolution**Party Game**Multiplayer mini-games for social playMinigame variety, accessibility, party size support, replayability**Rhythm**Synchronize actions to musicBeat mapping, difficulty scaling, music integration, visual feedback

* * *

## Using Game Type Templates

[Section titled “Using Game Type Templates”](#using-game-type-templates)

When you run the `create-gdd` workflow, the Game Designer agent will:

1. Help you select the appropriate game type for your concept
2. Load the specialized template for that type
3. Guide you through type-specific design considerations
4. Generate a GDD tailored to your chosen genre

**Example:** If you select “Action Platformer,” your GDD will include:

- Movement system design (jump mechanics, air control)
- Combat system design (attack types, combos)
- Level design patterns (platforming challenges, checkpoint placement)
- Player abilities and progression

* * *

Many games combine multiple game types. The Game Designer can help you:

1. **Identify your primary type** — The core gameplay loop
2. **Select secondary types** — Systems borrowed from other genres
3. **Balance the combination** — Ensure systems work together

**Examples:**

- **Action-RPG** — Action Platformer + RPG
- **Survival Horror** — Survival + Horror
- **Rogue-lite** — Roguelike + (another genre)
- **Tower Defense RPG** — Tower Defense + RPG

* * *

- [**Workflows Reference**](https://game-dev-studio-docs.bmad-method.org/reference/game-types/workflows/) — All BMGD workflows
- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/reference/game-types/agents/) — Learn about the Game Designer agent
- [**Set up Unity/Unreal/Godot**](https://game-dev-studio-docs.bmad-method.org/reference/how-to/setup-unity/) — Engine-specific setup guides