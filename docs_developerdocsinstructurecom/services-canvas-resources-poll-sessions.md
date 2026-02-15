---
title: Poll Sessions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/poll_sessions
source: sitemap
fetched_at: 2026-02-15T09:09:35.90391-03:00
rendered_js: false
word_count: 223
summary: This document defines the API endpoints and object structure for managing poll sessions, including methods for creating, updating, and querying session states and results within the Canvas LMS.
tags:
    - canvas-lms
    - api-documentation
    - poll-sessions
    - rest-api
    - polling-system
category: api
---

Manage poll sessions

**A PollSession object looks like:**

```
{
  // The unique identifier for the poll session.
"id": 1023,
  // The id of the Poll this poll session is associated with
"poll_id": 55,
  // The id of the Course this poll session is associated with
"course_id": 1111,
  // The id of the Course Section this poll session is associated with
"course_section_id": 444,
  // Specifies whether or not this poll session has been published for students to
  // participate in.
"is_published": true,
  // Specifies whether the results are viewable by students.
"has_public_results": true,
  // The time at which the poll session was created.
"created_at": "2014-01-07T15:16:18Z",
  // The results of the submissions of the poll. Each key is the poll choice id,
  // and the value is the count of submissions.
"results": {"144":10,"145":3,"146":27,"147":8},
  // If the poll session has public results, this will return an array of all
  // submissions, viewable by both students and teachers. If the results are not
  // public, for students it will return their submission only.
"poll_submissions": null
}
```

[Polling::PollSessionsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`GET /api/v1/polls/:poll_id/poll_sessions`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions`

Returns the paginated list of PollSessions in this poll.

**Example Response:**

```
{
  "poll_sessions": [PollSession]
}
```

[Polling::PollSessionsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`GET /api/v1/polls/:poll_id/poll_sessions/:id`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:id`

Returns the poll session with the given id

**Example Response:**

```
{
  "poll_sessions": [PollSession]
}
```

[Polling::PollSessionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`POST /api/v1/polls/:poll_id/poll_sessions`

**Scope:** `url:POST|/api/v1/polls/:poll_id/poll_sessions`

Create a new poll session for this poll

**Request Parameters:**

`poll_sessions[][course_id]`

The id of the course this session is associated with.

`poll_sessions[][course_section_id]`

The id of the course section this session is associated with.

`poll_sessions[][has_public_results]`

Whether or not results are viewable by students.

**Example Response:**

```
{
  "poll_sessions": [PollSession]
}
```

[Polling::PollSessionsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`PUT /api/v1/polls/:poll_id/poll_sessions/:id`

**Scope:** `url:PUT|/api/v1/polls/:poll_id/poll_sessions/:id`

Update an existing poll session for this poll

**Request Parameters:**

`poll_sessions[][course_id]`

The id of the course this session is associated with.

`poll_sessions[][course_section_id]`

The id of the course section this session is associated with.

`poll_sessions[][has_public_results]`

Whether or not results are viewable by students.

**Example Response:**

```
{
  "poll_sessions": [PollSession]
}
```

[Polling::PollSessionsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`DELETE /api/v1/polls/:poll_id/poll_sessions/:id`

**Scope:** `url:DELETE|/api/v1/polls/:poll_id/poll_sessions/:id`

**204 No Content** response code is returned if the deletion was successful.

[Polling::PollSessionsController#openarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`GET /api/v1/polls/:poll_id/poll_sessions/:id/open`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:id/open`

[Polling::PollSessionsController#closearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`GET /api/v1/polls/:poll_id/poll_sessions/:id/close`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:id/close`

[Polling::PollSessionsController#openedarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`GET /api/v1/poll_sessions/opened`

**Scope:** `url:GET|/api/v1/poll_sessions/opened`

A paginated list of all opened poll sessions available to the current user.

**Example Response:**

```
{
  "poll_sessions": [PollSession]
}
```

[Polling::PollSessionsController#closedarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_sessions_controller.rb)

`GET /api/v1/poll_sessions/closed`

**Scope:** `url:GET|/api/v1/poll_sessions/closed`

A paginated list of all closed poll sessions available to the current user.

**Example Response:**

```
{
  "poll_sessions": [PollSession]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago