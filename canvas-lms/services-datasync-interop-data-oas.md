---
title: Interop Data API | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/datasync/interop-data-oas
source: sitemap
fetched_at: 2026-02-15T09:15:29.167696-03:00
rendered_js: false
word_count: 1260
summary: This document outlines the API endpoints for managing task queues and retrieving educational rostering data, including organizations, students, and teachers.
tags:
    - api-reference
    - task-management
    - rostering-data
    - oauth2-authentication
    - lti-jwt
    - data-integration
category: api
---

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Get the next batch of Tasks for the authenticated actor. The number of Tasks returned is determined by Kimono and may change from time to time. See [Tasks]() for details.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

tenant\_idstring · uuidOptional

Specify the tenant\_id to restrict this operation to

schemastring · enumOptional

Specify the Task Schema to use for this operation

Possible values:

driverstringOptional

Restrict Tasks to a specific Driver by name

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Each Task that is returned from `listTasks` must be acknowledged to remove it from the Task Queue. If a Task is not acknowledged in a timely fashion Kimono may consider it to have timed-out and will return it in the next `listTasks` response for an Integration tenant. See [Tasks]() for details.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Task to acknowledge

task\_idstring · UUIDOptional

Task ID to acknowledge (Required if multiple TaskAcks are in a single request)

statusstring · enumOptionalPossible values:

messagestringOptional

Optional message to record and display in Kimono.

$sys.app\_idstringOptional

200

Task acknowledged successfully

Acknowledge a group of Tasks. Each Task that is returned from `listTasks` must be acknowledged to remove it from the Task Queue. If a Task is not acknowledged in a timely fashion Kimono may consider it to have timed-out and will return it in the next `listTasks` response for an Integration tenant. See [Tasks]() for details.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

task\_idstring · UUIDOptional

Task ID to acknowledge (Required if multiple TaskAcks are in a single request)

statusstring · enumOptionalPossible values:

messagestringOptional

Optional message to record and display in Kimono.

$sys.app\_idstringOptional

200

All Tasks acknowledged successfully

404

One or more Tasks not found

List Tasks for the authenticated actor. See [Tasks]() for details.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

schemastring · enumOptional

Specify the Task Schema to use for this operation

Possible values:

driverstringOptional

Restrict Tasks to a specific Driver by name

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

Each Task that is consumed by the client must be acknowledged to remove it from the Task Queue.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

id of the Task to acknowledge

task\_idstring · UUIDOptional

Task ID to acknowledge (Required if multiple TaskAcks are in a single request)

statusstring · enumOptionalPossible values:

messagestringOptional

Optional message to record and display in Kimono.

$sys.app\_idstringOptional

200

Task acknowledged successfully

### Acknowledge Tasks (Admin)

Acknowledge a group of Tasks. Each Task that is consumed by the client must be acknowledged to remove it from the Task Queue.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

task\_idstring · UUIDOptional

Task ID to acknowledge (Required if multiple TaskAcks are in a single request)

statusstring · enumOptionalPossible values:

messagestringOptional

Optional message to record and display in Kimono.

$sys.app\_idstringOptional

200

All Tasks acknowledged successfully

404

One or more Tasks not found

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

Delete a Task from the Task Queue. This operation is only available via the Task Admin API.

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### List all School-type Orgs

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

### List Students that are members of an Org

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

/rostering/orgs/{id}/students

### List Teachers that are members of an Org

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

/rostering/orgs/{id}/teachers

### List Courses that belong to an Org

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

/rostering/orgs/{id}/courses

### List Sections that belong to an Org

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

/rostering/orgs/{id}/sections

### List Terms that belong to an Org

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

/rostering/orgs/{id}/terms

### Find an LEA-type Org by $sys.id

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### List all Student-type Persons

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### List all Teacher-type Persons

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

idstring · uuidRequired

$sys.id of the Person to find

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

idstring · uuidRequired

$sys.id of the Course to find

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

### Find a Section by $sys.id

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

idstring · uuidRequired

$sys.id of the Section to find

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

idstring · uuidRequired

$sys.id of the Term to find

### List all Grading Categories

OAuth2clientCredentialsRequired

AuthorizationstringRequired

AuthorizationstringRequired

LTI JWT Authorization header using the Bearer scheme

pageinteger · int32Optional

Specify the page number (defaults to 0)

page\_sizeinteger · int32Optional

Specify the page\_size (defaults to the maximum page size)

/grades/gradingCategories

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).