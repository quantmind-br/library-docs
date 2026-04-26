---
title: Beta Agents
url: https://docs.mistral.ai/api/endpoint/beta/agents
source: sitemap
fetched_at: 2026-04-26T04:01:25.291014743-03:00
rendered_js: false
word_count: 215
summary: REST API endpoints for managing AI agent entities, including creation, versioning, and alias configuration.
tags:
    - api-endpoints
    - agent-management
    - version-control
    - rest-api
    - automation
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Beta Agents

CRUD API for AI agent entities.

---

## List Agents

`GET /v1/agents`

Retrieve agents sorted by creation time.

---

## Create Agent

`POST /v1/agents`

Create an agent with instructions, tools, and description. Available for use in conversations or agent pools.

---

## Get Agent

`GET /v1/agents/{agent_id}`

Retrieve agent entity. Use `agent_version` parameter (integer or alias string) to specify version.

---

## Update Agent

`PATCH /v1/agents/{agent_id}`

Update agent attributes and create new version.

---

## Delete Agent

`DELETE /v1/agents/{agent_id}`

---

## Switch Agent Version

`PATCH /v1/agents/{agent_id}/version`

Switch the version of an agent.

---

## List Agent Versions

`GET /v1/agents/{agent_id}/versions`

Retrieve all versions with full agent context. Supports pagination.

---

## Get Agent Version

`GET /v1/agents/{agent_id}/versions/{version}`

Get specific agent version by version number.

---

## List Aliases

`GET /v1/agents/{agent_id}/aliases`

Retrieve all version aliases for an agent.

---

## Create or Update Alias

`PUT /v1/agents/{agent_id}/aliases`

Create new alias or reassign existing alias to a different version. Aliases are unique per agent.

---

## Delete Alias

`DELETE /v1/agents/{agent_id}/aliases`

Delete an existing alias.

#agent-management #version-control #rest-api
