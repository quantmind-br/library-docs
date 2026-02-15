---
title: Users | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/users
source: sitemap
fetched_at: 2026-02-15T09:14:24.710833-03:00
rendered_js: false
word_count: 326
summary: This document outlines API endpoint specifications for managing user accounts, including authentication protocols, parameter definitions for user creation, and options for filtering or deleting user records.
tags:
    - api-reference
    - user-management
    - authentication
    - canvas-lms
    - catalog-api
    - endpoint-documentation
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

clear\_merged\_into\_user\_idstringOptional

It will clear merged\_into\_user\_id field of user if set to true

custom\_fieldsstringOptional

An object containing custom field values, e.g. { "phone": "867-5309" }. Custom field values must be strings or nulls, anything else will result in a 400 response. If Catalog already has a value for a given key, it will be overwritten, or if the new value is null, it will be deleted. If Catalog does not already have a value for a given key, it will be added. UDFs that are not included in the request will remain unchanged.

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

only\_orders\_and\_enrollmentsstringOptional

Delete only orders and enrollments (user dependencies) except user and related account admins OR delete user dependencies including user and related account admins

200

Deleting a specific user with dependencies

200

Deleting a specific user with dependencies

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

registered\_in\_catalogbooleanOptional

If true, only queries users registered through Catalog. If false, only queries users registered through Canvas. If not specified, queries all users.

canvas\_user\_idintegerOptional

created\_at\_fromstringOptional

Created at from. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

created\_at\_tostringOptional

Created at to. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

updated\_at\_fromstringOptional

Updated at from. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

updated\_at\_tostringOptional

Updated at to. Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

email\_addressstringRequired

E-mail address (will also serve as login)

registered\_account\_idstringOptional

ID of subcatalog to associate with user (optional). If not specified, the root account ID used to generate the API key will be registered\_account\_id

custom\_fieldsstringOptional

Hash of custom field values, e.g. { "phone": "867-5309" } (optional)

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).