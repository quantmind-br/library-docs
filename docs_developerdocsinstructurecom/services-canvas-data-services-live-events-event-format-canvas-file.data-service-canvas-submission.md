---
title: Submission | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_submission
source: sitemap
fetched_at: 2026-02-15T08:58:32.244421-03:00
rendered_js: false
word_count: 725
summary: This document provides technical specifications and schema definitions for submission-related event notifications within the Canvas LMS platform. It details the triggers, metadata, and data body structures for events such as comment creation, submission updates, and grade status changes.
tags:
    - canvas-lms
    - event-stream
    - webhooks
    - submission-events
    - api-reference
    - json-schema
    - instructure-canvas
category: reference
---

### submission\_comment\_created

**Definition:** The event is emitted anytime an end user or API request comments on a submission.

**Trigger:** Triggered when a new comment is added to a submission.

```
{
"metadata":{
"client_ip":"93.184.216.34",
"context_account_id":"21070000000000079",
"context_id":"21070000000000565",
"context_role":"TeacherEnrollment",
"context_sis_source_id":"2017.100.101.101-1",
"context_type":"Course",
"event_name":"submission_comment_created",
"event_time":"2019-11-01T19:11:13.216Z",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/courses/565/gradebook/speed_grader?assignment_id=2974715&student_id=1740548",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"time_zone":"America/Los_Angeles",
"url":"https://oxana.instructure.com/courses/410200/assignments/3964323/submissions/986036.text",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000012345",
"user_login":"oxana@example.com",
"user_sis_id":"456-T45"
},
"body":{
"attachment_ids":[
"54417187",
"54417188"
],
"body":"See the attached files",
"created_at":"2019-11-01T19:11:13.216Z",
"submission_comment_id":"19811981",
"submission_id":"9987654",
"user_id":"12345"
}
}
```

Array of Canvas ids (as strings) of attachments for this comment.

The text of the comment. NOTE: This field will be truncated to only include the first 8192 characters.

The timestamp when the comment was created.

The Canvas id of the new comment.

The Canvas id of the new submission.

The Canvas id of the user who authored the comment.

**Definition:** The event is emitted anytime an end user or API request submits or re-submits an assignment. This applies to assignments and new quizzes, not classic quizzes. Use quiz\_submitted for classic quiz submissions.

