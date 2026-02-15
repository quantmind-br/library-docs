---
title: canvas_logs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs
source: sitemap
fetched_at: 2026-02-15T09:12:05.882237-03:00
rendered_js: false
word_count: 535
summary: This document provides the schema specification for the canvas_logs namespace, detailing the table properties and enumeration types for Canvas web application access logs. It defines fields for tracking user activity, request metadata, and system responses within the Instructure Canvas environment.
tags:
    - canvas-lms
    - data-access-platform
    - canvas-logs
    - schema-definition
    - audit-logs
    - http-metadata
    - database-schema
category: reference
---

## Tables in canvas\_logs namespace

Stores the Canvas web application server access/request logs.

Logs include all interactions made with your instance of Canvas, therefore some interactions are done by users that are not present in the `users` table (originated from another institution). Note: Logs older than the retention limit of 30 days are no longer available via DAP API.

**Properties:**

- **id** (UUID) - `primary key` The unique identifier for a logged web request.
- **timestamp** (datetime) - Timestamp when the request was made in UTC.
- **user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - The unique ID of the user that made the request.
- **real\_user\_id** ([canvas.users](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.users) | None) - If the request was processed by one user masquerading as another, then this column contains the real user ID of the user.
- **quiz\_id** ([canvas.quizzes](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.quizzes) | None) - Identifies the quiz if the request is for a quiz.
- **conversation\_id** ([canvas.conversations](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.conversations) | None) - Identifies the conversation if the request is for a conversation.
- **assignment\_id** ([canvas.assignments](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.assignments) | None) - Identifies the assignment if the request is for an assignment.
- **url** (str) - The path and the query string components of the requested URL.
- **http\_method** ([HTTPMethod](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs#dap_schemas.canvas_logs.httpmethod)) - HTTP method/verb (GET, POST, PUT, etc.) that was sent with the request.
- **http\_status** ([HTTPStatus](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs#dap_schemas.canvas_logs.httpstatus)) - HTTP status code of the request (e.g. 200 OK).
- **http\_version** ([HTTPVersion](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs#dap_schemas.canvas_logs.httpversion)) - HTTP protocol version (e.g. HTTP/2.0).
- **remote\_ip** (IPv4Address | IPv6Address) - IP (IPv4 or IPv6) address that was recorded for the request.
- **interaction\_micros** (int32) - Total time required to service the request in microseconds.
- **web\_application\_controller** ([Controller](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs#dap_schemas.canvas_logs.controller) | str | None) - The controller that the Canvas web application used to service this request.
- **web\_application\_action** ([Action](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs#dap_schemas.canvas_logs.action) | str | None) - The action in the Canvas web application used to service this request.
- **web\_application\_context\_type** ([ContextType](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvaslogs#dap_schemas.canvas_logs.contexttype) | None) - Containing object type that the Canvas web application used to service this request.
- **web\_application\_context\_id** (int64 | None) - Containing object ID that the Canvas web application used to service this request.
- **session\_id** (UUID | None) - ID of the user's session where this request was made.
- **developer\_key\_id** ([canvas.developer\_keys](https://developerdocs.instructure.com/services/dap/dataset/dataset-namespaces/dataset-canvas#dap_schemas.canvas.developer_keys) | None) - ID of the developer who accessed this resource if the request was made by a developer.
- **participated** (bool) - Shows whether the HTTP request is considered a participation for the user.
- **user\_agent** (None | Literal\[`'__dap_oversized_truncated__'`] | Annotated\[str, MaxLength(255)]) - The user agent string sent by the HTTP client.

## Types in canvas\_logs namespace

Web application actions.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

Web application context types.

**Members:**

- **assessment\_question** = `'AssessmentQuestion'`
- **assignment** = `'Assignment'`
- **content\_migration** = `'ContentMigration'`
- **course\_section** = `'CourseSection'`
- **quiz\_submission** = `'Quizzes::QuizSubmission'`
- **student\_enrollment** = `'StudentEnrollment'`
- **user\_profile** = `'UserProfile'`

Web application controllers.

**Members:**

- **unspecified** = `'__dap_unspecified__'`

HTTP methods used in the Canvas API.

**Members:**

- **UNSUBSCRIBE** = `'UNSUBSCRIBE'`
- **MKACTIVITY** = `'MKACTIVITY'`

**Members:**

- **SWITCHING\_PROTOCOLS** = `101`
- **NON\_AUTHORITATIVE\_INFORMATION** = `203`
- **PROXY\_AUTHENTICATION\_REQUIRED** = `407`
- **PRECONDITION\_FAILED** = `412`
- **REQUEST\_ENTITY\_TOO\_LARGE** = `413`
- **REQUEST\_URI\_TOO\_LONG** = `414`
- **UNSUPPORTED\_MEDIA\_TYPE** = `415`
- **REQUESTED\_RANGE\_NOT\_SATISFIABLE** = `416`
- **MISDIRECTED\_REQUEST** = `421`
- **UNPROCESSABLE\_ENTITY** = `422`
- **PRECONDITION\_REQUIRED** = `428`
- **REQUEST\_HEADER\_FIELDS\_TOO\_LARGE** = `431`
- **UNAVAILABLE\_FOR\_LEGAL\_REASONS** = `451`
- **INTERNAL\_SERVER\_ERROR** = `500`
- **SERVICE\_UNAVAILABLE** = `503`
- **HTTP\_VERSION\_NOT\_SUPPORTED** = `505`
- **VARIANT\_ALSO\_NEGOTIATES** = `506`
- **INSUFFICIENT\_STORAGE** = `507`
- **NETWORK\_AUTHENTICATION\_REQUIRED** = `511`

HTTP protocol version.

**Members:**

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).