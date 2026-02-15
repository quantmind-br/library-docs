---
title: Courses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/courses
source: sitemap
fetched_at: 2026-02-15T08:57:34.847812-03:00
rendered_js: false
word_count: 5623
summary: This document defines the data structures and API endpoint for retrieving course-related information, including course progress, term details, and paginated lists of courses.
tags:
    - api-reference
    - course-management
    - data-models
    - canvas-lms
    - rest-api
    - enrollment-status
category: api
---

API for accessing course information.

**A Term object looks like:**

```
{
"id": 1,
"name": "Default Term",
"start_at": "2012-06-01T00:00:00-06:00",
"end_at": null
}
```

**A CourseProgress object looks like:**

```
{
  // total number of requirements from all modules
"requirement_count": 10,
  // total number of requirements the user has completed from all modules
"requirement_completed_count": 1,
  // url to next module item that has an unmet requirement. null if the user has
  // completed the course or the current module does not require sequential
  // progress
"next_requirement_url": "http://localhost/courses/1/modules/items/2",
  // date the course was completed. null if the course has not been completed by
  // this user
"completed_at": "2013-06-01T00:00:00-06:00"
}
```

**A Course object looks like:**

```
{
  // the unique identifier for the course
  "id": 370663,
  // the SIS identifier for the course, if defined. This field is only included if
  // the user has permission to view SIS information.
  "sis_course_id": null,
  // the UUID of the course
  "uuid": "WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5",
  // the integration identifier for the course, if defined. This field is only
  // included if the user has permission to view SIS information.
  "integration_id": null,
  // the unique identifier for the SIS import. This field is only included if the
  // user has permission to manage SIS information.
  "sis_import_id": 34,
  // the full name of the course. If the requesting user has set a nickname for
  // the course, the nickname will be shown here.
  "name": "InstructureCon 2012",
  // the course code
  "course_code": "INSTCON12",
  // the actual course name. This field is returned only if the requesting user
  // has set a nickname for the course.
  "original_name": "InstructureCon-2012-01",
  // the current state of the course, also known as ‘status’.  The value will be
  // one of the following values: 'unpublished', 'available', 'completed', or
  // 'deleted'.  NOTE: When fetching a singular course that has a 'deleted'
  // workflow state value, an error will be returned with a message of 'The
  // specified resource does not exist.'
  "workflow_state": "available",
  // the account associated with the course
  "account_id": 81259,
  // the root account associated with the course
  "root_account_id": 81259,
  // the enrollment term associated with the course
  "enrollment_term_id": 34,
  // A list of grading periods associated with the course
  "grading_periods": null,
  // the grading standard associated with the course
  "grading_standard_id": 25,
  // the grade_passback_setting set on the course
  "grade_passback_setting": "nightly_sync",
  // the date the course was created.
  "created_at": "2012-05-01T00:00:00-06:00",
  // the start date for the course, if applicable
  "start_at": "2012-06-01T00:00:00-06:00",
  // the end date for the course, if applicable
  "end_at": "2012-09-01T00:00:00-06:00",
  // the course-set locale, if applicable
  "locale": "en",
  // A list of enrollments linking the current user to the course. for student
  // enrollments, grading information may be included if include[]=total_scores
  "enrollments": null,
  // optional: the total number of active and invited students in the course
  "total_students": 32,
  // course calendar
  "calendar": null,
  // the type of page that users will see when they first visit the course -
  // 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules':
  // Course Modules/Sections Page - 'assignments': Course Assignments List -
  // 'syllabus': Course Syllabus Page other types may be added in the future
  "default_view": "feed",
  // optional: user-generated HTML for the course syllabus
  "syllabus_body": "<p>syllabus html goes here</p>",
  // optional: the number of submissions needing grading returned only if the
  // current user has grading rights and include[]=needs_grading_count
  "needs_grading_count": 17,
  // optional: the enrollment term object for the course returned only if
  // include[]=term
  "term": null,
  // optional: information on progress through the course returned only if
  // include[]=course_progress
  "course_progress": null,
  // weight final grade based on assignment group percentages
  "apply_assignment_group_weights": true,
  // optional: the permissions the user has for the course. returned only for a
  // single course and include[]=permissions
  "permissions": {"create_discussion_topic":true,"create_announcement":true},
  "is_public": true,
  "is_public_to_auth_users": true,
  "public_syllabus": true,
  "public_syllabus_to_auth": true,
  // optional: the public description of the course
  "public_description": "Come one, come all to InstructureCon 2012!",
  "storage_quota_mb": 5,
  "storage_quota_used_mb": 5,
  "hide_final_grades": false,
  "license": "Creative Commons",
  "allow_student_assignment_edits": false,
  "allow_wiki_comments": false,
  "allow_student_forum_attachments": false,
  "open_enrollment": true,
  "self_enrollment": false,
  "restrict_enrollments_to_course_dates": false,
  "course_format": "online",
  // optional: this will be true if this user is currently prevented from viewing
  // the course because of date restriction settings
  "access_restricted_by_date": false,
  // The course's IANA time zone name.
  "time_zone": "America/Denver",
  // optional: whether the course is set as a Blueprint Course (blueprint fields
  // require the Blueprint Courses feature)
  "blueprint": true,
  // optional: Set of restrictions applied to all locked course objects
  "blueprint_restrictions": {"content":true,"points":true,"due_dates":false,"availability_dates":false},
  // optional: Sets of restrictions differentiated by object type applied to
  // locked course objects
  "blueprint_restrictions_by_object_type": {"assignment":{"content":true,"points":true},"wiki_page":{"content":true}},
  // optional: whether the course is set as a template (requires the Course
  // Templates feature)
  "template": true
}
```

