---
title: Automated Code Review
url: https://docs.factory.ai/guides/droid-exec/code-review.md
source: llms
fetched_at: 2026-02-05T21:43:12.765429809-03:00
rendered_js: false
word_count: 350
summary: This guide explains how to set up and configure automated code reviews using the Factory GitHub App and Droid workflows. It covers installation, review logic behavior, and customization of GitHub Action triggers and prompts.
tags:
    - github-app
    - automated-code-review
    - droid-workflow
    - ci-cd-integration
    - pull-request-automation
    - factory-ai
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Automated Code Review

> Set up automated pull request reviews using the Factory GitHub App

Set up automated code review for your repository using the Factory GitHub App. Droid will analyze pull requests, identify issues, and post feedback as inline comments.

<div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
  <div style={{ flex: '1', minWidth: '300px' }}>
    <img src="https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=8e5dc1e73e4f6e81a18f0ca761df9404" alt="Factory Droid bot posting a code review summary with issues found" data-og-width="1442" width="1442" data-og-height="682" height="682" data-path="guides/droid-exec/code-review-picture-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?w=280&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=9f606ec2b1b7adc2ab372e117ab47f34 280w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?w=560&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=a0bf0cc12a333a9c5db2186b2e8d5b82 560w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?w=840&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=84e35ee18232de966598f83471ecaef1 840w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?w=1100&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=e2e4652d031fd973b62e5caecbfa0542 1100w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?w=1650&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=16512a21ab9cb055c9d4f314e3075196 1650w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-1.png?w=2500&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=505e33328b86dd60a95b97342783534c 2500w" />
  </div>

  <div style={{ flex: '1', minWidth: '300px' }}>
    <img src="https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=c3398857ac81c4dc013dac67ed078c0f" alt="Factory Droid bot posting inline code review comment on specific lines" data-og-width="1430" width="1430" data-og-height="760" height="760" data-path="guides/droid-exec/code-review-picture-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?w=280&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=ae3bb57443c05493a60380a4239b0daa 280w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?w=560&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=05159822841d106763f0b02d432f775a 560w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?w=840&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=600f50889da1978590d9210aaa0ff83c 840w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?w=1100&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=cfbd734c4d977063243deda01ba8d0df 1100w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?w=1650&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=c6c25dc75da9b31cfa37634b774ac446 1650w, https://mintcdn.com/factory/h-qPBH0CjxqIkqbW/guides/droid-exec/code-review-picture-2.png?w=2500&fit=max&auto=format&n=h-qPBH0CjxqIkqbW&q=85&s=77847360b5dee96484c289756744eac0 2500w" />
  </div>
</div>

## Setup

Use the `/install-github-app` command to install the Factory GitHub App and configure the code review workflow:

```bash  theme={null}
droid
> /install-github-app
```

The guided flow will:

1. Verify GitHub CLI prerequisites
2. Install the Factory GitHub App on your repository
3. Let you select the **Droid Review** workflow
4. Create a PR with the workflow files

For detailed setup instructions, see the [GitHub App installation guide](/cli/features/install-github-app).

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

* Dead/unreachable code
* Broken control flow (missing break, fallthrough bugs)
* Async/await mistakes
* Null/undefined dereferences
* Resource leaks
* SQL/XSS injection vulnerabilities
* Missing error handling
* Off-by-one errors
* Race conditions

It skips stylistic concerns, minor optimizations, and architectural opinions.

## Customizing the workflow

After the workflow is created, you can customize it by editing `.github/workflows/droid-review.yml` in your repository.

### Change the trigger conditions

Modify when reviews run:

```yaml  theme={null}
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
    paths:
      - 'src/**'  # Only review changes in src/
      - '!**/*.test.ts'  # Skip test files
```

### Adjust the review focus

Edit the prompt in the workflow to change what Droid looks for. For example, to add framework-specific checks:

```yaml  theme={null}
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

```yaml  theme={null}
droid exec --auto high --model claude-sonnet-4-5-20250929 -f prompt.txt
# Or use a faster model for quicker feedback:
droid exec --auto high --model claude-haiku-4-5-20251001 -f prompt.txt
```

### Skip certain PRs

Add conditions to skip reviews for specific cases:

```yaml  theme={null}
jobs:
  code-review:
    # Skip bot PRs and PRs with [skip-review] in title
    if: |
      github.event.pull_request.draft == false &&
      !contains(github.event.pull_request.user.login, '[bot]') &&
      !contains(github.event.pull_request.title, '[skip-review]')
```

### Limit comment count

Adjust the maximum number of comments in the prompt:

```
Guidelines:
- Submit at most 5 comments total, prioritizing the most critical issues
```

## See also

* [GitHub App installation](/cli/features/install-github-app) - Full setup guide for `/install-github-app`
* [GitHub Actions examples](/guides/droid-exec/github-actions) - More automation workflows
* [Droid Exec](/cli/commands/exec) - Running Droid in CI/CD environments