---
title: Error Responses | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/error-responses
source: sitemap
fetched_at: 2026-02-15T09:03:44.23241-03:00
rendered_js: false
word_count: 75
summary: This document describes the standard structure and schema of HTTP 4XX error responses returned by the API to assist with troubleshooting and corrective actions.
tags:
    - error-handling
    - api-responses
    - http-status-codes
    - json-pointer
    - error-schema
category: reference
---

Errors are returned as HTTP codes in the 4XX range. All errors are accompanied by a JSON response that provides the details of the error so corrective action can be taken.

```
    {
      "errors": [
        {
          "source": {
            "pointer": "a JSON Pointer RFC6901 to the associated entity in the request document E.g. \"/data\" for a primary data object, or \"/data/attributes/title\" for a specific attribute.",
            "parameter": "a string indicating which URI query parameter caused the error."
          },
          "detail": "<long error message>",
          "status": "<error code - same as HTTP status code>",
          "title": "<brief error message - typically same as the HTTP status title>"
        },
        ...
      ]
    }
```

See the documentation for the individual endpoint for the specifics of the errors that apply to that endpoint.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).