**A CalendarLink object looks like:**

```
{
  // The URL of the calendar in ICS format
  "ics": "https://canvas.instructure.com/feeds/calendars/course_abcdef.ics"
}
```

[CoursesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses`

**Scope:** `url:GET|/api/v1/courses`

Returns the paginated list of active courses for the current user.

**Request Parameters:**

When set, only return courses where the user is enrolled as this type. For example, set to “teacher” to return only courses where the user is enrolled as a Teacher. This argument is ignored if enrollment\_role is given.

Allowed values: `teacher`, `student`, `ta`, `observer`, `designer`

Deprecated When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the [Add Role API](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.add_role) or a base role type of ‘StudentEnrollment’, ‘TeacherEnrollment’, ‘TaEnrollment’, ‘ObserverEnrollment’, or ‘DesignerEnrollment’.

When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the [Add Role API](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.add_role) or a built\_in role type of ‘StudentEnrollment’, ‘TeacherEnrollment’, ‘TaEnrollment’, ‘ObserverEnrollment’, or ‘DesignerEnrollment’.

When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides.

Allowed values: `active`, `invited_or_pending`, `completed`

`exclude_blueprint_courses`

When set, only return courses that are not configured as blueprint courses.

- “needs\_grading\_count”: Optional information to include with each Course. When needs\_grading\_count is given, and the current user has grading rights, the total number of submissions needing grading for all assignments is returned.
- “syllabus\_body”: Optional information to include with each Course. When syllabus\_body is given the user-generated html for the course syllabus is returned.
- “public\_description”: Optional information to include with each Course. When public\_description is given the user-generated text for the course public description is returned.
- “total\_scores”: Optional information to include with each Course. When total\_scores is given, any student enrollments will also include the fields ‘computed\_current\_score’, ‘computed\_final\_score’, ‘computed\_current\_grade’, and ‘computed\_final\_grade’, as well as (if the user has permission) ‘unposted\_current\_score’, ‘unposted\_final\_score’, ‘unposted\_current\_grade’, and ‘unposted\_final\_grade’ (see Enrollment documentation for more information on these fields). This argument is ignored if the course is configured to hide final grades.
- “current\_grading\_period\_scores”: Optional information to include with each Course. When current\_grading\_period\_scores is given and total\_scores is given, any student enrollments will also include the fields ‘has\_grading\_periods’, ‘totals\_for\_all\_grading\_periods\_option’, ‘current\_grading\_period\_title’, ‘current\_grading\_period\_id’, current\_period\_computed\_current\_score’, ‘current\_period\_computed\_final\_score’, ‘current\_period\_computed\_current\_grade’, and ‘current\_period\_computed\_final\_grade’, as well as (if the user has permission) ‘current\_period\_unposted\_current\_score’, ‘current\_period\_unposted\_final\_score’, ‘current\_period\_unposted\_current\_grade’, and ‘current\_period\_unposted\_final\_grade’ (see Enrollment documentation for more information on these fields). In addition, when this argument is passed, the course will have a ‘has\_grading\_periods’ attribute on it. This argument is ignored if the total\_scores argument is not included. If the course is configured to hide final grades, the following fields are not returned: ‘totals\_for\_all\_grading\_periods\_option’, ‘current\_period\_computed\_current\_score’, ‘current\_period\_computed\_final\_score’, ‘current\_period\_computed\_current\_grade’, ‘current\_period\_computed\_final\_grade’, ‘current\_period\_unposted\_current\_score’, ‘current\_period\_unposted\_final\_score’, ‘current\_period\_unposted\_current\_grade’, and ‘current\_period\_unposted\_final\_grade’
- “grading\_periods”: Optional information to include with each Course. When grading\_periods is given, a list of the grading periods associated with each course is returned.
- “term”: Optional information to include with each Course. When term is given, the information for the enrollment term for each course is returned.
- “account”: Optional information to include with each Course. When account is given, the account json for each course is returned.
- “course\_progress”: Optional information to include with each Course. When course\_progress is given, each course will include a ‘course\_progress’ object with the fields: ‘requirement\_count’, an integer specifying the total number of requirements in the course, ‘requirement\_completed\_count’, an integer specifying the total number of requirements in this course that have been completed, and ‘next\_requirement\_url’, a string url to the next requirement item, and ‘completed\_at’, the date the course was completed (null if incomplete). ‘next\_requirement\_url’ will be null if all requirements have been completed or the current module does not require sequential progress. “course\_progress” will return an error message if the course is not module based or the user is not enrolled as a student in the course.
- “sections”: Section enrollment information to include with each Course. Returns an array of hashes containing the section ID (id), section name (name), start and end dates (start\_at, end\_at), as well as the enrollment type (enrollment\_role, e.g. ‘StudentEnrollment’).
- “storage\_quota\_used\_mb”: The amount of storage space used by the files in this course
- “total\_students”: Optional information to include with each Course. Returns an integer for the total amount of active and invited students.
- “passback\_status”: Include the grade passback\_status
- “favorites”: Optional information to include with each Course. Indicates if the user has marked the course as a favorite course.
- “teachers”: Teacher information to include with each Course. Returns an array of hashes containing the [UserDisplay](https://developerdocs.instructure.com/services/canvas/resources/users#UserDisplay) information for each teacher in the course.
- “observed\_users”: Optional information to include with each Course. Will include data for observed users if the current user has an observer enrollment.
- “tabs”: Optional information to include with each Course. Will include the list of tabs configured for each course. See the [List available tabs API](https://developerdocs.instructure.com/services/canvas/resources/tabs#method.tabs.index) for more information.
- “course\_image”: Optional information to include with each Course. Returns course image url if a course image has been set.
- “banner\_image”: Optional information to include with each Course. Returns course banner image url if the course is a Canvas for Elementary subject and a banner image has been set.
- “concluded”: Optional information to include with each Course. Indicates whether the course has been concluded, taking course and term dates into account.
- “post\_manually”: Optional information to include with each Course. Returns true if the course post policy is set to Manually post grades. Returns false if the the course post policy is set to Automatically post grades.

Allowed values: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `grading_periods`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `course_image`, `banner_image`, `concluded`, `post_manually`

If set, only return courses that are in the given state(s). By default, “available” is returned for students and observers, and anything except “deleted”, for all other enrollment types

Allowed values: `unpublished`, `available`, `completed`, `deleted`

Returns a list of [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) objects.

[CoursesController#user\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/users/:user_id/courses`

**Scope:** `url:GET|/api/v1/users/:user_id/courses`

Returns a paginated list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator.

**Request Parameters:**

- “needs\_grading\_count”: Optional information to include with each Course. When needs\_grading\_count is given, and the current user has grading rights, the total number of submissions needing grading for all assignments is returned.
- “syllabus\_body”: Optional information to include with each Course. When syllabus\_body is given the user-generated html for the course syllabus is returned.
- “public\_description”: Optional information to include with each Course. When public\_description is given the user-generated text for the course public description is returned.
- “total\_scores”: Optional information to include with each Course. When total\_scores is given, any student enrollments will also include the fields ‘computed\_current\_score’, ‘computed\_final\_score’, ‘computed\_current\_grade’, and ‘computed\_final\_grade’ (see Enrollment documentation for more information on these fields). This argument is ignored if the course is configured to hide final grades.
- “current\_grading\_period\_scores”: Optional information to include with each Course. When current\_grading\_period\_scores is given and total\_scores is given, any student enrollments will also include the fields ‘has\_grading\_periods’, ‘totals\_for\_all\_grading\_periods\_option’, ‘current\_grading\_period\_title’, ‘current\_grading\_period\_id’, current\_period\_computed\_current\_score’, ‘current\_period\_computed\_final\_score’, ‘current\_period\_computed\_current\_grade’, and ‘current\_period\_computed\_final\_grade’, as well as (if the user has permission) ‘current\_period\_unposted\_current\_score’, ‘current\_period\_unposted\_final\_score’, ‘current\_period\_unposted\_current\_grade’, and ‘current\_period\_unposted\_final\_grade’ (see Enrollment documentation for more information on these fields). In addition, when this argument is passed, the course will have a ‘has\_grading\_periods’ attribute on it. This argument is ignored if the course is configured to hide final grades or if the total\_scores argument is not included.
- “grading\_periods”: Optional information to include with each Course. When grading\_periods is given, a list of the grading periods associated with each course is returned.
- “term”: Optional information to include with each Course. When term is given, the information for the enrollment term for each course is returned.
- “account”: Optional information to include with each Course. When account is given, the account json for each course is returned.
- “course\_progress”: Optional information to include with each Course. When course\_progress is given, each course will include a ‘course\_progress’ object with the fields: ‘requirement\_count’, an integer specifying the total number of requirements in the course, ‘requirement\_completed\_count’, an integer specifying the total number of requirements in this course that have been completed, and ‘next\_requirement\_url’, a string url to the next requirement item, and ‘completed\_at’, the date the course was completed (null if incomplete). ‘next\_requirement\_url’ will be null if all requirements have been completed or the current module does not require sequential progress. “course\_progress” will return an error message if the course is not module based or the user is not enrolled as a student in the course.
- “sections”: Section enrollment information to include with each Course. Returns an array of hashes containing the section ID (id), section name (name), start and end dates (start\_at, end\_at), as well as the enrollment type (enrollment\_role, e.g. ‘StudentEnrollment’).
- “storage\_quota\_used\_mb”: The amount of storage space used by the files in this course
- “total\_students”: Optional information to include with each Course. Returns an integer for the total amount of active and invited students.
- “passback\_status”: Include the grade passback\_status
- “favorites”: Optional information to include with each Course. Indicates if the user has marked the course as a favorite course.
- “teachers”: Teacher information to include with each Course. Returns an array of hashes containing the [UserDisplay](https://developerdocs.instructure.com/services/canvas/resources/users#UserDisplay) information for each teacher in the course.
- “observed\_users”: Optional information to include with each Course. Will include data for observed users if the current user has an observer enrollment.
- “tabs”: Optional information to include with each Course. Will include the list of tabs configured for each course. See the [List available tabs API](https://developerdocs.instructure.com/services/canvas/resources/tabs#method.tabs.index) for more information.
- “course\_image”: Optional information to include with each Course. Returns course image url if a course image has been set.
- “banner\_image”: Optional information to include with each Course. Returns course banner image url if the course is a Canvas for Elementary subject and a banner image has been set.
- “concluded”: Optional information to include with each Course. Indicates whether the course has been concluded, taking course and term dates into account.
- “post\_manually”: Optional information to include with each Course. Returns true if the course post policy is set to “Manually”. Returns false if the the course post policy is set to “Automatically”.

Allowed values: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `grading_periods`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `course_image`, `banner_image`, `concluded`, `post_manually`

If set, only return courses that are in the given state(s). By default, “available” is returned for students and observers, and anything except “deleted”, for all other enrollment types

Allowed values: `unpublished`, `available`, `completed`, `deleted`

When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides.

Allowed values: `active`, `invited_or_pending`, `completed`

If set, only return homeroom courses.

If set, only include courses associated with this account

Returns a list of [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) objects.

[CoursesController#user\_progressarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/users/:user_id/progress`

**Scope:** `url:GET|/api/v1/courses/:course_id/users/:user_id/progress`

Return progress information for the user and course

You can supply `self` as the user\_id to query your own progress in a course. To query another user’s progress, you must be a teacher in the course, an administrator, or a linked observer of the user.

Returns a [CourseProgress](https://developerdocs.instructure.com/services/canvas/resources/courses#courseprogress) object.

[CoursesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`POST /api/v1/accounts/:account_id/courses`

**Scope:** `url:POST|/api/v1/accounts/:account_id/courses`

Create a new course

**Request Parameters:**

The name of the course. If omitted, the course will be named “Unnamed Course.”

The course code for the course.

Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless ‘restrict\_enrollments\_to\_course\_dates’ is set to true.

Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless ‘restrict\_enrollments\_to\_course\_dates’ is set to true.

The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference):

- ‘private’ (Private Copyrighted)
- ‘cc\_by\_nc\_nd’ (CC Attribution Non-Commercial No Derivatives)
- ‘cc\_by\_nc\_sa’ (CC Attribution Non-Commercial Share Alike)
- ‘cc\_by\_nc’ (CC Attribution Non-Commercial)
- ‘cc\_by\_nd’ (CC Attribution No Derivatives)
- ‘cc\_by\_sa’ (CC Attribution Share Alike)
- ‘public\_domain’ (Public Domain).

Set to true if course is public to both authenticated and unauthenticated users.

`course[is_public_to_auth_users]`

Set to true if course is public only to authenticated users.

Set to true to make the course syllabus public.

`course[public_syllabus_to_auth]`

Set to true to make the course syllabus public for authenticated users.

`course[public_description]`

A publicly visible description of the course.

`course[allow_student_wiki_edits]`

If true, students will be able to modify the course wiki.

`course[allow_wiki_comments]`

If true, course members will be able to comment on wiki pages.

`course[allow_student_forum_attachments]`

If true, students can attach files to forum posts.

Set to true if the course is open enrollment.

Set to true if the course is self enrollment.

`course[restrict_enrollments_to_course_dates]`

Set to true to restrict user enrollments to the start and end dates of the course. This value must be set to true in order to specify a course start date and/or end date.

The unique ID of the term to create to course in.

The unique SIS identifier.

The unique Integration identifier.

`course[hide_final_grades]`

If this option is set to true, the totals in student grades summary will be hidden.

`course[apply_assignment_group_weights]`

Set to true to weight final grade based on assignment groups percentages.

If this option is set to true, the course will be available to students immediately.

Set to true to enroll the current user as the teacher.

If this option is set to true, the template of the account will not be applied to this course It means copy\_from\_course\_template will not be executed. This option is thought for a course copy.

The type of page that users will see when they first visit the course

- ‘feed’ Recent Activity Dashboard
- ‘modules’ Course Modules/Sections Page
- ‘assignments’ Course Assignments List
- ‘syllabus’ Course Syllabus Page

other types may be added in the future

Allowed values: `feed`, `wiki`, `modules`, `syllabus`, `assignments`

The syllabus body for the course

`course[grading_standard_id]`

The grading standard id to set for the course. If no value is provided for this argument the current grading\_standard will be un-set from this course.

`course[grade_passback_setting]`

Optional. The grade\_passback\_setting for the course. Only ‘nightly\_sync’, ‘disabled’, and ” are allowed

Optional. Specifies the format of the course. (Should be ‘on\_campus’, ‘online’, or ‘blended’)

Default is false. When true, all grades in the course must be posted manually, and will not be automatically posted. When false, all grades in the course will be automatically posted.

When true, will first try to re-activate a deleted course with matching sis\_course\_id if possible.

Returns a [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) object.

[CoursesController#create\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`POST /api/v1/courses/:course_id/files`

**Scope:** `url:POST|/api/v1/courses/:course_id/files`

Upload a file to the course.

This API endpoint is the first step in uploading a file to a course. See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow.

Only those with the “Manage Files” permission on a course can upload files to the course. By default, this is Teachers, TAs and Designers.

[CoursesController#studentsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/students`

**Scope:** `url:GET|/api/v1/courses/:course_id/students`

Returns the paginated list of students enrolled in this course.

DEPRECATED: Please use the [course users](https://developerdocs.instructure.com/services/canvas/resources/courses#method.courses.users) endpoint and pass “student” as the enrollment\_type.

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[CoursesController#usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/users`

**Scope:** `url:GET|/api/v1/courses/:course_id/users`

`GET /api/v1/courses/:course_id/search_users`

**Scope:** `url:GET|/api/v1/courses/:course_id/search_users`

Returns the paginated list of users in this course. And optionally the user’s enrollments in the course.

**Request Parameters:**

The partial name or full ID of the users to match and return in the results list.

When set, sort the results of the search based on the given field.

Allowed values: `username`, `last_login`, `email`, `sis_id`

When set, only return users where the user is enrolled as this type. “student\_view” implies include\[]=test\_student. This argument is ignored if enrollment\_role is given.

Allowed values: `teacher`, `student`, `student_view`, `ta`, `observer`, `designer`

Deprecated When set, only return users enrolled with the specified course-level role. This can be a role created with the [Add Role API](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.add_role) or a base role type of ‘StudentEnrollment’, ‘TeacherEnrollment’, ‘TaEnrollment’, ‘ObserverEnrollment’, or ‘DesignerEnrollment’.

When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the [Add Role API](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.add_role) or a built\_in role id with type ‘StudentEnrollment’, ‘TeacherEnrollment’, ‘TaEnrollment’, ‘ObserverEnrollment’, or ‘DesignerEnrollment’.

When set, only return users who are enrolled in the given section(s).

Optionally include with each Course the user’s current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a ‘grades’ key with ‘current\_score’, ‘final\_score’, ‘current\_grade’ and ‘final\_grade’ values.

- “locked”: Optionally include whether an enrollment is locked.
- “avatar\_url”: Optionally include avatar\_url.
- “bio”: Optionally include each user’s bio.
- “test\_student”: Optionally include the course’s Test Student,

if present. Default is to not include Test Student.

- “custom\_links”: Optionally include plugin-supplied custom links for each student,

such as analytics information

- “current\_grading\_period\_scores”: if enrollments is included as

well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A ‘grading\_period\_id’ value will also be included with the scores. if grading\_period\_id is nil there is no current grading period and the score is a total score.

- “uuid”: Optionally include the users uuid

Allowed values: `enrollments`, `locked`, `avatar_url`, `test_student`, `bio`, `custom_links`, `current_grading_period_scores`, `uuid`

If this parameter is given and it corresponds to a user in the course, the `page` parameter will be ignored and the page containing the specified user will be returned instead.

If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the “user\_id” argument but multiple user\_ids can be included.

When set, only return users where the enrollment workflow state is of one of the given types. “active” and “invited” enrollments are returned by default.

Allowed values: `active`, `invited`, `rejected`, `completed`, `inactive`

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[CoursesController#recent\_studentsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/recent_students`

**Scope:** `url:GET|/api/v1/courses/:course_id/recent_students`

Returns the paginated list of users in this course, ordered by how recently they have logged in. The records include the ‘last\_login’ field which contains a timestamp of the last time that user logged into canvas. The querying user must have the ‘View usage reports’ permission.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/<course_id>/recent_users
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[CoursesController#userarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/users/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/users/:id`

Return information on a single user.

Accepts the same include\[] parameters as the :users: action, and returns a single user with the same fields as that action.

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[CoursesController#content\_share\_usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/content_share_users`

**Scope:** `url:GET|/api/v1/courses/:course_id/content_share_users`

Returns a paginated list of users you can share content with. Requires the content share feature and the user must have the manage content permission for the course.

**Request Parameters:**

Term used to find users. Will search available share users with the search term in their name.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/courses/<course_id>/content_share_users \
     -d 'search_term=smith'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[CoursesController#preview\_htmlarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`POST /api/v1/courses/:course_id/preview_html`

**Scope:** `url:POST|/api/v1/courses/:course_id/preview_html`

Preview html content processed for this course

**Request Parameters:**

The html content to process

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/preview_html \
     -F 'html=<p><badhtml></badhtml>processed html</p>' \
     -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "html": "<p>processed html</p>"
}
```

[CoursesController#activity\_streamarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/activity_stream`

**Scope:** `url:GET|/api/v1/courses/:course_id/activity_stream`

Returns the current user’s course-specific activity stream, paginated.

For full documentation, see the API documentation for the user activity stream, in the user api.

[CoursesController#activity\_stream\_summaryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/activity_stream/summary`

**Scope:** `url:GET|/api/v1/courses/:course_id/activity_stream/summary`

Returns a summary of the current user’s course-specific activity stream.

For full documentation, see the API documentation for the user activity stream summary, in the user api.

[CoursesController#todo\_itemsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/todo`

**Scope:** `url:GET|/api/v1/courses/:course_id/todo`

Returns the current user’s course-specific todo items.

For full documentation, see the API documentation for the user todo items, in the user api.

[CoursesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`DELETE /api/v1/courses/:id`

**Scope:** `url:DELETE|/api/v1/courses/:id`

Delete or conclude an existing course

**Request Parameters:**

The action to take on the course.

Allowed values: `delete`, `conclude`

**Example Response:**

[CoursesController#api\_settingsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/settings`

**Scope:** `url:GET|/api/v1/courses/:course_id/settings`

Returns some of a course’s settings.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/settings \
  -X GET \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "allow_student_discussion_topics": true,
  "allow_student_forum_attachments": false,
  "allow_student_discussion_editing": true,
  "grading_standard_enabled": true,
  "grading_standard_id": 137,
  "allow_student_organized_groups": true,
  "hide_final_grades": false,
  "hide_distribution_graphs": false,
  "hide_sections_on_course_users_page": false,
  "lock_all_announcements": true,
  "usage_rights_required": false,
  "homeroom_course": false,
  "default_due_time": "23:59:59",
  "conditional_release": false
}
```

[CoursesController#update\_settingsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`PUT /api/v1/courses/:course_id/settings`

**Scope:** `url:PUT|/api/v1/courses/:course_id/settings`

Can update the following course settings:

**Request Parameters:**

`allow_final_grade_override`

Let student final grades for a grading period or the total grades for the course be overridden

`allow_student_discussion_topics`

Let students create discussion topics

`allow_student_forum_attachments`

Let students attach files to discussions

`allow_student_discussion_editing`

Let students edit or delete their own discussion replies

`allow_student_organized_groups`

Let students organize their own groups

`allow_student_discussion_reporting`

Let students report offensive discussion content

`allow_student_anonymous_discussion_topics`

Let students create anonymous discussion topics

`filter_speed_grader_by_student_group`

Filter SpeedGrader to only the selected student group

Hide totals in student grades summary

Hide grade distribution graphs from students

`hide_sections_on_course_users_page`

Disallow students from viewing students in sections they do not belong to

Disable comments on announcements

Copyright and license information must be provided for files before they are published.

`restrict_student_past_view`

Restrict students from viewing courses after end date

`restrict_student_future_view`

Restrict students from viewing courses before start date

`show_announcements_on_home_page`

Show the most recent announcements on the Course home page (if a Wiki, defaults to five announcements, configurable via home\_page\_announcement\_limit). Canvas for Elementary subjects ignore this setting.

`home_page_announcement_limit`

Limit the number of announcements on the home page if enabled via show\_announcements\_on\_home\_page

Show the course summary (list of assignments and calendar events) on the syllabus page. Default is true.

Set the default due time for assignments. This is the time that will be pre-selected in the Canvas user interface when setting a due date for an assignment. It does not change when any existing assignment is due. It should be given in 24-hour HH:MM:SS format. The default is “23:59:59”. Use “inherit” to inherit the account setting.

Enable or disable individual learning paths for students based on assessment

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/settings \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'allow_student_discussion_topics=false'
```

[CoursesController#student\_view\_studentarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/student_view_student`

**Scope:** `url:GET|/api/v1/courses/:course_id/student_view_student`

Returns information for a test student in this course. Creates a test student if one does not already exist for the course. The caller must have permission to access the course’s student view.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/student_view_student \
  -X GET \
  -H 'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[CoursesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:id`

**Scope:** `url:GET|/api/v1/courses/:id`

`GET /api/v1/accounts/:account_id/courses/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/courses/:id`

Return information on a single course.

Accepts the same include\[] parameters as the list action plus:

**Request Parameters:**

- “all\_courses”: Also search recently deleted courses.
- “permissions”: Include permissions the current user has for the course.
- “observed\_users”: Include observed users in the enrollments
- “course\_image”: Include course image url if a course image has been set
- “banner\_image”: Include course banner image url if the course is a Canvas for Elementary subject and a banner image has been set
- “concluded”: Optional information to include with Course. Indicates whether the course has been concluded, taking course and term dates into account.
- “lti\_context\_id”: Include course LTI tool id.
- “post\_manually”: Include course post policy. If the post policy is manually post grades, the value will be true. If the post policy is automatically post grades, the value will be false.

Allowed values: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `all_courses`, `permissions`, `course_image`, `banner_image`, `concluded`, `lti_context_id`, `post_manually`

The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a *teacher\_count* key.

Returns a [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) object.

[CoursesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`PUT /api/v1/courses/:id`

**Scope:** `url:PUT|/api/v1/courses/:id`

Update an existing course.

Arguments are the same as Courses#create, with a few exceptions (enroll\_me).

If a user has content management rights, but not full course editing rights, the only attribute editable through this endpoint will be “syllabus\_body”

If an account has set prevent\_course\_availability\_editing\_by\_teachers, a teacher cannot change `course[start_at]`, `course[conclude_at]`, or `course[restrict_enrollments_to_course_dates]` here.

**Request Parameters:**

The unique ID of the account to move the course to.

The name of the course. If omitted, the course will be named “Unnamed Course.”

The course code for the course.

Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless ‘restrict\_enrollments\_to\_course\_dates’ is set to true, or the course is already published.

Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless ‘restrict\_enrollments\_to\_course\_dates’ is set to true.

The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference):

- ‘private’ (Private Copyrighted)
- ‘cc\_by\_nc\_nd’ (CC Attribution Non-Commercial No Derivatives)
- ‘cc\_by\_nc\_sa’ (CC Attribution Non-Commercial Share Alike)
- ‘cc\_by\_nc’ (CC Attribution Non-Commercial)
- ‘cc\_by\_nd’ (CC Attribution No Derivatives)
- ‘cc\_by\_sa’ (CC Attribution Share Alike)
- ‘public\_domain’ (Public Domain).

Set to true if course is public to both authenticated and unauthenticated users.

`course[is_public_to_auth_users]`

Set to true if course is public only to authenticated users.

Set to true to make the course syllabus public.

`course[public_syllabus_to_auth]`

Set to true to make the course syllabus to public for authenticated users.

`course[public_description]`

A publicly visible description of the course.

`course[allow_student_wiki_edits]`

If true, students will be able to modify the course wiki.

`course[allow_wiki_comments]`

If true, course members will be able to comment on wiki pages.

`course[allow_student_forum_attachments]`

If true, students can attach files to forum posts.

Set to true if the course is open enrollment.

Set to true if the course is self enrollment.

`course[restrict_enrollments_to_course_dates]`

Set to true to restrict user enrollments to the start and end dates of the course. Setting this value to false will remove the course end date (if it exists), as well as the course start date (if the course is unpublished).

The unique ID of the term to create to course in.

The unique SIS identifier.

The unique Integration identifier.

`course[hide_final_grades]`

If this option is set to true, the totals in student grades summary will be hidden.

`course[apply_assignment_group_weights]`

Set to true to weight final grade based on assignment groups percentages.

Set the storage quota for the course, in megabytes. The caller must have the “Manage storage quotas” account permission.

If this option is set to true, the course will be available to students immediately.

The action to take on each course.

- ‘claim’ makes a course no longer visible to students. This action is also called “unpublish” on the web site. A course cannot be unpublished if students have received graded submissions.
- ‘offer’ makes a course visible to students. This action is also called “publish” on the web site.
- ‘conclude’ prevents future enrollments and makes a course read-only for all participants. The course still appears in prior-enrollment lists.
- ‘delete’ completely removes the course from the web site (including course menus and prior-enrollment lists). All enrollments are deleted. Course content may be physically deleted at a future date.
- ‘undelete’ attempts to recover a course that has been deleted. This action requires account administrative rights. (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered.

Allowed values: `claim`, `offer`, `conclude`, `delete`, `undelete`

The type of page that users will see when they first visit the course

- ‘feed’ Recent Activity Dashboard
- ‘modules’ Course Modules/Sections Page
- ‘assignments’ Course Assignments List
- ‘syllabus’ Course Syllabus Page

other types may be added in the future

Allowed values: `feed`, `wiki`, `modules`, `syllabus`, `assignments`

The syllabus body for the course

`course[syllabus_course_summary]`

Optional. Indicates whether the Course Summary (consisting of the course’s assignments and calendar events) is displayed on the syllabus page. Defaults to `true`.

`course[grading_standard_id]`

The grading standard id to set for the course. If no value is provided for this argument the current grading\_standard will be un-set from this course.

`course[grade_passback_setting]`

Optional. The grade\_passback\_setting for the course. Only ‘nightly\_sync’ and ” are allowed

Optional. Specifies the format of the course. (Should be either ‘on\_campus’ or ‘online’)

This is a file ID corresponding to an image file in the course that will be used as the course image. This will clear the course’s image\_url setting if set. If you attempt to provide image\_url and image\_id in a request it will fail.

This is a URL to an image to be used as the course image. This will clear the course’s image\_id setting if set. If you attempt to provide image\_url and image\_id in a request it will fail.

If this option is set to true, the course image url and course image ID are both set to nil

`course[remove_banner_image]`

If this option is set to true, the course banner image url and course banner image ID are both set to nil

Sets the course as a blueprint course.

`course[blueprint_restrictions]`

Sets a default set to apply to blueprint course objects when restricted, unless *use\_blueprint\_restrictions\_by\_object\_type* is enabled. See the [Blueprint Restriction](https://developerdocs.instructure.com/services/canvas/resources/blueprint_courses#BlueprintRestriction) documentation

`course[use_blueprint_restrictions_by_object_type]`

When enabled, the *blueprint\_restrictions* parameter will be ignored in favor of the *blueprint\_restrictions\_by\_object\_type* parameter

`course[blueprint_restrictions_by_object_type]`

`multiple BlueprintRestrictions`

Allows setting multiple [Blueprint Restriction](https://developerdocs.instructure.com/services/canvas/resources/blueprint_courses#BlueprintRestriction) to apply to blueprint course objects of the matching type when restricted. The possible object types are “assignment”, “attachment”, “discussion\_topic”, “quiz” and “wiki\_page”. Example usage:

```
course[blueprint_restrictions_by_object_type][assignment][content]=1
```

Sets the course as a homeroom course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account.

`course[sync_enrollments_from_homeroom]`

Syncs enrollments from the homeroom that is set in homeroom\_course\_id. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync\_enrollments\_from\_homeroom is enabled.

`course[homeroom_course_id]`

Sets the Homeroom Course id to be used with sync\_enrollments\_from\_homeroom. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync\_enrollments\_from\_homeroom is enabled.

Enable or disable the course as a template that can be selected by an account

Sets a color in hex code format to be associated with the course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account.

Set a friendly name for the course. If this is provided and the course is associated with a Canvas for Elementary account, it will be shown instead of the course name. This setting takes priority over course nicknames defined by individual users.

`course[enable_course_paces]`

Enable or disable Course Pacing for the course. This setting only has an effect when the Course Pacing feature flag is enabled for the sub-account. Otherwise, Course Pacing are always disabled.

`course[conditional_release]`

Enable or disable individual learning paths for students based on assessment

When true, all grades in the course will be posted manually. When false, all grades in the course will be automatically posted. Use with caution as this setting will override any assignment level post policy.

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id> \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'course[name]=New course name' \
  -d 'course[start_at]=2012-05-05T00:00:00Z'
```

**Example Response:**

```
{
  "name": "New course name",
  "course_code": "COURSE-001",
  "start_at": "2012-05-05T00:00:00Z",
  "end_at": "2012-08-05T23:59:59Z",
  "sis_course_id": "12345"
}
```

[CoursesController#batch\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`PUT /api/v1/accounts/:account_id/courses`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/courses`

Update multiple courses in an account. Operates asynchronously; use the [progress endpoint](https://developerdocs.instructure.com/services/canvas/resources/progress#method.progress.show) to query the status of an operation.

**Request Parameters:**

List of ids of courses to update. At most 500 courses may be updated in one call.

The action to take on each course. Must be one of ‘offer’, ‘conclude’, ‘delete’, or ‘undelete’.

- ‘offer’ makes a course visible to students. This action is also called “publish” on the web site.
- ‘conclude’ prevents future enrollments and makes a course read-only for all participants. The course still appears in prior-enrollment lists.
- ‘delete’ completely removes the course from the web site (including course menus and prior-enrollment lists). All enrollments are deleted. Course content may be physically deleted at a future date.
- ‘undelete’ attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered.

Allowed values: `offer`, `conclude`, `delete`, `undelete`

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/<account_id>/courses \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'event=offer' \
  -d 'course_ids[]=1' \
  -d 'course_ids[]=2'
```

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[CoursesController#reset\_contentarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`POST /api/v1/courses/:course_id/reset_content`

**Scope:** `url:POST|/api/v1/courses/:course_id/reset_content`

Deletes the current course, and creates a new equivalent course with no content, but all sections and users moved over.

Returns a [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) object.

[CoursesController#effective\_due\_datesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/effective_due_dates`

**Scope:** `url:GET|/api/v1/courses/:course_id/effective_due_dates`

For each assignment in the course, returns each assigned student’s ID and their corresponding due date along with some grading period data. Returns a collection with keys representing assignment IDs and values as a collection containing keys representing student IDs and values representing the student’s effective due\_at, the grading\_period\_id of which the due\_at falls in, and whether or not the grading period is closed (in\_closed\_grading\_period)

The list of assignment IDs for which effective student due dates are requested. If not provided, all assignments in the course will be used.

**Request Parameters:**

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/effective_due_dates
  -X GET \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "1": {
     "14": { "due_at": "2015-09-05", "grading_period_id": null, "in_closed_grading_period": false },
     "15": { due_at: null, "grading_period_id": 3, "in_closed_grading_period": true }
  },
  "2": {
     "14": { "due_at": "2015-08-05", "grading_period_id": 3, "in_closed_grading_period": true }
  }
}
```

[CoursesController#permissionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/permissions`

**Scope:** `url:GET|/api/v1/courses/:course_id/permissions`

Returns permission information for the calling user in the given course. See also the [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts#method.accounts.permissions) and [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#method.groups.permissions) counterparts.

**Request Parameters:**

List of permissions to check against the authenticated user. Permission names are documented in the [List assignable permissions](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.manageable_permissions) endpoint.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/permissions \
  -H 'Authorization: Bearer <token>' \
  -d 'permissions[]=manage_grades'
  -d 'permissions[]=send_messages'
```

**Example Response:**

```
{'manage_grades': 'false', 'send_messages': 'true'}
```

[CoursesController#bulk\_user\_progressarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`GET /api/v1/courses/:course_id/bulk_user_progress`

**Scope:** `url:GET|/api/v1/courses/:course_id/bulk_user_progress`

Returns progress information for all users enrolled in the given course.

You must be a user who has permission to view all grades in the course (such as a teacher or administrator).

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/bulk_user_progress \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
[
  {
    "id": 1,
    "display_name": "Test Student 1",
    "avatar_image_url": "https://<canvas>/images/messages/avatar-50.png",
    "html_url": "https://<canvas>/courses/1/users/1",
    "pronouns": null,
    "progress": {
      "requirement_count": 2,
      "requirement_completed_count": 1,
      "next_requirement_url": "https://<canvas>/courses/<course_id>/modules/items/<item_id>",
      "completed_at": null
    }
  },
  {
    "id": 2,
    "display_name": "Test Student 2",
    "avatar_image_url": "https://<canvas>/images/messages/avatar-50.png",
    "html_url": "https://<canvas>/courses/1/users/2",
    "pronouns": null,
    "progress": {
      "requirement_count": 2,
      "requirement_completed_count": 2,
      "next_requirement_url": null,
      "completed_at": "2021-08-10T16:26:08Z"
    }
  }
]
```

[CoursesController#dismiss\_migration\_limitation\_msgarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`POST /api/v1/courses/:id/dismiss_migration_limitation_message`

**Scope:** `url:POST|/api/v1/courses/:id/dismiss_migration_limitation_message`

Remove alert about the limitations of quiz migrations that is displayed to a user in a course

you must be logged in to use this endpoint

**Example Response:**

[CoursesController#restore\_versionarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/courses_controller.rb)

`POST /api/v1/courses/:course_id/restore/:version_id`

**Scope:** `url:POST|/api/v1/courses/:course_id/restore/:version_id`

Restore a course to a prior version.

**Request Parameters:**

The version to restore to (use the syllabus\_versions include parameter in the course show API to see available versions)

**Example Request:**

```
curl -X POST -H 'Authorization: Bearer <token>' \
https://<canvas>/api/v1/courses/123/restore/4
```

Returns a [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) object.

[ContentImportsController#copy\_course\_statusarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_imports_controller.rb)

`GET /api/v1/courses/:course_id/course_copy/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/course_copy/:id`

DEPRECATED: Please use the [Content Migrations API](https://developerdocs.instructure.com/services/canvas/resources/content_migrations#method.content_migrations.create)

Retrieve the status of a course copy

**API response field:**

The unique identifier for the course copy.

The time that the copy was initiated.

The progress of the copy as an integer. It is null before the copying starts, and 100 when finished.

The current status of the course copy. Possible values: “created”, “started”, “completed”, “failed”

The url for the course copy status API endpoint.

**Example Response:**

```
{'progress':100, 'workflow_state':'completed', 'id':257, 'created_at':'2011-11-17T16:50:06Z', 'status_url':'/api/v1/courses/9457/course_copy/257'}
```

[ContentImportsController#copy\_course\_contentarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_imports_controller.rb)

`POST /api/v1/courses/:course_id/course_copy`

**Scope:** `url:POST|/api/v1/courses/:course_id/course_copy`

DEPRECATED: Please use the [Content Migrations API](https://developerdocs.instructure.com/services/canvas/resources/content_migrations#method.content_migrations.create)

Copies content from one course into another. The default is to copy all course content. You can control specific types to copy by using either the ‘except’ option or the ‘only’ option.

The response is the same as the course copy status endpoint

**Request Parameters:**

ID or SIS-ID of the course to copy the content from

A list of the course content types to exclude, all areas not listed will be copied.

Allowed values: `course_settings`, `assignments`, `external_tools`, `files`, `topics`, `calendar_events`, `quizzes`, `wiki_pages`, `modules`, `outcomes`

A list of the course content types to copy, all areas not listed will not be copied.

Allowed values: `course_settings`, `assignments`, `external_tools`, `files`, `topics`, `calendar_events`, `quizzes`, `wiki_pages`, `modules`, `outcomes`

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).