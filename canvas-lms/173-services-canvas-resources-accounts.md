---
title: Accounts | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/accounts
source: sitemap
fetched_at: 2026-02-15T09:05:51.024606-03:00
rendered_js: false
word_count: 2099
summary: This document provides technical specifications for the Canvas LMS Accounts API, defining data schemas for account objects and detailing endpoints for retrieving account lists and settings.
tags:
    - canvas-lms
    - rest-api
    - account-management
    - api-documentation
    - json-schema
    - student-information-system
category: api
---

API for accessing account data.

**An Account object looks like:**

```
{
  // the ID of the Account object
"id": 2,
  // The display name of the account
"name": "Canvas Account",
  // The UUID of the account
"uuid": "WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5",
  // The account's parent ID, or null if this is the root account
"parent_account_id": 1,
  // The ID of the root account, or null if this is the root account
"root_account_id": 1,
  // The storage quota for the account in megabytes, if not otherwise specified
"default_storage_quota_mb": 500,
  // The storage quota for a user in the account in megabytes, if not otherwise
  // specified
"default_user_storage_quota_mb": 50,
  // The storage quota for a group in the account in megabytes, if not otherwise
  // specified
"default_group_storage_quota_mb": 50,
  // The default time zone of the account. Allowed time zones are
  // {http://www.iana.org/time-zones IANA time zones} or friendlier
  // {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails
  // time zones}.
"default_time_zone": "America/Denver",
  // The account's identifier in the Student Information System. Only included if
  // the user has permission to view SIS information.
"sis_account_id": "123xyz",
  // The account's identifier in the Student Information System. Only included if
  // the user has permission to view SIS information.
"integration_id": "123xyz",
  // The id of the SIS import if created through SIS. Only included if the user
  // has permission to manage SIS information.
"sis_import_id": 12,
  // The number of courses directly under the account (available via include)
"course_count": 10,
  // The number of sub-accounts directly under the account (available via include)
"sub_account_count": 10,
  // The account's identifier that is sent as context_id in LTI launches.
"lti_guid": "123xyz",
  // The state of the account. Can be 'active' or 'deleted'.
"workflow_state": "active"
}
```

**A TermsOfService object looks like:**

```
{
  // Terms Of Service id
  "id": 1,
  // The given type for the Terms of Service
  "terms_type": "default",
  // Boolean dictating if the user must accept Terms of Service
  "passive": false,
  // The id of the root account that owns the Terms of Service
  "account_id": 1,
  // Content of the Terms of Service
  "content": "To be or not to be that is the question",
  // The type of self registration allowed
  "self_registration_type": "["none", "observer", "all"]"
}
```

**A HelpLink object looks like:**

```
{
  // The ID of the help link
  "id": "instructor_question",
  // The name of the help link
  "text": "Ask Your Instructor a Question",
  // The description of the help link
  "subtext": "Questions are submitted to your instructor",
  // The URL of the help link
  "url": "#teacher_feedback",
  // The type of the help link
  "type": "default",
  // The roles that have access to this help link
  "available_to": ["user", "student", "teacher", "admin", "observer", "unenrolled"]
}
```

**A HelpLinks object looks like:**

```
{
  // Help link button title
  "help_link_name": "Help And Policies",
  // Help link button icon
  "help_link_icon": "help",
  // Help links defined by the account. Could include default help links.
  "custom_help_links": [{"id":"link1","text":"Custom Link!","subtext":"Something something.","url":"https:\/\/google.com","type":"custom","available_to":["user","student","teacher","admin","observer","unenrolled"],"is_featured":true,"is_new":false,"feature_headline":"Check this out!"}],
  // Default help links provided when account has not set help links of their own.
  "default_help_links": [{"available_to":["student"],"text":"Ask Your Instructor a Question","subtext":"Questions are submitted to your instructor","url":"#teacher_feedback","type":"default","id":"instructor_question","is_featured":false,"is_new":true,"feature_headline":""}, {"available_to":["user","student","teacher","admin","observer","unenrolled"],"text":"Search the Canvas Guides","subtext":"Find answers to common questions","url":"https:\/\/community.canvaslms.com\/t5\/Guides\/ct-p\/guides","type":"default","id":"search_the_canvas_guides","is_featured":false,"is_new":false,"feature_headline":""}, {"available_to":["user","student","teacher","admin","observer","unenrolled"],"text":"Report a Problem","subtext":"If Canvas misbehaves, tell us about it","url":"#create_ticket","type":"default","id":"report_a_problem","is_featured":false,"is_new":false,"feature_headline":""}]
}
```

[AccountsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts`

**Scope:** `url:GET|/api/v1/accounts`

A paginated list of accounts that the current user can view or manage. Typically, students and even teachers will get an empty list in response, only account admins can view the accounts that they are in.

**Request Parameters:**

Array of additional information to include.

- “lti\_guid”
  
  the ‘tool\_consumer\_instance\_guid’ that will be sent for this account on LTI launches
- “registration\_settings”
  
  returns info about the privacy policy and terms of use
- “services”
  
  returns services and whether they are enabled (requires account management permissions)
- “course\_count”
  
  returns the number of courses directly under each account
- “sub\_account\_count”
  
  returns the number of sub-accounts directly under each account

Allowed values: `lti_guid`, `registration_settings`, `services`, `course_count`, `sub_account_count`

Returns a list of [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) objects.

[AccountsController#manageable\_accountsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/manageable_accounts`

**Scope:** `url:GET|/api/v1/manageable_accounts`

A paginated list of accounts where the current user has permission to create or manage courses. List will be empty for students and teachers as only admins can view which accounts they are in.

Returns a list of [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) objects.

[AccountsController#course\_creation\_accountsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/course_creation_accounts`

**Scope:** `url:GET|/api/v1/course_creation_accounts`

A paginated list of accounts where the current user has permission to create courses.

Returns a list of [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) objects.

[AccountsController#course\_accountsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/course_accounts`

**Scope:** `url:GET|/api/v1/course_accounts`

A paginated list of accounts that the current user can view through their admin course enrollments. (Teacher, TA, or designer enrollments). Only returns “id”, “name”, “workflow\_state”, “root\_account\_id” and “parent\_account\_id”

Returns a list of [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) objects.

[AccountsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:id`

**Scope:** `url:GET|/api/v1/accounts/:id`

Retrieve information on an individual account, given by id or sis sis\_account\_id.

Returns an [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) object.

[AccountsController#show\_settingsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:account_id/settings`

**Scope:** `url:GET|/api/v1/accounts/:account_id/settings`

Returns a JSON object containing a subset of settings for the specified account. It’s possible an empty set will be returned if no settings are applicable. The caller must be an Account admin with the manage\_account\_settings permission.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/<account_id>/settings \
  -H 'Authorization: Bearer <token>'
```

**Example Response:**

```
{"microsoft_sync_enabled": true, "microsoft_sync_login_attribute_suffix": false}
```

[AccountsController#environmentarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/settings/environment`

**Scope:** `url:GET|/api/v1/settings/environment`

Return a hash of global settings for the root account This is the same information supplied to the web interface as `ENV.SETTINGS`.

**Example Request:**

```
curl 'http://<canvas>/api/v1/settings/environment' \
  -H "Authorization: Bearer <token>"
```

**Example Response:**

```
{ "calendar_contexts_limit": 10, "open_registration": false, ...}
```

[AccountsController#permissionsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:account_id/permissions`

**Scope:** `url:GET|/api/v1/accounts/:account_id/permissions`

Returns permission information for the calling user and the given account. You may use ‘self\` as the account id to check permissions against the domain root account. The caller must have an account role or admin (teacher/TA/designer) enrollment in a course in the account.

See also the [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#method.courses.permissions) and [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#method.groups.permissions) counterparts.

**Request Parameters:**

List of permissions to check against the authenticated user. Permission names are documented in the [List assignable permissions](https://developerdocs.instructure.com/services/canvas/resources/roles#method.role_overrides.manageable_permissions) endpoint.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/self/permissions \
  -H 'Authorization: Bearer <token>' \
  -d 'permissions[]=manage_account_memberships' \
  -d 'permissions[]=become_user'
```

**Example Response:**

```
{'manage_account_memberships': 'false', 'become_user': 'true'}
```

[AccountsController#sub\_accountsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:account_id/sub_accounts`

**Scope:** `url:GET|/api/v1/accounts/:account_id/sub_accounts`

List accounts that are sub-accounts of the given account.

**Request Parameters:**

If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false.

Sorts the accounts by id or name. Only applies when recursive is false. Defaults to id.

Allowed values: `id`, `name`

Array of additional information to include.

- “course\_count”
  
  returns the number of courses directly under each account
- “sub\_account\_count”
  
  returns the number of sub-accounts directly under each account

Allowed values: `course_count`, `sub_account_count`

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/<account_id>/sub_accounts \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) objects.

[AccountsController#terms\_of\_servicearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:account_id/terms_of_service`

**Scope:** `url:GET|/api/v1/accounts/:account_id/terms_of_service`

Returns the terms of service for that account

Returns a [TermsOfService](https://developerdocs.instructure.com/services/canvas/resources/accounts#termsofservice) object.

[AccountsController#help\_linksarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:account_id/help_links`

**Scope:** `url:GET|/api/v1/accounts/:account_id/help_links`

Returns the help links for that account

Returns a [HelpLinks](https://developerdocs.instructure.com/services/canvas/resources/accounts#helplinks) object.

[AccountsController#manually\_created\_courses\_accountarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/manually_created_courses_account`

**Scope:** `url:GET|/api/v1/manually_created_courses_account`

Returns the sub-account that contains manually created courses for the domain root account.

Returns an [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) object.

[AccountsController#courses\_apiarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`GET /api/v1/accounts/:account_id/courses`

**Scope:** `url:GET|/api/v1/accounts/:account_id/courses`

Retrieve a paginated list of courses in this account.

**Request Parameters:**

If true, include only courses with at least one enrollment. If false, include only courses with no enrollments. If not present, do not filter on course enrollment status.

If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment types.

Allowed values: `teacher`, `student`, `ta`, `observer`, `designer`

`enrollment_workflow_state[]`

If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment workflow states.

Allowed values: `active`, `completed`, `deleted`, `invited`, `pending`, `creation_pending`, `rejected`, `inactive`

If true, include only published courses. If false, exclude published courses. If not present, do not filter on published status.

If true, include only completed courses (these may be in state ‘completed’, or their enrollment term may have ended). If false, exclude completed courses. If not present, do not filter on completed status.

If true, include only blueprint courses. If false, exclude them. If not present, do not filter on this basis.

If true, include only courses that inherit content from a blueprint course. If false, exclude them. If not present, do not filter on this basis.

If true, include only public courses. If false, exclude them. If not present, do not filter on this basis.

List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users.

List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts.

`hide_enrollmentless_courses`

If present, only return courses that have at least one enrollment. Equivalent to ‘with\_enrollments=true’; retained for compatibility.

If set, only return courses that are in the given state(s). By default, all states but “deleted” are returned.

Allowed values: `created`, `claimed`, `available`, `completed`, `deleted`, `all`

If set, only includes courses from the specified term.

The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters.

- “sections”, “needs\_grading\_count” and “total\_scores” are not valid options at the account level

Allowed values: `syllabus_body`, `term`, `course_progress`, `storage_quota_used_mb`, `total_students`, `teachers`, `account_name`, `concluded`, `post_manually`

The column to sort results by.

Allowed values: `course_status`, `course_name`, `sis_course_id`, `teacher`, `account_name`

The order to sort the given column by.

Allowed values: `asc`, `desc`

The filter to search by. “course” searches for course names, course codes, and SIS IDs. “teacher” searches for teacher names

Allowed values: `course`, `teacher`

If set, only return courses that start before the value (inclusive) or their enrollment term starts before the value (inclusive) or both the course’s start\_at and the enrollment term’s start\_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

If set, only return courses that end after the value (inclusive) or their enrollment term ends after the value (inclusive) or both the course’s end\_at and the enrollment term’s end\_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.

If set, only return homeroom courses.

Returns a list of [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) objects.

[AccountsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`PUT /api/v1/accounts/:id`

**Scope:** `url:PUT|/api/v1/accounts/:id`

Update an existing account.

**Request Parameters:**

Updates the account sis\_account\_id Must have manage\_sis permission and must not be a root\_account.

`account[default_time_zone]`

`account[default_storage_quota_mb]`

The default course storage quota to be used, if not otherwise specified.

`account[default_user_storage_quota_mb]`

The default user storage quota to be used, if not otherwise specified.

`account[default_group_storage_quota_mb]`

The default group storage quota to be used, if not otherwise specified.

`account[course_template_id]`

The ID of a course to be used as a template for all newly created courses. Empty means to inherit the setting from parent account, 0 means to not use a template even if a parent account has one set. The course must be marked as a template.

`account[parent_account_id]`

The ID of a parent account to move the account to. The new parent account must be in the same root account as the original. The hierarchy of sub-accounts will be preserved in the new parent account. The caller must be an administrator in both the original parent account and the new parent account.

`account[settings][restrict_student_past_view][value]`

Restrict students from viewing courses after end date

`account[settings][restrict_student_past_view][locked]`

Lock this setting for sub-accounts and courses

`account[settings][restrict_student_future_view][value]`

Restrict students from viewing courses before start date

`account[settings][microsoft_sync_enabled]`

Determines whether this account has Microsoft Teams Sync enabled or not.

Note that if you are altering Microsoft Teams sync settings you must enable the Microsoft Group enrollment syncing feature flag. In addition, if you are enabling Microsoft Teams sync, you must also specify a tenant, login attribute, and a remote attribute. Specifying a suffix to use is optional.

`account[settings][microsoft_sync_tenant]`

The tenant this account should use when using Microsoft Teams Sync. This should be an Azure Active Directory domain name.

`account[settings][microsoft_sync_login_attribute]`

The attribute this account should use to lookup users when using Microsoft Teams Sync. Must be one of “sub”, “email”, “oid”, “preferred\_username”, or “integration\_id”.

`account[settings][microsoft_sync_login_attribute_suffix]`

A suffix that will be appended to the result of the login attribute when associating Canvas users with Microsoft users. Must be under 255 characters and contain no whitespace. This field is optional.

`account[settings][microsoft_sync_remote_attribute]`

The Active Directory attribute to use when associating Canvas users with Microsoft users. Must be one of “mail”, “mailNickname”, or “userPrincipalName”.

`account[settings][restrict_student_future_view][locked]`

Lock this setting for sub-accounts and courses

`account[settings][lock_all_announcements][value]`

Disable comments on announcements

`account[settings][lock_all_announcements][locked]`

Lock this setting for sub-accounts and courses

`account[settings][usage_rights_required][value]`

Copyright and license information must be provided for files before they are published.

`account[settings][usage_rights_required][locked]`

Lock this setting for sub-accounts and courses

`account[settings][restrict_student_future_listing][value]`

Restrict students from viewing future enrollments in course list

`account[settings][restrict_student_future_listing][locked]`

Lock this setting for sub-accounts and courses

`account[settings][conditional_release][value]`

Enable or disable individual learning paths for students based on assessment

`account[settings][conditional_release][locked]`

Lock this setting for sub-accounts and courses

`account[settings][enable_course_paces][value]`

Enable or disable course pacing

`account[settings][enable_course_paces][locked]`

Lock this setting for sub-accounts and courses

`account[settings][password_policy]`

Hash of optional password policy configuration parameters for a root account

- allow\_login\_suspension boolean
  
  Allow suspension of user logins upon reaching maximum\_login\_attempts
- require\_number\_characters boolean
  
  Require the use of number characters when setting up a new password
- require\_symbol\_characters boolean
  
  Require the use of symbol characters when setting up a new password
- minimum\_character\_length integer
  
  Minimum number of characters required for a new password
- maximum\_login\_attempts integer
  
  Maximum number of login attempts before a user is locked out

*Required* feature option:

`account[settings][enable_as_k5_account][value]`

Enable or disable Canvas for Elementary for this account

`account[settings][use_classic_font_in_k5][value]`

Whether or not the classic font is used on the dashboard. Only applies if enable\_as\_k5\_account is true.

`account[settings][horizon_account][value]`

Enable or disable Canvas Career for this account

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

`account[settings][lock_outcome_proficiency][value]`

- DEPRECATED
  
  Restrict instructors from changing mastery scale

`account[lock_outcome_proficiency][locked]`

- DEPRECATED
  
  Lock this setting for sub-accounts and courses

`account[settings][lock_proficiency_calculation][value]`

- DEPRECATED
  
  Restrict instructors from changing proficiency calculation method

`account[lock_proficiency_calculation][locked]`

- DEPRECATED
  
  Lock this setting for sub-accounts and courses

Give this a set of keys and boolean values to enable or disable services matching the keys

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/<account_id> \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'account[name]=New account name' \
  -d 'account[default_time_zone]=Mountain Time (US & Canada)' \
  -d 'account[default_storage_quota_mb]=450'
```

Returns an [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) object.

[AccountsController#remove\_userarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`DELETE /api/v1/accounts/:account_id/users/:user_id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/users/:user_id`

Delete a user record from a Canvas root account. If a user is associated with multiple root accounts (in a multi-tenant instance of Canvas), this action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account. If they do this, they won’t be able to make API calls or log into Canvas at that account.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/3/users/5 \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -X DELETE
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[AccountsController#remove\_usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`DELETE /api/v1/accounts/:account_id/users`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/users`

Delete multiple users from a Canvas root account. If a user is associated with multiple root accounts (in a multi-tenant instance of Canvas), this action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account. If they do this, they won’t be able to make API calls or log into Canvas at that account.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/3/users \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -X DELETE
  -d 'user_ids[]=1' \
  -d 'user_ids[]=2'
```

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[AccountsController#update\_usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`PUT /api/v1/accounts/:account_id/users/bulk_update`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/users/bulk_update`

Updates multiple users in bulk.

**Request Parameters:**

- Array
  
  The IDs of the users to update.

The attributes to update for each user.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/3/users/bulk_update \
  -X PUT \
  -H 'Authorization: Bearer <token>' \
  -d 'user_ids[]=1' \
  -d 'user_ids[]=2' \
  -d 'user[event]=suspend'
```

Returns a [Progress](https://developerdocs.instructure.com/services/canvas/resources/progress#progress) object.

[AccountsController#restore\_userarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/accounts_controller.rb)

`PUT /api/v1/accounts/:account_id/users/:user_id/restore`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/users/:user_id/restore`

Restore a user record along with the most recently deleted pseudonym from a Canvas root account.

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/3/users/5/restore \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -X PUT
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[SubAccountsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sub_accounts_controller.rb)

`POST /api/v1/accounts/:account_id/sub_accounts`

**Scope:** `url:POST|/api/v1/accounts/:account_id/sub_accounts`

Add a new sub-account to a given account.

**Request Parameters:**

The name of the new sub-account.

The account’s identifier in the Student Information System.

`account[default_storage_quota_mb]`

The default course storage quota to be used, if not otherwise specified.

`account[default_user_storage_quota_mb]`

The default user storage quota to be used, if not otherwise specified.

`account[default_group_storage_quota_mb]`

The default group storage quota to be used, if not otherwise specified.

Returns an [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) object.

[SubAccountsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/sub_accounts_controller.rb)

`DELETE /api/v1/accounts/:account_id/sub_accounts/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/sub_accounts/:id`

Cannot delete an account with active courses or active sub\_accounts. Cannot delete a root\_account

Returns an [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).