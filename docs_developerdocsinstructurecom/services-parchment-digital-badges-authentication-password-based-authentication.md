---
title: Password-Based Authentication | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/authentication/password-based-authentication
source: sitemap
fetched_at: 2026-02-15T08:59:11.147264-03:00
rendered_js: false
word_count: 149
summary: This document explains how to perform password-based authentication with the Badges API to obtain an access token. It details the required POST request, the structure of the token response, and account prerequisites such as email verification.
tags:
    - authentication
    - api-token
    - password-grant
    - access-token
    - badges-api
    - oauth2
category: api
---

You can authenticate with the API using your username and password to access your own resources.

To obtain a token with your password, execute the following request:

```
curl-XPOST'https://{BADGES_DOMAIN}/o/token'-d"username=YOUREMAIL&password=YOURPASSWORD"
```

You’ll receive a document in response like the following:

```
{
"access_token":"YOURACCESSTOKEN",
"token_type":"Bearer",
"expires_in":86400,
"refresh_token":"YOURREFRESHTOKEN"
}
```

**Don’t have a password on your account?** In order to use the password-based grant, you need to set a password on your account. You might not have one already if you created your account via sign-in from an external identity provider, such as Facebook or Google. You can add a password once signed in from your Profile page. If you don’t yet have an account, sign up [herearrow-up-right](https://badges.parchment.com/signup). You will need a verified email address to access the following APIs, so make sure to complete that step.

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).