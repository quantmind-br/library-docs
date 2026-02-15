---
title: Assignment Groups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/assignment_groups
source: sitemap
fetched_at: 2026-02-15T08:57:44.106462-03:00
rendered_js: false
word_count: 617
summary: This document provides technical specifications for the Assignment Groups API, detailing the RESTful endpoints used to manage assignment groupings and grading rules within a course.
tags:
    - assignment-groups
    - canvas-lms-api
    - rest-api
    - grading-rules
    - course-management
    - endpoint-reference
category: api
---

API for accessing Assignment Group and Assignment information.

**A GradingRules object looks like:**

```
{
  // Number of lowest scores to be dropped for each user.
"drop_lowest": 1,
  // Number of highest scores to be dropped for each user.
"drop_highest": 1,
  // Assignment IDs that should never be dropped.
"never_drop": [33,17,24]
}
```

**An AssignmentGroup object looks like:**

```
{
  // the id of the Assignment Group
"id": 1,
  // the name of the Assignment Group
"name": "group2",
  // the position of the Assignment Group
"position": 7,
  // the weight of the Assignment Group
"group_weight": 20,
  // the sis source id of the Assignment Group
"sis_source_id": "1234",
  // the integration data of the Assignment Group
"integration_data": {"5678":"0954"},
  // the assignments in this Assignment Group (see the Assignment API for a
  // detailed list of fields)
"assignments": [],
  // the grading rules that this Assignment Group has
"rules": null
}
```

[AssignmentGroupsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_controller.rb)

`GET /api/v1/courses/:course_id/assignment_groups`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignment_groups`

Returns the paginated list of assignment groups for the current context. The returned groups are sorted by their position field.

**Request Parameters:**

Associations to include with the group. “discussion\_topic”, “all\_dates”, “can\_edit”, “assignment\_visibility” & “submission” are only valid if “assignments” is also included. “score\_statistics” requires that the “assignments” and “submission” options are included. The “assignment\_visibility” option additionally requires that the Differentiated Assignments course feature be turned on. If “observed\_users” is passed along with “assignments” and “submission”, submissions for observed users will also be included as an array. The “peer\_review” option requires that the Peer Review Grading course feature be turned on and that “assignments” is included.

Allowed values: `assignments`, `discussion_topic`, `all_dates`, `assignment_visibility`, `overrides`, `submission`, `observed_users`, `can_edit`, `score_statistics`, `peer_review`

If “assignments” are included, optionally return only assignments having their ID in this array. This argument may also be passed as a comma separated string.

`exclude_assignment_submission_types[]`

If “assignments” are included, those with the specified submission types will be excluded from the assignment groups.

Allowed values: `online_quiz`, `discussion_topic`, `wiki_page`, `external_tool`

`override_assignment_dates`

Apply assignment overrides for each assignment, defaults to true.

The id of the grading period in which assignment groups are being requested (Requires grading periods to exist.)

`scope_assignments_to_student`

If true, all assignments returned will apply to the current user in the specified grading period. If assignments apply to other students in the specified grading period, but not the current user, they will not be returned. (Requires the grading\_period\_id argument and grading periods to exist. In addition, the current user must be a student.)

Returns a list of [AssignmentGroup](https://developerdocs.instructure.com/services/canvas/resources/assignment_groups#assignmentgroup) objects.

[AssignmentGroupsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

`GET /api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

**Scope:** `url:GET|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

Returns the assignment group with the given id.

**Request Parameters:**

Associations to include with the group. “discussion\_topic” and “assignment\_visibility” and “submission” are only valid if “assignments” is also included. “score\_statistics” is only valid if “submission” and “assignments” are also included. The “assignment\_visibility” option additionally requires that the Differentiated Assignments course feature be turned on.

Allowed values: `assignments`, `discussion_topic`, `assignment_visibility`, `submission`, `score_statistics`

`override_assignment_dates`

Apply assignment overrides for each assignment, defaults to true.

The id of the grading period in which assignment groups are being requested (Requires grading periods to exist on the account)

Returns an [AssignmentGroup](https://developerdocs.instructure.com/services/canvas/resources/assignment_groups#assignmentgroup) object.

[AssignmentGroupsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

`POST /api/v1/courses/:course_id/assignment_groups`

**Scope:** `url:POST|/api/v1/courses/:course_id/assignment_groups`

Create a new assignment group for this course.

**Request Parameters:**

The assignment group’s name

The position of this assignment group in relation to the other assignment groups

The percent of the total grade that this assignment group represents

The sis source id of the Assignment Group

The integration data of the Assignment Group

Returns an [AssignmentGroup](https://developerdocs.instructure.com/services/canvas/resources/assignment_groups#assignmentgroup) object.

[AssignmentGroupsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

`PUT /api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

Modify an existing Assignment Group.

**Request Parameters:**

The assignment group’s name

The position of this assignment group in relation to the other assignment groups

The percent of the total grade that this assignment group represents

The sis source id of the Assignment Group

The integration data of the Assignment Group

The grading rules that are applied within this assignment group See the Assignment Group object definition for format

Returns an [AssignmentGroup](https://developerdocs.instructure.com/services/canvas/resources/assignment_groups#assignmentgroup) object.

[AssignmentGroupsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/assignment_groups_api_controller.rb)

`DELETE /api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/assignment_groups/:assignment_group_id`

Deletes the assignment group with the given id.

**Request Parameters:**

The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted.

Returns an [AssignmentGroup](https://developerdocs.instructure.com/services/canvas/resources/assignment_groups#assignmentgroup) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).