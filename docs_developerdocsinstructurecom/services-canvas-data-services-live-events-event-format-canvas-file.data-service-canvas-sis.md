---
title: Sis | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_sis
source: sitemap
fetched_at: 2026-02-15T09:06:45.105633-03:00
rendered_js: false
word_count: 182
summary: This document defines the event schemas and trigger conditions for SIS import creation and state updates within the Canvas LMS platform.
tags:
    - canvas-lms
    - sis-import
    - event-metadata
    - workflow-state
    - batch-processing
    - api-integration
category: reference
---

**Definition:** The event is emitted when a new SIS import is created.

**Trigger:** Triggered when a user or API call imported a new SIS csv file.

```
{
"metadata":{
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs:canvas-lms",
"user_login":"mysisimporterlogin",
"user_account_id":"21070000000000001",
"user_sis_id":null,
"user_id":"21070000000000109",
"time_zone":"America/Chicago",
"developer_key_id":"170000000056",
"context_type":"Account",
"context_id":"21070000000000001",
"context_sis_source_id":null,
"context_account_id":"21070000000000001",
"context_role":"AccountAdmin",
"request_id":"a3f928df-a423-423d-123a-8200f9ab09c3",
"session_id":null,
"hostname":"oxana.instructure.com",
"http_method":"POST",
"user_agent":"python-requests/2.5.1",
"client_ip":"93.184.216.34",
"url":"https://oxana.instructure.com/api/v1/accounts/self/sis_imports.json?access_token=1398~agJdJdaSLJfJULBa2803dfLJAFdsklj349FADJSLdsaLFlJUBOAUO39289342FJj&import_type=ims_xml&extension=xml",
"referrer":null,
"producer":"canvas",
"event_name":"sis_batch_created",
"event_time":"2020-01-14T14:14:11.498Z"
},
"body":{
"sis_batch_id":"31048324",
"account_id":"1",
"workflow_state":"initializing"
}
}
```

The internal SIS import id.

The id of the Canvas account the SIS csv file is being imported to.

The status of the current SIS Import.

**Definition:** The event is emitted when a newly created SIS import status changes.

**Trigger:** Triggered when workflow\_state state changes for a newly created SIS import.

```
{
  "metadata": {
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs:canvas-lms",
    "user_login": "mysisimporterlogin",
    "user_account_id": "21070000000000001",
    "user_sis_id": null,
    "user_id": "21070000000000109",
    "time_zone": "America/Los_Angeles",
    "developer_key_id": "170000000056",
    "context_type": "Account",
    "context_id": "21070000000000001",
    "context_sis_source_id": null,
    "context_account_id": "21070000000000001",
    "context_role": "AccountAdmin",
    "request_id": "ab398133-5324-4234-b31b-419b8d9f1209",
    "session_id": null,
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "user_agent": "python-requests/2.5.1",
    "client_ip": "93.184.216.34",
    "url": "https://oxana.instructure.com/api/v1/accounts/1/sis_imports.json?import_type=instructure_csv&override_sis_stickiness=true&extension=csv",
    "referrer": null,
    "producer": "canvas",
    "event_name": "sis_batch_updated",
    "event_time": "2020-01-15T16:20:25.548Z"
  },
  "body": {
    "sis_batch_id": "1440004",
    "account_id": "1",
    "workflow_state": "created"
  }
}
```

The internal SIS import id.

The id of the Canvas account the SIS data is being imported to.

The status of the current SIS Import.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).