---
title: Non-interactive mode
url: https://developers.openai.com/codex/noninteractive.md
source: llms
fetched_at: 2026-04-30T10:15:53.961804328-03:00
rendered_js: false
word_count: 657
summary: This document explains how to use the codex exec command to integrate Codex into non-interactive automated workflows, such as CI/CD pipelines, by handling input/output, authentication, and structured data.
tags:
    - codex-cli
    - automation
    - ci-cd
    - scripting
    - command-line
    - integration
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Non-interactive mode

Run Codex from scripts and CI jobs without opening the interactive TUI. Invoke with `codex exec`.

For flag details, see [[066-cli-reference#codex-exec|codex exec reference]].

## When to use `codex exec`

- Run as part of a pipeline (CI, pre-merge checks, scheduled jobs)
- Produce output you can pipe into other tools
- Fit into CLI workflows that chain command output into Codex and pass Codex output onward
- Run with explicit, pre-set sandbox and approval settings

## Basic usage

Pass a task prompt as a single argument:
```bash
codex exec "summarize the repository structure and list the top 5 risky areas"
```

While running, Codex streams progress to `stderr` and prints only the final agent message to `stdout`. Easy to redirect or pipe:
```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md
```

Use `--ephemeral` when you don't want to persist session rollout files:
```bash
codex exec --ephemeral "triage this repository and suggest next steps"
```

If stdin is piped and you also provide a prompt argument, Codex treats the prompt as the instruction and piped content as additional context:
```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md
```

## Permissions and safety

Default: read-only sandbox. In automation, set the least permissions needed:

| Need | Command |
|------|---------|
| Allow edits | `codex exec --full-auto "<task>"` |
| Broader access | `codex exec --sandbox danger-full-access "<task>"` |

Use `danger-full-access` only in controlled environments (isolated CI runner or container).

If an enabled MCP server has `required = true` and fails to initialize, `codex exec` exits with an error instead of continuing without it.

## Machine-readable output

### JSON Lines

```bash
codex exec --json "summarize the repo structure" | jq
```

`stdout` becomes a JSON Lines stream capturing every event: `thread.started`, `turn.started`, `turn.completed`, `turn.failed`, `item.*`, `error`.

Item types: agent messages, reasoning, command executions, file changes, MCP tool calls, web searches, plan updates.

Example stream:
```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122}}
```

### Final message file

Write final message to disk with `-o <path>` / `--output-last-message <path>`. Still prints to `stdout`.

## Structured outputs with schema

Request JSON Schema-conformant final responses for downstream steps:

`schema.json`:
```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}
```

Run:
```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json
```

Example output:
```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}
```

## Authenticate in CI

`codex exec` reuses saved CLI authentication by default. In CI, provide credentials explicitly.

### API key auth (recommended)

Set `CODEX_API_KEY` as a secret environment variable. To use a different key for a single run:
```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"
```

`CODEX_API_KEY` is only supported in `codex exec`.

### ChatGPT-managed auth in CI/CD (advanced)

Use this only if you specifically need to run as your Codex account instead of an API key (e.g., enterprise teams using ChatGPT-managed access on trusted runners, or users needing ChatGPT/Codex rate limits).

API keys are the recommended default for automation — simpler to provision and rotate.

Treat `~/.codex/auth.json` like a password. Don't commit it, paste it into tickets, or share it in chat. Do not use for public or open-source repositories.

If `codex login` isn't an option on the runner, seed `auth.json` through secure storage, run Codex so it refreshes in place, and persist the updated file between runs. See [Maintain Codex account auth in CI/CD (advanced)](https://developers.openai.com/codex/auth/ci-cd-auth).

## Resume a non-interactive session

Continue a previous run (e.g., two-stage pipeline):
```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"
```

Or target a specific session ID:
```bash
codex exec resume <SESSION_ID>
```

## Git repository required

Codex requires commands to run inside a Git repository to prevent destructive changes. Override with `codex exec --skip-git-repo-check` if you're sure the environment is safe.

## Common automation patterns

### Autofix CI failures in GitHub Actions

Trigger a follow-up workflow when main CI fails:
1. Check out the failing commit SHA.
2. Install dependencies and run Codex with a narrow prompt and minimal permissions.
3. Re-run the test command.
4. Open a PR with the resulting patch.

#### Minimal workflow using Codex CLI

```yaml
name: Codex auto-fix on CI failure
on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    env:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
      FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ env.FAILED_HEAD_SHA }}
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; else npm i; fi
      - name: Install Codex
        run: npm i -g @openai/codex
      - name: Authenticate Codex
        run: codex login --api-key "$OPENAI_API_KEY"
      - name: Run Codex
        run: |
          codex exec --full-auto --sandbox workspace-write \
            "Read the repository, run the test suite, identify the minimal change needed to make all tests pass, implement only that change, and stop. Do not refactor unrelated files."
      - name: Verify tests
        run: npm test --silent
      - name: Create pull request
        if: success()
        uses: peter-evans/create-pull-request@v6
        with:
          branch: codex/auto-fix-${{ github.event.workflow_run.run_id }}
          base: ${{ env.FAILED_HEAD_BRANCH }}
          title: "Auto-fix failing CI via Codex"
```

#### Alternative: Use the Codex GitHub Action

Run `codex exec` through [[019-github-action|Codex GitHub Action]] and pass the prompt as an input.

## Advanced stdin piping

| Pattern | Use case | Example |
|---------|----------|---------|
| **Prompt + stdin** | Instruction is fixed; piped output is context | `npm test 2>&1 \| codex exec "summarize failing tests and propose smallest fix" \| tee test-summary.md` |
| **stdin as prompt** | Another command generates the entire prompt | `cat prompt.txt \| codex exec -` or `generate_prompt.sh \| codex exec - --json > result.jsonl` |

More prompt+stdin examples:
```bash
# Summarize logs
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

# Inspect TLS or HTTP issues
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

# Prepare a Slack-ready update
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

# Draft a PR comment from CI logs
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -
```

#automation #ci-cd #codex-cli #scripting