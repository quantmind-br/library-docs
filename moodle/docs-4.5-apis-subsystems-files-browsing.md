---
title: File Browser API | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/files/browsing
source: sitemap
fetched_at: 2026-02-17T15:13:54.432961-03:00
rendered_js: false
word_count: 39
summary: This document explains how to use the Moodle File Browser API to retrieve metadata and hierarchical path information for files stored within the Moodle File API.
tags:
    - moodle
    - file-browser-api
    - php
    - file-management
    - metadata-extraction
category: api
---

The File Browser API is a supplemental API which can be used to fetch information relating to Files stored in the [Moodle File API](https://moodledev.io/docs/4.5/apis/subsystems/files).

This example demonstrates using the `filebrowser` API to fetch the parent folders of a file.

```
publicfunctionget_file_breadcrumbs(\stored_file$file):?array{
$browser=get_file_browser();
$context=get_system_context();

$fileinfo=$browser->get_file_info(
\context::instance_by_id($file->get_contextid()),
$file->get_component(),
$file->get_filearea(),
$file->get_itemid(),
$file->get_filepath(),
$file->get_filename()
)

if($fileinfo){
// Build a Breadcrumb trail
$level=$fileinfo->get_parent();
while($level){
$path[]=[
'name'=>$level->get_visible_name(),
];
$level=$level->get_parent();
}

$path=array_reverse($path);

return$path;
}

returnnull;
}
```