---
title: Public JWK | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/public_jwk
source: sitemap
fetched_at: 2026-02-15T09:09:10.36073-03:00
rendered_js: false
word_count: 98
summary: This document describes the Public JWK API endpoint for Canvas LMS, which allows developers to rotate public keys for LTI services.
tags:
    - canvas-lms
    - api-endpoint
    - lti-services
    - public-jwk
    - developer-key
    - security
category: api
---

circle-exclamation

**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentationarrow-up-right](https://api.instructure.com)).

## [hashtag](#public-jwk-api) Public JWK API

### [hashtag](#method.lti-public_jwk.update) [Update Public JWK](https://developerdocs.instructure.com/services/canvas/resources/public_jwk#method.lti/public_jwk.update)

[Lti::PublicJwkController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/public_jwk_controller.rb)

`PUT /api/lti/developer_key/update_public_jwk`

**Scope:** `url:PUT|/api/lti/developer_key/update_public_jwk`

Rotate the public key in jwk format when using lti services

**Request Parameters:**

Parameter

Type

Description

`public_jwk`

Required `json`

The new public jwk that will be set to the tools current public jwk.

Returns a [DeveloperKey](https://developerdocs.instructure.com/services/canvas/resources/developer_keys#developerkey) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

[PreviousProgresschevron-left](https://developerdocs.instructure.com/services/canvas/resources/progress)[NextQuiz Assignment Overrideschevron-right](https://developerdocs.instructure.com/services/canvas/resources/quiz_assignment_overrides)

Last updated 5 months ago

Was this helpful?