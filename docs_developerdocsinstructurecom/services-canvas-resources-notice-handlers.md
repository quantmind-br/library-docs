---
title: Notice Handlers | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/notice_handlers
source: sitemap
fetched_at: 2026-02-15T09:09:47.698917-03:00
rendered_js: false
word_count: 151
summary: This document provides the API specification for the LTI Platform Notification Service, detailing how to list and manage notice handlers for LTI tool deployments in Canvas.
tags:
    - lti-advantage
    - canvas-lms
    - notification-service
    - api-reference
    - notice-handlers
category: api
---

API for the LTI Platform Notification Service.

Requires LTI Advantage (JWT OAuth2) tokens with the `https://purl.imsglobal.org/spec/lti/scope/noticehandlers` scope.

See the Canvas [Platform Notification Service](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.pns) intro guide for an overview of these endpoints and information on specific notice types.

**A NoticeCatalog object looks like:**

```
// Set of notice handlers (one per notice type) for an LTI tool deployment.
{
  // The LTI tool's client ID (global developer key ID)
"client_id": "10000000000001",
  // String that identifies the Platform-Tool integration governing the notices
"deployment_id": "123:8865aa05b4b79b64a91a86042e43af5ea8ae79eb",
  // List of notice handlers for the tool
"notice_handlers": [{"handler":"","notice_type":"LtiHelloWorldNotice"}]
}
```

**A NoticeHandler object looks like:**

```
// A notice handler for a particular tool deployment and notice type.
{
  // URL to receive the notice
"handler": "https://example.com/notice_handler",
  // The type of notice
"notice_type": "LtiHelloWorldNotice",
  // The maximum number of notices to include in a single batch, or 'null' if not
  // set.
"max_batch_size": 100
}
```

[Lti::Ims::NoticeHandlersController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/notice_handlers_controller.rb)

`GET /api/lti/notice-handlers/:context_external_tool_id`

**Scope:** `url:GET|/api/lti/notice-handlers/:context_external_tool_id`

List all notice handlers for the tool

**Example Response:**

```
{
"client_id": 10000000000267,
"deployment_id": "123:8865aa05b4b79b64a91a86042e43af5ea8ae79eb",
"notice_handlers": [
{
"handler":"",
"notice_type":"LtiHelloWorldNotice"
}
  ]
}
```

Returns a [NoticeCatalog](https://developerdocs.instructure.com/services/canvas/resources/notice_handlers#noticecatalog) object.

[Lti::Ims::NoticeHandlersController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/ims/notice_handlers_controller.rb)

`PUT /api/lti/notice-handlers/:context_external_tool_id`

**Scope:** `url:PUT|/api/lti/notice-handlers/:context_external_tool_id`

Subscribe (set) or unsubscribe (remove) a notice handler for the tool

**Request Parameters:**

URL to receive the notice, or an empty string to unsubscribe

The maximum number of notices to include in a single batch

**Example Response:**

```
{
"handler": "",
"notice_type": "LtiHelloWorldNotice"
}
```

Returns a [NoticeHandler](https://developerdocs.instructure.com/services/canvas/resources/notice_handlers#noticehandler) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).