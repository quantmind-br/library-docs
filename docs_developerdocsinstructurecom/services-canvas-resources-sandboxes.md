---
title: Sandboxes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/sandboxes
source: sitemap
fetched_at: 2026-02-15T09:08:34.747285-03:00
rendered_js: false
word_count: 147
summary: This document describes the LTI Sandboxes API endpoint used to download a CSV mapping of original UUIDs to new UUIDs within a Canvas LMS sandbox environment.
tags:
    - lti-sandboxes
    - canvas-lms
    - uuid-mapping
    - api-reference
    - jwt-authentication
category: api
---

**LTI Sandboxes API (Must use** [**JWT access tokens**](https://developerdocs.instructure.com/services/canvas/external-tools/plagiarism-detection-platform/file.jwt_access_tokens) **with this API).**

Sandboxes are how Canvas creates a new environment based on a template. As part of creating the new sandbox, all UUIDs are remapped to new values. To avoid confusion with the original template. This API allows you to download the UUID mapping for a given sandbox.

`GET /api/lti/uuid_map`

**Scope:** `url:GET|/api/lti/uuid_map`

This endpoint returns a CSV file with the UUID mapping for the sandbox. The CSV has three columns:

```
* `type` - The object type
* `original_uuid` - The UUID of an object from the template
* `new_uuid` - The UUID of the corresponding object in the sandbox
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).