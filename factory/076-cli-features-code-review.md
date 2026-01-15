---
title: Code Review - Factory Documentation
url: https://docs.factory.ai/cli/features/code-review
source: sitemap
fetched_at: 2026-01-13T19:04:36.867896024-03:00
rendered_js: false
word_count: 593
summary: Explains the functionality and configuration of the /review command, an interactive CLI tool for performing AI-powered code analysis on branches, uncommitted changes, and specific commits.
tags:
    - code-review
    - cli
    - git
    - automation
    - workflows
    - bug-detection
category: guide
---

## Overview

The `/review` command provides an interactive workflow for analyzing code changes with AI-powered insights. It offers multiple review modes to fit different development scenarios—from reviewing uncommitted changes to analyzing full branches or specific commits. When you run `/review`, droid guides you through selecting a review type, configuring parameters, and then performs a comprehensive analysis of your code changes based on industry-standard review guidelines.

## Quick start

## Review types

### Review against a base branch

Compare your current branch against a base branch (like a pull request review). This is ideal for pre-PR reviews or checking what changes would be merged. **How it works:**

1. Select “Review against a base branch”
2. Choose your target base branch from the list (local and remote branches shown)
3. Droid finds the merge base and reviews the diff

**Use cases:**

- Pre-commit PR reviews
- Checking branch changes before creating a pull request
- Validating feature branch against main/develop

**Example workflow:**

```
> /review
# Select: Review against a base branch
# Choose: origin/main
# Droid reviews all changes that would be merged
```

### Review uncommitted changes

Analyze all current working directory changes—staged files, unstaged modifications, and untracked files. **Use cases:**

- Quick sanity check before committing
- Reviewing work in progress
- Finding issues early in development

**Example workflow:**

```
> /review
# Select: Review uncommitted changes
# Droid immediately reviews all working directory changes
```

### Review a commit

Examine the changes introduced by a specific commit in your repository history. **How it works:**

1. Select “Review a commit”
2. Browse commits with hash, message, author, and date
3. Select a commit to review

**Use cases:**

- Reviewing recent commits for issues
- Understanding changes in a specific commit
- Post-merge review of teammate’s work

**Example workflow:**

```
> /review
# Select: Review a commit
# Browse and select: abc1234 - "Add user authentication"
# Droid reviews that specific commit's changes
```

### Custom review instructions

Define your own review criteria for specialized analysis. **Use cases:**

- Security-focused reviews
- Performance analysis
- Checking specific coding standards
- Domain-specific validations

**Example workflow:**

```
> /review
# Select: Custom review instructions
# Enter: "Check for SQL injection vulnerabilities and ensure all database queries use parameterized statements"
# Droid performs a targeted security review
```

## Review guidelines

All code reviews follow a structured rubric designed to provide actionable, high-quality feedback:

### Severity levels

Reviews categorize findings using priority levels:

- **\[P0]** - Critical issues blocking release or operations
- **\[P1]** - Urgent issues that should be addressed in the next cycle
- **\[P2]** - Normal priority issues to fix eventually
- **\[P3]** - Low priority nice-to-have improvements

### Bug detection criteria

The AI only flags issues as bugs when they meet ALL of these criteria:

1. **Meaningful impact** - Affects accuracy, performance, security, or maintainability
2. **Discrete and actionable** - Clear, specific issue with a clear fix
3. **Appropriate rigor** - Fix doesn’t demand more rigor than the rest of the codebase
4. **Introduced in changes** - Bug was added in the reviewed changes (not pre-existing)
5. **Worth fixing** - Author would likely fix if made aware
6. **No unstated assumptions** - Based on verifiable facts, not speculation
7. **Provably affected** - Can identify specific affected code, not theoretical
8. **Not intentional** - Clearly not a deliberate design choice

Review comments follow these principles:

- **Clear reasoning** - Explains why something is an issue
- **Appropriate severity** - Communicates impact accurately
- **Brief** - Maximum 1 paragraph per finding
- **Minimal code** - Code chunks limited to 3 lines in markdown
- **Scenario-specific** - Describes affected environments/conditions
- **Matter-of-fact tone** - Avoids accusatory language
- **Immediately graspable** - Easy for the author to understand
- **No excessive flattery** - Focuses on actionable feedback

### Output format

Each finding includes:

- **Clear title** (≤80 characters, imperative mood)
- **Explanation** of why this is a problem
- **File path and line numbers** where applicable
- **Priority level** \[P0-P3]
- **Suggested fix** (when concrete replacement code is available)

Plus an **overall assessment**:

- Whether changes are correct or incorrect
- 1-3 sentence summary

## Tips and best practices

## Examples

### Pre-PR review

```
# Before creating a pull request
> /review
# Select: Review against a base branch
# Choose: origin/main
# Review findings, fix issues, then create PR
```

### Quick WIP check

```
# Check work in progress
> /review
# Select: Review uncommitted changes
# Get immediate feedback on current changes
```

### Security-focused review

```
# Custom security review
> /review
# Select: Custom review instructions
# Enter: "Check for security vulnerabilities: SQL injection, XSS, CSRF, insecure dependencies, exposed secrets, and authentication bypasses"
```

### Post-merge review

```
# Review a teammate's recent commit
> /review
# Select: Review a commit
# Choose the recent commit to understand changes
```

## See also

- [CLI Reference](https://docs.factory.ai/reference/cli-reference) - Complete command reference including `/review`
- [Code Review automation guide](https://docs.factory.ai/guides/droid-exec/code-review) - Automate reviews with `droid exec`
- [Common use cases](https://docs.factory.ai/cli/getting-started/common-use-cases) - Other workflows and patterns
- [How to talk to a droid](https://docs.factory.ai/cli/getting-started/how-to-talk-to-a-droid) - Getting better results from AI reviews