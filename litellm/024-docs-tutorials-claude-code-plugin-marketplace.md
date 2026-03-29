---
title: Claude Code Plugin Marketplace | liteLLM
url: https://docs.litellm.ai/docs/tutorials/claude_code_plugin_marketplace
source: sitemap
fetched_at: 2026-01-21T19:55:03.021784724-03:00
rendered_js: false
word_count: 405
summary: This document explains how to set up and manage a centralized Claude Code plugin marketplace using LiteLLM, covering administrator management, engineer installation workflows, and associated API endpoints.
tags:
    - litellm
    - claude-code
    - plugin-management
    - marketplace-registry
    - api-gateway
    - plugin-governance
category: guide
---

LiteLLM AI Gateway acts as a central registry for Claude Code plugins. Admins can govern which plugins are available across the organization, and engineers can discover and install approved plugins from a single source.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- LiteLLM Proxy running with database connected
- Admin access to LiteLLM UI
- Plugins hosted on GitHub, GitLab, or any git-accessible URL

## Admin Guide: Managing the Marketplace[​](#admin-guide-managing-the-marketplace "Direct link to Admin Guide: Managing the Marketplace")

### Step 1: Navigate to Claude Code Plugins[​](#step-1-navigate-to-claude-code-plugins "Direct link to Step 1: Navigate to Claude Code Plugins")

In the LiteLLM Admin UI, click on **Claude Code Plugins** in the left navigation menu.

### Step 2: View the Plugins List[​](#step-2-view-the-plugins-list "Direct link to Step 2: View the Plugins List")

You'll see the list of all registered plugins. From here you can add, enable, disable, or delete plugins.

### Step 3: Add a New Plugin[​](#step-3-add-a-new-plugin "Direct link to Step 3: Add a New Plugin")

Click **+ Add New Plugin** to register a plugin in your marketplace.

### Step 4: Fill in Plugin Details[​](#step-4-fill-in-plugin-details "Direct link to Step 4: Fill in Plugin Details")

Enter the plugin information:

- **Name**: Plugin identifier (kebab-case, e.g., `my-plugin`)
- **Source Type**: Choose GitHub or URL
- **Repository/URL**: The git source (e.g., `org/repo` for GitHub)
- **Version**: Semantic version (optional)
- **Description**: What the plugin does
- **Category**: Plugin category for organization
- **Keywords**: Search terms

### Step 5: Submit the Plugin[​](#step-5-submit-the-plugin "Direct link to Step 5: Submit the Plugin")

After filling in the details, click **Add Plugin** to register it.

### Step 6: Enable/Disable Plugins[​](#step-6-enabledisable-plugins "Direct link to Step 6: Enable/Disable Plugins")

Toggle plugins on or off to control what appears in the public marketplace. Only **enabled** plugins are visible to engineers.

## Engineer Guide: Installing Plugins[​](#engineer-guide-installing-plugins "Direct link to Engineer Guide: Installing Plugins")

### Step 1: Add the LiteLLM Marketplace[​](#step-1-add-the-litellm-marketplace "Direct link to Step 1: Add the LiteLLM Marketplace")

Add your company's LiteLLM marketplace to Claude Code:

```
claude plugin marketplace add http://your-litellm-proxy:4000/claude-code/marketplace.json
```

### Step 2: Browse Available Plugins[​](#step-2-browse-available-plugins "Direct link to Step 2: Browse Available Plugins")

List all available plugins from the marketplace:

```
claude plugin search @litellm
```

### Step 3: Install a Plugin[​](#step-3-install-a-plugin "Direct link to Step 3: Install a Plugin")

Install any plugin from the marketplace:

```
claude plugin install my-plugin@litellm
```

### Step 4: Verify Installation[​](#step-4-verify-installation "Direct link to Step 4: Verify Installation")

The plugin is now installed and ready to use:

## API Reference[​](#api-reference "Direct link to API Reference")

### Public Endpoint (No Auth Required)[​](#public-endpoint-no-auth-required "Direct link to Public Endpoint (No Auth Required)")

#### GET `/claude-code/marketplace.json`[​](#get-claude-codemarketplacejson "Direct link to get-claude-codemarketplacejson")

Returns the marketplace catalog for Claude Code discovery.

