---
title: Grades Exchange API | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/datasync/grades-oas
source: sitemap
fetched_at: 2026-02-15T08:56:05.653604-03:00
rendered_js: false
word_count: 839
summary: This document defines the API endpoints and authentication requirements for managing grades exchanges, batch processing, and grade synchronization schedules.
tags:
    - api-documentation
    - grades-exchange
    - lti-authorization
    - oauth2
    - data-synchronization
    - batch-processing
    - error-handling
category: api
---

Get a list of Grades Exchanges

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

course\_app\_idstringOptional

statestring · enumOptionalPossible values:

posted\_bystring · enumOptionalPossible values:

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

metadataobject · nullableOptional

### Get count of Grades Exchanges

Get the total count of Grades Exchanges (in scope of the actor credentials and the provided query parameters). Useful for determining the maximum page number of listExchanges (diving the returned number by the desired page size).

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

course\_app\_idstringOptional

statestring · enumOptionalPossible values:

posted\_bystring · enumOptionalPossible values:

### Find a Grades Exchange by id

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Exchange to find

course\_app\_idstringOptional

### List Grades Exchange Errors

Get a list of Grades Exchange Errors

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Exchange to list Errors

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

course\_app\_idstringOptional

### Create Grades Exchange Errors

Create a list of Grades Exchange Errors

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Exchange to create Errors

idstring · uuidRead-onlyOptional

created\_atstring · date-timeRead-onlyOptional

updated\_atstring · date-timeRead-onlyOptional

codestring · enumOptionalPossible values:

messagestringRead-onlyOptional

### Create Grades Exchange Data

Create Grades data for an Exchange

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Exchange to create Data

### Get Grades Exchange Details

Get the details artifact for a completed Exchange. The response is a .json.gz file but it is not decompressed by the client implicitly. If no details were produced (early failure), a 404 response will be returned.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Exchange to get details

course\_app\_idstringOptional

200

Exchange Details response

404

Exchange not found or the artifact is not available for it

/exchanges/{id}/artifacts/details

### Get Grades Exchange Consumer Logs

Get the consumer logs artifact for a completed Exchange. The response is a .json.gz file but it is not decompressed by the client implicitly. If no logs were produced (nothing was sent to SIS), a 404 response will be returned.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Exchange to get details

course\_app\_idstringOptional

200

Exchange Details response

404

Exchange not found or the artifact is not available for it

/exchanges/{id}/artifacts/consumerlogs

Returns details about the entity designated as this Grades Application's consumer.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

200

Consumer Details response

400

Consumer is not configured

### Resolve the section by ID

Resolves the provided Data Sync ID to an ID in the consumer's id space.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### List Batch Grades Exchanges

Get a list of Batch Grades Exchanges

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### Get count of Batch Grades Exchanges

Get the total count of Batch Grades Exchanges

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

### Get Batch Exchange Course IDs Report

Get the course IDs report for a Batch Exchange. The response is a CSV file.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Batch Exchange to get course IDs

### Create Batch Grades Exchange Error

Create a Batch Grades Exchange Error

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Batch Grades Exchange to create Error

codestring · enumOptionalPossible values:

200

Batch Exchange Error response

### Create Grades Exchange Batch Context Data

Create context data for a Batch Exchange

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Batch Exchange to create Context Data

course\_idsstring\[]Optional

200

Batch Exchanges Context Data response

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Update a grades schedule. Only the `enabled` attribute may be updated.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Schedule to update

Enqueues a grade schedule for execution

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the schedule to be executed

object · nullableOptional

409

Conflict, when running the schedule is rejected

429

When running the schedule is rejected due to rate limiting

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).