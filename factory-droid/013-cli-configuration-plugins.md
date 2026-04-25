---
title: Plugins - Factory Documentation
url: https://docs.factory.ai/cli/configuration/plugins
source: sitemap
fetched_at: 2026-04-15T09:00:41.70225375-03:00
rendered_js: false
word_count: 660
summary: This document explains how to create, manage, distribute, and install modular plugins in Droid to extend functionality with custom skills, commands, and agents.
tags:
    - droid-plugins
    - plugin-development
    - plugin-management
    - marketplace-configuration
    - software-extension
    - automation-tools
category: guide
---

Plugins let you extend Droid with custom functionality that can be shared across projects and teams. A plugin bundles skills, slash commands, agents, and MCP servers into a single, distributable package.

## What are plugins?

Plugins are directories containing a manifest file (`.factory-plugin/plugin.json`) and optional components like skills, commands, and agents. Unlike standalone configuration in `.factory/`, plugins are designed for sharing and distribution. **Plugin components:**

ComponentPurposeInvocation**Skills**Reusable capabilities with instructions and toolsModel-invoked automatically based on task**Commands**Slash commands for specific workflowsUser-invoked via `/command-name`**Agents**Specialized subagent definitionsCalled via Task tool**Hooks**Lifecycle event handlersAutomatic on matching events**MCP Servers**External tool integrationsAvailable as tools when plugin is active

## When to use plugins vs standalone configuration

ApproachBest for**Standalone** (`.factory/` directory)Personal workflows, project-specific customizations, quick experiments**Plugins**Sharing with teammates, distributing to community, versioned releases, reusable across projects

Start with standalone configuration in `.factory/` for quick iteration, then convert to a plugin when you’re ready to share.

## Managing plugins

Droid provides two ways to manage plugins:

### Interactive UI (recommended)

Use the `/plugins` slash command to open the plugin manager:

This opens a tabbed interface:

- **Browse** - View and install plugins from registered marketplaces
- **Installed** - Manage installed plugins (view info, update, uninstall)
- **Marketplaces** - Add, update, or remove marketplaces

**Navigation:**

- Left/Right arrows: Switch between tabs
- Up/Down arrows: Navigate within a tab
- Enter: Select/confirm
- Escape: Go back or close

### CLI commands (for scripting)

For automation, use CLI commands from your shell (not as slash commands):

```
# Marketplace management
droid plugin marketplace add <url>
droid plugin marketplace remove <name>
droid plugin marketplace list
droid plugin marketplace update [name]

# Plugin management
droid plugin install <plugin@marketplace> [--scope user|project]
droid plugin uninstall <plugin@marketplace> [--scope user|project]
droid plugin update [plugin@marketplace] [--scope user|project]
droid plugin list [--scope user|project]
```

Plugin IDs use the format `pluginName@marketplaceName` (e.g., `security-guidance@claude-plugins-official`).

## Plugin structure

Every plugin follows this directory structure:

```
my-plugin/
├── .factory-plugin/
│   └── plugin.json          # Plugin manifest (required)
├── commands/                 # Slash commands (optional)
│   └── my-command.md
├── skills/                   # Agent skills (optional)
│   └── my-skill/
│       └── SKILL.md
├── droids/                   # Subagent definitions (optional)
│   └── my-agent.md
├── mcp.json                  # MCP server configs (optional)
└── README.md                 # Documentation
```

### Plugin hooks

Plugins can include hooks that execute at specific lifecycle events. Add a `hooks/` directory with a `hooks.json` file:

```
my-plugin/
├── .factory-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json         # Hook configuration
│   └── my-script.sh       # Hook scripts
└── ...
```

**hooks/hooks.json example:**

```
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        {
          "type": "command",
          "command": "${DROID_PLUGIN_ROOT}/hooks/format.sh"
        }
      ]
    }
  ]
}
```

