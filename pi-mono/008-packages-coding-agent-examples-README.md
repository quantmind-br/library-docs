---
title: README
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/examples/README.md
source: git
fetched_at: 2026-03-03T03:41:38.057469-03:00
rendered_js: false
word_count: 105
summary: An introductory guide with essential setup instructions, dependencies, and installation notes for the project.
tags:
    - setup
    - guide
    - instructions
category: guide
---

# Examples

Example code for pi-coding-agent SDK and extensions.

## Directories

### [sdk/](sdk/)
Programmatic usage via `createAgentSession()`. Shows how to customize models, prompts, tools, extensions, and session management.

### [extensions/](extensions/)
Example extensions demonstrating:
- Lifecycle event handlers (tool interception, safety gates, context modifications)
- Custom tools (todo lists, questions, subagents, output truncation)
- Commands and keyboard shortcuts
- Custom UI (footers, headers, editors, overlays)
- Git integration (checkpoints, auto-commit)
- System prompt modifications and custom compaction
- External integrations (SSH, file watchers, system theme sync)
- Custom providers (Anthropic with custom streaming, GitLab Duo)

## Documentation

- [SDK Reference](sdk/README.md)
- [Extensions Documentation](../docs/extensions.md)
- [Skills Documentation](../docs/skills.md)
