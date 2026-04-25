---
title: Established Projects
url: https://docs.bmad-method.org/how-to/established-projects/
source: sitemap
fetched_at: 2026-04-08T11:31:09.405608006-03:00
rendered_js: false
word_count: 497
summary: This guide outlines the essential workflow for using the BMad Method when working within existing or legacy software projects. It details steps such as cleaning up planning artifacts, generating project context, and maintaining quality documentation to ensure new work aligns with the current codebase.
tags:
    - bmad-method
    - legacy-codebase
    - project-onboarding
    - context-generation
    - documentation
category: guide
---

Use BMad Method effectively when working on existing projects and legacy codebases.

This guide covers the essential workflow for onboarding to existing projects with BMad Method.

## Step 1: Clean Up Completed Planning Artifacts

[Section titled “Step 1: Clean Up Completed Planning Artifacts”](#step-1-clean-up-completed-planning-artifacts)

If you have completed all PRD epics and stories through the BMad process, clean up those files. Archive them, delete them, or rely on version history if needed. Do not keep these files in:

- `docs/`
- `_bmad-output/planning-artifacts/`
- `_bmad-output/implementation-artifacts/`

## Step 2: Create Project Context

[Section titled “Step 2: Create Project Context”](#step-2-create-project-context)

Run the generate project context workflow:

```bash

bmad-generate-project-context
```

This scans your codebase to identify:

- Technology stack and versions
- Code organization patterns
- Naming conventions
- Testing approaches
- Framework-specific patterns

You can review and refine the generated file, or create it manually at `_bmad-output/project-context.md` if you prefer.

[Learn more about project context](https://docs.bmad-method.org/explanation/project-context/)

## Step 3: Maintain Quality Project Documentation

[Section titled “Step 3: Maintain Quality Project Documentation”](#step-3-maintain-quality-project-documentation)

Your `docs/` folder should contain succinct, well-organized documentation that accurately represents your project:

- Intent and business rationale
- Business rules
- Architecture
- Any other relevant project information

For complex projects, consider using the `bmad-document-project` workflow. It offers runtime variants that will scan your entire project and document its actual current state.

### BMad-Help: Your Starting Point

[Section titled “BMad-Help: Your Starting Point”](#bmad-help-your-starting-point)

**Run `bmad-help` anytime you’re unsure what to do next.** This intelligent guide:

- Inspects your project to see what’s already been done
- Shows options based on your installed modules
- Understands natural language queries

```plaintext

bmad-help I have an existing Rails app, where should I start?
bmad-help What's the difference between quick-flow and full method?
bmad-help Show me what workflows are available
```

BMad-Help also **automatically runs at the end of every workflow**, providing clear guidance on exactly what to do next.

### Choosing Your Approach

[Section titled “Choosing Your Approach”](#choosing-your-approach)

You have two primary options depending on the scope of changes:

ScopeRecommended Approach**Small updates or additions**Run `bmad-quick-dev` to clarify intent, plan, implement, and review in a single workflow. The full four-phase BMad Method is likely overkill.**Major changes or additions**Start with the BMad Method, applying as much or as little rigor as needed.

### During PRD Creation

[Section titled “During PRD Creation”](#during-prd-creation)

When creating a brief or jumping directly into the PRD, ensure the agent:

- Finds and analyzes your existing project documentation
- Reads the proper context about your current system

You can guide the agent explicitly, but the goal is to ensure the new feature integrates well with your existing system.

### UX Considerations

[Section titled “UX Considerations”](#ux-considerations)

UX work is optional. The decision depends not on whether your project has a UX, but on:

- Whether you will be working on UX changes
- Whether significant new UX designs or patterns are needed

If your changes amount to simple updates to existing screens you are happy with, a full UX process is unnecessary.

### Architecture Considerations

[Section titled “Architecture Considerations”](#architecture-considerations)

When doing architecture, ensure the architect:

- Uses the proper documented files
- Scans the existing codebase

Pay close attention here to prevent reinventing the wheel or making decisions that misalign with your existing architecture.

- [**Quick Fixes**](https://docs.bmad-method.org/how-to/quick-fixes/) - Bug fixes and ad-hoc changes
- [**Established Projects FAQ**](https://docs.bmad-method.org/explanation/established-projects-faq/) - Common questions about working on established projects