---
title: Project Context
url: https://docs.bmad-method.org/explanation/project-context/
source: sitemap
fetched_at: 2026-04-08T11:30:03.121970766-03:00
rendered_js: false
word_count: 635
summary: This document explains the purpose and usage of `project-context.md`, a crucial file designed to guide AI agents by documenting project-specific rules, patterns, and technical constraints. It details when to create or update this file and how various workflows automatically incorporate its established context.
tags:
    - ai-agent-guidance
    - project-setup
    - llm-context
    - coding-standards
    - workflow-guide
category: guide
---

The `project-context.md` file is your project’s implementation guide for AI agents. Similar to a “constitution” in other development systems, it captures the rules, patterns, and preferences that ensure consistent code generation across all workflows.

AI agents make implementation decisions constantly — which patterns to follow, how to structure code, what conventions to use. Without clear guidance, they may:

- Follow generic best practices that don’t match your codebase
- Make inconsistent decisions across different stories
- Miss project-specific requirements or constraints

The `project-context.md` file solves this by documenting what agents need to know in a concise, LLM-optimized format.

Every implementation workflow automatically loads `project-context.md` if it exists. The architect workflow also loads it to respect your technical preferences when designing the architecture.

**Loaded by these workflows:**

- `bmad-create-architecture` — respects technical preferences during solutioning
- `bmad-create-story` — informs story creation with project patterns
- `bmad-dev-story` — guides implementation decisions
- `bmad-code-review` — validates against project standards
- `bmad-quick-dev` — applies patterns when implementing specs
- `bmad-sprint-planning`, `bmad-retrospective`, `bmad-correct-course` — provides project-wide context

## When to Create It

[Section titled “When to Create It”](#when-to-create-it)

The `project-context.md` file is useful at any stage of a project:

ScenarioWhen to CreatePurpose**New project, before architecture**Manually, before `bmad-create-architecture`Document your technical preferences so the architect respects them**New project, after architecture**Via `bmad-generate-project-context` or manuallyCapture architecture decisions for implementation agents**Existing project**Via `bmad-generate-project-context`Discover existing patterns so agents follow established conventions**Quick Flow project**Before or during `bmad-quick-dev`Ensure quick implementation respects your patterns

The file has two main sections:

### Technology Stack & Versions

[Section titled “Technology Stack & Versions”](#technology-stack--versions)

Documents the frameworks, languages, and tools your project uses with specific versions:

```markdown

## Technology Stack & Versions
- Node.js 20.x, TypeScript 5.3, React 18.2
- State: Zustand (not Redux)
- Testing: Vitest, Playwright, MSW
- Styling: Tailwind CSS with custom design tokens
```

### Critical Implementation Rules

[Section titled “Critical Implementation Rules”](#critical-implementation-rules)

Documents patterns and conventions that agents might otherwise miss:

```markdown

## Critical Implementation Rules
**TypeScript Configuration:**
- Strict mode enabled — no `any` types without explicit approval
- Use `interface` for public APIs, `type` for unions/intersections
**Code Organization:**
- Components in `/src/components/` with co-located `.test.tsx`
- Utilities in `/src/lib/` for reusable pure functions
- API calls use the `apiClient` singleton — never fetch directly
**Testing Patterns:**
- Unit tests focus on business logic, not implementation details
- Integration tests use MSW to mock API responses
- E2E tests cover critical user journeys only
**Framework-Specific:**
- All async operations use the `handleError` wrapper for consistent error handling
- Feature flags accessed via `featureFlag()` from `@/lib/flags`
- New routes follow the file-based routing pattern in `/src/app/`
```

Focus on what’s **unobvious** — things agents might not infer from reading code snippets. Don’t document standard practices that apply universally.

## Creating the File

[Section titled “Creating the File”](#creating-the-file)

You have three options:

Create the file at `_bmad-output/project-context.md` and add your rules:

```bash

# In your project root
mkdir-p_bmad-output
touch_bmad-output/project-context.md
```

Edit it with your technology stack and implementation rules. The architect and implementation workflows will automatically find and load it.

### Generate After Architecture

[Section titled “Generate After Architecture”](#generate-after-architecture)

Run the `bmad-generate-project-context` workflow after completing your architecture:

```bash

bmad-generate-project-context
```

This scans your architecture document and project files to generate a context file capturing the decisions made.

### Generate for Existing Projects

[Section titled “Generate for Existing Projects”](#generate-for-existing-projects)

For existing projects, run `bmad-generate-project-context` to discover existing patterns:

```bash

bmad-generate-project-context
```

The workflow analyzes your codebase to identify conventions, then generates a context file you can review and refine.

Without `project-context.md`, agents make assumptions that may not match your project:

Without ContextWith ContextUses generic patternsFollows your established conventionsInconsistent style across storiesConsistent implementationMay miss project-specific constraintsRespects all technical requirementsEach agent decides independentlyAll agents align with same rules

This is especially important for:

- **Quick Flow** — skips PRD and architecture, so context file fills the gap
- **Team projects** — ensures all agents follow the same standards
- **Existing projects** — prevents breaking established patterns

## Editing and Updating

[Section titled “Editing and Updating”](#editing-and-updating)

The `project-context.md` file is a living document. Update it when:

- Architecture decisions change
- New conventions are established
- Patterns evolve during implementation
- You identify gaps from agent behavior

You can edit it manually at any time, or re-run `bmad-generate-project-context` to update it after significant changes.