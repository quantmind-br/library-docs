---
title: Collaborations | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/collaborations
source: sitemap
fetched_at: 2026-02-15T09:05:34.366309-03:00
rendered_js: false
word_count: 229
summary: This document defines the REST API endpoints for accessing and managing course and group collaborations, including detailed specifications for collaboration and collaborator objects.
tags:
    - canvas-lms
    - api-endpoints
    - collaborations
    - course-management
    - group-collaboration
    - lti-integration
category: api
---

API for accessing course and group collaboration information.

**A Collaboration object looks like:**

```
{
  // The unique identifier for the collaboration
"id": 43,
  // A name for the type of collaboration
"collaboration_type": "Microsoft Office",
  // The collaboration document identifier for the collaboration provider
"document_id": "oinwoenfe8w8ef_onweufe89fef",
  // The canvas id of the user who created the collaboration
"user_id": 92,
  // The canvas id of the course or group to which the collaboration belongs
"context_id": 77,
  // The canvas type of the course or group to which the collaboration belongs
"context_type": "Course",
  // The LTI launch url to view collaboration.
"url": null,
  // The timestamp when the collaboration was created
"created_at": "2012-06-01T00:00:00-06:00",
  // The timestamp when the collaboration was last modified
"updated_at": "2012-06-01T00:00:00-06:00",
"description": null,
"title": null,
  // Another representation of the collaboration type
"type": "ExternalToolCollaboration",
  // The LTI launch url to edit the collaboration
"update_url": null,
  // The name of the user who owns the collaboration
"user_name": "John Danger"
}
```

**A Collaborator object looks like:**

```
{
  // The unique user or group identifier for the collaborator.
  "id": 12345,
  // The type of collaborator (e.g. 'user' or 'group').
  "type": "user",
  // The name of the collaborator.
  "name": "Don Draper"
}
```

[CollaborationsController#api\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/collaborations_controller.rb)

`GET /api/v1/courses/:course_id/collaborations`

**Scope:** `url:GET|/api/v1/courses/:course_id/collaborations`

`GET /api/v1/groups/:group_id/collaborations`

**Scope:** `url:GET|/api/v1/groups/:group_id/collaborations`

A paginated list of collaborations the current user has access to in the context of the course provided in the url. NOTE: this only returns ExternalToolCollaboration type collaborations.

```
curl https://<canvas>/api/v1/courses/1/collaborations/
```

Returns a list of [Collaboration](https://developerdocs.instructure.com/services/canvas/resources/collaborations#collaboration) objects.

[CollaborationsController#membersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/collaborations_controller.rb)

`GET /api/v1/collaborations/:id/members`

**Scope:** `url:GET|/api/v1/collaborations/:id/members`

A paginated list of the collaborators of a given collaboration

**Request Parameters:**

- “collaborator\_lti\_id”: Optional information to include with each member. Represents an identifier to be used for the member in an LTI context.
- “avatar\_image\_url”: Optional information to include with each member. The url for the avatar of a collaborator with type ‘user’.

Allowed values: `collaborator_lti_id`, `avatar_image_url`

**Example Request:**

```
curl https://<canvas>/api/v1/courses/1/collaborations/1/members
```

Returns a list of [Collaborator](https://developerdocs.instructure.com/services/canvas/resources/collaborations#collaborator) objects.

[CollaborationsController#potential\_collaboratorsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/collaborations_controller.rb)

`GET /api/v1/courses/:course_id/potential_collaborators`

**Scope:** `url:GET|/api/v1/courses/:course_id/potential_collaborators`

`GET /api/v1/groups/:group_id/potential_collaborators`

**Scope:** `url:GET|/api/v1/groups/:group_id/potential_collaborators`

A paginated list of the users who can potentially be added to a collaboration in the given context.

For courses, this consists of all enrolled users. For groups, it is comprised of the group members plus the admins of the course containing the group.

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).