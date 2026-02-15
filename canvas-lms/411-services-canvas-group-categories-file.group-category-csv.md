---
title: Group Categories CSV Format | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/group-categories/file.group_category_csv
source: sitemap
fetched_at: 2026-02-15T09:12:48.307032-03:00
rendered_js: false
word_count: 349
summary: This document outlines the CSV data format and technical requirements for bulk importing and updating group categories and group memberships in Canvas LMS.
tags:
    - canvas-lms
    - csv-import
    - group-categories
    - data-format
    - user-management
    - bulk-update
category: reference
---

## Group Category Import Format Documentation

Group categories can be updated in bulk by using the Group Categories Import API. Each row in a CSV file represents a user to be added to a group in the group category.

Groups that don't exist in the UI will be created. Groups that are created will only use the group\_name column for creation. User columns in the file are used to identify the user to be added to the group. Users names are available in the group\_category export, but not used or updated in the import process.

Standard CSV rules apply (including adherence to the CSV RFC 4180 format):

- The first row will be interpreted as a header defining the ordering of your columns. This header row is mandatory.
- Fields that contain a comma must be surrounded by double-quotes.
- Fields that contain double-quotes must also be surrounded by double-quotes, with the internal double-quotes doubled. Example: Chevy "The Man" Chase would be included in the CSV as "Chevy ""The Man"" Chase".

All text should be UTF-8 encoded.

## Group Category Data Format

The canvas id for a user, required to identify a user.

A unique identifier used to reference users in the enrollments table. This identifier must not change for the user, and must be globally unique. In the user interface, this is called the SIS ID.

The name that a user will use to login to Instructure. If you have an authentication service configured (like LDAP), this will be their username from the remote system.

The canvas id for a group.

A unique identifier used to reference groups in the group\_users data. This identifier must not change for the group, and must be globally unique. This column is for identification and does not populate new groups with sis\_ids

\* canvas\_user\_id, user\_id, or login\_id is required and group\_name, canvas\_group\_id or group\_id is required.

Sample:

```
canvas_user_id,user_id,login_id,group_name,canvas_group_id,group_id
92,,,Awesome Group,,
,13aa3,,,45,
,,mlemon,,,g125
```

```
canvas_user_id,user_id,login_id,group_name
92,,,Awesome Group
,13aa3,,Other Group
,,mlemon,Awesome Group
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).