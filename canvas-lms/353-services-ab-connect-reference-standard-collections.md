---
title: Standard Collections | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/standard-collections
source: sitemap
fetched_at: 2026-02-15T09:04:10.323884-03:00
rendered_js: false
word_count: 1031
summary: This document explains the concept of Standard Collections, detailing the structure of the filters object and how to construct filter expressions to query educational standards.
tags:
    - standard-collection
    - api-filters
    - educational-standards
    - json-structure
    - query-expressions
    - search-api
category: guide
---

When there is a need to quickly identify and refer to a filtered collection of standards, the "Standard Collection" is what provides a solution. Standard Collection stores the `filters` object with a `name` and a `guid` as reference.

- The "filters" is a JSON object that stores "filters (standard hierarchy)", "globalFilters". Searching filters are generated from this object to narrow down the result set the client wants to use.
- The "name" identifies the standard collection in human readable format.
- The "guid" identifies the standard collection in machine readable format.

The "filters" object stores the filtering expression for the standard collection. This stores standard hierarchy and global filters which helps to filter to only the desired standards.

Here is a formal description about the `filters` object. For a practical explanation see the example below.

- `filters` (object, required) - JSON API object for `filters` object containing various fields like: "filters (standard hierarchy)", "globalFilters"
  
  - `filters` (object) - Standard hierarchy
    
    - `key` (string) - Standard hierarchy element ID (guid or "root")
    - `value` (object) - Standard hierarchy element parameters
      
      - `collections` (array) - Array of GUIDs for the elements which are one level below in the hierarchy.
      - `id` (GUID) - GUID of the element in the hierarchy. (Same as the `key`.)
      - `parentId` (GUID) - GUID for the element which is one level above in the hierarchy.
      - `state` (string) - State is saying if the item element in the hierarchy is selected or not. Values can be: "checked" `[+]`, "indeterminate" `[-]`, "unchecked" `[ ]`
      - `type` (string) - Type of position in the hierarchy. Values in hierarchical order: "region" &gt; "publication" &gt; "document" &gt; "section" &gt; "standard".
  - `globalFilters` (object) - Standard global filters: filtering by standard facets
    
    - `key` (string) - Standard facet description. (Eg: `"document.publication.regions":`)
    - `value` (object) - Standard facet parameters
      
      - `guid` (GUID) - GUID of the element in the hierarchy. (Eg.: `"A832862C-901A-11DF-A622-0C319DFF4B22"`)
      - `name` (text) - Value of the facet parameter. (Eg.: `"California"`)

## Example to build a "filter expression" from the "filters" object

Here is a `filters` object. Let's see how filter expression can be generated from it step-by-step:

```
        "filters": {
          "assetType": "NLP_MHE",
          "facets": [
            {
              "label": "Grade",
              "id": "Grade",
              "field": {
                "name": "education_levels.grades",
                "id": "education_levels.grades.guid"
              },
              "facet": {
                "name": "data.descr",
                "id": "data.guid"
              },
              "selectedFilters": [
                {
                  "data": {
                    "descr": "Kindergarten",
                    "guid": "F1F9FA12-3B53-11E0-A421-F4B24952E9DF",
                    "code": "K",
                    "seq": 20
                  }
                },
                {
                  "data": {
                    "descr": "9th Grade",
                    "guid": "ABBAABBA-ACDC-ACDC-B042-495E9DFF4B22",
                    "code": "9",
                    "seq": 20,
                  }
                },
              ],
            },
            {
              "id": "Subject",
              "label": "Subject",
              "field": {
                "name": "disciplines.subjects",
                "id": "disciplines.subjects.ids"
              },
              "facet": {
                "name": "data.descr",
                "id": "data.guid"
              },
              "selectedFilters": [
                {
                  "data": {
                    "descr": "Mathematics",
                    "guid": "495E9DFF-3B53-11E0-B042-C4B222F1FB2F",
                    "code": "MATH"
                  },
                  "count": 2488
                }
              ]
            }
          ]
        }
```

The left side of the expression starts with `filter[asset] =`. There are two elements in the `filters.facets` array, so there will be two expressions on the right side. For example expressions `expr_1` and `expr_2`. These are the basis of the filtering. The `expr_1` is built up from `filters.facets[0]` and the `expr_2` is built up from `filters.facets[1]`.

```
    filter[asset] = expr_1 and expr_2
```

