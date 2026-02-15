---
title: How To Articles, Recommendations and Suggestions | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/how-to
source: sitemap
fetched_at: 2026-02-15T09:04:18.298212-03:00
rendered_js: false
word_count: 6092
summary: This guide explains the hierarchical organizational structure of academic standards and demonstrates how to navigate through authorities, publications, documents, and sections using API requests.
tags:
    - academic-standards
    - api-navigation
    - hierarchical-data
    - data-faceting
    - rest-api
    - guid-filtering
category: guide
---

## How to Navigate the Standards Organizational Structure

Standards are organized hierarchically under *authorities*. An authority is an organization that has defined a set of academic Standards (e.g. Alabama DOE or NGA Center/CCSSO). Authorities have groups of Standards that we refer to as *publications*. Publications typically cover multiple subject areas. An example of a publication is New York's Next Generation Learning Standards. It covers both math and ELA. Within a publication, we organize Standards into *documents* based on subject and adoption year. So within New York's Next Generation Learning Standards, one of the documents is Mathematics 2017. Each document is organized into *sections*. A section is a group in the document that covers the Standards for a particular set - typically a grade (e.g. 2nd Grade) or course (e.g. Algebra II). Once you've gotten to the section level, the rest of the data is organized into a hierarchical structure of the Standards by level and are related by parent/child relationships. Let's walk through an example:

First, to retrieve a list of authorities in your license, use faceting and list the authorities (`document.publication.authorities`). E.g.:

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?facet=document.publication.authorities&limit=0&filter[standards]=status EQ 'active'`
```

The results from that call will include a set of authority facets in the `meta.facet` part of the JSON. For this example, let's look at the New York Standards.

```
    ...
    {
        "data": {
            "guid": "9127D390-F1B9-11E5-862E-0938DC287387",
            "acronym": null,
            "descr": "New York DOE"
        },
        "count": 20047
    },
    ....
```

Now that you have the GUID for the New York DOE authority, you can use that to narrow your focus to NY and request publications.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=(document.publication.authorities.guid EQ '9127D390-F1B9-11E5-862E-0938DC287387' AND status EQ 'active')&facet=document.publication&limit=0`
```

We'll pick the Next Generation Learning Standards and look at the documents.

```
    ...
    {
        "count": 2650,
        "data": {
            "title": "Next Generation Learning Standards",
            "acronym": null,
            "guid": "4D7B5584-9C82-11E7-8A3F-4EABBF03DF2F",
            "descr": "Next Generation Learning Standards"
        }
    },
    ...
```

Let's take that publication GUID and look for related documents.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=(document.publication.guid EQ '4D7B5584-9C82-11E7-8A3F-4EABBF03DF2F' AND status EQ 'active')&facet=document&limit=0`
```

Let's focus on the math document.

```
    ...
    {
        "count": 1300,
        "data": {
            "descr": "Mathematics",
            "adopt_year": "2017",
            "guid": "49C1ACA6-9CC6-11E7-8E55-D1F6CCC8CA83"
        }
    }
    ...
```

With the math document GUID, you can list the related sections.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=(document.guid EQ '49C1ACA6-9CC6-11E7-8E55-D1F6CCC8CA83')&facet=section&limit=0`
```

Let's look at the Algebra II section.

```
    ...
    {
        "count": 149,
        "data": {
            "guid": "48382382-9CC7-11E7-BC16-0295BF03DF2F",
            "descr": "Algebra II",
            "seq": 2430
        }
    },
    ...
```

Now we are ready to start to navigate the Standards. To start that process, look for Standards in the Algebra II section. The Standards are organized in a hierarchy but are not necessarily returned in that order so limit the response to the top level of the hierarchy and sort by the sequence so you are reproducing the section as a user would expect to see it. If you are using these calls to build a tree in a UI, you may want to request the `children` property be included in the response so your front-end code can decide whether or not to add an icon to allow the browser to expand this Standard to show its children. I'll leave it out of this example so I don't clutter the data response, but you could include that information using a fields parameter in the URL like: `fields[standards]=seq,number,statement,children`.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=(section.guid eq '6C23310C-6EC0-11DF-AB2D-366B9DFF4B22' and level eq 1)&sort[standards]=seq&fields[standards]=seq,number,statement,children`
```

We'll ignore data paging here and assume that you can manage that part. Looking at the results, there are only a couple of branches at this level. We've simplified the data here to make it easier to read:

```
    ...
    {
        "attributes": {
            "number": {
                "raw": "5.OA",
                "enhanced": "CCSS.Math.Content.5.OA",
                "prefix_enhanced": "CCSS.Math.Content.5.OA",
                "alternate": "5.OA"
            },
            "statement": {
                "addendums": [],
                "descr": "Operations and Algebraic Thinking",
                "combined_descr": "Operations and Algebraic Thinking"
            }
        },
        "id": "1D9D7C1A-7053-11DF-8EBF-BE719DFF4B22",
        "type": "standards"
    },
    {
        "type": "standards",
        "id": "1DACEABA-7053-11DF-8EBF-BE719DFF4B22",
        "attributes": {
            "statement": {
                "combined_descr": "Number and Operations in Base Ten",
                "descr": "Number and Operations in Base Ten",
                "addendums": []
            },
            "number": {
                "raw": "5.NBT",
                "enhanced": "CCSS.Math.Content.5.NBT",
                "prefix_enhanced": "CCSS.Math.Content.5.NBT",
                "alternate": "5.NBT"
            }
        }
    }
    ...
