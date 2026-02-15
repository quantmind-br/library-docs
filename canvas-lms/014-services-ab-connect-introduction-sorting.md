---
title: Sorting | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/sorting
source: sitemap
fetched_at: 2026-02-15T09:04:16.862141-03:00
rendered_js: false
word_count: 158
summary: This document explains how to use the sort argument in API query strings to order list results, including syntax for multiple criteria and handling different data types.
tags:
    - api-sorting
    - query-parameters
    - list-results
    - data-types
    - custom-attributes
    - sort-order
category: guide
---

By default, list results are returned in order of decreasing relevance. However, you can specify a sort field using the `sort` argument in the URL query string. The format of the requests is:

```
`sort[object of sort]=<property name>`
```

E.g.

```
`sort[standards]=number.enhanced`
```

You can specify multiple criteria to ensure that items that may have duplicate values in one property have a secondary sort to guarantee order. E.g.

```
`sort[standards]=number.enhanced,statement.descr`
```

The default behavior is to sort in ascending order by the specified property. However, if you'd like descending order, prepend the property name with a hyphen/minus (U+002D) "-". E.g.

```
`sort[standards]=-number.enhanced`
```

- Custom attributes can be defined as text or numbers. If you aren't sure of the types for your custom attributes, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) for guidance.
- It is possible to create custom attributes with the same name and different data types in different asset types (or when searching across multiple owners). If you sort on custom attributes of different types, ascending sorts put number attribute values above text attribute values. Descending sorts reverse the order. Note that within a given type, numbers are sorted numerically and text attributes are sorted alphabetically.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).