---
title: Quiz | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_quiz
source: sitemap
fetched_at: 2026-02-15T09:06:39.162316-03:00
rendered_js: false
word_count: 120
summary: This document defines the quiz_submitted event in Canvas LMS, explaining its trigger mechanism and the structure of its data payload for old quiz assignments.
tags:
    - canvas-lms
    - quiz-submitted
    - event-stream
    - webhook-events
    - data-payload
    - educational-technology
category: reference
---

**Definition:** The event is emitted anytime a user submits a quiz assignment in Canvas \[old quizzes].

**Trigger:** Triggered when a user submits a quiz assignment \[old quizzes].

```
{
"metadata":{
"client_ip":"93.184.216.34",
"context_account_id":"21070000000000123",
"context_id":"21070000000100123",
"context_role":"StudentEnrollment",
"context_sis_source_id":"44942121",
"context_type":"Course",
"event_name":"quiz_submitted",
"event_time":"2019-11-01T19:11:33.388Z",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/courses/100123/quizzes/2223333/take/questions/47464543",
"request_id":"11394325-4220-4a39-8237-f198d193d393",
"root_account_id":"21070000000000123",
"root_account_lti_guid":"f63324b4e2a0841cbbe2b48abbccedb453becf36.oxana.instructure.com",
"root_account_uuid":"01314161-1afc-0f2f-ffbf-1f31f5f0f972",
"session_id":"dc29809b38908fe0890a8098b8982211",
"time_zone":"Pacific/Honolulu",
"url":"https://oxana.instructure.com/courses/100123/quizzes/2223333/submissions?user_id=987123",
"user_account_id":"21070000000000123",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000987123",
"user_login":"oxana",
"user_sis_id":"1243245"
},
"body":{
"quiz_id":"11210000002223333",
"submission_id":"11210000013995723"
}
}
```

The Canvas id of the quiz.

The Canvas id of the quiz submission.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).