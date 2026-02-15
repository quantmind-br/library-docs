---
title: Quiz Extensions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_extensions
source: sitemap
fetched_at: 2026-02-15T09:09:11.959895-03:00
rendered_js: false
word_count: 223
summary: This document defines the API endpoint and parameters required to grant quiz extensions to students, allowing for extra time, additional attempts, or manual unlocking of assessments.
tags:
    - canvas-lms
    - quiz-extensions
    - api-documentation
    - rest-api
    - educational-software
category: api
---

API for setting extensions on student quiz submissions

**A QuizExtension object looks like:**

```
{
  // The ID of the Quiz the quiz extension belongs to.
"quiz_id": 2,
  // The ID of the Student that needs the quiz extension.
"user_id": 3,
  // Number of times the student is allowed to re-take the quiz over the
  // multiple-attempt limit.
"extra_attempts": 1,
  // Amount of extra time allowed for the quiz submission, in minutes.
"extra_time": 60,
  // The student can take the quiz even if it's locked for everyone else
"manually_unlocked": true,
  // The time at which the quiz submission will be overdue, and be flagged as a
  // late submission.
"end_at": "2013-11-07T13:16:18Z"
}
```

[Quizzes::QuizExtensionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_extensions_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/extensions`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/extensions`

**Responses**

- **200 OK** if the request was successful
- **403 Forbidden** if you are not allowed to extend quizzes for this course

**Request Parameters:**

`quiz_extensions[][user_id]`

The ID of the user we want to add quiz extensions for.

`quiz_extensions[][extra_attempts]`

Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. This is limited to 1000 attempts or less.

`quiz_extensions[][extra_time]`

The number of extra minutes to allow for all attempts. This will add to the existing time limit on the submission. This is limited to 10080 minutes (1 week)

`quiz_extensions[][manually_unlocked]`

Allow the student to take the quiz even if it’s locked for everyone else.

`quiz_extensions[][extend_from_now]`

The number of minutes to extend the quiz from the current time. This is mutually exclusive to extend\_from\_end\_at. This is limited to 1440 minutes (24 hours)

`quiz_extensions[][extend_from_end_at]`

The number of minutes to extend the quiz beyond the quiz’s current ending time. This is mutually exclusive to extend\_from\_now. This is limited to 1440 minutes (24 hours)

**Example Request:**

```
{
  "quiz_extensions": [{
    "user_id": 3,
    "extra_attempts": 2,
    "extra_time": 20,
    "manually_unlocked": true
  },{
    "user_id": 2,
    "extra_attempts": 2,
    "extra_time": 20,
    "manually_unlocked": false
  }]
}
```

```
{
  "quiz_extensions": [{
    "user_id": 3,
    "extend_from_now": 20
  }]
}
```

**Example Response:**

```
{
  "quiz_extensions": [QuizExtension]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).