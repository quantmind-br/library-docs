---
title: Addressing Object Properties | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/addressing-object-properties
source: sitemap
fetched_at: 2026-02-15T09:03:57.701353-03:00
rendered_js: false
word_count: 180
summary: This document outlines the syntax rules for naming object properties within API URL parameters, specifically detailing the use of dot notation and how to handle JSON API keywords.
tags:
    - url-parameters
    - dot-notation
    - api-conventions
    - property-naming
    - ab-connect
    - json-api
category: reference
---

There are several URL Parameters where you will need to name specific properties of an object (like filter and fields). Generally speaking, see the endpoint's Response Attributes section for the properties that are available. Here are a few rules to keep in mind when constructing the property names.

- The name of a property on an object is addressed using dot notation like `object.property`. E.g. `disciplines.grades`
- JSON constructs in AB Connect responses that are inserted simply to adhere to JSON API requirements are not included in the property naming. E.g. if you want to address the `standard_type` of a `standard` object, the name is simply `standard_type` - not `data.attributes.standard_type`. Generally speaking, JSON API keywords can be left out of the names - things like attributes, relationships and data. Note that meta properties on relationships are the acception. We include the `meta` part of the property path to eliminate conflicts between object and relationship property names.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).