**Trigger:** Triggered when an assignment or new quizzes submission gets updated and has not yet been submitted.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "event_name": "submission_created",
    "event_time": "2019-11-01T19:11:21.419Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": null,
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "url": "https://oxana.instructure.com/api/lti/v1/tools/453919/grade_passback",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
  },
  "body": {
    "assignment_id": "21070000001234012",
    "attempt": 12,
    "body": "Test Submission Data",
    "grade": "Missing",
    "graded_at": "2019-11-01T19:11:21.419Z",
    "group_id": "120123",
    "late": false,
    "lti_assignment_id": "a1b2c3c4-z9x8-a1s2-q5w6-p9o8i7u6y5t6",
    "lti_user_id": "a1b2c3c4z9x8a1s2q5w6p9o8i7u6y5t6a2s3d4f5",
    "missing": false,
    "score": 99.5,
    "submission_id": "21070000012345567",
    "submission_type": "online_text_entry",
    "submitted_at": "2019-11-01T19:11:21.419Z",
    "updated_at": "2019-11-01T19:11:21.419Z",
    "url": "https://test.submission.net",
    "user_id": "21070000000014012",
    "workflow_state": "submitted"
  }
}
```

The Canvas id of the assignment being submitted.

This is the submission attempt number.

The content of the submission, if it was submitted directly in a text field. NOTE: This field will be truncated to only include the first 8192 characters.

The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example)

The timestamp when the assignment was graded, if it was graded.

The submissions’s group ID if the assignment is a group assignment.

Whether the submission was made after the applicable due date.

The LTI assignment guid of the submission's assignment

The Lti id of the user associated with the submission.

Whether the submission is missing, which generally means past-due and not yet submitted.

The Canvas id of the new submission.

The types of submission (basic\_lti\_launch, discussion\_topic, media\_recording, online\_quiz, online\_text\_entry, online\_upload, online\_url)

The timestamp when the assignment was submitted.

The state of the submission: normally 'submitted' or 'pending\_review'.

The time at which this assignment was last modified in any way

The URL of the submission (for 'online\_url' submissions)

The Canvas id of the user associated with the submission.

### submission\_custom\_grade\_status

**Definition:** The event gets emitted when a custom status is removed or applied to a student's submission.

**Trigger:** Triggered when a custom status is applied or removed from a student's submission.

```
{
  "metadata": {
    "root_account_uuid": "44fJ44GgJ29gJBsl43JLKgljsBIOTsbnKT48932g",
    "root_account_id": "10000000000001",
    "root_account_lti_guid": "794d72b707af6ea82cfe3d5d473f16888a8366c7.canvas.docker",
    "user_login": "oxana@instructure.com",
    "user_account_id": "10000000000002",
    "user_sis_id": null,
    "user_id": "21070000000000001",
    "time_zone": "America/Denver",
    "context_type": "Course",
    "context_id": "21070000000000002",
    "context_sis_source_id": "194387",
    "context_account_id": "21070000000000003",
    "context_role": "TeacherEnrollment",
    "request_id": "98e1b771-fe22-4481-8264-d523dadb16b1",
    "session_id": "242872453a9d69f7ccddeb4788d22506",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "client_ip": "93.184.216.34",
    "url": "http://oxana.instructure.com/courses/2/gradebook/update_submission",
    "referrer": "http://oxana.instructure.com/courses/2/gradebook/speed_grader?assignment_id=39&student_id=2",
    "producer": "canvas",
    "event_name": "submission_custom_grade_status",
    "event_time": "2019-12-11T16:26:34.552Z"
  },
  "body": {
    "assignment_id": "11",
    "submission_id": "100",
    "user_id": "2",
    "course_id": "2",
    "submission_status": "Completed",
    "submission_status_id": "2",
    "old_submission_status": "Incomplete",
    "old_submission_status_id": "1",
    "updated_at": "2019-12-11T16:26:34Z"
  }
}
```

The Canvas ID of the assignment.

The Canvas ID of the submission\_id.

The Canvas user ID of the student.

The Canvas ID of the course.

The new custom status name applied to a user's submission

The new custom status ID applied to a user's submission

The previous custom status name applied to a user's submission, if applicable

The previous custom status ID applied to a user's submission, if applicable

The time when the custom status was applied.

**Definition:** The event is emitted anytime an end user or API request modifies a submitted assignment or when a Teacher grades an assignment.

**Trigger:** Triggered when a submission gets updated.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "TeacherEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "submission_updated",
    "event_time": "2019-11-01T19:11:11.325Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/1465707/gradebook/speed_grader?assignment_id=21868751&student_id=8026013",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Los_Angeles",
    "url": "https://oxana.instructure.com/courses/2176632/gradebook/update_submission",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "assignment_id": "21070000000000396",
    "attempt": 1,
    "body": "user: 47, quiz: 78, score: 0.0, time: 2018-10-09 21:29:57 +0000",
    "grade": "S",
    "graded_at": "2018-10-09T21:29:57Z",
    "group_id": "120120",
    "late": false,
    "lti_assignment_id": "f7d76a11-95be-485b-8827-dbe8fdca3332",
    "lti_user_id": null,
    "missing": false,
    "score": 99.5,
    "submission_id": "21070000000011176",
    "submission_type": "online_quiz",
    "submitted_at": "2018-10-09T21:29:57Z",
    "updated_at": "2018-10-09T21:29:57Z",
    "url": null,
    "user_id": "21070000000000047",
    "workflow_state": "submitted"
  }
}
```

The Canvas id of the assignment being submitted.

This is the submission attempt number.

The content of the submission, if it was submitted directly in a text field. NOTE: This field will be truncated to only include the first 8192 characters.

The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example)

The timestamp when the assignment was graded, if it was graded.

The submissions’s group ID if the assignment is a group assignment.

Whether the submission was made after the applicable due date.

The LTI assignment guid of the submission's assignment

The Lti id of the user associated with the submission.

Whether the submission is missing, which generally means past-due and not yet submitted.

The Canvas id of the new submission.

The types of submission (online\_text\_entry, online\_url, online\_upload, media\_recording)

The timestamp when the assignment was submitted.

The state of the submission, such as 'submitted' or 'graded'.

The time at which this assignment was last modified in any way

The URL of the submission (for 'online\_url' submissions)

The Canvas id of the user associated with the submission.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).