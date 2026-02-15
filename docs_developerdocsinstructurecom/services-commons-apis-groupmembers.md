---
title: Groupmembers | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/groupmembers
source: sitemap
fetched_at: 2026-02-15T09:14:43.278274-03:00
rendered_js: false
word_count: 354
summary: This document details the API endpoints for managing group memberships, including adding, listing, updating, and removing users within the Canvas Learning Object Repository.
tags:
    - group-management
    - user-membership
    - api-endpoints
    - canvas-lms
    - session-authentication
    - instructure-lor
category: api
---

Add a user to the group members. Only administrators and managers of the group are allowed to perform this action. If attempted to add a user multiple times to a group, nothing will happen and their original membership record will be returned.

**Example:**

```
  curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/groups/1234/members"
  data.json:
  {
    "userId": "4LjxagScJoIlBACBRTI1XLXzCtTRn1CPDBLhWPEP:canvas-lmsf1ca849dd34eaef8040de8ffa7fe7fd5983e57e2",
    "isManager": true
  }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

userIdstringOptional

The identifier for the user to add to the group

isManagerbooleanOptional

Whether or not this user is a manager of the group

201

The newly created group membership

Gets a list of all the members in the group. Only Administrators and group managers are allowed to perform this action.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/groups/1234/members"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

An array of the group members

/api/groups/{id}/members/{memberId}

Update a member of the group by membership id. Can be used to change group managers. Only Administrators and group managers are allowed to perform this action. A manager cannot update their own management status.

**Example:**

````
  curl -X PUT -H "X-Session-ID: 01234567890" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/groups/1234/members/56789"```
  data.json:
  {
    "isManager": true
  }
````

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

isManagerbooleanOptional

Whether or not this user is a manager of the group

200

The updated group membership

/api/groups/{id}/members/{memberId}

/api/groups/{id}/members/{memberId}

Removes a member from the group by membership id. Only Administrators and group managers are allowed to perform this action. A manager cannot remove themself from the group.

**Example:** `curl -X DELETE -H "X-Session-ID: 01234567890" "https://lor.instructure.com/api/groups/1234/members/56789"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

/api/groups/{id}/members/{memberId}

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).