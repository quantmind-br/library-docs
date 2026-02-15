---
title: Certificates | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/catalog/openapi/certificates
source: sitemap
fetched_at: 2026-02-15T09:10:40.562896-03:00
rendered_js: false
word_count: 130
summary: This document details the API endpoints and authentication procedures for managing listing certificates, including retrieval and revocation processes.
tags:
    - api-reference
    - certificate-management
    - token-authentication
    - endpoint-documentation
    - user-authorization
category: api
---

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

listing\_idintegerRequired

200

Getting a listing certificate

200

Getting a listing certificate

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

days\_to\_expirestringOptional

Days until the certificate expires after it is awarded. Defaults to null. Must not be present when expires\_at is present.

expires\_atstringOptional

Date of certificate expiration. Defaults to null. Must not be present when days\_to\_expire is present.

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

nullify\_requirements\_completed\_atstringOptional

Should nullify the requirements\_completed\_at for the enrollments, defaults to false

AuthorizationstringRequired

API Token based authentication. Use format: Token token="your-api-key"

200

Revoking users certificate

/api/v1/certificates/revoke\_users\_certificate

200

Revoking users certificate

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).