---
title: Update Deployment - Fireworks AI Docs
url: https://docs.fireworks.ai/api-reference/update-deployment
source: sitemap
fetched_at: 2026-04-27T20:13:39.456450346-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - deployment-configuration
    - api-post
    - fireworks-ai
    - rest-api
    - autoscaling
    - replica-count
    - accelerator-type
    - model-precision
category: reference
word_count: 944
---
Updates an existing deployment via `PATCH /v1/accounts/{account_id}/deployments/{deployment_id}`.

## Authorization

Bearer authentication using your Fireworks API key. Format: `Bearer <API_KEY>`

## Query Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `skipShapeValidation` | boolean | If `true`, the new deployment shape is not required to be validated |

## Request Body

| Field | Type | Description |
|-------|------|-------------|
| `deployment.name` | string | **Required.** The resource name of the deployment being updated |
| `displayName` | string | Human-readable name; must be under 64 characters |
| `description` | string | Description of the deployment |
| `autoDeleteTime` | string (date-time) | **Deprecated.** Scheduled deletion time (no longer causes auto-deletion) |
| `annotations` | object | Key/value pairs for external tools; `image-tag-reason` is redacted for non-superusers |
| `minReplicaCount` | integer | Minimum replicas; default 0 |
| `maxReplicaCount` | integer | Maximum replicas; default `max(min_replica_count, 1)`; set to 0 to downscale |
| `maxWithRevocableReplicaCount` | integer | Max replica count including revocable capacity |
| `acceleratorCount` | integer | Accelerators per replica; defaults to the model's estimated minimum |
| `acceleratorType` | enum | Accelerator type: `ACCELERATOR_TYPE_UNSPECIFIED`, `NVIDIA_A100_80GB`, `NVIDIA_H100_80GB`, `AMD_MI300X_192GB`, `NVIDIA_A10G_24GB`, `NVIDIA_A100_40GB`, `NVIDIA_L4_24GB`, `NVIDIA_H200_141GB`, `NVIDIA_B200_180GB`, `AMD_MI325X_256GB`, `AMD_MI350X_288GB`, `NVIDIA_B300_288GB` |
| `precision` | enum | Serving precision: `PRECISION_UNSPECIFIED`, `FP16`, `FP8`, `FP8_MM`, `FP8_AR`, `FP8_MM_KV_ATTN`, `FP8_KV`, `FP8_MM_V2`, `FP8_V2`, `FP8_MM_KV_ATTN_V2`, `NF4`, `FP4`, `BF16`, `FP4_BLOCKSCALED_MM`, `FP4_MX_MOE` |
| `enableAddons` | boolean | Enable PEFT addons for this deployment |
| `speculativeDecodingDraftTokenCount` | integer | Candidate tokens per speculative decoding step; defaults to base model's value; set `disableSpeculativeDecoding` to `false` to disable |
| `speculativeDecodingDraftModel` | string | Draft model name; e.g. `accounts/fireworks/models/my-draft-model`; empty disables speculative decoding; defaults to base model's `default_draft_model` |
| `ngramSpeculationLength` | integer | Length of previous input sequence for N-gram speculation |
| `sessionAffinity` | boolean | Apply sticky routing based on `user` field |
| `directRouteApiKeys` | array | API keys for direct route access |
| `directRouteType` | enum | Bypass the API gateway: `DIRECT_ROUTE_TYPE_UNSPECIFIED`, `INTERNET`, `GCP_PRIVATE_SERVICE_CONNECT`, `AWS_PRIVATELINK` |
| `deploymentTemplate` | string | Deployment template name (enterprise only) |
| `performanceProfile` | string | Performance profile |
| `region` | string | Desired geographic region; default is `GLOBAL` multi-region |
| `maxContextLength` | integer | Maximum context length; defaults to model's default if 0 or unset |
| `disableDeploymentSizeValidation` | boolean | Disable deployment size validation |
| `useHotLoad` | boolean | Enable hot load |
| `hotLoadBucketType` | enum | Bucket type: `BUCKET_TYPE_UNSPECIFIED`, `MINIO`, `S3`, `NEBIUS`, `FW_HOSTED` |
| `enableHotReloadLatestAddon` | boolean | Allow up to 1 addon at a time, merged into the base model |
| `deploymentShape` | string | Deployment shape name; replaced server-side with the shape version name |
| `activeModelVersion` | string | Model version currently active on running replicas |
| `targetModelVersion` | string | Model version being rolled out; equals `activeModelVersion` at steady state |
| `pricingPlanId` | string | Custom billing plan ID |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `displayName` | string | Human-readable display name |
| `description` | string | Description |
| `createTime` | string (date-time) | Creation time (read-only) |
| `autoDeleteTime` | string (date-time) | **Deprecated.** Scheduled deletion time |
| `purgeTime` | string (date-time) | Hard deletion time (read-only) |
| `deleteTime` | string (date-time) | Soft deletion time (read-only) |
| `state` | enum | Deployment state (read-only): `STATE_UNSPECIFIED`, `CREATING`, `READY`, `DELETING`, `FAILED`, `UPDATING`, `DELETED` |
| `status` | object | RPC status per [google/rpc/status.proto](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) (read-only) |
| `annotations` | object | Key/value pairs; `image-tag-reason` redacted for non-superusers |
| `minReplicaCount` | integer | Minimum replicas |
| `maxReplicaCount` | integer | Maximum replicas |
| `maxWithRevocableReplicaCount` | integer | Max replicas including revocable capacity |
| `desiredReplicaCount` | integer | Target replica count (read-only) |
| `acceleratorCount` | integer | Accelerators per replica |
| `acceleratorType` | enum | Accelerator type |
| `precision` | enum | Serving precision |
| `cloudPremise` | boolean | Deployed to a cloud-premise cluster |
| `enableAddons` | boolean | PEFT addons enabled |
| `speculativeDecodingDraftTokenCount` | integer | Candidate tokens per step |
| `speculativeDecodingDraftModel` | string | Draft model name |
| `ngramSpeculationLength` | integer | N-gram speculation length |
| `sessionAffinity` | boolean | Sticky routing enabled |
| `directRouteApiKeys` | array | Direct route API keys |
| `directRouteType` | enum | Direct route type |
| `directRouteHandle` | string | Direct route handle (format depends on type: hostname for `INTERNET`, service attachment for `GCP_PRIVATE_SERVICE_CONNECT`, VPC endpoint for `AWS_PRIVATELINK`) |
| `deploymentTemplate` | string | Deployment template (enterprise only) |
| `performanceProfile` | string | Performance profile |
| `region` | string | Desired placement region |
| `region` | enum | Current region (read-only): `REGION_UNSPECIFIED`, `US_IOWA_1`, `US_VIRGINIA_1`, `US_VIRGINIA_2`, `US_ILLINOIS_1`, `AP_TOKYO_1`, `US_ARIZONA_1`, `US_TEXAS_1`, `US_ILLINOIS_2`, `EU_FRANKFURT_1`, `US_TEXAS_2`, `EU_ICELAND_1`, `EU_ICELAND_2`, `US_WASHINGTON_1`, `US_WASHINGTON_2`, `US_WASHINGTON_3`, `AP_TOKYO_2`, `US_CALIFORNIA_1`, `US_UTAH_1`, `US_GEORGIA_1`, `US_GEORGIA_2`, `US_WASHINGTON_4`, `US_GEORGIA_3`, `NA_BRITISHCOLUMBIA_1`, `US_GEORGIA_4`, `US_OHIO_1`, `US_NEWYORK_1`, `EU_NETHERLANDS_1`, `US_WASHINGTON_5`, `US_MINNESOTA_1`, `US_CALIFORNIA_2`, `AP_MALAYSIA_1`, `US_OHIO_2` |
| `maxContextLength` | integer | Maximum context length |
| `updateTime` | string (date-time) | Last update time (read-only) |
| `disableDeploymentSizeValidation` | boolean | Deployment size validation disabled |
| `useHotLoad` | boolean | Hot load enabled |
| `hotLoadBucketType` | enum | Bucket type |
| `enableHotReloadLatestAddon` | boolean | Hot reload of latest addon enabled |
| `deploymentShape` | string | Deployment shape name (replaced with version name server-side) |
| `activeModelVersion` | string | Active model version |
| `targetModelVersion` | string | Target model version being rolled out |
| `replicaStatusCounters` | object | Per-replica deployment status counters tracking replica lifecycle stages |
| `pricingPlanId` | string | Custom billing plan ID |
