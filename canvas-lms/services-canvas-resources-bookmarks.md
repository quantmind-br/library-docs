---
title: Bookmarks | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/bookmarks
source: sitemap
fetched_at: 2026-02-15T09:05:20.735823-03:00
rendered_js: false
word_count: 153
summary: This document provides technical documentation for the Canvas LMS Bookmarks API, detailing how to manage user bookmarks through various REST endpoints. It covers methods for listing, creating, retrieving, updating, and deleting bookmark resources.
tags:
    - canvas-lms
    - api-endpoints
    - bookmarks
    - rest-api
    - instructure
    - user-management
category: api
---

**A Bookmark object looks like:**

```
{
"id": 1,
"name": "Biology 101",
"url": "/courses/1",
"position": 1,
"data": {"active_tab":1}
}
```

[Bookmarks::BookmarksController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

`GET /api/v1/users/self/bookmarks`

**Scope:** `url:GET|/api/v1/users/self/bookmarks`

Returns the paginated list of bookmarks.

**Example Request:**

```
curl'https://<canvas>/api/v1/users/self/bookmarks'\
-H'Authorization: Bearer <token>'
```

Returns a list of [Bookmark](https://developerdocs.instructure.com/services/canvas/resources/bookmarks#bookmark) objects.

[Bookmarks::BookmarksController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

`POST /api/v1/users/self/bookmarks`

**Scope:** `url:POST|/api/v1/users/self/bookmarks`

Creates a bookmark.

**Request Parameters:**

The position of the bookmark. Defaults to the bottom.

The data associated with the bookmark

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/bookmarks' \
     -F 'name=Biology 101' \
     -F 'url=/courses/1' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Bookmark](https://developerdocs.instructure.com/services/canvas/resources/bookmarks#bookmark) object.

[Bookmarks::BookmarksController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

`GET /api/v1/users/self/bookmarks/:id`

**Scope:** `url:GET|/api/v1/users/self/bookmarks/:id`

Returns the details for a bookmark.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/bookmarks/1' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Bookmark](https://developerdocs.instructure.com/services/canvas/resources/bookmarks#bookmark) object.

[Bookmarks::BookmarksController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

`PUT /api/v1/users/self/bookmarks/:id`

**Scope:** `url:PUT|/api/v1/users/self/bookmarks/:id`

Updates a bookmark

**Request Parameters:**

The position of the bookmark. Defaults to the bottom.

The data associated with the bookmark

**Example Request:**

```
curl -X PUT 'https://<canvas>/api/v1/users/self/bookmarks/1' \
     -F 'name=Biology 101' \
     -F 'url=/courses/1' \
     -H 'Authorization: Bearer <token>'
```

Returns a [Folder](https://developerdocs.instructure.com/services/canvas/resources/files#folder) object.

[Bookmarks::BookmarksController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/bookmarks/bookmarks_controller.rb)

`DELETE /api/v1/users/self/bookmarks/:id`

**Scope:** `url:DELETE|/api/v1/users/self/bookmarks/:id`

Deletes a bookmark

**Example Request:**

```
curl -X DELETE 'https://<canvas>/api/v1/users/self/bookmarks/1' \
     -H 'Authorization: Bearer <token>'
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).