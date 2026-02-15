---
title: Users | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/users
source: sitemap
fetched_at: 2026-02-15T09:14:56.212247-03:00
rendered_js: false
word_count: 710
summary: This document details API endpoints for managing user resources, including tracking imported resource updates, managing favorites, and searching for users within a learning object repository.
tags:
    - api-documentation
    - user-management
    - resource-tracking
    - instructure-canvas
    - rest-api
    - learning-management-system
category: api
---

### List User's Imported Resources (DEPRECATED)

**DEPRECATED** (use GET /resources?onlyImported=true instead) List all of the resources the current user has imported.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users/0123456789/imports?cursor=abcdefg"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The current session user id

cursorstringOptional

An identifier from a prior result to continue retrieving results

200

List of imported resources

### List Available Updates to Resources

/api/users/{userId}/updates

List all of the updates to resources the current user has imported.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users/0123456789/updates?cursor=abcdefg"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The current session user id

cursorstringOptional

An identifier from a prior result to continue retrieving results

200

List of updates to resources available

/api/users/{userId}/updates

/api/users/{userId}/updates/{resourceId}

Get the update information for a resource the current user has imported, if available.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users/0123456789/updates/c8d82b560d094c8e82ca0e4e59145e06"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The current session user id

200

Update information for the resource

/api/users/{userId}/updates/{resourceId}

/api/users/{userId}/updates/{resourceId}/ignore

Ignore this update for particular courses that previously had imported the resource.

**Example:** `curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type:application/json" -d '{"courseIds":["123","456"]}' "https://lor.instructure.com/api/users/0123456789/updates/9145e06/ignore"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The current session user id

courseIdsstring\[]Optional

A list of ids for courses to ignore for this update

/api/users/{userId}/updates/{resourceId}/ignore

### List User's Favorite Resources

/api/users/{userId}/favorites

List all of the resources the current user has marked as Favorite.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users/0123456789/favorites"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The current session user id

200

List of favorite resources

/api/users/{userId}/favorites

200

List of favorite resources

### Mark Resource as Favorite

/api/users/{userId}/favorites

Adds a resource to the current user's favorites list.

**Example:**

```
  curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/users/1234/favorites"
  data.json:
    {
      "resourceId": "ajk123"
    }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The current session user id

resourceIdstringRequired

The resourceId to mark as favorite

201

List of all favorite resources of the current user

/api/users/{userId}/favorites

### Returns Canvas profile URL

/api/users/{userId}/profile

Returns the Canvas profile URL for the specified user.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users/abcdef/profile"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The ID of the user you want to see in Canvas

/api/users/{userId}/profile

### Unmark Resource from Favorites

/api/users/{userId}/favorites/{resourceId}

Remove a resource from the current user's favorites list.

**Example:** `curl -X DELETE -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users/1234/favorites/56789"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringRequired

The current session user id

resourceIdstringRequired

The resourceId to unflag from user favorites

/api/users/{userId}/favorites/{resourceId}

Search through a list of all of the users in your account. Only admins and group managers may access this.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/users?q=aaron"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

qstring · min: 3Required

The text to search for in the name or e-mail of the users. The results will be empty until the minimum length of 3 characters is satisfied.

cursorstringOptional

An identifier from a prior query to continue retrieving results for.

200

An array of all of the users found matching the search

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).