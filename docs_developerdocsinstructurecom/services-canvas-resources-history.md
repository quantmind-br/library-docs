---
title: History | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/history
source: sitemap
fetched_at: 2026-02-15T09:07:55.283934-03:00
rendered_js: false
word_count: 121
summary: This document defines the HistoryEntry object structure and describes the API endpoint for retrieving a paginated list of a user's recent activity in Canvas LMS.
tags:
    - canvas-lms
    - user-history
    - api-endpoint
    - history-entry
    - resource-schema
category: api
---

**A HistoryEntry object looks like:**

```
// Information about a recently visited item or page in Canvas
{
  // The asset string for the item viewed
"asset_code": "assignment_123",
  // The name of the item
"asset_name": "Test Assignment",
  // The icon type shown for the item. One of 'icon-announcement',
  // 'icon-assignment', 'icon-calendar-month', 'icon-discussion', 'icon-document',
  // 'icon-download', 'icon-gradebook', 'icon-home', 'icon-message',
  // 'icon-module', 'icon-outcomes', 'icon-quiz', 'icon-user', 'icon-syllabus'
"asset_icon": "icon-assignment",
  // The associated category describing the asset_icon
"asset_readable_category": "Assignment",
  // The type of context of the item visited. One of 'Course', 'Group', 'User', or
  // 'Account'
"context_type": "Course",
  // The id of the context, if applicable
"context_id": 123,
  // The name of the context
"context_name": "Something 101",
  // The URL of the item
"visited_url": "https://canvas.example.com/courses/123/assignments/456",
  // When the page was visited
"visited_at": "2019-08-01T19:49:47Z",
  // The estimated time spent on the page in seconds
"interaction_seconds": 400
}
```

[HistoryController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/history_controller.rb)

`GET /api/v1/users/:user_id/history`

**Scope:** `url:GET|/api/v1/users/:user_id/history`

Return a paginated list of the user’s recent history. History entries are returned in descending order, newest to oldest. You may list history entries for yourself (use `self` as the user\_id), for a student you observe, or for a user you manage as an administrator. Note that the `per_page` pagination argument is not supported and the number of history entries returned per page will vary.

Returns a list of [HistoryEntry](https://developerdocs.instructure.com/services/canvas/resources/history#historyentry) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).