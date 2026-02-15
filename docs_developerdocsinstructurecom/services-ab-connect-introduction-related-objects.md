---
title: Working with Related Object | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/related-objects
source: sitemap
fetched_at: 2026-02-15T09:04:00.877297-03:00
rendered_js: false
word_count: 2000
summary: This document explains how to work with resource relationships in the AB Connect API, detailing how to access meta properties, handle pagination, and use the include parameter.
tags:
    - ab-connect
    - json-api
    - api-relationships
    - data-pagination
    - filtering-syntax
    - meta-properties
category: guide
---

While the definition of a Standard or Topic can be helpful in adding value to your system, there is a lot of power in the relationships available in AB Connect. E.g. The Topics covered by a Standard are represented by a relationship between the Standard and one or more Topics. Assets are related to Standards when they are aligned. Standards are related to other Standards (like Peers).

AB Connect exposes these relationships via the `data.relationships` property. This section explains how to access the power of these relationships.

Some relationships in AB Connect have properties. E.g. Relationships between Assets and Standards have a disposition, prediction score, dates, etc. These properties are represented in the JSON as meta properties on the relationship. AB Connect allows you to address the relationship meta properties for use in either [fields statements](https://developerdocs.instructure.com/services/ab-connect/introduction/requesting-additional-properties) or [filter statements](https://developerdocs.instructure.com/services/ab-connect/introduction/introduction-to-odata-filters). When referencing these properties, include `meta.` as part of the property path. E.g. `fields[assets]=alignments.meta.date_created_utc`

Resources can have many related objects - sometimes thousands. In order to maintain system performance, AB Connect limits the number of related objects that are returned when requesting a resource. Use paging on the relationship endpoint to retrieve more (or all) of the related objects.

Some relationships have limited cardinality. E.g. a Standard can have zero or one "parent". Other relationships are not limited but commonly have a small set of related entities. E.g. a Standard typically has a handful of Concepts, however in some extreme situations a Standard may have 50 Concepts. To optimize transmissions, AB Connect will return up to the first 25 related objects but if there are more than 25 related objects, AB Connect returns the first 10 relationships with paging URLs. Note that neither the page size (`limit`) nor the `offset` can be changed at this point - but can be changed on the relationship endpoint.

Here is an example of a response showing a Standard's related Peers and the paging URLs to retrieve more peer data. To get this data, you might make a call like:

```
`https://api.abconnect.instructure.com/rest/v4.1/standards?fields[standards]=peers,statement,number&filter[standards]=not isempty(peers) and utilizations.type eq alignable&include=peers`
```

```
    ...
    {
        "id": "00003506-B001-11DA-93BA-9A7258581090",
        "type": "standards",
        "relationships": {
            "peers": {
                "data": [
                    {
                        "type": "standards",
                        "id": "665CDF54-29E7-11D8-9805-987DA0705AD0"
                    },
                    {
                        "id": "BA13F3EA-29EB-11D8-9212-963E918BB192",
                        "type": "standards"
                    },
                    ...
                    {
                        "type": "standards",
                        "id": "6573F63E-D88E-11D9-8407-9AE6FB2C8371"
                    }
                ],
                "links": {
                    "related": "https://api.abconnect.instructure.com/rest/v4.1/standards/00003506-B001-11DA-93BA-9A7258581090/peers",
                    "next": "https://api.abconnect.instructure.com/rest/v4.1/standards/00003506-B001-11DA-93BA-9A7258581090/peers?offset=10",
                    "last": "https://api.abconnect.instructure.com/rest/v4.1/standards/00003506-B001-11DA-93BA-9A7258581090/peers?offset=80"
                }
            }
        }
    },
    ...
```

To load the next page of Peers related to the Standard (00003506-B001-11DA-93BA-9A7258581090), follow the `next` URL:

`https://api.abconnect.instructure.com/rest/v4.1/standards/00003506-B001-11DA-93BA-9A7258581090/peers?offset=10&fields[standards]=statement,number`

- The data available on the relationship endpoints is a conflation between the related object (attributes and relationships) and the relationship properties (meta).
- Objects returned on the relationship endpoint do not support accessing *their* relationships nor including the further related data. For example, when viewing an Asset, you can see the alignments for that Asset, include related aligned Standards and page through the alignments at the relationship endpoint (assets/GUID/alignments). However, when you are viewing the properties of the aligned Standards on the alignment endpoint (assets/GUID/alignments), you can not include peers to those alignments nor can you page the peer standards. If you need to dig deeper into the aligned standards, you must request the data via the Standards endpoint.

The JSON API standard supports an `include` argument in the query string. The value of the `include` argument is a comma separated list of relationships on the specified endpoint. If the `include` statement appears in the query string, the resources returned in the `relationships` section and named in the statement are included in the response. This helps the caller avoid a second set of calls to retrieve the object details.

Note that it is important that you specify the **relationship** name in the `include` statement rather than the object type. For example, when retrieving Standards there are a number of relationships that are available: `parent`, `ancestors`, `children`, `derivatives`, `origins`, etc. Most of them are relationships to other Standards. If you asked the system to include "standards", it would not know which set you are actually requesting. You must explicitly request `children` (for example).

The generic form of the statement is:

```
`<endpoint URI>?include=<CSV list of relationships>`
```

For example:

```
`https://api.abconnect.instructure.com/rest/v4.1/topics/2CED2B98-4FD7-11E0-964D-6C069DFF4B22?fields[topics]=standards&include=standards`
```

Will return the details of the Standards related to the requested Topic.

- If you include a relationship that does not appear in the request as a "relationship" by being included through the fields argument then the include block will be left out of the response.
  
  - E.g. `https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22?include=ancestors` will **NOT** return the `ancestors` resources because that relationship is not delivered.
  - E.g. `https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22?fields[standards]=ancestors&include=ancestors` will have the `ancestors` listed in the relationships and their details in the `included` block

Sometimes it is convenient to filter the objects that are returned in the relationship. Meta properties on the relationship can always be used in filtering related objects. However, there are some scenarios where it is helpful to filter the related objects on key properties. E.g. one may only be interested in California Standards aligned to an Asset. To implement filtering related objects on all properties presents architectural challenges so to strike a balance and facilitate common use cases, AB Connect allows the caller to filter related object on specific properties on certain relationships.

When filtering on related objects, use the *relationship* name in the filter statement. E.g.

```
https://api.abconnect.instructure.com/rest/v4.1/assets?filter[assets]=disciplines.subjects.code eq 'MATH'&filter[alignments]=document.publication.authorities.guid eq '912830F6-F1B9-11E5-862E-0938DC287387' AND meta.date_created_utc gt '2020-03-12'
```

Will return math Assets and the `alignments` relationship for each Asset will only include Texas Standards aligned after March 12th 2020.

### Filtering Objects Related to Assets

This section describes properties that can be be used when filtering objects related to the Asset.

When filtering aligned Standards, use the *relationship* name in the filter statement. E.g.

```
...&filter[alignments]=document.publication.authorities.guid eq '912830F6-F1B9-11E5-862E-0938DC287387'&...
```

Supported properties include:

- `disciplines.subjects.descr`
- `disciplines.subjects.guid`
- `document.publication.descr`
- `document.publication.guid`
- `document.publication.authorities.descr`
- `document.publication.authorities.guid`
- `document.publication.regions.descr`
- `document.publication.regions.guid`
- `education_levels.grades.descr`
- `education_levels.grades.guid`

Notes:

- `deleted_alignments` are filterable in a similar fashion as `alignments`.
- You can use any of the "meta" properties on the relationship in the filtering - e.g. `meta.score`, `meta.tags`, etc. See the relationship definition for a complete list of meta properties.

Only data associated with accepted and predicted Topics are filterable. Filtering on Topics properties will not return any rejected Topics. The only supported property is the Topic description.

Note that the relationship and type of Topics is the same in this instance:

```
...&filter[topics]=query(descr,'square')&...
```

Only data associated with central and relevant Concepts are filterable. Filtering on Concept properties will not return any not\_applicable or avoid Concepts. The only supported properties are the Concept description and context.

Note that the relationship and type of Concepts is the same in this instance:

```
...&filter[concepts]=query(descr,'square') AND query(context,'exponents')&...
```

### Filtering Concepts Related to Standards

When retrieving Concepts related to a Standard, you can filter the list on context and description.

```
...&filter[concepts]=query(descr,'square') AND query(context,'exponents')&...
```

One common need is to search across object relationships - for example, search for Assets based on properties of related Standards. Since this is a common need, AB Connect supports searching Assets based on key properties of related entities. E.g.

```
`filter[assets]=(alignments.document.publication.authorities.descr eq 'California DOE')`
```

This will return Assets aligned to Standards in California. This can be combined with other properties on the Asset or related entities. E.g. to find Assets related to California Standards on a particular Topic

```
`filter[assets]=(alignments.document.publication.authorities.descr eq 'California DOE' and alignments.topics.descr eq 'Exponents and Roots')`
```

And combining that with Asset properties...

```
`filter[assets]=(alignments.document.publication.authorities.descr eq 'California DOE' and alignments.topics.descr eq 'Exponents and Roots' and education_levels.grades.code eq '8')`
```

The text fields on the related entities are also indexed with the Asset full text search. This strengthens the Asset full text search in two ways.

1. When searching Assets for a key word or phrase, the engine will respond with Assets that are associated with that word or phrase through relationships and not just with the Asset properties.
2. Full text search results include the text of related entities when ranking results. E.g. If an Asset is related to multiple Concepts, Topics or Standards that contain the word "triangle" it will appear higher in the search results than an Asset that only mentions the word in a text field or has a few related entities that contain "triangle".

The following list shows related entity properties that can be included in an Asset search:

- Standards
  
  - `alignments.concepts.context` - this field is also included in full text searches once for each Standard that has this Concept in a Key Idea
  - `alignments.concepts.descr` - this field is also included in full text searches once for each Standard that has this Concept in a Key Idea
  - `alignments.document.disciplines.subjects.descr`
  - `alignments.document.disciplines.subjects.guid`
  - `alignments.document.descr` - this field is also included in full text searches
  - `alignments.document.publication.descr` - this field is also included in full text searches
  - `alignments.document.publication.guid`
  - `alignments.document.publication.authorities.descr`
  - `alignments.document.publication.authorities.guid`
  - `alignments.document.publication.regions.descr`
  - `alignments.document.publication.regions.guid`
  - `alignments.education_levels.grades.descr`
  - `alignments.education_levels.grades.guid`
  - `alignments.number.enhanced`
  - `alignments.number.prefix_enhanced`
  - `alignments.section.descr` - this field is also included in full text searches
  - `alignments.statement.descr` - this field is also included in full text searches
  - `alignments.topics.descr` - this field is also included in full text searches once for each Standard that covers this Topic
- Topics - Only data associated with accepted and predicted Topics are searchable on the Asset
  
  - `topics.descr` - this field is also included in full text searches
- Concepts - Only data associated with central and relevant Concepts are searchable on the Asset
  
  - `concepts.context` - this field is also included in full text searches
  - `concepts.descr` - this field is also included in full text searches

Notes:

- Assets can be filtered by `deleted_alignments` properties in a similar fashion as `alignments`, however, no `deleted_alignments` properties are included in an Asset's full text search.
- The Academic Benchmarks Topics and Concepts are licensed separately. See the section on [Licensing Considerations](https://developerdocs.instructure.com/services/ab-connect/introduction/licensing) for a discussion on the licensing required for access to those taxonomies.

It is also possible to search on the properties of the relationship between Assets and entities with simple relationships to Assets (Standards, Topics, Concepts, etc.). In order to do that, address the relationship properties as if they were properties on the related entity itself. E.g. you can filter on accepted Standards with `alignments.meta.disposition eq 'accepted'`. To search for Assets that have accepted relationships with a specific standard, your filter statement will look like:

```
`filter[assets]=(alignments.id eq '0029A5C3-3C0C-4127-9766-C44E5E255C26' and alignments.meta.disposition eq 'accepted')`
```

Note that you can use any of the "meta" properties on the relationship in the filtering - e.g. `alignments.meta.score`, `alignments.meta.tags`, etc. See the relationship definition for a complete list of meta properties.

### Filtering Standards and Relationships

Like Assets, Standards can also be filtered by some key properties on related entities. The following list shows related entity properties that can be included in a Standard search:

- Concepts
  
  - `concepts.context` - this field is also included in full text searches
  - `concepts.descr` - this field is also included in full text searches

### Filtering by Other Properties and Relationships to Other Resources

To search for resources by properties on related entities other than those listed above, use the search capability to locate the related entities of interest, build a list of related entities and then search the resource by the related entity IDs. For example, if you'd like to find Standards in Virginia that cover Exponents in the 8th grade, first search for the Topic. Topics are grade banded so you'll want to include the grade in your filter to ensure you are getting the correct Topic for the grade.

```
`filter[topics]=(query(descr, 'exponents') and education_levels.grades.code eq '8')`
```

The result is Topic `06EA4018-32ED-11E0-8DE3-079AD51F4EFC`. Then search the Standards for items in Virginia related to this Topic.

```
`filter[standards]=(document.publication.authorities.descr eq 'Virginia DOE' and education_levels.grades.code eq '8' and topics.id eq '06EA4018-32ED-11E0-8DE3-079AD51F4EFC')`
```

If the result of the first search resulted in multiple related Topics (say you also wanted to include Standards related to "Problem Solving"), you can include them all in the Standards filter using the "IN" clause. E.g.

```
`filter[standards]=(document.publication.authorities.descr eq 'Virginia DOE' and education_levels.grades.code eq '8' and topics.id in ('06EA4018-32ED-11E0-8DE3-079AD51F4EFC','067C7C8E-EBE5-11E5-AE48-F5189AAB8BA3'))`
```

Although we use Standards and their relationships to Topics in this example, the same approach can be taken for searching for any objects based on their relationship to other objects. E.g.

- Locating Standards related to Concepts or other Standards
- Locating Topics related to Standards or other Topics
- Locating Assets related to other Assets or to properties of Standards, Topics or Concepts not listed above.

When searching across relationships and specifying the filter criteria, the filter property name is based on the relationship rather than the related object type. For example, `standards` is a resource type and the Standards endpoint has relationships with other Standards. However, those relationships are named `parent`, `ancestors`, `origins`, `derivatives`, `children`, `peers`, etc. If the filter referenced the *type* instead of the relationship *name*, the filter would read `filter[standards]=(standards.id eq 'F97EA8C2-D9AE-11E2-8230-99ABD51F4EFC')` and the system would have no way to know which relationship you were filtering on. Instead, if you were looking for Standards that were under a given Standard (i.e. Standards that had a certain Standard as an `ancestor`) the proper filter notation would be `filter[standards]=(ancestors.id eq 'CB411CD4-D90D-11E2-8BD3-EF629DFF4B22')`.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).