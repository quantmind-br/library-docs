---
title: ePub Exports | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/e_pub_exports
source: sitemap
fetched_at: 2026-02-15T09:00:23.663672-03:00
rendered_js: false
word_count: 165
summary: This document defines the endpoints and data models for exporting Canvas LMS courses as ePub files, including methods to list, create, and track export progress.
tags:
    - canvas-lms
    - epub-export
    - api-endpoints
    - course-management
    - content-export
category: api
---

API for exporting courses as an ePub

**A CourseEpubExport object looks like:**

```
// Combination of a Course & EpubExport.
{
  // the unique identifier for the course
"id": 101,
  // the name for the course
"name": "Maths 101",
  // ePub export API object
"epub_export": null
}
```

**An EpubExport object looks like:**

```
{
  // the unique identifier for the export
"id": 101,
  // the date and time this export was requested
"created_at": "2014-01-01T00:00:00Z",
  // attachment api object for the export ePub (not present until the export
  // completes)
"attachment": {"url":"https:\/\/example.com\/api\/v1\/attachments\/789?download_frd=1"},
  // The api endpoint for polling the current progress
"progress_url": "https://example.com/api/v1/progress/4",
  // The ID of the user who started the export
"user_id": 4,
  // Current state of the ePub export: created exporting exported generating
  // generated failed
"workflow_state": "exported"
}
```

[EpubExportsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/epub_exports_controller.rb)

`GET /api/v1/epub_exports`

**Scope:** `url:GET|/api/v1/epub_exports`

A paginated list of all courses a user is actively participating in, and the latest ePub export associated with the user & course.

Returns a list of [CourseEpubExport](https://developerdocs.instructure.com/services/canvas/resources/e_pub_exports#courseepubexport) objects.

[EpubExportsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/epub_exports_controller.rb)

`POST /api/v1/courses/:course_id/epub_exports`

**Scope:** `url:POST|/api/v1/courses/:course_id/epub_exports`

Begin an ePub export for a course.

You can use the [Progress API](https://developerdocs.instructure.com/services/canvas/resources/progress#method.progress.show) to track the progress of the export. The export’s progress is linked to with the *progress\_url* value.

When the export completes, use the [Show content export](https://developerdocs.instructure.com/services/canvas/resources/e_pub_exports#method.epub_exports.show) endpoint to retrieve a download URL for the exported content.

Returns an [EpubExport](https://developerdocs.instructure.com/services/canvas/resources/e_pub_exports#epubexport) object.

[EpubExportsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/epub_exports_controller.rb)

`GET /api/v1/courses/:course_id/epub_exports/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/epub_exports/:id`

Get information about a single ePub export.

Returns an [EpubExport](https://developerdocs.instructure.com/services/canvas/resources/e_pub_exports#epubexport) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).