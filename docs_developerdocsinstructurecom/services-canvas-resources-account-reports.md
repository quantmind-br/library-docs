---
title: Account Reports | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/account_reports
source: sitemap
fetched_at: 2026-02-15T08:56:55.687349-03:00
rendered_js: false
word_count: 385
summary: This document outlines the Account Reports API, providing technical details on how to list available reports, generate new report instances, and retrieve the status or results of report processes.
tags:
    - canvas-lms
    - api-reference
    - account-reports
    - data-export
    - report-generation
    - rest-api
category: api
---

API for accessing account reports.

**A Report object looks like:**

```
{
  // The unique identifier for the report.
"id": 1,
  // The type of report.
"report": "sis_export_csv",
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
  // The time (in seconds) the report has been waiting to run, has been running so
  // far, or took to run to completion, depending on its current state.
"run_time": 33.3,
  // The report parameters
"parameters": {"course_id":2,"start_at":"2012-07-13T10:55:20-06:00","end_at":"2012-07-13T10:55:20-06:00"},
  // The progress of the report
"progress": 100,
  // This is the current line count being written to the report. It updates every
  // 1000 records.
"current_line": 12000,
  // The user that initiated the account report. See the Users API for details.
"user": null
}
```

**A ReportParameters object looks like:**

```
// The parameters returned will vary for each report.
{
  // The canvas id of the term to get grades from
  "enrollment_term_id": 2,
  // If true, deleted objects will be included. If false, deleted objects will be
  // omitted.
  "include_deleted": false,
  // The id of the course to report on
  "course_id": 2,
  // The sort order for the csv, Options: 'users', 'courses', 'outcomes'.
  "order": "users",
  // If true, user data will be included. If false, user data will be omitted.
  "users": false,
  // If true, account data will be included. If false, account data will be
  // omitted.
  "accounts": false,
  // If true, term data will be included. If false, term data will be omitted.
  "terms": false,
  // If true, course data will be included. If false, course data will be omitted.
  "courses": false,
  // If true, section data will be included. If false, section data will be
  // omitted.
  "sections": false,
  // If true, enrollment data will be included. If false, enrollment data will be
  // omitted.
  "enrollments": false,
  // If true, group data will be included. If false, group data will be omitted.
  "groups": false,
  // If true, data for crosslisted courses will be included. If false, data for
  // crosslisted courses will be omitted.
  "xlist": false,
  "sis_terms_csv": 1,
  "sis_accounts_csv": 1,
  // If true, enrollment state will be included. If false, enrollment state will
  // be omitted. Defaults to false.
  "include_enrollment_state": false,
  // Include enrollment state. Defaults to 'all' Options: ['active'| 'invited'|
  // 'creation_pending'| 'deleted'| 'rejected'| 'completed'| 'inactive'| 'all']
  "enrollment_state": ["all"],
  // The beginning date for submissions. Max time range is 2 weeks.
  "start_at": "2012-07-13T10:55:20-06:00",
  // The end date for submissions. Max time range is 2 weeks.
  "end_at": "2012-07-13T10:55:20-06:00"
}
```

[AccountReportsController#available\_reportsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

`GET /api/v1/accounts/:account_id/reports`

**Scope:** `url:GET|/api/v1/accounts/:account_id/reports`

Returns a paginated list of reports for the current context.

**Request Parameters:**

Array of additional information to include.

- “description\_html”
  
  an HTML description of the report, with example output
- “parameters\_html”
  
  an HTML form for the report parameters

Allowed values: `description_html`, `params_html`

**API response field:**

The name of the report.

The parameters will vary for each report

- Report
  
  The last run of the report. This will be null if the report has never been run.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/accounts/<account_id>/reports/
```

**Example Response:**

```
[
  {
    "report":"student_assignment_outcome_map_csv",
    "title":"Student Competency",
    "parameters":null,
    "last_run": {
      "id": 1,
      "report": "student_assignment_outcome_map_csv",
      "file_url": "https://example.com/some/path",
      "status": "complete",
      "created_at": "2013-12-01T23:59:00-06:00",
      "started_at": "2013-12-02T00:03:21-06:00",
      "ended_at": "2013-12-02T00:03:21-06:00"
  },
  {
    "report":"grade_export_csv",
    "title":"Grade Export",
    "parameters":{
      "term":{
        "description":"The canvas id of the term to get grades from",
        "required":true
      }
    },
    "last_run": null
  }
]
```

[AccountReportsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

`POST /api/v1/accounts/:account_id/reports/:report`

**Scope:** `url:POST|/api/v1/accounts/:account_id/reports/:report`

Generates a report instance for the account. Note that “report” in the request must match one of the available report names. To fetch a list of available report names and parameters for each report (including whether or not those parameters are required), see [List Available Reports](https://developerdocs.instructure.com/services/canvas/resources/account_reports#method.account_reports.available_reports).

**Request Parameters:**

The parameters will vary for each report. To fetch a list of available parameters for each report, see [List Available Reports](https://developerdocs.instructure.com/services/canvas/resources/account_reports#method.account_reports.available_reports). A few example parameters have been provided below. Note that the example parameters provided below may not be valid for every report.

If true, no message will be sent to the user upon completion of the report.

The id of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report.

If true, user data will be included. If false, user data will be omitted. Note: this parameter has been listed to serve as an example and may not be valid for every report.

**Example Request:**

```
curl -X POST \
     https://<canvas>/api/v1/accounts/1/reports/provisioning_csv \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: multipart/form-data' \
     -F 'parameters[users]=true' \
     -F 'parameters[courses]=true' \
     -F 'parameters[enrollments]=true'
```

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

[AccountReportsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

`GET /api/v1/accounts/:account_id/reports/:report`

**Scope:** `url:GET|/api/v1/accounts/:account_id/reports/:report`

Shows all reports that have been run for the account of a specific type.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>
```

Returns a list of [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) objects.

[AccountReportsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

`GET /api/v1/accounts/:account_id/reports/:report/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/reports/:report/:id`

Returns the status of a report.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>/<report_id>
```

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

[AccountReportsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

`DELETE /api/v1/accounts/:account_id/reports/:report/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/reports/:report/:id`

Deletes a generated report instance.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     -X DELETE \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>/<id>
```

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

[AccountReportsController#abortarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/account_reports_controller.rb)

`PUT /api/v1/accounts/:account_id/reports/:report/:id/abort`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/reports/:report/:id/abort`

Abort a report in progress

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     -X PUT \
     https://<canvas>/api/v1/accounts/<account_id>/reports/<report_type>/<id>/abort
```

Returns a [Report](https://developerdocs.instructure.com/services/canvas/resources/course_reports#report) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).