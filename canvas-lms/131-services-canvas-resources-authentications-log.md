---
title: Authentications Log | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/authentications_log
source: sitemap
fetched_at: 2026-02-15T09:08:04.52723-03:00
rendered_js: false
word_count: 242
summary: This document describes API endpoints for querying authentication audit logs, allowing users to track login and logout events for specific accounts, users, or logins.
tags:
    - authentication-api
    - audit-logs
    - user-events
    - canvas-lms
    - login-tracking
    - security-auditing
category: api
---

Query audit log of authentication events (logins and logouts).

For each endpoint, a compound document is returned. The primary collection of event objects is paginated, ordered by date descending. Secondary collections of logins, accounts, page views, and users related to the returned events are also included. Refer to the Logins, Accounts, Page Views, and Users APIs for descriptions of the objects in those collections.

Authentication logs are stored for one year.

**An AuthenticationEvent object looks like:**

```
{
  // timestamp of the event
"created_at": "2012-07-19T15:00:00-06:00",
  // authentication event type ('login' or 'logout')
"event_type": "login",
  // ID of the pseudonym (login) associated with the event
"pseudonym_id": 9478,
  // ID of the account associated with the event. will match the account_id in the
  // associated pseudonym.
"account_id": 2319,
  // ID of the user associated with the event will match the user_id in the
  // associated pseudonym.
"user_id": 362
}
```

[AuthenticationAuditApiController#for\_loginarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_audit_api_controller.rb)

`GET /api/v1/audit/authentication/logins/:login_id`

**Scope:** `url:GET|/api/v1/audit/authentication/logins/:login_id`

List authentication events for a given login.

**Request Parameters:**

The beginning of the time range from which you want events. Events are stored for one year.

The end of the time range from which you want events.

[AuthenticationAuditApiController#for\_accountarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_audit_api_controller.rb)

`GET /api/v1/audit/authentication/accounts/:account_id`

**Scope:** `url:GET|/api/v1/audit/authentication/accounts/:account_id`

List authentication events for a given account.

**Request Parameters:**

The beginning of the time range from which you want events. Events are stored for one year.

The end of the time range from which you want events.

[AuthenticationAuditApiController#for\_userarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/authentication_audit_api_controller.rb)

`GET /api/v1/audit/authentication/users/:user_id`

**Scope:** `url:GET|/api/v1/audit/authentication/users/:user_id`

List authentication events for a given user.

**Request Parameters:**

The beginning of the time range from which you want events. Events are stored for one year.

The end of the time range from which you want events.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).