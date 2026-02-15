---
title: Assignment Extensions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/assignment_extensions
source: sitemap
fetched_at: 2026-02-15T09:08:01.856262-03:00
rendered_js: false
word_count: 141
summary: This document provides technical specifications for the Assignment Extensions API, which allows instructors to grant additional submission attempts to specific students for assignments.
tags:
    - canvas-lms
    - assignment-extensions
    - rest-api
    - student-submissions
    - extra-attempts
category: api
---

## Assignment Extensions API

API for setting extensions on student assignment submissions. These cannot be set for discussion assignments or quizzes. For quizzes, use [Quiz Extensions](https://developerdocs.instructure.com/services/canvas/resources/quiz_extensions) instead.

**An AssignmentExtension object looks like:**

```
{
  // The ID of the Assignment the extension belongs to.
"assignment_id": 2,
  // The ID of the Student that needs the assignment extension.
"user_id": 3,
  // Number of times the student is allowed to re-submit the assignment
"extra_attempts": 2
}
```

[AssignmentExtensionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_extensions_controller.rb)

`POST /api/v1/courses/:course_id/assignments/:assignment_id/extensions`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/extensions`

**Responses**

- **200 OK** if the request was successful
- **403 Forbidden** if you are not allowed to extend assignments for this course
- **400 Bad Request** if any of the extensions are invalid

**Request Parameters:**

`assignment_extensions[][user_id]`

The ID of the user we want to add assignment extensions for.

`assignment_extensions[][extra_attempts]`

Number of times the student is allowed to re-take the assignment over the limit.

**Example Request:**

```
{
  "assignment_extensions": [{
    "user_id": 3,
    "extra_attempts": 2
  },{
    "user_id": 2,
    "extra_attempts": 2
  }]
}
```

**Example Response:**

```
{
  "assignment_extensions": [AssignmentExtension]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).