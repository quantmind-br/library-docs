---
title: Authorization Code-Based Authentication | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/authentication/authorization-code-based-authentication
source: sitemap
fetched_at: 2026-02-15T08:59:15.424977-03:00
rendered_js: false
word_count: 1043
summary: This document explains how to implement OAuth2 authentication and authorization to securely connect applications with the Parchment Digital Badges API.
tags:
    - oauth2
    - authentication
    - api-integration
    - authorization-flow
    - access-tokens
    - permission-scopes
category: guide
---

Parchment Digital Badges offers OAuth2 Identity Provider/Authorization Server/Resource Server functionality to help your Connected App securely obtain a user-specific API token to use to access that user’s credentialing resources. You can add a **Connect to Parchment Digital Badges** or **Login with Parchment Digital Badges** button to your service. There are several Parchment Digital Badges servers deployed in different regions around the world, and your app can connect with each desired Parchment Digital Badges region separately. In order to sign OAuth requests to a particular Parchment Digital Badges server, your service needs to establish a shared secret with the administrator of that Parchment Digital Badges server.

You can build apps that connect with Parchment Digital Badges. Contact Parchment Digital Badges to request an application key and secret for signing your OAuth requests. Describe what you’re planning on building and what type of information you need from Parchment Digital Badges users.

## Requesting access to the Parchment Digital Badges API

For each availability region of the Parchment Digital Badges service, when you request a developer key, an application record will be created with a key and secret. When you request a key, make sure to describe which region you would like to use (Test sandbox, Australia, Canada, EU/Ireland, Singapore or US). These regional servers also have their own UI and API domain, so be sure to use the correct domain based on which server you are using. We use the US production server as a default in our documentation. The ability to automatically obtain a key and secret for certain types of applications is also available via the [Badge Connect (Open Badges 2.1)arrow-up-right](https://www.imsglobal.org/spec/ob/v2p1/) protocol. These scopes allow your app to access a user's backpack to read their badges or send them new badges.

Issuer and displayer apps need some combination of permissions to issuer and backpack (recipient) API endpoints. These are accomplished by requesting a set of permission scopes when you register your application with the Parchment Digital Badges server administrator. These scopes or a subset of them will be available to you when you request authorization on behalf of a user of your app.

### Profile Scope (Automatic)

- **r:profile** This allows you to get information about the user that they have defined in Parchment Digital Badges, including their firstname, lastname, and registered email addresses. This scope is automatically available. It gives you the ability to access the GET ***/v2/user/profile*** endpoint.

<!--THE END-->

- **r:issuer** This allows you to get information about the issuer profiles where the authenticated user acts as a staff member, editor, or owner. You may view issuer metadata, badges defined by these issuers, and badge awards granted by these issuers.
- **rw:issuer** This allows read/write access to the resources above, to the extent that the authenticated user may perform these actions. "Staff" level users may read all data and award new instances of defined badges; "Editor" level users may also define new BadgeClasses and edit existing ones. "Owner" members may modify the staff list.

<!--THE END-->

- **r:backpack** Allows you to read assertions that the user has received from issuers on this Parchment Digital Badges server or imported into their backpack from external Open Badges issuers.
- **rw:backpack** Allows you to read, create, and update assertions and collections of assertions. For assertions, this means you can trigger import of an Open Badges assertion defined elsewhere, pushing it to the recipient’s backpack.

<!--THE END-->

- **r:org** Allows you to get information about the organizations where the authenticated user is staff. This includes the organization’s name, description, and other metadata.
- **rw:org** Allows you to read and update information about the organizations where the authenticated user is staff.

## The OAuth2 Dance (Authorization Code grant workflow)

Once you have emailed us your Scope and Redirect URIs and we have replied with a ***client\_id*** and ***client\_secret***—we can dance. Suppose a Parchment Digital Badges user would like to grant you access to her badges, issuers and profile information. First, create a “Login with Parchment Digital Badges” button on your website that links to the following URI (line breaks added for readability):

`https://{BADGES_DOMAIN}/auth/oauth2/authorize?`

`client_id=123&redirect_uri=https%3A%2F%2Fexample.com%2Fauth&scope=r%3Aprofile%20rw%3Aissuer%20r%3Abackpack`

Set ***client\_id*** to the Client ID you received from the Parchment Digital Badges team. Set ***redirect\_uri*** to the Redirect URI for your application (url encode this and all parameters). We use this to redirect the user back to your website with an Authorization Code after they have logged in and granted you access. Set ***scope*** to the level of access you are requesting.

After Parchment Digital Badges redirects the user back to your application with the Authorization Code in the query parameter ***code*** your application will need to exchange that temporary code for a long-lived Access Token via a POST request. Here’s an example using ***curl***:

```
curl https://{BADGES_DOMAIN}/o/token \
-d "grant_type=authorization_code&code=XYZ&client_id=123&client_secret=ABC&redirect_uri=https://example.com/auth"
```

**Note**: You may pass a state parameter, which should be a URL-safe URL-encoded string. For example, you may encode a small snippet of JSON. This parameter will be passed back to you at your Redirect URL

Exchange this ***authorization\_code*** for an access token.

```
curl https://{BADGES_DOMAIN}/o/token \
-d "grant_type=authorization_code&code=authorization_code"
```

And that’s it! You’re done. You’ll receive a response like this:

```
{
  "token_type": "Bearer",
  "access_token": "C1HePsbwS3tUmwC6OCKsC41w96xckc",
  "expires_in": 86400,
  "refresh_token": "xwHPFwH55tQpCy3qCgsIW59k3g3aPh",
  "scope": "rw:issuer rw:profile rw:backpack"
}
```

And that’s it! You can securely store the access token in your application. You may now use the ***access\_token*** obtained from this request to authenticate API requests. See Using the Parchment Digital Badges API below.

Your access token will expire (by default, 24 hours after issue). At that point, you may refresh it using the refresh\_token included with the token. Refresh tokens are long-lived and must be stored securely. Access tokens also must be stored securely, but are lower risk due to their shorter duration. You may obtain a new access token using your refresh token by making a new POST to the authorization endpoint.

```
curl https://{BADGES_DOMAIN}/o/token -X POST \
-d "grant_type=refresh_token&refresh_token=YOURREFRESHTOKEN&client_id=YOURCLIENTID&client_secret=YOURCLIENTSECRET"
```

You will get back a new token document, including a new ***access\_token*** and ***refresh\_token***. The new access token will be valid for the identified number of seconds.

**Note:** If you have given us a ***localhost*** Redirection URI remember to use our test sandbox environment's endpoints for testing. Use [***https://test.badges.parchment.com/auth/oauth2/authorize***arrow-up-right](https://test.badges.parchment.com/auth/oauth2/authorize) and [***https://api.test.badges.parchment.com/o/token***arrow-up-right](https://api.test.badges.parchment.com/o/token). For more detailed information on OAuth2 read RFC 6749 [https://tools.ietf.org/html/rfc6749arrow-up-right](https://tools.ietf.org/html/rfc6749). For production environments, HTTPS is required for redirect URIs, and localhost or developer machine tunnel domains are not permitted.

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).