---
title: Sending custom Push Notifications to the Moodle App | Moodle Developer Resources
url: https://moodledev.io/general/app/development/custom-push-notifications
source: sitemap
fetched_at: 2026-02-17T15:54:26.578911-03:00
rendered_js: false
word_count: 578
summary: This document explains the two primary methods for sending custom push notifications to Moodle app users via the Moodle Message API or the Airnotifier API. It outlines the differences between these methods and provides technical details on payload structures and implementation requirements.
tags:
    - moodle-app
    - push-notifications
    - message-api
    - airnotifier
    - api-integration
    - mobile-notifications
category: guide
---

There are two ways to send custom Push Notifications to the Moodle app users:

1. By using Moodle's Message API implementing a message provider
2. By directly using the Airnotifier (Moodle's Push Notification server) APIs

**The main differences are:**

By using Moodle's Message API, users (students, teachers, etc..) can opt-out to not receive custom notifications. They can also opt-in to receive them not only on the app but also via email. Messages sent using this API can be delivered to non-app users.

Using the Airnotifier API will force the user to receive the notification unless they change their app settings to not receive any notification. Messages sent using this API will only get to active app users.

In both cases, please remember that the number of user devices that can receive Push Notifications is dictated by your app [subscription](https://moodle.com/app/).

## Moodle's Message API[​](#moodles-message-api "Direct link to Moodle's Message API")

Please read the official Moodle documentation, [Message API](https://moodledev.io/docs/5.2/apis/core/message), where it is explained how to create a new message provider within a plugin.

Apart from what is explained in the [Message API](https://moodledev.io/docs/5.2/apis/core/message) please notice that it is possible to add a "customdata" field (json-encoded) with additional parameters. Those parameters are the ones described in the Airnotifier API section below.

## Airnotifier API[​](#airnotifier-api "Direct link to Airnotifier API")

Airnotifier is the name of the Push Notification server used by Moodle. It is possible to use its own API to send custom notifications from Moodle without having to use Moodle's Message API.

### Payload format[​](#payload-format "Direct link to Payload format")

**Mandatory fields:**

- `processor` (string): Always set to Moodle
- `notification` (number): Whether it is a notification (1) or a message (0).
- `subject` (string): Notification title.
- `smallmessage` (string): Notification body, short text.
- `fullmessage` (string): Notification body, ignored if smallmessage is set.

**Optional fields:**

- `site` (string): Site ID (md5 hash of site URL + username)
- `siteurl` (string): Site URL (used to identify the site the notification is coming from)
- `wwwroot` (string): Moodle's $CFG-&gt;wwwroot
- `component` (string): Moodle's component that generated the notification
- `contexturl` (string): URL the notification is related to
- `customdata` (JSON encoded object, all fields are optional)
  
  - `notificationiconurl` (string): Icon to display in the notification (Android only).
  - `notificationpictureurl` (string). Large picture to display in the notification (Android only).
  - `tokenpluginfile` (string): Token to view the icon if needed.
  - `extendedtext` (string). An extended text (HTML), opened in popup when clicked.
  - `appurl` (string): When notification is clicked, open this URL. It has preference over `contexturl` but it will be ignored if `extendedtext` is set.
  - `appurlopenin` (string): Where to open the previous URL `browser`, `in-app` or any other value.

### Sample CURL requests[​](#sample-curl-requests "Direct link to Sample CURL requests")

Simple notification, only subject and body:

```
 curl AIRNOTIFIER_URL/api/v2/push -X POST -H "X-AN-APP-NAME: APP_ID" -H "X-AN-APP-KEY: AIRNOTIFIER_ACCESS_KEY" --data '{"device": "android-fcm", "token": "DEVICE_TOKEN",  "extra": {"processor" : "moodle", "notification": 1, "subject": "Title test", "fullmessage": "Message test"}}'
```

Notification including an icon and picture (only displayed on Android devices) opening a popup with custom content on the app:

```
curl AIRNOTIFIER_URL/api/v2/push -X POST -H "X-AN-APP-NAME: APP_ID" -H "X-AN-APP-KEY: AIRNOTIFIER_ACCESS_KEY" --data '{"device": "android-fcm", "token": "DEVICE_TOKEN", "extra": {"processor" : "moodle", "notification": 1, "subject": "Title test", "fullmessage": "Message test", "customdata": "{\\"extendedtext\\" : \\"Extended tex that will open in a popupt\\", \\"notificationiconurl\\" : \\"<https://picsum.photos/50\\">, \\"notificationpictureurl\\" : \\"<https://picsum.photos/200\\"}"}}'>
```

Notification opening URL that can be handled by the app (a course within the app):

```
 curl AIRNOTIFIER_URL/api/v2/push -X POST -H "X-AN-APP-NAME: APP_ID" -H "X-AN-APP-KEY: AIRNOTIFIER_ACCESS_KEY" --data '{"device": "android-fcm", "token": "DEVICE_TOKEN", "extra": {"processor" : "moodle", "notification": 1, "subject": "Title test", "fullmessage": "Message test", "customdata": "{ \\"appurl\\" : \\"<https://mymoodlesite.net/course/view.php?id=18\\">, \\"notificationiconurl\\" : \\"<https://picsum.photos/50\\">, \\"notificationpictureurl\\" : \\"<https://picsum.photos/200\\"}"}}'>
```

**Replace the following fields:**

- AIRNOTIFIER\_URL: Can be obtained from your Moodle site settings: Site administration &gt; Messaging &gt; Mobile.
- APP\_ID: `commoodlemoodlemobile` for the standard Moodle app, it can also be obtained from Site administration &gt; Messaging &gt; Mobile.
- AIRNOTIFIER\_ACCESS\_KEY: Your Airnotifier Access key can be obtained from Site administration &gt; Messaging &gt; Mobile.
- DEVICE\_TOKEN: The user's receiving the notification device token, for testing purposes you can get it via the app &gt; App settings &gt; About &gt; Click at app version on the footer &gt; Push notification ID.

In Moodle the push ids are in the user\_devices table (`pushid` field), the previous table has to be joined with message\_airnotifier\_devices to obtain active devices.

The device could be android-fcm or ios-fcm (in the example we used android-fcm only).