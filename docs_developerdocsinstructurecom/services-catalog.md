---
title: Catalog | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog
source: sitemap
fetched_at: 2026-02-15T09:14:28.061208-03:00
rendered_js: false
word_count: 362
summary: This document provides technical instructions for authenticating and interacting with the Catalog API, including details on security requirements, pagination via RFC5988, and specific file upload formats.
tags:
    - catalog-api
    - authentication
    - pagination
    - api-security
    - rfc5988
    - request-headers
category: api
---

So, you want to develop some tooling around the Catalog API - perhaps some custom reports? Great! This API gives you everything that Catalog has to offer.

Visit Catalog Admin API page to create an API key. Once you've received your key, **treat it like a password**.

Use SSL for all requests to the API. Non-SSL requests will result in redirects, and your API key will be sent in the clear.

To authenticate, send the API key as a request header. Here's an example using cURL:

```
curl https://[URL]/api/v1/products -H 'Authorization: Token token="my-api-key"'
```

All index endpoints support pagination. Specifically, we implement [RFC5988arrow-up-right](http://tools.ietf.org/html/rfc5988).

You can use `?page=` to set the page of data you want to retrieve. If no items exist for that page, the response will be a root key with an empty array.

```
curl https://[URL]/api/v1/courses?page=2
{
  "courses": []
}
```

To change the number of items returned for each page, you can use `?per_page=`. This defaults to 20 and has a max of 100.

```
curl https://[URL]/api/v1/courses?per_page=40&page=2
```

Information about pagination is provided in the Link header. Here is an example of what the header could look like

```
curl -I https://[URL]/api/v1/courses?page=3
Link: <https://[URL]/api/v1/courses?page=4>; rel="next",  
      <https://[URL]/api/v1/courses?page=15>; rel="last",
      <https://[URL]/api/v1/courses?page=1>; rel="first",
      <https://[URL]/api/v1/courses?page=2>; rel="prev"
```

Let's talk about what each link means. `rel="next"` lets us know that the next page of data is `page=4`. This make sense given that we requested page 3. `rel="prev"` lets us know that the page previous to the one we requested is `page=2`. `rel="next"` indicates the next page of data to request. `rel="last"` tells us the last and total number of pages of data that currently exist.

Not all `rel=` links will exist on every response. For instance, the response for the first page of data will not have `rel="first"` or `rel="prev"`. The same is true for the last page of data. This means that you can programmatically traverse all pages of data by requesting the first page and continuing to request the `rel="next"` until the response does not contain a `rel="next"`.

It's important to note that altering the `per_page=` will change the total number of pages.

If you are uploading a product image in SVG format. You will need to specify the file type.

```
curl https://[URL]/api/v1/products -F "course[listing_image]=@somefile.svg;type=image/svg+xml"'
```

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).