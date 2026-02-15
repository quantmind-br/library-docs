---
title: Polls | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/polls
source: sitemap
fetched_at: 2026-02-15T09:09:19.845787-03:00
rendered_js: false
word_count: 146
summary: This document defines the data structure and REST API endpoints for creating, retrieving, updating, and deleting poll objects within Canvas LMS.
tags:
    - canvas-lms
    - polling-api
    - rest-api
    - poll-management
    - api-endpoints
category: api
---

Manage polls

**A Poll object looks like:**

```
{
  // The unique identifier for the poll.
"id": 1023,
  // The question/title of the poll.
"question": "What do you consider most important to your learning in this course?",
  // A short description of the poll.
"description": "This poll is to determine what priorities the students in the course have.",
  // The time at which the poll was created.
"created_at": "2014-01-07T15:16:18Z",
  // The unique identifier for the user that created the poll.
"user_id": 105,
  // An aggregate of the results of all associated poll sessions, with the poll
  // choice id as the key, and the aggregated submission count as the value.
"total_results": {"543":20,"544":5,"545":17}
}
```

[Polling::PollsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

`GET /api/v1/polls`

**Scope:** `url:GET|/api/v1/polls`

Returns the paginated list of polls for the current user.

**Example Response:**

[Polling::PollsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

`GET /api/v1/polls/:id`

**Scope:** `url:GET|/api/v1/polls/:id`

Returns the poll with the given id

**Example Response:**

[Polling::PollsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

`POST /api/v1/polls`

**Scope:** `url:POST|/api/v1/polls`

Create a new poll for the current user

**Request Parameters:**

A brief description or instructions for the poll.

**Example Response:**

[Polling::PollsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

`PUT /api/v1/polls/:id`

**Scope:** `url:PUT|/api/v1/polls/:id`

Update an existing poll belonging to the current user

**Request Parameters:**

A brief description or instructions for the poll.

**Example Response:**

[Polling::PollsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/polls_controller.rb)

`DELETE /api/v1/polls/:id`

**Scope:** `url:DELETE|/api/v1/polls/:id`

**204 No Content** response code is returned if the deletion was successful.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).