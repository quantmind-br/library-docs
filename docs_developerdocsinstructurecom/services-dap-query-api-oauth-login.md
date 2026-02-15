---
title: Authentication | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/query-api/oauth_login
source: sitemap
fetched_at: 2026-02-15T08:57:20.478469-03:00
rendered_js: false
word_count: 299
summary: This document provides step-by-step instructions for obtaining a ClientID and Secret, requesting a short-lived access token (JWT), and using it to authenticate API calls to Instructure services.
tags:
    - authentication
    - access-token
    - jwt
    - instructure-api
    - canvas-lms
    - api-gateway
category: tutorial
---

## 1. Get your ClientID and Secret

**If you are an Institution**: make sure that you have generated your ClientID and Secret for institutional use on the [Identity Servicearrow-up-right](https://identity.instructure.com/login/) page.

**If you are a Partner of Instructure**: make sure that you have received your ClientID and Secret from your Institution.

Keep your ClientID and Secret in a safe place! Do not share with anyone else!

## 2. Requesting the Access Token

Using the ClientID and Secret you are ready to request for an `access token`. The `access token` is a JSON Web Token, that grants access to the targeted Instructure service. This is a short lived token, it needs to be renewed periodically. Typically expires in one hour.

Issues a JSON Web Token (JWT) to be used in subsequent to API calls.

The received JWT (see `access_token` property in the Responses section) needs to be passed in the header of every upcoming service call as a Bearer token.

Note that this is a short lived token, it needs to be renewed periodically. Typically expires in one hour.

AuthorizationstringRequired

400

The request could not be understood due to malformed syntax

403

Request forbidden due to missing/invalid authentication information

The following code snippet uses `curl` to send the request and `jq` to extract the `access token` from the answer:

```
ACCESS_TOKEN=$(curl --request POST https://api-gateway.instructure.com/ids/auth/login \
--user "${CLIENT_ID}:${SECRET}"  \
--data-urlencode 'grant_type=client_credentials' | jq -r '.access_token')
echo $ACCESS_TOKEN
```

## 3. Using the Access Token

Once you received the `access token` you can call the desired service. The example below will demonstrate this by querying the list of table names that exist in Canvas using the [DAP Query API](https://developerdocs.instructure.com/services/dap/query-api/query-api-reference). The `access token` shall be passed as a bearer token in the Authorization header:

```
curl --request GET 'https://api-gateway.instructure.com/dap/query/canvas/table' \
--header "Authorization: Bearer ${ACCESS_TOKEN}" 
```

Upon success the call returns with a list of table names available Canvas.

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).