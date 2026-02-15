---
title: Canvas Roles | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/external-tools/file.canvas_roles
source: sitemap
fetched_at: 2026-02-15T09:13:25.988482-03:00
rendered_js: false
word_count: 234
summary: This document defines the standard role vocabularies and URN/URL identifiers used in LTI 1.1 and 1.3 to communicate user privilege levels between platforms and tools.
tags:
    - lti
    - lti-1-3
    - user-roles
    - lis-specification
    - canvas-lms
    - interoperability
category: reference
---

LTI generally recognizes that users make use of the integrated functionality offered by tools to platforms. These users typically come with a defined role with respect to the context within which they operate when using a tool.

The role represents the level of privilege a user has been given within the context hosted by the platform. Typical roles are "learner", "instructor", and "administrator". Note that it's entirely possible that a user might have a different role in a different context (a user that is a "student" in one context may be an "instructor" in another, for example).

The IMS role vocabularies are derived from the [LIS specificationarrow-up-right](https://www.imsglobal.org/activity/onerosterlis#LIS)

### LTI 1.1 using the LIS 1.1 Roles

urn:lti:sysrole:ims/lis/User

urn:lti:sysrole:ims/lis/SysAdmin

urn:lti:instrole:ims/lis/Instructor

urn:lti:instrole:ims/lis/Student

urn:lti:instrole:ims/lis/Administrator

urn:lti:role:ims/lis/Learner/NonCreditLearner

urn:lti:role:ims/lis/Mentor

urn:lti:instrole:ims/lis/Administrator

urn:lti:role:ims/lis/Learner

urn:lti:role:ims/lis/Instructor

urn:lti:role:ims/lis/TeachingAssistant

urn:lti:role:ims/lis/ContentDeveloper

urn:lti:role:ims/lis/Learner/NonCreditLearner

urn:lti:role:ims/lis/Mentor

urn:lti:role:ims/lis/Learner

Source: [LTI 1.1 - Role vocabulariesarrow-up-right](http://www.imsglobal.org/specs/ltiv1p1/implementation-guide#toc-8)

### LTI 1.3 using the LIS 2.0 Roles

http://purl.imsglobal.org/vocab/lis/v2/system/person#User

http://purl.imsglobal.org/vocab/lis/v2/system/person#SysAdmin

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Instructor

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Student

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Administrator

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Administrator

http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor

http://purl.imsglobal.org/vocab/lis/v2/membership/Instructor#TeachingAssistant

http://purl.imsglobal.org/vocab/lis/v2/membership#Learner

http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor

http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper

http://purl.imsglobal.org/vocab/lis/v2/membership#Mentor

http://purl.imsglobal.org/vocab/lis/v2/membership#Learner

Source: [LTI 1.3 - Role vocabulariesarrow-up-right](https://www.imsglobal.org/spec/lti/v1p3#role-vocabularies)

### LTI 1.3 using the LIS 2.0 LTI Advantage Roles

http://purl.imsglobal.org/vocab/lis/v2/system/person#User

http://purl.imsglobal.org/vocab/lis/v2/system/person#SysAdmin

http://purl.imsglobal.org/vocab/lti/system/person#TestUser

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Instructor

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Student

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Administrator

http://purl.imsglobal.org/vocab/lis/v2/institution/person#Administrator

http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor

http://purl.imsglobal.org/vocab/lis/v2/membership/Instructor#TeachingAssistant

http://purl.imsglobal.org/vocab/lis/v2/membership#Learner

http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor

http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper

http://purl.imsglobal.org/vocab/lis/v2/membership#Mentor

http://purl.imsglobal.org/vocab/lis/v2/membership#Learner

http://purl.imsglobal.org/vocab/lti/system/person#TestUser

http://purl.imsglobal.org/vocab/lis/v2/membership#Member

http://purl.imsglobal.org/vocab/lis/v2/membership#Member

http://purl.imsglobal.org/vocab/lis/v2/membership#Manager

Source: [LTI 1.3 - Role vocabulariesarrow-up-right](https://www.imsglobal.org/spec/lti/v1p3#role-vocabularies)

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).