---
title: Facets | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/facets
source: sitemap
fetched_at: 2026-02-15T09:04:13.347197-03:00
rendered_js: false
word_count: 972
summary: This document explains how to use facet arguments and summaries in API requests to provide end users with structured filtering options and item counts. It describes the syntax for requesting specific facet attributes and how to interpret the resulting metadata in the response.
tags:
    - api-facets
    - query-parameters
    - data-filtering
    - rest-api
    - facet-summary
    - metadata-extraction
category: api
---

Facets are common filter criteria that will help you present useful filter options to your end users. To request a list of facets for your license and filter criteria, use the facet argument in the GET query. The results are returned in the meta section of the response.

The form of the request is:

`facet=<CSV list of facet attributes>`

Calculating the facet summaries returned in the `meta.facet` section of the response does incur some calculation overhead. It is negligible in most circumstances but you have control over how much faceting the server performs. The URL query parameter `facet_summary` allows you to specify which data fields are processed with the call. A few useful examples:

- `facet_summary=*` - Return all of the facets available for the endpoint. See [Using Facets as an Entry Point for Browsing Assets](https://developerdocs.instructure.com/services/ab-connect/introduction/facets#using-facets-as-an-entry-point-for-browsing-assets). Note that using an asterisk can have an impact on system performance so we strongly recommend you use the asterisk only for discovery when you are learning the API. To ensure the use of wildcards with the `facet_summary` parameter does not impact overall system performance, such calls are throttled to 2 per second.
- `facet_summary=<CSV list of facet attributes>` - Return the summaries of the listed facets.

The facets that are available vary by endpoint and licensing. While some facets values offer additional properties, all of them have at least a `guid` and `descr` property. Note that Topic facets also offer information about their parents so a calling application can easily assemble the required tree without the added overhead of calls to the Topics endpoint.

## Using Facets as an Entry Point for Browsing Standards

By way of example, let's examine the facet capability of the Standards endpoint. This can be used as a convenient starting point for users browsing for Standards. It can also be used as a means for examining "categories" of Standards in your license. To get started, if you call the endpoint requesting all facet summaries without any filtering, the system will respond with the types of facets available and the number of elements in each facet. For convenience, we'll set the `limit` to 0 here so the system doesn't bother to respond with any actual Standards because at this point, we are only interested in the facets themselves which come back via the meta portion of the response.

```
`GET https://api.abconnect.instructure.com/rest/v4.1/standards?limit=0&facet_summary=*`
{
    "links": {
        "self": "https://api.abconnect.instructure.com/rest/v4.1/standards?limit=0&facet_summary=*"
    },
    "data": [],
    "meta": {
        "count": 378522,
        "facets": [
            {
                "count": 14,
                "facet": "education_levels.grades"
            },
            {
                "facet": "education_levels.ece_ages",
                "count": 8
            },
            {
                "count": 54,
                "facet": "document.publication.authorities"
            },
            {
                "facet": "disciplines.strands",
                "count": 111
            },
            {
                "facet": "disciplines.subjects",
                "count": 17
            },
            {
                "count": 440,
                "facet": "document"
            },
            {
                "facet": "document.publication.regions",
                "count": 54
            },
            {
                "count": 5542,
                "facet": "section"
            },
            {
                "facet": "disciplines.ece_domains",
                "count": 6
            },
            {
                "facet": "document.publication",
                "count": 163
            }
        ],
        "limit": 0,
        "took": 336,
        "offset": 0
    }
}
```

The facet counts respect both your license limitations and the current filter. In this case, we are not specifying a filter, so the counts reflect our licensing.

If you wanted to build a user interface that offers the user control over each facet in filtering the Standards, you could request the elements for each facet and populate lists with the results. You may find that offering 10 facets is overwhelming for your users so you may want to select a few key facets. Perhaps we start by allowing the users to select an authority and subject. Let's retrieve the details of those two facets. The facet "names" are the values of the `facet` properties - in this case, `document.publication.authorities` and `disciplines.subjects`. Note that you can see in the response above that there are 17 subjects and 54 authorities in this license (although yours will vary). The example response below has been simplified to improve readability.

```
`GET https://api.abconnect.instructure.com/rest/v4.1/standards?facet=document.publication.authorities,disciplines.subjects&limit=0`
{
    "links": {
        "self": "https://api.abconnect.instructure.com/rest/v4.1/standards?facet=document.publication.authorities,disciplines.subjects&limit=0"
    },
    "data": [],
    "meta": {
        "count": 378522,
        "facets": [
            {
                "facet": "disciplines.subjects",
                "details": [
                    {
                        "data": {
                            "descr": "Language Arts",
                            "guid": "F1FAC302-3B53-11E0-B042-495E9DFF4B22",
                            "code": "LANG"
                        },
                        "count": 120749
                    },
                    {
                        "count": 88449,
                        "data": {
                            "descr": "Science",
                            "guid": "F1FB3DD2-3B53-11E0-B042-495E9DFF4B22",
                            "code": "SCI"
                        }
                    },
                    {
                        "count": 85870,
                        "data": {
                            "code": "MATH",
                            "guid": "F1FB2F2C-3B53-11E0-B042-495E9DFF4B22",
                            "descr": "Mathematics"
                        }
                    },
                    {
                        "data": {
                            "code": "SOC",
                            "guid": "F1FB4B38-3B53-11E0-B042-495E9DFF4B22",
                            "descr": "Social Studies"
                        },
                        "count": 83445
                    },
                    {
                        "data": {
                            "code": "SCIT",
                            "descr": "Science and Technology",
                            "guid": "F1FC8A52-3B53-11E0-B042-495E9DFF4B22"
                        },
                        "count": 6638
                    },
                    ...
                ],
                "count": 17
            },
            {
                "details": [
                    {
                        "data": {
                            "acronym": null,
                            "descr": "Virginia DOE",
                            "guid": "912F0480-F1B9-11E5-862E-0938DC287387"
                        },
                        "count": 20833
                    },
                    {
                        "data": {
                            "guid": "9129D578-F1B9-11E5-862E-0938DC287387",
                            "acronym": null,
                            "descr": "Maryland DOE"
                        },
                        "count": 17919
                    },
                    {
                        "data": {
                            "descr": "Pennsylvania DOE",
                            "acronym": null,
                            "guid": "912DF40A-F1B9-11E5-862E-0938DC287387"
                        },
                        "count": 15428
                    },
                    {
                        "data": {
                            "guid": "9127D390-F1B9-11E5-862E-0938DC287387",
                            "descr": "New York DOE",
                            "acronym": null
                        },
                        "count": 14565
                    },
                    {
                        "data": {
                            "acronym": null,
                            "descr": "Georgia DOE",
                            "guid": "91296E80-F1B9-11E5-862E-0938DC287387"
                        },
                        "count": 13192
                    },
                    ...
                ],
                "facet": "document.publication.authorities",
                "count": 54
            }
        ],
        "limit": 0,
        "took": 459,
        "offset": 0
    }
}
```

Once a user has selected an authority (Georgia DOE) and subject (Science), you may want to offer them a list of relevant strands. Note that there are 111 strands in this sample license. Let's limit the scope to Georgia DOE and Science and get the list of relevant strands to offer the user.

```
`GET https://api.abconnect.instructure.com/rest/v4.1/standards?facet=disciplines.strands&filter[standards]=(document.publication.authorities.guid eq '91296E80-F1B9-11E5-862E-0938DC287387' and disciplines.subjects.code eq 'SCI')&limit=0`
{
    "links": {
        "self": "https://api.abconnect.instructure.com/rest/v4.1/standards?facet=disciplines.strands&filter[standards]=(document.publication.authorities.guid%20eq%20%2791296E80-F1B9-11E5-862E-0938DC287387%27%20and%20disciplines.subjects.code%20eq%20%27SCI%27)&limit=0"
    },
    "data": [],
    "meta": {
        "took": 119,
        "facets": [
            {
                "facet": "disciplines.strands",
                "details": [
                    {
                        "count": 1416,
                        "data": {
                            "descr": "Nature of Science",
                            "guid": "81C5F6E2-046C-11E0-9AE1-661C9DFF4B22"
                        }
                    },
                    {
                        "data": {
                            "guid": "81C4A2BA-046C-11E0-9AE1-661C9DFF4B22",
                            "descr": "Life Science"
                        },
                        "count": 353
                    },
                    {
                        "data": {
                            "guid": "81C51DF8-046C-11E0-9AE1-661C9DFF4B22",
                            "descr": "Physical Science"
                        },
                        "count": 296
                    },
                    {
                        "data": {
                            "descr": "Scientific Inquiry",
                            "guid": "81C58A0E-046C-11E0-9AE1-661C9DFF4B22"
                        },
                        "count": 276
                    },
                    {
                        "data": {
                            "guid": "81C62CFC-046C-11E0-9AE1-661C9DFF4B22",
                            "descr": "Earth Science"
                        },
                        "count": 240
                    },
                    {
                        "data": {
                            "guid": "81C5544E-046C-11E0-9AE1-661C9DFF4B22",
                            "descr": "Environmental Science"
                        },
                        "count": 65
                    },
                    {
                        "count": 28,
                        "data": {
                            "descr": "Space Science",
                            "guid": "81C63AA8-046C-11E0-9AE1-661C9DFF4B22"
                        }
                    }
                ],
                "count": 7
            }
        ],
        "limit": 0,
        "count": 2690,
        "offset": 0
    }
}
```

Now you see that there are only 7 relevant strands. One thing to note: the `detail.count` property is the number of Standards that match the associated criteria. For example, there are 28 Space Science related Standards in Georgia.

You can continue this approach to help the user narrow the Standards down to a manageable count and then present them to the user for selection.

## Using Facets as an Entry Point for Browsing Assets

Using faceting on Assets is similar to that of Standards with one major exception. Asset faceting can include custom attributes. E.g. if your Assets represent assessment items and you have an `item_type` field that may contain values like "Multiple Choice", "Essay", etc. you can request the facet summary by explicitly requesting `facet_summary=custom_attributes.item_type` and/or retrieve the details with `facet=custom_attributes.item_type`. The custom attributes may contain unique values (like a URL or external ID) and calculating the facets can impact performance.

- Although this section focused on the Standards endpoint as an example, all endpoints except Clarifier support faceting.
- The facet results appear in the meta section of the JSON API response.
- Facet summaries that have high counts (counts in the thousands) may not be exact - they are approximate for performance reasons. If you need an exact count, you must request the facet. The count returned with the facet is accurate as are the counts returned with each facet value.
- If you do not supply a `facet_summary` parameter, the system does not return any facet information.
- If the `facet` or `facet_summary` arguments are combined with filter criteria, the results respect the filter requirements.
- AB Connect does not support paging of facet data.
- When requesting facets with a large number of values (count &gt; 10,000) only the first 10,000 entries are returned. In general faceting on a large number of values has performance implications and should be avoided.
- A quick way to retrieve facet information without cluttering the response with actual Standards data is to use the `limit` argument and set the `limit` to `0`. For example:
  
  - `https://api.abconnect.instructure.com/rest/v4.1/standards?limit=0&facet_summary=*` returns a minimal set of data including the facets and counts for your license. You can use this as a starting point if you are dynamically building a UI to allow users to select facet criteria.
  - `https://api.abconnect.instructure.com/rest/v4.1/standards?limit=0&filter[standards]=(document.publication.authorities.descr%20eq%20%27Kentucky%20DOE%27)&facet_summary=*` returns the facets and counts for Kentucky DOE Standards.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).