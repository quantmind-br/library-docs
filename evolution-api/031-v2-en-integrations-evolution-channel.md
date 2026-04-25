---
title: Evolution Channel - Evolution API Documentation
url: https://doc.evolution-api.com/v2/en/integrations/evolution-channel
source: sitemap
fetched_at: 2026-04-12T18:46:19.929820255-03:00
rendered_js: false
word_count: 493
summary: This document serves as a comprehensive guide detailing how to integrate with the Evolution Channel via the Evolution API. It covers the necessary steps for creating an integration instance and configuring webhooks to receive incoming messages, as well as receiving status updates through various event channels.
tags:
    - webhook-setup
    - api-integration
    - instance-creation
    - message-handling
    - event-notifications
category: guide
---

**Evolution Channel** is a universal integration channel that allows messages to be received through webhooks, providing flexibility to connect various systems and applications with the Evolution API. This channel facilitates automation and message management, supporting multiple integrations and workflows.

* * *

## 1. Configuring the Evolution Instance

To configure an instance in the Evolution Channel, you need to access the `/instance/create` route of the Evolution API with the following request body:

### Creating the Instance

**Endpoint**

```
POST {{baseUrl}}/instance/create
```

**Request Body** Here is an example of how to create an instance in the Evolution Channel:

```
{
    "instanceName": "INSTANCE NAME",
    "token": "INSTANCE TOKEN (OPTIONAL)",
    "number": "INSTANCE NUMBER ID",
    "qrcode": false,
    "integration": "EVOLUTION"
}
```

### Request Body Parameters

- **`instanceName`** : Name of the instance you are creating.
- **`token`** : Optional token to authenticate the instance.
- **`number`** : Number ID of the instance that will be used to receive and send messages.
- **`qrcode`** : Set to `false` because the integration does not require a QR Code.
- **`integration`** : Use `"EVOLUTION"` to specify that this integration is with the universal Evolution channel.

**Example Request**

```
curl -X POST http://API_URL/instance/create \
-H "Content-Type: application/json" \
-d '{
    "instanceName": "MyInstance",
    "token": "123456",
    "number": "9876543210",
    "qrcode": false,
    "integration": "EVOLUTION"
}'
```

* * *

## 2. Message Input in the Evolution Channel

After creating the instance, the Evolution Channel will receive the messages sent to the configured instance. These messages are sent to the `{baseUrl}/webhook/evolution` route as POST requests. This is the entry point for messages that the Evolution Channel will process. **Webhook URL for Message Input**

```
POST {{baseUrl}}/webhook/evolution
```

### Example of Message Input Payload

Here is an example of the payload format sent to the Evolution Channel when a message is received:

```
{
    "numberId": "1234567", 
    "key": {
        "remoteJid": "557499879409",
        "fromMe": false,
        "id": "ABC1234"
    },
    "pushName": "Davidson",
    "message": {
        "conversation": "What is your name?"
    },
    "messageType": "conversation"
}
```

### Explanation of Payload Fields

- **`numberId`** : ID of the number registered when creating the instance.
- **`key.remoteJid`** : Number or unique ID of the contact who sent the message.
- **`key.fromMe`** : Indicates whether the message was sent by the contact (`false`) or by the system itself (`true`).
- **`key.id`** : Unique ID of the message.
- **`pushName`** : Name of the contact who sent the message.
- **`message.conversation`** : Content of the received message.
- **`messageType`** : Type of message (in this case, `conversation`).

* * *

## 3. Feedback and Postbacks

The Evolution Channel sends feedback and postbacks through configured event channels such as webhooks, RabbitMQ, or SQS. This allows you to receive real-time notifications about the status of messages and interactions, keeping your system up to date. **Examples of Event Channels**

- **Webhook**: Notifications are sent to a specified HTTP endpoint.
- **RabbitMQ**: Messages are sent to a configured RabbitMQ queue.
- **SQS**: Messages are sent to an AWS SQS queue.

**Event Channel Configuration** To configure event channels, define the necessary parameters in your configuration file or directly in the instance, according to the Evolution API specifications.

* * *

## Conclusion

With the instance created and the message input webhook configured, your Evolution API is ready to operate with the Evolution Channel. All received messages and associated events will be managed centrally, allowing for seamless and efficient integration with your messaging and automation systems. This documentation provides a clear and detailed overview of how to integrate the Evolution Channel with the Evolution API, from instance creation to configuring webhooks and event channels. By following these steps, you will be prepared to use the universal Evolution channel in your application.