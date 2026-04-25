---
title: Chatwoot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/integrations/chatwoot
source: sitemap
fetched_at: 2026-04-12T18:46:36.764660446-03:00
rendered_js: false
word_count: 468
summary: This document provides a detailed technical guide on how to configure the integration between the Evolution API and the Chatwoot customer support platform. It explains the necessary steps and request bodies for setting up this connection both during new instance creation and for updating existing instances.
tags:
    - chatwoot-integration
    - api-configuration
    - instance-setup
    - whatsapp-support
    - endpoint-guide
category: guide
---

The Evolution API allows direct integration with **Chatwoot**, a customer support platform that centralizes communications from multiple channels. This documentation details how to configure this integration both when creating a new instance and in an existing instance.

## Chatwoot Integration Configuration

### 1. Configuration During Instance Creation

You can configure Chatwoot directly when creating a new instance in the Evolution API. Use the following request body for the `/instance/create` endpoint:

#### Endpoint

```
POST {{baseUrl}}/instance/create
```

#### Request Body

```
{
    "instanceName": "INSTANCE NAME",
    "number": "WHATSAPP NUMBER TO GENERATE PAIRING CODE",
    "qrcode": true,
    "integration": "WHATSAPP-BAILEYS",
    "chatwootAccountId": "1",
    "chatwootToken": "TOKEN",
    "chatwootUrl": "https://chatwoot.com",
    "chatwootSignMsg": true,
    "chatwootReopenConversation": true,
    "chatwootConversationPending": false,
    "chatwootImportContacts": true,
    "chatwootNameInbox": "evolution",
    "chatwootMergeBrazilContacts": true,
    "chatwootImportMessages": true,
    "chatwootDaysLimitImportMessages": 3,
    "chatwootOrganization": "Evolution Bot",
    "chatwootLogo": "https://evolution-api.com/files/evolution-api-favicon.png"
}
```

### 2. Configuration for Existing Instances

If you already have an instance created and want to configure or change the integration with Chatwoot, use the `/chatwoot/set/{{instance}}` endpoint with the following request format:

#### Endpoint

```
POST {{baseUrl}}/chatwoot/set/{{instance}}
```

#### Request Body

Here is an example of how the request body should look to configure the integration:

```
{
    "enabled": true,
    "accountId": "1",
    "token": "TOKEN",
    "url": "https://chatwoot.com",
    "signMsg": true,
    "reopenConversation": true,
    "conversationPending": false,
    "nameInbox": "evolution",
    "mergeBrazilContacts": true,
    "importContacts": true,
    "importMessages": true,
    "daysLimitImportMessages": 2,
    "signDelimiter": "\n",
    "autoCreate": true,
    "organization": "BOT",
    "logo": "your_logo_link"
}
```

### Parameters Explanation

- **`enabled`** : Enables (`true`) or disables (`false`) the Chatwoot integration for the instance.
- **`accountId`** : The Chatwoot account ID associated with the integration.
- **`token`** : The authentication token of the admin user in Chatwoot.
- **`url`** : The base URL of Chatwoot. Important: Do not include a trailing `/` in the URL.
- **`signMsg`** : When enabled (`true`), adds the attendant’s signature to the messages sent.
- **`reopenConversation`** : Defines whether the integration should always reopen the same conversation (`true`) or create a new one.
- **`conversationPending`** : Starts conversations as pending (`true`), awaiting action from an attendant.
- **`nameInbox`** : Custom name for the inbox in Chatwoot. If not provided, the instance name will be used.
- **`mergeBrazilContacts`** : Merges Brazilian contacts that have the additional `9` digit in their numbers (`true`).
- **`importContacts`** : Imports WhatsApp contacts into Chatwoot (`true`).
- **`importMessages`** : Imports WhatsApp messages into Chatwoot (`true`).
- **`daysLimitImportMessages`** : Sets the limit of days for importing old WhatsApp messages.
- **`signDelimiter`** : Delimiter used to separate the signature from the message body.
- **`autoCreate`** : If enabled (`true`), automatically creates the inbox configuration in Chatwoot.
- **`organization`** : The name of the bot command contact, used to customize the interaction.
- **`logo`** : URL of the image to be used as the profile picture for the bot command contact.

## Steps to Configure the Integration

1. **Obtain Credentials and URLs**:
   
   - Access the Chatwoot dashboard and obtain the `accountId` and `token` of the admin user.
   - Verify your Chatwoot’s base URL and configure it without a trailing `/`.
2. **Create or Configure the Instance**:
   
   - Use the `/instance/create` endpoint to configure Chatwoot during instance creation.
   - Use the `/chatwoot/set/{{instance}}` endpoint to configure Chatwoot in an existing instance.
3. **Verify the Configuration**:
   
   - Access Chatwoot to ensure the inbox has been created and the settings are correct.
   - Test sending and receiving messages to confirm the integration.

## Final Considerations

The integration of Evolution API with Chatwoot allows you to centralize and automate WhatsApp communication directly in your customer support platform. With options for customization, importing contacts and messages, and the ability to reopen existing conversations, this integration offers flexibility to meet the specific needs of your workflow.