```

Now that we have the top level of Standards, we need to look at the children Standards. We'll start with the Operations and Algebraic Thinking branch and look for its children by searching for Standards that have this particular Standard as a parent. Again, we are sorting by the sequence order.

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?filter[standards]=(parent.id eq '1D9D7C1A-7053-11DF-8EBF-BE719DFF4B22')&sort[standards]=seq&fields[standards]=seq,number,statement,children`
```

The results look something like the data below (again simplifying the response for clarity).

```
    ...
    {
        "attributes": {
            "number": {
                "raw": null,
                "prefix_enhanced": "CCSS.Math.Content.5.OA.A",
                "enhanced": "CCSS.Math.Content.5.OA.A",
                "alternate": "5.OA.A"
            },
            "statement": {
                "combined_descr": "Write and interpret numerical expressions.",
                "addendums": [],
                "descr": "Write and interpret numerical expressions."
            }
        },
        "id": "1D9F7E02-7053-11DF-8EBF-BE719DFF4B22",
        "type": "standards"
    },
    {
        "attributes": {
            "number": {
                "prefix_enhanced": "CCSS.Math.Content.5.OA.B",
                "enhanced": "CCSS.Math.Content.5.OA.B",
                "raw": null,
                "alternate": "5.OA.B"
            },
            "statement": {
                "descr": "Analyze patterns and relationships.",
                "addendums": [],
                "combined_descr": "Analyze patterns and relationships."
            }
        },
        "id": "1DA6C82E-7053-11DF-8EBF-BE719DFF4B22",
        "type": "standards"
    }
    ...
```

Now you can repeat that process for each Standard in this list - searching for Standards that have each of these as parents - until you reach the bottom of the hierarchy. As you do this, there are a few things to keep in mind:

- Most documents are not consistent in the number of levels they have. The bottom level is often the level that represents a single learning objective but sometimes the bottom is an example and the level above is the objective.
- Check the `utilization.type` of a Standard to validate its usage. `alignable` Standards are the learning objectives. These typically have Key Ideas, Topics and Concepts associated with them.

## Special Considerations When Rendering Standards In User Interfaces

### Representing Standards As Chips

A common modern user interface element in selection scenarios is the "chip". A chip is a compact element that typically represents a more complex object in a tight space. If you are not familiar with chips, you can see examples on the [Material Design sitearrow-up-right](https://material.io/design/components/chips.html#input-chips). The dominant attribute of chips is compactness. For this reason, the representation of a Standard as a chip is challenging. We find that using the enhanced (or pre-fix enhanced) number is the best representation of a standard on a chip combined with hover text or an info icon to allow the user to easily find a more complete definition of the Standard.

Be aware that numbers are not guaranteed to be unique and some Standards do not have numbers. When working with Standards that aren't numbered, you may want to fallback to showing the first 10-15 characters of the text. While that is not likely to be too informative, when you combine it with the ability to see more details about the standard, it should be enough for a user to understand its usage.

### Handling Standards That Have Lists and Addenda

Standards with addenda with `position` set to `after` that have `has_list` set to `Y` are very rare, but they do occur periodically, and the rendering requires special treatment. In this case, addenda with `position` set to `after` should be displayed after the list of items. The final rendering is determined by your application, but here is an example and two likely renderings.

- Statement: Determine the equation of a linear relation, given:
  
  - Before Addendum: It is expected that students will:
  - After Addendum: to solve problems.
  - Child List Standards:
    
    - a point and the equation of a parallel or perpendicular line

## Working With Deleted Standards

Standards are occasionally deleted when the authority makes changes that impact the intent of the Standard. When this happens, the Standard is deleted and the related GUID is "retired" so the integrity of related alignments is not tarnished by a change in the intent of the Standard. You can still access these Standards via AB Connect but there are a couple of things to keep in mind:

- When looking up a standard by GUID (`https://api.abconnect.instructure.com/rest/v4.1/standards/<GUID>`), the system will respond with the standard regardless of whether it is deleted or not.
- When filtering Standards, deleted Standards are excluded from filter results unless the filter criteria explicitly includes Standards with `deleted` status. E.g. `status EQ 'deleted'` or `status IN ('active','deleted')`
- AB Connect tracks deleted Standards back to January 2008. Due to the evolution of the AB Connect data model, the amount of metadata available on deleted standards varies over time. Standards deleted in January 2008 have less metadata than modern standards.

