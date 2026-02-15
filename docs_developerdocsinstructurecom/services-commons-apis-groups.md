---
title: Groups | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/groups
source: sitemap
fetched_at: 2026-02-15T09:14:37.107219-03:00
rendered_js: false
word_count: 319
summary: This document defines the REST API endpoints for managing groups, providing instructions for creating, listing, updating, retrieving, and deleting group resources.
tags:
    - api-documentation
    - group-management
    - rest-api
    - instructure
    - authentication
    - user-administration
category: api
---

Create a group in the current user's account. Only administrators are allowed to perform this action.

**Example:**

```
  curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/groups"
  data.json:
  {
    "name": "The Group Name"
  }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

namestring · min: 1 · max: 50Optional

The desired name for the group

### List all groups for an account

Gets a list of all the groups the user has access to. If the user is an admin it will return all the groups in the account.

**Example:**

```
  curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/groups"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

An array of the groups for the account

Update a group in the current user's account. Only an admin or manager of the group can perform this request.

**Example:**

```
  curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/groups/:id"
  data.json:
  {
    "name": "The Group Name"
  }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

namestring · min: 1 · max: 50Optional

The desired name for the group

Get a group by its ID. Only an admin or manager of the group can use this endpoint.

**Example:**

```
  curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/groups/:id"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

Deletes a group. Only Administrators are allowed to perform this action.

**Example:**

```
  curl -X DELETE -H "X-Session-ID: 01234567890" "https://lor.instructure.com/api/groups/asdf"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).