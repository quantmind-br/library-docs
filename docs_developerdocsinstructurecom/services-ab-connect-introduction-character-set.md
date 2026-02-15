---
title: Character Set Support | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/character-set
source: sitemap
fetched_at: 2026-02-15T09:03:53.011478-03:00
rendered_js: false
word_count: 315
summary: This document explains the licensing constraints for accessing Academic Benchmarks data and provides technical specifications for supported character sets and HTTP headers.
tags:
    - academic-benchmarks
    - ab-connect
    - licensing
    - character-encoding
    - utf-8
    - http-headers
    - error-handling
category: guide
---

Access to the Academic Benchmarks data and services is licensed by breadth of coverage (authority and subject area) as well as depth of metadata and functionality. If you attempt to access a feature or piece of data and receive a 401 error, check your credentials and the details of the error message body. It may be that your current license does not support the call you are making. In some instances, you'll get a valid response, but the data related to one of these features will simply not be included in the response. E.g. if you are licensed for Standards, but not Topics, when you retrieve a Standard the `topics` relationship will not exist.

To clarify or discuss your licensing, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) at Instructure or your sales representative.

UTF-8 is the recommended character set for transmitting data using AB Connect - AB Connect stores data in UTF-8 and it is the most common character set on the web. However, as adoption for Unicode and UTF-8 has evolved over the life of Academic Benchmarks, we've built support for a few other character sets to support legacy situations. AB Connect supports RESPONSES in UTF-8, latin1, ISO-8859-1 or Windows-1252 character sets.

**Note that at this time AB Connect does not support REQUESTS in any character set other than UTF-8.**

To request a specific character set response, include the `Accept-Charset` HTTP header in your request and supply one of the supported values:

In the case that utf-8 is desired, there is no need to actually include the `Accept-Charset` header as utf-8 is the default.

The AB Connect response includes a `Content-Type` header indicating the data type (application/json) as well as the character set of the response. E.g.

```
`Content-Type: application/json; charset=utf-8`
```

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).