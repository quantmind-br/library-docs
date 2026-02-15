---
title: Getting Started | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/getting-started
source: sitemap
fetched_at: 2026-02-15T08:59:06.014301-03:00
rendered_js: false
word_count: 1138
summary: This document provides a guided introduction to the Parchment Digital Badges API, explaining how to authenticate and automate the creation of issuers, badge classes, and assertions. It serves as a starting point for developers to integrate open badge functionality into their systems.
tags:
    - parchment-api
    - digital-badges
    - oauth2-authentication
    - open-badges-specification
    - api-integration
    - badge-issuance
category: tutorial
---

Here are some guided examples through which you can learn how to use the Parchment Digital Badges API by showing you how to authenticate, create an Issuer, define a BadgeClass, and issue an Assertion. There are many more things that you can do with the Parchment Digital Badges API. See full Parchment Digital Badges API Docs for a list of endpoints and other pages of this documentation to get more detailed instructions.

We support servers in various regions as well as a test server. The UI domain and API domain vary based on which server you are using. Please review the domains for Parchment Digital Badges environments around the globe. We use the US domain as a default in our documentation so be sure to substitute the proper domain if you are not using the US production servers.

Parchment Digital Badges uses OAuth2 for most operations. As an API client user, you may obtain an OAuth2 Bearer Token on behalf of your own Parchment Digital Badges user account using a password-based grant, or you can obtain such auth tokens on behalf of many users by registering your own Connected App. See more about registering for an app key and secret in the *Developers: Build an app that integrates with the Parchment Digital Badges API* section.

This guide will focus on getting started quickly, so we’ll use a password-based grant on Parchment Digital Badges’s US-based hosted service. Request authentication by making a POST request to https://api.badges.parchment.com/o/token with your email address and password.

For example, with cURL:

```
curl-XPOST'https://api.badges.parchment.com/o/token'-d"username=YOUREMAIL&password=YOURPASSWORD"
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

### Authenticating requests with an OAuth2 Bearer token

Add an ***Authorization*** header to each of the subsequent API requests with a value of ***Bearer*** ***YOURACCESSTOKEN***, (replacing YOURACCESSTOKEN with the value of the ***access\_token*** key in the above response).

For example, in a request to retrieve the user’s own profile using cURL, this header would be set like:

```
curl 'https://api.badges.parchment.com/v2/users/self' -H "Authorization: Bearer YOURACCESSTOKEN"
```

Some of the most important API calls that clients make against the Parchment Digital Badges API are to issue badges. Issuing manually via the web interface is great, but in order to scale your badge issuing programs, you’ve got to start automating, and the Parchment Digital Badges API makes it easy. Every badge is awarded by an Issuer, so we’ll start by creating an Issuer, then we’ll define the BadgeClass to award, and finally we’ll award an Assertion of that BadgeClass.

Each of the three requests we’ll start with in this section is a POST request. We recommend using the API in JSON for both request body ***Content-Type*** and response body content. By default, if you do not specify an ***Accept: application/json*** header, JSON will be returned.

**Request Path**: /v2/issuers

An Issuer Profile describes an entity that awards Open Badges. It is published as the Open Badges [Profile (Issuer)arrow-up-right](https://www.imsglobal.org/sites/default/files/Badges/OBv2p0Final/index.html#Profile) class.

Properties:

- ***name*** is required: string.
- ***description*** is required: string.
- ***url*** is required. This should be a fully-qualified URL of a page that describes this issuer/program.
- ***image*** is optional should be base-64 encoded strings and may only be PNG or SVG. For example, a small PNG image file should appear like this in request bodies that require an image field: ***"image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mN0nmxRDwADvgGPapFGzwAAAABJRU5ErkJggg=="***
- ***email*** must be a verified email on the authenticating user’s Parchment Digital Badges account. Get ***/v2/users/self*** to retrieve your profile and see your verified email addresses.
- ***organizationId*** is the ID of your existing organization under which your issuer will be created.

**Request Path**: /v2/issuers/**:issuer\_id**/badgeclasses A BadgeClass is a type of badge that an Issuer may award over and over (creating many Assertions of that BadgeClass, each for a different recipient). See Open Badges Specification: [BadgeClassarrow-up-right](https://www.imsglobal.org/sites/default/files/Badges/OBv2p0Final/index.html#BadgeClass)

Properties:

- ***name*** is required: string.
- ***description*** is required: string.
- ***image*** is required and may only be PNG or SVG format. For example, a small PNG image file should appear like this in request bodies that require an image field: ***"image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mN0nmxRDwADvgGPapFGzwAAAABJRU5ErkJggg=="***
- Criteria is required. One or both of ***criteriaNarrative*** (a markdown-formatted string) and/or ***criteriaUrl*** (a fully-qualified URL of a page representing the criteria for this badge) must be supplied.
- ***tags*** is optional. If present, it should be a list of one or more strings;
- ***alignments*** is optional. If present, it should be a list (\[]) of one or more JSON objects that each have these properties:
  
  - ***targetName*** required, string
  - ***targetUrl*** required, fully-qualified URL string
  - ***targetDescription*** optional, string
  - ***targetFramework*** optional, string (what competency framework name does this alignment target fall under?)
  - ***targetCode*** optional, string (is there a sub-tag under the targetUrl that distinguishes this from other possible targets that you would identify with the EXACT same URL? Only use this if the ***targetUrl*** would be otherwise ambiguous.)

**Request Path**: /v2/badgeclasses/**:badgeclass\_id**/assertions

An Assertion is an instance of a BadgeClass (type of achievement recognized by an Issuer) that is awarded to one recipient. There might be many Assertions of a particular BadgeClass that an Issuer has awarded to different recipients. See Open Badges Specification: [Assertionarrow-up-right](https://www.imsglobal.org/sites/default/files/Badges/OBv2p0Final/index.html#Assertion)

Properties:

- ***recipient*** is required, (the only required property) and it must be a JSON object with at least an ***identity*** key. Other optional properties of the ***recipient*** “IdentityObject” include: ***type*** (what type of identifier is ***identity***? Choose between ***email***, ***telephone***, and ***url***); and ***hashed*** (boolean, should the ***identity*** be hashed in the final Open Badges Assertion?). When you GET the object back from the API, ***plaintextIdentity***, a read-only property appears to show you what your original ***identity*** value was in case it is obscured behind the public-facing hash (when ***hashed == true***).
- ***recipient*** is required, (the only required property) and it must be a JSON object with the following properties:
  
  - ***type*** determines what type of identifier is ***identity***, choose between ***email*** (default), ***telephone***, and ***url***)
  - ***identity*** is the value of the recipient identifier, for example an email address
  - ***hashed*** (boolean, should the ***identity*** be hashed in the final Open Badges Assertion?). When you GET the object back from the API, ***plaintextIdentity***, a read-only property appears to show you what your original ***identity*** value was in case it is obscured behind the public-facing hash (when ***hashed == true***).
- Evidence may be expressed in terms of an overall “narrative” and/or one or more “evidence items”. ***narrative*** is an optional property that accepts Markdown-formatted strings. ***evidence*** is a property that accepts a list (\[]) of JSON objects ({}) that each have a ***narrative*** and/or an ***id*** (which is a URL to a piece of evidence hosted on HTTP)
- ***issuedOn*** is optional: you may override the issue date with a date in the past. Expects an ISO8601 formatted datetime stamp including time zone identifier. e.g. ***2018-11-26T13:45:00Z*** (In this case, “Z” stands for “Zulu”, UTC)
- ***expires*** is an optional expiration date for the Assertion. Same format expectations as ***issuedOn***.

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).