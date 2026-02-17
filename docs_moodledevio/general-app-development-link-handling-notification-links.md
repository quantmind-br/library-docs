---
title: Moodle App Notification Links | Moodle Developer Resources
url: https://moodledev.io/general/app/development/link-handling/notification-links
source: sitemap
fetched_at: 2026-02-17T15:54:34.397627-03:00
rendered_js: false
word_count: 100
summary: This document explains how to customize the destination URL and link handling behavior when a user clicks on a push notification in the mobile app.
tags:
    - push-notifications
    - deep-linking
    - mobile-app
    - link-handling
    - custom-data
    - site-plugins
category: guide
---

Push notifications will open the app when clicked, and you can customize which page is open by default.

The easiest way to achieve it is to include a `contexturl` property in your notification. Notice that using this property, the url will also be displayed when you see the notification in the web. You can override this behaviour in the app using `appurl` within `customdata`:

```
$notification->customdata=[
'appurl'=>$myurl->out(),
];
```

The url will be handled using the default [link handling](https://moodledev.io/general/app/development/link-handling/app-links) in the app. If you want to implement some custom behaviour when opening notifications, you can achieve it with a Site Plugin implementing a [CorePushNotificationsDelegate](https://moodledev.io/general/app/development/plugins-development-guide/api-reference#corepushnotificationsdelegate) handler.