---
title: Run sprint planning with BMGD
url: https://game-dev-studio-docs.bmad-method.org/how-to/sprint-planning/
source: sitemap
fetched_at: 2026-04-08T11:34:06.487092002-03:00
rendered_js: false
word_count: 683
summary: This guide explains a multi-step workflow for managing game development sprints using BMGD, detailing processes from generating initial sprint status to implementing, reviewing, and closing feature stories.
tags:
    - sprint-planning
    - game-development
    - agile-workflow
    - story-management
    - scrum-process
    - gdd
    - technical-guidance
category: guide
---

## Run sprint planning with BMGD

[Section titled “Run sprint planning with BMGD”](#run-sprint-planning-with-bmgd)

Plan and track development sprints using BMGD’s agile workflows for game development.

* * *

## When to Use This Guide

[Section titled “When to Use This Guide”](#when-to-use-this-guide)

- You have a completed GDD and/or Architecture document
- You’re ready to start implementing features
- You want to track progress through stories and sprints

* * *

## When to Skip This

[Section titled “When to Skip This”](#when-to-skip-this)

- You’re still in the design phase — complete the GDD and Architecture first
- You’re doing Quick Flow prototyping — use Indie’s quick-prototype instead
- You just want to test a single feature — Quick Dev is faster

* * *

> **Before starting:**
> 
> - BMad Method installed with BMGD module enabled
> - Completed `gdd.md` (Game Design Document)
> - Completed `architecture.md` (Technical Architecture)
> - Basic familiarity with agile/scrum concepts

* * *

### Step 1: Generate sprint status from epics

[Section titled “Step 1: Generate sprint status from epics”](#step-1-generate-sprint-status-from-epics)

The Game Scrum Master reads your epic files to create the sprint tracking document.

The **Game Scrum Master (Max)** will:

1. Read your GDD and Architecture documents
2. Identify epics (large feature areas)
3. Generate `sprint-status.yaml` with all stories
4. Organize stories into sprints based on dependencies and priority

### Step 2: Review your sprint status

[Section titled “Step 2: Review your sprint status”](#step-2-review-your-sprint-status)

The generated `sprint-status.yaml` includes:

```yaml

sprint: 1
status: In Progress
stories:
- id: story-001
title: "Player movement system"
status: Ready
priority: P0
points: 5
assignee: ""
- id: story-002
title: "Basic enemy AI"
status: Pending
priority: P1
points: 8
assignee: ""
```

Review the stories and adjust as needed:

- **P0** — Must have for this sprint
- **P1** — Should have if time allows
- **P2** — Nice to have, defer if needed

### Step 3: Create detailed stories

[Section titled “Step 3: Create detailed stories”](#step-3-create-detailed-stories)

For each story, the Game Scrum Master creates a complete story file:

```plaintext

/bmgd-create-story [story-id]
```

This generates a story file in `stories/` with:

- **Title** and description
- **Acceptance criteria** — Definition of done
- **Technical notes** — From architecture
- **Test cases** — What needs to be tested
- **Dependencies** — Other stories or systems

### Step 4: Implement stories

[Section titled “Step 4: Implement stories”](#step-4-implement-stories)

Use the Game Developer agent to implement each story:

```plaintext

/bmgd-dev-story [story-id]
```

The **Game Developer (Link Freeman)** will:

1. Read the story file and acceptance criteria
2. Reference the architecture for technical guidance
3. Implement the feature with game-specific considerations
4. Create or update tests
5. Mark the story complete when all criteria pass

### Step 5: Review code (when flagged)

[Section titled “Step 5: Review code (when flagged)”](#step-5-review-code-when-flagged)

When a story is flagged “Ready for Review,” use the code review workflow:

The Game Developer performs a clean context QA review:

- Verifies acceptance criteria are met
- Checks for performance issues
- Reviews test coverage
- Provides feedback or approves the story

### Step 6: Check sprint status

[Section titled “Step 6: Check sprint status”](#step-6-check-sprint-status)

At any time, check your sprint progress:

This shows:

- Current sprint number and status
- Story progress (Ready, In Progress, Complete, Blocked)
- Risks and blockers
- Recommended next actions

### Step 7: Close the sprint

[Section titled “Step 7: Close the sprint”](#step-7-close-the-sprint)

When all sprint stories are complete:

The Game Scrum Master facilitates a retrospective:

- What went well
- What could be improved
- Action items for next sprint

Then run `sprint-planning` again to start the next sprint.

* * *

File/FolderPurpose`sprint-status.yaml`Sprint tracking with stories, progress, and risks`stories/`Folder containing individual story filesEach story fileComplete definition with acceptance criteria and tests

* * *

## Sprint Workflow Summary

[Section titled “Sprint Workflow Summary”](#sprint-workflow-summary)

```plaintext

sprint-planning → create-story → dev-story → code-review → sprint-status → retrospective
↑_____________|
(repeat for each story)
```

* * *

> **Best Practice:** Always generate stories from GDD and Architecture. Don’t write stories from scratch — let the Game Scrum Master create complete drafts from your existing documentation.

> **Avoid:** Don’t start implementation without stories. Stories keep you focused and provide clear acceptance criteria.

> **Remember:** Every sprint should deliver a playable increment. Test your game after each story completes.

* * *

MistakeSolutionWriting stories manuallyUse `bmgd-create-story` to generate complete stories from GDD/ArchitectureStarting P2 stories before P0Follow priority order — P0 first, then P1, then P2Skipping acceptance criteriaEach story must have clear “definition of done” before implementationNot testing after each storyPlaytest after every story completes — catches issues early

* * *

StateMeaningNext Action**Pending**Not yet ready to startMove to Ready when dependencies complete**Ready**Ready to implementRun `bmgd-dev-story`**In Progress**Currently being implementedComplete implementation or flag if blocked**Complete**Done and testedMove to next story**Blocked**Cannot proceed due to dependencyResolve blocker or re-plan sprint

* * *

- [**Quick Flow vs Full Production**](https://game-dev-studio-docs.bmad-method.org/how-to/explanation/quick-flow-vs-full/) — Understand both development approaches
- [**Set up Unity/Unreal/Godot**](https://game-dev-studio-docs.bmad-method.org/how-to/how-to/setup-unity/) — Engine-specific setup guides
- [**Agents Reference**](https://game-dev-studio-docs.bmad-method.org/how-to/reference/agents/) — Learn about the Game Scrum Master agent