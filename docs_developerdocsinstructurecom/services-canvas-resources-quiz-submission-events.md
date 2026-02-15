---
title: Quiz Submission Events | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_events
source: sitemap
fetched_at: 2026-02-15T09:08:50.523586-03:00
rendered_js: false
word_count: 128
summary: This document provides an API reference for recording and retrieving events captured during a quiz session, such as answering questions or flagging items.
tags:
    - canvas-lms
    - quiz-submission-events
    - api-reference
    - event-tracking
    - quiz-auditing
    - rest-api
category: api
---

## Quiz Submission Events API

**A QuizSubmissionEvent object looks like:**

```
// An event passed from the Quiz Submission take page
{
  // a timestamp record of creation time
"created_at": "2014-10-08T19:29:58Z",
  // the type of event being sent
"event_type": "question_answered",
  // custom contextual data for the specific event type
"event_data": {"answer":"42"}
}
```

[Quizzes::QuizSubmissionEventsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_events_api_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

Store a set of events which were captured during a quiz taking session.

On success, the response will be 204 No Content with an empty body.

**Request Parameters:**

The submission events to be recorded

**Example Request:**

```
{
  "quiz_submission_events":
  [
    {
      "client_timestamp": "2014-10-08T19:29:58Z",
      "event_type": "question_answered",
      "event_data" : {"answer": "42"}
    }, {
      "client_timestamp": "2014-10-08T19:30:17Z",
      "event_type": "question_flagged",
      "event_data" : { "question_id": "1", "flagged": true }
    }
  ]
}
```

[Quizzes::QuizSubmissionEventsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_events_api_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/events`

Retrieve the set of events captured during a specific submission attempt.

**Request Parameters:**

The specific submission attempt to look up the events for. If unspecified, the latest attempt will be used.

**Example Response:**

```
{
  "quiz_submission_events": [
    {
      "id": "3409",
      "event_type": "page_blurred",
      "event_data": null,
      "created_at": "2014-11-16T13:37:21Z"
    },
    {
      "id": "3410",
      "event_type": "page_focused",
      "event_data": null,
      "created_at": "2014-11-16T13:37:27Z"
    }
  ]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).