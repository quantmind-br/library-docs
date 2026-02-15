---
title: Differentiation Tags CSV Format | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/group-categories/file.differentiation_tags_csv
source: sitemap
fetched_at: 2026-02-15T09:11:16.797637-03:00
rendered_js: false
word_count: 452
summary: This document outlines the requirements and data format for using the Differentiation Tags Import API to bulk update user tags and tag sets via CSV files. It explains the identification criteria for users and tags, mandatory CSV headers, and the behavior of tag creation and assignment within the system.
tags:
    - canvas-lms
    - differentiation-tags
    - api-import
    - csv-formatting
    - user-management
    - data-integration
category: api
---

Differentiation Tags can be updated in bulk by using the Differentiation Tags Import API. Each row in a CSV file represents a user to be added to a tag, where a tag set can be specified.

Tags and tag sets that don't exist in the UI will be created. Tags that are created will only use the tag\_name column for creation. User columns in the file are used to identify the user to be added to the tag. Users names are available in the Differentiation Tags export, but not used or updated in the import process.

If a tag set is provided, tags that don't exist in the UI will be created under that set and existing tags will be moved (along with their memberships) to that tag set.

Standard CSV rules apply (including adherence to the CSV RFC 4180 format):

- The first row will be interpreted as a header defining the ordering of your columns. This header row is mandatory.
- Fields that contain a comma must be surrounded by double-quotes.
- Fields that contain double-quotes must also be surrounded by double-quotes, with the internal double-quotes doubled. Example: Chevy "The Man" Chase would be included in the CSV as "Chevy ""The Man"" Chase".

All text should be UTF-8 encoded.

## Differentiation Tag Data Format

The canvas id for a user, required to identify a user.

A unique identifier used to reference users in the enrollments table. This identifier must not change for the user, and must be globally unique. In the user interface, this is called the SIS ID.

The name that a user will use to login to Instructure. If you have an authentication service configured (like LDAP), this will be their username from the remote system.

The name of the differentiation tag.

The canvas id for a differentiation tag.

A unique identifier used to reference tags. This identifier must not change for the tag, and must be globally unique. This column is for identification and does not populate new tags with sis\_ids

The name of the differentiation tag set.

The canvas id for a differentiation tag set.

A unique identifier used to reference tag sets. This identifier must not change for the tag, and must be globally unique. This column is for identification and does not populate new tag sets with sis\_ids

\* canvas\_user\_id, user\_id, or login\_id is required and tag\_name, canvas\_tag\_id or tag\_id is required. If you would like to specify a tag set, tag\_set\_name, canvas\_tag\_set\_id or tag\_set\_id is required.

Sample:

```
canvas_user_id,user_id,login_id,tag_name,canvas_tag_id,tag_id,tag_set_name,canvas_tag_set_id,tag_set_id
92,,,Awesome Tag,,,Awesome Tag Set,,
,13aa3,,,45,,,,
,,mlemon,,,g125,,,
```

```
canvas_user_id,user_id,login_id,tag_name
92,,,Awesome Tag
,13aa3,,Other Tag
,,mlemon,Awesome Tag
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 6 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).