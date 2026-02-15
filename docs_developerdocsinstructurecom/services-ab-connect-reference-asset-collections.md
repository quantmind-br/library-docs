---
title: Asset Collections | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/asset-collections
source: sitemap
fetched_at: 2026-02-15T09:04:37.232586-03:00
rendered_js: false
word_count: 1062
summary: This document explains the structure of the filters object within an Asset Collection and provides a step-by-step guide on how to transform its JSON properties into valid API filtering expressions.
tags:
    - asset-collection
    - api-filtering
    - json-filters
    - facets
    - query-construction
    - academic-benchmarks
category: guide
---

When there is a need to quickly identify and refer to a filtered collection of assets, the "Asset Collection" is what provides a solution. Asset Collection stores the `filters` object with a `name` and a `guid` as reference.

- The "filters" is a JSON object that stores "assetType" and "facets". Searching filters are generated from this object to narrow down the result set the client wants to use.
- The "name" identifies the asset collection in human readable format.
- The "guid" identifies the asset collection in machine readable format.

The "filters" object stores the filtering expression for the asset collection. This stores facets and asset types which helps to filter to only the desired assets.

Here is a formal description about the `filters` object. For a practical explanation see the example below.

- `filters` (object, required) - JSON API object for `filters` object containing various fields like: `assetType` and `facets`.
  
  - `assetType` (string) - The Asset type defines the Asset's structure and is setup by in Academic Benchmarks an Administrative User.
  - `facets` (array) - List of facets derived from the Asset Definition.
    
    - (object)
      
      - `label` (string) - Name of the facet. Derived from Asset Definition: `data[n].attributes.properties[m].label`
      - `id` (string) - Same as `label`.
      - `field` (object) - The field object for the property. Derived from Asset Definition: `data[n].attributes.properties[m].field`.
        
        - `name` (string) - The API-recognized name for the entity you are filtering by. This is the property you would use when asking for facets.
        - `id` (string) - API identifier for the field which uniquely identifies the entity being filtered by. This is the property you would use when constructing your filter statement as the key field.
      - `facet` (object) - The facets object for the property. Derived from Asset Definition: `data.[n].attributes.properties.[m].facet`
        
        - `name` (string) - The API Identifier for the human-readable property in the facets response.
        - `id` (GUID) - The API Identifier for the entity-unique property in the facets response. This is the property you would use when constructing your filter statement and thus must correspond with the values in this entity’s `field.id`.
      - `selectedFilters` (array) - The list of selected values for the queries.
        
        - (object) - This objects holds the elements to which the `facid.id` refers.
          
          - `data` (object) - The object details for this facet item. See the definition of the object for the specific facet for details, but they all have at least the `descr` and `guid`.
            
            - `descr` (string) - Facet value text.
            - `guid` (GUID) - Facet value GUID.
            - `code` (string) - Facet value code name.

## Asset filtering expression

Filtering an asset query by a "field" and different "values" in AB API looks like this:

```
    filter[asset] = field_1 in (value_A, value_B)
```

With multiple fields it look like this:

```
    filter[asset] = field_1 in (value_A, value_B) and field_2 in (value_C, value_D)
```

Similar filters are created from the `filters` object. The left side of the query is the same. On the right side the expressions divided by the `and` are generated from the `filters.facets` list elements. The `field_1` and `field_2` are defined by `field.id`. The "values" are those items in the `selectedFilters` object which have the object-path defined in the `facet.id`. If `facet.id == "a.b"` then the values will be `selectedFilters[i].a.b`.

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

When there is a need to quickly identify and refer to a filtered collection of assets, the "Asset Collection" is what provides a solution. Asset Collection stores the `filters` object with a `name` and a `guid` as reference.

### List All Asset Collections

- To **list** Asset Collections the partner has access to, send a GET to the endpoint.
- To **find** an Asset Collection by exact name, send a GET to the endpoint with the `collection_name` parameter. This gives back only the case sensitive exact match if there is any.
- To **search** Asset Collections by name, send a GET to the endpoint with the `search_collection_name` parameter. This search uses case insensitive partial matching.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[asset\_collections]stringOptional

comma separated list of field names

filter\[asset\_collections]stringOptional

an ODATA-like query string used to filter

sort\[asset\_collections]stringOptional

a comma separated list of property names specifying the sort order of the returned results

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

### Create a new Asset Collection

To create an Asset Collection within the AB Connects system, you send a POST request to the endpoint. The body of the POST contains the Asset Collection definition in JSON format.

The response will be the same as a GET by GUID request for the created Asset Collection. See in the "Retrieving the Details of an Asset Collection".

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

## Working with Assets Collection

### Retrieving the Details of an Asset Collection

To get the Asset Collections you've created, call the endpoint with a GET while supplying the AB GUID for the Asset Collection. To retrieve the GUID, use the list and search functionality.

guidstringRequired

guid of specified asset collection

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[asset\_collections]stringOptional

comma separated list of field names

/asset\_collections/{guid}

### Modifying an Asset Collection

To update an Asset Collection, send a PATCH to the Asset Collection URL (with GUID) sending JSON in the body similar to that in the create statement. The JSON body only needs to contain the attributes that need to be updated. You can update the `name`, `filters` or `advanced_search` fields for the Asset Collection. You can update only one of these or all.

The response will contain the modified Asset Collection just as it would be in a GET by GUID request for the created Asset Collection. See in the "Retrieving Assets Collection".

### Deleting an Asset Collection

To delete an Asset Collection you've created, send a DELETE the endpoint while supplying the AB GUID for the Asset Collection. If you have the name for the Asset Collection but not the AB GUID, see the section on searching for Asset Collections.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).