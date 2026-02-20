---
title: Function Definitions | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/subsystems/external/functions
source: sitemap
fetched_at: 2026-02-17T14:56:18.876697-03:00
rendered_js: false
word_count: 0
summary: This document defines a PHP class for a Moodle external API function that allows the creation of groups within a course through a structured web service interface.
tags:
    - moodle-development
    - external-api
    - php
    - web-services
    - group-management
    - plugin-development
category: api
---

```
<?php

namespacelocal_groupmanager\external;

defined('MOODLE_INTERNAL')||die;

require_once("{$CFG->libdir}/externallib.php");

classcreate_groupsextendsexternal_api{
publicstaticfunctionexecute_parameters():external_function_parameters{
returnnewexternal_function_parameters([
'groups'=>newexternal_multiple_structure(
newexternal_single_structure([
'courseid'=>newexternal_value(PARAM_INT,'The course to create the group for'),
'idnumber'=>newexternal_value(
PARAM_RAW,
'An arbitrary ID code number perhaps from the institution',
VALUE_DEFAULT,
null
),
'name'=>newexternal_value(
PARAM_RAW,
'The name of the group'
),
'description'=>newexternal_value(
PARAM_TEXT,
'A description',
VALUE_OPTIONAL
),
]),
'A list of groups to create'
),
]);
}

publicstaticfunctionexecute(array$groups):array{
// Validate all of the parameters.
[
'groups'=>$groups,
]=self::validate_parameters(self::execute_parameters(),[
'groups'=>$groups,
]);

// Perform security checks, for example:
$coursecontext=\context_course::instance($courseid);
self::validate_context($coursecontext);
require_capability('moodle/course:creategroups',$coursecontext);

// Create the group using existing Moodle APIs.
$createdgroups=\local_groupmanager\util::create_groups($groups);

// Return a value as described in the returns function.
return[
'groups'=>$createdgroups,
];
}

publicstaticfunctionexecute_returns():external_single_structure{
returnnewexternal_single_structure(
'groups'=>newexternal_multiple_structure([
'id'=>newexternal_value(PARAM_INT,'Id of the created user'),
'name'=>newexternal_value(PARAM_RAW,'The name of the group'),
])
);
}
}
```