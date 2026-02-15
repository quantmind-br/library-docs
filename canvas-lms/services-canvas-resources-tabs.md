---
title: Tabs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/tabs
source: sitemap
fetched_at: 2026-02-15T09:08:15.97484-03:00
rendered_js: false
word_count: 158
summary: This document defines the API endpoints and data structure for managing navigation tabs within contexts like accounts, courses, groups, and users. It outlines how to retrieve lists of tabs and modify their visibility or display order.
tags:
    - canvas-lms
    - tabs-api
    - navigation-tabs
    - rest-api
    - endpoint-reference
    - course-management
category: api
---

**A Tab object looks like:**

```
{
"html_url": "/courses/1/external_tools/4",
"id": "context_external_tool_4",
"label": "WordPress",
"type": "external",
  // only included if true
"hidden": true,
  // possible values are: public, members, admins, and none
"visibility": "public",
  // 1 based
"position": 2
}
```

[TabsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tabs_controller.rb)

`GET /api/v1/accounts/:account_id/tabs`

**Scope:** `url:GET|/api/v1/accounts/:account_id/tabs`

`GET /api/v1/courses/:course_id/tabs`

**Scope:** `url:GET|/api/v1/courses/:course_id/tabs`

`GET /api/v1/groups/:group_id/tabs`

**Scope:** `url:GET|/api/v1/groups/:group_id/tabs`

`GET /api/v1/users/:user_id/tabs`

**Scope:** `url:GET|/api/v1/users/:user_id/tabs`

Returns a paginated list of navigation tabs available in the current context.

**Request Parameters:**

- “course\_subject\_tabs”: Optional flag to return the tabs associated with a canvas\_for\_elementary subject course’s home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context in a canvas\_for\_elementary-enabled account or sub-account.

Allowed values: `course_subject_tabs`

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/groups/<group_id>/tabs"
```

**Example Response:**

```
[
{
"html_url":"/courses/1",
"id":"home",
"label":"Home",
"position":1,
"visibility":"public",
"type":"internal"
},
{
"html_url":"/courses/1/external_tools/4",
"id":"context_external_tool_4",
"label":"WordPress",
"hidden":true,
"visibility":"public",
"position":2,
"type":"external"
},
{
"html_url":"/courses/1/grades",
"id":"grades",
"label":"Grades",
"position":3,
"hidden":true
"visibility": "admins"
"type": "internal"
}
]
```

[TabsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tabs_controller.rb)

`PUT /api/v1/courses/:course_id/tabs/:tab_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/tabs/:tab_id`

Home and Settings tabs are not manageable, and can’t be hidden or moved

Returns a tab object

**Request Parameters:**

The new position of the tab, 1-based

**Example Request:**

```
curlhttps://<canvas>/api/v1/courses/<course_id>/tabs/tab_id\
-XPUT\
-H'Authorization: Bearer <token>'\
-d'hidden=true'\
-d'position=2'//1based
```

Returns a [Tab](https://developerdocs.instructure.com/services/canvas/resources/tabs#tab) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).