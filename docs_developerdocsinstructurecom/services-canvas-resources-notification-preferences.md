---
title: Notification Preferences | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/notification_preferences
source: sitemap
fetched_at: 2026-02-15T09:09:51.208562-03:00
rendered_js: false
word_count: 225
summary: This document outlines the API endpoints for managing notification preferences, allowing users to view and update how frequently they receive notifications across various communication channels.
tags:
    - canvas-lms
    - notification-api
    - user-preferences
    - communication-channels
    - api-endpoints
category: api
---

## Notification Preferences API

API for managing notification preferences

**A NotificationPreference object looks like:**

```
{
"href": "https://canvas.instructure.com/users/1/communication_channels/email/student@example.edu/notification_preferences/new_announcement",
  // The notification this preference belongs to
"notification": "new_announcement",
  // The category of that notification
"category": "announcement",
  // How often to send notifications to this communication channel for the given
  // notification. Possible values are 'immediately', 'daily', 'weekly', and
  // 'never'
"frequency": "daily"
}
```

[NotificationPreferencesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/notification_preferences_controller.rb)

`GET /api/v1/users/:user_id/communication_channels/:communication_channel_id/notification_preferences`

**Scope:** `url:GET|/api/v1/users/:user_id/communication_channels/:communication_channel_id/notification_preferences`

`GET /api/v1/users/:user_id/communication_channels/:type/:address/notification_preferences`

**Scope:** `url:GET|/api/v1/users/:user_id/communication_channels/:type/:address/notification_preferences`

Fetch all preferences for the given communication channel

Returns a list of [NotificationPreference](https://developerdocs.instructure.com/services/canvas/resources/notification_preferences#notificationpreference) objects.

[NotificationPreferencesController#category\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/notification_preferences_controller.rb)

`GET /api/v1/users/:user_id/communication_channels/:communication_channel_id/notification_preference_categories`

**Scope:** `url:GET|/api/v1/users/:user_id/communication_channels/:communication_channel_id/notification_preference_categories`

Fetch all notification preference categories for the given communication channel

[NotificationPreferencesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/notification_preferences_controller.rb)

`GET /api/v1/users/:user_id/communication_channels/:communication_channel_id/notification_preferences/:notification`

**Scope:** `url:GET|/api/v1/users/:user_id/communication_channels/:communication_channel_id/notification_preferences/:notification`

`GET /api/v1/users/:user_id/communication_channels/:type/:address/notification_preferences/:notification`

**Scope:** `url:GET|/api/v1/users/:user_id/communication_channels/:type/:address/notification_preferences/:notification`

Fetch the preference for the given notification for the given communication channel

Returns a [NotificationPreference](https://developerdocs.instructure.com/services/canvas/resources/notification_preferences#notificationpreference) object.

[NotificationPreferencesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/notification_preferences_controller.rb)

`PUT /api/v1/users/self/communication_channels/:communication_channel_id/notification_preferences/:notification`

**Scope:** `url:PUT|/api/v1/users/self/communication_channels/:communication_channel_id/notification_preferences/:notification`

`PUT /api/v1/users/self/communication_channels/:type/:address/notification_preferences/:notification`

**Scope:** `url:PUT|/api/v1/users/self/communication_channels/:type/:address/notification_preferences/:notification`

Change the preference for a single notification for a single communication channel

**Request Parameters:**

`notification_preferences[frequency]`

The desired frequency for this notification

[NotificationPreferencesController#update\_preferences\_by\_categoryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/notification_preferences_controller.rb)

`PUT /api/v1/users/self/communication_channels/:communication_channel_id/notification_preference_categories/:category`

**Scope:** `url:PUT|/api/v1/users/self/communication_channels/:communication_channel_id/notification_preference_categories/:category`

Change the preferences for multiple notifications based on the category for a single communication channel

**Request Parameters:**

The name of the category. Must be parameterized (e.g. The category “Course Content” should be “course\_content”)

`notification_preferences[frequency]`

The desired frequency for each notification in the category

[NotificationPreferencesController#update\_allarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/notification_preferences_controller.rb)

`PUT /api/v1/users/self/communication_channels/:communication_channel_id/notification_preferences`

**Scope:** `url:PUT|/api/v1/users/self/communication_channels/:communication_channel_id/notification_preferences`

`PUT /api/v1/users/self/communication_channels/:type/:address/notification_preferences`

**Scope:** `url:PUT|/api/v1/users/self/communication_channels/:type/:address/notification_preferences`

Change the preferences for multiple notifications for a single communication channel at once

**Request Parameters:**

`notification_preferences[<X>][frequency]`

The desired frequency for &lt;X&gt; notification

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).