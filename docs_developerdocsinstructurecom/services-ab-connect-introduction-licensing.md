---
title: Licensing Considerations | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/licensing
source: sitemap
fetched_at: 2026-02-15T09:03:45.450292-03:00
rendered_js: false
word_count: 155
summary: This document explains how licensing levels determine the breadth and depth of access to Academic Benchmarks data and services, including troubleshooting unauthorized access errors.
tags:
    - academic-benchmarks
    - licensing
    - api-access
    - authorization
    - error-handling
    - data-coverage
category: concept
---

Access to the Academic Benchmarks data and services is licensed by breadth of coverage (authority and subject area) as well as depth of metadata and functionality. If you attempt to access a feature or piece of data and receive a 401 error, check your credentials and the details of the error message body. It may be that your current license does not support the call you are making. In some instances, you'll get a valid response, but the data related to one of these features will simply not be included in the response. E.g. if you are licensed for Standards, but not Topics, when you retrieve a Standard the `topics` relationship will not exist.

To clarify or discuss your licensing, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) at Instructure or your sales representative.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).