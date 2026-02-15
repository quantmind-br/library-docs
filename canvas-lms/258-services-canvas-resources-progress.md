---
title: Progress | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/progress
source: sitemap
fetched_at: 2026-02-15T09:09:13.603311-03:00
rendered_js: false
word_count: 153
summary: This document describes the API endpoints and data structures used to track the progress of asynchronous operations and manage active jobs.
tags:
    - asynchronous-jobs
    - progress-tracking
    - api-endpoints
    - canvas-lms
    - job-monitoring
category: api
---

API for querying the progress of asynchronous API operations.

API for querying the progress of asynchronous API operations.

**A Progress object looks like:**

```
{
  // the ID of the Progress object
"id": 1,
  // the context owning the job.
"context_id": 1,
"context_type": "Account",
  // the id of the user who started the job
"user_id": 123,
  // the type of operation
"tag": "course_batch_update",
  // percent completed
"completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
"workflow_state": "completed",
  // the time the job was created
"created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
"updated_at": "2013-01-15T15:04:00Z",
  // optional details about the job
"message": "17 courses processed",
  // optional results of the job. omitted when job is still pending
"results": {"id":"123"},
  // url where a progress update can be retrieved
"url": "https://canvas.example.edu/api/v1/progress/1"
}
```

**A Progress object looks like:**

```
{
  // the ID of the Progress object
  "id": 1,
  // the context owning the job.
  "context_id": 1,
  "context_type": "Account",
  // the id of the user who started the job
  "user_id": 123,
  // the type of operation
  "tag": "course_batch_update",
  // percent completed
  "completion": 100,
  // the state of the job one of 'queued', 'running', 'completed', 'failed'
  "workflow_state": "completed",
  // the time the job was created
  "created_at": "2013-01-15T15:00:00Z",
  // the time the job was last updated
  "updated_at": "2013-01-15T15:04:00Z",
  // optional details about the job
  "message": "17 courses processed",
  // optional results of the job. omitted when job is still pending
  "results": {"id":"123"},
  // url where a progress update can be retrieved with an LTI access token
  "url": "https://canvas.example.edu/api/lti/courses/1/progress/1"
}
```

[ProgressController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb)

`GET /api/v1/progress/:id`

**Scope:** `url:GET|/api/v1/progress/:id`

Return completion and status information about an asynchronous job

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[ProgressController#cancelarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/progress_controller.rb)

`POST /api/v1/progress/:id/cancel`

**Scope:** `url:POST|/api/v1/progress/:id/cancel`

Cancel an asynchronous job associated with a Progress object If you include “message” in the POSTed data, it will be set on the Progress and returned. This is handy to distinguish between cancel and fail for a workflow\_state of “failed”.

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[Lti::Ims::ProgressController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/progress_controller.rb)

`GET /api/lti/courses/:course_id/progress/:id`

**Scope:** `url:GET|/api/lti/courses/:course_id/progress/:id`

Return completion and status information about an asynchronous job

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).