Use `${DROID_PLUGIN_ROOT}` to reference files within your plugin directory. This variable is expanded to the actual plugin path when the hook runs. See [Hooks reference](https://docs.factory.ai/reference/hooks-reference#plugin-hooks) for details.

### Plugin manifest

The manifest at `.factory-plugin/plugin.json` defines your plugin’s identity:

```
{
  "name": "my-plugin",
  "description": "A helpful description of what this plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```

FieldPurpose`name`Unique identifier for the plugin.`description`Shown in the plugin manager when browsing or installing.`version`Track releases using semantic versioning.`author`Optional. Helpful for attribution.

## Plugin scopes

When installing plugins, you choose an installation scope:

ScopeLocationVisibility**User**`~/.factory/`Available across all your projects**Project**`<project>/.factory/`Shared with teammates via git

A plugin can only exist at one scope. To change scope, uninstall first and reinstall.

## Version tracking

Plugins are versioned by Git commit hash, not semantic version. When you update a plugin, Droid fetches the latest commit from the marketplace repository.

## Marketplaces

Marketplaces are catalogs of plugins that you can browse and install from.

### Adding marketplaces

Via UI: `/plugins` → Marketplaces tab → “Add new marketplace” → enter URL Via CLI:

```
# From GitHub
droid plugin marketplace add https://github.com/owner/repo

# From other Git hosts
droid plugin marketplace add https://gitlab.com/company/plugins.git

# From local path (for development)
droid plugin marketplace add /path/to/local/marketplace
```

### Managing marketplaces

Via UI: `/plugins` → Marketplaces tab → select marketplace → choose action (Update, Disable auto-update, Delete) Via CLI:

```
droid plugin marketplace list
droid plugin marketplace update [marketplace-name]
droid plugin marketplace remove <marketplace-name>
```

### Team marketplaces

Configure automatic marketplace and plugin installation by adding to `.factory/settings.json`:

```
{
  "extraKnownMarketplaces": {
    "your-org-internal-plugins": {
      "source": {
        "source": "github",
        "repo": "your-org/internal-plugins"
      }
    }
  },
  "enabledPlugins": {
    "code-standards@your-org-internal-plugins": true
  }
}
```

When Droid starts, it automatically:

1. Registers any marketplaces from `extraKnownMarketplaces` that aren’t already registered
2. Installs any plugins from `enabledPlugins` that aren’t already installed

The installation scope depends on where the setting is defined:

- Org-managed settings → `org` scope
- User settings → `user` scope
- Project settings → `project` scope

## Discovering plugins

### Official Factory plugins

Factory maintains an official plugin marketplace at `Factory-AI/factory-plugins` with curated plugins. Add via `/plugins` UI or CLI:

```
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
```

**Available plugins:**

PluginDescription[**droid-control**](https://docs.factory.ai/cli/features/droid-control)Terminal, browser, and computer automation. Record demos, verify behavior claims, and run QA flows.**droid-evolved**Skills for continuous learning: session navigation, human writing, skill creation, visual design, frontend design, browser automation**security-engineer**Security review, threat modeling, commit scanning, and vulnerability validation

Install via `/plugins` UI (Browse tab) or CLI:

```
droid plugin install droid-control@factory-plugins
droid plugin install droid-evolved@factory-plugins
droid plugin install security-engineer@factory-plugins
```

PluginDescriptionSource**superpowers**Complete software development workflow with brainstorming, planning, and subagent-driven development`obra/superpowers`

### Enterprise Plugin Registry

For organizations that need centralized control over approved plugins, see [Enterprise Plugin Registry](https://docs.factory.ai/enterprise/enterprise-plugin-registry). This allows you to:

- Maintain a private marketplace of approved plugins
- Pre-install mandatory plugins for all users
- Organize plugins by team, role, or capability

### Claude Code compatibility

Droid is compatible with plugins built for Claude Code. If you find a Claude Code plugin you’d like to use, you can install it directly - the plugin format is interoperable. See the [Claude Code plugins documentation](https://code.claude.com/docs/en/plugins) for more details.

## Next steps