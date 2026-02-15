---
title: Logged | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_logged
source: sitemap
fetched_at: 2026-02-15T09:06:26.511755-03:00
rendered_js: false
word_count: 145
summary: This document defines the event data structures and triggers for user login and logout actions within the Canvas LMS. It details the metadata and body schemas emitted when users authenticate or terminate their sessions.
tags:
    - canvas-lms
    - event-streams
    - authentication
    - login-events
    - logout-events
    - api-reference
    - json-schema
category: reference
---

**Definition:** The event is emitted anytime an end user logs into Canvas

**Trigger:** Triggered when a user has logged in.

```
{
"metadata":{
"client_ip":"93.184.216.34",
"event_name":"logged_in",
"event_time":"2019-11-01T19:11:01.335Z",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"producer":"canvas",
"referrer":"https://oxana.instructure.com/idp/profile/SAML2/Redirect/SSO?execution=e1s2",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"url":"https://oxana.instructure.com/login/saml",
"user_account_id":"21070000000000001",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"user_id":"21070000000000001",
"user_login":"oxana@example.com",
"user_sis_id":"456-T45"
},
"body":{
"redirect_url":"https://oxana.instructure.com/"
}
}
```

The URL the user was redirected to after logging in. Is set when the user logs in after clicking a deep link into Canvas.

**Definition:** The event is emitted anytime an end user logs out of Canvas

**Trigger:** Triggered when a user has logged out.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "event_name": "logged_out",
    "event_time": "2019-11-01T19:11:04.195Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/1188569/quizzes/4266352?module_item_id=23650329",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Los_Angeles",
    "url": "https://oxana.instructure.com/logout",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {}
}
```

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).