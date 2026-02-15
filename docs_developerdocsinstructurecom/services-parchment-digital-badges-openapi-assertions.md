---
title: Assertions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi/assertions
source: sitemap
fetched_at: 2026-02-15T08:58:51.530457-03:00
rendered_js: false
word_count: 440
summary: This document defines API endpoints for managing digital badge assertions, including procedures for issuing new badges, revoking existing ones, and retrieving assertion records.
tags:
    - api-endpoints
    - digital-badges
    - badge-assertions
    - open-badges
    - oauth2-auth
    - credential-management
category: api
---

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/assertions/{idOrEntityId}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

narrativestringOptional

Markdown narrative of the achievement

expiresstring · date-timeOptional

issuedOnstring · date-timeOptional

Timestamp when the assertion was issued

/v2/assertions/{idOrEntityId}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

revocation\_reasonstringOptional

/v2/assertions/{idOrEntityId}

### Get list of Assertions for the specified scope

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

scopestring · enumRequiredPossible values:

idOrEntityIdstringRequired

recipientstringOptional

A recipient identifier to filter by

numinteger · int32Optional

Request pagination of results, before/after cursors may be provided in response header

include\_expiredbooleanOptionalDefault: `false`

include\_revokedbooleanOptionalDefault: `false`

afterstringOptional

Pagination cursor provided in "Link" response header

beforestringOptional

Pagination cursor provided in "Link" response header

/v2/{scope}/{idOrEntityId}/assertions

### Issue a new Assertion to a recipient

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

scopestring · enumRequiredPossible values:

idOrEntityIdstringRequired

The entity ID of the selected scope entity

Example: `K829IK8RS6ercwkpeFOn-Q`

Request to award an assertion. When request scope is issuers, one of badgeclass or badgeclassOpenBadgeId must be provided.

badgeclassstringOptional

ID or Entity ID of the badge class to be awarded

Example: `K829IK8RS6ercwkpeFOn-Q`

badgeclassOpenBadgeIdstring · uriOptional

OB URL of the badge class to be awarded

Example: `https://api.badgr.io/public/badges/K829IK8RS6ercwkpeFOn-Q`

issuedOnstring · date-timeOptional

Timestamp when the assertion was issued

allowDuplicateAwardsbooleanOptional

If set to false and the recipient already has this assertion, then the request will fail

narrativestringOptional

Markdown narrative of the achievement

expiresstring · date-timeOptional

/v2/{scope}/{idOrEntityId}/assertions

### Revoke multiple Assertions

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idstringOptional

ID of the Assertion to revoke

Example: `62aa04adf5afe00d0a6dac72`

entityIdstringOptional

Entity ID of the Assertion to revoke

Example: `i9CirfwJTuSfiqg0FFUBdQ`

revocationReasonstringRequired

Short description of why the Assertion is being revoked

Example: `Course was cancelled`

revokedbooleanRead-onlyOptional

reasonstringRead-onlyOptional

Error reason if assertion could not be revoked

codestringRead-onlyOptional

Error code if assertion could not be revoked

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).