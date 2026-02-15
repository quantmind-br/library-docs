---
title: Final | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_final
source: sitemap
fetched_at: 2026-02-15T08:58:35.714881-03:00
rendered_js: false
word_count: 209
summary: This document defines the schema and trigger conditions for the final_grade_custom_status event in Canvas LMS. It describes the metadata and body parameters sent when a custom status is applied to or removed from a student's final grade.
tags:
    - canvas-lms
    - event-streams
    - grading
    - webhooks
    - metadata-schema
category: reference
---

### final\_grade\_custom\_status

**Definition:** The event gets emitted when a custom status is removed or applied to a student's final grade.

**Trigger:** Triggered when a custom status is applied or removed from a student's final grade.

```
{
"metadata":{
"root_account_uuid":"44fJ44GgJ29gJBsl43JLKgljsBIOTsbnKT48932g",
"root_account_id":"10000000000001",
"root_account_lti_guid":"794d72b707af6ea82cfe3d5d473f16888a8366c7.canvas.docker",
"user_login":"oxana@instructure.com",
"user_account_id":"10000000000002",
"user_sis_id":null,
"user_id":"21070000000000001",
"time_zone":"America/Denver",
"context_type":"Course",
"context_id":"21070000000000002",
"context_sis_source_id":"194387",
"context_account_id":"21070000000000003",
"context_role":"TeacherEnrollment",
"request_id":"98e1b771-fe22-4481-8264-d523dadb16b1",
"session_id":"242872453a9d69f7ccddeb4788d22506",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"client_ip":"93.184.216.34",
"url":"http://oxana.instructure.com/courses/2/gradebook/update_submission",
"referrer":"http://oxana.instructure.com/courses/2/gradebook/speed_grader?assignment_id=39&student_id=2",
"producer":"canvas",
"event_name":"final_grade_custom_status",
"event_time":"2019-12-11T16:26:34.552Z"
},
"body":{
"score_id":"12345",
"enrollment_id":"67890",
"user_id":"2",
"course_id":"2",
"grading_period_id":"13579",
"override_status":"Incomplete Passing",
"override_status_id":"2",
"old_override_status":"Incomplete",
"old_override_status_id":"1",
"updated_at":"2019-12-11T16:26:34Z"
}
}
```

The Canvas ID of the score record.

The Canvas ID of the enrollment record for the student.

The Canvas user ID of the student.

The Canvas ID of the course.

The Canvas ID of the grading period, if applicable.

The new custom status name applied to a user's final grade

The new custom status ID applied to a user's final grade

The previous custom status name applied to a user's final grade, if applicable

The previous custom status ID applied to a user's final grade, if applicable

The time when the custom status was applied.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).