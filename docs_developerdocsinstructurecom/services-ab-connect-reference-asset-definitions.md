---
title: Asset Definitions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/asset-definitions
source: sitemap
fetched_at: 2026-02-15T09:03:43.606168-03:00
rendered_js: false
word_count: 315
summary: This document outlines the Asset Definition API endpoint, detailing how to retrieve specific asset types or search for asset definitions using ODATA filters. It describes the required authentication parameters and optional query fields for interacting with the resource via HTTP GET requests.
tags:
    - api-reference
    - asset-definitions
    - odata-filtering
    - partner-authentication
    - http-get
    - asset-management
category: api
---

The Asset Definition endpoint provides direct access to the properties on Assets. Asset type is an attribute on an Asset.

The Asset Definitions resource can be used to access different asset types for setting up a browse and filter experience on the Asset resource. See the documentation on the [Asset endpoint](https://developerdocs.instructure.com/services/ab-connect/reference/assets) for details.

All calls against the Asset Definitions resource must be implemented as HTTP GET requests, and must include proper [Partner Authentication Credentials](https://developerdocs.instructure.com/services/ab-connect/introduction/authentication).

## Retrieving Asset Definitions

In its simplest form, you are able to retrieve the details of a specific Asset Definitions resource by appending the AB GUID to the path portion of the URL.

### Asset Definitions Fetching

guidstringRequired

guid of specified asset definition

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[asset\_definitions]stringOptional

comma separated list of field names

/asset\_definitions/{guid}

## Searching for Asset Definitions

Using filterings, it is possible to retrieve sets of Asset Definitions that match specific criteria. These Asset Definitions are returned in an array of Asset Definitions objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters).

### Finding Sets of Assets Definitions

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[asset\_definitions]stringOptional

comma separated list of field names

filter\[asset\_definitions]stringOptional

an ODATA-like query string used to filter

sort\[asset\_definitions]stringOptional

a comma separated list of property names specifying the sort order of the returned results

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).