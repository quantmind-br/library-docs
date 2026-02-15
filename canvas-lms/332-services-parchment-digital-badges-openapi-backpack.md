---
title: Backpack | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi/backpack
source: sitemap
fetched_at: 2026-02-15T08:58:58.49692-03:00
rendered_js: false
word_count: 535
summary: This document outlines API endpoints for managing digital badge assertions and collections within a user's backpack, covering operations for uploading, retrieving, updating, and deleting credentials.
tags:
    - api-documentation
    - digital-badges
    - backpack-management
    - badge-assertions
    - oauth2-authentication
    - openbadges
category: api
---

### Get Assertion Collection(s) associated with the authenticated user's backpack

This endpoint requires the following scopes:

- : List assertions in your backpack
- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/backpack/collections/{idOrEntityId}

This endpoint requires the following scopes:

- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

namestringOptionalExample: `My Collection`

descriptionstringOptional

Short description of the Collection

Example: `This is a collection of my favorite badges`

publishedbooleanOptional

True if the Collection should have a share url

Example: `true`

assertionsstring\[]Optional

The IDs or entity IDs of the assertions associated with this Collection

Example: `UQbhRmNrQ4qn9_FJ5-eTtA`

credentialsstring\[]Optional

The IDs or entity IDs of the credentials associated with this Collection

Example: `UQbhRmNrQ4qn9_FJ5-eTtA`

/v2/backpack/collections/{idOrEntityId}

This endpoint requires the following scopes:

- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/backpack/collections/{idOrEntityId}

### Get detail on an Assertion in the user's Backpack

This endpoint requires the following scopes:

- : List assertions in your backpack
- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/backpack/assertions/{idOrEntityId}

### Update acceptance of an Assertion in the user's Backpack

This endpoint requires the following scopes:

- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/backpack/assertions/{idOrEntityId}

### Remove an assertion from the backpack

This endpoint requires the following scopes:

- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/backpack/assertions/{idOrEntityId}

### Upload a new Assertion to the backpack

Upload a new Assertion to the backpack using url, image or OpenBadge JSON

This endpoint requires the following scopes:

- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

urlstring · uriOptional

URL of the badge to import

Example: `https://example.com/assertions/1`

assertionobjectOptional

OpenBadge JSON of the award to import

imagestringOptional

Image URL or base64 encoded image data of the assertion.

Example: `https://example.com/assertions/1/image`

### Get Assertion Collection(s) associated with the authenticated user's backpack

This endpoint requires the following scopes:

- : List assertions in your backpack
- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

This endpoint requires the following scopes:

- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

namestringRequiredExample: `My Collection`

descriptionstringOptional

Short description of the Collection

Example: `This is a collection of my favorite badges`

publishedbooleanRequired

True if the Collection should have a share url

Example: `true`

### Get a list of Assertions in authenticated user's backpack

This endpoint requires the following scopes:

- : List assertions in your backpack
- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).