---
title: File Converters | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/plugintypes/fileconverter
source: sitemap
fetched_at: 2026-02-17T15:12:07.068505-03:00
rendered_js: false
word_count: 363
summary: Provides technical instructions for creating file converter plugins in Moodle, including file structure requirements and the implementation of mandatory conversion methods.
tags:
    - moodle-development
    - file-converter
    - plugin-architecture
    - file-conversion
    - php-interface
category: guide
---

File converters are an important tool to support other plugins with file conversion supported between a wide range of file formats. File converters are accessed using the [File conversion API](https://moodledev.io/docs/4.5/apis/subsystems/files/converter) and are typically consumed by other plugins rather than by the user directly.

## File structure[​](#file-structure "Direct link to File structure")

File converter plugins are located in the `/files/converter` directory.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

View an example directory layout for the `fileconverter_unoconv` plugin.

```
files/converter/unoconv
├── classes
│   ├── converter.php
│   └── privacy
│       └── provider.php
├── lang
│   └── en
│       └── fileconverter_unoconv.php
├── settings.php
└── version.php
```

Some of the important files for the fileconverter plugintype are described below. See the [common plugin files](https://moodledev.io/docs/4.5/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

### Converter class[​](#converter-class "Direct link to Converter class")

#### File conversion implementation

##### File path: /classes/converter.php

The `classes/converter.php` class must be defined in the correct namespace for your plugin, and must implement the `\core_files\converter_interface` interface.

It is responsible for converting files

View example

\[path/to/plugintype]/example/classes/converter.php

```
<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * File conversion implementation for the plugintype_example plugin.
 *
 * @package   plugintype_example
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

namespacefileconverter_myexample;

classconverterimplementscore_filesconverter_interface{
// ...
}
```

#### are\_requirements\_met()[​](#are_requirements_met "Direct link to are_requirements_met()")

This function informs the File Converter API whether the system requirements of the plugin are met. That is whether appropriate API keys are present, and the API might be available.

It should be lightweight to call and cache where required.

Example implementation

```
publicstaticfunctionare_requirements_met(){
returnextension_loaded('my_php_extension');
}
```

#### start\_document\_conversion() and poll\_conversion\_status()[​](#start_document_conversion-and-poll_conversion_status "Direct link to start_document_conversion() and poll_conversion_status()")

The `start_document_conversion()` function starts a conversion, whilst `poll_conversion_status` should poll for any status update. The following apply:

- If any failures occur, it should set the conversion status to `\core_files\conversion::STATUS_FAILED` and immediately return. There is no need to update the `$conversion` record in this situation.
- When the conversion process starts, the status should be set to `\core_files\conversion::STATUS_IN_PROGRESS` and the record **must** be updated. This ensures that, should the process take a long time, the current status is accurately reflected.
- Upon successful completion, the status should be updated to `\core_files\conversion::STATUS_COMPLETE` and the newly created `\stored_file` should be stored against the conversion using either the `store_destfile_from_string` or `store_destfile_from_path` function as appropriate.

#### supports()[​](#supports "Direct link to supports()")

This function allows the plugin to answer whether it supports conversion between two formats. It is typically only used internally by the File Conversion subsystem.

Example implementation

```
classconverterimplements\core_files\converter_interface{
// ...
publicstaticfunctionsupports($from,$to){
// This plugin supports conversion from doc and docx to pdf only.
if($from!=='doc'&&$from!=='docx'){
returnfalse;
}

return$to==='pdf';
}
}
```

Example usage

```
if(\fileconverter_example::supports('jpg','pdf')){
// ...
}
```

#### get\_supported\_conversion()[​](#get_supported_conversion "Direct link to get_supported_conversion()")

This function is used purely for information purposes to display possible conversions to an administrator.

## See also[​](#see-also "Direct link to See also")

- Using the [File Converter API](https://moodledev.io/docs/4.5/apis/subsystems/files/converter)