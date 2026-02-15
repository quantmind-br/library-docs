---
title: Search | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/search
source: sitemap
fetched_at: 2026-02-15T09:08:34.470497-03:00
rendered_js: false
word_count: 478
summary: This document defines the API endpoints for searching valid message recipients, including users, courses, and groups, as well as listing public courses within the Canvas LMS.
tags:
    - canvas-lms
    - search-api
    - messaging
    - user-search
    - course-search
    - pagination
category: api
---

[SearchController#recipientsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/search_controller.rb)

`GET /api/v1/conversations/find_recipients`

**Scope:** `url:GET|/api/v1/conversations/find_recipients`

`GET /api/v1/search/recipients`

**Scope:** `url:GET|/api/v1/search/recipients`

Find valid recipients (users, courses and groups) that the current user can send messages to. The /api/v1/search/recipients path is the preferred endpoint, /api/v1/conversations/find\_recipients is deprecated.

Pagination is supported.

**Request Parameters:**

Search terms used for matching users/courses/groups (e.g. “bob smith”). If multiple terms are given (separated via whitespace), only results matching all terms will be returned.

Limit the search to a particular course/group (e.g. “course\_3” or “group\_4”).

Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with “course\_” or “group\_” respectively, e.g. [exclude\[\]=1&exclude](https://developerdocs.instructure.com/services/canvas/resources/search)=2&exclude\[]=course\_3

Limit the search just to users or contexts (groups/courses).

Allowed values: `user`, `context`

Search for a specific user id. This ignores the other above parameters, and will never return more than one result.

When searching by user\_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context – if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations.

Array of permission strings to be checked for each matched context (e.g. “send\_messages”). This argument determines which permissions may be returned in the response; it won’t prevent contexts from being returned if they don’t grant the permission(s).

**API response field:**

The unique identifier for the user/context. For groups/courses, the id is prefixed by “group\_”/“course\_” respectively.

The name of the context or short name of the user

Only set for users. The full name of the user

Avatar image url for the user/context

- “context”|“course”|“section”|“group”|“user”|null
  
  Type of recipients to return, defaults to null (all). “context” encompasses “course”, “section” and “group”

Array of recipient types to return (see type above), e.g. [types\[\]=user&types](https://developerdocs.instructure.com/services/canvas/resources/search)=course

Only set for contexts, indicates number of messageable users

Only set for users. Hash of course ids and enrollment types for each course to show what they share with this user

Only set for users. Hash of group ids and enrollment types for each group to show what they share with this user

Only set for contexts. Mapping of requested permissions that the context grants the current user, e.g. { send\_messages: true }

**Example Response:**

```
[
  {"id": "group_1", "name": "the group", "type": "context", "user_count": 3},
  {"id": 2, "name": "greg", "full_name": "greg jones", "common_courses": {}, "common_groups": {"1": ["Member"]}}
]
```

[SearchController#all\_coursesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/search_controller.rb)

`GET /api/v1/search/all_courses`

**Scope:** `url:GET|/api/v1/search/all_courses`

A paginated list of all courses visible in the public index

**Request Parameters:**

Search terms used for matching users/courses/groups (e.g. “bob smith”). If multiple terms are given (separated via whitespace), only results matching all terms will be returned.

Only return courses with public content. Defaults to false.

Only return courses that allow self enrollment. Defaults to false.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).