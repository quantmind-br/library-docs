---
number: 73
category: reference
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/security/faq.md
word_count: 677
---
# Security FAQ

> **BLUF:** Codex security model uses zero-knowledge architecture. OpenAI sees no prompts, code, or file contents. Enterprise data is never used for model training. Authentication uses OAuth 2.0 + API key, with device code flow for CLI.

## Architecture & Privacy

### Does OpenAI see my code or prompts?

**No.** Codex uses a zero-knowledge architecture:

- Prompts, code, files, Git history, and tool outputs stay in-memory during your session
- Nothing is logged, persisted, or shared with OpenAI beyond API calls for model inference
- Session transcripts are stored locally only (`~/.codex/sessions/`), not in the cloud

### Is my data used for training?

**No.** OpenAI does not use customer data from Codex for training. See [Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq) for details.

### Does Codex work offline?

**Partial.** Without internet, Codex can:

- Use previously cached model responses
- Run local open-source models (OSS) with `--oss`

Full Codex functionality (API access, cloud tasks, updates) requires connectivity.

### Are Git commit messages visible to OpenAI?

**No.** Commit messages remain on your machine. Codex may generate commit messages as a tool, but it doesn't read your commit history unless explicitly configured.

## Authentication

### How does CLI authentication work?

Codex CLI supports two flows:

| Method | Description |
|--------|-------------|
| **Device code flow** (default) | OAuth with `openai.com/device`. Opens browser for auth. |
| **API key (`--with-api-key`)** | Pipe API key via stdin. Use for CI/CD, SSH, containers. |

```bash
# Device auth (interactive)
codex login

# API key (non-interactive)
echo $OPENAI_API_KEY | codex login --with-api-key
```

### Is API key stored securely?

- CLI credentials stored in `~/.codex/credentials` (mode 0600)
- Windows: Credential Manager
- Optional: Keyring via `cli_auth_credentials_store = "keyring"` in `config.toml`

### How does ChatGPT (app) authentication work?

Uses existing ChatGPT session via OAuth. No separate Codex credentials needed.

## Enterprise & Compliance

### Does Codex work with existing OpenAI API keys?

**Yes.** Codex supports both:

- **ChatGPT-auth** (app/IDE, uses ChatGPT session)
- **API-key auth** (CLI, uses platform.openai.com key)

Enterprise customers can use either method.

### How does Codex handle data residency?

OpenAI API operates from US data centers by default. Configure custom model providers to route through region-specific endpoints if needed.

### Does Codex support SSO/SAML?

Codex app/IDE integrates with ChatGPT's authentication. ChatGPT supports SSO for organizations. Contact your OpenAI account team for enterprise setup.

### Are there audit logs?

OpenAI maintains standard API audit logs. For detailed session logging, configure `history.persistence = "save-all"` in `config.toml` to save transcripts locally.

## Sandbox & Permissions

### How does the sandbox work?

Codex sandbox constrains file system and network access:

| Mode | Access |
|------|--------|
| `read-only` | Read files only, no writes |
| `workspace-write` | Read + write in workspace + `/tmp` |
| `danger-full-access` | Full filesystem + network (isolated environments only) |

### Can Codex run dangerous commands?

Only with explicit approval. Approval modes:

| Mode | Behavior |
|------|----------|
| `untrusted` | Ask before every untrusted action |
| `on-request` | Ask only when Codex explicitly requests |
| `never` | Never ask, execute immediately |

### Can I allow specific commands?

Use [execpolicy rules](https://developers.openai.com/codex/security/threat-model#execpolicy) to allow or prompt for specific command patterns.

### Does Codex have access to the internet?

| Mode | Internet Access |
|------|-----------------|
| `read-only` | Blocked |
| `workspace-write` | Blocked by default; enable via `network_access: true` |
| `danger-full-access` | Full access |

Configure via `sandbox_workspace_write.network_access` in `config.toml`.

## Third-Party & Integrations

### Is MCP secure?

MCP servers run as separate processes. Codex controls:

- Which tools are exposed (via `enabled_tools` / `disabled_tools`)
- Environment variables passed (whitelist via `env_vars`)
- OAuth scope (configured per server)

### Does Codex read my MCP server data?

Codex reads only what your MCP server returns. It does not inspect MCP server code or configuration.

### What data do integrations (GitHub, Slack, Linear) access?

| Integration | Data Access |
|-------------|-------------|
| GitHub | Read/write repos per OAuth scopes granted |
| Slack | Read/write messages per OAuth scopes granted |
| Linear | Read/write issues per OAuth scopes granted |

## Related

- [[036-security-threat-model|Security Threat Model]]
- [[016-cloud|Codex Cloud]]

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/security/faq.md)*