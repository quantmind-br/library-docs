---
title: External Services | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/external
source: sitemap
fetched_at: 2026-02-17T15:13:24.717834-03:00
rendered_js: false
word_count: 252
summary: This document provides an overview of Moodle's Web Service framework and External API, serving as a central hub for developer resources on creating, implementing, and managing web services.
tags:
    - moodle
    - web-services
    - external-api
    - api-development
    - plugin-development
    - file-handling
    - backend-development
category: api
---

Moodle has a full-featured Web Service framework, allowing you to use and create web services for use in external systems. The Web Service framework and the External API work closely together providing a number of *Endpoints*, and self-describing classes to support a wide range of uses.

Moodle uses these web services internally for:

- AJAX interactions in the Moodle Web Interface; and
- The official Moodle Mobile App.

The following example shows a typical authentication and protocol workflow.

## Developer documentation[​](#developer-documentation "Direct link to Developer documentation")

The External Service API has two categories of documentation:

1. this documentation details how to *write* a web service and use the External API; and
2. API documentation for a live Moodle site, which can be found under \** Site administration &gt; Server &gt; Web services &gt; API Documentation \*\*.

In addition to the standard API endpoints, several additional API endpoints are available for the purpose of uploading, and downloading, files. For more information on these endpoints, see the [file handling](https://moodledev.io/docs/4.5/apis/subsystems/external/files) documentation.

- [How to contribute a web service function to core](https://docs.moodle.org/dev/How_to_contribute_a_web_service_function_to_core)
- [Adding a web service to your plugin](https://moodledev.io/docs/4.5/apis/subsystems/external/writing-a-service)
- Code example: [Adding a web service, using APIs](https://gist.github.com/timhunt/51987ad386faca61fe013904c242e9b4) by (Tim Hunt)
- [Implement a web service client](https://docs.moodle.org/dev/Creating_a_web_service_client)
- [Web services files handling](https://moodledev.io/docs/4.5/apis/subsystems/external/files)
- [Web service Listing & Roadmap](https://docs.moodle.org/dev/Web_services_Roadmap)

## Specification and brainstorming[​](#specification-and-brainstorming "Direct link to Specification and brainstorming")

- [External services security](https://moodledev.io/docs/4.5/apis/subsystems/external/security)
- [External services description](https://moodledev.io/docs/4.5/apis/subsystems/external/description)

## See also[​](#see-also "Direct link to See also")

- [Web service API functions](https://docs.moodle.org/dev/Web_service_API_functions)
- [Web services FAQ](https://docs.moodle.org/en/Web_services_FAQ)
- [How to create and enable a web service](https://docs.moodle.org/en/How_to_create_and_enable_a_web_service)
- [How to enable the mobile web service](https://docs.moodle.org/en/Enable_mobile_web_services)
- [Web services user documentation](https://docs.moodle.org/en/Web_services)
- [Mastering Moodle Web Services development](http://www.slideshare.net/juanleyva/mastering-moodle-web-services-development) - Last session of the Hackfest in the MoodleMoot UK 2016