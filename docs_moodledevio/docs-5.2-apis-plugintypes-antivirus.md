---
title: Antivirus plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/plugintypes/antivirus
source: sitemap
fetched_at: 2026-02-17T15:43:54.18661-03:00
rendered_js: false
word_count: 670
summary: This document explains how to develop antivirus plugins for Moodle, detailing the mandatory file structure and the implementation of the core scanner class. It covers the required configuration files and methods needed to integrate external virus scanning tools into the platform.
tags:
    - moodle-development
    - antivirus-plugin
    - file-security
    - plugin-architecture
    - php-api
category: guide
---

Moodle supports automatic virus scanning of files as they are uploaded by users. To enable this developers can write an antivirus plugin, which acts as a bridge between Moodle and the antivirus tooling.

A plugin to support the Open Source [ClamAV](https://www.clamav.net/) antivirus engine is included with Moodle core as standard.

## File structure[​](#file-structure "Direct link to File structure")

Antivirus plugins are located in the `/lib/antivirus` directory.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

View an example directory layout for the `antivirus_scanmyfile` plugin.

```
 lib/antivirus/scanmyfile/
 |-- classes
 |   `-- scanner.php
 |-- db
 |   `-- upgrade.php
 |-- lang
 |   `-- en
 |       `-- antivirus_scanmyfile.php
 |-- settings.php
 |-- tests
 |   `-- scanner_test.php
 `-- version.php
```

Some of the important files for the antivirus plugintype are described below. See the [common plugin files](https://moodledev.io/docs/5.2/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

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

public/lib/antivirus/pluginname/version.php

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
 * Version metadata for the antivirus_pluginname plugin.
 *
 * @package   antivirus_pluginname
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

### settings.php[​](#settingsphp "Direct link to settings.php")

#### Plugin settings

##### File path: /settings.php

You can define settings for your plugin that the administrator can configure by creating a `settings.php` file in the root of your plugins' directory.

caution

Settings must named in the following format:

```
plugintype_pluginname/settingname
```

By following the correct naming, all settings will automatically be stored in the `config_plugins` database table.

Full details on how to create settings are available in the [Admin settings](https://moodledev.io/docs/5.2/apis/subsystems/admin) documentation.

View example

public/lib/antivirus/scanmyfile/settings.php

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
 * Plugin settings for the antivirus_scanmyfile plugin.
 *
 * @package   antivirus_scanmyfile
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

if($ADMIN->fulltree){
$settings->add(
newadmin_setting_configexecutable(
'antivirus_scanmyfile/pathtoscanner',",
            new lang_string('pathtoscanner', 'antivirus_scanmyfile'),",
newlang_string('configpathtoscanner','antivirus_scanmyfile'),",
            ''",
)
);
}
```

### lang/en/antivirus\_scanmyfile.php[​](#langenantivirus_scanmyfilephp "Direct link to lang/en/antivirus_scanmyfile.php")

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

public/lib/antivirus/scanmyfile/lang/en/plugintype\_pluginname.php

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
 * Languages configuration for the antivirus_scanmyfile plugin.
 *
 * @package   antivirus_scanmyfile
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['pluginname']='ScanMyFile antivirus';
$string['pathtoscanner']='Path to scanner';
$string['configpathtoscanner']='Define full path to scanner';
```

### classes/scanner.php[​](#classesscannerphp "Direct link to classes/scanner.php")

#### Antivirus scanner

##### File path: /classes/scanner.php

The `classes/scanner.php` class must be defined in the correct namespace for your plugin, and must extend the `\core\antivirus\scanner` class.

It is responsible for implementing the interface between Moodle and the antivirus scanning tool.

The following methods are compulsory:

- `is_configured(): bool` - returns true, if this antivirus plugin is configured.
- `scan_file($file, $filename, $deleteinfected): void` - performs the **$file** scanning using antivirus functionality, using **$filename** as filename string in any reporting, deletes infected file if **$deleteinfected** is true.

If a virus is found the `scan_file()` function *must* throw an instance of the `\core\antivirus\scanner_exception` type.

View example

public/lib/antivirus/scanmyfile/classes/scanner.php

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
 * Antivirus scanner for the antivirus_scanmyfile plugin.
 *
 * @package   antivirus_scanmyfile
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

namespaceantivirus_scanmyfile;

classscannerextends\core\antivirus\scanner{

publicfunctionis_configured(){
// Note: You will likely want a more specific check.
// This example just checks whether configuration exists.
return(bool)$this->get_config('pathtoscanner');
}

publicfunctionscan_file($file,$filename,$deleteinfected){
if(!is_readable($file)){
// This should not happen.
debugging('File is not readable.');
return;
}

// Execute the scan using the fictitious scanmyfile tool.
// In this case the tool returns:
// - 0 if no virus is found
// - 1 if a virus was found
// - [int] on error
$return=$this->scan_file_using_scanmyfile_scanner_tool($file);

if($return==0){
// Perfect, no problem found, file is clean.
return;
}elseif($return==1){
// Infection found.
if($deleteinfected){
unlink($file);
}
thrownew\core\antivirus\scanner_exception(
'virusfounduser',
'',
['filename'=>$filename]
);
}else{
// Unknown problem.
debugging('Error occurred during file scanning.');
return;
}
}

publicfunctionscan_file_using_scanmyfile_scanner_tool($file):int{
// Scanning routine using antivirus own tool goes here..
// You should choose a return value appropriate for your tool.
// These must match the expected values in the scan_file() function.
// In this example the following are returned:
// - 0: No virus found
// - 1: Virus found
return0;
}
}
```

### tests/scanner\_test.php (optional)[​](#testsscanner_testphp-optional "Direct link to tests/scanner_test.php (optional)")

Writing unit tests is strongly encouraged as it can help to identify bugs, or changes in behaviour, that you had not anticipated.

Since antivirus plugins typically rely on an external dependency, it is usually a good idea to replace the real component with a test "double". You can see an example of this in Moodle in the [antivirus\_clamav unit tests](https://github.com/moodle/moodle/blob/81407f18ecff1fded66a9d8bdc25bbf9d8ccd5ca/lib/antivirus/clamav/tests/scanner_test.php#L45-L56).

The PHPUnit Manual contains a dedicated [section on Test Doubles](https://docs.phpunit.de/en/9.6/test-doubles.html).

You may also wish to include some tests of the real system to ensure that upgrades to the Antivirus software do not break your plugin.