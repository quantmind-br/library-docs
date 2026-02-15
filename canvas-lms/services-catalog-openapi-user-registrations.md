---
title: User Registrations | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/user_registrations
source: sitemap
fetched_at: 2026-02-15T09:10:33.093491-03:00
rendered_js: false
word_count: 134
summary: This document provides technical specifications for the User Registrations API, detailing endpoints for retrieving individual records, listing multiple entries with time-based filters, and creating new registrations.
tags:
    - api-reference
    - user-registrations
    - authentication
    - rest-api
    - registration-management
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Getting a specific user registration

/api/v1/user\_registrations/{id}

200

Getting a specific user registration

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

fromstringOptional

Earliest date/time to return (optional, String). Suggested format YYYY-MM-DDTHH:MM:SSZ, e.g. 2018-01-01T00:00:00Z. System time zone is UTC.

tostringOptional

Latest date/time to return (optional, String). See 'from' above for format.

200

Listing user registrations

/api/v1/user\_registrations

200

Listing user registrations

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

emailstringOptional

E-mail address (will also serve as login)

catalog\_idstringOptional

ID of subcatalog to associate with user (optional)

custom\_fieldsstringOptional

Hash of custom field values, e.g. { 'phone': '867-5309' } (optional)

/api/v1/user\_registrations

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).