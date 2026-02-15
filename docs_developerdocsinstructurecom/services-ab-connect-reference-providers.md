---
title: Providers | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/providers
source: sitemap
fetched_at: 2026-02-15T09:15:33.79016-03:00
rendered_js: false
word_count: 486
summary: This document describes the Providers resource, explaining how to retrieve and filter information about provider accounts and their asset-sharing relationships within the API.
tags:
    - providers-resource
    - api-documentation
    - asset-sharing
    - odata-filtering
    - identity-management
category: api
---

The Providers resource can be used to retrieve information about your Provider account as well as Providers that have shared all or some of their Assets with your organization and Providers with whom you have shared Assets. You can list all of the Providers related to you, filter the list of related Providers or lookup a specific Provider. The response contains the name of the related Provider as well as the Provider's unique GUID and a list of AB taxonomies they have licensed. In the special circumstance where your own Provider object shows up in the response, you will also see relationships listing Providers that are sharing Assets with you (Owners) as well as Providers with whom you are sharing assets (Consumers).

To locate your own Provider object, user the filter parameter and request Providers with ID `_me`. That is a special constant that matches yourself. While not terribly helpful with the Providers endpoint, you can also use `_all` as a match on Provider fields to indicate that you want to match on all Providers. This can be used with the `owner.id` property on the Assets resource where the default behavior is to only list Assets owned by you.

In its simplest form, you are able to retrieve the details of a specific Provider by appending the AB GUID to the path portion of the URL.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[providers]stringOptional

comma separated list of field names

includestringOptional

A comma separated list of resource names that will be returned in the response.

Using filtering and facets, it is possible to retrieve sets of Providers that match specific criteria. These Providers are returned in an array of Provider objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters) and the use of [facets](https://developerdocs.instructure.com/services/ab-connect/introduction/facets). This section covers the specifics of using these parameters with the Providers resource. Note that by default, the endpoint returns your Provider object and the objects of all Providers related to you.

### Finding Sets of Providers

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[providers]stringOptional

comma separated list of field names

filter\[providers]stringOptional

an ODATA-like query string used to filter

sort\[providers]stringOptional

a comma separated list of property names specifying the sort order of the returned results

includestringOptional

A comma separated list of resource names that will be returned in the response.

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).