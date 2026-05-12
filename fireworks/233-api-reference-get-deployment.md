---
title: Get Deployment - Fireworks AI
url: https://docs.fireworks.ai/api-reference/get-deployment
source: sitemap
fetched_at: 2026-04-27T20:14:16.061870917-03:00
rendered_js: false
word_count: 533
summary: Response schema for the GET /accounts/{account_id}/deployments/{deployment_id} endpoint.
tags:
    - api-reference
    - deployments
    - response-schema
    - autoscaling
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
GET `v1/accounts/{account_id}/deployments/{deployment_id}`

## Response

| Field | Type | Description |
|---|---|---|
| `name` | string | Resource name |
| `displayName` | string | Display name |
| `description` | string | Description |
| `baseModel` | string | Base model identifier |
| `createTime` | string (RFC3339) | Creation timestamp |
| `expireTime` | string (RFC3339) | Expiration timestamp |
| `purgeTime` | string (RFC3339) | Purge timestamp |
| `deleteTime` | string (RFC3339) | Deletion timestamp |
| `state` | string | Deployment state |
| `status.code` | string | Status code (e.g. `OK`) |
| `status.message` | string | Status message |
| `annotations` | object | Annotations key-value pairs |
| `minReplicaCount` | integer | Minimum replica count |
| `maxReplicaCount` | integer | Maximum replica count |
| `maxWithRevocableReplicaCount` | integer | Max revocable replicas |
| `desiredReplicaCount` | integer | Desired replica count |
| `replicaCount` | integer | Current replica count |
| `autoscalingPolicy.scaleUpWindow` | string | Scale-up window duration |
| `autoscalingPolicy.scaleDownWindow` | string | Scale-down window duration |
| `autoscalingPolicy.scaleToZeroWindow` | string | Scale-to-zero window duration |
| `autoscalingPolicy.loadTargets` | object | Load target metrics |
| `autoscalingPolicy.scalingSchedules` | object | Scheduled scaling rules |
| `acceleratorCount` | integer | Number of accelerators |
| `acceleratorType` | string | Accelerator type |
| `precision` | string | Precision setting |
| `cluster` | string | Cluster identifier |
| `enableAddons` | boolean | Enable addons |
| `draftTokenCount` | integer | Draft token count |
| `draftModel` | string | Draft model |
| `ngramSpeculationLength` | integer | N-gram speculation length |
| `enableSessionAffinity` | boolean | Enable session affinity |
| `directRouteApiKeys` | string[] | API keys for direct routing |
| `numPeftDeviceCached` | integer | Number of PEFT devices cached |
| `directRouteType` | string | Direct route type |
| `directRouteHandle` | string | Direct route handle |
| `deploymentTemplate` | string | Deployment template |
| `autoTune.longPrompt` | boolean | Auto-tune for long prompts |
| `placement.region` | string | Primary region |
| `placement.multiRegion` | string | Multi-region mode |
| `placement.regions` | string[] | Allowed regions |
| `region` | string | Deployment region |
| `maxContextLength` | integer | Max context length |
| `updateTime` | string (RFC3339) | Last update timestamp |
| `disableDeploymentSizeValidation` | boolean | Disable size validation |
| `enableHotLoad` | boolean | Enable hot load |
| `hotLoadBucketType` | string | Hot load bucket type |
| `enableHotReloadLatestAddon` | boolean | Auto-reload latest addon |
| `deploymentShape` | string | Deployment shape name |
| `activeModelVersion` | string | Active model version |
| `targetModelVersion` | string | Target model version |
| `replicaStats.pendingSchedulingReplicaCount` | integer | Pending scheduling replicas |
| `replicaStats.downloadingModelReplicaCount` | integer | Downloading model replicas |
| `replicaStats.initializingReplicaCount` | integer | Initializing replicas |
| `replicaStats.readyReplicaCount` | integer | Ready replicas |
| `replicaStats.revocableReplicaCount` | integer | Revocable replicas |
| `replicaStats.partialReplicaCount` | integer | Partial replicas |
| `hotLoadBucketUrl` | string | Hot load bucket URL |
| `pricingPlanId` | string | Pricing plan identifier |
| `hotLoadTrainerJob` | string | Hot load trainer job |

```json
{
  "baseModel": "<string>",
  "name": "<string>",
  "displayName": "<string>",
  "description": "<string>",
  "createTime": "2023-11-07T05:31:56Z",
  "expireTime": "2023-11-07T05:31:56Z",
  "purgeTime": "2023-11-07T05:31:56Z",
  "deleteTime": "2023-11-07T05:31:56Z",
  "state": "STATE_UNSPECIFIED",
  "status": {
    "code": "OK",
    "message": "<string>"
  },
  "annotations": {},
  "minReplicaCount": 123,
  "maxReplicaCount": 123,
  "maxWithRevocableReplicaCount": 123,
  "desiredReplicaCount": 123,
  "replicaCount": 123,
  "autoscalingPolicy": {
    "scaleUpWindow": "<string>",
    "scaleDownWindow": "<string>",
    "scaleToZeroWindow": "<string>",
    "loadTargets": {},
    "scalingSchedules": {}
  },
  "acceleratorCount": 123,
  "acceleratorType": "ACCELERATOR_TYPE_UNSPECIFIED",
  "precision": "PRECISION_UNSPECIFIED",
  "cluster": "<string>",
  "enableAddons": true,
  "draftTokenCount": 123,
  "draftModel": "<string>",
  "ngramSpeculationLength": 123,
  "enableSessionAffinity": true,
  "directRouteApiKeys": [
    "<string>"
  ],
  "numPeftDeviceCached": 123,
  "directRouteType": "DIRECT_ROUTE_TYPE_UNSPECIFIED",
  "directRouteHandle": "<string>",
  "deploymentTemplate": "<string>",
  "autoTune": {
    "longPrompt": true
  },
  "placement": {
    "region": "REGION_UNSPECIFIED",
    "multiRegion": "MULTI_REGION_UNSPECIFIED",
    "regions": [
      "REGION_UNSPECIFIED"
    ]
  },
  "region": "REGION_UNSPECIFIED",
  "maxContextLength": 123,
  "updateTime": "2023-11-07T05:31:56Z",
  "disableDeploymentSizeValidation": true,
  "enableHotLoad": true,
  "hotLoadBucketType": "BUCKET_TYPE_UNSPECIFIED",
  "enableHotReloadLatestAddon": true,
  "deploymentShape": "<string>",
  "activeModelVersion": "<string>",
  "targetModelVersion": "<string>",
  "replicaStats": {
    "pendingSchedulingReplicaCount": 123,
    "downloadingModelReplicaCount": 123,
    "initializingReplicaCount": 123,
    "readyReplicaCount": 123,
    "revocableReplicaCount": 123,
    "partialReplicaCount": 123
  },
  "hotLoadBucketUrl": "<string>",
  "pricingPlanId": "<string>",
  "hotLoadTrainerJob": "<string>"
}
```