---
title: Standards | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/standards
source: sitemap
fetched_at: 2026-02-15T09:04:01.378868-03:00
rendered_js: false
word_count: 612
summary: Explains how to use the Standards resource API to access academic standards, manage entity relationships, and perform data retrieval using filters and facets.
tags:
    - ab-connect
    - academic-standards
    - api-reference
    - json-api
    - odata-filtering
    - resource-relationships
category: api
---

The Standards resource can be used to access academic Standards and related metadata. The API provides a simple integration point, eliminates the need to manage Standards data in your organization and system, and provides the foundation for additional connected metadata. Use of the API ensures the most current Standards data is available to your application.

One of the greatest benefits of AB Connect is the ability to navigate relationships between Standards, other Standards and Topics. Retrieving the related Standards and Topics is done in a similar fashion as attributes, but they are contained in the JSON API relationships response. Note that due to the JSON API standard, only the type and ID are returned in the relationship data. Keep in mind that the JSON API ID is the same as the AB GUID for these entities. If you'd like to retrieve the data of the related resources, use the `include` parameter.

Standards can also be related to Assets. Note that if a Standard is related to an Asset, Topics related to that same Standard automatically become related to Asset as "predicted" relationships when you are licensed for the Academic Benchmarks Topic Taxonomy. Note that this implied relationship is bidirectional, so relating a Topic to an Asset directly also generates predicted Standards relationships. Relationships between Standards and Assets are managed through the Asset endpoint. See the documentation on the [Asset endpoint](https://developerdocs.instructure.com/services/ab-connect/reference/assets) for details.

All calls against the Standards resource must be implemented as HTTP GET requests, and must include proper [Partner Authentication Credentials](https://developerdocs.instructure.com/services/ab-connect/introduction/authentication).

In its simplest form, you are able to retrieve the details of a specific Standard by appending the AB GUID to the path portion of the URL.

guidstringRequired

guid of specified standard

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standards]stringOptional

comma separated list of field names

includestringOptional

A comma separated list of resource names that will be returned in the response. Standards have relationships with other resources (e.g. other Standards, Topics and Concepts). By default, those related resources are returned as references to other endpoints and only their IDs are included in the response. If you list the related resources by their relationship name in the include statement, the properties of the related resources are included as well.

Using filtering and facets, it is possible to retrieve sets of Standards that match specific criteria. These Standards are returned in an array of Standard objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters) and the use of [facets](https://developerdocs.instructure.com/services/ab-connect/introduction/facets). This section covers the specifics of using these parameters with the Standards resource.

### Finding Sets of Standards

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standards]stringOptional

comma separated list of field names

filter\[standards]stringOptional

an ODATA-like query string used to filter

sort\[standards]stringOptional

a comma separated list of property names specifying the sort order of the returned results

facetstringOptional

A comma separated list of facet names that you are requesting the options on.

facet\_summarystringOptional

A comma separated list of facet names for which you are requesting summary information.

includestringOptional

A comma separated list of resource names that will be returned in the response.

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).