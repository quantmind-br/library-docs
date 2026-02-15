---
title: Account Calendars | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/account_calendars
source: sitemap
fetched_at: 2026-02-15T09:05:26.256964-03:00
rendered_js: false
word_count: 455
summary: Provides documentation for the Canvas LMS Account Calendars API, detailing endpoints for listing, retrieving, and updating the visibility and subscription settings of account calendars.
tags:
    - canvas-lms
    - account-calendars
    - api-documentation
    - calendar-management
    - visibility-toggling
    - bulk-operations
category: api
---

API for viewing and toggling settings of account calendars.

An account calendar is available for each account in Canvas. All account calendars are hidden by default, but administrators with the `manage_account_calendar_visibility` permission may set calendars as visible. Administrators with the `manage_account_calendar_events` permission can create events in visible account calendars, and users associated with an account can add the calendar and see its events (if the calendar is visible). Events on calendars set as `auto_subscribe` calendars will appear on users' calendars even if they do not manually add it.

**An AccountCalendar object looks like:**

```
{
  // the ID of the account associated with this calendar
"id": 204,
  // the name of the account associated with this calendar
"name": "Department of Chemistry",
  // the account's parent ID, or null if this is the root account
"parent_account_id": 1,
  // the ID of the root account, or null if this is the root account
"root_account_id": 1,
  // whether this calendar is visible to users
"visible": true,
  // whether users see this calendar's events without needing to manually add it
"auto_subscribe": false,
  // number of this account's direct sub-accounts
"sub_account_count": 0,
  // Asset string of the account
"asset_string": "account_4",
  // Object type
"type": "account",
  // url to get full detailed events
"calendar_event_url": "/accounts/2/calendar_events/%7B%7B%20id%20%7D%7D",
  // whether the user can create calendar events
"can_create_calendar_events": true,
  // API path to create events for the account
"create_calendar_event_url": "/accounts/2/calendar_events",
  // url to open the more options event editor
"new_calendar_event_url": "/accounts/6/calendar_events/new"
}
```

[AccountCalendarsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_calendars_api_controller.rb)

`GET /api/v1/account_calendars`

**Scope:** `url:GET|/api/v1/account_calendars`

Returns a paginated list of account calendars available to the current user. Includes visible account calendars where the user has an account association.

**Request Parameters:**

When included, searches available account calendars for the term. Returns matching results. Term must be at least 2 characters.

**Example Request:**

```
curl https://<canvas>/api/v1/account_calendars \
  -H 'Authorization: Bearer <token>'
```

Returns a list of [AccountCalendar](https://developerdocs.instructure.com/services/canvas/resources/account_calendars#accountcalendar) objects.

[AccountCalendarsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_calendars_api_controller.rb)

`GET /api/v1/account_calendars/:account_id`

**Scope:** `url:GET|/api/v1/account_calendars/:account_id`

Get details about a specific account calendar.

**Example Request:**

```
curl https://<canvas>/api/v1/account_calendars/204 \
  -H 'Authorization: Bearer <token>'
```

Returns an [AccountCalendar](https://developerdocs.instructure.com/services/canvas/resources/account_calendars#accountcalendar) object.

[AccountCalendarsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_calendars_api_controller.rb)

`PUT /api/v1/account_calendars/:account_id`

**Scope:** `url:PUT|/api/v1/account_calendars/:account_id`

Set an account calendar’s visibility and auto\_subscribe values. Requires the ‘manage\_account\_calendar\_visibility\` permission on the account.

**Request Parameters:**

Allow administrators with ‘manage\_account\_calendar\_events\` permission to create events on this calendar, and allow users to view this calendar and its events.

When true, users will automatically see events from this account in their calendar, even if they haven’t manually added that calendar.

**Example Request:**

```
curl https://<canvas>/api/v1/account_calendars/204 \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'visible=false' \
  -d 'auto_subscribe=false'
```

Returns an [AccountCalendar](https://developerdocs.instructure.com/services/canvas/resources/account_calendars#accountcalendar) object.

[AccountCalendarsApiController#bulk\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_calendars_api_controller.rb)

`PUT /api/v1/accounts/:account_id/account_calendars`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/account_calendars`

Set visibility and/or auto\_subscribe on many calendars simultaneously. Requires the ‘manage\_account\_calendar\_visibility\` permission on the account.

Accepts a JSON array of objects containing 2-3 keys each: ‘id\` (the account’s id, required), ‘visible\` (a boolean indicating whether the account calendar is visible), and \`auto\_subscribe\` (a boolean indicating whether users should see these events in their calendar without manually subscribing).

Returns the count of updated accounts.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/1/account_calendars \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  --data '[{"id": 1, "visible": true, "auto_subscribe": false}, {"id": 13, "visible": false, "auto_subscribe": true}]'
```

[AccountCalendarsApiController#all\_calendarsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_calendars_api_controller.rb)

`GET /api/v1/accounts/:account_id/account_calendars`

**Scope:** `url:GET|/api/v1/accounts/:account_id/account_calendars`

Returns a paginated list of account calendars for the provided account and its first level of sub-accounts. Includes hidden calendars in the response. Requires the ‘manage\_account\_calendar\_visibility\` permission.

**Request Parameters:**

When included, searches all descendent accounts of provided account for the term. Returns matching results. Term must be at least 2 characters. Can be combined with a filter value.

When included, only returns calendars that are either visible or hidden. Can be combined with a search term.

Allowed values: `visible`, `hidden`

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/1/account_calendars \
  -H 'Authorization: Bearer <token>'
```

Returns a list of [AccountCalendar](https://developerdocs.instructure.com/services/canvas/resources/account_calendars#accountcalendar) objects.

[AccountCalendarsApiController#visible\_calendars\_countarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_calendars_api_controller.rb)

`GET /api/v1/accounts/:account_id/visible_calendars_count`

**Scope:** `url:GET|/api/v1/accounts/:account_id/visible_calendars_count`

Returns the number of visible account calendars.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/1/visible_calendars_count \
  -H 'Authorization: Bearer <token>'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).