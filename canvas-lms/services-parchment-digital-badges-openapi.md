---
title: APIs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi
source: sitemap
fetched_at: 2026-02-15T08:55:57.411225-03:00
rendered_js: false
word_count: 3863
summary: Technical documentation for API endpoints used to manage digital badge issuers, staff permissions, and user profile data.
tags:
    - api-reference
    - issuer-management
    - user-profiles
    - digital-badges
    - authorization-scopes
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

### Get a single BadgeUser profile

This endpoint requires the following scopes:

- : See who you are
- : Update your profile

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

This endpoint requires the following scopes:

- : See who you are
- : Update your profile

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

firstNamestringOptionalExample: `Jane`

lastNamestringOptionalExample: `Doe`

marketingOptInbooleanOptionalExample: `true`

This endpoint requires the following scopes:

- : See who you are
- : Update your profile

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

firstNamestringOptionalExample: `Jane`

lastNamestringOptionalExample: `Doe`

marketingOptInbooleanOptionalExample: `true`

### Get your own BadgeUser profile

This endpoint requires the following scopes:

- : See who you are
- : Update your profile

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

### Update your own BadgeUser

This endpoint requires the following scopes:

- : See who you are
- : Update your profile

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

firstNamestringOptionalExample: `Jane`

lastNamestringOptionalExample: `Doe`

marketingOptInbooleanOptionalExample: `true`

### Update your own BadgeUser

This endpoint requires the following scopes:

- : See who you are
- : Update your profile

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

firstNamestringOptionalExample: `Jane`

lastNamestringOptionalExample: `Doe`

marketingOptInbooleanOptionalExample: `true`

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

/v2/pathways/{id}/versions/draft

/v2/pathways/{id}/versions/draft

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

### Create pathway in draft state

issuerIdstringRequired

ID of the issuer where the pathway will be created

Example: `62aa04adf5afe00d0a6dac72`

### Evaluate experience on the pathway for a user

experienceIdstring · uuidRequired

/v2/pathways/{pathwayId}/experience/{experienceId}/submit

### Evaluate experience on the pathway for multiple users

CSV file should contain recipientId,passed header row. Each row should contain a single entry of recipientId (email:[mail@example.com](mailto:mail@example.com)) and a passed value (true/false) separated by a comma.

experienceIdstring · uuidRequired

stringOptionalExample: `recipientId,passed email:mail@example.com,true`

/v2/pathways/{pathwayId}/experience/{experienceId}/submit-csv

/v2/pathways/{id}/versions/published

### Promote current draft version to published

/v2/pathways/{id}/versions/published

### Reverts pathway draft to the current published version

/v2/pathways/{id}/versions/draft/revert

### Update pathway group subscriptions

groupIdsToAddstring\[]RequiredExample: `61aa04adf5afe00d0a6dac72`

groupIdsToRemovestring\[]RequiredExample: `67aa04adf5afe00d0a6dac72`

/v2/pathways/{id}/subscriptions

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

### Get progress status for the recipient

recipientIdentifierstringRequired

Identifier of the recipient, format: recipientType:recipientId

Example: `email:mail@example.com`

/v2/pathways/{id}/recipient-progress

### Get progress status for the recipient group

recipientGroupIdstringRequired

/v2/pathways/{id}/recipient-groups/{recipientGroupId}/progress

### Get aggregate progress status for the entire pathway

/v2/pathways/{id}/aggregate-progress

### Get a list of Organizations where the authenticated user is admin

This endpoint requires the following scopes:

- : Read organization data

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

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

### Get a list of Assertions in authenticated user's backpack

This endpoint requires the following scopes:

- : List assertions in your backpack
- : Upload badges to your backpack

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

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