---
title: Managing and Predicting Relationships | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/reference/relationships
source: sitemap
fetched_at: 2026-02-15T09:04:54.920922-03:00
rendered_js: false
word_count: 6397
summary: This document explains how the AB Connect Content Enrichment service manages and predicts relationships between educational assets, standards, topics, and concepts based on metadata profiles.
tags:
    - ab-connect
    - content-enrichment
    - relationship-prediction
    - educational-standards
    - metadata-alignment
    - taxonomy-management
category: concept
---

One of the most powerful features of AB Connect is the ability to build, predict and navigate relationships. These relationships are managed by direct connection (e.g. relating a Standard to an Asset), indirect reference (e.g. relating entities based on mutual relationships with other entities), prediction (when the system suggests a relationship) and through other system derived means. The following sections explain how to manage these relationships.

Note that some relationships are complex having multiple properties that exist on the relationship. These relationships are represented in AB Connect as relational objects and have their own endpoints. These relationship objects are not covered here but have their own sections in the documentation.

## Content Enrichment Overview

AB Connect offers a Content Enrichment service which helps to establish, maintain and predict relationships between Assets (content, assessment items, etc.), Standards, Topics, Concepts and other Assets. This system uses the Asset metadata profile, learning algorithms and relationship data we've built over 15 years of aligning content. Content Enrichment makes your Assets more discoverable and aids in building relationships. Content Enrichment uses intermediaries like Topics, Concepts and Key Ideas when relating Asset and Standards.

The AB Topic Taxonomy is a broad taxonomy used for general categorization of Standards. Every Standard in the core four subjects (language arts, math, science and social studies) is associated with at least one Topic. The use of Topics builds relationships quickly and easily. When a Standard is related to an Asset, a predicted relationship between the Asset and one or more Topics is established. This is a bi-directional capability so establishing a relationship between a Topic and an Asset will create predicted relationships between the Asset and Standards (typically multiple Standards - across all authorities in your license). The use of Topics to enrich your Assets is a very efficient way to power search-by-Standard capabilities in your system and enable the fast discovery of relationships.

