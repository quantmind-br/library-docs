---
title: Examples | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/examples
source: sitemap
fetched_at: 2026-02-15T09:03:36.879718-03:00
rendered_js: false
word_count: 957
summary: This document provides an overview of available sample applications and source code repositories designed to help developers learn and implement integrations with the AB Connect API.
tags:
    - ab-connect
    - api-integration
    - sample-apps
    - developer-resources
    - standards-browser
    - academic-benchmarks
    - github-repository
category: guide
---

One of the challenges with adopting a new integration is coming up to speed on the basics of interacting with the partner system. To lower the slope of the learning curve, Academic Benchmarks has documented examples and developed apps. We are sharing the source to give developer's working examples of how to integrate with AB Connect.

Below are brief descriptions of efficient means for implementing solutions and useful examples apps with links to the [Instructure Github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples) where they can be downloaded. All samples and apps are offered as-is with no warranty. Although they are often usable as is, the main purpose is to illustrate how to interact with the AB Connect API. If any particular app doesn't do what you need, feel free to download a copy and modify it to meet your needs. This repository is not meant to host solutions for non-technical users nor is it a location to submit requests for changes or additions to the API or the samples listed here. Be sure to read the ReadMe for each app for details.

## Standards Relationships Browser

Among other things, AB Connect exposes the relationships between Standards. This app is a web page client that allows the user to browse Standards in their license, view the metadata profile of the Standard and find related Standards in other documents. The user is allowed to select from a set of relationships types when navigating across relationships. The types of relationships that are available is based on the licensing of the account used. If the account is not licensed for relationships, the app falls back to a simple Standards browser. This app is also an example of an integration with the embeddable Standards Browser widget (see [Using AB Connect's Embeddable Widgets](https://developerdocs.instructure.com/services/ab-connect/introduction/widgets) ). You can find the source in the relationships-browser folder of our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples). You can find a [working version of the app herearrow-up-right](https://widgets.academicbenchmarks.com/ABConnect/v4/relationships-browser/RelationshipBrowser.html).

This is a very simple example app that does little more than illustrate a minimal integration with the embeddable Standards Browser widget. This app is a web page client that allows the user to browse Standards in their license and view the metadata profile of the Standard. See [Using AB Connect's Embeddable Widgets](https://developerdocs.instructure.com/services/ab-connect/introduction/widgets) below for more information. You can find the source in the standards-browser-min folder of our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples). You can find a [working version of the app herearrow-up-right](https://widgets.academicbenchmarks.com/ABConnect/v4/standards-browser-min/StandardsBrowser.html).

## Browse Standards by Topic

AB Connect includes a few taxonomies that can aid in the navigation of Standards and searchability of Assets. The Topics Browser is a basic example of how one could use topics to locate relevant Standards. You can find the source in the topicsBrowser folder of our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples). You can find a [working version of the app herearrow-up-right](https://widgets.academicbenchmarks.com/ABConnect/v4/topicsBrowser/topicsBrowser.html).

## Show Alignments On Your Content Page

This example app is designed to give you a quick leg up on showing alignments on your web site. This small sample allows the user to search for content by `client_id` (usually your internal ID for the content), AB Asset GUID or general text search. It then shows the alignments for the first Asset it finds in AB Connect that matches the search criteria. The user can narrow the scope of the authorities to show only alignments in one state (for example). You can find the source in the display-alignments folder of our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

This is a web page client that allows the user to use faceting to search their Asset repository on AB Connect. Note that the app requires that the account already has a set of Assets and at least a minimal configuration that should take a couple of minutes to get it up and running in a demo mode. You can find the source in the asset-browser folder of our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

## Standards Relationships Report

This example is similar to the browser app but is a node.js based and generates a report with a mapping of a set of Standards from one document to another. The input and output are done through Excel files. There is a template supplied as part of the repository. You'll need to use another means for gathering the input which is a set of Standard GUIDs. One quick way to build the list is to use something like Postman to gather the Standards of interest. You can find the source in the relationships-report folder of our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

The source for the Standards Browser Widget documented in [Using AB Connect's Embeddable Widgets](https://developerdocs.instructure.com/services/ab-connect/introduction/widgets) is accessable as well. This is a more complex example that spends more effort on the quality of the look and user experience. Where the other examples are good for accelerating API ramp up, the widget source code is best suited to situations where the widget itself is close to meeting your organization's needs but you need to add or modify some features. In that case, start with the existing widget and extend it to meet your needs. You can download the latest [source herearrow-up-right](https://widgets.academicbenchmarks.com/ABConnect/v4/dist/widgets-src.zip).

Here are basic instructions for building the supplied source for distribution. All commands must be executed in the directory where you've unzipped the source.

1. Unzip the file into a folder on your system.
2. Run the following commands in the folder where you placed the unzipped source.
3. Use dist/widgets.js and dist/widgets.js.map

To obtain a production widgets bundle, follow these steps:

1. For a bash shell:
   
   1. `NODE_ENV=production npm run build`

The illustrative-postman-collections folder in our [public repositoryarrow-up-right](https://github.com/instructure/abconnect-samples) hosts a set of Postman collections that can help get you started with API calls for various scenarios. The ReadMe file gives the details of the available collections.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).