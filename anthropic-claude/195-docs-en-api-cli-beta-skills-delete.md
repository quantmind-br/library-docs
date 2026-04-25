---
title: Delete Skill (Beta) (cli)
url: https://platform.claude.com/docs/en/api/cli/beta/skills/delete.md
source: llms
fetched_at: 2026-04-16T22:45:31.990304436-03:00
rendered_js: false
word_count: 55
summary: This document defines the API endpoint and parameters required to permanently remove a specific skill using the beta CLI command.
tags:
    - cli-command
    - api-reference
    - resource-deletion
    - beta-features
category: api
---

## Delete

`$ ant beta:skills delete`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillDeleteResponse: object { id, type }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```cli
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```