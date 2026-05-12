---
number: 34
category: guide
status: published
optimized: true
optimized_at: 2025-01-27T22:45:00Z
source_url: https://developers.openai.com/codex/plugins/build.md
word_count: 313
---
# Build Plugins

> **BLUF:** Package reusable skills, app integrations, MCP config into distributable plugins. Use `$plugin-creator` for scaffolding, marketplaces for distribution. Start with local skills for iteration, graduate to plugins for sharing.

## When to Use Plugins

| Approach | When |
|---------|------|
| **Local skill** | Iterating on one repo or personal workflow |
| **Plugin** | Share across teams, bundle app integrations/MCP, publish stable package |

## Create with `$plugin-creator`

Use the built-in `$plugin-creator` skill. Scaffolds `.codex-plugin/plugin.json` manifest + optional local marketplace entry.

If you already have a plugin folder, `$plugin-creator` can wire it into a local marketplace.

## Plugin Structure

```
my-plugin/
├── .codex-plugin/
│   └── plugin.json        # Required manifest
├── skills/
│   └── my-skill/
│       └── SKILL.md      # Optional bundled skill
├── .app.json             # Optional app/connector mappings
├── .mcp.json             # Optional MCP server config
└── assets/               # Optional icons, logos, screenshots
```

### Manifest (`plugin.json`)

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Bundle reusable skills and app integrations.",
  "author": {
    "name": "Your team",
    "email": "team@example.com",
    "url": "https://example.com"
  },
  "homepage": "https://example.com/plugins/my-plugin",
  "repository": "https://github.com/example/my-plugin",
  "license": "MIT",
  "keywords": ["research", "crm"],
  "skills": "./skills/",
  "mcpServers": "./.mcp.json",
  "apps": "./.app.json",
  "interface": {
    "displayName": "My Plugin",
    "shortDescription": "Reusable skills and apps",
    "developerName": "Your team",
    "category": "Productivity",
    "defaultPrompt": [
      "Use My Plugin to summarize new CRM notes.",
      "Use My Plugin to triage customer follow-ups."
    ],
    "brandColor": "#10A37F",
    "composerIcon": "./assets/icon.png",
    "logo": "./assets/logo.png",
    "screenshots": ["./assets/screenshot-1.png"]
  }
}
```

**Required:** `name` (kebab-case), `version`, `description`.  
**Optional:** author, homepage, repository, license, keywords, skills, mcpServers, apps, interface.

### Path Rules

- All paths relative to plugin root, start with `./`
- Store visual assets under `./assets/`
- `skills` for skill folders, `apps` for `.app.json`, `mcpServers` for `.mcp.json`

## Minimal Plugin (One Skill)

1. Create plugin folder:
   ```bash
   mkdir -p my-first-plugin/.codex-plugin
   ```
2. Add manifest:
   ```json
   {
     "name": "my-first-plugin",
     "version": "1.0.0",
     "description": "Reusable greeting workflow",
     "skills": "./skills/"
   }
   ```
3. Add skill:
   ```bash
   mkdir -p my-first-plugin/skills/hello
   ```
   ```md
   ---
   name: hello
   description: Greet the user with a friendly message.
   ---
   
   Greet the user warmly and ask how you can help.
   ```

## Marketplaces

A marketplace is a JSON catalog of plugins. Codex reads from:
- Official Plugin Directory (curated)
- Repo: `$REPO_ROOT/.agents/plugins/marketplace.json`
- Personal: `~/.agents/plugins/marketplace.json`

### Marketplace Format

```json
{
  "name": "local-example-plugins",
  "interface": { "displayName": "Local Example Plugins" },
  "plugins": [
    {
      "name": "my-plugin",
      "source": { "source": "local", "path": "./plugins/my-plugin" },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

**Policy values:** `installation`: `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`. `authentication`: `ON_INSTALL`, `ON_USE`.

### Git-Backed Plugins

```json
{
  "name": "remote-helper",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/codex-plugins.git",
    "path": "./plugins/remote-helper",
    "ref": "main"
  }
}
```

## CLI Marketplace Commands

```bash
# Add marketplace
codex plugin marketplace add owner/repo
codex plugin marketplace add owner/repo --ref main
codex plugin marketplace add https://github.com/example/plugins.git --sparse .agents/plugins
codex plugin marketplace add ./local-marketplace-root

# Manage
codex plugin marketplace upgrade
codex plugin marketplace upgrade marketplace-name
codex plugin marketplace remove marketplace-name
```

Sources: GitHub shorthand (`owner/repo[@ref]`), HTTP(S) Git URLs, SSH Git URLs, local directories.

## Local Installation

### Repo-Scoped

1. Copy plugin to `$REPO_ROOT/plugins/my-plugin`
2. Add marketplace at `$REPO_ROOT/.agents/plugins/marketplace.json`
3. Restart Codex

### Personal

1. Copy plugin to `~/.codex/plugins/my-plugin`
2. Add marketplace at `~/.agents/plugins/marketplace.json`
3. Restart Codex

After plugin changes: update plugin directory + restart Codex.

## Installation from Marketplace

1. Open plugin directory in Codex
2. Select marketplace source
3. Browse/install plugins

Codex installs to `~/.codex/plugins/cache/$MARKETPLACE_NAME/$PLUGIN_NAME/$VERSION/`. Local plugins use `version: local`.

Enable/disable per plugin via `~/.codex/config.toml`.

## Related

- [[044-skills|Skills]] — authoring format
- [[035-security-setup|Security Setup]] — plugin security considerations

---

*Source: [OpenAI Developers](https://developers.openai.com/codex/plugins/build.md)*