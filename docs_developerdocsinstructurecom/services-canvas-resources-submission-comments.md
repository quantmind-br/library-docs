---
title: Submission Comments | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/submission_comments
source: sitemap
fetched_at: 2026-02-15T09:05:07.981991-03:00
rendered_js: false
word_count: 155
summary: This document details the API endpoints for managing submission comments, specifically covering how to update, delete, and upload file attachments for comments within assignments.
tags:
    - canvas-lms
    - api-documentation
    - submission-comments
    - file-upload
    - rest-api
    - assignment-submissions
category: api
---

This API can be used to edit and delete submission comments.

[SubmissionCommentsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submission_comments_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`

Edit the given submission comment.

**Request Parameters:**

If this argument is present, edit the text of a comment.

Returns a [SubmissionComment](https://developerdocs.instructure.com/services/canvas/resources/submissions#submissioncomment) object.

[SubmissionCommentsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submission_comments_api_controller.rb)

`DELETE /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/:id`

Delete the given submission comment.

**Example Request:**

```
curlhttps://<canvas>/api/v1/courses/<course_id>/assignments/<assignment_id>/submissions/<user_id>/comments/<id>\
-XDELETE\
-H'Authorization: Bearer <token>'
```

Returns a [SubmissionComment](https://developerdocs.instructure.com/services/canvas/resources/submissions#submissioncomment) object.

[SubmissionCommentsApiController#create\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/submission_comments_api_controller.rb)

`POST /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/files`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id/comments/files`

Upload a file to attach to a submission comment

See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data, including the new file id. The caller can then PUT the file\_id to the submission API to attach it to a comment

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).