---
title: Roles | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/roles
source: sitemap
fetched_at: 2026-02-15T09:04:46.257181-03:00
rendered_js: false
word_count: 893
summary: This document defines the API for managing account-level and course-level roles, including specifications for role objects and endpoints to list, retrieve, and create custom roles with specific permissions.
tags:
    - api-reference
    - roles-and-permissions
    - access-control
    - account-management
    - canvas-lms
    - granular-permissions
category: api
---

API for managing account- and course-level roles, and their associated permissions.

**A RolePermissions object looks like:**

```
{
  // Whether the role has the permission
"enabled": true,
  // Whether the permission is locked by this role
"locked": false,
  // Whether the permission applies to the account this role is in. Only present
  // if enabled is true
"applies_to_self": true,
  // Whether the permission cascades down to sub accounts of the account this role
  // is in. Only present if enabled is true
"applies_to_descendants": false,
  // Whether the permission can be modified in this role (i.e. whether the
  // permission is locked by an upstream role).
"readonly": false,
  // Whether the value of enabled is specified explicitly by this role, or
  // inherited from an upstream role.
"explicit": true,
  // The value that would have been inherited from upstream if the role had not
  // explicitly set a value. Only present if explicit is true.
"prior_default": false
}
```

**A Role object looks like:**

```
{
  // The id of the role
  "id": 1,
  // The label of the role.
  "label": "New Role",
  // The label of the role. (Deprecated alias for 'label')
  "role": "New Role",
  // The role type that is being used as a base for this role. For account-level
  // roles, this is 'AccountMembership'. For course-level roles, it is an
  // enrollment type.
  "base_role_type": "AccountMembership",
  // Whether this role applies to account memberships (i.e., not linked to an
  // enrollment in a course).
  "is_account_role": true,
  // JSON representation of the account the role is defined in.
  "account": {"id":1019,"name":"CGNU","parent_account_id":73,"root_account_id":1,"sis_account_id":"cgnu"},
  // The state of the role: 'active', 'inactive', or 'built_in'
  "workflow_state": "active",
  // The date and time the role was created.
  "created_at": "2020-12-01T16:20:00-06:00",
  // The date and time the role was last updated.
  "last_updated_at": "2023-10-31T23:59:00-06:00",
  // A dictionary of permissions keyed by name (see 'List assignable permissions'
  // API).
  "permissions": {"read_course_content":{"enabled":true,"locked":false,"readonly":false,"explicit":true,"prior_default":false},"read_course_list":{"enabled":true,"locked":true,"readonly":true,"explicit":false},"read_question_banks":{"enabled":false,"locked":true,"readonly":false,"explicit":true,"prior_default":false},"read_reports":{"enabled":true,"locked":false,"readonly":false,"explicit":false}}
}
```

**A Permission object looks like:**

```
// A permission that can be granted to a role
{
  // The API identifier for the permission
  "key": "manage_lti_add",
  // The human-readable label for the permission
  "label": "LTI - add",
  // The group this permission belongs to, if it is part of a granular permission
  // group
  "group": "manage_lti",
  // The human-readable label for the group this permission belongs to
  "group_label": "Manage LTI",
  // The base role types this permission can be enabled for
  "available_to": ["AccountAdmin", "AccountMembership", "TeacherEnrollment", "TaEnrollment", "DesignerEnrollment"],
  // The base role types this permission is enabled for by default
  "true_for": ["AccountAdmin", "TeacherEnrollment", "TaEnrollment", "DesignerEnrollment"]
}
```

**A PermissionHelpText object looks like:**

```
// Information about a permission, including its purpose and considerations for
// use.
{
  // Detailed explanations about what the permission does.
  "details": [{"title":"Add External Tools","description":"Allows users to add external tools (LTI) to courses."}],
  // A list of considerations or warnings about using the permission.
  "considerations": [{"title":"Security Risk","description":"Granting this permission may expose your system to security vulnerabilities."}]
}
```

