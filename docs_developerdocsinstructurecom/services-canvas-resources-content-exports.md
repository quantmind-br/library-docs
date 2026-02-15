---
title: Content Exports | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/content_exports
source: sitemap
fetched_at: 2026-02-15T08:59:38.339828-03:00
rendered_js: false
word_count: 348
summary: This document details the Canvas LMS API endpoints for creating, listing, and retrieving content exports for courses, groups, and users.
tags:
    - canvas-lms
    - content-exports
    - api-reference
    - common-cartridge
    - qti
    - data-export
category: api
---

API for exporting courses and course content

**A ContentExport object looks like:**

```
{
  // the unique identifier for the export
"id": 101,
  // the date and time this export was requested
"created_at": "2014-01-01T00:00:00Z",
  // the type of content migration: 'common_cartridge' or 'qti'
"export_type": "common_cartridge",
  // attachment api object for the export package (not present before the export
  // completes or after it becomes unavailable for download.)
"attachment": {"url":"https:\/\/example.com\/api\/v1\/attachments\/789?download_frd=1"},
  // The api endpoint for polling the current progress
"progress_url": "https://example.com/api/v1/progress/4",
  // The ID of the user who started the export
"user_id": 4,
  // Current state of the content migration: created exporting exported failed
"workflow_state": "exported"
}
```

[ContentExportsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb)

`GET /api/v1/courses/:course_id/content_exports`

**Scope:** `url:GET|/api/v1/courses/:course_id/content_exports`

`GET /api/v1/groups/:group_id/content_exports`

**Scope:** `url:GET|/api/v1/groups/:group_id/content_exports`

`GET /api/v1/users/:user_id/content_exports`

**Scope:** `url:GET|/api/v1/users/:user_id/content_exports`

A paginated list of the past and pending content export jobs for a course, group, or user. Exports are returned newest first.

Returns a list of [ContentExport](https://developerdocs.instructure.com/services/canvas/resources/content_exports#contentexport) objects.

[ContentExportsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb)

`GET /api/v1/courses/:course_id/content_exports/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/content_exports/:id`

`GET /api/v1/groups/:group_id/content_exports/:id`

**Scope:** `url:GET|/api/v1/groups/:group_id/content_exports/:id`

`GET /api/v1/users/:user_id/content_exports/:id`

**Scope:** `url:GET|/api/v1/users/:user_id/content_exports/:id`

Get information about a single content export.

Returns a [ContentExport](https://developerdocs.instructure.com/services/canvas/resources/content_exports#contentexport) object.

[ContentExportsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_exports_api_controller.rb)

`POST /api/v1/courses/:course_id/content_exports`

**Scope:** `url:POST|/api/v1/courses/:course_id/content_exports`

`POST /api/v1/groups/:group_id/content_exports`

**Scope:** `url:POST|/api/v1/groups/:group_id/content_exports`

`POST /api/v1/users/:user_id/content_exports`

**Scope:** `url:POST|/api/v1/users/:user_id/content_exports`

Begin a content export job for a course, group, or user.

You can use the [Progress API](https://developerdocs.instructure.com/services/canvas/resources/progress#method.progress.show) to track the progress of the export. The migration’s progress is linked to with the *progress\_url* value.

When the export completes, use the [Show content export](https://developerdocs.instructure.com/services/canvas/resources/content_exports#method.content_exports_api.show) endpoint to retrieve a download URL for the exported content.

**Request Parameters:**

- “common\_cartridge”
  
  Export the contents of the course in the Common Cartridge (.imscc) format
- “qti”
  
  Export quizzes from a course in the QTI format
- “zip”
  
  Export files from a course, group, or user in a zip file

Allowed values: `common_cartridge`, `qti`, `zip`

Don’t send the notifications about the export to the user. Default: false

The select parameter allows exporting specific data. The keys are object types like ‘files’, ‘folders’, ‘pages’, etc. The value for each key is a list of object ids. An id can be an integer or a string.

Multiple object types can be selected in the same call. However, not all object types are valid for every export\_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described below.

- “folders”
  
  Also supported for zip export\_type.
- “files”
  
  Also supported for zip export\_type.
- “quizzes”
  
  Also supported for qti export\_type.

Allowed values: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics`

Returns a [ContentExport](https://developerdocs.instructure.com/services/canvas/resources/content_exports#contentexport) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).