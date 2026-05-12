---
title: README
url: https://github.com/openagen/zeroclaw/blob/master/docs/setup-guides/README.md
source: git
fetched_at: 2026-05-02T14:52:12.68470451-03:00
rendered_js: false
word_count: 189
summary: Provides a comprehensive orientation for new users, detailing setup procedures, onboarding command options, and environment validation steps.
tags:
    - onboarding
    - cli-setup
    - quick-start
    - environment-validation
    - installation-guide
category: guide
optimized: true
optimized_at: 2026-05-05T00:00:00Z
---
# Getting Started Docs

> [!info] Purpose
> Comprehensive orientation for new users with setup procedures, onboarding command options, and environment validation.

## Start Path

1. Main overview: [[019-readme|README]]
2. One-click setup: [[064-setup-guides-one-click-bootstrap|One click bootstrap]]
3. Update/uninstall on macOS: [[059-setup-guides-macos-update-uninstall|Macos update uninstall]]
4. Find commands by task: [[126-reference-cli-commands-reference|Commands reference]]

## Choose Your Path

| Scenario | Command |
|----------|---------|
| Have API key, want fastest setup | `zeroclaw onboard --api-key sk-... --provider openrouter` |
| Want guided prompts | `zeroclaw onboard --interactive` |
| Config exists, fix channels only | `zeroclaw onboard --channels-only` |
| Config exists, force full overwrite | `zeroclaw onboard --force` |
| Using subscription auth | See [Subscription Auth](https://github.com/openagen/zeroclaw/blob/master/docs/README.md#subscription-auth-openai-codex--claude-code) |

## Onboarding and Validation

- Quick onboarding: `zeroclaw onboard --api-key "sk-..." --provider openrouter`
- Interactive onboarding: `zeroclaw onboard --interactive`
- Existing config protection: reruns require explicit confirmation (or `--force` in non-interactive flows)
- Ollama cloud models (`:cloud`) require remote `api_url` and API key (e.g., `api_url = "https://ollama.com"`)
- Validate environment: `zeroclaw status` + `zeroclaw doctor`

## Next

- Runtime operations: [[16-readme|README]]
- Reference catalogs: [[23-reference-readme|README]]
- macOS lifecycle: [[059-setup-guides-macos-update-uninstall|Macos update uninstall]]

#zeroclaw #onboarding #cli-setup #quick-start