```
curl http://localhost:4000/claude-code/marketplace.json
```

**Response:**

```
{
"name":"litellm",
"owner":{
"name":"LiteLLM",
"email":"support@litellm.ai"
},
"plugins":[
{
"name":"my-plugin",
"source":{
"source":"github",
"repo":"org/my-plugin"
},
"version":"1.0.0",
"description":"My awesome plugin",
"category":"productivity",
"keywords":["automation","tools"]
}
]
}
```

### Admin Endpoints (Auth Required)[​](#admin-endpoints-auth-required "Direct link to Admin Endpoints (Auth Required)")

#### POST `/claude-code/plugins`[​](#post-claude-codeplugins "Direct link to post-claude-codeplugins")

Register a new plugin.

```
curl -X POST http://localhost:4000/claude-code/plugins \
  -H "Authorization: Bearer sk-..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-plugin",
    "source": {"source": "github", "repo": "org/my-plugin"},
    "version": "1.0.0",
    "description": "My awesome plugin",
    "category": "productivity",
    "keywords": ["automation", "tools"]
  }'
```

#### GET `/claude-code/plugins`[​](#get-claude-codeplugins "Direct link to get-claude-codeplugins")

List all registered plugins.

```
curl http://localhost:4000/claude-code/plugins \
  -H "Authorization: Bearer sk-..."
```

#### POST `/claude-code/plugins/{name}/enable`[​](#post-claude-codepluginsnameenable "Direct link to post-claude-codepluginsnameenable")

Enable a plugin.

```
curl -X POST http://localhost:4000/claude-code/plugins/my-plugin/enable \
  -H "Authorization: Bearer sk-..."
```

#### POST `/claude-code/plugins/{name}/disable`[​](#post-claude-codepluginsnamedisable "Direct link to post-claude-codepluginsnamedisable")

Disable a plugin.

```
curl -X POST http://localhost:4000/claude-code/plugins/my-plugin/disable \
  -H "Authorization: Bearer sk-..."
```

#### DELETE `/claude-code/plugins/{name}`[​](#delete-claude-codepluginsname "Direct link to delete-claude-codepluginsname")

Delete a plugin.

```
curl -X DELETE http://localhost:4000/claude-code/plugins/my-plugin \
  -H "Authorization: Bearer sk-..."
```

## Plugin Source Formats[​](#plugin-source-formats "Direct link to Plugin Source Formats")

- GitHub
- Git URL

```
{
"name":"my-plugin",
"source":{
"source":"github",
"repo":"organization/repository"
}
}
```

## Example: Setting Up an Internal Plugin Marketplace[​](#example-setting-up-an-internal-plugin-marketplace "Direct link to Example: Setting Up an Internal Plugin Marketplace")

### 1. Create Internal Plugins[​](#1-create-internal-plugins "Direct link to 1. Create Internal Plugins")

Structure your plugin repository:

```
my-company-plugin/
├── plugin.json          # Plugin manifest
├── SKILL.md            # Main skill file
├── skills/             # Additional skills
│   └── helper.md
└── README.md
```

### 2. Register Plugins via API[​](#2-register-plugins-via-api "Direct link to 2. Register Plugins via API")

```
# Register your internal tools plugin
curl -X POST http://localhost:4000/claude-code/plugins \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "internal-tools",
    "source": {"source": "github", "repo": "mycompany/internal-tools"},
    "version": "1.0.0",
    "description": "Internal development tools and utilities",
    "author": {"name": "Platform Team", "email": "platform@mycompany.com"},
    "category": "internal",
    "keywords": ["internal", "tools", "utilities"]
  }'
```

Send engineers the marketplace URL:

```
# One-time setup for each engineer
claude plugin marketplace add http://litellm.internal.company.com/claude-code/marketplace.json

# Install company plugins
claude plugin install internal-tools@litellm
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Plugin not appearing in marketplace:**

- Verify the plugin is **enabled** in the admin UI
- Check that the plugin has a valid `source` field

**Installation fails:**

- Ensure the git repository is accessible from the engineer's machine
- For private repos, engineers need appropriate git credentials configured

**Database errors:**

- Verify LiteLLM proxy is connected to the database
- Check proxy logs for detailed error messages