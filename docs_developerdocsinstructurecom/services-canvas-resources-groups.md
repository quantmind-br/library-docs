---
title: Groups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/groups
source: sitemap
fetched_at: 2026-02-15T08:56:35.795143-03:00
rendered_js: false
word_count: 1341
summary: This document defines the structure and behavior of Group and GroupMembership objects within the Canvas LMS and provides API endpoint specifications for managing group data across accounts and courses.
tags:
    - canvas-lms
    - groups-api
    - group-memberships
    - api-endpoints
    - course-management
    - rest-api
category: api
---

Groups serve as the data for a few different ideas in Canvas. The first is that they can be a community in the canvas network. The second is that they can be organized by students in a course, for study or communication (but not grading). The third is that they can be organized by teachers or account administrators for the purpose of projects, assignments, and grading. This last kind of group is always part of a group category, which adds the restriction that a user may only be a member of one group per category.

All of these types of groups function similarly, and can be the parent context for many other types of functionality and interaction, such as collections, discussions, wikis, and shared files.

Group memberships are the objects that tie users and groups together.

**A Group object looks like:**

```
{
  // The ID of the group.
"id": 17,
  // The display name of the group.
"name": "Math Group 1",
  // A description of the group. This is plain text.
"description": null,
  // Whether or not the group is public.  Currently only community groups can be
  // made public.  Also, once a group has been set to public, it cannot be changed
  // back to private.
"is_public": false,
  // Whether or not the current user is following this group.
"followed_by_user": false,
  // How people are allowed to join the group.  For all groups except for
  // community groups, the user must share the group's parent course or account. 
  // For student organized or community groups, where a user can be a member of as
  // many or few as they want, the applicable levels are
  // 'parent_context_auto_join', 'parent_context_request', and 'invitation_only'. 
  // For class groups, where students are divided up and should only be part of
  // one group of the category, this value will always be 'invitation_only', and
  // is not relevant. * If 'parent_context_auto_join', anyone can join and will be
  // automatically accepted. * If 'parent_context_request', anyone  can request to
  // join, which must be approved by a group moderator. * If 'invitation_only',
  // only those how have received an invitation my join the group, by accepting
  // that invitation.
"join_level": "invitation_only",
  // The number of members currently in the group
"members_count": 0,
  // The url of the group's avatar
"avatar_url": "https://<canvas>/files/avatar_image.png",
  // The course or account that the group belongs to. The pattern here is that
  // whatever the context_type is, there will be an _id field named after that
  // type. So if instead context_type was 'account', the course_id field would be
  // replaced by an account_id field.
"context_type": "Course",
  // The course or account name that the group belongs to.
"context_name": "Course 101",
"course_id": 3,
  // Certain types of groups have special role designations. Currently, these
  // include: 'communities', 'student_organized', and 'imported'. Regular
  // course/account groups have a role of null.
"role": null,
  // The ID of the group's category.
"group_category_id": 4,
  // The SIS ID of the group. Only included if the user has permission to view SIS
  // information.
"sis_group_id": "group4a",
  // The id of the SIS import if created through SIS. Only included if the user
  // has permission to manage SIS information.
"sis_import_id": 14,
  // the storage quota for the group, in megabytes
"storage_quota_mb": 50,
  // optional: the permissions the user has for the group. returned only for a
  // single group and include[]=permissions
"permissions": {"create_discussion_topic":true,"create_announcement":true},
  // optional: A list of users that are members in the group. Returned only if
  // include[]=users. WARNING: this collection's size is capped (if there are an
  // extremely large number of users in the group (thousands) not all of them will
  // be returned). If you need to capture all the users in a group with certainty
  // or experiencing slow response consider using the paginated
  // /api/v1/groups/<group_id>/users endpoint.
"users": null,
  // Indicates whether this group category is non-collaborative. A value of true
  // means these group categories rely on the manage_tags permissions and do not
  // have collaborative features
"non_collaborative": null
}
```

**A GroupMembership object looks like:**

