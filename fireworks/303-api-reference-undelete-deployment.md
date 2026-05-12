---
title: Undelete Deployment
url: https://docs.fireworks.ai/api-reference/undelete-deployment
source: sitemap
fetched_at: 2026-04-27T20:13:31.78720411-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - reference
category: reference
word_count: 30
---
# Undelete Deployment

> [!note]
> This is a response schema — there is no standalone API method page for undeletion. Deployments that enter a soft-deleted state return this object.

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
  "directRouteApiKeys": ["<string>"],
  "numPeftDeviceCached": 123,
  "directRouteType": "DIRECT_ROUTE_TYPE_UNSPECIFIED",
  "directRouteHandle": "<string>",
  "deploymentTemplate": "<string>",
  "autoTune": { "longPrompt": true },
  "placement": {
    "region": "REGION_UNSPECIFIED",
    "multiRegion": "MULTI_REGION_UNSPECIFIED",
    "regions": ["REGION_UNSPECIFIED"]
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