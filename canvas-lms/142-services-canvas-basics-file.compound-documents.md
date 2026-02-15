---
title: Compound Documents | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/basics/file.compound_documents
source: sitemap
fetched_at: 2026-02-15T09:13:03.182932-03:00
rendered_js: false
word_count: 252
summary: This document defines the structure of compound documents, which allow for side-loading related data collections to reduce redundancy in JSON responses.
tags:
    - compound-documents
    - side-loading
    - json-structure
    - api-design
    - canvas-lms
category: concept
---

Compound documents contain multiple collections to allow for side-loading of related objects. Side-loading is desirable when nested representation of related objects would result in potentially expensive repetition. For example, given a list of 50 comments by only 3 authors, a nested representation would include 50 author objects where a side-loaded representation would contain only 3 author objects.

A compound document is a JSON object with two reserved properties ("meta" and "links"). The "meta" property is required and is described below; the "links" property is currently unused but reserved. All other properties of the compound document's root object should be interpreted as collections of model objects. A compound document will always contain at least one collection.

The "meta" property is a JSON object with one recognized property ("primaryCollection"). If present, the "meta.primaryCollection" property will contain the property name of one of the collections in the compound document. The primary collection contains the data most directly associated with the request. Any pagination indicated through a Link header accompanying a compound document applies to the primary collection.

Any remaining collections in a compound document are secondary collections and will contain objects related (perhaps indirectly, through other secondary objects) to those in the primary collection. Secondary collections should never be considered as ordered or complete.

Example:

```
{
"meta":{"primaryCollection":"comments"},
"comments":[...],
"authors":[...]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).