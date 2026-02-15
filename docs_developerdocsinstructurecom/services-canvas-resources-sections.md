---
title: Sections | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/sections
source: sitemap
fetched_at: 2026-02-15T08:56:19.767815-03:00
rendered_js: false
word_count: 710
summary: Technical documentation for the Sections API, detailing endpoints for creating, updating, retrieving, and cross-listing course sections within the Canvas LMS.
tags:
    - canvas-lms
    - sections-api
    - rest-api
    - course-management
    - sis-integration
    - cross-listing
category: api
---

API for accessing section information.

**A Section object looks like:**

```
{
  // The unique identifier for the section.
"id": 1,
  // The name of the section.
"name": "Section A",
  // The sis id of the section. This field is only included if the user has
  // permission to view SIS information.
"sis_section_id": "s34643",
  // Optional: The integration ID of the section. This field is only included if
  // the user has permission to view SIS information.
"integration_id": "3452342345",
  // The unique identifier for the SIS import if created through SIS. This field
  // is only included if the user has permission to manage SIS information.
"sis_import_id": 47,
  // The unique Canvas identifier for the course in which the section belongs
"course_id": 7,
  // The unique SIS identifier for the course in which the section belongs. This
  // field is only included if the user has permission to view SIS information.
"sis_course_id": "7",
  // the start date for the section, if applicable
"start_at": "2012-06-01T00:00:00-06:00",
  // the end date for the section, if applicable
"end_at": null,
  // Restrict user enrollments to the start and end dates of the section
"restrict_enrollments_to_section_dates": null,
  // The unique identifier of the original course of a cross-listed section
"nonxlist_course_id": null,
  // optional: the total number of active and invited students in the section
"total_students": 13,
  // optional: A list of students that are included in the section. Returned only
  // if include[]=students. WARNING: this collection's size is capped (if there
  // are an extremely large number of users in the section (thousands) not all of
  // them will be returned). If you need to capture all the users in a section
  // with certainty or experiencing slow response consider using the paginated
  // /api/v1/sections/<section_id>/users endpoint.
"students": null
}
```

[SectionsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`GET /api/v1/courses/:course_id/sections`

**Scope:** `url:GET|/api/v1/courses/:course_id/sections`

A paginated list of the list of sections for this course.

**Request Parameters:**

- “students”: Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course
- “avatar\_url”: Include the avatar URLs for students returned.
- “enrollments”: If ‘students’ is also included, return the section enrollment for each student
- “total\_students”: Returns the total amount of active and invited students for the course section
- “passback\_status”: Include the grade passback status.
- “permissions”: Include whether section grants :manage\_calendar permission to the caller

Allowed values: `students`, `avatar_url`, `enrollments`, `total_students`, `passback_status`, `permissions`

When included, searches course sections for the term. Returns only matching results. Term must be at least 2 characters.

Returns a list of [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) objects.

[SectionsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`POST /api/v1/courses/:course_id/sections`

**Scope:** `url:POST|/api/v1/courses/:course_id/sections`

Creates a new section for this course.

**Request Parameters:**

`course_section[sis_section_id]`

The sis ID of the section. Must have manage\_sis permission to set. This is ignored if caller does not have permission to set.

`course_section[integration_id]`

The integration\_id of the section. Must have manage\_sis permission to set. This is ignored if caller does not have permission to set.

Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z

Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z

`course_section[restrict_enrollments_to_section_dates]`

Set to true to restrict user enrollments to the start and end dates of the section.

When true, will first try to re-activate a deleted section with matching sis\_section\_id if possible.

Returns a [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) object.

[SectionsController#crosslistarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`POST /api/v1/sections/:id/crosslist/:new_course_id`

**Scope:** `url:POST|/api/v1/sections/:id/crosslist/:new_course_id`

Move the Section to another course. The new course may be in a different account (department), but must belong to the same root account (institution).

**Request Parameters:**

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

Returns a [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) object.

[SectionsController#uncrosslistarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`DELETE /api/v1/sections/:id/crosslist`

**Scope:** `url:DELETE|/api/v1/sections/:id/crosslist`

Undo cross-listing of a Section, returning it to its original course.

**Request Parameters:**

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

Returns a [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) object.

[SectionsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`PUT /api/v1/sections/:id`

**Scope:** `url:PUT|/api/v1/sections/:id`

Modify an existing section.

**Request Parameters:**

`course_section[sis_section_id]`

The sis ID of the section. Must have manage\_sis permission to set.

`course_section[integration_id]`

The integration\_id of the section. Must have manage\_sis permission to set.

Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z

Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z

`course_section[restrict_enrollments_to_section_dates]`

Set to true to restrict user enrollments to the start and end dates of the section.

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

Returns a [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) object.

[SectionsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`GET /api/v1/courses/:course_id/sections/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/sections/:id`

`GET /api/v1/sections/:id`

**Scope:** `url:GET|/api/v1/sections/:id`

Gets details about a specific section

**Request Parameters:**

- “students”: Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course
- “avatar\_url”: Include the avatar URLs for students returned.
- “enrollments”: If ‘students’ is also included, return the section enrollment for each student
- “total\_students”: Returns the total amount of active and invited students for the course section
- “passback\_status”: Include the grade passback status.
- “permissions”: Include whether section grants :manage\_calendar permission to the caller

Allowed values: `students`, `avatar_url`, `enrollments`, `total_students`, `passback_status`, `permissions`

Returns a [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) object.

[SectionsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`DELETE /api/v1/sections/:id`

**Scope:** `url:DELETE|/api/v1/sections/:id`

Delete an existing section. Returns the former Section.

Returns a [Section](https://developerdocs.instructure.com/services/canvas/resources/sections#section) object.

[SectionsController#usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sections_controller.rb)

`GET /api/v1/sections/:id/users`

**Scope:** `url:GET|/api/v1/sections/:id/users`

Returns a paginated list of users in the section.

**Request Parameters:**

The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters.

“avatar\_url”: Include users’ avatar\_urls.

Allowed values: `avatar_url`

Whether to filter out inactive users from the results. Defaults to false unless explicitly provided.

When set, only return users with the specified enrollment type for the given section.

Allowed values: `teacher`, `student`, `ta`, `observer`, `designer`

**Example Request:**

```
curlhttps://<canvas>/api/v1/sections/1/users\
-H'Authorization: Bearer <token>'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).