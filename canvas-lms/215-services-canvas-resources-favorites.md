---
title: Favorites | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/favorites
source: sitemap
fetched_at: 2026-02-15T09:07:34.75125-03:00
rendered_js: false
word_count: 389
summary: This document outlines the REST API endpoints for managing user favorites in Canvas LMS, specifically for courses and groups. It provides details on listing favorites, adding new ones, and removing or resetting them to defaults.
tags:
    - canvas-lms
    - rest-api
    - favorites-management
    - course-api
    - group-api
    - user-endpoints
category: api
---

**A Favorite object looks like:**

```
{
  // The ID of the object the Favorite refers to
"context_id": 1170,
  // The type of the object the Favorite refers to (currently, only 'Course' is
  // supported)
"context_type": "Course"
}
```

[FavoritesController#list\_favorite\_coursesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`GET /api/v1/users/self/favorites/courses`

**Scope:** `url:GET|/api/v1/users/self/favorites/courses`

Retrieve the paginated list of favorite courses for the current user. If the user has not chosen any favorites, then a selection of currently enrolled courses will be returned.

See the [List courses API](https://developerdocs.instructure.com/services/canvas/resources/courses#method.courses.index) for details on accepted include\[] parameters.

**Request Parameters:**

`exclude_blueprint_courses`

When set, only return courses that are not configured as blueprint courses.

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/favorites/courses \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a list of [Course](https://developerdocs.instructure.com/services/canvas/resources/courses#course) objects.

[FavoritesController#list\_favorite\_groupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`GET /api/v1/users/self/favorites/groups`

**Scope:** `url:GET|/api/v1/users/self/favorites/groups`

Retrieve the paginated list of favorite groups for the current user. If the user has not chosen any favorites, then a selection of groups that the user is a member of will be returned.

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/favorites/groups \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a list of [Group](https://developerdocs.instructure.com/services/canvas/resources/groups#group) objects.

[FavoritesController#add\_favorite\_coursearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`POST /api/v1/users/self/favorites/courses/:id`

**Scope:** `url:POST|/api/v1/users/self/favorites/courses/:id`

Add a course to the current user’s favorites. If the course is already in the user’s favorites, nothing happens. Canvas for Elementary subject and homeroom courses can be added to favorites, but this has no effect in the UI.

**Request Parameters:**

The ID or SIS ID of the course to add. The current user must be registered in the course.

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/favorites/courses/1170 \
  -X POST \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Length: 0'
```

Returns a [Favorite](https://developerdocs.instructure.com/services/canvas/resources/favorites#favorite) object.

[FavoritesController#add\_favorite\_groupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`POST /api/v1/users/self/favorites/groups/:id`

**Scope:** `url:POST|/api/v1/users/self/favorites/groups/:id`

Add a group to the current user’s favorites. If the group is already in the user’s favorites, nothing happens.

**Request Parameters:**

The ID or SIS ID of the group to add. The current user must be a member of the group.

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/favorites/group/1170 \
  -X POST \
  -H 'Authorization: Bearer <ACCESS_TOKEN>' \
  -H 'Content-Length: 0'
```

Returns a [Favorite](https://developerdocs.instructure.com/services/canvas/resources/favorites#favorite) object.

[FavoritesController#remove\_favorite\_coursearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`DELETE /api/v1/users/self/favorites/courses/:id`

**Scope:** `url:DELETE|/api/v1/users/self/favorites/courses/:id`

Remove a course from the current user’s favorites.

**Request Parameters:**

the ID or SIS ID of the course to remove

**Example Request:**

```
curl https://<canvas>/api/v1/users/self/favorites/courses/1170 \
  -X DELETE \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a [Favorite](https://developerdocs.instructure.com/services/canvas/resources/favorites#favorite) object.

[FavoritesController#remove\_favorite\_groupsarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`DELETE /api/v1/users/self/favorites/groups/:id`

**Scope:** `url:DELETE|/api/v1/users/self/favorites/groups/:id`

Remove a group from the current user’s favorites.

**Request Parameters:**

the ID or SIS ID of the group to remove

**Example Request:**

```
curlhttps://<canvas>/api/v1/users/self/favorites/groups/1170\
-XDELETE\
-H'Authorization: Bearer <ACCESS_TOKEN>'
```

Returns a [Favorite](https://developerdocs.instructure.com/services/canvas/resources/favorites#favorite) object.

[FavoritesController#reset\_course\_favoritesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`DELETE /api/v1/users/self/favorites/courses`

**Scope:** `url:DELETE|/api/v1/users/self/favorites/courses`

Reset the current user’s course favorites to the default automatically generated list of enrolled courses

**Example Request:**

```
curlhttps://<canvas>/api/v1/users/self/favorites/courses\
-XDELETE\
-H'Authorization: Bearer <ACCESS_TOKEN>'
```

[FavoritesController#reset\_groups\_favoritesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/favorites_controller.rb)

`DELETE /api/v1/users/self/favorites/groups`

**Scope:** `url:DELETE|/api/v1/users/self/favorites/groups`

Reset the current user’s group favorites to the default automatically generated list of enrolled group

**Example Request:**

```
curlhttps://<canvas>/api/v1/users/self/favorites/group\
-XDELETE\
-H'Authorization: Bearer <ACCESS_TOKEN>'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).