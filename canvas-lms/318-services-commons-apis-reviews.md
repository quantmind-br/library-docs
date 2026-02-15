---
title: Reviews | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/reviews
source: sitemap
fetched_at: 2026-02-15T09:14:57.916451-03:00
rendered_js: false
word_count: 347
summary: This document outlines the API endpoints for managing resource reviews, including instructions for creating, updating, retrieving, deleting, and listing reviews for specific resources.
tags:
    - api-endpoints
    - resource-reviews
    - instructure-lor
    - authentication
    - crud-operations
category: api
---

### Update or Create a Review

/api/resources/{resourceId}/reviews/self

Create or update a user's review for a resource. You cannot create multiple reviews for a single user on a resource. If a user tries to create a second review on a resource it will just update their first review. You must provide a textual review, rating, or both. A 200 status code is returned upon a successful update and a 201 status code is returned on successful creation.

**Example:**

```
  curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type:application/json" --data @data.json "https://lor.instructure.com/api/resources/9cd972bef89b9fc7de6357a473f845db/reviews/self"
  data.json:
  {
    "body": "I find your lack of faith disturbing",
    "rating": 1
  }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The id of the resource to review

200

Review updated successfully

201

Review created successfully

/api/resources/{resourceId}/reviews/self

/api/resources/{resourceId}/reviews/self

Get a review for the resource that was authored by the current user.

**Example:**

```
  curl -X GET -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/9cd972bef89b9fc7de6357a473f845db/reviews/self"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The id of the resource to get the review for

/api/resources/{resourceId}/reviews/self

### Destroy Review by This User

/api/resources/{resourceId}/reviews/self

Destroy a user's review for this resource.

**Example:**

```
  curl -X DELETE -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/9cd972bef89b9fc7de6357a473f845db/reviews/self"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The id of the resource to delete the review for

204

Review deleted successfully

/api/resources/{resourceId}/reviews/self

### List Reviews for a Resource

/api/resources/{resourceId}/reviews

List reviews for the specified resource.

`curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/resources/0123456789/reviews?cursor=abcdefg"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

resourceIdstringRequired

The id of the resource to list reviews for

cursorstringOptional

An identifier from a prior query to continue retrieving results for

200

List of reviews for a resource

/api/resources/{resourceId}/reviews

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).