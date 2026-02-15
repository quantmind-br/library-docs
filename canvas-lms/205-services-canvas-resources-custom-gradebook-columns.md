---
title: Custom Gradebook Columns | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns
source: sitemap
fetched_at: 2026-02-15T09:07:16.761983-03:00
rendered_js: false
word_count: 331
summary: This document outlines the API endpoints for managing custom gradebook columns and their associated data within the Canvas LMS, including operations for creating, updating, reordering, and deleting columns.
tags:
    - canvas-lms
    - gradebook-api
    - custom-columns
    - rest-api
    - lms-integration
category: api
---

## Custom Gradebook Columns API

API for adding additional columns to the gradebook. Custom gradebook columns will be displayed with the other frozen gradebook columns.

**A CustomColumn object looks like:**

```
{
  // The ID of the custom gradebook column
"id": 2,
  // When true, this column's visibility will be toggled in the Gradebook when a
  // user selects to show or hide notes
"teacher_notes": false,
  // header text
"title": "Stuff",
  // column order
"position": 1,
  // won't be displayed if hidden is true
"hidden": false,
  // won't be editable in the gradebook UI
"read_only": true
}
```

**A ColumnDatum object looks like:**

```
// ColumnDatum objects contain the entry for a column for each user.
{
  "content": "Nut allergy",
  "user_id": 2
}
```

[CustomGradebookColumnsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_columns_api_controller.rb)

`GET /api/v1/courses/:course_id/custom_gradebook_columns`

**Scope:** `url:GET|/api/v1/courses/:course_id/custom_gradebook_columns`

A paginated list of all custom gradebook columns for a course

**Request Parameters:**

Include hidden parameters (defaults to false)

Returns a list of [CustomColumn](https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns#customcolumn) objects.

[CustomGradebookColumnsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_columns_api_controller.rb)

`POST /api/v1/courses/:course_id/custom_gradebook_columns`

**Scope:** `url:POST|/api/v1/courses/:course_id/custom_gradebook_columns`

Create a custom gradebook column

**Request Parameters:**

The position of the column relative to other custom columns

Hidden columns are not displayed in the gradebook

Set this if the column is created by a teacher. The gradebook only supports one teacher\_notes column.

Set this to prevent the column from being editable in the gradebook ui

Returns a [CustomColumn](https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns#customcolumn) object.

[CustomGradebookColumnsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_columns_api_controller.rb)

`PUT /api/v1/courses/:course_id/custom_gradebook_columns/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/custom_gradebook_columns/:id`

Accepts the same parameters as custom gradebook column creation

Returns a [CustomColumn](https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns#customcolumn) object.

[CustomGradebookColumnsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_columns_api_controller.rb)

`DELETE /api/v1/courses/:course_id/custom_gradebook_columns/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/custom_gradebook_columns/:id`

Permanently deletes a custom column and its associated data

Returns a [CustomColumn](https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns#customcolumn) object.

[CustomGradebookColumnsApiController#reorderarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_columns_api_controller.rb)

`POST /api/v1/courses/:course_id/custom_gradebook_columns/reorder`

**Scope:** `url:POST|/api/v1/courses/:course_id/custom_gradebook_columns/reorder`

Puts the given columns in the specified order

**200 OK** is returned if successful

**Request Parameters:**

[CustomGradebookColumnDataApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_column_data_api_controller.rb)

`GET /api/v1/courses/:course_id/custom_gradebook_columns/:id/data`

**Scope:** `url:GET|/api/v1/courses/:course_id/custom_gradebook_columns/:id/data`

This does not list entries for students without associated data.

**Request Parameters:**

If true, hidden columns will be included in the result. If false or absent, only visible columns will be returned.

Returns a list of [ColumnDatum](https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns#columndatum) objects.

[CustomGradebookColumnDataApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_column_data_api_controller.rb)

`PUT /api/v1/courses/:course_id/custom_gradebook_columns/:id/data/:user_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/custom_gradebook_columns/:id/data/:user_id`

Set the content of a custom column

**Request Parameters:**

Column content. Setting this to blank will delete the datum object.

Returns a [ColumnDatum](https://developerdocs.instructure.com/services/canvas/resources/custom_gradebook_columns#columndatum) object.

[CustomGradebookColumnDataApiController#bulk\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/custom_gradebook_column_data_api_controller.rb)

`PUT /api/v1/courses/:course_id/custom_gradebook_column_data`

**Scope:** `url:PUT|/api/v1/courses/:course_id/custom_gradebook_column_data`

Set the content of custom columns

{

```
"column_data": [
  {
    "column_id": example_column_id,
    "user_id": example_student_id,
    "content": example_content
    },
    {
    "column_id": example_column_id,
    "user_id": example_student_id,
    "content: example_content
  }
]
```

}

**Request Parameters:**

Column content. Setting this to an empty string will delete the data object.

**Example Request:**

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).