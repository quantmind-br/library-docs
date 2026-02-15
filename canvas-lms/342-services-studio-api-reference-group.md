---
title: Group | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/studio/api-reference/group
source: sitemap
fetched_at: 2026-02-15T09:12:32.636493-03:00
rendered_js: false
word_count: 244
summary: This document provides technical specifications for API endpoints used to retrieve and manage user memberships and permissions within groups.
tags:
    - group-management
    - user-permissions
    - api-documentation
    - access-control
    - batch-update
    - rest-api
category: api
---

### Get details of users for a group

This endpoint will return the users with details and permission for a group

AuthorizationstringRequired

group\_idintegerRequired

ID of the group to retrieve users and their details

200

After a successful request, the endpoint returns HTTP 200.

401

Authorization information is missing or invalid.

403

If non-admin user or non-group member tries to call this endpoint, the call is rejected with 403 Forbidden.

404

If group is not found with the provided id, the endpoint returns HTTP 404.

422

Invalid group\_id is provided.

### Update users and theirs permissions for a group

This endpoint will update the users and their permissions for a group

AuthorizationstringRequired

group\_idintegerRequired

ID of the group to update users and their permissions

List of operations to perform

actionstring · enumRequired

Type of action to perform

Possible values:

user\_idintegerRequired

ID of the user to perform the action on

permissionstring · enumOptional

Permission to set for the user when action is add or update

Possible values:

200

After a successful request, the endpoint returns HTTP 200.

401

Authorization information is missing or invalid.

403

If non-admin user tries to call this endpoint, the call is rejected with 403 Forbidden.

404

If group is not found with the provided id, the endpoint returns HTTP 404.

422

Invalid group\_id or changes are provided.

/groups/{group\_id}/users/batch\_update

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).