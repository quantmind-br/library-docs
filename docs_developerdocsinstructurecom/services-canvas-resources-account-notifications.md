---
title: Account Notifications | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/account_notifications
source: sitemap
fetched_at: 2026-02-15T09:05:47.129053-03:00
rendered_js: false
word_count: 445
summary: This document provides the REST API specification for managing account-level notifications and global announcements, including endpoints for creating, retrieving, updating, and dismissing notifications.
tags:
    - canvas-lms
    - account-notifications
    - api-endpoints
    - global-announcements
    - rest-api
    - notification-management
category: api
---

## Account Notifications API

API for account notifications.

**An AccountNotification object looks like:**

```
{
  // The subject of the notifications
"subject": "Attention Students",
  // The message to be sent in the notification.
"message": "This is a test of the notification system.",
  // When to send out the notification.
"start_at": "2013-08-28T23:59:00-06:00",
  // When to expire the notification.
"end_at": "2013-08-29T23:59:00-06:00",
  // The icon to display with the message.  Defaults to warning.
"icon": "information",
  // (Deprecated) The roles to send the notification to.  If roles is not passed
  // it defaults to all roles
"roles": ["StudentEnrollment"],
  // The roles to send the notification to.  If roles is not passed it defaults to
  // all roles
"role_ids": [1],
  // The author of the notification. Available only to admins using include_all.
"author": {"id":1,"name":"John Doe"}
}
```

[AccountNotificationsController#user\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_notifications_controller.rb)

`GET /api/v1/accounts/:account_id/account_notifications`

**Scope:** `url:GET|/api/v1/accounts/:account_id/account_notifications`

Returns a list of all global notifications in the account for the current user Any notifications that have been closed by the user will not be returned, unless a include\_past parameter is passed in as true. Admins can request all global notifications for the account by passing in an include\_all parameter.

**Request Parameters:**

Include past and dismissed global announcements.

Include all global announcements, regardless of user’s role or availability date. Only available to account admins.

Include a flag for each notification indicating whether it has been read by the user.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/2/users/self/account_notifications
```

Returns a list of [AccountNotification](https://developerdocs.instructure.com/services/canvas/resources/account_notifications#accountnotification) objects.

[AccountNotificationsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_notifications_controller.rb)

`GET /api/v1/accounts/:account_id/account_notifications/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/account_notifications/:id`

Returns a global notification for the current user A notification that has been closed by the user will not be returned

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/2/users/self/account_notifications/4
```

Returns an [AccountNotification](https://developerdocs.instructure.com/services/canvas/resources/account_notifications#accountnotification) object.

[AccountNotificationsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_notifications_controller.rb)

`POST /api/v1/accounts/:account_id/account_notifications`

**Scope:** `url:POST|/api/v1/accounts/:account_id/account_notifications`

Create and return a new global notification for an account.

**Request Parameters:**

`account_notification[subject]`

The subject of the notification.

`account_notification[message]`

The message body of the notification.

`account_notification[start_at]`

The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z

`account_notification[end_at]`

The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z

`account_notification[icon]`

The icon to display with the notification. Note: Defaults to warning.

Allowed values: `warning`, `information`, `question`, `error`, `calendar`

`account_notification_roles[]`

The role(s) to send global notification to. Note: ommitting this field will send to everyone Example:

```
account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"]
```

**Example Request:**

```
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/2/account_notifications \
-d 'account_notification[subject]=New notification' \
-d 'account_notification[start_at]=2014-01-01T00:00:00Z' \
-d 'account_notification[end_at]=2014-02-01T00:00:00Z' \
-d 'account_notification[message]=This is a global notification'
```

**Example Response:**

```
{
  "subject": "New notification",
  "start_at": "2014-01-01T00:00:00Z",
  "end_at": "2014-02-01T00:00:00Z",
  "message": "This is a global notification"
}
```

[AccountNotificationsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_notifications_controller.rb)

`PUT /api/v1/accounts/:account_id/account_notifications/:id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/account_notifications/:id`

Update global notification for an account.

**Request Parameters:**

`account_notification[subject]`

The subject of the notification.

`account_notification[message]`

The message body of the notification.

`account_notification[start_at]`

The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z

`account_notification[end_at]`

The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z

`account_notification[icon]`

The icon to display with the notification.

Allowed values: `warning`, `information`, `question`, `error`, `calendar`

`account_notification_roles[]`

The role(s) to send global notification to. Note: ommitting this field will send to everyone Example:

```
account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"]
```

**Example Request:**

```
curl -X PUT -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/2/account_notifications/1 \
-d 'account_notification[subject]=New notification' \
-d 'account_notification[start_at]=2014-01-01T00:00:00Z' \
-d 'account_notification[end_at]=2014-02-01T00:00:00Z' \
-d 'account_notification[message]=This is a global notification'
```

**Example Response:**

```
{
  "subject": "New notification",
  "start_at": "2014-01-01T00:00:00Z",
  "end_at": "2014-02-01T00:00:00Z",
  "message": "This is a global notification"
}
```

[AccountNotificationsController#user\_close\_notificationarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_notifications_controller.rb)

`DELETE /api/v1/accounts/:account_id/account_notifications/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/account_notifications/:id`

If the current user no longer wants to see this account notification, it can be closed with this call. This affects the current user only.

If the current user is an admin and they pass a remove parameter with a value of “true”, the account notification will be destroyed. This affects all users.

**Request Parameters:**

Destroy the account notification.

**Example Request:**

```
curl -X DELETE -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/accounts/2/account_notifications/4
```

Returns an [AccountNotification](https://developerdocs.instructure.com/services/canvas/resources/account_notifications#accountnotification) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).