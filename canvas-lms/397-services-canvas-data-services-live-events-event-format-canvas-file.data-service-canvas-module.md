---
title: Module | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_module
source: sitemap
fetched_at: 2026-02-15T09:06:29.000304-03:00
rendered_js: false
word_count: 382
summary: This document defines the technical specifications and payload schemas for Canvas LMS event notifications related to the creation and modification of course modules and module items.
tags:
    - canvas-lms
    - event-streaming
    - api-reference
    - module-management
    - json-schema
    - webhooks
category: reference
---

**Definition:** The event is emitted anytime a new module is created by an end user or API request.

**Trigger:** Triggered when a new module is created.

```
{
"metadata":{
"event_name":"module_created",
"event_time":"2019-11-01T19:11:05.880Z",
"job_id":"1020020528469291",
"job_tag":"CC::Importer::CCWorker#perform",
"producer":"canvas",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
},
"body":{
"context_id":"1234560",
"context_type":"Course",
"module_id":"1234567",
"name":"Module 3",
"position":101,
"workflow_state":"active"
}
}
```

The local Canvas id of the context.

The type of module's context.

The Canvas id of the module.

The position of the module in the course.

The workflow state of the module.

**Definition:** The event is emitted anytime a new module item is added to a module by an end user or API request.

**Trigger:** Triggered when a new module item is created.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "developer_key_id": "170000000056",
    "event_name": "module_item_created",
    "event_time": "2019-11-01T19:11:07.287Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": null,
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/New_York",
    "url": "https://oxana.instructure.com/api/v1/courses/sis_course_id:syllabus-registry-F9-HSS/modules/61660/items",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "context_id": "565",
    "context_type": "Course",
    "module_id": "14",
    "module_item_id": "19587",
    "position": 1,
    "workflow_state": "active"
  }
}
```

The local Canvas id of the context.

The type of module's context, usually "Course".

The Canvas id of the module.

The Canvas id of the module item.

The position of the module item in the module.

The workflow state of the module item.

**Definition:** The event is emitted anytime a module item is updated in a module by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when a new module item is updated.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "TeacherEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "module_item_updated",
    "event_time": "2019-11-01T19:11:01.676Z",
    "hostname": "oxana.instructure.com",
    "http_method": "PUT",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/565/modules",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/Chicago",
    "url": "https://oxana.instructure.com/api/v1/courses/565/modules/14/items/19587",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "context_id": "565",
    "context_type": "Course",
    "module_id": "14",
    "module_item_id": "19587",
    "position": 1,
    "workflow_state": "active"
  }
}
```

The local Canvas id of the context.

The type of module's context.

The Canvas id of the module.

The Canvas id of the module item.

The position of the module item in the module.

The workflow state of the module item (active, deleted, unpublished).

**Definition:** The event is emitted anytime a module is updated by an end user or API request. Only changes to the fields included in the body of the event payload will emit the `updated` event.

**Trigger:** Triggered when a new module is updated.

```
{
  "metadata": {
    "client_ip": "93.184.216.34",
    "context_account_id": "21070000000000079",
    "context_id": "21070000000000565",
    "context_role": "TeacherEnrollment",
    "context_sis_source_id": "2017.100.101.101-1",
    "context_type": "Course",
    "event_name": "module_updated",
    "event_time": "2019-11-01T19:11:03.000Z",
    "hostname": "oxana.instructure.com",
    "http_method": "POST",
    "producer": "canvas",
    "referrer": "https://oxana.instructure.com/courses/565/modules",
    "request_id": "1dd9dc6f-2fb0-4c19-a6c5-7ee1bf3ed295",
    "root_account_id": "21070000000000001",
    "root_account_lti_guid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
    "root_account_uuid": "VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs",
    "session_id": "ef686f8ed684abf78cbfa1f6a58112b5",
    "time_zone": "America/New_York",
    "url": "https://oxana.instructure.com/courses/565/modules/reorder",
    "user_account_id": "21070000000000001",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "user_id": "21070000000000001",
    "user_login": "oxana@example.com",
    "user_sis_id": "456-T45"
  },
  "body": {
    "context_id": "565",
    "context_type": "Course",
    "module_id": "14",
    "name": "Module 4",
    "position": 3,
    "workflow_state": "unpublished"
  }
}
```

The local Canvas id of the context.

The type of module's context.

The Canvas id of the module.

The position of the module in the course.

The workflow state of the module (active, deleted, unpublished).

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).