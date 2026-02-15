---
title: Provisioning | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.provisioning
source: sitemap
fetched_at: 2026-02-15T09:13:51.509133-03:00
rendered_js: false
word_count: 889
summary: This document outlines various strategies for external tools to synchronize course rosters and user role data from Canvas using LTI services, launch payloads, and supplemental REST APIs.
tags:
    - lti-nrps
    - canvas-lms
    - user-provisioning
    - lti-advantage
    - roster-sync
    - rest-api
    - enrollment-management
category: guide
---

Many external tools will need to know which users are enrolled in a course and their roles. The approaches to this are varied depending on the version of LTI used and sometimes a single approach is not sufficient for all the use cases a tool might be interested in. Here, we outline several different approaches:

## LTI Advantage: Names and Role Provisioning Service

The IMS [Names and Role Provisioning Service (NRPS)arrow-up-right](https://www.imsglobal.org/spec/lti-nrps/v2p0) provides an efficient API for synchronizing course rosters. This capability is only available to LTI 1.3 tools. We will not discuss details of the specification here, but instead focus on configuring and using NRPS within the Canvas platform.

Before NRPS can be used, an [LTI Developer Key must be createdarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-LTI-key-for-an-account/ta-p/140) and enabled with the https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly scope. Next, the [external tool must be installedarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-configure-an-external-app-for-an-account-using-a-client/ta-p/202) in, or above, the context of the course that needs to be provisioned.

As with the other LTI Advantage service, tools must complete a specific [OAuth2 client credentials](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-lti-advantage-services) grant in order to obtain an access token. This access token works for any course that the tool is available in. A single token can be used for multiple courses and services.

Once an access token is obtained, tools may begin to [synchronize data using NRPS](https://developerdocs.instructure.com/services/canvas/resources/names_and_role). Using endpoint require knowledge of the context\_memberships\_url, which can either be obtained during the LTI launch in the [Names and Role Service claimarrow-up-right](https://www.imsglobal.org/spec/lti-nrps/v2p0#lti-1-3-integration), or by substituting the desired course\_id/group\_id in the [Names and Role API](https://developerdocs.instructure.com/services/canvas/resources/names_and_role).

- Canvas REST API access is not required (i.e. no additional authorization UI)
- Can provision all users in an entire course/group as long as the tool knows the context\_memberships\_url. This is easily obtained in the LTI payload.
- Can easily deterine if users have been removed from a course

<!--THE END-->

- Must have knowledge of the Canvas course\_id/group\_id or context\_memberships\_url
- Unidirectional: cannot push new enrollments to Canvas

<!--THE END-->

- Step 1: Configure a tool that support NRPS in Canvas

*Note:* Once a single launch has happened from a course, the tool has enough information to use NRPS at any time and get info about all the users.

## Provisioning during launch

This approach requires an LTI integration (any version) to be configured and visible somewhere within a Canvas course. Ideally, this LTI connection will already have an LTI SSO mechanism. If username, login ID, email, and/or SIS ID is required, make sure the privacy level is set to Public in the tool configuration. Otherwise, Canvas will only send an opaque LTI user id (as the user\_id parameter) and a Canvas ID (as the custom\_canvas\_user\_id).

- Canvas REST API access not required
- Can provision users on-the-fly as they launch the tool

<!--THE END-->

- The tool is only aware of users who've launched their tool at least once
- Unidirectional: cannot push new enrollments to Canvas
- Cannot determine if users drop courses or are deleted from Canvas

#### Instructor/Admin/Student Workflow

- Step 1: Configure an LTI tool in Canvas
- Step 3: Tool consumes user information (name, email, ID's, roles, contextual information etc...) and attempts to match on an ID. Best practice is to match on the user\_id from the launch and then fall back to some other ID if a match is not found
- Step 4: If a match is confirmed (and the signature matches), let the user access their information in your application
- Step 5: If no match is found, either or send them through a user-creation flow within the iframe, or auto-create a user for them based on the information in Canvas (you may want to let them set a password at this point, or email them a registration URL).

## Supplemental Provisioning via API

In the event that the LTI standard alone is not enough to satisfy your tool's provisioning needs, Canvas has an open REST API and a data service ( [Canvas Dataarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/What-is-Canvas-Data-Services/ta-p/142)). Using the API or Canvas Data can help overcome some of the limitations of LTI-only integrations, but they have their own challenges. Where possible, tools should try to avoid using services that are not part of the LTI standards unless it is absolutely necessary.

Accessing Canvas API's requires an institution to issue a [Developer Key](https://developerdocs.instructure.com/services/canvas/oauth2/file.developer_keys). Once issued, tools can begin using [OAuth2](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth#accessing-canvas-api) to request access tokens from individual users. The access token issued to access LTI advantage services **will not work** to access REST APIs.

Accessing Canvas Data also has its own authentication system that is [discussed elsewherearrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/What-is-Canvas-Data-Services/ta-p/142).

- more efficiently pre-provision an entire account by exporting provisioning reports or using Canvas Data.
- Obtaining course\_id's/group\_id's required to sync courses via NRPS without a launch occurring from that course.

<!--THE END-->

- Requires implementation of additional authentication systems.
- Results in non-interoperable integrations.
- If using Canvas APIs to sync entire accounts, can be slow for large accounts due to [API throttling](https://developerdocs.instructure.com/services/canvas/basics/file.throttling) and the sheer volume of requests being made
- Reports can take hours to generate for large accounts; breaking into many smaller reports broken by term or object is recommended.
- Canvas Data is not updated in real-time.

Other options include connecting directly to that same SIS that the client may be using, or leveraging [Canvas Dataarrow-up-right](https://community.canvaslms.com/t5/Admin-Guide/What-is-Canvas-Data-Services/ta-p/142) to pull flat files for courses and enrollments.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).