---
title: Assets | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/assets
source: sitemap
fetched_at: 2026-02-15T09:04:28.333509-03:00
rendered_js: false
word_count: 1528
summary: This document explains how to manage Assets in AB Connect, detailing the API operations for creating, retrieving, updating, and deleting content metadata and custom attributes.
tags:
    - ab-connect
    - asset-management
    - api-reference
    - metadata
    - custom-attributes
    - crud-operations
category: api
---

Academic Benchmarks refers to partner content and assessment items as Assets. In AB Connect, an Asset is the metadata that describes the content - not the actual content itself. The Assets resource can be used to perform a host of operations on partner Assets to allow you to manage and relate your Assets. You can create, modify and delete Assets. You can also build a metadata profile for your Assets which allow you to take advantage of the power of the AB Connect prediction engine to establish and maintain relationships between your Asset, Standards and other Assets. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to Assets.

In addition to the attributes and relationships built into AB Connect to support Content Enrichment and predictions, AB Connect allows you to define your own attributes to support needs such as advanced searching. These customer defined attributes are referred to as descriptors or custom attributes. They can be configured per Asset type either by you (if you have web access enabled for your account) or by [AB Supportenvelope](mailto:absupport@instructure.com?subject=Setup%20custom%20properties).

Custom attributes are represented in the API in two ways: through the `descriptors` array or by direct named properties of the custom\_attributes object property. The name of the property is defined in the Asset setup screens. The `descriptors` array was the initial implementation and has been kept for backwards compatibility but the direct named attributes are easier to work with (particularly when filtering) and are the recommended approach. To illustrate the payload for custom attributes, if the Asset type has a property named "Color", it will be represented in the `descriptors` array as an anonymous name/value pair like:

```
    "descriptors": [
        {
            "name": "Color",
            "value": "blue"
        }
    ],
```

However, it will also be represented as a named attribute like:

```
    "custom_attributes": {
        "color": ["blue"]
    },
```

A couple of key points:

- When custom attributes are exchanged in JSON as named attributes, they are converted to lower case and any spaces or special characters are replaced by underscores. Multiple underscores in a row are collapsed into a single underscore. You won't need to think too much about this because the Asset type setup screen shows both the full property name and the JSON API attribute property name.
- It is the responsibility of the client application to control the values of the custom attributes, so if you have single-valued properties or controlled vocabularies in your use case, ensure they are handled properly before sending the data to AB Connect.
- The named attribute is an array. This is because custom attributes are multi-valued in AB Connect. In the `descriptors` array, this is represented by multiple anonymous objects with the same "name" and different "values". For example, if your Asset type is college logos, the University of Michigan Asset may have Color values of blue and yellow. The Color property would appear in the JSON as:

```
    "descriptors": [
        {
            "name": "Color",
            "value": "blue"
        },
        {
            "name": "Color",
            "value": "yellow"
        }
    ],
```

And:

```
    "custom_attributes": {
        "color": ["blue","yellow"]
    },
```

Finally, all calls against the Asset resource must be implemented as HTTP GET, POST, DELETE or PATCH requests, and must include proper [Partner Authentication Credentials](https://developerdocs.instructure.com/services/ab-connect/introduction/authentication).

To create an Asset within the AB Connects system, you send a POST to the endpoint. The body of the POST contains the Asset definition in JSON format. The only required fields are `client_id` and `asset_type`. You can define your `asset_type` using the Academic Benchmarks web interface or have support set it up for you. If you do not know your `asset_type` or need to have one setup for you, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) for details.

