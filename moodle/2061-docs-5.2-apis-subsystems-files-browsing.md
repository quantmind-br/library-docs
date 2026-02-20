---
title: File Browser API | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/files/browsing
source: sitemap
fetched_at: 2026-02-17T15:45:42.933629-03:00
rendered_js: false
word_count: 39
summary: This document introduces the Moodle File Browser API and explains how to use it to retrieve metadata and hierarchical folder information for stored files. It includes a code implementation for generating file breadcrumbs by traversing parent folders.
tags:
    - moodle-development
    - file-browser-api
    - php
    - file-management
    - metadata-retrieval
category: api
---

The File Browser API is a supplemental API which can be used to fetch information relating to Files stored in the [Moodle File API](https://moodledev.io/docs/5.2/apis/subsystems/files).

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