---
title: Quiz Assignment Overrides | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_assignment_overrides
source: sitemap
fetched_at: 2026-02-15T09:09:05.812392-03:00
rendered_js: false
word_count: 167
summary: This document outlines the API endpoints and data structures used to retrieve quiz assignment overrides, including due dates and availability windows for specific students or sections.
tags:
    - canvas-lms
    - quiz-overrides
    - assignment-overrides
    - api-endpoints
    - due-dates
category: api
---

## Quiz Assignment Overrides API

**A QuizAssignmentOverrideSet object looks like:**

```
// Set of assignment-overridden dates for a quiz.
{
  // ID of the quiz those dates are for.
"quiz_id": "1",
  // An array of quiz assignment overrides. For students, this array will always
  // contain a single item which is the set of dates that apply to that student.
  // For teachers and staff, it may contain more.
"due_dates": null,
  // An array of all assignment overrides active for the quiz. This is visible
  // only to teachers and staff.
"all_dates": null
}
```

**A QuizAssignmentOverrideSetContainer object looks like:**

```
// Container for set of assignment-overridden dates for a quiz.
{
  // The QuizAssignmentOverrideSet
"quiz_assignment_overrides": null
}
```

**A QuizAssignmentOverride object looks like:**

```
// Set of assignment-overridden dates for a quiz.
{
  // ID of the assignment override, unless this is the base construct, in which
  // case the 'id' field is omitted.
  "id": 1,
  // The date after which any quiz submission is considered late.
  "due_at": "2014-02-21T06:59:59Z",
  // Date when the quiz becomes available for taking.
  "unlock_at": null,
  // When the quiz will stop being available for taking. A value of null means it
  // can always be taken.
  "lock_at": "2014-02-21T06:59:59Z",
  // Title of the section this assignment override is for, if any.
  "title": "Project X",
  // If this property is present, it means that dates in this structure are not
  // based on an assignment override, but are instead for all students.
  "base": true
}
```

[Quizzes::QuizAssignmentOverridesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_assignment_overrides_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/assignment_overrides`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/assignment_overrides`

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes based on the assignment overrides active for the current API user.

**Request Parameters:**

`quiz_assignment_overrides[][quiz_ids][]`

An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned.

**Example Response:**

```
{
"quiz_assignment_overrides": [{
"quiz_id":"1",
"due_dates": [QuizAssignmentOverride],
"all_dates": [QuizAssignmentOverride]
},{
"quiz_id":"2",
"due_dates": [QuizAssignmentOverride],
"all_dates": [QuizAssignmentOverride]
}]
}
```

Returns a [QuizAssignmentOverrideSetContainer](https://developerdocs.instructure.com/services/canvas/resources/quiz_assignment_overrides#quizassignmentoverridesetcontainer) object.

[Quizzes::QuizAssignmentOverridesController#new\_quizzesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_assignment_overrides_controller.rb)

`GET /api/v1/courses/:course_id/new_quizzes/assignment_overrides`

**Scope:** `url:GET|/api/v1/courses/:course_id/new_quizzes/assignment_overrides`

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes based on the assignment overrides active for the current API user.

**Request Parameters:**

`quiz_assignment_overrides[][quiz_ids][]`

An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned.

**Example Response:**

```
{
"quiz_assignment_overrides": [{
"quiz_id":"1",
"due_dates": [QuizAssignmentOverride],
"all_dates": [QuizAssignmentOverride]
},{
"quiz_id":"2",
"due_dates": [QuizAssignmentOverride],
"all_dates": [QuizAssignmentOverride]
}]
}
```

Returns a [QuizAssignmentOverrideSetContainer](https://developerdocs.instructure.com/services/canvas/resources/quiz_assignment_overrides#quizassignmentoverridesetcontainer) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).