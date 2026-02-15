---
title: Plagiarism Detection Platform Users | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/plagiarism_detection_platform_users
source: sitemap
fetched_at: 2026-02-15T09:05:19.019664-03:00
rendered_js: false
word_count: 106
summary: This document outlines the Plagiarism Detection Platform Users API for Canvas LMS, detailing endpoints for retrieving individual user information and lists of users within specific groups.
tags:
    - canvas-lms
    - plagiarism-detection
    - users-api
    - lti-integration
    - rest-api
    - jwt-authentication
category: api
---

## [hashtag](#plagiarism-detection-platform-users-api) Plagiarism Detection Platform Users API

**Plagiarism Detection Platform API for Users (Must use** [**JWT access tokens**](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

### [hashtag](#method.lti-users_api.show)

[Lti::UsersApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/users_api_controller.rb)

`GET /api/lti/users/:id`

**Scope:** `url:GET|/api/lti/users/:id`

Get a single Canvas user by Canvas id or LTI id. Tool providers may only access users that have been assigned an assignment associated with their tool.

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

### [hashtag](#method.lti-users_api.group_index)

[Lti::UsersApiController#group\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/users_api_controller.rb)

`GET /api/lti/groups/:group_id/users`

**Scope:** `url:GET|/api/lti/groups/:group_id/users`

Get all Canvas users in a group. Tool providers may only access groups that belong to the context the tool is installed in.

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).