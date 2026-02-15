---
title: Issuers | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi/issuers
source: sitemap
fetched_at: 2026-02-15T08:55:59.973237-03:00
rendered_js: false
word_count: 1788
summary: This document provides an API reference for managing badge issuers and their staff members, including endpoints for adding staff, updating roles, and modifying issuer profile information.
tags:
    - api-endpoints
    - issuer-management
    - staff-roles
    - digital-badges
    - oauth2-authentication
category: api
---

### Update a staff member's role on the Issuer

User must have an owner role on the issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

emailstringRequired

Email address associated with the staff member

Example: `jane.doe@example.com`

rolestring · enumRequired

Role of the user in the issuer.

Possible values:

/v2/issuers/{idOrEntityId}/staff

### Add a staff member to an Issuer

User must have an owner role on the issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

emailstringRequired

Email address associated with the staff member

Example: `jane.doe@example.com`

rolestring · enumRequired

Role of the user in the issuer.

Possible values:

/v2/issuers/{idOrEntityId}/staff

### Update a staff member's role on the Issuer

User must have an owner role on the issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

emailstringRequired

Email address associated with the staff member

Example: `jane.doe@example.com`

rolestring · enumRequired

Role of the user in the issuer.

Possible values:

/v2/issuers/{idOrEntityId}/staff

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

include\_staffstringOptionalDefault: `true`

/v2/issuers/{idOrEntityId}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Required

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptional

/v2/issuers/{idOrEntityId}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/issuers/{idOrEntityId}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Required

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptional

/v2/issuers/{idOrEntityId}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

include\_staffstringOptionalDefault: `true`

/v2/issuers/openBadgeId/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Required

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptional

/v2/issuers/openBadgeId/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

/v2/issuers/openBadgeId/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Required

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptional

/v2/issuers/openBadgeId/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

include\_staffstringOptionalDefault: `true`

/v2/issuers/ref/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Required

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptional

/v2/issuers/ref/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

/v2/issuers/ref/{issuerOpenBadgeIdBase64}

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

issuerOpenBadgeIdBase64stringRequired

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Required

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptional

/v2/issuers/ref/{issuerOpenBadgeIdBase64}

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

### Get a list of Issuers for authenticated user

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

include\_staffstringOptionalDefault: `true`

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

include\_staffstringOptionalDefault: `true`

namestring · max: 1024RequiredExample: `Credentials Faculty`

emailstring · email · max: 255Required

Contact email for the Issuer

Example: `contact@example.com`

urlstring · uri · max: 1024Required

Homepage or website associated with the Issuer

Example: `https://example.com`

sourceUrlstring · uriOptional

The original URL of the issuer if it was imported

Example: `https://example.com/issuers/1`

originalJsonstring · max: 2000000Optional

The original OB JSON of the issuer if it was imported

Example: `{}`

imagestringOptional

Image of the issuer. An URL or a bas64 encoded images.

Example: `https://api.badgr.ws/public/issuers/Uu4wd2I1SKmD3vmtMJ19hw/image`

descriptionstring · max: 16384Optional

Short description of the Issuer

Example: `This is the faculty of the Credentials University.`

badgrDomainstringOptionalExample: `badgrsupportgroup.badgr.com`

createdBystringOptional

User who created this issuer

organizationIdstringOptional

The ID of the organization which this issuer should be associated with. Requires organization write access.

Example: `6f4e4e4e2dc038241ad01d83`

### Invite a staff member to an Issuer

User must have an owner role on the issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

emailstringRequired

Email address associated with the staff member

Example: `jane.doe@example.com`

rolestring · enumRequired

Role of the user in the issuer.

Possible values:

/v2/issuers/{idOrEntityId}/staff/invitations

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

### List public issuers for the specified organization with pagination and optional name filtering

nameQuerystring · max: 256Optional

Case-insensitive filter for the name of the issuers

numstring · max: 9223372036854776000Optional

Number of items to return per page

Example: `10`

pagestring · min: 1Optional

Index of the requested page (1-based)

Example: `1`

/v2/organizations/{id}/public-issuers

### List all pathways for the issuer

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/issuers/{idOrEntityId}/pathways

### Remove a staff member from the Issuer

User must have an owner role on the issuer.

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

emailBase64stringRequired

Base64 encoded email address of the staff member

/v2/issuers/{idOrEntityId}/staff/{emailBase64}