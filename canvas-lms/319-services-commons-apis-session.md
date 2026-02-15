---
title: Session | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/commons/apis/session
source: sitemap
fetched_at: 2026-02-15T09:15:03.108602-03:00
rendered_js: false
word_count: 327
summary: This document provides API specifications for managing user sessions in Instructure Commons, including endpoints for creating, retrieving, and destroying sessions.
tags:
    - instructure-commons
    - session-management
    - api-endpoints
    - authentication
    - canvas-lms
    - jwt
category: api
---

Destroy the current session, effectively logging out. `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/sessions/logout"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

### Get Contents of Your Session

Get the contents of the specified session. Session contents will only be returned for the current session. Sessions are always created for a specific user. Thus user specific information in the session will always belong to the user who created the session.

**Example:** `curl -H "X-Session-ID: 0123456789" "https://lor.instructure.com/api/sessions/0123456789"`

x-session-idstringRequired

Session authentication. The session ID can be provided in any of the following ways: \[Cookie: 'session'] \[Header: 'x-session-id'] \[Query parameter: 'session-id'] \[Query parameter: first value of 'state'] \[Body property: 'sessionId']

200

Session information returned successfully

Create a session in Commons. In order to generate a Commons session using this API, you must have already launched into Commons through Canvas at least once before. If not, you will get an error informing you that you have never launched into Commons before. Additionally, you will need to have accepted the terms of service. This endpoint also requires that you first acquire a JWT (JSON Web Token) that contains certain information needed by Commons to set up the session. You can acquire this JWT by sending a HTTP GET request to: `https://[your-canvas-domain]/api/lti/accounts/self/jwt_token?tool_launch_url=https://lor.instructure.com/api/lti`

This endpoint requires the typical Canvas Authorization header. This means you will need to generate an Access Token as described [here](http://guides.instructure.com/m/4214/l/40399-how-do-i-obtain-an-api-access-token-for-my-account).

**Example:** `curl -X POST -H "Content-Type: application/json" --data '{"jwt_token": "<contents of JWT token>"}' "https://lor.instructure.com/api/sessions"`

jwt\_tokenstringRequired

The JWT that is given to you by Canvas. It should be exactly as Canvas gives it to you. Do not decode it and give us the decoded version. We will handle that for you.

201

Session created successfully

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).