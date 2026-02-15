---
title: Topics | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/topics
source: sitemap
fetched_at: 2026-02-15T09:04:34.500456-03:00
rendered_js: false
word_count: 577
summary: This document outlines the usage of the Academic Benchmarks Topics resource API for accessing topic taxonomies and managing relationships between topics, standards, and assets. It details authentication requirements, hierarchical navigation, and supported query parameters for filtering and facets.
tags:
    - academic-benchmarks
    - topic-taxonomy
    - api-resource
    - metadata-retrieval
    - ab-connect
    - odata-filtering
category: api
---

The Topics resource can be used to access the Academic Benchmarks Topic Taxonomy and related metadata. The API provides a simple integration point, eliminates the need to maintain a copy of the taxonomy locally and provides the foundation for additional connected metadata. Use of the API ensures the most current taxonomy is available to your application.

One of the benefits of AB Connect is the ability to navigate relationships between Topics and Standards. Topics can also be related to other Topics by the nature of their position in the hierarchy of the Topic Taxonomy (parent/child). Retrieving related Standards and Topics is done in a similar fashion as attributes, but they are contained in the JSON API relationships response. Note that due to the JSON API standard, only the type and ID are returned in the relationship data. Keep in mind that the JSON API ID is the same as the AB GUID for these entities. If you'd like to retrieve the data of the related Standards or Topics, use the `include` parameter.

Topics can also be related to Assets. Note that if a Topic is related to an Asset, Standards related to that same Topic automatically become related to the Asset as "predicted" (and vice versa). Relationships between Topics and Assets are managed through the Asset endpoint. See the documentation on the [Asset endpoint](https://developerdocs.instructure.com/services/ab-connect/reference/assets) for details.

All calls against the Topics resource must be implemented as HTTP GET requests, and must include proper [Partner Authentication Credentials](https://developerdocs.instructure.com/services/ab-connect/introduction/authentication).

Note that the Academic Benchmarks Topic Taxonomy is licensed separately. If your credentials are correct and you are still receiving a 401 error (or no results), check with [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) to ensure you are licensed for Topics.

In its simplest form, you are able to retrieve the details of a specific Topic by appending the AB GUID to the path portion of the URL.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[topics]stringOptional

comma separated list of field names

includestringOptional

A comma separated list of resource names that will be returned in the response.

Using filtering and facets, it is possible to retrieve sets of Topics that match specific criteria. These Topics are returned in an array of Topics objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters) and the use of [facets](https://developerdocs.instructure.com/services/ab-connect/introduction/facets). This section covers the specifics of using these parameters with the Topics resource.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[topics]stringOptional

comma separated list of field names

filter\[topics]stringOptional

an ODATA-like query string used to filter

sort\[topics]stringOptional

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