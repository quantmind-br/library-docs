---
title: API Endpoint Attributes | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/basics/file.endpoint_attributes
source: sitemap
fetched_at: 2026-02-15T09:13:09.088743-03:00
rendered_js: false
word_count: 145
summary: This document explains how the Canvas LMS API enriches HTML snippets with custom data attributes to help developers identify resource endpoints and return types.
tags:
    - canvas-lms
    - api-metadata
    - html-attributes
    - resource-linking
    - data-api-endpoint
category: reference
---

Canvas adds attributes to links in returned HTML snippets to make it easier for API consumers to digest the referenced resources. These attributes are as follows:

- `data-api-endpoint` - A URL where the linked object can be accessed via the API
- `data-api-returntype` - The type of data returned

For example, consider an assignment description containing a link to a wiki page in the same course. The description returned by the Get Assignment API might look like this:

```
<ahref="http://canvas.example.com/courses/123/pages/a-wiki-page"
data-api-endpoint="http://canvas.example.com/api/v1/courses/123/pages/a-wiki-page"
data-api-returntype="Page">More information here</a>
```

The currently supported `data-api-returntype` values are:

If the API returns a list of objects instead of a single object, the `data-api-returntype` will be wrapped in square brackets, e.g. `[Assignment]`.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).