---
title: Course Reports | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/course_reports
source: sitemap
fetched_at: 2026-02-15T09:07:14.758308-03:00
rendered_js: false
word_count: 197
summary: This document outlines the API endpoints for managing course reports, including methods for generating new report instances and checking the status of existing or recent reports. It defines the schema for report objects and details the parameters required for various report types.
tags:
    - canvas-lms
    - course-reports
    - api-documentation
    - rest-api
    - report-generation
    - data-extraction
category: api
---

API for accessing course reports.

**A Report object looks like:**

```
{
  // The unique identifier for the report.
"id": 1,
  // The url to the report download.
"file_url": "https://example.com/some/path",
  // The attachment api object of the report. Only available after the report has
  // completed.
"attachment": null,
  // The status of the report
"status": "complete",
  // The date and time the report was created.
"created_at": "2013-12-01T23:59:00-06:00",
  // The date and time the report started processing.
"started_at": "2013-12-02T00:03:21-06:00",
  // The date and time the report finished processing.
"ended_at": "2013-12-02T00:03:21-06:00",
  // The report parameters
"parameters": {"course_id":2,"start_at":"2012-07-13T10:55:20-06:00","end_at":"2012-07-13T10:55:20-06:00"},
  // The progress of the report
"progress": 100
}
```

**A ReportParameters object looks like:**

```
// The parameters returned will vary for each report.
{

}
```

[CourseReportsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_reports_controller.rb)

`GET /api/v1/courses/:course_id/reports/:report_type/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/reports/:report_type/:id`

Returns the status of a report.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/<course_id>/reports/<report_type>/<report_id>
```

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

[CourseReportsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_reports_controller.rb)

`POST /api/v1/courses/:course_id/reports/:report_type`

**Scope:** `url:POST|/api/v1/courses/:course_id/reports/:report_type`

Generates a report instance for the account. Note that “report” in the request must match one of the available report names.

**Request Parameters:**

The id of the course to report on.

The type of report to generate.

The parameters will vary for each report. A few example parameters have been provided below. Note: the example parameters provided below may not be valid for every report.

`parameters[section_ids[]]`

The sections of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report.

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

[CourseReportsController#lastarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/course_reports_controller.rb)

`GET /api/v1/courses/:course_id/reports/:report_type`

**Scope:** `url:GET|/api/v1/courses/:course_id/reports/:report_type`

Returns the status of the last report initiated by the current user.

**Example Request:**

```
curl-H'Authorization: Bearer <token>'\
https://<canvas>/api/v1/courses/<course_id>/reports/<report_type>
```

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).