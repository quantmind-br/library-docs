---
title: Quiz Submission Files | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/quiz_submission_files
source: sitemap
fetched_at: 2026-02-15T09:08:50.086002-03:00
rendered_js: false
word_count: 106
summary: This document outlines the API endpoint for initiating file uploads to quiz submissions in Canvas LMS. It details the request parameters and references the general file upload workflow required to associate attachments with quiz attempts.
tags:
    - canvas-lms
    - quiz-submission
    - file-upload
    - rest-api
    - quizzes
category: api
---

## Quiz Submission Files API

[Quizzes::QuizSubmissionFilesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/quizzes/quiz_submission_files_controller.rb)

`POST /api/v1/courses/:course_id/quizzes/:quiz_id/submissions/self/files`

**Scope:** `url:POST|/api/v1/courses/:course_id/quizzes/:quiz_id/submissions/self/files`

Associate a new quiz submission file

This API endpoint is the first step in uploading a quiz submission file. See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow as these parameters are interpreted as per the documentation there.

**Request Parameters:**

The name of the quiz submission file

How to handle duplicate names

**Example Response:**

```
{
"attachments": [
{
"upload_url":"https://some-bucket.s3.amazonaws.com/",
"upload_params":{
"key":"/users/1234/files/answer_pic.jpg",
"acl":"private",
"Filename":"answer_pic.jpg",
"AWSAccessKeyId":"some_id",
"Policy":"some_opaque_string",
"Signature":"another_opaque_string",
"Content-Type":"image/jpeg"
}
}
  ]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).