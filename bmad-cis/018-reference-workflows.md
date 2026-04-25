---
title: CIS Workflows
url: https://cis-docs.bmad-method.org/reference/workflows/
source: sitemap
fetched_at: 2026-04-08T11:34:00.861730667-03:00
rendered_js: false
word_count: 508
summary: This document serves as a technical reference guide detailing five structured creative workflows—brainstorming, design thinking, innovation strategy, problem solving, and storytelling. It outlines the purpose, required inputs, invocation methods (CLI commands), and expected contents for each process.
tags:
    - workflow-reference
    - creative-process
    - ai-workflows
    - technical-guide
    - methodology
    - structured-output
category: reference
---

Technical reference for all CIS workflows including inputs, outputs, and invocation methods.

## Workflows Overview

[Section titled “Workflows Overview”](#workflows-overview)

WorkflowAgentPurposeOutput File**brainstorming**CarsonGenerate diverse ideas`brainstorming-{date}.md`**design-thinking**MayaHuman-centered design`design-thinking-{date}.md`**innovation-strategy**VictorStrategic innovation`innovation-strategy-{date}.md`**problem-solving**Dr. QuinnRoot cause analysis`problem-solution-{date}.md`**storytelling**SophiaNarrative crafting`story-{date}.md`

## Brainstorming Workflow

[Section titled “Brainstorming Workflow”](#brainstorming-workflow)

**Purpose:** Generate diverse, creative ideas using structured ideation techniques.

```bash

# Direct command
/cis-brainstorm
# With context data
workflowbrainstorming--data/path/to/context.md
# Via agent
/cis-agent-brainstorming-coach
> brainstorm
```

InputDescriptionRequired**topic**What to brainstorm aboutYes**technique**Which ideation method to useNo (Carson recommends)**mode**user-selected, AI-recommended, random, progressiveNo

SectionContents**Topic**Your brainstorming challenge**Technique**Method applied and rationale**Ideas**Complete list of all generated ideas**Top Picks**Recommended ideas for pursuit**Next Steps**How to move forward

### Techniques Library

[Section titled “Techniques Library”](#techniques-library)

Carson has access to 36 techniques across 7 categories stored in `brainstorming-techniques.csv`:

CategoryTechnique CountCollaborative4Structured4Creative4Deep4Theatrical4Wild4Introspective4

* * *

## Design Thinking Workflow

[Section titled “Design Thinking Workflow”](#design-thinking-workflow)

**Purpose:** Create human-centered solutions through five-phase design thinking.

```bash

# Direct command
/cis-design-thinking
# With user research context
workflowdesign-thinking--data/path/to/user-research.md
# Via agent
/cis-agent-design-thinking-coach
> design-thinking
```

InputDescriptionRequired**design\_challenge**Problem or opportunity being exploredYes**users\_stakeholders**Primary users and affected partiesNo**constraints**Time, budget, technology limitationsNo

SectionContents**Design Challenge**Framed opportunity**Point of View**User-centered problem statement**User Insights**Empathy findings and personas**How Might We Questions**Reframed as opportunities**Solution Concepts**Generated ideas**Prototypes**Testable artifacts**Test Plan**Validation approach

### Design Methods Library

[Section titled “Design Methods Library”](#design-methods-library)

Maya has access to phase-specific design methods in `design-methods.csv`.

* * *

## Innovation Strategy Workflow

[Section titled “Innovation Strategy Workflow”](#innovation-strategy-workflow)

**Purpose:** Identify disruption opportunities and business model innovation.

```bash

# Direct command
/cis-innovation-strategy
# With market context
workflowinnovation-strategy--data/path/to/market-analysis.md
# Via agent
/cis-agent-innovation-strategist
> innovation-strategy
```

InputDescriptionRequired**market\_context**Industry landscape and competitive intelligenceNo**innovation\_challenge**Strategic opportunity or threatYes**constraints**Resource limitations and strategic boundariesNo

SectionContents**Strategic Question**Innovation challenge being addressed**Market Analysis**Forces, trends, competitive landscape**Jobs-to-be-Done**Unmet customer needs**Blue Ocean Opportunities**Uncontested market spaces**Business Model**Value creation and capture**Competitive Advantages**Sustainable moats**Strategic Roadmap**Execution priorities

### Innovation Frameworks Library

[Section titled “Innovation Frameworks Library”](#innovation-frameworks-library)

Victor has access to strategic frameworks in `innovation-frameworks.csv`:

- Jobs-to-be-Done
- Blue Ocean Strategy
- Disruptive Innovation
- Business Model Canvas
- Value Chain Analysis

* * *

## Problem Solving Workflow

[Section titled “Problem Solving Workflow”](#problem-solving-workflow)

**Purpose:** Systematic problem diagnosis and root cause analysis.

```bash

# Direct command
/cis-problem-solving
# With problem brief
workflowproblem-solving--data/path/to/problem-brief.md
# Via agent
/cis-agent-creative-problem-solver
> problem-solving
```

InputDescriptionRequired**problem\_description**Challenge with symptoms and contextYes**previous\_attempts**Prior solutions and outcomesNo**constraints**Solution boundariesNo**success\_criteria**How to measure effectivenessNo

SectionContents**Problem Statement**Clearly defined challenge**Diagnosis**Root cause analysis**Solution Options**Multiple approaches with evaluation**Recommended Solution**Best option with rationale**Implementation Plan**Actionable steps**Risk Mitigation**Potential issues and prevention**Success Metrics**How to measure results

### Solving Methods Library

[Section titled “Solving Methods Library”](#solving-methods-library)

Dr. Quinn has access to analytical frameworks in `solving-methods.csv`:

- Five Whys
- TRIZ
- Theory of Constraints
- Systems Thinking
- Root Cause Analysis

* * *

## Storytelling Workflow

[Section titled “Storytelling Workflow”](#storytelling-workflow)

**Purpose:** Craft compelling narratives using proven story frameworks.

```bash

# Direct command
/cis-storytelling
# With brand context
workflowstorytelling--data/path/to/brand-info.md
# Via agent
/cis-agent-storyteller
> story
```

InputDescriptionRequired**story\_purpose**Why the story is being toldYes**target\_audience**Who will experience itYes**story\_subject**What or whom it’s aboutYes**platform\_medium**Where it will be toldNo**desired\_impact**What audience should feel/think/doNo

SectionContents**Story Framework**Structure used and rationale**Audience Profile**Who the story is for**Emotional Arc**The feeling journey**Complete Narrative**Full story with vivid details**Character Development**Voice and transformation**Platform Adaptation**Formatted for medium**Impact Plan**Effectiveness measurement

### Story Frameworks Library

[Section titled “Story Frameworks Library”](#story-frameworks-library)

Sophia has access to 25 narrative frameworks in `story-types.csv`:

- Hero’s Journey
- Story Brand
- Three-Act Structure
- Before-After-Bridge
- Pixar Pitch
- And 20 more

* * *

All workflows save output to the configured output folder (default: `./creative-outputs/` or `_bmad-output/` depending on configuration).

Output files include timestamp in format: `{workflow-name}-{YYYY-MM-DD}.md`

## Common Workflow Features

[Section titled “Common Workflow Features”](#common-workflow-features)

All CIS workflows share:

- **Interactive facilitation** — AI guides through questions, not just generation
- **Technique libraries** — CSV databases of proven methods
- **Context integration** — Optional document input for relevance
- **Structured output** — Comprehensive reports with insights and actions
- **Energy monitoring** — Adaptive pacing based on engagement

<!--THE END-->

- [**Getting Started**](https://cis-docs.bmad-method.org/tutorials/getting-started/) — Try your first workflow
- [**Agents Reference**](https://cis-docs.bmad-method.org/reference/agents/) — Learn about workflow facilitators
- [**Configuration**](https://cis-docs.bmad-method.org/reference/configuration/) — Customize workflow behavior