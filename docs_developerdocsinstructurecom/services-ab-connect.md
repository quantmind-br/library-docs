---
title: Elevate Standards Alignment - AB Connect | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect
source: sitemap
fetched_at: 2026-02-15T09:03:50.599978-03:00
rendered_js: false
word_count: 509
summary: This document introduces the AB Connect API, a RESTful service for integrating K-12 academic standards metadata and content alignment features into educational platforms.
tags:
    - ab-connect
    - k-12-standards
    - curriculum-alignment
    - rest-api
    - json-api
    - educational-metadata
    - odata-filtering
category: api
---

Welcome to the AB Connect interactive documentation. The documentation and related API were developed to help you integrate AB Connect data and decision support services into your system to power the discovery of your content as well as its relationships to academic standards (e.g. alignments) and other content. AB Connect is built upon the most comprehensive collection of connected K-12 standards metadata, machine learning algorithms and subject matter expert validation available.

If you find your users asking questions like the following, AB Connect has a solution for you.

- I have a standard from Texas, is there a similar standard statement in Arizona?
- I have a very useful lesson plan that is aligned to a Florida standard, but I'm teaching in California. What California standard might this lesson plan help me fulfill?
- I have a very useful lesson plan aligned to a Nevada standard. Are there other similar lesson plans aligned to other state standards that I might use?
- I want to create a lesson around the topic of equivalent numbers. Is there instructional material related to this topic that I can use to build my lesson?
- I have an assessment item covering mass and energy equivalence. Is there any instructional material I could use to reinforce this concept?
- I started tagging my assessment items with a few main concepts. What other concepts within standards may be related to these main concepts?
- I have a lesson plan that is covering divisibility rules. What standards across 50 states cover this concept? What other materials cover this concept?
- I have lessons aligned to Ohio's 2011 Science standards and they've just released the 2018 standards. How can I remap my alignments quickly?

This documentation describes the AB Connect API in great detail offering examples and an interactive [Reference section](https://developerdocs.instructure.com/services/ab-connect/reference/standards) to get you started right away. We invite you to learn more about AB Connect or take a test drive. [Check out the examples section](https://developerdocs.instructure.com/services/ab-connect/introduction/examples) to see working examples built using AB Connect.

*© 2024 Instructure, Inc. All rights reserved.*

Version 4.1 of AB Connect is [RESTfularrow-up-right](https://en.wikipedia.org/wiki/Representational_state_transfer) and is structurally compliant with [JSON APIarrow-up-right](http://jsonapi.org/). Since JSON API does not explicitly state syntax of filter statements, Academic Benchmarks adopted a simple filtering syntax based on [ODATAarrow-up-right](http://www.odata.org/)'s query $filter. Note that ODATA's syntax is not directly compatible with JSON API but [this discussion threadarrow-up-right](http://discuss.jsonapi.org/t/share-propose-a-filtering-strategy/257) was the inspiration for our solution.

When you send data through the interactive endpoints in the [Reference section](https://developerdocs.instructure.com/services/ab-connect/reference/standards), you must authenticate in order to make the call and the responses are handled by a production Academic Benchmarks server so the functionality is real and complete.

If you are already a licensed customer and don't know your credentials or would like to inquire about purchasing a license, please reach out to [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29) at Instructure.

If you are not a customer but would like to become familiar with the API, you can request a sandbox account [herearrow-up-right](https://community.canvaslms.com/plugins/custom/instructure/instructure/custom.ab-form).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).