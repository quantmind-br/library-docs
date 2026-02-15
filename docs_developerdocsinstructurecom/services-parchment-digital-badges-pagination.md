---
title: Pagination | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/parchment-digital-badges/pagination
source: sitemap
fetched_at: 2026-02-15T08:59:18.412019-03:00
rendered_js: false
word_count: 178
summary: This document explains how to handle paginated API responses using the HTTP link header to navigate through multiple pages of results.
tags:
    - pagination
    - api-response
    - link-header
    - http-headers
    - resource-navigation
category: guide
---

When a response is paginated, the response headers will include a link header. If the endpoint does not support pagination, or if all results fit on a single page, the link header will be omitted.

The link header contains URLs that you can use to fetch additional pages of results. For example, the previous and next page of results.

If the response is paginated, the link header will look something like this:

```
link: <https://{BADGES_DOMAIN}/v2/issuers/ENTITY_ID/assertions?num=2&before=CURSOR>; rel="prev",
<https://{BADGES_DOMAIN}/v2/issuers/ENTITY_ID/assertions?num=10&after=CURSOR>; rel="next"
```

The link header provides the URL for the previous and next page of results:

The URL for the previous page is followed by rel="prev". The URL for the next page is followed by rel="next". In some cases, only a subset of these links are available. For example, the link to the previous page won't be included if you are on the first page of results.

You can use the URLs from the link header to request another page of results.

Last updated 3 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).