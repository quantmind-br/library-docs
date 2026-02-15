---
title: Paging Data | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/paging
source: sitemap
fetched_at: 2026-02-15T09:04:07.8951-03:00
rendered_js: false
word_count: 480
summary: This document explains how to manage large data sets in the AB Connect v4.1 API using pagination parameters like limit and offset to control response sizes.
tags:
    - ab-connect
    - api-pagination
    - rest-api
    - limit-parameter
    - offset-parameter
    - json-response
category: guide
---

All AB Connect v4.1 endpoints deal with lists of data. Unless you are requesting a single element using its GUID (or ID), the response will contain a list - even if there is just a single element in the list. For efficiency reasons, AB Connect breaks the list up into pages. The default page size is 10 elements except for the Clarifier which returns 5 Concepts and 5 Standards by default. The `limit` and `offset` arguments help your application manage the list of data by setting the page size and enabling the application to walk through the pages of the list. This way, you can strike the proper balance between efficiency and performance.

Note that in order to maintain server stability, page sizes are capped at 100 objects per page to prevent resource depletion on the server.

This section illustrates the general use of limit and offset but doesn't go into the details of any given particular endpoint.

As mentioned above, AB Connect limits the size of a response to 10 elements by default. This limit only applies to the primary list of elements for the endpoint. E.g. the Standards endpoint will break the Standards list into pages. However, if you request the Standards endpoint to include related Concepts, all Concepts related to each Standard will be returned in the single call regardless of length of the Concepts list.

When responding with a list, AB Connect supplies paging URLs in the links section of the response can use the `next` and `previous` links to walk the response list.

```
    {
        "links": {
            "last": "https://api.abconnect.instructure.com/rest/v4.1/<object>?offset=248960",
            "next": "https://api.abconnect.instructure.com/rest/v4.1/<object>?offset=10",
            "self": "https://api.abconnect.instructure.com/rest/v4.1/<object>"
        }
    }
```

The first page of data includes `next` and `last` links. The `next` link supplies the URL to retrieve the next set of data based on your current page size (which is specified by the `limit` argument and defaults to 10). Note the use of the `offset` argument above to support the paging. Offset indicates how far into the list you'd like AB Connect to dive when responding to the request.

One of the middle pages of data should include not just `next` and `last` but also `first` and `previous` links to support bidirectional paging.

```
    {
        "links": {
            "last": "https://api.abconnect.instructure.com/rest/v4.1/<object>?offset=248960",
            "next": "https://api.abconnect.instructure.com/rest/v4.1/<object>?offset=20",
            "first": "https://api.abconnect.instructure.com/rest/v4.1/<object>",
            "self": "https://api.abconnect.instructure.com/rest/v4.1/<object>?offset=10",
            "prev": "https://api.abconnect.instructure.com/rest/v4.1/<object>"
        }
    }
```

If you'd like to make the page responses larger or smaller, you can use the limit parameter. E.g.

```
`https://api.abconnect.instructure.com/rest/v4.1/<object>?...&limit=25`
```

In which case, the number of elements from the list that you receive for each request changes. This is also reflected in the links you get in response in order to enable the system to properly track page size as you navigate the list.

```
    {
        "links": {
            "last": "https://api.abconnect.instructure.com/rest/v4.1/<object>?limit=25&offset=248950",
            "next": "https://api.abconnect.instructure.com/rest/v4.1/<object>?limit=25&offset=25",
            "self": "https://api.abconnect.instructure.com/rest/v4.1/<object>?limit=25"
        }
    }
```

Between these two parameters, you should be able to control how your system receives responses and tune it for optimum performance.

When would you ever want your response to contain 0 elements? In addition to the object data contained in the response, most endpoints can return data in the `meta` object (like facets). If you want to explore the meta object without inducing the overhead of processing data elements in the list, set the `limit` to 0. E.g.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?limit=0&facet_summary=*`
```

Will return something similar to the following:

```
    {
        "links": {
            "self": "https://api.abconnect.instructure.com/rest/v4.1/standards?limit=0"
        },
        "data": [ ],
        "meta": {
            "offset": 0,
            "limit": 0,
            "took": 232,
            "count": 248969,
            "facets": [
                {
                    "facet": "document.publication.authorities",
                    "count": 54
                    ...
                },
                ...
            ]
        },
    ...
    }
```

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).