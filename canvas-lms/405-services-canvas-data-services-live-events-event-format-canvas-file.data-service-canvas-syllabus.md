---
title: Syllabus | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_syllabus
source: sitemap
fetched_at: 2026-02-15T09:06:49.951357-03:00
rendered_js: false
word_count: 180
summary: This document defines the structure and trigger conditions for the syllabus_updated event in Canvas LMS, detailing the metadata and body fields included in the event payload.
tags:
    - canvas-lms
    - event-schema
    - syllabus-management
    - api-reference
    - webhook-events
category: reference
---

**Definition:** The event is emitted anytime a syllabus is changed in a course by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when a course syllabus gets updated.

```
{
"metadata":{
"client_ip":"93.184.216.34",
"event_name":"syllabus_updated",
"event_time":"2019-11-01T19:11:14.519Z",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/courses/565/assignments/syllabus",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"time_zone":"America/Los_Angeles",
"url":"https://oxana.instructure.com/courses/565",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000000001",
"user_login":"oxana@example.com",
"user_sis_id":"456-T45"
},
"body":{
"course_id":"21070000000000565",
"old_syllabus_body":"<p><iframe style=\"width: 800px; height: 880px;\" src=\"/courses/565/external_tools/retrieve?display=borderless&amp;url=https%3A%2F%2Foxana.instructuremedia.com%2F...",
"syllabus_body":"<p><iframe style=\"width: 800px; height: 880px;\" src=\"/courses/565/external_tools/retrieve?display=borderless&amp;url=https%3A%2F%2Foxana.instructuremedia.com%2F..."
}
}
```

The Canvas id of the updated course.

The old syllabus content. NOTE: This field will be truncated to only include the first 8192 characters. NOTE: This field will be truncated to only include the first 8192 characters.

The new syllabus content. NOTE: This field will be truncated to only include the first 8192 characters.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).