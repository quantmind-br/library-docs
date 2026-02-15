---
title: Requesting Additional Properties in the Response | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/requesting-additional-properties
source: sitemap
fetched_at: 2026-02-15T09:04:37.112998-03:00
rendered_js: false
word_count: 254
summary: This document explains how to use the fields URL parameter in the AB Connect API to request specific object properties and customize the level of detail in the response data.
tags:
    - ab-connect
    - api-parameters
    - fields-selection
    - partial-responses
    - performance-throttling
    - query-strings
category: api
---

By default, if the fields argument is not included in the request, AB Connect responds with the object ID and type. In order to request that AB Connect return additional properties in its response, use the `fields` URL parameter. The form is `fields[<type>]=<CSV list of properties>`.

To illustrate the usage, let's take a look at the properties of a Standard and how use of the `fields` parameter affects the system response. Let's begin with the default response.

```
`GET https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22`
{
    "links": {
        "self": "https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22"
    },
    "data": {
        "type": "standards",
        "id": "1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22"
    },
    "meta": {
        "took": 66
    }
}
```

As you can see, the response does not include much useful information. Let's make the call again asking just for the main text of the Standard, its number and the AB `standard_type`.

```
`GET https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22?fields[standards]=statement.descr,standard_type,number.enhanced`
{
    "links": {
        "self": "https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22?fields[standards]=statement.descr,standard_type,number.enhanced"
    },
    "data": {
        "attributes": {
            "number": {
                "enhanced": "CCSS.Math.Content.HSN-VM.A.1"
            },
            "standard_type": "objective",
            "statement": {
                "descr": "Recognize vector quantities as having both magnitude and direction. Represent vector quantities by directed line segments, and use appropriate symbols for vectors and their magnitudes (e.g., ?, |?|, ||?||, ?)."
            }
        },
        "type": "standards",
        "id": "1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22"
    },
    "meta": {
        "took": 156
    }
}
```

Conversely, if you really want it ALL, you can use an asterisk to indicate that you want the system to give you EVERYTHING! Note that this can have an impact on system performance so we strongly recommend you use the asterisk only for discovery when you are learning the API. To ensure the use of wildcards with the `fields` parameter does not impact overall system performance, such calls are throttled to 2 per second.

For brevity, we've removed some details in this example as the payload is quite large.

