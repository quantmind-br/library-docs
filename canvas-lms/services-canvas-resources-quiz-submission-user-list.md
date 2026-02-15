---
title: Quiz Submission User List | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_user_list
source: sitemap
fetched_at: 2026-02-15T09:08:42.710095-03:00
rendered_js: false
word_count: 88
summary: This document defines the API structures and endpoints for retrieving quiz submission users and sending targeted messages based on submission status.
tags:
    - canvas-lms
    - api-reference
    - quiz-submissions
    - pagination
    - user-management
    - messaging
category: api
---

## Quiz Submission User List API

List of users who have or haven't submitted for a quiz.

**A QuizSubmissionUserList object looks like:**

```
{
"meta": {
"$ref":"QuizSubmissionUserListMeta",
"description":"contains meta information (such as pagination) for the list of users"
},
"users": {
"$ref":"User",
"description":"list of users that match the query"
}
}
```

**A QuizSubmissionUserListMeta object looks like:**

```
{
"pagination": {
"$ref":"JSONAPIPagination",
"description":"contains pagination information for the list of users"
}
}
```

**A JSONAPIPagination object looks like:**

```
{
  "per_page": {
    "type": "integer",
    "description": "number of results per page",
    "example": 10
  },
  "page": {
    "type": "integer",
    "description": "the current page passed as the ?page= parameter",
    "example": 1
  },
  "template": {
    "type": "string",
    "description": "URL template for building out other paged URLs for this endpoint",
    "example": "https://example.instructure.com/api/v1/courses/1/quizzes/1/submission_users?page={page}"
  },
  "page_count": {
    "type": "integer",
    "description": "number of pages for this collection",
    "example": 10
  },
  "count": {
    "type": "integer",
    "description": "total number of items in this collection",
    "example": 100
  }
}
```

[Quizzes::QuizSubmissionUsersController#messagearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_users_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:id/submission_users/message`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:id/submission_users/message`

{

```
"body": {
  "type": "string",
  "description": "message body of the conversation to be created",
  "example": "Please take the quiz."
},
"recipients": {
  "type": "string",
  "description": "Who to send the message to. May be either 'submitted' or 'unsubmitted'",
  "example": "submitted"
},
"subject": {
  "type": "string",
  "description": "Subject of the new Conversation created",
  "example": "ATTN: Quiz 101 Students"
}
```

}

**Request Parameters:**

- Body and recipients to send the message to.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).