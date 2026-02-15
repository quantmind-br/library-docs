---
title: Outcomes CSV Format | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/outcomes/file.outcomes_csv
source: sitemap
fetched_at: 2026-02-15T09:13:23.010486-03:00
rendered_js: false
word_count: 910
summary: This document specifies the CSV file format and field requirements for bulk importing learning outcomes and outcome groups into Canvas LMS via the Outcomes Import API. It outlines mandatory headers, data encoding standards, and detailed definitions for each supported column in the import file.
tags:
    - canvas-lms
    - csv-import
    - learning-outcomes
    - data-format
    - api-integration
    - outcome-groups
category: reference
---

## Outcomes Import Format Documentation

Learning outcomes can be updated in bulk by using the Outcomes Import API. Each row in a CSV file represents either a learning outcome or a learning outcome group to create or update.

Standard CSV rules apply (including adherence to the CSV RFC 4180 format):

- The first row will be interpreted as a header defining the ordering of your columns. This header row is mandatory.
- Fields that contain a comma must be surrounded by double-quotes.
- Fields that contain double-quotes must also be surrounded by double-quotes, with the internal double-quotes doubled. Example: Chevy "The Man" Chase would be included in the CSV as "Chevy ""The Man"" Chase".

All text should be UTF-8 encoded.

All timestamps are sent and returned in ISO 8601 format. All timestamps default to UTC time zone unless specified.

A value that uniquely identifies this learning outcome or learning outcome group. For learning outcome groups, this value can be referenced by other learning outcomes or learning outcome groups in the parent\_guids field below, to indicate that this group contains an outcome or group. This value cannot contain spaces. If outcomes have been exported from an account with no vendor\_guid values set, canvas will auto-assign vendor\_guid values from internal identifiers. These ids will have the prefix "canvas\_outcome:" and "canvas\_outcome\_group:" for outcomes and groups respectively. We recommend that you \*do not* change these values once they have been assigned. If you want to set your own vendor\_guid values for existing outcomes, you should do that using the Canvas API prior to exporting outcomes from an account. In addition, these prefixes are reserved; newly created outcomes and groups may not have vendor\_guid fields with these prefixes.

A value of "outcome" indicates this is a learning outcome. A value of "group" indicates this is a learning outcome group

May only be given for rows where object\_type="group". If given, the generated learning outcome group will belong to the course with the given ID instead of to the account from which the import was initiated. Referenced course must belong to the initiating account or one of its sub-accounts. Can not be used in course-level imports.

The title of the learning outcome or learning outcome group.

The description of the learning outcome or learning outcome group (optional, defaults to blank).

Learning outcome display description in "friendly" language for students and parents (optional, defaults to blank). This value must be less than 255 characters in length.

The display name (or friendly name) of the learning outcome. This value does not apply to learning outcome groups.

Must be one of "decaying\_average", "n\_mastery", "highest", "latest", "average" or blank. This field must be blank for learning outcome groups. If not provided and this is a learning outcome, then the calculation method defaults to "decaying\_average". If the Account and Course Level Outcome Mastery Scales flag is enabled, the calculation\_method field does not need to be defined in the imported .csv. The calculation\_method field will be determined by the account and course settings. If Outcomes New Decaying Average Calculation Method feature flag is enabled then we will have one more calculation method "weighted\_average" and it would be the default calculation method.

Valid values depend on the "calculation\_method". For "decaying\_average", the value must be between 1 and 99, inclusive. For "n\_mastery", the value must be between 1 and 10, inclusive. For "highest", "latest" and "average", this field must be blank. If the Account and Course Level Outcome Mastery Scales flag is enabled, the calculation\_int field does not need to be defined in the imported .csv. The calculation\_int field will be determined by the account and course settings. If Outcomes New Decaying Average Calculation Method feature flag is enabled then For "weighted\_average", the value must be between 1 and 99, inclusive. For "standard\_decaying\_average", the value must be between 50 and 99, inclusive.

A space-separated list of vendor\_guid values of parent learning outcome groups for this learning outcome or learning outcome group. All of these vendor\_guid values must refer to previous rows, and all of these previous rows must represent learning outcome groups. If no value is provided, then this outcome or group will be added to the context's root outcome group.

Must be either "active" or "deleted". If not present, we assume the learning outcome or learning outcome group is "active".

The number of points that define mastery for this learning outcome. Must be blank for learning outcome groups. If the Account and Course Level Outcome Mastery Scales flag is enabled, the mastery\_points field does not need to be defined in the imported .csv. The mastery\_points field will be determined by the account and course settings.

number/text (multiple columns)

These columns must be the final columns of each row, and contain the scoring tiers for the given outcome. The columns alternate in decreasing point order: first, number of points for the tier, then tier description. This alternating pattern continues until there are no more scoring tiers for this outcome. These columns must be blank for learning outcome groups. See sample below. If the Account and Course Level Outcome Mastery Scales flag is enabled, the ratings field does not need to be defined in the imported .csv. The ratings field will be determined by the account and course settings.

Sample:

```
vendor_guid,object_type,title,description,display_name,calculation_method,calculation_int,workflow_state,parent_guids,ratings,,,,,,,
a,group,Parent group,parent group description,G-1,,,active,,,,,,,,,
b,group,Child group,child group description,G-1.1,,,active,a,,,,,,,,
c,outcome,Learning Standard,outcome description,LS-100,decaying_average,40,active,a b,3,Excellent,2,Better,1,Good,,
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 7 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).