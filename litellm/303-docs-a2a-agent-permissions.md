---
title: Agent Permission Management | liteLLM
url: https://docs.litellm.ai/docs/a2a_agent_permissions
source: sitemap
fetched_at: 2026-01-21T19:43:49.200196267-03:00
rendered_js: false
word_count: 345
summary: This document explains how to manage access control for A2A agents in LiteLLM by restricting agent permissions for specific virtual keys and teams.
tags:
    - litellm
    - agent-permissions
    - access-control
    - security
    - multi-tenancy
    - api-keys
    - team-management
category: guide
---

Control which A2A agents can be accessed by specific keys or teams in LiteLLM.

## Overview[​](#overview "Direct link to Overview")

Agent Permission Management lets you restrict which agents a LiteLLM Virtual Key or Team can access. This is useful for:

- **Multi-tenant environments**: Give different teams access to different agents
- **Security**: Prevent keys from invoking agents they shouldn't have access to
- **Compliance**: Enforce access policies for sensitive agent workflows

When permissions are configured:

- `GET /v1/agents` only returns agents the key/team can access
- `POST /a2a/{agent_id}` (Invoking an agent) returns `403 Forbidden` if access is denied

## Setting Permissions on a Key[​](#setting-permissions-on-a-key "Direct link to Setting Permissions on a Key")

This example shows how to create a key with agent permissions and test access.

### 1. Get Your Agent ID[​](#1-get-your-agent-id "Direct link to 1. Get Your Agent ID")

- UI
- API

<!--THE END-->

1. Go to **Agents** in the sidebar
2. Click into the agent you want
3. Copy the **Agent ID**

### 2. Create a Key with Agent Permissions[​](#2-create-a-key-with-agent-permissions "Direct link to 2. Create a Key with Agent Permissions")

- UI
- API

<!--THE END-->

1. Go to **Keys** → **Create Key**
2. Expand **Agent Settings**
3. Select the agents you want to allow

### 3. Test Access[​](#3-test-access "Direct link to 3. Test Access")

**Allowed agent (succeeds):**

Invoke allowed agent

```
curl -X POST "http://localhost:4000/a2a/agent-123" \
  -H "Authorization: Bearer sk-your-new-key" \
  -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"type": "text", "text": "Hello"}]}}'
```

**Blocked agent (fails with 403):**

Invoke blocked agent

```
curl -X POST "http://localhost:4000/a2a/agent-456" \
  -H "Authorization: Bearer sk-your-new-key" \
  -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"type": "text", "text": "Hello"}]}}'
```

Response:

403 Forbidden Response

```
{
"error":{
"message":"Access denied to agent: agent-456",
"code":403
}
}
```

## Setting Permissions on a Team[​](#setting-permissions-on-a-team "Direct link to Setting Permissions on a Team")

Restrict all keys belonging to a team to only access specific agents.

### 1. Create a Team with Agent Permissions[​](#1-create-a-team-with-agent-permissions "Direct link to 1. Create a Team with Agent Permissions")

- UI
- API

<!--THE END-->

1. Go to **Teams** → **Create Team**
2. Expand **Agent Settings**
3. Select the agents you want to allow for this team

### 2. Create a Key for the Team[​](#2-create-a-key-for-the-team "Direct link to 2. Create a Key for the Team")

- UI
- API

<!--THE END-->

1. Go to **Keys** → **Create Key**
2. Select the **Team** from the dropdown

### 3. Test Access[​](#3-test-access-1 "Direct link to 3. Test Access")

The key inherits agent permissions from the team.

**Allowed agent (succeeds):**

Invoke allowed agent

```
curl -X POST "http://localhost:4000/a2a/agent-123" \
  -H "Authorization: Bearer sk-team-key" \
  -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"type": "text", "text": "Hello"}]}}'
```

**Blocked agent (fails with 403):**

Invoke blocked agent

```
curl -X POST "http://localhost:4000/a2a/agent-456" \
  -H "Authorization: Bearer sk-team-key" \
  -H "Content-Type: application/json" \
  -d '{"message": {"role": "user", "parts": [{"type": "text", "text": "Hello"}]}}'
```

## How It Works[​](#how-it-works "Direct link to How It Works")

Key PermissionsTeam PermissionsResultNotesNoneNoneKey can access **all** agentsOpen access by default when no restrictions are set`["agent-1", "agent-2"]`NoneKey can access `agent-1` and `agent-2`Key uses its own permissionsNone`["agent-1", "agent-3"]`Key can access `agent-1` and `agent-3`Key inherits team's permissions`["agent-1", "agent-2"]``["agent-1", "agent-3"]`Key can access `agent-1` onlyIntersection of both lists (most restrictive wins)

## Viewing Permissions[​](#viewing-permissions "Direct link to Viewing Permissions")

- UI
- API

<!--THE END-->

1. Go to **Keys** or **Teams**
2. Click into the key/team you want to view
3. Agent permissions are displayed in the info view