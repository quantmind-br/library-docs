---
title: Group Categories | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/group_categories
source: sitemap
fetched_at: 2026-02-15T08:57:53.853896-03:00
rendered_js: false
word_count: 1123
summary: This document defines the Group Category object and provides a detailed specification of the API endpoints for listing, creating, and managing group categories within a course or account context.
tags:
    - canvas-lms
    - group-categories
    - rest-api
    - group-management
    - api-reference
category: api
---

Group Categories allow grouping of groups together in canvas. There are a few different built-in group categories used, or custom ones can be created. The built in group categories are: "communities", "student\_organized", and "imported".

**A GroupCategory object looks like:**

```
{
  // The ID of the group category.
"id": 17,
  // The display name of the group category.
"name": "Math Groups",
  // Certain types of group categories have special role designations. Currently,
  // these include: 'communities', 'student_organized', and 'imported'. Regular
  // course/account group categories have a role of null.
"role": "communities",
  // If the group category allows users to join a group themselves, thought they
  // may only be a member of one group per group category at a time. Values
  // include 'restricted', 'enabled', and null 'enabled' allows students to assign
  // themselves to a group 'restricted' restricts them to only joining a group in
  // their section null disallows students from joining groups
"self_signup": null,
  // Gives instructors the ability to automatically have group leaders assigned. 
  // Values include 'random', 'first', and null; 'random' picks a student from the
  // group at random as the leader, 'first' sets the first student to be assigned
  // to the group as the leader
"auto_leader": null,
  // The course or account that the category group belongs to. The pattern here is
  // that whatever the context_type is, there will be an _id field named after
  // that type. So if instead context_type was 'Course', the course_id field would
  // be replaced by an course_id field.
"context_type": "Account",
"account_id": 3,
  // If self-signup is enabled, group_limit can be set to cap the number of users
  // in each group. If null, there is no limit.
"group_limit": null,
  // The SIS identifier for the group category. This field is only included if the
  // user has permission to manage or view SIS information.
"sis_group_category_id": null,
  // The unique identifier for the SIS import. This field is only included if the
  // user has permission to manage SIS information.
"sis_import_id": null,
  // If the group category has not yet finished a randomly student assignment
  // request, a progress object will be attached, which will contain information
  // related to the progress of the assignment request. Refer to the Progress API
  // for more information
"progress": null,
  // Indicates whether this group category is non-collaborative. A value of true
  // means these group categories rely on the manage_tags permissions and do not
  // have collaborative features
"non_collaborative": null
}
```

[GroupCategoriesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`GET /api/v1/accounts/:account_id/group_categories`

**Scope:** `url:GET|/api/v1/accounts/:account_id/group_categories`

`GET /api/v1/courses/:course_id/group_categories`

**Scope:** `url:GET|/api/v1/courses/:course_id/group_categories`

Returns a paginated list of group categories in a context. The list returned depends on the permissions of the current user and the specified collaboration state.

**Request Parameters:**

Filter group categories by their collaboration state:

- “all”: Return both collaborative and non-collaborative group categories
- “collaborative”: Return only collaborative group categories (default)
- “non\_collaborative”: Return only non-collaborative group categories

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/<account_id>/group_categories \
     -H 'Authorization: Bearer <token>' \
     -d 'collaboration_state=all'
```

Returns a list of [GroupCategory](https://developerdocs.instructure.com/services/canvas/resources/group_categories#groupcategory) objects.

[GroupCategoriesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`GET /api/v1/group_categories/:group_category_id`

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id`

Returns the data for a single group category, or a 401 if the caller doesn’t have the rights to see it.

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/<group_category_id> \
     -H 'Authorization: Bearer <token>'
```

Returns a [GroupCategory](https://developerdocs.instructure.com/services/canvas/resources/group_categories#groupcategory) object.

[GroupCategoriesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`POST /api/v1/accounts/:account_id/group_categories`

**Scope:** `url:POST|/api/v1/accounts/:account_id/group_categories`

`POST /api/v1/courses/:course_id/group_categories`

**Scope:** `url:POST|/api/v1/courses/:course_id/group_categories`

Create a new group category

**Request Parameters:**

Name of the group category

Can only be set by users with the Differentiation Tag - Add permission

If set to true, groups in this category will be only be visible to users with the Differentiation Tag - Manage permission.

Allow students to sign up for a group themselves (Course Only). valid values are:

- “enabled”
  
  allows students to self sign up for any group in course
- “restricted”
  
  allows students to self sign up only for groups in the same section null disallows self sign up

Allowed values: `enabled`, `restricted`

Assigns group leaders automatically when generating and allocating students to groups Valid values are:

- “first”
  
  the first student to be allocated to a group is the leader
- “random”
  
  a random student from all members is chosen as the leader

Allowed values: `first`, `random`

Limit the maximum number of users in each group (Course Only). Requires self signup.

The unique SIS identifier.

Create this number of groups (Course Only).

(Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with “enable\_self\_signup”. because the group assignment happens synchronously, it’s recommended that you instead use the assign\_unassigned\_members endpoint. (Course Only)

**Example Request:**

```
curl htps://<canvas>/api/v1/courses/<course_id>/group_categories \
    -F 'name=Project Groups' \
    -H 'Authorization: Bearer <token>'
```

Returns a [GroupCategory](https://developerdocs.instructure.com/services/canvas/resources/group_categories#groupcategory) object.

[GroupCategoriesController#bulk\_manage\_differentiation\_tagarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`POST /api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag`

**Scope:** `url:POST|/api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag`

This API is only meant for Groups and GroupCategories where non\_collaborative is true.

Perform bulk operations on groups within a group category, or create a new group category along with the groups in one transaction. If creation of the GroupCategory or any Group fails, the entire operation will be rolled back.

**Request Parameters:**

A hash containing arrays of create/update/delete operations: {

```
"create": [
  { "name": "New Group A" },
  { "name": "New Group B" }
],
"update": [
  { "id": 123, "name": "Updated Group Name A" },
  { "id": 456, "name": "Updated Group Name B" }
],
"delete": [
  { "id": 789 },
  { "id": 101 }
]
```

}

Attributes for the GroupCategory. May include:

```
- id [Optional, Integer]: The ID of an existing GroupCategory.
- name [Optional, String]: A new name for the GroupCategory. If provided with an ID, the category name will be updated.
```

**Example Request:**

```
curl https://<canvas>/api/v1/courses/:course_id/group_categories/bulk_manage_differentiation_tag \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -H 'Content-Type: application/json' \
     -d '{
           "operations": {
             "create": [{"name": "New Group"}],
             "update": [{"id": 123, "name": "Updated Group"}],
             "delete": [{"id": 456}]
           },
           "group_category": {"id": 1, "name": "New Category Name"}
         }'
