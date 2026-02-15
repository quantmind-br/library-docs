---
title: Consortiums | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/consortiums
source: sitemap
fetched_at: 2026-02-15T09:15:10.070788-03:00
rendered_js: false
word_count: 738
summary: Technical documentation for the consortiums API, detailing endpoints for creating, managing, and deleting consortiums and their member accounts.
tags:
    - consortium-management
    - api-endpoints
    - membership-administration
    - instructure-lor
    - rest-api
category: api
---

### Invite account to consortium

/api/consortiums/{id}/members

Invites an account to become a member of a consortium. This can only be performed by admins of the account that created the consortium. If the account is already a pending or joined member of the consortium, their existing membership record will be returned.

**Example:**

```
curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/consortiums/0123456789/members"
data.json:
{
  "accountId": "0123456789"
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The id of the consortium, provided in the url

accountIdstringRequired

The id of the account to invite to the consortium

200

Membership record created or returned

/api/consortiums/{id}/members

### Remove a member account from a consortium

/api/consortiums/{id}/members/{memberId}

Delete a membership record for a consortium. This request can only be performed by an admin of the institution that created the consortium for which the membership record belongs. The creator of the consortium cannot remove themselves as a member of the consortium. The memberId must be for a membership record that is part of the consortium (consortiumId).

**Example:**

```
curl -X DELETE -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/consortiums/123/members/456"
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

idstringRequired

The id of the consortium that the membership belongs to

memberIdstringRequired

The id of the membership to be deleted

/api/consortiums/{id}/members/{memberId}

### Update consortium membership

/api/consortiums/{id}/members/{memberId}

Update an account member's contributor setting. Only an admin of the account that created the consortium can perform this action.

**Example:**

```
curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/consortiums/0123456789/members/9876543210"
data.json:
{
  "isContributor": true
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

memberIdstringRequired

The id of the membership record to update

isContributorbooleanRequired

Whether the consortium member has the privilege to share resources to the consortium

200

Membership record updated

/api/consortiums/{id}/members/{memberId}

### Update consortium membership status

/api/consortiums/{id}/members/{memberId}/status

Update the membership status of your own institution in a consortium. This action can only be performed by an admin of the institution that is a member of the consortium.

**Example:**

```
curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/consortiums/0123456789/members/9876543210/status"
data.json:
{
  "status": "member"
}
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

memberIdstringRequired

The id of the membership record to update

statusstring · enumRequired

The new membership status for the institution in the consortium. The existing membership in the consortium must be pending.

Possible values:

200

Membership record updated

/api/consortiums/{id}/members/{memberId}/status

Gets a list of all consortiums that the current user's account is a part of.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/consortiums"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

### Create account consortiums

Creates a new consortium with the provided name. Only account admins may perform this action.

**Example:**

```
  curl -X POST -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json  "https://lor.instructure.com/api/consortiums"
  data.json:
  {
    "name": "The consortium name"
  }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

namestring · min: 1 · max: 50Optional

The desired name for the consortium

201

The newly created consortium

### Get consortium and details

/api/consortiums/{consortiumId}

Gets a consortium as well as all membership information for the consortium. Must be an admin of the account that created the consortium to use this request.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/consortiums/0123456789"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

consortiumIdstringRequired

/api/consortiums/{consortiumId}

### Update consortium settings

/api/consortiums/{consortiumId}

Update a consortium's settings.

**Example:**

```
  curl -X PUT -H "X-Session-ID: 0123456789" -H "Content-Type: application/json" --data @data.json "https://lor.instructure.com/api/consortiums/0123456789"
  data.json:
  {
    "name": "New name"
  }
```

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

consortiumIdstringRequired

namestringOptional

The new name to use for the consortium

/api/consortiums/{consortiumId}

/api/consortiums/{consortiumId}

Deletes a consortium. Only Administrators are allowed to perform this action.

**Example:** `curl -X DELETE -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/consortiums/123"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

consortiumIdstringRequired

/api/consortiums/{consortiumId}

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).