Expressions are built up from a "field" and set of "values". The filter will give back those assets which have given the "values" on the given "field".

Let's find the "field" values. In the JSON object the "field" is defined by `field.id`.

```
facets[0].field.id = "education_levels.grades.guid"`
facets[1].field.id = "disciplines.subjects.ids"
```

Substitute these as "fields" into the filter expression.

```
    filter[asset] = education_levels.grades.guid in (values_1) and disciplines.subjects.ids in (values_2)
```

Let's find the "values". The variables' names that are holding the "values" are defined by the `facet.id`. The "values" are those items in the `selectedFilters` object which have the object-path defined in the `facet.id`.

The variable for "values\_1" is `facet.id = "data.guid"`. Let's gather the values from `selectedFilters.data.guid` and generate the "values\_1".

```
    selectedFilters[0].data.guid = "F1F9FA12-3B53-11E0-A421-F4B24952E9DF"
    selectedFilters[1].data.guid = "ABBAABBA-ACDC-ACDC-B042-495E9DFF4B22"
    ==> 
    values_1 = "F1F9FA12-3B53-11E0-A421-F4B24952E9DF", "ABBAABBA-ACDC-ACDC-B042-495E9DFF4B22"
```

The variable for "values\_2" is `facet.id = "data.guid"`. Let's gather the values from `selectedFilters.data.guid` and generate the "values\_2".

```
    selectedFilters[0].data.guid = "495E9DFF-3B53-11E0-B042-C4B222F1FB2F"
    ==> 
    values_2 = "495E9DFF-3B53-11E0-B042-C4B222F1FB2F"
```

Finally substitute the "values" into the filter expression:

```
    filter[asset] = education_levels.grades in ("F1F9FA12-3B53-11E0-A421-F4B24952E9DF", "ABBAABBA-ACDC-ACDC-B042-495E9DFF4B22") and disciplines.subjects.ids in ("495E9DFF-3B53-11E0-B042-C4B222F1FB2F")
```

This example will filter only those assets which are in the grade: "Kindergarten" or "9th Grade" and are in the subject: "Mathematics".

To get the available facets for standards check the `facet_summary` at [facets](https://developerdocs.instructure.com/services/ab-connect/introduction/facets) for details.

When there is a need to quickly identify and refer to a filtered collection of standards, the "Standard Collection" is what provides a solution. Standard Collection stores the `filters` object `name` and a `guid` as reference.

### List All Standard Collections

- To **list** Standard Collections the partner has access to, send a GET to the endpoint.
- To **find** a Standard Collection by exact name, send a GET to the endpoint with the `collection_name` parameter. This gives back only the case sensitive exact match if there is any.
- To **search** Standard Collections by name, send a GET to the endpoint with the `search_collection_name` parameter. This search uses case insensitive partial matching.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standard\_collections]stringOptional

comma separated list of field names

filter\[standard\_collections]stringOptional

an ODATA-like query string used to filter

sort\[standard\_collections]stringOptional

a comma separated list of property names specifying the sort order of the returned results

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

### Create a new Standard Collection

To create a Standard Collection within the AB Connects system, you send a POST request to the endpoint. The body of the POST contains the Standard Collection definition in JSON format.

The response will be the same as a GET by GUID request for the created Standard Collection.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

## Working with Standards Collection

### Retrieving the Details of a Standard Collection

To get the Standard Collections you've created, call the endpoint with a GET while supplying the AB GUID for the Standard Collection. To retrieve the GUID, use the list and search functionality.

guidstringRequired

guid of specified standard collection

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standard\_collections]stringOptional

comma separated list of field names

/standard\_collections/{guid}

### Modifying a Standard Collection

To update a Standard Collection, send a PATCH to the Standard Collection URL (with GUID) sending JSON in the body similar to that in the create statement. The JSON body only needs to contain the attributes that need to be updated. You can update the `name` or `filters` fields for the Standard Collection. You can update only one of these or all.

The response will contain the modified Standard Collection just as it would be in a GET by GUID request for the created Standard Collection.

guidstringRequired

guid of specified standard collection

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

/standard\_collections/{guid}

### Deleting a Standard Collection

To delete a Standard Collection you've created, send a DELETE the endpoint while supplying the AB GUID for the Standard Collection. If you have the name for the Standard Collection but not the AB GUID, see the section on searching for Standard Collections.

guidstringRequired

guid of specified standard collection

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

/standard\_collections/{guid}

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).