---
title: Pathways | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/openapi/pathways
source: sitemap
fetched_at: 2026-02-15T08:57:12.638638-03:00
rendered_js: false
word_count: 191
summary: Technical documentation for the v2 Pathways API, detailing endpoints for managing pathway drafts, publishing versions, tracking learner progress, and handling experience evaluations.
tags:
    - api-documentation
    - pathway-management
    - version-control
    - learner-progress
    - issuer-services
category: api
---

/v2/pathways/{id}/versions/draft

/v2/pathways/{id}/versions/draft

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

### List all pathways for the issuer

This endpoint requires the following scopes:

- : Award badges and update your issuers

OAuth2authorizationCodeRequired

OAuth2 authorizationCode flow is currently not functional on the Swagger UI.

Authorization URL: Token URL:

idOrEntityIdstringRequired

/v2/issuers/{idOrEntityId}/pathways

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).