## How To Populate Your Local Cache With AB Connect Data

Many AB Connect customers cache the data locally to support analytics and other operations that require performant combination of AB Connect data with local data. This article discusses the options for downloading that initial cache.

The first consideration is when your v4.1API access was enabled vs. when you became an Academic Benchmarks partner. If you are a new partner, the easiest approach is to implement use of the Events endpoint and start with `seq GT 0`. This will download all events as each document is added to your license and you can use these events to populate your local cache. See Using Events As A New Partner in the [Events documentation](https://developerdocs.instructure.com/services/ab-connect/reference/events) for more details.

However, if you were a partner before v4.1was enabled for your account (or you became a customer before November 2018), the initial events to add documents to your license don't exist. In that case, a common approach is to have your system [Navigate the Standards Organizational Structure](https://developerdocs.instructure.com/services/ab-connect/introduction/how-to#how-to-navigate-the-standards-organizational-structure) and cache the Standards as the system walks the structure.

## How To Efficiently Update Your Local Cache With The Latest AB Connect Data

Many Academic Benchmarks partners opt to take advantage of AB Connect's fast search architecture to directly power their system search, standards and alignment activities while others prefer to cache the data locally. If you cache data, AB Connect has solutions that make updates and workflows like alignment maintenance efficient.

Standards evolve over time. Authorities frequently make minor changes to individual standards and periodically adopt new documents that replace existing standards. When a new document is adopted, it may be added to your standards delivery. Either way, it is important that you keep your cache fresh. While it is possible to purge your cache and retrieve the entire set of Standards periodically, that is inefficient and does not support the maintenance of alignments and other related data. It is more efficient and useful to request differential updates. With AB Connect, you do this using the `events` endpoint. You can read more about Events and keeping your cache current in the section on the [Events endpoint](https://developerdocs.instructure.com/services/ab-connect/reference/events).

As standards evolve and your content library changes and expands, you will need to update your local storage of alignments. See the paragraph titled "Locating Recent Changes to Relationships Between Assets and Standards" in the [Managing and Predicting Relationships](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#managing-relationships-between-assets-and-standards%23creating-relationships) section for information on retrieving alignment changes.

If AB Connect is the system of truth for your content's metadata profiles, you can update your cache by locating and retrieving modified Assets. The following filter returns assets updated since September 2018.

```
  /assets?filter[assets]=(date_modified_utc gt '2018-09-12 12:00:00')
```

## How To Map Alignments From One Document To Another

Content publishers often partner with Academic Benchmarks as they expand their offerings by bringing content to new market segments and geographies through alignment to new standards. With such expansion, many publishers experience the challenge of aligning content and maintaining alignments across multiple states and authorities. AB Connect offers a wide array of metadata and functionality to assist. There are a couple of approaches you can take using AB Connect to address this challenge.

AB Connect includes standards relationships, which allow publishers to leverage existing standards alignments and expedite alignment of content from one authority to another, or across multiple states and markets segments. The advantage of this approach is a degree of automation that can drastically reduce the number of correlations that need to be hand reviewed.

Some standards documents have direct relationships to other documents - either historical (2021 document replaces the 2017 document) or from other authorities (a state derives its standards from the Common Core). For documents without a data relationship or a state published relationship to other standards, Academic Benchmarks subject matter experts curate a crosswalk relationship. E.g. Texas standards are not related to the Common Core. Academic Benchmarks curates relationships between various documents and captures the relationships in the Crosswalks field.

Standards related as Crosswalks share at least one skill. Crosswalks are based on close relationships where they are established by the authority and hand curation where they are not. Not all documents are directly crosswalked to every other document. At the time of the writing of this documentation, math, science and ELA in the US should all be mapped to at least one common document but the scope of coverage in subjects and regions will continue to expand. You can use the `predictions` endpoint to help get Crosswalks between documents that are not directly connected. See [Generating Predictions](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#generating-predictions) for details.

Note that Crosswalks are not available on all accounts. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to Crosswalks.

If your content is aligned to a national document, you can use the Derivatives Relationship on the national standards to locate standards in a derived document - E.g. Common Core Math to California Common Core Content Standards.

Derivatives carry two key pieces of metadata to assist with automation: "same text" and "same Concepts." The former is true ("Y" in the API data model) if the standard in the national document is character for character the same as the standard in the derived document. The latter is true if the standard in the national document covers the same concepts. Derivatives with the same text and concepts can typically be automatically mapped to content. Most organizations automatically map derivatives with same concepts as well, but we recommend making that decision in coordination with your editorial team.

Notes:

- In many cases, an authority will clearly state that their Standards are derived from a national document but in cases where they disclaim derivation but are very closely modeled after the national document, AB Connect still exposes derivative relationships.
- While a Standard will often have a 1:1 mapping with a Standard in a derived state, it is possible that there are multiple Standards derived from the single national Standard. This typically happens when a state breaks out a compound Standard into multiple, more specific Standards.
- There are relationships where the Standards have the same text but same Concepts is N. This occurs when a state has limited or otherwise changed the intent of the Standard through verbiage found in the hierarchical parentage of the Standard.

If your content is aligned to a derived document and you want to map to the national document, the Origins Relationship helps you do that - E.g. Georgia Standards of Excellence ELA to Common Core ELA. It is the inverse of the derivatives relationship. The approach and metadata are the same as that described above in the Derivatives section. Note that just as there may be multiple standards derived from one national standard, it is possible that a derived standard is a combination of multiple origin standards.

If your content is aligned to a derived document and you want to map to another state document derived from the same origin, you can use the Peer Derivatives Relationship. Peer derivatives are related through a common Origin Standard. An example of this relationship includes two states that have adopted the Common Core State Standards. The approach and metadata are largely the same as that of origins and derivatives but there is one caveat: the "same text" and "same concepts" metadata on the peer derivatives is with respect to the origin - not the standard you are starting from. In order to be confident that the existing alignment equates with an alignment to the new destination, both the origin AND the peer derivative same text (and/or same concepts) flags should be true. If the origin same text is Y but the peer derivative is N, then the text of the Standard you are starting with is not the same as the text of the peer derivative.

Derivatives, origins and peer derivatives are great where they exist, but how do you handle mapping alignments to non-derived authorities (e.g. Common Core to Texas) or where there is no derivative, origin or peer derivative in the destination document? Two additional relationships are provided between these documents: Peers and Crosswalks. This section gives an overview of Peers. See the above section for more details on Crosswalks.

Peers are standards that are related through alignments to common educational resources. These standards are crowd sourced from curated, targeted, resources. Due to the nature of peers, editorial staff typically review the system suggestions for applicability for their specific use case.

Note that peer relationships are strongest with math and ELA. They also offer relatively good coverage for science (grades 3-12) and some limited coverage for social studies (grades 6-12).

Where no other relationships yield good results, use Topics to casts a broad net and identify standards covering the same general topic in the desired document. This is a two-step process where you get the list of Topics a standard is related to and then look for standards in the destination state related to one or more of those Topics. Topics cover multiple grades, so you may want to add grade filtering when looking for similar standards.

Topics offer the loosest of the relationships and is good for identifying Standards that editorial staff may want to consider when other relationships don't provide more specific suggestions. Topics are available for the core 4 subject areas.

Academic Benchmarks has developed example application that can help accelerate the integration of relationships into your system and processes. See the [Standards Relationship Browser](https://developerdocs.instructure.com/services/ab-connect/introduction/examples#standards-relationships-browser) and [Standards Relationship Report generator](https://developerdocs.instructure.com/services/ab-connect/introduction/examples#standards-relationships-report) in our [Examples](https://developerdocs.instructure.com/services/ab-connect/introduction/examples) section. They include code samples that can be downloaded from the AB Connect repository and used as a starting point for your implementation.

1. In many instances the Standard in question does not have an exact match in the destination state. Since using relationships does not take the specifics of the content under consideration, your degree of automation is limited. Where there aren't exact matches, editorial staff will need to review system suggestions. With fewer and fewer states adhering to the Common Core, you may find that this isn't the most efficient approach for your team.
2. Content alignment is not a once and done situation. Standards are constantly evolving. Sometimes Standards within an existing document change. Other times the entire document is replaced by a new version. A one-time mapping using relationships doesn't address the maintenance of alignments over time.
3. Relationships tend to be strongest and most prevalent with ELA, math and science. Topics have good coverage of social studies.
4. Peer relationships are limited to authorities in the US.
5. Crosswalk relationships are currently focused on authorities in the US with limited support in other regions.

### Tagging Content and Recommending Relationships

While using relationships to move from one document to another is relatively easy and efficient, at the end of the process you only have one more document's worth of alignments. As you expand your perspective to additional documents, as well as changes over time, you'll need to repeat this process. As you approach alignments across many authorities at one time, however, our robust machine-learning powered recommendation engine that uses your previous decisions to inform predictions can set you up to handle changes over time with a more holistic approach to alignment.

To assist, Academic Benchmarks created a recommendation engine that uses metadata descriptions of content to recommend alignments. In AB Connect, the content is represented by an Asset object and the metadata description is often referred to as an Asset profile.

Using either the API with a user interface in your system or AB Connect's alignment web solution, aligners describe content by tagging it with standards and education search terms. The recommendation engine uses the profile to make recommendations for additional standards.

While this approach takes more upfront effort from aligners to describe the content, it has several distinct advantages:

1. It works across all authorities and most subjects.
2. The engine updates recommendations as Standards are changed and new Standards become available easing long term maintenance.
3. Recommendations are made in the context of the specific content. The process of using relationships ignores the subtlety of the content description and errors can drift into alignments.

## How To Offer Your Partners Advanced Discovery Of Your Assets

AB Connect can be a powerful solution for interoperability challenges between systems exchanging content. It is possible to share Assets with other AB Connect customers (referred to as Providers). The Provider who owns the Assets is referred to as the Owner. Providers that can search and read the Asset metadata profile are referred to as Consumers. When access is shared, the Consumer can use AB Connect to include the Owner's Assets in their search results and retrieve the Asset descriptions to power activities like displaying alignment information and finding related content. For example, if you are a Learning Management System (LMS) and have purchased lesson plans from one Provider and assessment questions from another, you can use AB Connect to search the lesson repository, retrieve the description of the plan and look for related questions in the assessment repository (Assets that cover the same Standards and Concepts as the lesson). This capability is facilitated using the Providers resource as well as the Owner property on the Assets. To share your Assets with other Providers, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Asset%20Sharing). We can configure the sharing for you.

When using AB Connect for interoperability, you don't need to be concerned about the AB license status of your partners. AB Connect automatically handles the Consumer's licensing and only shares data with them that they have been licensed for. This is true for reading the Asset data as well as searching. E.g. if you are using Concepts in your Asset description, a Consumer that is only licensed for Standards will not be able to include Concepts in their search criteria. Similarly, if you are only licensed for Standards, Consumers of your Assets will not be able to find them using Concepts (or Topics) because your Asset descriptions will not include Concepts (or Topics).

See the `owner` property in the section on [Assets](https://developerdocs.instructure.com/services/ab-connect/reference/assets#searching-for-assets) for details on searching by owner.

## Exchanging Alignment Data With Partners

A common need in the industry is to exchange alignment and taxonomic metadata with partners to support reporting and discoverability. E.g. a school district purchases lessons from a provider. An administrator at the district imports the lesson into their LMS. While the lesson data is enough to run the lesson, alignment and taxonomies are required in order to support full discovery of the plans and analytics of the lesson usage.

What's the best way to share the content metadata with your partners?

### Recommendation: AB Connect's Owner/Consumer Capability

AB Connect allows you (the Owner) to share your content's description (Asset metadata profile) with your partners (Consumers). The Consumers can retrieve your Asset's metadata directly from AB Connect using the AB Asset GUID. This approach has several advantages:

1. It is concise. One GUID is exchanged with your payload and it conveys the complete Asset metadata profile.
2. Alignments and other descriptive metadata change over time. New Standards documents are published. Alignments are adjusted. Standards are deleted. Concepts and Topics are added to the description. Exchanging the Asset GUID allows the Consumer to refresh the Asset profile dynamically.
3. Your AB Connect license is likely not the same as your partner's license. If you send them AB GUIDs that are not in their license, it is a violation of the license agreement and confusing for the recipient since they won't have matching data on their end. If you exchange data using the Asset profile, AB Connect filters the Consumer's view of the Asset to match their license.
4. Using this approach also enables your partners to search your Assets via AB Connect using the full Asset metadata profile. See the [section above on Advanced Discovery](https://developerdocs.instructure.com/services/ab-connect/introduction/how-to#how-to-share-alignments-with-your-partners-and-offer-them-advanced-discovery-of-your-assets) for more information on this advantage.

To setup your account to share your Asset descriptions with your partners, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29).

#### Exchanging The Asset GUID Via The Common Cartridge, Thin Common Cartridge, LTI or QTI

The taxonomic classification property in the LOM section of the manifest is a convenient place to pass the AB Asset GUID. As you can see in the example below, the GUID can be exchanged as a taxonomy entry using the source name `AcademicBenchmarksAssetGUID`.

For example:

```
  ...
    <metadata>
      ...
      <lom xmlns="http://ltsc.ieee.org/xsd/LOM">
        ...
        <classification>
          <purpose>
            <source>LOMv1.0</source>
            <value>discipline</value>
          </purpose>
          <taxonPath>
            <source>
              <string xml:lang="en">AcademicBenchmarksAssetGUID</string>
            </source>
            <taxon>
              <entry>
                <string xml:lang="en">7E80697A-7440-11DF-93FA-01FD9CFF4B22</string>
              </entry>
            </taxon>
          </taxonPath>
          ...
        </classification>
        ...
      </lom>
      ...
    </metadata>
  ...
```

While using the Asset GUID to exchange metadata with your partners is a better approach, there may be situations where you are limited to passing Standard GUIDs to a partner. The following sections outline how to include AB GUIDs in your payload.

#### Exchanging AB Standards GUIDs Via Learnosity

Learnosity has integrated directly with AB Connect. [This section of their documentationarrow-up-right](https://help.learnosity.com/hc/en-us/sections/360001598818-Academic-Benchmarks) describes their implementation and how to configure Learnosity to work with AB for your content. While you can use custom tags in Learnosity to store your AB GUIDs with any tag name you'd like, to maximize compatibility with Learnosity's integration with AB Connect, we recommend you use the tag name `lrn_ab_aligned`. Following the Learnosity API documentation on setting tags, the tags portion of the payload might look like:

```
  ...
  {
      "tags": [
          {
              "type": "lrn_ab_aligned",
              "name": "000DD508-29E9-11D8-8162-F2F2B6C137B9"
          },
          {
              "type": "lrn_ab_aligned",
              "name": "000b4dc7-adfc-46be-b72a-7a0ed91601fa"
          },
          {
              "type": "lrn_ab_aligned",
              "name": "00109D60-29E9-11D8-A8C1-FD5D7E873ABE"
          }
      ]
  }
  ...
```

**References**

#### Exchanging AB Standard GUIDs Via Ed-Fi

The Ed-Fi data model supports the tagging of assessment items with AB Standards GUIDs. In the Ed-Fi model, they are referred to as `LearningStandards` and the AB GUID is stored as the `LearningStandardId`.

Note that the Ed-Fi ODS will typically only house standards for the given education agency and any related origin standards that they are derived from. You will be unable to add alignments to standards in other states/districts.

**References**

#### Exchanging AB Standards GUIDs Via The Common Cartridge, Thin Common Cartridge, LTI or QTI

IMS Global has a data element to help support the transmission of related Standards data. There does not appear to be a single page on the IMS site that concisely describes the exchange with explanations and examples, so we'll summarize it here.

**Recommended Representation**

The `curriculumStandardsMetadata` object has one optional property `providerId`. Per the IMS Global GUID registry the Academic Benchmarks provider ID is "**AB**".

The `setOfGUIDs` object has optional properties `region` and `version`. In spite of the inappropriate use of the phrase `region`, it is our recommendation that providers use the authority description (`document.publication.authorities[0].descr`) for this field. We'd recommend supplying the document adoption year (`document.adopt_year`) for the `version` and create a new `setOfGUIDs` for each document for which they are supplying Standards.

The `setOfGUIDs` body consists of repeated `labelledGUID` objects. That object consists of an optional `label` element and a required `GUID` element.

For example:

```
  ...
    <metadata>
      <curriculumStandardsMetadataSet xmlns=/xsd/imscsmetadata_v1p0>
        <curriculumStandardsMetadata providerId="AB">
          <setOfGUIDs region="NGA Center/CCSSO" version="2010">
            <labelledGUID>
               <GUID>7E80697A-7440-11DF-93FA-01FD9CFF4B22</GUID>
            </labelledGUID>
            <labelledGUID>
               <GUID>7E7EF798-7440-11DF-93FA-01FD9CFF4B22</GUID>
             </labelledGUID>
          </setOfGUIDs>
        </curriculumStandardsMetadata>
      </curriculumStandardsMetadataSet>
    </metadata>
  ...
```

**References**

#### Handling Problems Consuming Alignments From A Partner

In some situations, the consumer of alignment data may have difficulties resolving AB GUIDs they receive in a payload. The difficulties arise from two sources: stale partner caches of AB data and license differences. Both of these issues are addressed when using the API and using the Asset GUID as a means to exchange data. However, if you are exchanging individual Standards GUIDs, here are some tips:

1. If you receive a GUID that you don't recognize, it is either because it isn't a valid AB GUID, you aren't licensed for that particular GUID (e.g. it may be in a state or subject you haven't licensed), your cache is out of date or your partner's cache is out of date.
2. If you cache data, try refreshing your cache or call the API to retrieve that specific GUID. If your cache is stale and the GUID is new, the problem should be resolved. One alternative solution is to always use the API directly rather than cache data so you don't have to worry about a stale cache.
3. If your cache is up to date or you use the API dynamically, your partner may have a stale cache. In that case, the GUID they passed you may no longer be active. If you request the Standard by GUID from the API, even deleted Standards will be returned. You can check the Standard's status to confirm that it has been deleted.
4. Regardless of whether you cache data or not, if you aren't licensed for a GUID your partner passed to you, you won't be able to access it. However, you can verify this (and determine which additional units you may want to license) by requesting the Standard by GUID from the API. If it is a valid GUID but you aren't licensed for it, the API will respond with a 403. The error payload will include information that will help you work with [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) to add it to your license.
5. If requesting the Standard by GUID from the API doesn't resolve the issue, the GUID your partner passed is not a valid AB GUID. Contact your partner to help resolve the issue.

In addition to traditional Standards, some authorities provide course definitions that are groups of Standards defined elsewhere but combined separately into a course. Course definitions are captured into publications where the `publication_type` is set to `course`. Those are special publications where the top level of Standards represent courses. The Standards that must be covered in the course are available in the `course_standards` relationship on the Standard. So, for example, to see the Standards that comprise the Florida CPALMS Language Arts - Kindergarten (#5010041) course, you would use the falling call:

```
  /rest/v4.1/standards/2FADED92-647D-4183-89C1-17F28CF065ED?fields[standards]=statement,number,section,course_standards&include=course_standards
```

The `related_courses` relationship points in the opposite direction, so you can get a list of courses that a Standard is used in by examining the `related_courses` relationship. Since `related_courses` points in the opposite direction of `course_standards`, an alternative call to the one above that returns the same data would be:

```
  /rest/v4.1/standards?filter[standards]=related_courses.id eq '2FADED92-647D-4183-89C1-17F28CF065ED&fields[standards]=number,statement,section'
```

Or you could use a call like the following to get information on all of the courses that reference a standard:

```
  /rest/v4.1/standards/C3B5C384-E1BF-11DC-A10B-B5479DFF4B22?fields[standards]=statement,number,section,related_courses&include=related_courses
```

## Managing Alignments as Standards Evolve

From time to time, authorities edit their Standards and make minor or major changes. Minor changes are often reflected as change events on Standards but they can also result in the deleting of one Standard and a creation of another. This typically happens when the modification of the Standard is significant enough that it would impact alignments. In this case, the old GUID is retired and a new one to represent the new Standard is created. Major changes come in the form of new documents that replace all of the standards in older documents.

AB Connect offers a couple of solutions to help you manage your alignments as changes occur. One approach is to use AB Connect's prediction algorithms which maintain alignments based on the content description rather than fixed relationships with specific standards. This requires little to no extra work as alignments change. Another approach is to use the Standards relationships available in AB Connect. AB Connect supplies maps from outdated Standards to their replacements. We often refer to these as migration maps. These maps are exposed in the `replaces` and `replaced_by` relationships on the Standards. The `replaced_by` relationship points forward from outdated Standards to their replacements. The `replaces` relationship points backwards from the new Standards.

If you would like to use the prediction algorithms to maintain alignments, see the section on [Managing and Predicting Relationships](https://developerdocs.instructure.com/services/ab-connect/reference/relationships#managing-relationships-between-assets-and-standards/creating-relationships). If you would prefer to use the migration maps, the first step in the process would be to identify which workflow will work best for your organization. There are two general approaches that can be taken: starting with Standards or starting with Assets.

You may want to start with Standards if you have a local cache and use the `events` endpoint to sync the cache. In this case, you would get notifications for Standards that have been deleted or new documents that are available. You may have a different process for determining which new Standards you need to migrate alignments to or which old Standards you need to update. But whatever the approach, you start with a list of either outdated Standards or new Standards and you need to update alignments to ensure they are current.

If you are starting with a deleted or outdated Standard, the first step is to locate its replacement(s)(their may be more than one replacement). You can use the `replaces` relationship to search for standards that replace the Standard in question. E.g.

```
  /rest/v4.1/standards?filter[standards]=replaces.id eq '0011921D-A923-435C-985F-FBB3C810E735'
```

You can combine search criteria if you need to narrow the focus. For example, you can add document GUIDs to look for replacements in the same document when an individual Standard has been deleted.

The example above returns standard `A34FE67F-9AEB-4A04-B14C-59BAE6A6404C` which is NOT a "same concept" match. In this case, the interpretation of the applicability of the new Standards to the alignment may need to be reviewed by an aligner.

If you are only interested in exact concept matches, you can add that as a criteria. E.g.

```
  /rest/v4.1/standards?filter[standards]=replaces.id eq '00CAA27E-AF8B-4385-AC22-285B911685B5' and replaces.same_concepts eq Y
```

But what about when a new document is added? How do you determine which Standards are being outdated? You can reverse the search direction. E.g. You know South Dakota released their 2018 English Language Arts Standards but you are currently aligned to the 2010 Standards. Where do you start? Grab a Standard from the 2018 document and either look at its `replaces` list or search for Standards in the 2010 document that are replaced by the Standard you are focusing on. We'll do the latter here because it is more interesting.

```
  /rest/v4.1/standards?filter[standards]=replaced_by.id eq '8CB54468-0F56-4767-95DE-6D684CC9244F' and document.guid eq 'E1C9B054-DA22-11E2-95B3-3B359DFF4B22'
```

Here you'll get `00000CD0-D9E7-11E2-BBB0-00249DFF4B22`. If you examine the relationship metadata you'll notice that they have the same concepts but not exact same wording.

Once you have the Standard that is being replaced and the Standard that is replacing it, the next step is to identify which Assets will need to be re-aligned. To locate Assets aligned to an outdated Standard (e.g. `0011921D-A923-435C-985F-FBB3C810E735`), you can use a call like:

```
  /rest/v4.1/assets?filter[assets]=alignments.id eq '00000CD0-D9E7-11E2-BBB0-00249DFF4B22'
```

How you update the alignments is dependent on your editorial processes. E.g. can you automatically migrate alignments to new Standards as long as they have the same concepts? Or do you require the same text? What if the text is the same but the Standard moved to a new grade? These are questions that the editorial staff has already answered but they will need to be codified and applied to any automation you build.

Now let's flip that over. Rather than tightly monitor Standards, some organizations prefer a periodic review of their content alignments. In this case, you start with the Assets and look for alignments that need to be updated.

It is easy to locate Asset alignments to deleted standards. For a given Asset, you can find alignments to deleted standards using a call like:

```
  /rest/v4.1/assets/02213D12-0A8A-11E8-AA1B-EB8924FEA1B3/alignments?filter[alignments]=status eq 'deleted' and meta.disposition eq 'accepted'
```

Here we only search for Standards that are marked as `accepted`. There is no need to update `rejected` alignments and `predicted` alignments are automatically updated on the next snapshot (POST a set of predictions to the Asset).

Determining what alignments an Asset should have to new documents isn't possible directly from the Asset itself without using the alignment prediction functionality or examining the Standards (or at least documents) involved. So to add alignments to new documents, either use predictions, combine your asset centric approach with the Standards approach mentioned above or start with something like an alignment gap report.

One search you may find helpful is locating all Assets aligned to an older version of a document. So using the example that we used in the Standards centric approach above, the older document is South Dakota's 2010 Language Arts Standards (`E1C9B054-DA22-11E2-95B3-3B359DFF4B22`). To locate Assets that are good candidates for alignment to the 2018 document, use a call similar to:

```
  /rest/v4.1/assets?filter[assets]=standards.document.guid eq 'E1C9B054-DA22-11E2-95B3-3B359DFF4B22'
```

## Optimizing Use of AB Connect

When working with APIs, it's important to keep performance optimized. There are a few basic practices that can ensure top performance when working with AB Connect.

Calculating facets can be time consuming. Custom attributes on Assets can be particularly challenging as they may have unique values which will significantly impact performance. Only facet properties you need and avoid facetting properties that have unique values.

Another source of processing and network waste is the processing and returning large quantities of unused fields. We recommend using the `fields` parameter to request only the specific fields required for each call. Use `fields[]=*` only for discovery during programming. To ensure the use of wildcards with the `fields` parameter does not impact overall system performance, such calls are throttled to 2 per second.

### Request Only What You Need, Only When You Need It

Using sparse fieldsets and minimizing facet requests are simple changes that can have significant impact on the response times of calls, but the design of the your system's interaction with the API may have a larger impact.

It's tempting to make few calls and pull more data per call because you may need it. While this seems efficient on the surface, it can actually have notable impact on the overall API experience - particularly for user interfaces. In practice, it is typically more efficient and more interactive to make multiple calls and request only enough data to meet the immediate need.

Several examples:

One common mistake is to attempt to load a large set of Standards to populate a tree or set of drop-downs. This could take many seconds depending on whether you are loading a section, document or publication. A best practice is to lazy load the UI and request just enough information to show the user what they requested. The AB Connect Standards browser uses this approach for a very efficient interactive experience.

Another common scenario is searching for Assets and alignments. It is tempting to show all results or load large pages of Assets but this can result in a slow user experience and users don't typically scroll through large sets of data. It is better to show them a small page of results quickly and allow them to refine their search or page/infinite scroll the results.

#### Showing Appropriate Amount Of Information

It is tempting to show a lot of data in your search results but not only can this slow API response times but can clutter the user interface making it difficult to digest and navigate. Avoid things like attempting to show large quantities of properties or alignments in Asset search results. It's better to have a list or tiles with a simple title, perhaps a brief description, subject and grade. The user can use faceting to further narrow results and if they need details they drill down into the individual Asset to see things like alignments, concepts, etc.

Another common source of waste is retrieving and exposing irrelevant data to your users. If your user is an 8th grade math teacher from California, don't force them to select 8th grade math when searching for content. When displaying alignments, limit your queries to 8th grade math Standards in California. This will significantly reduce the data the system is processing and will speed up the response times.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).