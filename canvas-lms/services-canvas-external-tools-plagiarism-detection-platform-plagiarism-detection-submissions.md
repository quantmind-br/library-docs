---
title: Plagiarism Detection Submissions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_submissions
source: sitemap
fetched_at: 2026-02-15T09:00:40.4837-03:00
rendered_js: false
word_count: 100
summary: This document details the LTI API endpoints for retrieving plagiarism detection submissions and their attempt history, including data structures for submission and file objects.
tags:
    - plagiarism-detection
    - lti-api
    - canvas-lms
    - submissions-api
    - jwt-authentication
    - api-reference
category: api
---

## Plagiarism Detection Submissions API

**LTI API for Plagiarism Detection Submissions (Must use** [**JWT access tokens**](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

**A Submission object looks like:**

```
{
"lti_course_id": "66157096483e6b3a50bfedc6bac902c0b20a8241",
"course_id": 10000000000060,
  // The submission's assignment id
"assignment_id": 23,
  // This is the submission attempt number.
"attempt": 1,
  // The content of the submission, if it was submitted directly in a text field.
"body": "There are three factors too...",
  // The types of submission ex:
  // ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_
  // annotation')
"submission_type": "online_text_entry",
  // The timestamp when the assignment was submitted
"submitted_at": "2012-01-01T01:00:00Z",
  // The URL of the submission (for 'online_url' submissions).
"url": null,
  // The id of the user who created the submission
"user_id": 134,
  // UTC timestamp showing when the user agreed to the EULA (if given by the tool
  // provider)
"eula_agreement_timestamp": "1508250487578",
  // The current state of the submission
"workflow_state": "submitted",
  // Files that are attached to the submission
"attachments": null
}
```

**A File object looks like:**

```
{
  "size": 4,
  "content-type": "text/plain",
  "url": "http://www.example.com/files/569/download?download_frd=1",
  "id": 569,
  "display_name": "file.txt",
  "created_at": "2012-07-06T14:58:50Z",
  "updated_at": "2012-07-06T14:58:50Z"
}
```

[Lti::SubmissionsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/submissions_api_controller.rb)

`GET /api/lti/assignments/:assignment_id/submissions/:submission_id`

**Scope:** `url:GET|/api/lti/assignments/:assignment_id/submissions/:submission_id`

Get a single submission, based on submission id.

[Lti::SubmissionsApiController#historyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/submissions_api_controller.rb)

`GET /api/lti/assignments/:assignment_id/submissions/:submission_id/history`

**Scope:** `url:GET|/api/lti/assignments/:assignment_id/submissions/:submission_id/history`

Get a list of all attempts made for a submission, based on submission id.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).