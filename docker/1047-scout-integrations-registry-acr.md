---
title: Azure Container Registry
url: https://docs.docker.com/scout/integrations/registry/acr/
source: llms
fetched_at: 2026-01-24T14:29:13.613486623-03:00
rendered_js: false
word_count: 0
summary: This Azure Resource Manager template automates the integration of Docker Scout with Azure Container Registry by configuring Event Grid system topics and subscriptions for image events.
tags:
    - arm-template
    - azure-container-registry
    - docker-scout
    - event-grid
    - infrastructure-as-code
    - webhook-integration
category: configuration
---

```
{
   "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
   "contentVersion": "1.0.0.0",
   "parameters": {
      "DockerScoutWebhook": {
         "metadata": {
            "description": "EventGrid's subscription Webhook"
         },
         "type": "String"
      },
      "RegistryName": {
         "metadata": {
            "description": "Name of the registry to add Docker Scout"
         },
         "type": "String"
      },
      "systemTopics_dockerScoutRepository": {
         "defaultValue": "docker-scout-repository",
         "metadata": {
            "description": "EventGrid's topic name"
         },
         "type": "String"
      }
   },
   "resources": [
      {
         "apiVersion": "2023-06-01-preview",
         "identity": {
            "type": "None"
         },
         "location": "[resourceGroup().location]",
         "name": "[parameters('systemTopics_dockerScoutRepository')]",
         "properties": {
            "source": "[extensionResourceId(resourceGroup().Id , 'Microsoft.ContainerRegistry/Registries', parameters('RegistryName'))]",
            "topicType": "Microsoft.ContainerRegistry.Registries"
         },
         "type": "Microsoft.EventGrid/systemTopics"
      },
      {
         "apiVersion": "2023-06-01-preview",
         "dependsOn": [
            "[resourceId('Microsoft.EventGrid/systemTopics', parameters('systemTopics_dockerScoutRepository'))]"
         ],
         "name": "[concat(parameters('systemTopics_dockerScoutRepository'), '/image-change')]",
         "properties": {
            "destination": {
               "endpointType": "WebHook",
               "properties": {
                  "endpointUrl": "[parameters('DockerScoutWebhook')]",
                  "maxEventsPerBatch": 1,
                  "preferredBatchSizeInKilobytes": 64
               }
            },
            "eventDeliverySchema": "EventGridSchema",
            "filter": {
               "enableAdvancedFilteringOnArrays": true,
               "includedEventTypes": [
                  "Microsoft.ContainerRegistry.ImagePushed",
                  "Microsoft.ContainerRegistry.ImageDeleted"
               ]
            },
            "labels": [],
            "retryPolicy": {
               "eventTimeToLiveInMinutes": 1440,
               "maxDeliveryAttempts": 30
            }
         },
         "type": "Microsoft.EventGrid/systemTopics/eventSubscriptions"
      },
      {
         "apiVersion": "2023-01-01-preview",
         "name": "[concat(parameters('RegistryName'), '/docker-scout-readonly-token')]",
         "properties": {
            "credentials": {},
            "scopeMapId": "[resourceId('Microsoft.ContainerRegistry/registries/scopeMaps', parameters('RegistryName'), '_repositories_pull_metadata_read')]"
         },
         "type": "Microsoft.ContainerRegistry/registries/tokens"
      }
   ],
   "variables": {}
}
```