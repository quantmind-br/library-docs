---
title: Analytics | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/analytics
source: sitemap
fetched_at: 2026-02-15T09:10:37.028309-03:00
rendered_js: false
word_count: 254
summary: This document specifies the authentication requirements and request parameters for several analytics API endpoints covering products, enrollments, and student data.
tags:
    - api-reference
    - analytics
    - canvas-lms
    - enrollment-data
    - product-tracking
    - rest-api
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

product\_idsinteger\[]Optional

product\_statusesstring\[]Optional

List of product statuses (OPEN, CLOSED, and/or DELETED)

creation\_date\_fromstringOptional

creation\_date\_tostringOptional

enrollment\_count\_minintegerOptional

enrollment\_count\_maxintegerOptional

completion\_count\_minintegerOptional

completion\_count\_maxintegerOptional

dropped\_count\_minintegerOptional

dropped\_count\_maxintegerOptional

listing\_price\_minnumberOptional

listing\_price\_maxnumberOptional

promo\_codesstring\[]Optional

List of promotion code states (APPLIED and/or NOT\_APPLIED)

revenue\_minnumberOptional

revenue\_maxnumberOptional

certificate\_offeredbooleanOptional

Certificate offered for the product

200

Getting products analytics

/api/v1/analytics/products

200

Getting products analytics

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

product\_idsinteger\[]Optional

product\_statusesstring\[]Optional

List of product statuses (OPEN, CLOSED, and/or DELETED)

student\_idsinteger\[]Optional

List of student ids(catalog user id)

student\_canvas\_user\_idsinteger\[]Optional

List of student ids(canvas user id)

enrollment\_date\_fromstringOptional

enrollment\_date\_tostringOptional

enrollment\_statusesstring\[]Optional

List of enrollment statuses (ACTIVE, COMPLETED, DROPPED and/or CONCLUDED)

completion\_date\_fromstringOptional

completion\_date\_tostringOptional

200

Getting enrollments analytics

/api/v1/analytics/enrollments

200

Getting enrollments analytics

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

product\_idsinteger\[]Optional

product\_statusesstring\[]Optional

List of product statuses (OPEN, CLOSED, and/or DELETED)

student\_idsinteger\[]Optional

List of student ids(catalog user id)

student\_canvas\_user\_idsinteger\[]Optional

List of student ids(canvas user id)

purchaser\_idsinteger\[]Optional

List of purchaser ids(catalog user id)

purchaser\_canvas\_user\_idsinteger\[]Optional

List of purchaser ids(canvas user id)

bulk\_purchases\_onlybooleanOptional

purchase\_date\_fromstringOptional

purchase\_date\_tostringOptional

order\_feestring\[]Optional

List of order fee types (FREE and/or PAID)

listing\_price\_minnumberOptional

listing\_price\_maxnumberOptional

promo\_codesstring\[]Optional

List of promotion code states (APPLIED and/or NOT\_APPLIED)

revenue\_minnumberOptional

revenue\_maxnumberOptional

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

account\_idsinteger\[]Optional

student\_idsinteger\[]Optional

List of student ids(catalog user id)

student\_canvas\_user\_idsinteger\[]Optional

List of student ids(canvas user id)

enrollment\_count\_minintegerOptional

enrollment\_count\_maxintegerOptional

last\_enrollment\_date\_fromstringOptional

Last enrollment date from

last\_enrollment\_date\_tostringOptional

registration\_date\_fromstringOptional

registration\_date\_tostringOptional

registered\_throughstring\[]Optional

List of registration sources (CANVAS and/or CATALOG)

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).