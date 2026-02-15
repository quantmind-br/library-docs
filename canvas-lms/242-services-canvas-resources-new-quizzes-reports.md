---
title: New Quizzes Reports | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/new_quizzes_reports
source: sitemap
fetched_at: 2026-02-15T09:09:55.00554-03:00
rendered_js: false
word_count: 133
summary: This document describes the API endpoint for generating student and item analysis reports for Canvas New Quizzes and monitoring their progress.
tags:
    - canvas-lms
    - quiz-reports
    - api-endpoint
    - report-generation
    - progress-tracking
category: api
---

API for generating New Quizzes Reports.

**A Progress object looks like:**

```
{
  // the ID of the Progress object
"id": 1,
  // the context owning the job.
"context_id": 1,
"context_type": "Assignment",
  // the id of the user who started the job
"user_id": 123,
  // percent completed
"completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
"workflow_state": "completed",
  // the time the job was created
"created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
"updated_at": "2013-01-15T15:04:00Z",
  // for successfully completed jobs, this is a JSON object containing url of the
  // report and other details
"results": {"url":"https:\/\/canvas.example.edu\/api\/assignments\/1\/files\/2\/download"},
  // url where a progress update can be retrieved
"url": "https://canvas.example.edu/api/v1/progress/1"
}
```

`POST /api/quiz/v1/courses/:course_id/quizzes/:assignment_id/reports`

**Scope:** `url:POST|/api/quiz/v1/courses/:course_id/quizzes/:assignment_id/reports`

Generate a new report for this quiz. Returns a progress object that can be used to track the progress of the report generation.

**Responses**

- `400 Bad Request` if the specified report type or format is invalid
- `409 Conflict` if a quiz report of the specified type is already being generated

**Request Parameters:**

The type of report to be generated.

Allowed values: `student_analysis`, `item_analysis`

The format of report to be generated.

Allowed values: `csv`, `json`

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).