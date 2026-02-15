---
title: SIS Import Errors | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/sis_import_errors
source: sitemap
fetched_at: 2026-02-15T09:08:25.450279-03:00
rendered_js: false
word_count: 100
summary: Describes the SisImportError object structure and the API endpoints used to retrieve error logs for SIS imports in Canvas LMS.
tags:
    - canvas-lms
    - sis-import
    - api-reference
    - error-reporting
    - sis
category: api
---

**A SisImportError object looks like:**

```
{
  // The unique identifier for the SIS import.
"sis_import_id": 1,
  // The file where the error message occurred.
"file": "courses.csv",
  // The error message that from the record.
"message": "No short_name given for course C001",
  // The contents of the line that had the error.
"row_info": "account_1, Sub account 1,, active ",
  // The line number where the error occurred. Some Importers do not yet support
  // this. This is a 1 based index starting with the header row.
"row": 34
}
```

[SisImportErrorsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sis_import_errors_api_controller.rb)

`GET /api/v1/accounts/:account_id/sis_imports/:id/errors`

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_imports/:id/errors`

`GET /api/v1/accounts/:account_id/sis_import_errors`

**Scope:** `url:GET|/api/v1/accounts/:account_id/sis_import_errors`

Returns the list of SIS import errors for an account or a SIS import. Import errors are only stored for 30 days.

Example:

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
  -H "Authorization: Bearer <token>"
```

Example:

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
  -H "Authorization: Bearer <token>"
```

**Request Parameters:**

If set, only shows errors on a sis import that would cause a failure.

Returns a list of [SisImportError](https://developerdocs.instructure.com/services/canvas/resources/sis_import_errors#sisimporterror) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).