The AB Concept Taxonomy is a granular means for identifying precise relationships between Standards and Assets. Concepts represent individual notions covered by an Asset or Standard. Concepts are linked together to build Key Ideas that are then associated with Standards. Key Ideas are similar to unpacked Standards and are a key component to the AB Content Enrichment Engine. As an Asset's Concept profile is defined, the prediction engine is able to more accurately predict relationships between the Asset and new Standards. Note that the prediction engine utilizes the Disciplines and Education Levels specified in the Assets and Standards profiles (when present) to assist in predictions. Connecting an Asset to Concepts or Standards outside of the Asset's Discipline and Education Level profile will not aid or alter the predictions or clarifications. See [Managing Relationships Between Assets and Concepts](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#managing-relationships-between-assets-and-concepts)

for details on tagging content with Concepts and the section on [Standards](https://developerdocs.instructure.com/services/ab-connect/reference/standards) for information on retrieving Key Idea data from a Standard.

However you choose to enrich your content, calling the Predictions endpoint engages the engine to predict relationships between your Asset and other entities in the system. While many aspects of the Asset metadata profile can impact predictions, the predictions are not actually generated until the predictions endpoint is called. This is true for changes in disciplines, education levels and relationships to Standards, Topics, Concepts and donors. See [Managing and Predicting Relationships](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#getting-and-updating-predictions) for details on using the prediction engine.

While a detailed explanation of Content Enrichment is beyond the scope of this API documentation, you can get more information by contacting [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) at Instructure or your sales representative.

Note that use of Academic Benchmarks Assets, Topics, Concepts and Clarifier is enabled through licensing. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on how to enable these features.

### The Effect of Metadata on Predictions and Clarifications

AB Connect uses the metadata profiles of Topics, Standards and Assets to understand relationships, recommend additional relationships and determine where the recommendation engine needs further clarification. The profiles can impact the engine in many ways. A couple of things to be aware of when working with AB Connect and relationships between Assets, Topics and Standards:

- If disciplines and education levels are defined on an Asset, they should match or at least overlap with those on the Topic or Standard if you hope to have the relationship shape the recommendations made by the system. When the descriptions do not match, the engine ignores the relationship for the purpose of recommendations and requesting clarifications.
- Standards that do not have an utilization type of "alignable" typically do not impact future recommendations for the Asset relationships.
- If you are working with Assets that are using v2 of the prediction engine (see the prediction\_algorithm field), creating, deleting and modifying relationships between the Asset and Standards, Concepts or Topics upgrades the prediction algorithm to v3.

For example, if you have a 3rd grade Asset (`education_levels.grades.code eq '3'`) and create a relationship between that Asset and the middle school Topic "Solving Equations", the system will not predict any relationships to Standards because the grade ranges don't match between the Topic and Asset.

### Locating Recent Changes to Relationships Between Assets and Standards

Some AB Connect customers prefer to cache Asset and Standards data within their system and refresh the data periodically. To make this process more efficient and to support customer processes where changes may go through an internal review process, AB Connect allows you to search for Assets by the date that a relationship between a Standard and Asset changed. To do this, search for Assets where `date_alignments_modified_utc` is greater than a certain point in time. E.g.

```
    /assets?filter[assets]=(date_alignments_modified_utc gt '2017-09-12 12:00:00')
```

Once you have a list of Assets where their relationships with Standards have changed recently, you can filter on the related Standards by date to see which specific changes have been made. E.g.

```
    /assets/00005A1C-3229-11E6-9E77-9DD429C466BA/alignments?filter[alignments]=(meta.date_modified_utc gt '2017-09-12 12:00:00')
```

```
    /assets/00005A1C-3229-11E6-9E77-9DD429C466BA/alignments?filter[alignments]=(meta.date_created_utc gt '2017-09-12 12:00:00')
```

```
    /assets/00005A1C-3229-11E6-9E77-9DD429C466BA/deleted_alignments?filter[deleted_alignments]=(meta.date_deleted_utc gt '2017-09-12 12:00:00')
```

### Retrieving Standards Related to an Asset that Meet Certain Criteria

Some AB Connect customers display "alignments" (relationships between Assets and Standards) with their content. Often, they will know the Authority associated with the browser (e.g. a teacher registered in an LMS may have their state in their profile). In this case, it is possible to retrieve only the given Authority's Standards related to this Asset. To do this, search for Standards related to the Asset and filter the Standards by Authority. E.g.

```
    /assets/00005A1C-3229-11E6-9E77-9DD429C466BA/alignments?filter[alignments]=(meta.disposition eq 'accepted' and document.publication.authorities.descr eq 'Texas DOE')&fields[standards]=number.enhanced,statement.descr
```

This same concept can be used to filter on any of the "meta" fields on the relationship and the Standards properties listed in [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources).

### Retrieving Topics Related to an Asset that Meet Certain Criteria

Similar to the Standards based example above, you may want to retrieve related Topics that are accepted. To do this, search for Topics related to the Asset and filter the disposition. E.g.

```
    /assets/00005A1C-3229-11E6-9E77-9DD429C466BA/topics?filter[topics]=(meta.disposition eq 'accepted')
```

This same concept can be used to filter on any of the "meta" fields on the relationship and the Topics properties listed in [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources).

### Retrieving Concepts Related to an Asset that Meet Certain Criteria

Similar to the examples above, you may want to retrieve related Concepts that are central. To do this, search for Concepts related to the Asset and filter the emphasis. E.g.

```
    /assets/00005A1C-3229-11E6-9E77-9DD429C466BA/concepts?filter[concepts]=(meta.emphasis eq 'central')
```

This same concept can be used to filter on any of the "meta" fields on the relationship and the Concepts properties listed in [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources).

## Managing Relationships Between Assets and Standards

AB Connect allows you to connect your Assets directly to Standards. Establishing relationships between Assets and Standards can power services like searching for Assets by Standards and gap analysis. Building (and rejecting) direct relationships like this can also be the first step accelerating Content Enrichment. Direct relationships can be very helpful in building and managing your Asset library but full Content Enrichment with intermediaries like Topics and Concepts can greatly accelerate the process and broaden the network of relationships quickly and efficiently.

You can create (and add) a direct relationship between an Asset and Standards by POSTing to `/assets/{guid}/alignments`. You can "accept" or "reject" a direct relationship. Accepting one is indicating that the relationship has been reviewed and is correct. Rejecting a relationship indicates that the relationship has been reviewed and there is no relationship between the Asset and Standard. This is known as the disposition of the relationship.

In addition to specifying the disposition, for accepted relationships, you can associate tags with the relationship. The meaning of the tag is partner defined and the following values are accepted:

Since JSON API does not allow direct properties on relationships, the disposition and tags are stored in the relationship metadata.

### Updating and Deleting All Relationships

To replace all existing relationships between and Asset and some Standards, PATCH the endpoint sending the new relationships in the PATCH body. The body is in the same format as when creating a relationship. In JSON API, relationships either exist or do not, so there isn't a mechanism to directly support altering relationship properties of a subset of the relationships. In order to alter the metadata on one or more relationships (e.g. `disposition` or `tags`), you must PATCH all relationships including the desired metadata for each relationship. Any relationships or relationship metadata properties NOT included in the PATCH body will be removed. Note that you can remove ALL relationships between Assets and Standards by sending an empty set in the PATCH body. E.g. `{ "data": [] }`

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

/assets/{guid}/alignments

### Removing Specific Relationships

It is possible to remove specific relationships between an Asset and one or more Standards using the DELETE method and including the Standards you'd like to remove from the Asset.

## Filtering and Paging Relationships Between Assets and Standards

AB Connect allows you to filter and page through the list of Standards related to an Asset. This can be helpful if you are wanting to limit the alignments you are showing a user to those in their specified state or if you are caching Assets and only want to retrieve alignments that have changed since the last time you cached the data (for example).

You can filter and sort on relationship properties like `meta.disposition` and `meta.date_modified_utc` or on Standards properties. If you are using Standards properties in your filtering and sorting, you are limited to the fields listed in the Standards section of the [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources) documentation. Note that when using Standards properties for filtering here, you can drop the `alignments.` from the property name.

### Fetching Related Standards

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standards]stringOptional

comma separated list of field names

filter\[alignments]stringOptional

an ODATA-like query string used to filter

sort\[alignments]stringOptional

a comma separated list of property names specifying the sort order of the returned results

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

/assets/{guid}/alignments

## Filtering and Paging Deleted Alignments

AB Connect allows you to filter and page through the list of Standards that used to be related to an Asset. This can be helpful if you are caching Assets and only want to retrieve alignments that have changed since the last time you cached the data. This is the only way to get the list of deleted alignments.

### Fetching Formerly Related Standards

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standards]stringOptional

comma separated list of field names

filter\[alignments]stringOptional

an ODATA-like query string used to filter

sort\[alignments]stringOptional

a comma separated list of property names specifying the sort order of the returned results

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

/assets/{guid}/deleted\_alignments

## Managing Relationships Between Assets and Topics

If you have licensed the Academic Benchmarks Topic Taxonomy (here referred to simply as Topics), Topics can assist with Asset searches and be a powerful tool to help establish relationships between Assets and Standards. One of the most powerful features of AB Connect is the ability to build, predict and navigate relationships. These relationships are managed by direct connection (e.g. relating a Topic to an Asset), indirect reference (e.g. automatically relating to Topics based in their relationships to Standards) and through other system derived means. The process of developing these relationships and describing an Asset with metadata is known as Content Enrichment because by associating an asset with the Academic Benchmark metadata, you gain access to a rich network of additional relationships that can serve to power search and discovery, alignment processes, and navigability within content.

Content Enrichment with the Academic Benchmarks Topic Taxonomy enables coarse-grained description and relationship management. The Topic Taxonomy was developed with browsability in mind, ...not only controlling the vocabulary, but also the organization in a rigid 4-level hierarchy that includes Subject &gt; Grade Band &gt; Branch &gt; Topic. Topics represetn what should be learned at a broad level. The coarse-grained nature of the AB Topic Taxonomy enables a simple relationship management mechanism and can be used in your search technologies for advanced and efficient discovery capabilities. At its simplest, establishing a relationship between an Asset and a Topic enables AB Connect to predict relationships between the Asset and Standards. This is a bi-directional relationship, so the process could alternatively start with creating a direct relationship between a Standard and Asset which would predict relationships between the Asset and one or more Topics.

If you are in need of tighter relationship management, see [Concepts](https://developerdocs.instructure.com/services/ab-connect/reference/concepts) and [Managing Relationships Between Assets and Concepts](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#managing-relationships-between-assets-and-concepts).

Enriching your Asset with Topics:

1. Create a relationship between the Topic and Asset (see below)
2. Now if you [retrieve the Asset](https://developerdocs.instructure.com/services/ab-connect/reference/assets#retrieving-assets), you'll see the `accepted` Topic relationship and a number of `predicted` Standards relationships
3. You can also reject bad matches and delete erroneous matches.

Note that use of Academic Benchmarks Assets, Topics, Concepts and Clarifier is enabled through licensing. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on how to enable these features.

You can create (and add) a direct relationship between an Asset and Topics by POSTing to `/assets/{guid}/topics`. You can "accept" or "reject" a direct relationship. Accepting one is indicating that the relationship has been reviewed and is correct. Rejecting a relationship indicates that the relationship has been reviewed and there is no relationship between the Asset and Topic. This is known as the disposition of the relationship. Since JSON API does not allow direct properties on relationships, the disposition is stored in the relationship metadata.

### Updating and Deleting All Relationships

To replace all existing relationships between and Asset and some Topics, PATCH the endpoint sending the new relationships in the PATCH body. The body is in the same format as when creating a relationship. In JSON API, relationships either exist or do not, so there isn't a mechanism to directly support altering relationship properties of a subset of the relationships. In order to alter the metadata on one or more relationships (e.g. `disposition`), you must PATCH all relationships including the desired metadata for each relationship. Any relationships or relationship metadata properties NOT included in the PATCH body will be removed. Note that you can remove ALL relationships between Assets and Topics by sending an empty set in the PATCH body. E.g.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

### Removing Specific Relationships

It is possible to remove specific relationships between an Asset and one or more Topics using the DELETE method and including the Topics relationships to remove from the Asset.

## Filtering and Paging Relationships Between Assets and Topics

AB Connect allows you to filter and page through the list of Topics related to an Asset. This can be helpful if you are wanting to limit the Topics you are showing a user to those that have been accepted (for example).

You can filter and sort on relationship properties like `meta.disposition` or on Topics properties. If you are using Topics properties in your filtering, you are limited to the fields listed in the Topics section of the [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources) documentation. Note that when using Topics properties for filtering here, you can drop the `topics.` from the property name.

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

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

## Managing Relationships Between Assets and Concepts

If you have licensed the Academic Benchmarks Concept Taxonomy, Concepts enable detailed definition of Asset metadata profiles which power precise search and relationship prediction capabilities. The Asset metadata included describes the Asset with a controlled vocabulary to reflect what should be learned at the most granular level. This level of granular description, combined with machine learning technology, results in an Asset profile that learns from user input, and updates recommendations automatically, facilitating easier change management of Standards. Beyond relationships management, Concepts can be used in your search technologies for advanced and efficient search capabilities.

The process of developing these relationships and describing an Asset with metadata is known as Content Enrichment because by associating an asset with the Academic Benchmark metadata, you gain access to a rich network of additional relationships that can serve to power search and discovery, alignment processes, and navigability within content. When you establish a relationship between a Concept and an Asset, you will notice that the system predictions between the Asset and Standards change and tighten. The Clarifier helps you to tune the system predictions and can be a very powerful addition to your arsenal. See the [Clarifier documentation](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#request-a-clarification) for details.

Here is an easy approach for tagging your Asset with Concepts:

1. Confirm relationships with Concepts (see below) and/or additional [Standards](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#managing-relationships-between-assets-and-standards) to refine the metadata profile for the Asset
2. Update the predictions made by the system.
3. Repeat the clarification steps until the content is fully tagged and predicted relationships are strong.

Note that the `context` of the Concept is important. Any decisions regarding a relationship between a Concept and an Asset should be made with the `context` taken into consideration.

Note that use of Academic Benchmarks Assets, Topics, Concepts and Clarifier is enabled through licensing. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on how to enable these features.

You can create (and add) a relationship between an Asset and Concepts by POSTing to `/assets/{guid}/concepts`. Concepts have different types of relationships with Assets than Topics and Standards. Instead of accepting or rejecting a disposition, Concept relationships have an emphasis of either `central`, `related`, `not_applicable` or `avoid`. `central` indicates that the Concept is one of the key notions covered by the Asset. `related` indicates that the Asset covers the Concept but it is not core to the Asset. `not_applicable` indicates that the Concept is **NOT** relevant to the Asset (used to clarify Concepts to aid in predicting relationships). `avoid` indicates that this Concept is not only irrelevant to the Asset but Standards that relate to this Concept should be avoided when predicting relationships. Since JSON API does not allow direct properties on relationships, the disposition is stored in the relationship metadata.

### Updating and Deleting All Relationships

To replace all existing relationships between and Asset and some Concepts, PATCH the endpoint sending the new relationships in the PATCH body. The body is in the same format as when creating a relationship. In JSON API, relationships either exist or do not, so there isn't a mechanism to directly support altering relationship properties of a subset of the relationships. In order to alter the metadata on one or more relationships (e.g. `emphasis`), you must PATCH all relationships including the desired metadata for each relationship. Any relationships or relationship metadata properties NOT included in the PATCH body will be removed. Note that you can remove ALL relationships between Assets and Concepts by sending an empty set in the PATCH body. E.g.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

### Removing Specific Relationships

It is possible to remove specific relationships between an Asset and one or more Concepts using the DELETE method and including the Concepts remove from the Asset.

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

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

## Filtering and Paging Relationships Between Assets and Concepts

AB Connect allows you to filter and page through the list of Concepts related to an Asset. This can be helpful if you are wanting to limit the Concepts you are showing a user to those that are central (for example).

You can filter and sort on relationship properties like `emphasis` or on Concepts properties. If you are using Concepts properties in your filtering, you are limited to the fields listed in the Concepts section of the [Filtering Resources by Properties on Related Resources](https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects#filtering-resources-by-properties-on-related-resources) documentation. Note that when using Concepts properties for filtering here, you can drop the `concepts.` from the property name.

### Fetching Related Concepts

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

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

## Managing Relationships Between Assets

It is possible to configure the properties of an Asset to allow inter-Asset relationships to be managed. These are very rare use cases. If you have a need to express Asset-to-Asset relationships within AB Connect, start the project with a conversation with [AB Supportarrow-up-right](https://certicasolutions.freshdesk.com/support/tickets/new) to discuss your use case. AB Support can setup your Asset configuration (`asset_type`) to allow you to manage these relationships.

AB Connect can support three inter-Asset relationship types:

1. `parent` - The parent relationship allows you to build a Asset hierarchy. No additional properties, data or services are conveyed through this relationship. It is simply a means for expressing a hierarchy. Note that there is no reciprocal `children` property and an Asset can have only one parent.
2. `alignment_donors` - Alignment Donors are Assets that convey relationships with Standards and Topics to their Recipients. A Recipient is an Asset that has one or more Assets listed in its `alignment_donors` relationship. Notes:
   
   1. Alignment Donor Assets (Assets appearing in an `alignment_donor` list on some other Asset) can not be deleted. To delete an Alignment Donor, remove it from all `alignment_donor` relationships and then delete the Asset.
   2. Only Standards and Topics relationships with a disposition of `predicted` or `accepted` are conveyed to Recipients.
   3. In the event of disposition conflict in the Donors, `accepted` takes precedence.
   4. The relationship conveyence is dynamic so changes to Donors are reflected in Recipients. However, if an alignment (relationship to a Standard) is changed on the Alignment Donor, the new alignment will not appear on the Recipient until the Recipient Asset's predictions have been updated.
   5. Standards and Topics relationships can be applied directly to Recipients to augment or override relationships conveyed from Donors.
   6. It is not possible to delete conveyed relationships but it is possible to override them by creating the same relationship directly on the Recipient but setting the disposition to `rejected`.
3. `concept_donors` - Concept Donors are Assets that convey relationships with Concepts to their Recipients. A Recipient is an Asset that has one or more Assets listed in its `concept_donors` relationship. Notes:
   
   1. Concept Donor Assets (Assets appearing in a `concept_donors` list on some other Asset) can not be deleted. To delete a Concept Donor, remove it from all `concept_donors` relationships and then delete the Asset.
   2. In the event of emphasis conflict in the Donors, the order of precedence is `central`, `related`, `not_applicable` and then `avoid`.
   3. Unlike Alignment Donors, with Concept Donors, Concepts relationships can NOT be applied directly to Concept Recipients.
   4. The relationship conveyence is dynamic so changes to Donors are reflected in Recipients.
      
      1. If a Concept is added, modified or deleted from a Donor, the Concept relationship change does not show up immediately on the Recipients. In order for the change to propagate to the Recipient, the Recipient has to be modified (be POSTed or PATCHed to) or the Recipient Asset's predictions have been updated.
      2. If a Concept is added, modified or deleted from a Donor, the relationship predictions on the Recipient are not updated until the Recipient Asset's predictions have been updated.

You can create (and add) a relationship between Assets by POSTing to `/assets/{guid}/{relationship}`. Parent relationships are single entities. The others must be arrays.

### Updating and Deleting All Relationships

To replace all existing relationships between an Asset and its `alignment_donors` or `concept_donors`, PATCH the endpoint sending the new relationships in the PATCH body. The body is in the same format as when creating a relationship. In order to alter the relationships with PATCH, you must include all relationships you'd like to retain in the request. Any relationships of this type that are NOT included in the PATCH are removed. Note that you can remove ALL relationships between Assets and Concepts by sending an empty set in the PATCH body. E.g.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

/assets/{guid}/alignment\_donors

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

/assets/{guid}/concept\_donors

### Removing Specific Relationships

It is possible to remove specific relationships between a Assets using the DELETE method and including the Assets to remove.

The Predictions endpoint allows you to predict relationships between unrelated entities. AB Connect currently supports three prediction scenarios:

- Predict Standards alignments and Topics for an Asset based on the metadata description of the Asset and machine learning algorithms
- Predict Standards alignments for an Asset based on Crosswalk relationships
- Predict Assets that would align to a Standard based on Crosswalk relationships

Note that access to Predictions is licensed. If your credentials are correct and you are still receiving a 401 error (or no results), check with [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20%3APredictions%20Licensing) to ensure you are licensed for Predictions. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to Predictions.

Working with Predictions for an Asset is implemented as follows:

```
    POST Predictions to start the calculation process
    if queue-status Response has code pending
        loop until queue-status has code complete
            GET queue-status with max_wait=25
        endloop
    if you want to review Predictions, GET Predictions and page/filter through them
    POST to Predictions/Asset to update Predictions on Asset
```

Predicting Assets for Standards is implemented as follows:

```
    POST Predictions to start the calculation process
    if queue-status Response has code pending
        loop until queue-status has code complete
            GET queue-status with max_wait=25
        endloop
    Review Predictions, GET Predictions and page/filter through them
    Determine which Assets should get alignments to the standard in question
    POST new alignments to those Assets
```

### Calculating the Latest Predictions

Using the POST method, you can generate a set of predictions for the specified scenario. Calculating Predictions does not create relationships. It just calculates what relationships appear to be relevant. The relationships can be established as a later step. There are two algorithms for generating Predictions: machine learning and crosswalk relationships.

**Machine Learning** The machine learning algorithm for predicting relationships is called the "confidence" algorithm. At this point, confidence can only be used to predict Standards and Topics alignments for Assets. Attempting to use confidence to predict Assets for a Standard will result in an error. The Topics relationships are predicted based on the established relationships between the Topics and Standards already aligned to the Asset. Standards relationships are predicted based on the metadata definition of the Asset which includes alignments to other Standards, Topics, Concepts, subjects, etc.

**Crosswalks** When Crosswalks are used for prediction purposes, they represent two corners of a triangle, with an asset providing the third corner. Using existing alignments (and traversing the edges of the triangle), the system provides predictions of both new standards to assets as well as unaligned assets to new standards. This algorithm uses the Crosswalk relationships between Standards to identify additional relevant Standards. In the case of predicting related Assets, the system walks the Standards relationships and identifies Assets related to the connected Standards.

Note that the Crosswalk relationships are available directly to the calling application through the Standards endpoint, but the predictor simplifies use by navigating common relationships to generate Crosswalks between documents that aren't directly related. E.g. if you are attempting to predict from an Indiana Standard to a New Jersey Standard and Academic Benchmarks has not directly curated relationships between those documents, the predictor will use an intermediary document (perhaps one in Texas) to synthesize the relationships for the predictions. Note that the steps the system had to take to establish the prediction is available in the `steps` property. Predictions with 1 step are from directly connected Standards. Predictions with 2 are generated by walking from one authority to a common document then to the second authority. In this case, the relationships may lose some precision.

**Usage** Sometimes calculating Predictions can be resource intensive and take several seconds or even a few minutes. For this reason, the Predictions endpoint uses a queue model. The request to calculate Predictions returns a `queue-status` object. The `queue-status` object indicates the state of the queued processing of Predictions. If the calculations complete quickly (less than 30 seconds), the request response will indicate that the calculations are complete and you can GET the Predictions right away. If the calculations go beyond 30 seconds, the response will indicate that the calculations are continuing in which case you will need to check the queue periodically until you receive a response indicating that the calculations are complete. See [Fetching the Prediction Queue Status](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#checking-the-prediction-queue-status) for details on polling the queue.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[queue-status]stringOptional

comma separated list of field names

Note that both the `queue-status` and `predictions` objects have GUIDs that are different from the related Asset GUID. If you are checking the queue status, use the `links.self` URL or construct the URL manually using the GUID in the `data.id` property. Similarly, once the predictions are complete, use the `relationships.predictions.links.related` property to locate the predicted alignments.

## Checking the Prediction Queue Status

The Queue Status endpoint allows you to check on the Predictions calculations progress for long running Predictions.

### Fetching the Queue Status

Using the GET method, you can retrieve the `queue-status` and check the `data.attributes.code` field. `pending` means the Predictions are still being calculated. `complete` means the Predictions are ready. See the `data.relationships.predictions.links.related` property for a link to the results.

guidstringRequired

guid of specified prediction

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[queue-status]stringOptional

comma separated list of field names

max\_waitnumberOptional

comma separated list of field names

/predictions/queue-status/{guid}

The Predictions endpoint allows you to retrieve the details of the Prediction set (like when it expires, what Asset it is related to) and start paging through predicted relationships.

Note that access to Predictions is licensed. If your credentials are correct and you are still receiving a 401 error (or no results), check with [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) to ensure you are licensed for Predictions. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to Predictions.

Using the GET method, you can see what predictions the engine makes for the Asset metadata profile using the GUID or related URL (`relationships.predictions.links.related`) returned when calculating the predictions.

guidstringRequired

guid of specified prediction set

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[predictions]stringOptional

comma separated list of field names

fields\[standards]stringOptional

comma separated list of field names

fields\[topics]stringOptional

comma separated list of field names

fields\[assets]stringOptional

comma separated list of field names

includestringOptional

A comma separated list of resource names that will be returned in the response.

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

## Filtering and Paging Predictions

AB Connect allows you to filter and page through predicted standards. You can filter and sort on relationship properties like `meta.score` or on the item properties themselves.

### Fetching Related Standards

guidstringRequired

guid of specified prediction set

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

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

/predictions/{guid}/standards

guidstringRequired

guid of specified prediction set

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

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

/predictions/{guid}/topics

## Updating Predictions on the Asset

To commit the Predictions to the Asset as alignments, POST to the `predictions/assets` endpoint supplying the Predictions GUID. This updates the predicted alignments on the Asset, replacing any previously predicted alignments and creating new deleted\_alignments as appropriate.

### Updating Predictions on the Asset

Note that the POST has no request nor response body.

guidstringRequired

guid of specified prediction set

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

/predictions/{guid}/asset

One key component to the prediction engine is the Clarifier which can be used on an Asset to request Concepts and Standards for which the system needs clarification regarding the status of the relationship between the Asset and Concepts/Standards. As the user provides input about clarifications, the system refines its calibration for the ranking of Asset-Standards relationship predictions. The Clarifier, combined with setting the disposition of Standards and the emphasis of Concepts, helps the user build an Asset profile that continues to learn and adapt as input is provided, making search capabilities stronger and relationship maintenance far simpler.

To retrieve clarifications for an Asset, call the Clarifier endpoint appending the AB GUID of the Asset in question to the path portion of the URL. If you do not know the AB GUID for the Asset in question, you can search the Asset endpoint filtering on the `client_id` which should be your ID for the Asset. See the section on [Assets](https://developerdocs.instructure.com/services/ab-connect/reference/assets#searching-for-assets) for details on searching for Assets.

Note that access to the Clarifier is controlled by licensing. If your credentials are correct and you are still receiving a 401 error (or no results), check with [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) to ensure you are licensed for the Clarifier. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to the Clarifier.

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

includestringOptional

A comma separated list of resource names that will be returned in the response.

fields\[clarifier]stringOptional

comma separated list of field names

fields\[standards]stringOptional

comma separated list of field names

fields\[concepts]stringOptional

comma separated list of field names

filter\[clarification\_standards]stringOptional

an ODATA-like query string used to filter

## Filtering and Paging Relationships on Standards

AB Connect allows you to filter and page through related objects. You can filter and sort on relationship properties like `meta.same_text` or, in the case of Concepts, `descr` or `context`.

### Fetching Related Standards

guidstringRequired

guid of specified standard

relationshipstring · enumRequiredPossible values:

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[standards]stringOptional

comma separated list of field names

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

/standards/{guid}/{relationship}

guidstringRequired

guid of specified standard

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[topics]stringOptional

comma separated list of field names

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

### Fetching Related Concepts

guidstringRequired

guid of specified standard

partner.idstringRequired

Your partner ID - you should have gotten them from AB Support or when you signed up for a sandbox account.

auth.signaturestringRequired

Signature for the request authorization.

auth.expiresstringRequired

Expiration timestamp for the authorization.

fields\[concepts]stringOptional

comma separated list of field names

limitnumberOptional

The page size for the response dataset. limit must be 100 or less.

offsetnumberOptional

How far into the dataset you are paging

/standards/{guid}/concepts

## Filtering and Paging Relationships on Topics

AB Connect allows you to page through objects related to the Topic. Filtering the list of related objects is not supported at this point in time.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).