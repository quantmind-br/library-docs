---
title: "Custom Rules Guide for ForgeCode"
url: https://forgecode.dev/docs/custom-rules-guide/
source: sitemap
fetched_at: 2026-04-30T14:09:04.335012338-03:00
rendered_js: false
word_count: 365
summary: "Standardize AI coding behavior in ForgeCode by defining project-specific rules in an `AGENTS.md` file."
tags:
  - ai-agents
  - coding-standards
  - developer-productivity
  - system-prompts
  - project-configuration
  - markdown-guidelines
category: configuration
optimized: true
---
# Custom Rules Guide for ForgeCode

> **TL;DR**
> Define team standards in `AGENTS.md` to guide AI behavior persistently.

## Why Use Custom Rules?
- **Consistency**: AI follows team standards automatically.
- **Efficiency**: No need to repeat guidelines in every session.
- **Priority**: Overrides default AI behaviors.

## How It Works

### File Location Priority
1. **Base path** (`environment.base_path`)
2. **Git root**
3. **Current directory** (`environment.cwd`)

> **Note**: First `AGENTS.md` found is used.

### Injection Process
1. Search for `AGENTS.md`.
2. Parse Markdown content.
3. Inject into AI system prompt.
4. Apply to all responses.

## Getting Started

### Basic Setup
Create `AGENTS.md` in project root:
```markdown
# Project Guidelines

- **Code Style**: Follow Prettier + ESLint.
- **Testing**: Write tests for all new features.
- **Error Handling**: Use custom `AppError` class.
```

### Example: Before/After
| Scenario | Before | After |
|----------|--------|-------|
| **Code Style** | Inconsistent | Prettier + ESLint |
| **Testing** | Manual | Automated tests |
| **Error Handling** | Generic | `AppError` |

## Rule Levels

| Level | Focus | Example |
|-------|-------|---------|
| **1** | Basic standards | Code style, testing |
| **2** | Language-specific | React hooks, Python type hints |
| **3** | Architecture | Microservices, event sourcing |

### Level 1: Basic Standards
```markdown
# Core Rules
- Use 2-space indentation.
- Write docstrings for all public methods.
- Commit messages: `<type>(<scope>): <subject>`.
```

### Level 2: Language-Specific
```markdown
# React/TypeScript
- Use `useReducer` for complex state.
- Type all props and hooks.

# Python
- Use `mypy` for static typing.
- Follow Black formatting.
```

### Level 3: Architecture
```markdown
# System Design
- Use CQRS for data operations.
- Event sourcing for audit trails.
```

## Advanced Features

### Conditional Rules
```markdown
# Frontend Rules (*.tsx)
- Use `styled-components` for CSS.

# Backend Rules (*.py)
- Use `pydantic` for data validation.
```

### Environment-Specific
```markdown
# Production
- Enable strict type checking.

# Development
- Allow `any` types for prototyping.
```

## Best Practices

| Do | Don’t |
|----|------|
| Be specific | Vague instructions |
| Use bullet points | Walls of text |
| Group related rules | Scatter rules |
| Start small | Overload initially |

## Debugging

| Issue | Solution |
|-------|----------|
| Rules not applied | Check file location/name, restart session |
| Conflicting rules | Review for contradictions |
| Vague rules | Add specificity |
| Too many rules | Start with 3–5 core rules |

## Team Adoption

1. **Consensus**: Agree on 3–5 core rules.
2. **Document**: Explain the "why" for each rule.
3. **Iterate**: Update as practices evolve.
4. **Share**: Show before/after examples.

## Example Workflow

1. Create `AGENTS.md`.
2. Add 3–5 basic rules.
3. Test with a small feature.
4. Ask AI: "What guidelines are you following?"
5. Iterate based on results.

## Related Guides
- [Agent Selection](https://forgecode.dev/docs/operating-agents/)
- [Model Selection](https://forgecode.dev/docs/model-selection-guide/)
- [File Tagging](https://forgecode.dev/docs/file-tagging/)
- [Plan and Act](https://forgecode.dev/docs/plan-and-act-guide/)