```
{
  // The id of the membership object
  "id": 92,
  // The id of the group object to which the membership belongs
  "group_id": 17,
  // The id of the user object to which the membership belongs
  "user_id": 3,
  // The current state of the membership. Current possible values are 'accepted',
  // 'invited', and 'requested'
  "workflow_state": "accepted",
  // Whether or not the user is a moderator of the group (the must also be an
  // active member of the group to moderate)
  "moderator": true,
  // optional: whether or not the record was just created on a create call (POST),
  // i.e. was the user just added to the group, or was the user already a member
  "just_created": true,
  // The id of the SIS import if created through SIS. Only included if the user
  // has permission to manage SIS information.
  "sis_import_id": 4
}
```

[GroupsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/users/self/groups`

**Scope:** `url:GET|/api/v1/users/self/groups`

Returns a paginated list of active groups for the current user.

**Request Parameters:**

Only include groups that are in this type of context.

Allowed values: `Account`, `Course`

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/groups?context_type=Account \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) objects.

[GroupsController#context\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/accounts/:account_id/groups`

**Scope:** `url:GET|/api/v1/accounts/:account_id/groups`

`GET /api/v1/courses/:course_id/groups`

**Scope:** `url:GET|/api/v1/courses/:course_id/groups`

Returns the paginated list of active groups in the given context that are visible to user.

**Request Parameters:**

Will only include groups that the user belongs to if this is set

Filter groups by their collaboration state:

- “all”: Return both collaborative and non-collaborative groups
- “collaborative”: Return only collaborative groups (default)
- “non\_collaborative”: Return only non-collaborative groups

**Example Request:**

```
curl https://<canvas>/api/v1/courses/1/groups \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) objects.

[GroupsController#bulk\_user\_tagsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/courses/:course_id/bulk_user_tags`

**Scope:** `url:GET|/api/v1/courses/:course_id/bulk_user_tags`

Returns a mapping of user IDs to arrays of non-collaborative group (tag) IDs for each user in the given course.

**Request Parameters:**

The ID of the course context (from the route).

An array of user IDs to fetch tags for.

**Example Request:**

```
curl "https://<canvas>/api/v1/courses/1/bulk_user_tags?user_ids[]=35&user_ids[]=79" \
     -H 'Authorization: Bearer <token>'
```

[GroupsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/groups/:group_id`

**Scope:** `url:GET|/api/v1/groups/:group_id`

Returns the data for a single group, or a 401 if the caller doesn’t have the rights to see it.

**Request Parameters:**

- “permissions”: Include permissions the current user has for the group.

Allowed values: `permissions`, `tabs`

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id> \
     -H 'Authorization: Bearer <token>'
```

Returns a [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) object.

[GroupsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`POST /api/v1/groups`

**Scope:** `url:POST|/api/v1/groups`

`POST /api/v1/group_categories/:group_category_id/groups`

**Scope:** `url:POST|/api/v1/group_categories/:group_category_id/groups`

Creates a new group. Groups created using the “/api/v1/groups/” endpoint will be community groups.

**Request Parameters:**

A description of the group

whether the group is public (applies only to community groups)

no description

Allowed values: `parent_context_auto_join`, `parent_context_request`, `invitation_only`

The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage\_storage\_quotas permission.

The sis ID of the group. Must have manage\_sis permission to set.

**Example Request:**

```
curl https://<canvas>/api/v1/groups \
     -F 'name=Math Teachers' \
     -F 'description=A place to gather resources for our classes.' \
     -F 'is_public=true' \
     -F 'join_level=parent_context_auto_join' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) object.

[GroupsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`PUT /api/v1/groups/:group_id`

**Scope:** `url:PUT|/api/v1/groups/:group_id`

Modifies an existing group. Note that to set an avatar image for the group, you must first upload the image file to the group, and the use the id in the response as the argument to this function. See the [File Upload Documentation](https://developerdocs.instructure.com/services/canvas/basics/file.file_uploads) for details on the file upload workflow.

**Request Parameters:**

A description of the group

Whether the group is public (applies only to community groups). Currently you cannot set a group back to private once it has been made public.

no description

Allowed values: `parent_context_auto_join`, `parent_context_request`, `invitation_only`

The id of the attachment previously uploaded to the group that you would like to use as the avatar image for this group.

The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage\_storage\_quotas permission.

An array of user ids for users you would like in the group. Users not in the group will be sent invitations. Existing group members who aren’t in the list will be removed from the group.

The sis ID of the group. Must have manage\_sis permission to set.

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id> \
     -X PUT \
     -F 'name=Algebra Teachers' \
     -F 'join_level=parent_context_request' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) object.

[GroupsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`DELETE /api/v1/groups/:group_id`

**Scope:** `url:DELETE|/api/v1/groups/:group_id`

Deletes a group and removes all members.

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id> \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Returns a [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) object.

[GroupsController#invitearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`POST /api/v1/groups/:group_id/invite`

**Scope:** `url:POST|/api/v1/groups/:group_id/invite`

Sends an invitation to all supplied email addresses which will allow the receivers to join the group.

**Request Parameters:**

An array of email addresses to be sent invitations.

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/invite \
     -F 'invitees[]=leonard@example.com' \
     -F 'invitees[]=sheldon@example.com' \
     -H 'Authorization: Bearer <token>'
```

[GroupsController#usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/groups/:group_id/users`

**Scope:** `url:GET|/api/v1/groups/:group_id/users`

Returns a paginated list of users in the group.

**Request Parameters:**

The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters.

“avatar\_url”: Include users’ avatar\_urls.

Allowed values: `avatar_url`

Whether to filter out inactive users from the results. Defaults to false unless explicitly provided.

**Example Request:**

```
curl https://<canvas>/api/v1/groups/1/users \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[GroupsController#create\_filearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`POST /api/v1/groups/:group_id/files`

**Scope:** `url:POST|/api/v1/groups/:group_id/files`

Upload a file to the group.

This API endpoint is the first step in uploading a file to a group. See the [File Upload Documentationarrow-up-right](https://github.com/instructure/api-docu-portal/blob/prod/gitbook/services/canvas/file_uploads.md) for details on the file upload workflow.

Only those with the “Manage Files” permission on a group can upload files to the group. By default, this is anybody participating in the group, or any admin over the group.

[GroupsController#preview\_htmlarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`POST /api/v1/groups/:group_id/preview_html`

**Scope:** `url:POST|/api/v1/groups/:group_id/preview_html`

Preview html content processed for this group

**Request Parameters:**

The html content to process

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/preview_html \
     -F 'html=<p><badhtml></badhtml>processed html</p>' \
     -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{
  "html": "<p>processed html</p>"
}
```

[GroupsController#activity\_streamarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/groups/:group_id/activity_stream`

**Scope:** `url:GET|/api/v1/groups/:group_id/activity_stream`

Returns the current user’s group-specific activity stream, paginated.

For full documentation, see the API documentation for the user activity stream, in the user api.

[GroupsController#activity\_stream\_summaryarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/groups/:group_id/activity_stream/summary`

**Scope:** `url:GET|/api/v1/groups/:group_id/activity_stream/summary`

Returns a summary of the current user’s group-specific activity stream.

For full documentation, see the API documentation for the user activity stream summary, in the user api.

[GroupsController#permissionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/groups_controller.rb)

`GET /api/v1/groups/:group_id/permissions`

**Scope:** `url:GET|/api/v1/groups/:group_id/permissions`

Returns permission information for the calling user in the given group. See also the [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts#method.accounts.permissions) and [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#method.courses.permissions) counterparts.

**Request Parameters:**

List of permissions to check against the authenticated user. Permission names are documented in the [List assignable permissions](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.manageable_permissions) endpoint.

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/permissions \
  -H 'Authorization: Bearer <token>' \
  -d 'permissions[]=read_roster'
  -d 'permissions[]=send_messages_all'
```

**Example Response:**

```
{'read_roster': 'true', 'send_messages_all': 'false'}
```

[GroupMembershipsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_memberships_controller.rb)

`GET /api/v1/groups/:group_id/memberships`

**Scope:** `url:GET|/api/v1/groups/:group_id/memberships`

A paginated list of the members of a group.

**Request Parameters:**

Only list memberships with the given workflow\_states. By default it will return all memberships.

Allowed values: `accepted`, `invited`, `requested`

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/memberships \
     -F 'filter_states[]=invited&filter_states[]=requested' \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [GroupMembership](https://developerdocs.instructure.com/services/canvas/resources/groups#groupmembership) objects.

[GroupMembershipsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_memberships_controller.rb)

`GET /api/v1/groups/:group_id/memberships/:membership_id`

**Scope:** `url:GET|/api/v1/groups/:group_id/memberships/:membership_id`

`GET /api/v1/groups/:group_id/users/:user_id`

**Scope:** `url:GET|/api/v1/groups/:group_id/users/:user_id`

Returns the group membership with the given membership id or user id.

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/memberships/<membership_id> \
     -H 'Authorization: Bearer <token>'
```

```
curl https://<canvas>/api/v1/groups/<group_id>/users/<user_id> \
     -H 'Authorization: Bearer <token>'
```

Returns a [GroupMembership](https://developerdocs.instructure.com/services/canvas/resources/groups#groupmembership) object.

[GroupMembershipsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_memberships_controller.rb)

`POST /api/v1/groups/:group_id/memberships`

**Scope:** `url:POST|/api/v1/groups/:group_id/memberships`

Join, or request to join, a group, depending on the join\_level of the group. If the membership or join request already exists, then it is simply returned.

For differentiation tags, you can bulk add users using one of two methods:

1. Provide an array of user IDs via the ‘members\[]\` parameter.
2. Use the course-wide option with the following parameters:
   
   - ‘all\_in\_group\_course\` \[Boolean]: If set to true, the endpoint will add every currently enrolled student (from the course context) to the differentiation tag.
   - ‘exclude\_user\_ids\[]\` \[Integer]: When using \`all\_in\_group\_course\`, you can optionally exclude specific users by providing their IDs in this parameter.

In this context, these parameters only apply to differentiation tag memberships.

**Request Parameters:**

- The ID of the user for individual membership creation.

<!--THE END-->

- Bulk add multiple users to a differentiation tag.

<!--THE END-->

- If true, add all enrolled students from the course.

<!--THE END-->

- An array of user IDs to exclude when using all\_in\_group\_course.

**Example Request:**

```
(Individual membership creation)
curl https://<canvas>/api/v1/groups/<group_id>/memberships \
     -F 'user_id=self' \
     -H 'Authorization: Bearer <token>'
```

```
(Bulk addition using members array)
curl https://<canvas>/api/v1/groups/<group_id>/memberships \
     -F 'members[]=123' \
     -F 'members[]=456' \
     -H 'Authorization: Bearer <token>'
```

```
(Bulk addition using all_in_group_course with exclusions)
curl https://<canvas>/api/v1/groups/<group_id>/memberships \
     -F 'all_in_group_course=true' \
     -F 'exclude_user_ids[]=123' \
     -H 'Authorization: Bearer <token>'
```

[GroupMembershipsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_memberships_controller.rb)

`PUT /api/v1/groups/:group_id/memberships/:membership_id`

**Scope:** `url:PUT|/api/v1/groups/:group_id/memberships/:membership_id`

`PUT /api/v1/groups/:group_id/users/:user_id`

**Scope:** `url:PUT|/api/v1/groups/:group_id/users/:user_id`

Accept a membership request, or add/remove moderator rights.

**Request Parameters:**

Currently, the only allowed value is “accepted”

Allowed values: `accepted`

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/memberships/<membership_id> \
     -F 'moderator=true'
     -H 'Authorization: Bearer <token>'
```

```
curl https://<canvas>/api/v1/groups/<group_id>/users/<user_id> \
     -F 'moderator=true'
     -H 'Authorization: Bearer <token>'
```

Returns a [GroupMembership](https://developerdocs.instructure.com/services/canvas/resources/groups#groupmembership) object.

[GroupMembershipsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_memberships_controller.rb)

`DELETE /api/v1/groups/:group_id/memberships/:membership_id`

**Scope:** `url:DELETE|/api/v1/groups/:group_id/memberships/:membership_id`

`DELETE /api/v1/groups/:group_id/users/:user_id`

**Scope:** `url:DELETE|/api/v1/groups/:group_id/users/:user_id`

Leave a group if you are allowed to leave (some groups, such as sets of course groups created by teachers, cannot be left). You may also use ‘self’ in place of a membership\_id.

**Example Request:**

```
curl https://<canvas>/api/v1/groups/<group_id>/memberships/<membership_id> \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

```
curl https://<canvas>/api/v1/groups/<group_id>/users/<user_id> \
     -X DELETE \
     -H 'Authorization: Bearer <token>'
```

Bulk deletes memberships by providing an array of user IDs.](#method.group\_memberships.destroy\_bulk)

[GroupMembershipsController#destroy\_bulkarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/group_memberships_controller.rb)

`DELETE /api/v1/groups/:group_id/users`

**Scope:** `url:DELETE|/api/v1/groups/:group_id/users`

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).