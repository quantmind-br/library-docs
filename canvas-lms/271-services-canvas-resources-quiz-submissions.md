---
title: Quiz Submissions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_submissions
source: sitemap
fetched_at: 2026-02-15T09:08:41.720447-03:00
rendered_js: false
word_count: 678
summary: This document provides technical documentation for the Quiz Submissions API, detailing how to retrieve, start, update, and complete student quiz attempts.
tags:
    - canvas-lms
    - quiz-submissions
    - api-endpoints
    - grading
    - student-data
    - rest-api
category: api
---

API for accessing quiz submissions

**A QuizSubmission object looks like:**

```
{
  // The ID of the quiz submission.
"id": 1,
  // The ID of the Quiz the quiz submission belongs to.
"quiz_id": 2,
  // The ID of the Student that made the quiz submission.
"user_id": 3,
  // The ID of the Submission the quiz submission represents.
"submission_id": 1,
  // The time at which the student started the quiz submission.
"started_at": "2013-11-07T13:16:18Z",
  // The time at which the student submitted the quiz submission.
"finished_at": "2013-11-07T13:16:18Z",
  // The time at which the quiz submission will be overdue, and be flagged as a
  // late submission.
"end_at": "2013-11-07T13:16:18Z",
  // For quizzes that allow multiple attempts, this field specifies the quiz
  // submission attempt number.
"attempt": 3,
  // Number of times the student was allowed to re-take the quiz over the
  // multiple-attempt limit.
"extra_attempts": 1,
  // Amount of extra time allowed for the quiz submission, in minutes.
"extra_time": 60,
  // The student can take the quiz even if it's locked for everyone else
"manually_unlocked": true,
  // Amount of time spent, in seconds.
"time_spent": 300,
  // The score of the quiz submission, if graded.
"score": 3,
  // The original score of the quiz submission prior to any re-grading.
"score_before_regrade": 2,
  // For quizzes that allow multiple attempts, this is the score that will be
  // used, which might be the score of the latest, or the highest, quiz
  // submission.
"kept_score": 5,
  // Number of points the quiz submission's score was fudged by.
"fudge_points": 1,
  // Whether the student has viewed their results to the quiz.
"has_seen_results": true,
  // The current state of the quiz submission. Possible values:
  // ['untaken'|'pending_review'|'complete'|'settings_only'|'preview'].
"workflow_state": "untaken",
  // Indicates whether the quiz submission is overdue and needs submission
"overdue_and_needs_submission": false
}
```

