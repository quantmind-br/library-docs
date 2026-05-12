---
number: 33
category: open-source
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://github.com/openai/codex
word_count: 373
---
# OpenAI Codex (Open Source)

> **BLUF:** OpenAI Codex is an open-source coding agent available as a CLI tool and TypeScript SDK. Licensed under Apache 2.0, it supports local execution with sandboxed command running, file editing, and multi-model support.

## Repository

- **GitHub:** [openai/codex](https://github.com/openai/codex)
- **License:** Apache 2.0
- **Language:** TypeScript (Node.js 22+)
- **Monorepo:** CLI (`codex-cli/`), SDK (`packages/codex-sdk/`), docs (`docs/`)

## Architecture

```
codex/
├── codex-cli/          # CLI application
│   ├── src/
│   │   ├── commands/   # CLI commands (chat, init, config)
│   │   ├── utils/      # Helpers (git, sandbox, config)
│   │   └── agents/     # Agent implementations
│   └── tests/
├── packages/
│   └── codex-sdk/      # TypeScript SDK
│       ├── src/
│       │   ├── client/ # API client
│       │   ├── types/  # TypeScript definitions
│       │   └── tools/  # Tool implementations
│       └── tests/
└── docs/               # Documentation
```

## Key Components

| Component | Description |
|-----------|-------------|
| `Agent` | Core agent loop: planning, tool use, response generation |
| `Sandbox` | Platform-specific isolation (seatbelt/Landlock) |
| `GitIntegration` | Automatic diff review and commit staging |
| `ConfigLoader` | Hierarchical config resolution |
| `MCPClient` | Model Context Protocol server connections |

## SDK Usage

```typescript
import { CodexClient } from '@openai/codex-sdk';

const client = new CodexClient({
  apiKey: process.env.OPENAI_API_KEY,
  model: 'o4-mini',
  approvalMode: 'human-in-the-loop'
});

const result = await client.run({
  prompt: 'Refactor auth.ts to use Zod',
  cwd: './src',
  onApprovalRequest: async (action) => {
    console.log('Approve?', action);
    return true;
  }
});

console.log(result.filesModified);
```

## Development Setup

```bash
# Clone
git clone https://github.com/openai/codex.git
cd codex

# Install dependencies
npm install

# Build
npm run build

# Test
npm test

# Run CLI locally
npm run cli -- "your prompt"
```

## Contributing

| Step | Command |
|------|---------|
| Fork & clone | `git clone git@github.com:yourusername/codex.git` |
| Create branch | `git checkout -b feature/your-feature` |
| Make changes | Edit files |
| Run tests | `npm test` |
| Lint | `npm run lint` |
| Commit | `git commit -m "feat: description"` |
| Push | `git push origin feature/your-feature` |

### Commit Convention
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance

## Testing

| Test Type | Command | Coverage Target |
|-----------|---------|-----------------|
| Unit | `npm run test:unit` | 80% |
| Integration | `npm run test:integration` | - |
| E2E | `npm run test:e2e` | - |
| Sandbox | `npm run test:sandbox` | - |

## Release Process

1. Update `CHANGELOG.md`
2. Bump version in `package.json`
3. Run `npm run version:bump`
4. Create GitHub release with auto-generated notes
5. NPM publishes via GitHub Actions

## Security

- Report vulnerabilities to security@openai.com
- GPG key: [OpenAI Security](https://openai.com/security)
- Bug bounty: [HackerOne](https://hackerone.com/openai)

## Community

| Resource | Link |
|----------|------|
| Discussions | [GitHub Discussions](https://github.com/openai/codex/discussions) |
| Issues | [GitHub Issues](https://github.com/openai/codex/issues) |
| Discord | [OpenAI Developer Discord](https://discord.gg/openai) |
| Twitter/X | [@OpenAI](https://twitter.com/OpenAI) |

## Related Projects

| Project | Description |
|---------|-------------|
| [codex-rs](https://github.com/openai/codex-rs) | Rust port of Codex CLI |
| [codex-vscode](https://github.com/openai/codex-vscode) | VS Code extension |
| [codex-mcp](https://github.com/openai/codex-mcp) | MCP server implementations |

---

*Source: [openai/codex](https://github.com/openai/codex)*
