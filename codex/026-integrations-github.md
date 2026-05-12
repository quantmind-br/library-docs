---
number: 26
category: integrations
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://github.com/openai/codex/blob/main/INTEGRATIONS.md
word_count: 453
---
# GitHub Integration

> **BLUF:** Codex CLI integrates with GitHub for authentication, repository access, and pull request workflows. Supports GitHub Actions, Codespaces, and direct repo manipulation via MCP servers.

## Authentication

### OAuth Flow
```bash
codex login --provider github
```

- Opens browser for GitHub OAuth
- Stores token in `~/.codex/auth.json`
- Supports GitHub Enterprise via `--github-base-url`

### Personal Access Token
```bash
export GITHUB_TOKEN=ghp_xxxxxxxx
codex --github-token $GITHUB_TOKEN "review open PRs"
```

### App Authentication
For organization-wide access:
1. Install Codex GitHub App on repository
2. Provide app ID and private key via env vars:
```bash
export GITHUB_APP_ID=123456
export GITHUB_PRIVATE_KEY="$(cat app.pem)"
```

## Repository Operations

| Command | Description |
|---------|-------------|
| `codex github clone <repo>` | Clone with auth |
| `codex github pr list` | List open PRs |
| `codex github pr checkout <n>` | Checkout PR branch |
| `codex github pr review <n>` | Review PR with AI |
| `codex github issue create` | Create issue from prompt |
| `codex github issue list` | List issues |

## Pull Request Workflow

```bash
# 1. Checkout and review
codex github pr checkout 42
codex "review this PR for security issues"

# 2. Make changes
codex "fix the SQL injection in auth.ts"

# 3. Push and update PR
codex github pr update --push
```

## GitHub Actions

### Workflow Integration
```yaml
name: Codex Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          instructions: ./.codex/pr-review.md
          model: o3
```

### Action Inputs
| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `openai-api-key` | Yes | - | OpenAI API key |
| `instructions` | No | - | Path to review instructions |
| `model` | No | o4-mini | Model to use |
| `approval-mode` | No | human-in-the-loop | Auto-approval setting |

### Action Outputs
| Output | Description |
|--------|-------------|
| `review-comment` | PR comment with findings |
| `issues-found` | Number of issues detected |
| `suggestions` | JSON array of code suggestions |

## GitHub Codespaces

### Prebuild Configuration
```json
// .devcontainer/devcontainer.json
{
  "features": {
    "ghcr.io/openai/codex-devcontainer-feature:1": {
      "version": "latest"
    }
  },
  "postCreateCommand": "codex login",
  "customizations": {
    "vscode": {
      "extensions": ["openai.codex"]
    }
  }
}
```

### Codespace Commands
```bash
# Inside Codespace
codex "setup this project"
codex "run the test suite"
codex "debug the failing test"
```

## MCP Server

The GitHub MCP server exposes repository operations as tools:

```json
// ~/.codex/mcp.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@openai/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### Available Tools
| Tool | Parameters | Description |
|------|------------|-------------|
| `github_search_code` | `q`, `language` | Search code across repos |
| `github_get_file` | `repo`, `path`, `ref` | Get file contents |
| `github_create_pr` | `repo`, `title`, `body`, `head`, `base` | Create PR |
| `github_merge_pr` | `repo`, `pull_number` | Merge PR |
| `github_list_issues` | `repo`, `state`, `labels` | List issues |
| `github_create_issue` | `repo`, `title`, `body` | Create issue |

## Security Considerations

| Risk | Mitigation |
|------|------------|
| Token exposure | Use `secrets.` in Actions; never log tokens |
| Overly broad permissions | Use fine-grained PATs with minimal scopes |
| PR auto-merge | Requires explicit `--approval-mode=full-auto` |
| Code injection | Review all AI-generated changes before merging |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `401 Bad credentials` | Regenerate token; check `GITHUB_TOKEN` env var |
| `404 Not Found` | Verify repository access permissions |
| Rate limiting | Use GitHub App auth (higher limits) |
| Merge conflicts | Pull latest main before running Codex |

---

*Source: [openai/codex](https://github.com/openai/codex/blob/main/INTEGRATIONS.md)*
