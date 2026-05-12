---
title: Update LoRA
url: https://docs.fireworks.ai/api-reference/update-deployed-model
source: sitemap
fetched_at: 2026-04-27T20:13:38.495957185-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - api-authorization
    - bearer-authentication
    - deployed-model
    - resource-properties
    - deployment-status
category: reference
word_count: 198
---
Updates a deployed model (LoRA) via the Fireworks API.

#### Authorizations

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

#### Body

| Field | Type | Description |
|-------|------|-------------|
| `deployed_model.name` | string | **Required.** Updated resource name. |
| `description` | string | Description of the resource. |
| `deployment` | string | Resource name of the base deployment. |
| `default` | boolean | If `true`, this is the default target when querying without the `#<deployment>` suffix. The first deployment a model is deployed to has this set to `true`. |
| `public` | boolean | If `true`, the deployed model is publicly reachable. |

#### Response

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Description |
| `createTime` | string (date-time) | Creation time (read-only) |
| `deployment` | string | Base deployment resource name |
| `default` | boolean | Default deployment flag |
| `state` | enum | State (read-only): `STATE_UNSPECIFIED`, `UNDEPLOYING`, `DEPLOYING`, `DEPLOYED`, `UPDATING` |
| `status` | object | Deploy/undeploy details per [google.rpc.status](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) (read-only) |
| `public` | boolean | Public reachability |
| `updateTime` | string (date-time) | Last update time (read-only) |
