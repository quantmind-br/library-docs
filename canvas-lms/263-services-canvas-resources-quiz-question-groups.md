---
title: Quiz Question Groups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_question_groups
source: sitemap
fetched_at: 2026-02-15T08:56:25.936979-03:00
rendered_js: false
word_count: 264
summary: This document outlines the REST API endpoints for managing quiz question groups in Canvas LMS, including methods for creating, updating, deleting, and reordering groups.
tags:
    - canvas-lms
    - quiz-groups
    - rest-api
    - api-endpoints
    - learning-management-system
category: api
---

API for accessing information on quiz question groups

**A QuizGroup object looks like:**

```
{
  // The ID of the question group.
"id": 1,
  // The ID of the Quiz the question group belongs to.
"quiz_id": 2,
  // The name of the question group.
"name": "Fraction questions",
  // The number of questions to pick from the group to display to the student.
"pick_count": 3,
  // The amount of points allotted to each question in the group.
"question_points": 10,
  // The ID of the Assessment question bank to pull questions from.
"assessment_question_bank_id": 2,
  // The order in which the question group will be retrieved and displayed.
"position": 1
}
```

[Quizzes::QuizGroupsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/groups`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/groups`

Returns a list of question groups in a quiz.

**Example Response:**

```
{
"quiz_groups": [QuizGroup]
}
```

[Quizzes::QuizGroupsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

Returns details of the quiz group with the given id.

Returns a [QuizGroup](https://developerdocs.instructure.com/services/canvas/resources/quiz_question_groups#quizgroup) object.

[Quizzes::QuizGroupsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/groups`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/groups`

Create a new question group for this quiz

**201 Created** response code is returned if the creation was successful.

**Request Parameters:**

The name of the question group.

`quiz_groups[][pick_count]`

The number of questions to randomly select for this group.

`quiz_groups[][question_points]`

The number of points to assign to each question in the group.

`quiz_groups[][assessment_question_bank_id]`

The id of the assessment question bank to pull questions from.

**Example Response:**

```
{
  "quiz_groups": [QuizGroup]
}
```

[Quizzes::QuizGroupsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

`PUT /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

Update a question group

**Request Parameters:**

The name of the question group.

`quiz_groups[][pick_count]`

The number of questions to randomly select for this group.

`quiz_groups[][question_points]`

The number of points to assign to each question in the group.

**Example Response:**

```
{
"quiz_groups": [QuizGroup]
}
```

[Quizzes::QuizGroupsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

`DELETE /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id`

Delete a question group

&lt;b&gt;204 No Content&lt;b&gt; response code is returned if the deletion was successful.

[Quizzes::QuizGroupsController#reorderarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_groups_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id/reorder`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/groups/:id/reorder`

Change the order of the quiz questions within the group

&lt;b&gt;204 No Content&lt;b&gt; response code is returned if the reorder was successful.

**Request Parameters:**

The associated item’s unique identifier

The type of item is always ‘question’ for a group

Allowed values: `question`

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).