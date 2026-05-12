---
title: Load LoRA
optimized: true
optimized_at: 2026-04-27T00:00:00Z
word_count: 224
---
> [!info] Auth: Bearer token required. Format: `Bearer <API_KEY>`

## Request

### Query Parameters

| Param | Type | Description |
|---|---|---|
| `addon` | string | Merges new addon to the base model. Unmerges/deletes any existing addon in the deployment. Required for hot reload deployments. |

## Body

| Field | Type | Description |
|---|---|---|
| `description` | string | Resource description. |
| `baseDeployment` | string | Resource name of the base deployment. |
| `isDefault` | boolean | If true, this is the default target when querying the model without the `#<deployment>` suffix. The first deployment a model is deployed to sets this to true. |
| `public` | boolean | If true, the deployed model is publicly reachable. |

## Response

| Field | Type | Description |
|---|---|---|
| `description` | string | Resource description. |
| `createTime` | string (date-time) | read-only. Creation time. |
| `baseDeployment` | string | Base deployment resource name. |
| `isDefault` | boolean | read-only. Default target flag. |
| `state` | enum | read-only. Deployed model state. Default: `STATE_UNSPECIFIED`. |
| `status` | object | read-only. Mirrors [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto). Deploy/undeploy details. |
| `public` | boolean | read-only. Public reachability flag. |
| `updateTime` | string (date-time) | read-only. Last update time. |

### State Options

`STATE_UNSPECIFIED`, `UNDEPLOYING`, `DEPLOYING`, `DEPLOYED`, `UPDATING`
