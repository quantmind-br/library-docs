---
title: Enterprise Plugin Registry
url: https://docs.factory.ai/enterprise/enterprise-plugin-registry.md
source: llms
fetched_at: 2026-02-05T21:42:26.498534918-03:00
rendered_js: false
word_count: 766
summary: This document explains how to establish and manage a private Enterprise Plugin Registry for centralizing and distributing approved plugins across an organization.
tags:
    - enterprise-registry
    - plugin-management
    - marketplace-configuration
    - organization-settings
    - git-integration
category: guide
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enterprise Plugin Registry

> Centralize and distribute approved plugins across your organization with a private plugin marketplace.

An **Enterprise Plugin Registry** is a centralized, private repository where organizations maintain approved plugins for company-wide distribution. Instead of individual teams discovering and vetting plugins independently, the registry provides a curated catalog of capabilities that are pre-approved, maintained, and ready to use.

## Why use an Enterprise Plugin Registry?

| Challenge                                          | Solution                                                                      |
| -------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Inconsistent tooling** across teams              | Single source of approved plugins ensures everyone uses the same capabilities |
| **Security and compliance review** for each plugin | Vet plugins once at the org level, distribute everywhere                      |
| **Onboarding new developers**                      | New team members instantly access all approved capabilities                   |
| **Role-specific tooling**                          | Package plugins by team function (security, frontend, data, etc.)             |
| **Version control**                                | Manage plugin versions centrally, roll out updates organization-wide          |

## Setting up a registry

An Enterprise Plugin Registry is a Git repository containing your organization's approved plugins with a marketplace manifest.

### Repository structure

```
your-org/droid-plugins/
├── .factory-plugin/
│   └── marketplace.json      # Registry manifest
├── plugins/
│   ├── security-toolkit/     # Security team plugins
│   │   ├── .factory-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   ├── frontend-standards/   # Frontend team plugins
│   │   ├── .factory-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   ├── data-engineering/     # Data team plugins
│   │   └── ...
│   └── platform-tools/       # Platform/DevOps plugins
│       └── ...
└── README.md
```

### Marketplace manifest

Create `.factory-plugin/marketplace.json` to register your plugins:

```json  theme={null}
{
  "name": "acme-corp-plugins",
  "description": "ACME Corp approved Droid plugins",
  "owner": {
    "name": "ACME Platform Team",
    "email": "platform@acme.com"
  },
  "plugins": [
    {
      "name": "security-toolkit",
      "description": "Security review, threat modeling, and vulnerability scanning",
      "source": "./plugins/security-toolkit",
      "category": "security"
    },
    {
      "name": "frontend-standards",
      "description": "React component patterns, accessibility checks, design system integration",
      "source": "./plugins/frontend-standards",
      "category": "frontend"
    },
    {
      "name": "data-engineering",
      "description": "SQL review, pipeline validation, data quality checks",
      "source": "./plugins/data-engineering",
      "category": "data"
    },
    {
      "name": "platform-tools",
      "description": "CI/CD helpers, infrastructure review, deployment automation",
      "source": "./plugins/platform-tools",
      "category": "platform"
    }
  ]
}
```

## Org-level configuration

Configure the registry at the organization level so it's automatically available to all users. Add to your org-managed settings:

```json  theme={null}
{
  "extraKnownMarketplaces": {
    "acme-corp-plugins": {
      "source": {
        "source": "github",
        "repo": "your-org/droid-plugins"
      }
    }
  },
  "enabledPlugins": {
    "security-toolkit@acme-corp-plugins": true,
    "platform-tools@acme-corp-plugins": true
  }
}
```

| Field                    | Purpose                                                           |
| ------------------------ | ----------------------------------------------------------------- |
| `extraKnownMarketplaces` | Registers the marketplace so users can browse and install plugins |
| `enabledPlugins`         | Pre-installs specific plugins for all users (optional)            |

### Restricting marketplaces

To prevent users from adding unapproved marketplaces, use `strictKnownMarketplaces`:

```json  theme={null}
{
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "your-org/droid-plugins" },
    { "source": "github", "repo": "Factory-AI/factory-plugins" }
  ]
}
```

When `strictKnownMarketplaces` is set:

* Users can only add marketplaces from the approved list
* Plugin installations from non-approved marketplaces are blocked
* Existing unapproved marketplaces continue to work but cannot be updated

With this configuration:

* The registry appears automatically when users run `/plugins`
* Pre-enabled plugins are available immediately without manual installation
* Users can install additional plugins from the registry as needed

## User experience

Users manage plugins via the `/plugins` UI:

1. Run `/plugins` to open the plugin manager
2. Browse tab shows plugins from all registered marketplaces including the org registry
3. Org-enabled plugins are pre-installed automatically on startup

For CLI access:

```bash  theme={null}
droid plugin install frontend-standards@acme-corp-plugins
droid plugin update security-toolkit@acme-corp-plugins
```

Users see the registry alongside public marketplaces, with org plugins clearly labeled.

## Organizing plugins by role

Structure your registry to match your organization's teams and workflows:

### By team function

```
plugins/
├── security/           # AppSec team
├── frontend/           # Web/mobile teams  
├── backend/            # API/services teams
├── data/               # Data engineering/science
├── platform/           # DevOps/SRE
└── compliance/         # Legal/compliance
```

