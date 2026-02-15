---
title: SIS IDs | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/basics/file.object_ids
source: sitemap
fetched_at: 2026-02-15T09:12:59.284551-03:00
rendered_js: false
word_count: 393
summary: This document explains how to reference objects within the API using internal IDs, SIS IDs, LTI IDs, and special aliases, including requirements for URI encoding and server configuration.
tags:
    - object-identification
    - sis-ids
    - lti-ids
    - uri-encoding
    - canvas-lms
    - api-reference
category: reference
---

## Object IDs, SIS IDs, and special IDs

Throughout the API, objects are referenced by internal IDs. You can also reference objects by SIS ID, by prepending the SIS ID with the name of the SIS field, like `sis_course_id:`. For instance, to retrieve the list of assignments for a course with SIS ID of `A1234`:

```
/api/v1/courses/sis_course_id:A1234/assignments
```

The following objects support SIS IDs in the API:

- `sis_integration_id` (for users and courses)

Some objects support LTI IDs:

- `lti_context_id` (for accounts, assignments, courses, groups, and users)
- `lti_1_1_id` (for users, an alias of `lti_context_id`, which is sent in LTI 1.1 launches as `user_id`)
- `lti_1_3_id` (for users, a separate value from `lti_context_id`, sent in LTI 1.3 launches as `sub`)

Additionally, some objects support special IDs:

- Users support `self` to mean the current user.
- Accounts support `self` to mean the root account for the current domain, `default` to mean the Default account, and `site_admin` to mean the Site Admin account.
- Terms support `default` to mean the default term, and `current` to mean the term that is currently active according to term dates. A term must have a start date or an end date to be considered the current term. If there is more than one term that's active, `current` will not be found.

SIS IDs should be encoded as UTF-8, and then escaped normally for inclusion in a URI. For instance the SIS ID `CS/101.11é` is encoded and escaped as `CS%2F101%2E11%C3%A9`.

Note that some web servers have difficulties with escaped characters, particularly forward slashes. They may require special configuration to properly pass encoded slashes to Rails.

For Apache and Passenger, the following settings should be set:

Also beware that if you use [`ProxyPass`arrow-up-right](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypass), you should enable the `nocanon` option. Similarly, [`RewriteRule`arrow-up-right](https://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#rewriterule) should use the [`NE`arrow-up-right](https://httpd.apache.org/docs/2.2/rewrite/flags.html#flag_ne), or `noescape` flag. Other modules may also need additional configuration to prevent double-escaping of `%2f` (/) as `%252f`.

Prior versions of this API documentation described using a hex encoding to circumvent these issues, since the proper Apache/Passenger configuration was not known at the time. This format is deprecated, and will no longer be described, but will continue to be handled by the server for backwards compatibility.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).