---
title: Outcomes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_outcomes
source: sitemap
fetched_at: 2026-02-15T09:06:34.531885-03:00
rendered_js: false
word_count: 147
summary: This document defines the schema and triggers for the outcomes.retry_outcome_alignment_clone event, which occurs when a user manually retries the alignment cloning process in Canvas LMS.
tags:
    - canvas-lms
    - event-schema
    - outcome-alignment
    - learning-outcomes
    - event-streaming
category: reference
---

### outcomes.retry\_outcome\_alignment\_clone

**Definition:** The event is emitted anytime an outcome alignment clone process is retried, this can happend due to a network issue or a missing alignment

**Trigger:** Manually triggered by the user

```
{
"metadata":{
"context_type":"Course",
"context_id":"10000000000001",
"context_account_id":"10000000000034",
"context_sis_source_id":null,
"root_account_uuid":"8H3aGjEatiLI42zzV0ly8t5UGQAxYfvrI3MDlrCx",
"root_account_id":"10000000000001",
"root_account_lti_guid":"8H3aGjEatiLI42zzV0ly8t5UGQAxYfvrI3MDlrCx:canvas-lms",
"user_login":"canvas@instructure.com",
"user_account_id":"10000000000002",
"user_sis_id":null,
"user_id":"10000000000001",
"time_zone":"America/Denver",
"context_role":"TeacherEnrollment",
"request_id":"61b6044c-5fba-4a0a-bf61-c918f7aea445",
"session_id":"bf950e2284bd720a28e407fe326dce68",
"hostname":"canvas.docker",
"http_method":"POST",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
"client_ip":"192.168.65.1",
"url":"http://canvas.docker/api/v1/courses/1/assignments/2/retry_alignment_clone?target_assignment_id=3&target_course_id=2",
"referrer":"http://canvas.docker/courses/2/assignments",
"producer":"canvas",
"event_name":"outcomes.retry_outcome_alignment_clone",
"event_time":"2024-07-30T19:04:35.872Z"
},
"body":{
"original_course_uuid":"RuBP4jfbRXyaG6LpOFW70jkZyFmj5beZxeGO5bMB",
"new_course_uuid":"fFFdVF27nlchmL1IZgfJRqV8FxPkNQxwdLu7dWNv",
"new_course_resource_link_id":"f97330a96452fc363a34e0ef6d8d0d3e9e1007d2",
"domain":"canvas.docker",
"original_assignment_resource_link_id":"aececbb42db5da02927f416330b6aed170351ab5",
"new_assignment_resource_link_id":"669532ec8df2f15c8d176a7e8c96eb29565e0e89",
"status":"outcome_alignment_cloning"
}
}
```

The uuid of the source course

The uuid of the target course

**new\_course\_resource\_link\_id**

lti\_context\_id of the target course

**original\_assignment\_resource\_link\_id**

lti\_resource\_link\_id of the source assignment

**new\_assignment\_resource\_link\_id**

lti\_resource\_link\_id of the target assignment

status of the target assignment

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).