### By capability

```
plugins/
├── code-review/        # Review and quality
├── testing/            # Test generation and validation
├── documentation/      # Doc generation and maintenance
├── migrations/         # Code and data migrations
└── security/           # Security scanning and review
```

### By project type

```
plugins/
├── microservices/      # Service development patterns
├── monolith/           # Legacy system tools
├── data-pipelines/     # ETL and batch processing
└── ml-projects/        # ML/AI development
```

## Pre-installing plugins

For critical capabilities that everyone needs, use `enabledPlugins` in org-managed settings:

```json  theme={null}
{
  "enabledPlugins": {
    "security-toolkit@acme-corp-plugins": true,
    "code-standards@acme-corp-plugins": true
  }
}
```

Pre-installed plugins:

* Are available immediately on first Droid session
* Are installed with `org` scope automatically
* Can be updated via `/plugins` UI or `droid plugin update`

## Version management

Plugins are versioned by Git commit hash. When a plugin is updated, Droid fetches the latest commit from the marketplace.

To control versions, use Git branches:

* `main` - Production-ready for all users
* `staging` - For early adopters
* `dev` - For internal testing

<Note>
  Version pinning via the `version` field is not currently supported. The field is for documentation only.
</Note>

## Private repository access

For private Git repositories, ensure Droid can authenticate:

### GitHub Enterprise

```bash  theme={null}
# Users authenticate via gh CLI
gh auth login --hostname github.your-company.com
```

### GitLab Self-Hosted

```bash  theme={null}
# Configure git credentials
git config --global credential.helper store
```

### SSH-based access

Ensure SSH keys are configured for the repository host.

## Local marketplaces

For air-gapped environments or when Git access is restricted, you can use local directory marketplaces. This is useful for:

* Environments without internet access
* Testing plugins before publishing
* Internal distribution via shared network drives

### Setting up a local marketplace

Create a directory with the standard marketplace structure:

```
/shared/company-plugins/
├── .factory-plugin/
│   └── marketplace.json
└── plugins/
    ├── security-toolkit/
    │   └── .factory-plugin/
    │       └── plugin.json
    └── code-standards/
        └── .factory-plugin/
            └── plugin.json
```

### Adding a local marketplace

Via UI: `/plugins` → Marketplaces tab → "Add new marketplace" → enter absolute path

Via CLI:

```bash  theme={null}
droid plugin marketplace add /shared/company-plugins
```

### Configuration for auto-registration

Use the `local` source type in settings:

```json  theme={null}
{
  "extraKnownMarketplaces": {
    "company-local-plugins": {
      "source": {
        "source": "local",
        "path": "/shared/company-plugins"
      }
    }
  }
}
```

<Note>
  When removing a local marketplace from the registry, Droid does **not** delete the source directory. Only Git-cloned marketplaces have their directories removed on deletion.
</Note>

## Best practices

<AccordionGroup>
  <Accordion title="Establish a review process">
    Before adding plugins to the registry:

    * Security review for any external dependencies
    * Code review by platform team
    * Testing in isolated environment
    * Documentation requirements
  </Accordion>

  <Accordion title="Document each plugin">
    Every plugin should have a README covering:

    * What capabilities it provides
    * When to use it (and when not to)
    * Any prerequisites or dependencies
    * Example usage
  </Accordion>

  <Accordion title="Version semantically">
    Use semantic versioning so teams know what to expect:

    * **Major**: Breaking changes to commands or behavior
    * **Minor**: New capabilities, backward compatible
    * **Patch**: Bug fixes only
  </Accordion>

  <Accordion title="Monitor adoption">
    Track which plugins are being used:

    * Installation counts
    * Active usage metrics
    * Feedback from teams
    * Issues and feature requests
  </Accordion>

  <Accordion title="Plan for deprecation">
    When retiring plugins:

    * Announce deprecation timeline
    * Provide migration path to alternatives
    * Keep deprecated plugins available (read-only) during transition
  </Accordion>
</AccordionGroup>

## Example: Financial services org

A financial services company sets up their registry:

**Mandatory plugins** (pre-installed for everyone):

* `compliance-checks` - PCI-DSS and SOX compliance validation
* `security-scanner` - OWASP vulnerability detection
* `audit-logging` - Enhanced audit trail for all Droid actions

**Team-specific plugins** (available for install):

* `trading-systems` - For quantitative and trading teams
* `risk-models` - For risk management teams
* `regulatory-reporting` - For compliance teams

**Configuration (org-managed-settings.json):**

```json  theme={null}
{
  "extraKnownMarketplaces": {
    "acme-financial-plugins": {
      "source": {
        "source": "github",
        "repo": "acme-financial/droid-plugins"
      }
    }
  },
  "enabledPlugins": {
    "compliance-checks@acme-financial-plugins": true,
    "security-scanner@acme-financial-plugins": true,
    "audit-logging@acme-financial-plugins": true
  }
}
```

This ensures every developer has compliance and security tooling from day one, while specialized teams can add domain-specific capabilities.

## Related

* [Hierarchical Settings & Org Control](/enterprise/hierarchical-settings-and-org-control) - How org-level settings work
* [Plugins](/cli/configuration/plugins) - Plugin basics and installation
* [Building Plugins](/guides/building/building-plugins) - Create your own plugins