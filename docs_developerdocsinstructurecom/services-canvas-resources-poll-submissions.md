---
title: PollSubmissions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/poll_submissions
source: sitemap
fetched_at: 2026-02-15T09:09:23.375471-03:00
rendered_js: false
word_count: 90
summary: This document outlines the API endpoints and data structure for managing poll submissions, including retrieving specific submission details and creating new entries for a poll session.
tags:
    - canvas-lms
    - poll-submissions
    - rest-api
    - polling
    - api-documentation
category: api
---

Manage submissions for polls

**A PollSubmission object looks like:**

```
{
  // The unique identifier for the poll submission.
"id": 1023,
  // The unique identifier of the poll choice chosen for this submission.
"poll_choice_id": 155,
  // the unique identifier of the user who submitted this poll submission.
"user_id": 4555,
  // The date and time the poll submission was submitted.
"created_at": "2013-11-07T13:16:18Z"
}
```

[Polling::PollSubmissionsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_submissions_controller.rb)

`GET /api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions/:id`

**Scope:** `url:GET|/api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions/:id`

Returns the poll submission with the given id

**Example Response:**

```
{
  "poll_submissions": [PollSubmission]
}
```

[Polling::PollSubmissionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/polling/poll_submissions_controller.rb)

`POST /api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions`

**Scope:** `url:POST|/api/v1/polls/:poll_id/poll_sessions/:poll_session_id/poll_submissions`

Create a new poll submission for this poll session

**Request Parameters:**

`poll_submissions[][poll_choice_id]`

The chosen poll choice for this submission.

**Example Response:**

```
{
  "poll_submissions": [PollSubmission]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).