```
`GET https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22?fields[standards]=*`
{
    "links": {
        "self": "https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22?fields[standards]=%2A"
    },
    "data": {
        "type": "standards",
        "id": "1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22",
        "attributes": {
            "statement": {
                "addendums": [],
                "combined_descr": "Recognize vector quantities as having both magnitude and direction. Represent vector quantities by directed line segments, and use appropriate symbols for vectors and their magnitudes (e.g., 𝙫, |𝙫|, ||𝙫||, 𝘷).",
                "descr": "Recognize vector quantities as having both magnitude and direction. Represent vector quantities by directed line segments, and use appropriate symbols for vectors and their magnitudes (e.g., 𝙫, |𝙫|, ||𝙫||, 𝘷)."
            },
            "label": "Standard",
            "education_levels": {
                "grades": [
                    {
                        "code": "9",
                        "descr": "9th Grade",
                        "guid": "F1FA7154-3B53-11E0-B042-495E9DFF4B22",
                        "seq": 110
                    },
                    {
                        "seq": 120,
                        "guid": "F1FA7E92-3B53-11E0-B042-495E9DFF4B22",
                        "descr": "10th Grade",
                        "code": "10"
                    },
                    {
                        "code": "11",
                        "guid": "F1FA8BD0-3B53-11E0-B042-495E9DFF4B22",
                        "descr": "11th Grade",
                        "seq": 130
                    },
                    {
                        "guid": "F1FA9904-3B53-11E0-B042-495E9DFF4B22",
                        "descr": "12th Grade",
                        "seq": 140,
                        "code": "12"
                    }
                ],
                "ece_ages": []
            },
            "number": {
                "raw": "1.",
                "prefix_enhanced": "CCSS.Math.Content.HSN-VM.A.1",
                "enhanced": "CCSS.Math.Content.HSN-VM.A.1"
            },
            "utilizations": [
                {
                    "guid": "3A6BCD99-F093-4782-9708-5E65F2DEC3F2",
                    "type": "alignable"
                }
            ],
            "in_list": "N",
            "status": "active",
            "captured_by": "AB",
            "deepest" : "Y",
            "disciplines": {
                "subjects": [
                    {
                        "guid": "F1FB2F2C-3B53-11E0-B042-495E9DFF4B22",
                        "descr": "Mathematics",
                        "code": "MATH"
                    }
                ],
                "_content_connections": [],
                "strands": [
                    {
                        "guid": "81C28CFA-046C-11E0-9AE1-661C9DFF4B22",
                        "descr": "Patterns, Functions, and Algebra"
                    }
                ],
                "genres": [],
                "ece_domains": []
            },
            "key_ideas": [
                {
                    "concepts": [
                        {
                            "guid": "0AADCE68-3BA2-11E1-A29D-011A9DFF4B22",
                            "descr": "Vectors"
                        },
                        {
                            "descr": "Mathematical Notation",
                            "guid": "0CB810D8-3BA2-11E1-A29D-011A9DFF4B22"
                        }
                    ],
                    "guid": "75757524-D232-11DE-8EF1-B44B9DFF4B22"
                },
                {
                    "guid": "982B3456-D236-11DE-B34E-394D9DFF4B22",
                    "concepts": [
                        {
                            "descr": "Vectors",
                            "guid": "0AADCE68-3BA2-11E1-A29D-011A9DFF4B22"
                        },
                        {
                            "guid": "0BE351EA-3BA2-11E1-A29D-011A9DFF4B22",
                            "descr": "Vector Direction"
                        }
                    ]
                },
                {
                    "concepts": [
                        {
                            "descr": "Vectors",
                            "guid": "0AADCE68-3BA2-11E1-A29D-011A9DFF4B22"
                        },
                        {
                            "guid": "0BE36E64-3BA2-11E1-A29D-011A9DFF4B22",
                            "descr": "Vector Magnitude"
                        }
                    ],
                    "guid": "982B4BE4-D236-11DE-B34E-394D9DFF4B22"
                }
            ],
            "document": {
                "assessment_year": null,
                "disciplines": {
                    "primary_subject": {
                        "code": "MATH",
                        "guid": "F1FB2F2C-3B53-11E0-B042-495E9DFF4B22",
                        "descr": "Mathematics"
                    }
                },
                "adopt_year": "2010",
                "source_url": "http://www.corestandards.org/Math/",
                "revision_year": "2010",
                "guid": "6C2635F0-6EC0-11DF-AB2D-366B9DFF4B22",
                "date_modified_utc": "2018-02-13 16:26:49",
                "descr": "Mathematics",
                "obsolete_year": null,
                "implementation_year": null,
                "publication": {
                    "guid": "964E0FEE-AD71-11DE-9BF2-C9169DFF4B22",
                    "regions": [
                        {
                            "code": "US",
                            "guid": "91273AE8-F1B9-11E5-862E-0938DC287387",
                            "descr": "United States of America",
                            "type": "country"
                        },
                        {
                            "type": "other",
                            "guid": "A83297F2-901A-11DF-A622-0C319DFF4B22",
                            "descr": "CCSS",
                            "code": "CC"
                        }
                    ],
                    "descr": "Common Core State Standards",
                    "authorities": [
                        {
                            "acronym": "CC",
                            "descr": "NGA Center/CCSSO",
                            "guid": "A83297F2-901A-11DF-A622-0C319DFF4B22"
                        }
                    ],
                    "acronym": null,
                    "source_url": "http://www.corestandards.org/the-standards"
                }
            },
            "topic_organizer": null,
            "has_list": "N",
            "date_deleted_utc": null,
            "section": {
                "_id": 21003,
                "date_modified_utc": "2018-02-13 16:26:49",
                "guid": "25EC8E56-7053-11DF-8EBF-BE719DFF4B22",
                "descr": "High School - Number and Quantity",
                "obsolete_year": null,
                "seq": 2410,
                "assessment_year": null,
                "disciplines": {
                    "primary_subject": {
                        "code": "MATH",
                        "descr": "Mathematics",
                        "guid": "F1FB2F2C-3B53-11E0-B042-495E9DFF4B22"
                    }
                },
                "adopt_year": "2010",
                "implementation_year": null,
                "label": "Conceptual Category",
                "number": null
            },
            "alt_identifiers": [
                {
                    "type": "GUID",
                    "id": "05BAE0DE74104B1AADC31E85AA1A6128",
                    "source": "canonical"
                },
                {
                    "source": "canonical",
                    "id": "http://corestandards.org/Math/Content/HSN-VM/A/1",
                    "type": "URI"
                }
            ],
            "level": 3,
            "date_modified_utc": "2014-06-19 16:36:44",
            "guid": "1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22",
            "seq": 30,
            "extensions": [],
            "uri": "https://api.abconnect.instructure.com/rest/v4.1/standards/1F9D5A8A-7053-11DF-8EBF-BE719DFF4B22",
            "legends": [
                {
                    "symbol_position": "before",
                    "descr": "Additional mathematics that students should learn in order to take advanced courses",
                    "symbol": "+"
                }
            ],
            "standard_type": "objective"
        },
        "relationships": {
            "concepts": {
                "data": [...]
            },
            "derivatives": {
                "data": [...]
            },
            "peers": {
                "data": [...]
            },
            "contexts": {
                "data": [
                    {
                        "type": "standards",
                        "id": "1F9A411A-7053-11DF-8EBF-BE719DFF4B22"
                    }
                ]
            },
            "topics": {
                "data": [
                    {
                        "type": "topics",
                        "id": "9E783750-4445-11E0-9271-67D4D51F4EFC"
                    }
                ]
            },
            "origins": {
                "data": []
            },
            "parent": {
                "data": {
                    "id": "1F9BE786-7053-11DF-8EBF-BE719DFF4B22",
                    "type": "standards"
                }
            },
            "ancestors": {
                "data": [
                    {
                        "type": "standards",
                        "id": "1F9A411A-7053-11DF-8EBF-BE719DFF4B22"
                    },
                    {
                        "id": "1F9BE786-7053-11DF-8EBF-BE719DFF4B22",
                        "type": "standards"
                    }
                ]
            },
            "peer_derivatives": {
                "data": []
            },
            "children": {
                "data": []
            }
        }
    },
    "meta": {
        "took": 152
    }
}
```

See the section on [Addressing Object Properties](https://developerdocs.instructure.com/services/ab-connect/introduction/addressing-object-properties) for insight into property names.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).