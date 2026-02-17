---
title: Filter plugins | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/plugintypes/filter
source: sitemap
fetched_at: 2026-02-17T15:12:08.317797-03:00
rendered_js: false
word_count: 761
summary: This document explains how to create and implement filter plugins in Moodle to automatically transform text content before it is displayed. It covers the mandatory file structure, the text_filter class implementation, and performance best practices for developers.
tags:
    - moodle-development
    - filter-plugins
    - output-api
    - plugin-development
    - php
    - text-processing
    - performance-optimization
category: guide
---

Filters are a way to automatically transform content before it is output. Filters may be used to:

- Render embedded equations to images (the TeX filter).
- Automatically convert links to media files to embedded players.
- Automatically convert mentions of glossary terms to links.

Filters are one of the easiest types of plugin to create.

Filters are applied to content passed into the `format_string()` and `format_text()` functions, which are part of the [Output API](https://moodledev.io/docs/4.5/apis/subsystems/output).

## File structure[​](#file-structure "Direct link to File structure")

Filter plugins are located in the `/filter` directory.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

View an example directory layout for the `filter_pluginname` plugin.

```
 filter/pluginname/
 |-- lang
 |   `-- en
 |       `-- filter_pluginname.php
 |-- classes
 |   `-- text_filter.php
 `-- version.php
```

Some of the important files for the filter plugintype are described below. See the [common plugin files](https://moodledev.io/docs/4.5/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

### filter.php[​](#filterphp "Direct link to filter.php")

#### Filter main class

##### File path: /classes/text\_filter.php

The filter file contains the code for the main filter class. Unlike more complex plugins like activities or repositories, filters only have one mandatory class extending the core \`\\core\_filters\\text\_filter\` class.

View example

public/filter/pluginname/classes/text\_filter.php

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
 * Filter main class for the filter_pluginname plugin.
 *
 * @package   filter_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

namespacefilter_pluginname;

classtext_filterextends\core_filters\text_filter{
functionfilter(string$text,array$options=[]){
// Return the modified text.
return$text;
}
}
```

### version.php[​](#versionphp "Direct link to version.php")

#### Version metadata

##### File path: /version.php

The version.php contains metadata about the plugin.

It is used during the installation and upgrade of the plugin.

This file contains metadata used to describe the plugin, and includes information such as:

- the version number
- a list of dependencies
- the minimum Moodle version required
- maturity of the plugin

View example

public/filter/pluginname/version.php

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
 * Version metadata for the filter_pluginname plugin.
 *
 * @package   filter_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL')||die();

$plugin->version=TODO;
$plugin->requires=TODO;
$plugin->supported=TODO;// Available as of Moodle 3.9.0 or later.
$plugin->incompatible=TODO;// Available as of Moodle 3.9.0 or later.
$plugin->component='TODO_FRANKENSTYLE';
$plugin->maturity=MATURITY_STABLE;
$plugin->release='TODO';

$plugin->dependencies=[
'mod_forum'=>2022042100,
'mod_data'=>2022042100
];
```

### lang/en/filter\_pluginname.php[​](#langenfilter_pluginnamephp "Direct link to lang/en/filter_pluginname.php")

#### Language files

##### File path: /lang/en/plugintype\_pluginname.php

Each plugin must define a set of language strings with, at a minimum, an English translation. These are specified in the plugin's `lang/en` directory in a file named after the plugin. For example the LDAP authentication plugin:

```
// Plugin type: `auth`
// Plugin name: `ldap`
// Frankenstyle plugin name: `auth_ldap`
// Plugin location: `auth/ldap`
// Language string location: `auth/ldap/lang/en/auth_ldap.php`
```

warning

Every plugin *must* define the name of the plugin, or its `pluginname`.

The `get_string` API can be used to translate a string identifier back into a translated string.

```
get_string('pluginname', '[plugintype]_[pluginname]');
```

- See the [String API](https://docs.moodle.org/dev/String_API#Adding_language_file_to_plugin) documentation for more information on language files.

View example

public/filter/pluginname/lang/en/plugintype\_pluginname.php

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
 * Languages configuration for the filter_pluginname plugin.
 *
 * @package   filter_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['filtername']='Activity names auto-linking';
```

## Test a filter[​](#test-a-filter "Direct link to Test a filter")

To enable a filter, go to the [filters administration screen](https://moodledev.io/docs/4.5/apis/plugintypes/filter) and set the filter active to "On".

Filters are applied to all text that is printed with the output functions `format_text()` and `format_string()`. To see a filter in action, add some content to a label resource. When you look at that course in the course listing, you should see that your filter has transformed the text accordingly.

## Filter performance[​](#filter-performance "Direct link to Filter performance")

It is important to note that all active filters will be called to transform every bit of text output using `format_text()` (headers and content), and `format_string()` (headers only). As a result a filter plugin can cause big performance problems. It is extremely important to use cache if your filter must retrieve data from the database, or other similar sources.

If a filter uses a special syntax or it is based on an appearance of a substring in the text, it is recommend to perform a quick and cheap `strpos()` search first prior to executing the full regex-based search and replace.

View example

```
/**
 * Example of a filter that uses <a> links in some way.
 */
publicfunctionfilter($text,array$options=[]){

if(!is_string($text)orempty($text)){
// Non-string data can not be filtered anyway.
return$text;
}

if(stripos($text,'</a>')===false){
// Performance shortcut - if there is no </a> tag, nothing can match.
return$text;
}

// Here we can perform some more complex operations with the <a>
// links in the text.
}
```

## Local configuration[​](#local-configuration "Direct link to Local configuration")

Filters can use different configuration depending on the context in which they are called. For example, the glossary filter can be configured such that when displayed in Forum A it only links words from a particular glossary, while in Forum B it links words from a different glossary..

To support this behaviour, a filter plugin must provide a `filterlocalsettings.php` file which defines a Moodle form which subclasses the `filter_local_settings_form` class. In addition to the standard formslib methods, you must also define a `save_changes` method.

View example

filterlocalsettings.php

```
classpluginfile_filter_local_settings_formextends\core_filters\form\local_settings_form{
protectedfunctiondefinition_inner(\MoodleQuickForm$mform){
$mform->addElement(
'text',
'word',
get_string('word','filter_helloworld'),
['size'=>20]
);
$mform->setType('word',PARAM_NOTAGS);
}
}
```

All the local configurations can be accessed in the main filter class in the `$this->localconfig` property.

View example

filter/pluginname/classes/text\_filter.php

```
<?php
namespacefilter_pluginname;

classtext_filterextends\core_filters\text_filter{
publicfunctionfilter(string$text,array$options=[]){
global$CFG;

$search=$this->localconfig['word']??'default';
returnstr_replace($search,"Hello $search!",$text);
}
}
```

## Filtering dynamic content[​](#filtering-dynamic-content "Direct link to Filtering dynamic content")

It is possible that page content is loaded by ajax after the page is loaded. In certain filter types (for example MathJax) JavaScript is required to be run on the output of the filter in order to do the final markup. For these types of filters, a JavaScript event is triggered when new content is added to the page (the content will have already been processed by the filter in php). The JavaScript for a filter can listen for these event notifications and reprocess the affected dom nodes.

The content updated event is registered in the `core_filters/events` module and can be imported as:

```
import{eventTypes}from'core_filters/events';

document.addEventListener(eventTypes.filterContentUpdated, eventHandler);
```

View example

```
import{eventTypes}from'core_filters/events';

/** @var{bool} Whether this is the first load of videojs module */
let firstLoad;

/**
 * Initialise the dynamic content filter.
 *
 * @method
 * @listens event:filterContentUpdated
 */
exportconstinit=()=>{
if(!firstLoad){
return;
}
    firstLoad =true;
// Add the event listener.
document.addEventListener(eventTypes.filterContentUpdated, contentUpdatedHandler);
};

/**
 * Notify video.js of new nodes.
 *
 * @param{Event}event The event.
 */
constcontentUpdatedHandler=(event)=>{
const updatedContent = event.detail.nodes;
    updatedContent.forEach(content=>{
// Alter any updated content.
});
};
```