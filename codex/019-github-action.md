---
title: Codex GitHub Action
url: https://developers.openai.com/codex/github-action.md
source: llms
fetched_at: 2026-04-30T10:15:35.967263507-03:00
rendered_js: false
word_count: 579
summary: This document describes how to implement the Codex GitHub Action to automate code reviews, migration tasks, and quality checks within CI/CD pipelines.
tags:
    - github-actions
    - codex
    - automation
    - ci-cd
    - workflow-configuration
    - security-best-practices
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Codex GitHub Action

`openai/codex-action@v1` runs Codex in CI/CD jobs, applies patches, or posts reviews from GitHub Actions.

Use it when you want to:
- Automate Codex feedback on PRs or releases without managing the CLI yourself
- Gate changes on Codex-driven quality checks
- Run repeatable tasks (code review, release prep, migrations) from a workflow file

For CI examples, see [[032-noninteractive|Non-interactive mode]] and [openai/codex-action](https://github.com/openai/codex-action).

## Prerequisites

- Store OpenAI key as a GitHub secret (e.g. `OPENAI_API_KEY`) and reference it in the workflow.
- Run on Linux or macOS runner. For Windows, set `safety-strategy: unsafe`.
- Check out code before invoking the action so Codex can read the repository.
- Decide prompts: inline text via `prompt` or a committed file via `prompt-file`.

## Example workflow

Reviews new PRs, captures Codex's response, and posts it back:

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
      - name: Pre-fetch base and head refs
        run: |
          git fetch --no-tags origin \
            ${{ github.event.pull_request.base.ref }} \
            +refs/pull/${{ github.event.pull_request.number }}/head
      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md
          safety-strategy: drop-sudo
          sandbox: workspace-write

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}
```

Replace `.github/codex/prompts/review.md` with your own prompt file or use `prompt` for inline text. The example writes the final message to `codex-output.md` for later inspection.

## Configure `codex exec`

| Input | Purpose |
|-------|---------|
| `prompt` or `prompt-file` (choose one) | Inline instructions or repo path to task file |
| `codex-args` | Extra CLI flags as JSON array or shell string |
| `model`, `effort` | Agent configuration; empty = defaults |
| `sandbox` | `workspace-write`, `read-only`, `danger-full-access` |
| `output-file` | Save final message to disk for later steps |
| `codex-version` | Pin a specific CLI release; blank = latest |
| `codex-home` | Shared Codex home for reusing config or MCP setups |

## Manage privileges

| Input | Behavior |
|-------|----------|
| `safety-strategy` (default `drop-sudo`) | Removes `sudo` before running Codex. Irreversible for the job. On Windows must set `unsafe` |
| `unprivileged-user` + `codex-user` | Run Codex as a specific account. Ensure read/write access to checkout |
| `read-only` | Prevents file changes and network use, but still runs elevated. Don't rely on it alone to protect secrets |
| `sandbox` | Limits filesystem/network access within Codex. Choose the narrowest option that lets the task complete |
| `allow-users`, `allow-bots` | Restrict who can trigger the workflow. Default: only users with write access |

## Capture outputs

The action emits the last Codex message through `final-message` output. Map it to a job output or handle directly in later steps. Combine `output-file` with artifact upload for the full transcript. For structured data, pass `--output-schema` through `codex-args`.

## Security checklist

- Limit who can start the workflow. Prefer trusted events or explicit approvals.
- Sanitize prompt inputs from PRs, commit messages, or issue bodies to avoid prompt injection.
- Protect `OPENAI_API_KEY`: keep `safety-strategy` on `drop-sudo` or use unprivileged user. Never leave `unsafe` on multi-tenant runners.
- Run Codex as the last step so later steps don't inherit unexpected state changes.
- Rotate keys immediately if proxy logs or action output exposed secret material.

## Troubleshooting

| Issue | Cause / Fix |
|-------|-------------|
| Both `prompt` and `prompt-file` set | Remove duplicate; provide exactly one source |
| `responses-api-proxy` didn't write server info | Confirm API key is present and valid; proxy starts only when `openai-api-key` provided |
| `sudo` removal expected but succeeded | Ensure no earlier step restored `sudo`; runner must be Linux/macOS |
| Permission errors after `drop-sudo` | Grant write access before action runs (e.g. `chmod -R g+rwX "$GITHUB_WORKSPACE"` or use unprivileged-user pattern) |
| Unauthorized trigger blocked | Adjust `allow-users` or `allow-bots` to permit service accounts beyond default write collaborators |

#github-actions #ci-cd #automation #codex