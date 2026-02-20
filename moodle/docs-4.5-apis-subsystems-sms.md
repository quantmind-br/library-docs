---
title: SMS API | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/sms
source: sitemap
fetched_at: 2026-02-17T15:15:11.040388-03:00
rendered_js: false
word_count: 606
summary: This document explains how to utilize the SMS API and the core SMS manager class to send, retrieve, and monitor SMS messages within a plugin environment.
tags:
    - sms-api
    - messaging
    - moodle-development
    - sms-gateway
    - message-tracking
    - hooks
category: api
---

The SMS API allows developers to implement SMS-related features into their plugins. The subsystem contains an SMS Manager class `\core_sms\manager` which facilitates the actions performed by the API.

Some of the actions made possible are:

- Sending messages
- Fetching messages
- Checking the status of a message
- Getting SMS gateways.

Currently, the design of the SMS API features the following plugin types:

- [SMS gateway](https://moodledev.io/docs/4.5/apis/plugintypes/sms)

## Sending an SMS[​](#sending-an-sms "Direct link to Sending an SMS")

Messages can be sent using the `send()` method of the SMS Manager class, which should be fetched using Dependency Injection, for example:

Sending a message

```
$message=\core\di::get(\core_sms\manager::class)
->send(
recipientnumber:'+61987654321',
content:'This is the content of the message',
component:'mod_example',
messagetype:'demonstrationmessage',
recipientuserid:$user->id,
issensitive:false,
async:false,
);
```

Message lengths

A single SMS sent by the API may consist of up to 480 UTF-8 characters. It is up to the message *gateway plugin* to determine how this message is sent to the recipient.

Any message longer than the maximum length will be immediately rejected.

### Parameter consideration while sending messages[​](#parameter-consideration-while-sending-messages "Direct link to Parameter consideration while sending messages")

When sending a message it's important to add the correct `component` (for example `tool_mfa`) and `messagetype` (for example `mfa code`) for record keeping purposes.

One component can have many different types of messages and those types should be clearly mentioned while sending the messages so that they are clear in reporting and other locations.

info

In future reporting will be available for messages status. See [MDL-80963](https://moodle.atlassian.net/browse/MDL-80963) for further information

### Sending messages containing sensitive information[​](#sending-messages-containing-sensitive-information "Direct link to Sending messages containing sensitive information")

When sending a message containing something like a 2FA login token, you should make use of the `issensitive` flag.

Passing this flag prevents the SMS subsystem from storing the content of the message in the message log.

The `send()` method return an instance of `\core_sms\message` which can be used to check on the message status.

warning

Messages containing sensitive information cannot be sent asynchronously.

Sensitive content is not persisted to the database and is therefore not available in a separate PHP process.

Availability of asynchronous message handling

The ability to send messages asynchronously has not yet been implemented. The parameter is included for future compatibility.

See [MDL-81015](https://moodle.atlassian.net/browse/MDL-81015) for more information on this feature.

## Fetching messages[​](#fetching-messages "Direct link to Fetching messages")

Every sent message is stored in the database to support status checks, and for subsequent reporting.

Messages can be fetched from the database by calling the `\core_sms\manager::get_message()` and `\core_sms\manager::get_messages()` methods and supplying a filter.

Fetching messages

```
$message=\core\di::get(\core_sms\manager::class)
->get_message(['id'=>$id]);

$messages=\core\di::get(\core_sms\manager::class)
->get_messages(['recipientuserid'=>$userid]);
```

Sensitive content

If the message was sent with the `issensitive` flag the message body will not be stored.

## Checking the status of a message[​](#checking-the-status-of-a-message "Direct link to Checking the status of a message")

Once a message is sent, a status is recorded against it. This can be used to determine whether the message was sent successfully.

info

The level of status information available will depend on individual message gateways and recipient regions. In some regions delivery status may be available, but not in others.

Message status can be checked using the `\core_sms\message::$status` property.

Statuses are represented by a PHP Enum object with each status having a translatable description, and methods to determine whether the message was sent, is failed, or still in-progress.

Checking the status of a message

```
$message=\core\di::get(\core_sms\manager::class)
->get_message(['id'=>$id]);

// Check if the message is failed.
$message->is_failed();

// Check if the message is still in transit.
$message->is_in_progress();

// Check if the message is sent.
$message->is_sent();

// Get the description of the state.
$message->description();
```

## Getting SMS gateways[​](#getting-sms-gateways "Direct link to Getting SMS gateways")

[SMS gateways](https://moodledev.io/docs/4.5/apis/plugintypes/sms) are plugins that provide a way to interface with external SMS providers. Once a gateway is configured, any component implementing the SMS API can get a list of gateways.

Getting the list of enabled gateways

```
$manager=\core\di::get(\core_sms\manager::class);
$gatewayrecords=$manager->get_gateway_records();

// It is also possible to filter the request.
$gatewayrecords=$manager->get_gateway_records(['id'=>$id]);

// To get all the enabled gateway instances.
$gatewayrecords=$manager->get_enabled_gateway_instances();
```

## Important hooks[​](#important-hooks "Direct link to Important hooks")

The SMS API dispatches some [hooks](https://moodledev.io/docs/4.5/apis/core/hooks) which should be considered when implemented by a plugin/component.

- before\_gateway\_deleted
- before\_gateway\_disabled

Before deleting or disabling an [SMS gateways](https://moodledev.io/docs/4.5/apis/plugintypes/sms), these two hooks are dispatched from the SMS API. This allows components that are actively using that gateway to stop the action, or do necessary cleanup. Listening to these hooks is crucial to avoid data loss or accidental deletion when disabling an active gateway.

Implement the hooks to check for usage before deletion or deactivation

```

publicstaticfunctioncheck_gateway_usage_in_example_plugin(
before_gateway_deleted|before_gateway_disabled$hook,
):void{
try{
$smsgatewayid=(int)get_config('example_plugin','smsgateway');
if($smsgatewayid&&$smsgatewayid===(int)$hook->gateway->id){
$hook->stop_propagation();
}
}catch(\dml_exception$exception){
$hook->stop_propagation();
}
}

```