---
title: Using Skills | goose
url: https://block.github.io/goose/docs/guides/context-engineering/using-skills
source: github_pages
fetched_at: 2026-01-22T22:13:43.730010935-03:00
rendered_js: true
word_count: 414
summary: This document explains how to create and manage Skills in Goose, which are reusable sets of instructions and resources for specific workflows. It covers file structure, storage locations, and best practices for implementing custom task-based automation.
tags:
    - goose-ai
    - skills
    - workflow-automation
    - project-configuration
    - ai-instructions
    - developer-tools
category: guide
---

Skills are reusable sets of instructions and resources that teach goose how to perform specific tasks. A skill can range from a simple checklist to a detailed workflow with domain expertise, and can include supporting files like scripts or templates. Example use cases include deployment procedures, code review checklists, and API integration guides.

info

This functionality requires the built-in [Skills extension](https://block.github.io/goose/docs/mcp/skills-mcp) to be enabled (it's enabled by default).

When a session starts, goose adds any skills that it discovers to its instructions. During the session, goose automatically loads a skill when:

- Your request clearly matches a skill's purpose
- You explicitly ask to use a skill, for example:
  
  - "Use the code-review skill to review this PR"
  - "Follow the new-service skill to set up the auth service"
  - "Apply the deployment skill"

You can also ask goose what skills are available.

## Skill Locations[​](#skill-locations "Direct link to Skill Locations")

Skills can be stored globally and/or per-project. goose checks all of these directories in order and combines what it finds. If the same skill name exists in multiple directories, later directories take priority:

1. `~/.claude/skills/` — Global, shared with Claude Desktop
2. `~/.config/agents/skills/` — Global, portable across AI coding agents
3. `~/.config/goose/skills/` — Global, goose-specific
4. `./.claude/skills/` — Project-level, shared with Claude Desktop
5. `./.goose/skills/` — Project-level, goose-specific
6. `./.agents/skills/` — Project-level, portable across AI coding agents

Use global skills for workflows you use across projects. Use project-level skills for procedures unique to a codebase.

## Creating a Skill[​](#creating-a-skill "Direct link to Creating a Skill")

Create a skill when you have a repeatable workflow that involves multiple steps, specialized knowledge, or supporting files.

### Skill File Structure[​](#skill-file-structure "Direct link to Skill File Structure")

Each skill lives in its own directory with a `SKILL.md` file:

```
~/.config/agents/skills/
└── code-review/
    └── SKILL.md
```

A `SKILL.md` file requires YAML frontmatter with `name` and `description`, followed by the skill content:

```
---
name: code-review
description: Comprehensive code review checklist for pull requests
---

# Code Review Checklist

When reviewing code, check each of these areas:

## Functionality
- [ ] Code does what the PR description claims
- [ ] Edge cases are handled
- [ ] Error handling is appropriate

## Code Quality
- [ ] Follows project style guide
- [ ] No hardcoded values that should be configurable
- [ ] Functions are focused and well-named

## Testing
- [ ] New functionality has tests
- [ ] Tests are meaningful, not just for coverage
- [ ] Existing tests still pass

## Security
- [ ] No credentials or secrets in code
- [ ] User input is validated
- [ ] SQL queries are parameterized
```

### Supporting Files[​](#supporting-files "Direct link to Supporting Files")

Skills can include supporting files like scripts, templates, or configuration files. Place them in the skill directory:

```
~/.config/agents/skills/
└── api-setup/
    ├── SKILL.md
    ├── setup.sh
    └── templates/
        └── config.template.json
```

When goose loads the skill, it sees the supporting files and can access them using the [Developer extension's](https://block.github.io/goose/docs/mcp/developer-mcp) file tools.

Example Skill with Supporting Files

## Common Use Case Examples[​](#common-use-case-examples "Direct link to Common Use Case Examples")

Deployment Workflow

Testing Strategy

API Integration Guide

Other goose features that support reuse

- [.goosehints](https://block.github.io/goose/docs/guides/context-engineering/using-goosehints): Best for general preferences, project context, and repeated instructions like "Always use TypeScript"
- [recipes](https://block.github.io/goose/docs/guides/recipes/session-recipes): Shareable configurations that package instructions, prompts, and settings together

## Best Practices[​](#best-practices "Direct link to Best Practices")

- **Keep skills focused** — One skill per workflow or domain. If a skill is getting long, consider splitting it.
- **Write for clarity** — Skills are instructions for goose. Use clear, direct language and numbered steps.
- **Include verification steps** — Help goose confirm the workflow completed successfully.

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")