---
title: Interop API | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/datasync/interop-oas
source: sitemap
fetched_at: 2026-02-15T09:15:16.599889-03:00
rendered_js: false
word_count: 1807
summary: This document specifies a set of API endpoints for managing Interop Clouds, actors, integrations, and tenants, including authentication requirements and CRUD operations.
tags:
    - interop-clouds
    - api-endpoints
    - integration-management
    - tenant-management
    - oauth2-authentication
    - lti-jwt
category: api
---

Get a list of actors installed in Interop Clouds for accounts visible to you. This API is used to obtain coordinates and credentials essential for interacting with Integrations and other actors.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Get a list of Interop Clouds for accounts visible to you.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

Get a list of Interop Clouds matching the search criteria.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

generationinteger · int32Optional

List all Clouds of a matching generation

userdatastringOptional

List all Clouds with matching userdata

namestringOptional

List all Clouds with a matching name

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Find an Interop Cloud by identifier

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Cloud to delete

### List all Actors in an Interop Cloud

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

include\_credentialsbooleanOptional

Include actor credentials

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

namestringOptional

Find an Integration by name

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### List Integration Versions

List the versions of an Integration. Each version is described by an Integration Blueprint.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

200

Integration Versions response

/integrations/{id}/versions

200

Integration Versions response

### Create Integration Version

Create a new version of an Integration

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

/integrations/{id}/versions

### Update Integration Version

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Integration to update

/integrations/{id}/versions/{version}

### Delete Integration Version

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Integration to update

/integrations/{id}/versions/{version}

### Update Integration Blueprint

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Integration to update

200

IntegrationVersion response

/integrations/{id}/versions/{version}/blueprint

200

IntegrationVersion response

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Integration to find

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Integration to update

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Integration to delete

Get a list of `TenantInfo` representing your licensed and authorized Integration tenants.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

accountsstring · uuid\[] · min: 1Optional

Optionally restrict the returned list of tenants to only those for the specified Accounts.

integrationstring\[] · min: 1Optional

Optionally restrict the returned list of tenants to only those for the specified Integration or Integrations. Use this parameter when you have multiple Integrations all serviced by the same client application. When omitted, includes tenants of all Integrations owned by your account.

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the TenantInfo to find

### Find Interop Tenant by actor authentication credentials

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Get tenant state by actor authentication credentials

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

Get the list of `ScopingSchool`s that define how to scope this tenant's repository by school

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

replacebooleanOptional

true to replace existing Scoping Schools, false to append to existing Scoping Schools

Default: `true`

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the ScopingSchool to find

/tenant/scoping/schools/{id}

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Scoping School to update

account\_idstring · uuidOptional

tenant\_idstring · uuidOptional

school\_idstring · uuidOptional

school\_ref\_idstringOptional

/tenant/scoping/schools/{id}

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

/tenant/scoping/schools/{id}

Get the list of Scoping Courses to apply to this tenant's repository

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

replacebooleanOptional

true to replace existing Scoping Courses, false to append to existing Scoping Courses

Default: `true`

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the ScopingCourse to find

/tenant/scoping/courses/{id}

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Scoping Course to update

account\_idstring · uuidOptional

tenant\_idstring · uuidOptional

course\_idstring · uuidOptional

course\_ref\_idstringOptional

school\_idstring · uuidOptional

school\_ref\_idstringOptional

/tenant/scoping/courses/{id}

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

/tenant/scoping/courses/{id}

The endpoint returns tenant application's authentication parameters (defined in the integration blueprint), as well as configuration options. The tenant (identified by actor authentication credentials) must be an integration. The response should be cached by driver implementations in memory.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

200

Tenant Application Response

200

Tenant Application Response

### Update Tenant Application

Intended to be used during the authentication setup workflow (if there is authentication defined in the integration blueprint). The tenant (identified by actor authentication credentials) must be an integration. Can be updated and only when the pending auth status of the application is 'updating'). Only a subset of the Tenant Application configuration may be changed: auth message, pending auth state (can only be set to 'confirmed'/'error'), pending auth attributes.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

account\_idstring · uuidRead-onlyOptional

tenant\_idstring · uuidRead-onlyOptional

deliver\_tasksbooleanRead-onlyOptional

validate\_tasksbooleanRead-onlyOptional

auth\_typestring · enumRead-onlyOptionalPossible values:

auth\_statestring · enumRead-onlyOptionalPossible values:

auth\_session\_id\_pendingstring · uuid · nullableRead-onlyOptional

auth\_messagestring · nullableOptional

auth\_state\_pendingstring · enumOptionalPossible values:

Get the list of rollovers for the tenant. The tenant is identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

sortstring · enumOptional

Sorting criteria. Prefix with `-` for descending order.

Example: `-name`Possible values:

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### Create a rollover for the tenant identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

namestringRead-onlyRequired

start\_datestring · date-timeRead-onlyRequired

end\_datestring · date-timeRead-onlyRequired

typestring · enumRequiredPossible values:

statusstring · enumRequiredPossible values:

cloud\_idstring · uuidRequired

actor\_idstring · uuidOptional

409

Conflict due to overlap with other rollovers or concurrent modification

Get the count of rollovers for the tenant. The tenant is identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

Get a rollover for the tenant. The tenant is identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the rollover to query

### Update a rollover for the tenant identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the rollover to update

namestringRead-onlyRequired

start\_datestring · date-timeRead-onlyRequired

end\_datestring · date-timeRead-onlyRequired

typestring · enumRequiredPossible values:

statusstring · enumRequiredPossible values:

cloud\_idstring · uuidRequired

actor\_idstring · uuidOptional

409

Conflict due to overlap with other rollovers or concurrent modification

### Delete a rollover for the tenant identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the rollover to delete

409

Conflict due to trying to delete an active rollover

Get the list of schedules for the tenant. The tenant is identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### Create a Schedule for the tenant identified by actor authentication credentials. Only the \`hour\` (understood in UTC) field is expected, only creating collection schedules is possible.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

hourinteger · max: 23Required

409

Conflict due to overlaps with other schedules or concurrent modification

Only permitted for unpaused collection schedules, and if there is no pending ingestion.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Schedule to run

object · nullableOptional

204

No content, schedule queued for execution

400

Bad request, when the schedule type cannot be run on demand

409

Conflict, schedule was not run, response body contains details

/tenant/schedules/{id}/run

Get the count of schedules for the tenant. The tenant is identified by actor authentication credentials.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Schedule to find

Update a schedule. Only the `enabled` attribute may be updated.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Schedule to update

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Schedule to update

Get a list of Ingestions.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Get the total count of ingestions that would be returned by listIngestions

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Ingestion to find

Last updated 7 months ago