[RoleOverridesController#api\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`GET /api/v1/accounts/:account_id/roles`

**Scope:** `url:GET|/api/v1/accounts/:account_id/roles`

A paginated list of the roles available to an account.

**Request Parameters:**

The id of the account to retrieve roles for.

Filter by role state. If this argument is omitted, only ‘active’ roles are returned.

Allowed values: `active`, `inactive`

If this argument is true, all roles inherited from parent accounts will be included.

Returns a list of [Role](https://developerdocs.instructure.com/services/canvas/resources/roles#role) objects.

[RoleOverridesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`GET /api/v1/accounts/:account_id/roles/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/roles/:id`

Retrieve information about a single role

**Request Parameters:**

The id of the account containing the role

The unique identifier for the role

Returns a [Role](https://developerdocs.instructure.com/services/canvas/resources/roles#role) object.

[RoleOverridesController#add\_rolearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`POST /api/v1/accounts/:account_id/roles`

**Scope:** `url:POST|/api/v1/accounts/:account_id/roles`

Create a new course-level or account-level role.

**Request Parameters:**

Deprecated alias for label.

Specifies the role type that will be used as a base for the permissions granted to this role.

Defaults to ‘AccountMembership’ if absent

Allowed values: `AccountMembership`, `StudentEnrollment`, `TeacherEnrollment`, `TaEnrollment`, `ObserverEnrollment`, `DesignerEnrollment`

`permissions[<X>][explicit]`

`permissions[<X>][enabled]`

If explicit is 1 and enabled is 1, permission &lt;X&gt; will be explicitly granted to this role. If explicit is 1 and enabled has any other value (typically 0), permission &lt;X&gt; will be explicitly denied to this role. If explicit is any other value (typically 0) or absent, or if enabled is absent, the value for permission &lt;X&gt; will be inherited from upstream. Ignored if permission &lt;X&gt; is locked upstream (in an ancestor account).

May occur multiple times with unique values for &lt;X&gt;. Recognized permission names for &lt;X&gt; can be found on the Permissions list page.

Some of these permissions are applicable only for roles on the site admin account, on a root account, or for course-level roles with a particular base role type; if a specified permission is inapplicable, it will be ignored.

Additional permissions may exist based on installed plugins.

A comprehensive list of all permissions are available:

Course Permissions PDF: [bit.ly/cnvs-course-permissionsarrow-up-right](http://bit.ly/cnvs-course-permissions)

Account Permissions PDF: [bit.ly/cnvs-acct-permissionsarrow-up-right](http://bit.ly/cnvs-acct-permissions)

If the value is 1, permission &lt;X&gt; will be locked downstream (new roles in subaccounts cannot override the setting). For any other value, permission &lt;X&gt; is left unlocked. Ignored if permission &lt;X&gt; is already locked upstream. May occur multiple times with unique values for &lt;X&gt;.

`permissions[<X>][applies_to_self]`

If the value is 1, permission &lt;X&gt; applies to the account this role is in. The default value is 1. Must be true if applies\_to\_descendants is false. This value is only returned if enabled is true.

`permissions[<X>][applies_to_descendants]`

If the value is 1, permission &lt;X&gt; cascades down to sub accounts of the account this role is in. The default value is 1. Must be true if applies\_to\_self is false.This value is only returned if enabled is true.

**Example Request:**

```
curl 'https://<canvas>/api/v1/accounts/<account_id>/roles.json' \
     -H "Authorization: Bearer <token>" \
     -F 'label=New Role' \
     -F 'permissions[read_course_content][explicit]=1' \
     -F 'permissions[read_course_content][enabled]=1' \
     -F 'permissions[read_course_list][locked]=1' \
     -F 'permissions[read_question_banks][explicit]=1' \
     -F 'permissions[read_question_banks][enabled]=0' \
     -F 'permissions[read_question_banks][locked]=1'
```

Returns a [Role](https://developerdocs.instructure.com/services/canvas/resources/roles#role) object.

[RoleOverridesController#remove\_rolearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`DELETE /api/v1/accounts/:account_id/roles/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/roles/:id`

Deactivates a custom role. This hides it in the user interface and prevents it from being assigned to new users. Existing users assigned to the role will continue to function with the same permissions they had previously. Built-in roles cannot be deactivated.

**Request Parameters:**

The unique identifier for the role

Returns a [Role](https://developerdocs.instructure.com/services/canvas/resources/roles#role) object.

[RoleOverridesController#activate\_rolearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`POST /api/v1/accounts/:account_id/roles/:id/activate`

**Scope:** `url:POST|/api/v1/accounts/:account_id/roles/:id/activate`

Re-activates an inactive role (allowing it to be assigned to new users)

**Request Parameters:**

The unique identifier for the role

Returns a [Role](https://developerdocs.instructure.com/services/canvas/resources/roles#role) object.

[RoleOverridesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`PUT /api/v1/accounts/:account_id/roles/:id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/roles/:id`

Update permissions for an existing role.

Recognized roles are:

- Any previously created custom role

**Request Parameters:**

The label for the role. Can only change the label of a custom role that belongs directly to the account.

`permissions[<X>][explicit]`

`permissions[<X>][enabled]`

These arguments are described in the documentation for the [add\_role method](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.add_role). The list of available permissions can be found on the Permissions list page.

`permissions[<X>][applies_to_self]`

If the value is 1, permission &lt;X&gt; applies to the account this role is in. The default value is 1. Must be true if applies\_to\_descendants is false. This value is only returned if enabled is true.

`permissions[<X>][applies_to_descendants]`

If the value is 1, permission &lt;X&gt; cascades down to sub accounts of the account this role is in. The default value is 1. Must be true if applies\_to\_self is false.This value is only returned if enabled is true.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/:account_id/roles/2 \
  -X PUT \
  -H 'Authorization: Bearer <access_token>' \
  -F 'label=New Role Name' \
  -F 'permissions[manage_groups][explicit]=1' \
  -F 'permissions[manage_groups][enabled]=1' \
  -F 'permissions[manage_groups][locked]=1' \
  -F 'permissions[send_messages][explicit]=1' \
  -F 'permissions[send_messages][enabled]=0'
```

Returns a [Role](https://developerdocs.instructure.com/services/canvas/resources/roles#role) object.

[RoleOverridesController#manageable\_permissionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/role_overrides_controller.rb)

`GET /api/v1/accounts/:account_id/roles/permissions`

**Scope:** `url:GET|/api/v1/accounts/:account_id/roles/permissions`

List all permissions that can be granted to roles in the given account.

This returns largely the same information documented on the Permissions list page, with a few caveats:

- Permission labels and group labels returned by this API are localized (the same text visible in the web UI).
- This API includes permissions added by plugins.
- This API excludes permissions that are disabled in or otherwise do not apply to the given account.

**Request Parameters:**

If provided, return only permissions whose key, label, group, or group\_label match the search string.

Returns a list of [Permission](https://developerdocs.instructure.com/services/canvas/resources/roles#permission) objects.

[PermissionsHelpController#helparrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/permissions_help_controller.rb)

`GET /api/v1/permissions/:context_type/:permission/help`

**Scope:** `url:GET|/api/v1/permissions/:context_type/:permission/help`

Retrieve information about what Canvas permissions do and considerations for their use.

**Example Request:**

```
curl -H 'Authorization: Bearer <token>' \
     https://<canvas>/api/v1/permissions/account/view_user_logins/help
```

Returns a [PermissionHelpText](https://developerdocs.instructure.com/services/canvas/resources/roles#permissionhelptext) object.

[PermissionsHelpController#groupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/permissions_help_controller.rb)

`GET /api/v1/permissions/groups`

**Scope:** `url:GET|/api/v1/permissions/groups`

Retrieve information about groups of granular permissions

The return value is a dictionary of permission group keys to objects containing `label` and `subtitle` keys.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).