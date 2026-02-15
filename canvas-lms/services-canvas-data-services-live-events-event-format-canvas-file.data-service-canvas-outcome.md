---
title: Outcome | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_outcome
source: sitemap
fetched_at: 2026-02-15T09:06:32.871223-03:00
rendered_js: false
word_count: 258
summary: This document defines the schema and triggers for event notifications emitted when outcome calculation methods are created or updated in Canvas LMS.
tags:
    - canvas-lms
    - event-stream
    - webhooks
    - learning-outcomes
    - json-schema
    - api-events
category: reference
---

### outcome\_calculation\_method\_created

**Definition:** The event is emitted anytime a new outcome\_calculation\_method is created by an end user or API request.

**Trigger:** Triggered when a new outcome\_calculation\_method is saved.

```
{
"metadata":{
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"7db438071375c02373713c12c73869ff2f470b68.oxana.instructure.com",
"user_login":"oxana@instructure.com",
"user_account_id":"21070000000000001",
"user_sis_id":"456-T45",
"user_id":"21070000000000001",
"time_zone":"America/Denver",
"context_type":"Account",
"context_id":"21070000000000144",
"context_sis_source_id":"2017.100.101.101-1",
"context_account_id":"21070000000000079",
"request_id":"1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
"session_id":"ef686f8ed684abf78cbfa1f6a58112b5",
"hostname":"oxana.instructure.com",
"http_method":"POST",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
"client_ip":"93.184.216.34",
"url":"https://oxana.instructure.com/api/graphql",
"referrer":null,
"producer":"canvas",
"event_name":"outcome_calculation_method_created",
"event_time":"2020-08-18T23:28:24.396Z"
},
"body":{
"outcome_calculation_method_id":"1",
"context_type":"Account",
"context_id":"1",
"calculation_method":"decaying_average",
"calculation_int":65,
"workflow_state":"active"
}
}
```

**outcome\_calculation\_method\_id**

The Canvas id of the outcome calculation method.

The type of context the outcome calculation method is used in.

The id of the context the outcome calculation method is used in.

Workflow state of the outcome calculation method. E.g active, deleted.

Defines the variable value used by the calculation\_method. Included only if calculation\_method uses it.

The method used to calculate student score.

### outcome\_calculation\_method\_updated

**Definition:** The event is emitted anytime an outcome\_calculation\_method is updated by an end user or API request.

**Trigger:** Triggered when an outcome\_calculation\_method is updated.

```
{
  "metadata": {
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "7db438071375c02373713c12c73869ff2f470b68.oxana.instructure.com",
    "user_login": "oxana@instructure.com",
    "user_account_id": "21070000000000001",
    "user_sis_id": "456-T45",
    "user_id": "21070000000000001",
    "time_zone": "America/Denver",
    "context_type": "Account",
    "context_id": "21070000000000144",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_account_id": "21070000000000079",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "client_ip": "93.184.216.34",
    "url": "https://oxana.instructure.com/api/graphql",
    "referrer": null,
    "producer": "canvas",
    "event_name": "outcome_calculation_method_updated",
    "event_time": "2020-08-18T23:28:24.396Z"
  },
  "body": {
    "outcome_calculation_method_id": "1",
    "context_type": "Account",
    "context_id": "1",
    "calculation_method": "decaying_average",
    "calculation_int": 65,
    "workflow_state": "active",
    "updated_at": "2020-08-18T17:24:46-06:00"
  }
}
```

**outcome\_calculation\_method\_id**

The Canvas id of the outcome calculation method.

The type of context the outcome calculation method is used in.

The id of the context the outcome calculation method is used in.

Workflow state of the outcome calculation method. E.g active, deleted.

Defines the variable value used by the calculation\_method. Included only if calculation\_method uses it.

The method used to calculate student score.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).