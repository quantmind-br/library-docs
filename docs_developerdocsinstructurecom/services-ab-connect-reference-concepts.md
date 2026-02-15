---
title: Concepts | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/concepts
source: sitemap
fetched_at: 2026-02-15T09:04:20.378321-03:00
rendered_js: false
word_count: 626
summary: This document describes the Academic Benchmarks Concepts resource, a granular controlled vocabulary used to establish relationships between educational standards and content assets via the AB Connect API. It provides technical specifications for retrieving specific concept metadata and performing filtered searches.
tags:
    - academic-benchmarks
    - ab-connect
    - concepts-api
    - metadata-enrichment
    - standards-alignment
    - api-reference
category: api
---

Academic Benchmarks includes a controlled vocabulary of Concepts that has been used for over 15 years to aid in building relationships between content or assessment items (together referred to as Assets) and Standards. AB Connect Content Enrichment tools (Clarifier and prediction engine) are built on top of the Concepts. Each Concept represents a unique notion that a Standard or Asset covers. Academic Benchmarks unpacks Standards into groups of Concepts called `key_ideas` which can be retrieved via the Standards endpoint. Similarly, Assets can be related to Concepts which can act as an intermediary between Assets and Standards.

Topics are a similar intermediary controlled vocabulary but while Topics are comparatively broad or higher level than Standards, Concepts are very granular and operate at the unpacked Standard level.

The Concepts resource can be used to access the Academic Benchmarks Concepts and related metadata. Use of the API ensures the most current Concepts data is available to your application. At this point in time, the Concepts endpoint is relatively simple as the expectation is that partners will use Standards or Topics as a starting point for building an Asset's metadata profile and then refine it using the Clarifier. However, this endpoint does allow the caller to retrieve `context` of the Concept which can clarify ambiguous terms.

The relationship between Concepts and other objects are tracked and reported via the other objects. For example, to understand what Concepts a Standard encompasses, retrieve the `concepts` list via the Standard endpoint (or see the `key_ideas` field). Similarly, the Asset endpoint can be used to associate Assets with Concepts and retrieve the current relationship. See also the Clarifier endpoint to further explore potential relationships between Concepts, Standards and Assets.

All calls against the Concepts resource must be implemented as HTTP GET requests, and must include proper [Partner Authentication Credentials](https://developerdocs.instructure.com/services/ab-connect/introduction/authentication).

Note that access to AB Concepts is licensed separately. If your credentials are correct and you are still receiving a 401 error (or no results), check with [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) to ensure you are licensed for Concepts. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to Key Ideas and Concepts.

In its simplest form, you are able to retrieve the details of a specific Concept by appending the AB GUID to the path portion of the URL.

guidstringRequired

guid of specified concept

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[concepts]stringOptional

comma separated list of field names

Using filtering and facets, it is possible to retrieve sets of Concepts that match specific criteria. These Concepts are returned in an array of Concept objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters) and the use of [facets](https://developerdocs.instructure.com/services/ab-connect/introduction/facets). This section covers the specifics of using these parameters with the Concepts resource.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[concepts]stringOptional

comma separated list of field names

filter\[concepts]stringOptional

an ODATA-like query string used to filter

sort\[concepts]stringOptional

a comma separated list of property names specifying the sort order of the returned results

facetstringOptional

A comma separated list of facet names that you are requesting the options on.

facet\_summarystringOptional

A comma separated list of facet names for which you are requesting summary information.

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).