```

[GroupCategoriesController#import\_tagsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`POST /api/v1/courses/:course_id/group_categories/import_tags`

**Scope:** `url:POST|/api/v1/courses/:course_id/group_categories/import_tags`

Create Differentiation Tags through a CSV import

For more information on the format that’s expected here, please see the “Differentiation Tag CSV” section in the API docs.

**Request Parameters:**

There are two ways to post differentiation tag import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.

‘attachment’ is required for multipart/form-data style posts. Assumed to be tag data from a file upload form field named ‘attachment’.

Examples:

```
curl -F attachment=@<filename> -H "Authorization: Bearer <token>" <br>    'https://<canvas>/api/v1/group_categories/import_tags'
```

If you decide to do a raw post, you can skip the ‘attachment’ argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the ‘extension’ argument.

Examples:

```
curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv <br>    -H "Authorization: Bearer <token>" <br>    'https://<canvas>/api/v1/group_categories_tags'
```

**Example Response:**

```
# Progress (default)
{
    "completion": 0,
    "context_id": 20,
    "context_type": "Course",
    "created_at": "2013-07-05T10:57:48-06:00",
    "id": 2,
    "message": null,
    "tag": "course_tag_import",
    "updated_at": "2013-07-05T10:57:48-06:00",
    "user_id": null,
    "workflow_state": "running",
    "url": "http://localhost:3000/api/v1/progress/2"
}
```

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[GroupCategoriesController#importarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`POST /api/v1/group_categories/:group_category_id/import`

**Scope:** `url:POST|/api/v1/group_categories/:group_category_id/import`

Create Groups in a Group Category through a CSV import

For more information on the format that’s expected here, please see the “Group Category CSV” section in the API docs.

**Request Parameters:**

There are two ways to post group category import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.

‘attachment’ is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named ‘attachment’.

Examples:

```
curl -F attachment=@<filename> -H "Authorization: Bearer <token>" <br>    'https://<canvas>/api/v1/group_categories/<category_id>/import'
```

If you decide to do a raw post, you can skip the ‘attachment’ argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the ‘extension’ argument.

Examples:

```
curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv <br>    -H "Authorization: Bearer <token>" <br>    'https://<canvas>/api/v1/group_categories/<category_id>/import'
```

**Example Response:**

```
# Progress (default)
{
    "completion": 0,
    "context_id": 20,
    "context_type": "GroupCategory",
    "created_at": "2013-07-05T10:57:48-06:00",
    "id": 2,
    "message": null,
    "tag": "course_group_import",
    "updated_at": "2013-07-05T10:57:48-06:00",
    "user_id": null,
    "workflow_state": "running",
    "url": "http://localhost:3000/api/v1/progress/2"
}
```

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[GroupCategoriesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`PUT /api/v1/group_categories/:group_category_id`

**Scope:** `url:PUT|/api/v1/group_categories/:group_category_id`

Modifies an existing group category.

**Request Parameters:**

Name of the group category

Allow students to sign up for a group themselves (Course Only). Valid values are:

- “enabled”
  
  allows students to self sign up for any group in course
- “restricted”
  
  allows students to self sign up only for groups in the same section null disallows self sign up

Allowed values: `enabled`, `restricted`

Assigns group leaders automatically when generating and allocating students to groups Valid values are:

- “first”
  
  the first student to be allocated to a group is the leader
- “random”
  
  a random student from all members is chosen as the leader

Allowed values: `first`, `random`

Limit the maximum number of users in each group (Course Only). Requires self signup.

The unique SIS identifier.

Create this number of groups (Course Only).

(Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with “enable\_self\_signup”. because the group assignment happens synchronously, it’s recommended that you instead use the assign\_unassigned\_members endpoint. (Course Only)

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/<group_category_id> \
    -X PUT \
    -F 'name=Project Groups' \
    -H 'Authorization: Bearer <token>'
```