[Quizzes::QuizSubmissionsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

Get a list of all submissions for this quiz. Users who can view or manage grades for a course will have submissions from multiple users returned. A user who can only submit will have only their own submissions returned. When a user has an in-progress submission, only that submission is returned. When there isn’t an in-progress quiz\_submission, all completed submissions, including previous attempts, are returned.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

Associations to include with the quiz submission.

Allowed values: `submission`, `quiz`, `user`

**Example Response:**

```
{
  "quiz_submissions": [QuizSubmission]
}
```

[Quizzes::QuizSubmissionsApiController#submissionarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submission`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submission`

Get the submission for this quiz for the current user.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

Associations to include with the quiz submission.

Allowed values: `submission`, `quiz`, `user`

**Example Response:**

```
{
  "quiz_submissions": [QuizSubmission]
}
```

[Quizzes::QuizSubmissionsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

Get a single quiz submission.

**200 OK** response code is returned if the request was successful.

**Request Parameters:**

Associations to include with the quiz submission.

Allowed values: `submission`, `quiz`, `user`

**Example Response:**

```
{
  "quiz_submissions": [QuizSubmission]
}
```

[Quizzes::QuizSubmissionsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions`

Start taking a Quiz by creating a QuizSubmission which you can use to answer questions and submit your answers.

**Responses**

- **200 OK** if the request was successful
- **400 Bad Request** if the quiz is locked
- **403 Forbidden** if an invalid access code is specified
- **403 Forbidden** if the Quiz’s IP filter restriction does not pass
- **409 Conflict** if a QuizSubmission already exists for this user and quiz

**Request Parameters:**

Access code for the Quiz, if any.

Whether this should be a preview QuizSubmission and not count towards the user’s course record. Teachers only.

**Example Response:**

```
{
  "quiz_submissions": [QuizSubmission]
}
```

[Quizzes::QuizSubmissionsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`PUT /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id`

Update the amount of points a student has scored for questions they’ve answered, provide comments for the student about their answer(s), or simply fudge the total score by a specific amount of points.

**Responses**

- **200 OK** if the request was successful
- **403 Forbidden** if you are not a teacher in this course
- **400 Bad Request** if the attempt parameter is missing or invalid
- **400 Bad Request** if the specified QS attempt is not yet complete

**Request Parameters:**

`quiz_submissions[][attempt]`

The attempt number of the quiz submission that should be updated. This attempt MUST be already completed.

`quiz_submissions[][fudge_points]`

Amount of positive or negative points to fudge the total score by.

`quiz_submissions[][questions]`

A set of scores and comments for each question answered by the student. The keys are the question IDs, and the values are hashes of ‘score`and`comment\` entries. See [Appendix: Manual Scoring](https://developerdocs.instructure.com/services/canvas/resources/quiz_submissions#Manual+Scoring-appendix) for more on this parameter.

**Example Request:**

```
{
  "quiz_submissions": [{
    "attempt": 1,
    "fudge_points": -2.4,
    "questions": {
      "1": {
        "score": 2.5,
        "comment": "This can't be right, but I'll let it pass this one time."
      },
      "2": {
        "score": 0,
        "comment": "Good thinking. Almost!"
      }
    }
  }]
}
```

**Example Response:**

```
{
  "quiz_submissions": [QuizSubmission]
}
```

**See Also:**

[Quizzes::QuizSubmissionsApiController#completearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/complete`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/complete`

Complete the quiz submission by marking it as complete and grading it. When the quiz submission has been marked as complete, no further modifications will be allowed.

**Responses**

- **200 OK** if the request was successful
- **403 Forbidden** if an invalid access code is specified
- **403 Forbidden** if the Quiz’s IP filter restriction does not pass
- **403 Forbidden** if an invalid token is specified
- **400 Bad Request** if the QS is already complete
- **400 Bad Request** if the attempt parameter is missing
- **400 Bad Request** if the attempt parameter is not the latest attempt

**Request Parameters:**

The attempt number of the quiz submission that should be completed. Note that this must be the latest attempt index, as earlier attempts can not be modified.

The unique validation token you received when this Quiz Submission was created.

Access code for the Quiz, if any.

**Example Response:**

```
{
  "quiz_submissions": [QuizSubmission]
}
```

[Quizzes::QuizSubmissionsApiController#timearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submissions_api_controller.rb)

`GET /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/time`

**Scope:** `url:GET|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/:id/time`

Get the current timing data for the quiz attempt, both the end\_at timestamp and the time\_left parameter.

**Responses**

- **200 OK** if the request was successful

**Example Response:**

```
{
  "end_at": [DateTime],
  "time_left": [Integer]
}
```

**Parameter synopsis**

```
{
  "quiz_submissions": [{
    "fudge_points": null, // null for no change, or a signed decimal
    "questions": {
      "QUESTION_ID": {
        "score": null, // null for no change, or an unsigned decimal
        "comment": null // null for no change, '' for no comment, or a string
      }
    }
  }]
}
```

**Fudging the score by a negative amount**

```
{
  "quiz_submissions": [{
    "attempt": 1,
    "fudge_points": -2.4
  }]
}
```

**Removing an earlier comment on a question**

```
{
  "quiz_submissions": [{
    "attempt": 1,
    "questions": {
      "1": {
        "comment": ""
      }
    }
  }]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).