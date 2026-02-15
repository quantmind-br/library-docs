---
title: Introduction | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_intro
source: sitemap
fetched_at: 2026-02-15T08:58:17.864385-03:00
rendered_js: false
word_count: 1097
summary: This document provides an overview of integrating external tools into Canvas using the LTI standard, outlining various tool placement types and configuration methods.
tags:
    - lti-integration
    - canvas-lms
    - external-tools
    - lti-advantage
    - tool-placement
    - ims-standard
category: concept
---

Canvas, like many LMSs, supports loading external resources inline using the [IMS LTI standardarrow-up-right](http://www.imsglobal.org/lti/). These tools can be deployed on a course or account level. Once configured, tools can be surfaced [as links in course modules](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.link_selection_placement) or used to [deliver custom assignment experiences](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.assignment_selection_placement). Canvas supports some additional integration points using LTI (see the "Placements" dropdown in the left hand navigation here) to offer a more integrated experience and to allow for more customization of the Canvas product. This is accomplished by [configuring additional settings](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.lti_dev_key_config) on external tools used inside of Canvas and by leveraging [LTI Advantage servicesarrow-up-right](https://www.imsglobal.org/lti-advantage-overview).

Because tools can be deployed at any level in the system hierarchy, they can be as general or specific as needed. The Chemistry Department can add chemistry-specific tools without those tools cluttering everyone else's interfaces. Or, a single teacher who is trying out some new web service can do so without needing the tool to be set up at the account level.

### Types of Tool Integrations

Canvas currently supports the following types of tool placements.

**External tool** [**assignments integrations**](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools)**:**

This type of integration is part of the [LTI 1.1 Outcomes Servicearrow-up-right](http://www.imsglobal.org/LTI/v1p1/ltiIMGv1p1.html) or [LTI 1.3 Assignment and Grade Servicesarrow-up-right](http://www.imsglobal.org/spec/lti-ags/v2p0/) and allows external services to synchronize grades, and other assignment details.

Example use cases might include:

- Administering a timed, auto-graded coding project
- Evaluating a student's ability to correctly draw notes at different musical intervals
- Giving students credit for participating in an interactive lesson on the Civil War

**Adding a link/tab to the** [**course navigation**](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.navigation_tools#course_navigation)**:**

Example use cases might include:

- Building a specialized attendance/seating chart tool
- Adding an "ebooks" link with course required reading
- Connecting to study room scheduling tool
- Linking to campus communication hub
- Displaying a course-level dashboard (ex: analytics, student engagement, risk assessment, etc.)

**Adding a link/tab to the** [**account navigation**](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.navigation_tools#account_navigation)**:**

Example use cases might include:

- Including outside reports in the Canvas UI
- Building helper libraries for campus-specific customizations
- Leveraging single sign-on for access to other systems, like SIS

**Adding a link/tab to the** [**user profile navigation**](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.navigation_tools#user_navigation)**:**

Example use cases might include:

- Leveraging single sign-on to student portal from within Canvas
- Linking to an external user profile

**Selecting content to add to a variety of locations as** [**LTI deep links**](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.content_item)**:**

Example use cases might include:

- adding a button to [embed content to the Rich Content Editor](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.editor_button_placement):
  
  - Embedding resources from campus video/image repository
  - Inserting custom-designed chemistry diagrams into quiz question text
  - Building integrations with new or subject-area-specialized web authoring services
- [selecting links for modules](https://developerdocs.instructure.com/services/canvas/external-tools/lti/placements/file.link_selection_placement)
  
  - Building and then linking to a remixed version of an online Physics textbook
  - Selecting from a list of pre-built, interactive quizzes on blood vessels
  - Choosing a specific chapter from an e-textbook to add to a module
- [creating custom assignments for Canvas](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.assignment_tools)
  
  - Creating a Canvas assignment that launches the student to a custom assessment that can be automatically graded by the tool and synced with the Canvas Gradebook
  - Launching the student to an assessment with interactive videos. Once complete, the tool returns an LTI launch url that allows the teacher to see the submission without leaving Canvas.

**Subscribing to notifications with** [**Platform Notification Service**](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.pns)**:**

Platform Notification Service (PNS) enables server-to-server communication by allowing the Platform to send messages, known as Notices, to Tools outside the scope of an active user session. Tools can register a "webhook" or handler endpoint using PNS to receive specific types of Notices, facilitating seamless integration and automation.

### How to Configure/Import Integrated Tools

Tool's placements can be configured using [LTI configuration XML](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.tools_xml) as specified in the IMS Common Cartridge specification, or using the [external tools API](https://developerdocs.instructure.com/services/canvas/resources/external_tools). Configuration XML contains all non-account-specific settings (except the consumer key and shared secret, which must always be entered manually). The user can [configure the tool by a tool-provided URLarrow-up-right](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-configure-an-external-app-for-a-course-using-a-URL/ta-p/884) (recommended), or [paste in the XMLarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-external-app-for-an-account-using-XML/ta-p/221) that the tool provides.

For information on how to programmatically configure external tools, so users don't have to copy and paste URLs or XML, please see the Canvas [external tools API](https://developerdocs.instructure.com/services/canvas/resources/external_tools).

Similar to LTI 1.1, tools built on the [LTI 1.3 specificationarrow-up-right](https://www.imsglobal.org/spec/lti/v1p3/) can be configured by either supplying clients with a JSON block or URL that hosts the JSON. This JSON is used to determine the behavior of the tool within Canvas by [configuring an LTI Developer Keyarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-LTI-key-for-an-account/ta-p/140). Once the developer key is created and turned on, users with sufficient permissions can [install the tool using the developer key's client IDarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-external-app-for-an-account-using-a-client/ta-p/202).

**LTI Advantage Services permissions**

When setting up Developer Keys, the section “LTI Advantage Services” allows you to enable or disable permissions for access via that developer key. Below is the list of permissions available:

**Can create and view assignment data in the gradebook associated with the tool**

https://purl.imsglobal.org/spec/lti-ags/scope/lineitem

**Can view assignment data in the gradebook associated with the tool**

https://purl.imsglobal.org/spec/lti-ags/scope/lineitem.readonly

**Can view submission data for assignments associated with the tool.**

https://purl.imsglobal.org/spec/lti-ags/scope/result.readonly

**Can create and update submission results for assignments associated with the tool**

https://purl.imsglobal.org/spec/lti-ags/scope/score

**Can view Progress records associated with the context the tool is installed in**

https://canvas.instructure.com/lti-ags/progress/scope/show

**Can retrieve user data associated with the context the tool is installed in**

https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly

**Can register to receive asynchronous notifications from Canvas**

Allows use of the 1EdTech Platform Notification Service.

https://purl.imsglobal.org/spec/lti/scope/noticehandlers

**Can retrieve submissions from Document Processor Assignments (experimental)**

Allows use of the Asset Service (part of the 1EdTech Asset Processor specification). *Under development and not available yet for general use.*

https://purl.imsglobal.org/spec/lti/scope/asset.readonly

**Can send reports for Document Processor Assignments (experimental)**

Allows use of the Asset Report Service (part of the 1EdTech Asset Processor specification). *Under development and not available yet for general use.*

https://purl.imsglobal.org/spec/lti/scope/report

**Can track if EULA has been accepted (experimental)**

Allows use of the EULA Acceptance Service (part of the 1EdTech Asset Processor specification). *Under development and not available yet for general use.*

https://purl.imsglobal.org/spec/lti/scope/eula/user

**Can reset EULA acceptance status (experimental)**

Allows use of the EULA Deployment Service (part of the 1EdTech Asset Processor specification). *Under development and not available yet for general use.*

https://purl.imsglobal.org/spec/lti/scope/eula/deployment

**Can update public jwk for LTI services**

https://canvas.instructure.com/lti/public\_jwk/scope/update

**Can lookup Account information**

https://canvas.instructure.com/lti/account\_lookup/scope/show

**Can view the content of a page the tool is launched from**

https://canvas.instructure.com/lti/page\_content/show

**Can view LTI registrations associated with the tool**

Allows readonly access to the tool's own registration

https://purl.imsglobal.org/spec/lti-reg/scope/registration.readonly

**Can send automatic updates to be approved by an Administrator**

Allows the tool to view and push update requests to it's own registration

https://purl.imsglobal.org/spec/lti-reg/scope/registration

NOTE: scopes with `https://canvas.instructure.com` are Canvas specific while others are LTI specifications

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).