Returns a [GroupCategory](https://developerdocs.instructure.com/services/canvas/resources/group_categories#groupcategory) object.

[GroupCategoriesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`DELETE /api/v1/group_categories/:group_category_id`

**Scope:** `url:DELETE|/api/v1/group_categories/:group_category_id`

Deletes a group category and all groups under it. Protected group categories can not be deleted, i.e. “communities” and “student\_organized”.

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/<group_category_id> \
      -X DELETE \
      -H 'Authorization: Bearer <token>'
```

[GroupCategoriesController#groupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`GET /api/v1/group_categories/:group_category_id/groups`

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id/groups`

Returns a paginated list of groups in a group category

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/<group_cateogry_id>/groups \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) objects.

[GroupCategoriesController#exportarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/group_categories/:group_category_id/export`

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id/export`

Returns a csv file of users in format ready to import.

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/<group_category_id>/export \
     -H 'Authorization: Bearer <token>'
```

[GroupCategoriesController#export\_tagsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

BETA: This API endpoint is not finalized, and there could be breaking changes before its final release.

`GET /api/v1/courses/:course_id/group_categories/export_tags`

**Scope:** `url:GET|/api/v1/courses/:course_id/group_categories/export_tags`

Returns a csv file of users in format ready to import.

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/export_tags \
     -H 'Authorization: Bearer <token>'
```

[GroupCategoriesController#usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`GET /api/v1/group_categories/:group_category_id/users`

**Scope:** `url:GET|/api/v1/group_categories/:group_category_id/users`

Returns a paginated list of users in the group category.

**Request Parameters:**

The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.

Set this value to true if you wish only to search unassigned users in the group category.

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/1/users \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[GroupCategoriesController#assign\_unassigned\_membersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_categories_controller.rb)

`POST /api/v1/group_categories/:group_category_id/assign_unassigned_members`

**Scope:** `url:POST|/api/v1/group_categories/:group_category_id/assign_unassigned_members`

Assign all unassigned members as evenly as possible among the existing student groups.

**Request Parameters:**

The assigning is done asynchronously by default. If you would like to override this and have the assigning done synchronously, set this value to true.

**Example Request:**

```
curl https://<canvas>/api/v1/group_categories/1/assign_unassigned_members \
     -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
# Progress (default)
{
    "completion": 0,
    "context_id": 20,
    "context_type": "GroupCategory",
    "created_at": "2013-07-05T10:57:48-06:00",
    "id": 2,
    "message": null,
    "tag": "assign_unassigned_members",
    "updated_at": "2013-07-05T10:57:48-06:00",
    "user_id": null,
    "workflow_state": "running",
    "url": "http://localhost:3000/api/v1/progress/2"
}
```

```
# New Group Memberships (when sync = true)
[
  {
    "id": 65,
    "new_members": [
      {
        "user_id": 2,
        "name": "Sam",
        "display_name": "Sam",
        "sections": [
          {
            "section_id": 1,
            "section_code": "Section 1"
          }
        ]
      },
      {
        "user_id": 3,
        "name": "Sue",
        "display_name": "Sue",
        "sections": [
          {
            "section_id": 2,
            "section_code": "Section 2"
          }
        ]
      }
    ]
  },
  {
    "id": 66,
    "new_members": [
      {
        "user_id": 5,
        "name": "Joe",
        "display_name": "Joe",
        "sections": [
          {
            "section_id": 2,
            "section_code": "Section 2"
          }
        ]
      },
      {
        "user_id": 11,
        "name": "Cecil",
        "display_name": "Cecil",
        "sections": [
          {
            "section_id": 3,
            "section_code": "Section 3"
          }
        ]
      }
    ]
  }
]
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).