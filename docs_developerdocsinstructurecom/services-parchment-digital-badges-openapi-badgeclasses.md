---
title: Badgeclasses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi/badgeclasses
source: sitemap
fetched_at: 2026-02-15T08:58:42.918614-03:00
rendered_js: false
word_count: 1374
summary: This document details the v2 API endpoints for managing digital badge classes, issuing assertions to recipients, and configuring claim codes within the Badgr ecosystem. It specifies authentication requirements, required scopes, and request parameter structures for creating, updating, and retrieving badge-related data.
tags:
    - rest-api
    - digital-badges
    - oauth2-authentication
    - badge-management
    - assertion-issuance
    - open-badges
category: api
---

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

include\_archivedbooleanOptionalDefault: `false`

/v2/badgeclasses/{idOrEntityId}

### Update an existing BadgeClass.

Previously awarded Assertions will be updated with image rebaking

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

namestring · max: 1024RequiredExample: `Math Expert`

descriptionstring · max: 16384Required

Short description of the BadgeClass

Example: `This badge is awarded to students who have demonstrated mastery of Math.`

imagestringRequired

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.io/public/badges/iOMWsaF1QbmMCofM54JlUg/image`

achievementTypestringOptionalExample: `Course`

criteriaUrlstring · uriOptional

External URL that describes in a human-readable format the criteria for the BadgeClass

Example: `https://example.com/badge-classes/1/criteria`

criteriaNarrativestringOptional

Markdown formatted description of the criteria

tagsstring\[]Optional

List of tags that describe the BadgeClass

imageAltTextstringOptional

/v2/badgeclasses/{idOrEntityId}

Restricted to owners or editors (not staff) of the corresponding Issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

hard\_deletestringOptional

archivalNotestringOptional

/v2/badgeclasses/{idOrEntityId}

### Update an existing ClaimCode for a BadgeClass

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

labelstringOptional

The label of the claim code

Example: `Conference Event`

limitinteger · int64Optional

The number of times the claim code can be used

Example: `10`

expirationDatestring · date-timeOptional

/v2/badgeclasses/{idOrEntityId}/claim-codes/{claimCode}

### Archive a ClaimCode for a BadgeClass

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/badgeclasses/{idOrEntityId}/claim-codes/{claimCode}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

include\_archivedbooleanOptionalDefault: `false`

/v2/badgeclasses/ref/{ref}

### Update an existing BadgeClass.

Previously awarded Assertions will be updated with image rebaking

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

namestring · max: 1024RequiredExample: `Math Expert`

descriptionstring · max: 16384Required

Short description of the BadgeClass

Example: `This badge is awarded to students who have demonstrated mastery of Math.`

imagestringRequired

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.io/public/badges/iOMWsaF1QbmMCofM54JlUg/image`

achievementTypestringOptionalExample: `Course`

criteriaUrlstring · uriOptional

External URL that describes in a human-readable format the criteria for the BadgeClass

Example: `https://example.com/badge-classes/1/criteria`

criteriaNarrativestringOptional

Markdown formatted description of the criteria

tagsstring\[]Optional

List of tags that describe the BadgeClass

imageAltTextstringOptional

/v2/badgeclasses/ref/{ref}

Restricted to owners or editors (not staff) of the corresponding Issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

hard\_deletestringOptional

archivalNotestringOptional

/v2/badgeclasses/ref/{ref}

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

### Get a list of BadgeClasses for a single Issuer

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

include\_archivedbooleanOptionalDefault: `false`

/v2/issuers/{idOrEntityId}/badgeclasses

### Create a new BadgeClass associated with an Issuer

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

issuerstringOptionalExample: `ZvYydoQhRtOKalNzFPZR2A-Q`

namestring · max: 1024RequiredExample: `Math Expert`

imagestringRequired

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.io/public/badges/iOMWsaF1QbmMCofM54JlUg/image`

achievementTypestringOptionalExample: `Course`

descriptionstring · max: 16384Required

Short description of the BadgeClass

Example: `This badge is awarded to students who have demonstrated mastery of Math.`

criteriaUrlstring · uriOptional

External URL that describes in a human-readable format the criteria for the BadgeClass

Example: `https://example.com/badge-classes/1/criteria`

criteriaNarrativestringOptional

Markdown formatted description of the criteria

tagsstring\[]Optional

List of tags that describe the BadgeClass

imageAltTextstringOptional

/v2/issuers/{idOrEntityId}/badgeclasses

### Get a list of BadgeClasses for authenticated user

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

include\_archivedbooleanOptionalDefault: `false`

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerstringRequiredExample: `ZvYydoQhRtOKalNzFPZR2A-Q`

namestring · max: 1024RequiredExample: `Math Expert`

descriptionstring · max: 16384Required

Short description of the BadgeClass

Example: `This badge is awarded to students who have demonstrated mastery of Math.`

imagestringRequired

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://example.com/images/1`

achievementTypestringOptionalExample: `Course`

criteriaUrlstring · uriOptional

External URL that describes in a human-readable format the criteria for the BadgeClass

Example: `https://example.com/badge-classes/1/criteria`

criteriaNarrativestringOptional

Markdown formatted description of the criteria

tagsstring\[]Optional

List of tags that describe the BadgeClass

imageAltTextstringOptional

Create a duplicate of the original BadgeClass with a new name

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

newNamestringRequired

The new name for the duplicate badgeclass

Example: `Badgeclass Copy`

/v2/badgeclasses/{idOrEntityId}/duplicate

### Get a list of ClaimCodes for a single BadgeClass

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

includeClaimCodeCountbooleanOptional

/v2/badgeclasses/{idOrEntityId}/claim-codes

### Create a new ClaimCode for a BadgeClass

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

labelstringOptional

The label of the claim code

Example: `Conference Event`

limitinteger · int64Optional

The number of times the claim code can be used

Example: `10`

expirationDatestring · date-timeOptional

/v2/badgeclasses/{idOrEntityId}/claim-codes

### Reactivate a BadgeClass by id

Reactivate a BadgeClass that was archived

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/badgeclasses/reactivate/{idOrEntityId}

### Reactivate a BadgeClass by ref

Reactivate an archived BadgeClass by its base64 encoded OpenBadge ID

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

/v2/badgeclasses/reactivate/ref/{ref}

### Enable a disabled ClaimCode for a BadgeClass

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/badgeclasses/{idOrEntityId}/claim-codes/{claimCode}/enable

### Disable an enabled ClaimCode for a BadgeClass

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/badgeclasses/{idOrEntityId}/claim-codes/{claimCode}/disable

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).