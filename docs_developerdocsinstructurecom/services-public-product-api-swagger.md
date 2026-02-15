---
title: Public Product Endpoints | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/public-product-api/swagger
source: sitemap
fetched_at: 2026-02-15T09:11:11.936697-03:00
rendered_js: false
word_count: 310
summary: This document specifies API endpoints for retrieving product listings, accessing individual product details, and submitting user lead information for follow-up inquiries.
tags:
    - api-reference
    - product-retrieval
    - data-filtering
    - pagination
    - lead-generation
    - authentication
category: api
---

### Retrieve a collection of Products via get

AuthorizationstringRequired

Enter JWT Bearer token in the format: Bearer {your-token}

pageinteger · min: 1 · nullableOptional

Page of the index to retrieve

Example: `1`

per\_pageinteger · min: 1 · max: 100 · nullableOptional

Number of Products per page to retrieve for the index

Example: `20`

search\_termsstring\[] · nullableOptional

Array of search terms for filtering the Products to retrieve in the index

Example: `test`

tag\_filtersstring\[] · nullableOptional

Array of tags to filter the Products to retrieve in the index

Example: `LTI11`

200

get success: Product Collection

### Retrieve a collection of Products via post

AuthorizationstringRequired

Enter JWT Bearer token in the format: Bearer {your-token}

pageinteger · min: 1 · nullableOptional

Page of the index to retrieve

Example: `1`

per\_pageinteger · min: 1 · max: 100 · nullableOptional

Number of Products per page to retrieve for the index

Example: `20`

search\_termsstring\[] · nullableOptional

Array of search terms for filtering the Products to retrieve in the index

Example: `test`

tag\_filtersstring\[] · nullableOptional

Array of tags to filter the Products to retrieve in the index

Example: `LTI11`

200

post success: Product Collection

### Returns details for a Product

AuthorizationstringRequired

Enter JWT Bearer token in the format: Bearer {your-token}

idinteger · min: 1Required

ID of the Product to retrieve

Example: `1`

/api/public/v1/products/{id}

### Save details of user for learn more

countrystringRequiredExample: `US`

statestringRequiredExample: `AR`

organizationstringRequiredExample: `Lawrence Public School District`

current\_canvas\_companyboolean · nullableOptionalExample: `true`

gradestring · enum · nullableOptionalExample: `K12`Possible values:

namestringRequiredExample: `Anne Example`

rolestringRequiredExample: `C&I Director`

emailstring · emailRequiredExample: `anne.example@lpsd.edu`

notesstring · nullableOptionalExample: `Please detail any specific information you would like to learn from this partner.`

tool\_idintegerRequiredExample: `123`

201

post success: User details saved when state is empty

422

Not accepting leads: Unprocessable Entity

/api/public/v1/learn\_more

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).