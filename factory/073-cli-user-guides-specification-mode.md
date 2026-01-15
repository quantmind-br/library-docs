---
title: Specification Mode - Factory Documentation
url: https://docs.factory.ai/cli/user-guides/specification-mode
source: sitemap
fetched_at: 2026-01-13T19:03:49.557217244-03:00
rendered_js: false
word_count: 706
summary: Explains Specification Mode, a feature that transforms feature descriptions into implementation plans through analysis and planning phases before code execution.
tags:
    - specification-mode
    - planning
    - workflow
    - cli
    - code-generation
    - security
    - autonomy-levels
category: guide
---

Specification Mode transforms simple feature descriptions into working code with automatic planning and safety checks. You provide a brief description of what you want, and droid creates a detailed specification and implementation plan before making any changes.

## How it works

## Example workflow

**Your input:**

```
Add a feature for users to export their personal data.
It should create a ZIP file with their profile, posts, and uploaded files.
Send them an email when it's ready. Make sure it follows GDPR requirements.
The export should work for accounts up to 2GB of data.
```

**Droid generates:**

- Complete specification with detailed acceptance criteria
- Technical implementation plan covering backend, frontend, and email
- File-by-file breakdown of changes needed
- Testing strategy and verification steps
- Security and compliance considerations

**You approve, then droid implements** the complete solution while showing each change for review.

## How to activate Specification Mode

To enter Specification Mode, press **Shift+Tab** while in the CLI. This will enable the specification planning workflow for your next request.

## What happens during planning

**Analysis phase (read-only):**

- Examines your existing codebase and patterns
- Reviews related files and dependencies
- Studies your AGENTS.md conventions
- Gathers context from external sources

**Planning phase:**

- Develops comprehensive implementation strategy
- Identifies all files that need changes
- Plans sequence of modifications
- Considers testing and verification steps

**Safety guarantees:**

- Cannot edit files during analysis
- Cannot run commands that modify anything
- Cannot create, delete, or move files
- All exploration is read-only until you approve

## Writing effective requests

**Focus on outcomes:** Describe what the software should accomplish, not how to build it.

```
Users need to be able to reset their passwords using email verification.
The reset link should expire after 24 hours for security.
Include rate limiting to prevent abuse.
```

**Include important constraints:**

```
Add user data export functionality that works for accounts up to 5GB.
Must comply with GDPR and include audit logging.
Should complete within 10 minutes and not impact application performance.
```

**Reference existing patterns:**

```
Add a notification system similar to how we handle email confirmations.
Use the same background job pattern as our existing report generation.
Follow the authentication patterns we use for other sensitive operations.
```

**Be specific about verification:** Tell droid how to confirm the implementation works correctly. **Consider the full user journey:** Describe the complete experience, not just technical requirements. **Include error scenarios:** Specify how failures should be handled and communicated to users. **Think about scale:** Mention performance requirements and expected usage patterns.

## Enterprise integration

Reference external requirements by pasting links:

```
Implement the user management features described in this Jira ticket:
https://company.atlassian.net/browse/PROJ-123

Follow our security standards and include comprehensive error handling.
```

If you’ve integrated platforms through Factory’s dashboard, droid can read context from tickets, documents, and specs during analysis.

## Benefits

## AGENTS.md integration

Document your project conventions to enhance Specification Mode’s planning. See [AGENTS.md](https://docs.factory.ai/cli/configuration/agents-md) for more information. Specification Mode automatically incorporates these conventions, ensuring consistency with your team’s standards.

## Breaking down large features

For complex features spanning multiple components, break them into focused phases: **Phase 1:**

```
Implement user data export backend API and job processing.
Focus only on the server-side functionality, not the UI yet.
```

**Phase 2:**

```
Add the frontend UI for data export using the API from Phase 1.
Include progress indicators and download management.
```

This approach allows you to validate each phase before proceeding to the next.

## Specification approval options

After droid presents the specification, choose how to continue:

1. **Proceed with implementation** – Approve the plan and keep normal (manual) execution controls.
2. **Proceed, and allow file edits and read-only commands (Low)** – Enable low autonomy auto-run so droid can edit files and run safe read-only commands automatically.
3. **Proceed, and allow reversible commands (Medium)** – Enable medium autonomy auto-run so droid can also run reversible commands without additional prompts.
4. **Proceed, and allow all commands (High)** – Enable high autonomy auto-run for fully automated execution, including commands that are not easily reversible.
5. **No, keep iterating on spec** – Stay in Specification Mode to refine the plan before implementation.

Selecting any auto-run option sets the corresponding autonomy level for the rest of the session. Choosing to keep iterating leaves Specification Mode active so you can continue shaping the plan.

## Saving your specifications as Markdown

Specification Mode can automatically write the approved plan to disk. Open the CLI settings and enable **Save spec as Markdown** to turn this on.

- By default, plans are saved to `.factory/docs` inside the nearest project-level `.factory` directory. If none exists, the CLI falls back to `~/.factory/docs` in your home directory.
- Use the **Spec save directory** setting to pick between the project directory, your home directory, or a custom path. Custom values support absolute paths, `~` expansion, `.factory/...` shortcuts, and relative paths from the current workspace.
- The CLI creates the target directory if it does not exist and writes the Markdown exactly as shown in the approval dialog.
- Files are named `YYYY-MM-DD-slug.md`, where the slug comes from the spec title or first heading, and a counter is appended if a file with the same name already exists.

## What happens after approval

Once you approve a specification plan, droid systematically implements the changes while showing each modification for review. You maintain full control through the approval workflow, ensuring quality and alignment with requirements. For simpler changes that don’t need comprehensive planning, droid can proceed directly while still showing all modifications for approval. Ready to try Specification Mode? Start with a simple description of what you want to build, and let droid handle the specification and planning complexity.