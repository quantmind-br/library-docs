---
title: Automated Code Review - Factory Documentation
url: https://docs.factory.ai/guides/droid-exec/code-review
source: sitemap
fetched_at: 2026-01-13T19:03:42.987194933-03:00
rendered_js: false
word_count: 308
summary: This guide explains how to configure and customize the Factory Droid GitHub App for automated code review, detailing the setup process, triggering mechanisms, and review scope.
tags:
    - github-app
    - code-review
    - automation
    - ci-cd
    - pull-request
    - droid-exec
    - configuration
category: guide
---

Set up automated code review for your repository using the Factory GitHub App. Droid will analyze pull requests, identify issues, and post feedback as inline comments.

![Factory Droid bot posting a code review summary with issues found](https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=8e5dc1e73e4f6e81a18f0ca761df9404)

![Factory Droid bot posting inline code review comment on specific lines](https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=c3398857ac81c4dc013dac67ed078c0f)

## Setup

Use the `/install-gh-app` command to install the Factory GitHub App and configure the code review workflow:

The guided flow will:

1. Verify GitHub CLI prerequisites
2. Install the Factory GitHub App on your repository
3. Let you select the **Droid Review** workflow
4. Create a PR with the workflow files

For detailed setup instructions, see the [GitHub App installation guide](https://docs.factory.ai/cli/features/install-github-app).

## How it works

Once enabled, the Droid Review workflow:

1. Triggers on pull request events (opened, synchronized, reopened, ready for review)
2. Skips draft PRs to avoid noise during development
3. Fetches the PR diff and existing comments
4. Analyzes code changes for issues
5. Posts inline comments on problematic lines
6. Submits an approval when no issues are found

## What Droid reviews

The automated reviewer focuses on clear bugs and issues:

- Dead/unreachable code
- Broken control flow (missing break, fallthrough bugs)
- Async/await mistakes
- Null/undefined dereferences
- Resource leaks
- SQL/XSS injection vulnerabilities
- Missing error handling
- Off-by-one errors
- Race conditions

It skips stylistic concerns, minor optimizations, and architectural opinions.

## Customizing the workflow

After the workflow is created, you can customize it by editing `.github/workflows/droid-review.yml` in your repository.

### Change the trigger conditions

Modify when reviews run:

```
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
    paths:
      - 'src/**'  # Only review changes in src/
      - '!**/*.test.ts'  # Skip test files
```

### Adjust the review focus

Edit the prompt in the workflow to change what Droid looks for. For example, to add framework-specific checks:

```
run: |
  cat > prompt.txt << 'EOF'
  You are an automated code review system...

  Additional checks for this codebase:
  - React hooks rules violations
  - Missing TypeScript types on public APIs
  - Prisma query performance issues
  EOF
```

### Change the model

Use a different model for reviews:

```
droid exec --auto high --model claude-sonnet-4-5-20250929 -f prompt.txt
# Or use a faster model for quicker feedback:
droid exec --auto high --model claude-haiku-4-5-20251001 -f prompt.txt
```

### Skip certain PRs

Add conditions to skip reviews for specific cases:

```
jobs:
  code-review:
    # Skip bot PRs and PRs with [skip-review] in title
    if: |
      github.event.pull_request.draft == false &&
      !contains(github.event.pull_request.user.login, '[bot]') &&
      !contains(github.event.pull_request.title, '[skip-review]')
```

Adjust the maximum number of comments in the prompt:

```
Guidelines:
- Submit at most 5 comments total, prioritizing the most critical issues
```

## See also

- [GitHub App installation](https://docs.factory.ai/cli/features/install-github-app) - Full setup guide for `/install-gh-app`
- [GitHub Actions examples](https://docs.factory.ai/guides/droid-exec/github-actions) - More automation workflows
- [Droid Exec](https://docs.factory.ai/cli/commands/exec) - Running Droid in CI/CD environments