Note: The Asset endpoint allows you to manipulate basic attributes of the Asset. To manage relationships, see the section on [Managing and Predicting Relationships](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#managing-relationships-between-assets-and-standards%23creating-relationships).

{% swagger src="../openapi.yml" path="/assets" method="post" %} openapi.yml {% endswagger %}

To work with an Asset, you've created, call the endpoint with a GET while supplying the AB GUID for the Asset. If you have your organization's ID for the Asset but not the AB GUID, see the section on [finding Assets](https://developerdocs.instructure.com/services/ab-connect/reference/assets#searching-for-assets) and search on `client_id` to retrieve the AB GUID.

### Retrieving the Details of an Asset

{% swagger src="../openapi.yml" path="/assets/{guid}" method="get" %} openapi.yml {% endswagger %}

To work with an Asset you've created, call the endpoint while supplying the AB GUID for the Asset. If you have your organization's ID for the Asset but not the AB GUID, see the section on [finding Assets](https://developerdocs.instructure.com/services/ab-connect/reference/assets#searching-for-assets) and search on `client_id` to retrieve the AB GUID.

To update an Asset, PATCH the Asset URL (with GUID) sending JSON in the body similar to that in the create statement. The JSON body only needs to contain the attributes that need to be updated. You cannot update the `client_id` or `asset_type` once the Asset is created. If one of those needs to change, you will need to delete the old Asset and create a new one.

Notes on PATCHing Assets:

1. You do not need to include every field in a PATCH body. However, any field you include will replace the current value of that field on the Asset. For simple fields like `title`, that's not surprising. However, if you PATCH an object or array, you need to send the final state of that array or object - not just a single element. E.g. if the Asset has a `descriptor` with 5 name/value pairs on it and you send a PATCH to change 1 name/value pair, be sure to have copies of the other 4 name/value pairs in the `descriptor` array or the resulting Asset will only have one `descriptor` name/value pair.
2. If you are doing a bulk update of Assets where you are requesting a large number of Assets, paging through the list and PATCHing the Assets as you page, be sure to sort the list on a field you are not modifying - preferably on a unique fields like the GUID. If you leave the sort order to the default (relevance) or sort on a field you are changing, you will likely get duplicate and skipped Assets as you page through the list.

{% swagger src="../openapi.yml" path="/assets/{guid}" method="patch" %} openapi.yml {% endswagger %}

To delete an Asset you've created, call the endpoint while supplying the AB GUID for the Asset. If you have your organization's ID for the Asset but not the AB GUID, see the section on [finding Assets](https://developerdocs.instructure.com/services/ab-connect/reference/assets#searching-for-assets) and search on `client_id` to retrieve the AB GUID.

Assets can be deleted by sending a DELETE to their "self" URL.

{% swagger src="../openapi.yml" path="/assets" method="delete" %} openapi.yml {% endswagger %}

Using filtering it is possible to retrieve sets of Assets that match specific criteria. These Assets are returned in an array of Asset objects. See the Introduction for an explanation on [filtering](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters) and [faceting](https://developerdocs.instructure.com/services/ab-connect/introduction/facets#using-facets-as-an-entry-point-for-browsing-assets). This section covers the specifics of using filtering with the Assets resource.

To find Assets related to Standards, search based on the Standard GUID in the \`

alignments.id\` field. E.g.

```
filter[assets]=(alignments.id eq '6B29DCD6-29EB-11D8-9C6E-A97B3BAEC73A')
filter[assets]=(alignments.id in ('6B29DCD6-29EB-11D8-9C6E-A97B3BAEC73A','6DF95514-36D9-11E6-B844-14D399AB8BA3'))
```

A similar approach can be applied to Topics and Concepts.

If you have your organization's identifier for the Asset, but not the AB GUID for it, you can retrieve the GUID by doing a search on `client_id` to locate the Asset. E.g.

`filter[assets]=(client_id eq 'AJIH-45679')`

### Searching for Assets Owned by Another Provider

With AB Connect, it is possible to share your Assets with other AB Connect customers (Providers) to facilitate application interoperability. You can allow other Providers (the Consumer) to search sets of your Assets and retrieve the metadata profile describing your content. See the section on the [Providers](https://developerdocs.instructure.com/services/ab-connect/reference/providers) endpoint for an overview.

Assets include an `owner` relationship that references the object of the Provider to which the Asset belongs. By default, the Assets endpoint only searches the Assets you own. To search the Assets of other Providers, include `owner.id` in your filter criteria. You can get the IDs of the Owners to which you have access using the Providers endpoint. Alternatively, you can use the special keyword `_all` to search across all repositories to which you have access. E.g. `filter[assets]=owner.id eq _all`. You can also use the keyword `_me` to limit the search to just the Assets you own, but this is redundant with the approach of not specifying the `owner.id` at all.

Note that if you are including other Owners in your request, you can not include `custom_attributes`. Cross-owner searches can only operate on built-in properties.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[assets]stringOptional

comma separated list of field names

filter\[assets]stringOptional

an ODATA-like query string used to filter

filter\[alignments]stringOptional

an ODATA-like query string used to filter

sort\[assets]stringOptional

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