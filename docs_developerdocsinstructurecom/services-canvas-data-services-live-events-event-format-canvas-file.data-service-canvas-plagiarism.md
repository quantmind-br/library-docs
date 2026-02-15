---
title: Plagiarism | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_plagiarism
source: sitemap
fetched_at: 2026-02-15T09:06:37.130958-03:00
rendered_js: false
word_count: 259
summary: This document defines the structure and triggers for the Canvas LMS plagiarism_resubmit event, detailing the metadata and body fields included in the event notification.
tags:
    - canvas-lms
    - event-data
    - plagiarism-detection
    - webhook-reference
    - submission-events
    - json-schema
category: reference
---

**Definition:** The event is emitted anytime a submission is created for an assignment with plagiarism settings turned on.

**Trigger:** Triggered when a submission is resubmitted.

```
{
"metadata":{
"client_ip":"93.184.216.34",
"context_account_id":"21070000000000079",
"context_id":"21070000000000565",
"context_role":"TaEnrollment",
"context_sis_source_id":"2017.100.101.101-1",
"context_type":"Course",
"event_name":"plagiarism_resubmit",
"event_time":"2019-11-05T21:52:21.127Z",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/courses/27745/gradebook/speed_grader?assignment_id=154394&student_id=90175",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"time_zone":"America/New_York",
"url":"https://oxana.instructure.com/courses/565/assignments/1234567/submissions/98765/turnitin/resubmit",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000000001",
"user_login":"oxana@example.com",
"user_sis_id":"456-T45"
},
"body":{
"assignment_id":"21070000001234567",
"attempt":1,
"body":"This is my submission to the assignment",
"grade":"F",
"graded_at":"2019-11-05T21:52:21.127Z",
"group_id":"21070000000000099",
"lti_assignment_id":"a1b2c3c4-z9x8-a1s2-q5w6-p9o8i7u6y5t6",
"lti_user_id":"a1b2c3c4z9x8a1s2q5w6p9o8i7u6y5t6a2s3d4f5",
"score":99.5,
"submission_id":"21070000000112233",
"submission_type":"online_text_entry",
"submitted_at":"2019-11-04T21:52:21.127Z",
"updated_at":"2019-11-05T21:52:21.127Z",
"url":null,
"user_id":"21070000000098765",
"workflow_state":"submitted"
}
}
```

The Canvas id of the assignment being submitted.

This is the submission attempt number.

The content of the submission, if it was submitted directly in a text field. NOTE: This field will be truncated to only include the first 8192 characters.

The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example)

The timestamp when the assignment was graded.

The submissions’s group ID if the assignment is a group assignment.

The LTI assignment guid of the submission's assignment

The LTI id of the user associated with the submission.

The Canvas id of the new submission.

The type of submission (online\_text\_entry, online\_url, online\_upload, media\_recording)

The timestamp when the assignment was submitted.

The time at which this assignment was last modified in any way.

The URL of the submission (for 'online\_url' submissions).

The Canvas id of the user associated with the submission.

The state of the submission, such as 'submitted'

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).