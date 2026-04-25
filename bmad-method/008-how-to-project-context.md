---
title: Manage Project Context
url: https://docs.bmad-method.org/how-to/project-context/
source: sitemap
fetched_at: 2026-04-08T11:31:17.332343025-03:00
rendered_js: false
word_count: 374
summary: This document explains the purpose and methods for creating a `project-context.md` file to enforce technical preferences, implementation rules, and established patterns across AI agent workflows working on a project.
tags:
    - ai-agent-guidance
    - project-context
    - coding-standards
    - workflow-documentation
    - best-practices
    - codebase-patterns
category: guide
---

Use the `project-context.md` file to ensure AI agents follow your project’s technical preferences and implementation rules throughout all workflows. To make sure this is always available, you can also add the line `Important project context and conventions are located in [path to project context]/project-context.md` to your tools context or always rules file (such as `AGENTS.md`)

- You have strong technical preferences before starting architecture
- You’ve completed architecture and want to capture decisions for implementation
- You’re working on an existing codebase with established patterns
- You notice agents making inconsistent decisions across stories

## Step 1: Choose Your Approach

[Section titled “Step 1: Choose Your Approach”](#step-1-choose-your-approach)

**Manual creation** — Best when you know exactly what rules you want to document

**Generate after architecture** — Best for capturing decisions made during solutioning

**Generate for existing projects** — Best for discovering patterns in existing codebases

## Step 2: Create the File

[Section titled “Step 2: Create the File”](#step-2-create-the-file)

### Option A: Manual Creation

[Section titled “Option A: Manual Creation”](#option-a-manual-creation)

Create the file at `_bmad-output/project-context.md`:

```bash

mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Add your technology stack and implementation rules:

```markdown

---
project_name: 'MyProject'
user_name: 'YourName'
date: '2026-02-15'
sections_completed: ['technology_stack', 'critical_rules']
---
# Project Context for AI Agents
## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand
- Testing: Vitest, Playwright
- Styling: Tailwind CSS
## Critical Implementation Rules
**TypeScript:**
- Strict mode enabled, no `any` types
- Use `interface` for public APIs, `type` for unions
**Code Organization:**
- Components in `/src/components/` with co-located tests
- API calls use `apiClient` singleton — never fetch directly
**Testing:**
- Unit tests focus on business logic
- Integration tests use MSW for API mocking
```

### Option B: Generate After Architecture

[Section titled “Option B: Generate After Architecture”](#option-b-generate-after-architecture)

Run the workflow in a fresh chat:

```bash

bmad-generate-project-context
```

The workflow scans your architecture document and project files to generate a context file capturing the decisions made.

### Option C: Generate for Existing Projects

[Section titled “Option C: Generate for Existing Projects”](#option-c-generate-for-existing-projects)

For existing projects, run:

```bash

bmad-generate-project-context
```

The workflow analyzes your codebase to identify conventions, then generates a context file you can review and refine.

## Step 3: Verify Content

[Section titled “Step 3: Verify Content”](#step-3-verify-content)

Review the generated file and ensure it captures:

- Correct technology versions
- Your actual conventions (not generic best practices)
- Rules that prevent common mistakes
- Framework-specific patterns

Edit manually to add anything missing or remove inaccuracies.

A `project-context.md` file that:

- Ensures all agents follow the same conventions
- Prevents inconsistent decisions across stories
- Captures architecture decisions for implementation
- Serves as a reference for your project’s patterns and rules

<!--THE END-->

- [**Project Context Explanation**](https://docs.bmad-method.org/explanation/project-context/) — Learn more about how it works
- [**Workflow Map**](https://docs.bmad-method.org/reference/workflow-map/) — See which workflows load project context