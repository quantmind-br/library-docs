---
title: Content Shares | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/content_shares
source: sitemap
fetched_at: 2026-02-15T09:06:58.475393-03:00
rendered_js: false
word_count: 336
summary: This document outlines the API endpoints and data structures for managing content sharing between users, allowing for the creation, retrieval, and updating of shared resources. It provides detailed specifications for tracking read status and managing lists of sent and received shared content.
tags:
    - content-sharing
    - canvas-lms
    - api-endpoints
    - rest-api
    - resource-sharing
    - user-communication
category: api
---

API for creating, accessing and updating Content Sharing. Content shares are used to share content directly between users.

**A ContentShare object looks like:**

```
// Content shared between users
{
  // The id of the content share for the current user
"id": 1,
  // The name of the shared content
"name": "War of 1812 homework",
  // The type of content that was shared. Can be assignment, discussion_topic,
  // page, quiz, module, or module_item.
"content_type": "assignment",
  // The datetime the content was shared with this user.
"created_at": "2017-05-09T10:12:00Z",
  // The datetime the content was updated.
"updated_at": "2017-05-09T10:12:00Z",
  // The id of the user who sent or received the content share.
"user_id": 1578941,
  // The user who shared the content. This field is provided only to receivers; it
  // is not populated in the sender's list of sent content shares.
"sender": {"id":1,"display_name":"Matilda Vargas","avatar_image_url":"http:\/\/localhost:3000\/image_url","html_url":"http:\/\/localhost:3000\/users\/1"},
  // An Array of users the content is shared with.  This field is provided only to
  // senders; an empty array will be returned for the receiving users.
"receivers": [{"id":1,"display_name":"Jon Snow","avatar_image_url":"http:\/\/localhost:3000\/image_url2","html_url":"http:\/\/localhost:3000\/users\/2"}],
  // The course the content was originally shared from.
"source_course": {"id":787,"name":"History 105"},
  // Whether the recipient has viewed the content share.
"read_state": "read",
  // The content export record associated with this content share
"content_export": {"id":42}
}
```

[ContentSharesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`POST /api/v1/users/:user_id/content_shares`

**Scope:** `url:POST|/api/v1/users/:user_id/content_shares`

Share content directly between two or more users

**Request Parameters:**

IDs of users to share the content with.

Type of content you are sharing.

Allowed values: `assignment`, `discussion_topic`, `page`, `quiz`, `module`, `module_item`

The id of the content that you are sharing

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/content_shares \
      -d 'content_type=assignment' \
      -d 'content_id=1' \
      -H 'Authorization: Bearer <token>' \
      -X POST
```

Returns a [ContentShare](https://developerdocs.instructure.com/services/canvas/resources/content_shares#contentshare) object.

[ContentSharesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`GET /api/v1/users/:user_id/content_shares/sent`

**Scope:** `url:GET|/api/v1/users/:user_id/content_shares/sent`

`GET /api/v1/users/:user_id/content_shares/received`

**Scope:** `url:GET|/api/v1/users/:user_id/content_shares/received`

Return a paginated list of content shares a user has sent or received. Use `self` as the user\_id to retrieve your own content shares. Only linked observers and administrators may view other users’ content shares.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/content_shares/received'
```

Returns a list of [ContentShare](https://developerdocs.instructure.com/services/canvas/resources/content_shares#contentshare) objects.

[ContentSharesController#unread\_countarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`GET /api/v1/users/:user_id/content_shares/unread_count`

**Scope:** `url:GET|/api/v1/users/:user_id/content_shares/unread_count`

Return the number of content shares a user has received that have not yet been read. Use `self` as the user\_id to retrieve your own content shares. Only linked observers and administrators may view other users’ content shares.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/content_shares/unread_count'
```

[ContentSharesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`GET /api/v1/users/:user_id/content_shares/:id`

**Scope:** `url:GET|/api/v1/users/:user_id/content_shares/:id`

Return information about a single content share. You may use `self` as the user\_id to retrieve your own content share.

**Example Request:**

```
curl 'https://<canvas>/api/v1/users/self/content_shares/123'
```

Returns a [ContentShare](https://developerdocs.instructure.com/services/canvas/resources/content_shares#contentshare) object.

[ContentSharesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`DELETE /api/v1/users/:user_id/content_shares/:id`

**Scope:** `url:DELETE|/api/v1/users/:user_id/content_shares/:id`

Remove a content share from your list. Use `self` as the user\_id. Note that this endpoint does not delete other users’ copies of the content share.

**Example Request:**

```
curl -X DELETE 'https://<canvas>/api/v1/users/self/content_shares/123'
```

[ContentSharesController#add\_usersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`POST /api/v1/users/:user_id/content_shares/:id/add_users`

**Scope:** `url:POST|/api/v1/users/:user_id/content_shares/:id/add_users`

Send a previously created content share to additional users

**Request Parameters:**

IDs of users to share the content with.

**Example Request:**

```
curl -X POST 'https://<canvas>/api/v1/users/self/content_shares/123/add_users?receiver_ids[]=789'
```

Returns a [ContentShare](https://developerdocs.instructure.com/services/canvas/resources/content_shares#contentshare) object.

[ContentSharesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/content_shares_controller.rb)

`PUT /api/v1/users/:user_id/content_shares/:id`

**Scope:** `url:PUT|/api/v1/users/:user_id/content_shares/:id`

Mark a content share read or unread

**Request Parameters:**

Read state for the content share

Allowed values: `read`, `unread`

**Example Request:**

```
curl -X PUT 'https://<canvas>/api/v1/users/self/content_shares/123?read_state=read'
```

Returns a [ContentShare](https://developerdocs.instructure.com/services/canvas/resources/content_shares#contentshare) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).