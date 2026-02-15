---
title: Content | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/data-services/live-events/event-format/canvas/file.data_service_canvas_content
source: sitemap
fetched_at: 2026-02-15T09:06:04.638677-03:00
rendered_js: false
word_count: 214
summary: This document defines the schema and trigger conditions for the content_migration_completed event, which is emitted when a content migration request is finished in Canvas LMS.
tags:
    - canvas-lms
    - content-migration
    - event-streaming
    - api-reference
    - webhook-events
category: reference
---

### content\_migration\_completed

**Definition:** The event is emitted anytime a content migration request is completed.

**Trigger:** Triggered anytime a content migration request is completed.

```
{
"metadata":{
"context_id":"21070000000008972",
"context_type":"Course",
"event_name":"content_migration_completed",
"event_time":"2019-11-01T19:11:02.024Z",
"job_id":"1020020528469291",
"job_tag":"ContentMigration#import_content",
"producer":"canvas",
"root_account_id":"21070000000000001",
"root_account_lti_guid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs.oxana.instructure.com",
"root_account_uuid":"VicYj3cu5BIFpoZhDVU4DZumnlBrWi1grgJEzADs"
},
"body":{
"content_migration_id":"21070000000000072",
"context_id":"21070000000008972",
"context_type":"Course",
"context_uuid":"Uc69p8GCYLMYWQJqkyzQGqg1kNMXbmnRl8qdCJge",
"import_quizzes_next":false,
"lti_context_id":"694d2e30346f6a94ad20cea11ce78d19bd849c9c",
"source_course_lti_id":"38ab9de0f0bc8e8e0889432275420de08f0d8380",
"destination_course_lti_id":"694d2e30346f6a94ad20cea11ce78d19bd849c9c",
"migration_type":"course_copy_importer",
"domain":"oxana.instructure.com"
}
}
```

The Canvas id of the content migration.

The Canvas id of the context associated with the content migration.

The type of context associated with the content migration.

The uuid of the context associated with the content migration.

Indicates whether the user requested that the quizzes in the content migration be created in Quizzes.Next (true) or in native Canvas (false).

The lti context id of the context associated with the content migration.

The lti context id of the the source course, if applicable.

**destination\_course\_lti\_id**

Alias for lti\_context\_id.

The migration type. Examples include: academic\_benchmark\_importer, angel\_exporter, blackboard\_exporter, canvas\_cartridge\_importer, common\_cartridge\_importer, course\_copy\_importer, d2l\_exporter, master\_course\_import, moodle\_converter, qti\_converter, webct\_scraper, zip\_file\_importer, context\_external\_tool\_1234.

The default hostname for the Canvas root account.

Note: Timestamps will be in ISO8601 format, including an offset. Be sure to take that into account when parsing, since it’s unspecified which offset timestamps will use, and the offset may even change between different timestamps within a single event.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).