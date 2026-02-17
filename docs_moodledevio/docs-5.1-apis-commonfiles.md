---
title: Common files | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/commonfiles
source: sitemap
fetched_at: 2026-02-17T15:33:49.188172-03:00
rendered_js: false
word_count: 2704
summary: This document outlines the standard file structure and mandatory components required for developing Moodle subsystems and plugins, including versioning, localization, and database definitions.
tags:
    - moodle-development
    - plugin-architecture
    - versioning
    - database-migration
    - localization
    - php-moodle
category: reference
---

This page describes the common files which may be present in any Moodle subsystem or [plugin type](https://moodledev.io/docs/5.1/apis/plugintypes). Some of these files are mandatory and **must** exist within a component, whilst others are optional.

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

\[path/to/plugintype]/pluginname/version.php

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
 * Version metadata for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
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

### lang/en/plugintype\_pluginname.php[​](#langenplugintype_pluginnamephp "Direct link to lang/en/plugintype_pluginname.php")

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

Activity modules are different

Activity modules do not use the **frankenstyle** name as a filename, they use the plugin name. For example the forum activity plugin:

```
// Plugin type: `mod`
// Plugin name: `forum`
// Frankenstyle plugin name: `mod_forum`
// Plugin location: `mod/forum`
// Language string location: `mod/forum/lang/en/forum.php`
```

View example

\[path/to/plugintype]/pluginname/lang/en/plugintype\_pluginname.php

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
 * Languages configuration for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['pluginname']='The name of my plugin will go here';
```

### lib.php[​](#libphp "Direct link to lib.php")

#### Global plugin functions

##### File path: /lib.php

The `lib.php` file is a legacy file which acts as a bridge between Moodle core, and the plugin. In recent plugins it is should only used to define callbacks and related functionality which currently is not supported as an auto-loadable class.

All functions defined in this file **must** meet the requirements set out in the relevant section of the [Coding style](https://moodledev.io/general/development/policies/codingstyle#functions-and-methods).

Performance impact

Moodle core often loads all the `lib.php` files of a given plugin types. For performance reasons, it is strongly recommended to keep this file as small as possible and have just required code implemented in it. All the plugin's internal logic should be implemented in the auto-loaded classes.

### locallib.php[​](#locallibphp "Direct link to locallib.php")

#### Global support functions

##### File path: /locallib.php

Legacy feature

The use of this file is no longer recommended, and new uses of it will not be permitted in core code.

Rather than creating global functions in a global namespace in a `locallib.php` file, you should use autoloaded classes which are located in the `classes/` directory.

Where this file is in use, all functions **must** meet the requirements set out in the relevant section of the [Coding style](https://moodledev.io/general/development/policies/codingstyle#functions-and-methods)

Existing functions which have been incorrectly named **will not** be accepted as an example of an existing convention. Existing functions which are incorrectly named **should** be converted to use a namespaced class.

### db/install.xml[​](#dbinstallxml "Direct link to db/install.xml")

#### Database schema

##### File path: /db/install.xml

The `install.xml` file is used to define any database tables, fields, indexes, and keys, which should be created for a plugin during its initial installation.

caution

When creating or updating the `install.xml` you **must** use the built-in [XMLDB editor](https://docs.moodle.org/dev/XMLDB_Documentation) within Moodle.

### db/upgrade.php[​](#dbupgradephp "Direct link to db/upgrade.php")

#### Upgrade steps

##### File path: /db/upgrade.php

The `db/upgrade.php` file contains upgrade steps, including database schema changes, changes to settings, and other steps which must be performed during upgrade.

See the [Upgrade API](https://moodledev.io/docs/5.1/guides/upgrade) documentation for further information.

Generating Database Schema changes

When making changes to the database schema you **must** use the build-in [XMLDB editor](https://docs.moodle.org/dev/XMLDB_Documentation) within Moodle. This can be used to generate php upgrade steps.

The [install.xml](https://moodledev.io/docs/5.1/apis/commonfiles#dbinstallxml) schema must match the schema generated by the upgrade at all times.

To create an upgrade step you must:

1. Use the [XMLDB editor](https://moodledev.io/general/development/tools/xmldb) to create the definition of the new fields
2. Update the `install.xml` from the XMLDB editor
3. Generate the PHP upgrade steps from within the XMLDB Editor
4. Update the version number in your `version.php`

tip

In many cases you will be able to combine multiple upgrade steps into a single version change.

When a version number increment is detected during an upgrade, the `xmldb_[pluginname]_upgrade` function is called with the old version number as the first argument.

See the [Upgrade API](https://moodledev.io/docs/5.1/guides/upgrade) documentation for more information on the upgrade process.

View example

\[path/to/plugintype]/pluginname/db/upgrade.php

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
 * Upgrade steps for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

functionxmldb_certificate_upgrade($oldversion=0){
if($oldversion<2012091800){
// Add new fields to certificate table.
$table=newxmldb_table('certificate');
$field=newxmldb_field('showcode');
$field->set_attributes(XMLDB_TYPE_INTEGER,'1',XMLDB_UNSIGNED,XMLDB_NOTNULL,null,'0','savecert');
if(!$dbman->field_exists($table,$field)){
$dbman->add_field($table,$field);
}
// Add new fields to certificate_issues table.
$table=newxmldb_table('certificate_issues');
$field=newxmldb_field('code');
$field->set_attributes(XMLDB_TYPE_CHAR,'50',null,null,null,null,'certificateid');
if(!$dbman->field_exists($table,$field)){
$dbman->add_field($table,$field);
}

// Certificate savepoint reached.
upgrade_mod_savepoint(true,2012091800,'certificate');
}

// Everything has succeeded to here. Return true.
returntrue;
}
```

### db/access.php[​](#dbaccessphp "Direct link to db/access.php")

#### Plugin capabilities

##### File path: /db/access.php

The `db/access.php` file contains the **initial** configuration for a plugin's access control rules.

Access control is handled in Moodle by the use of Roles, and Capabilities. You can read more about these in the [Access API](https://moodledev.io/docs/5.1/apis/subsystems/access) documentation.

Changing initial configuration

If you make changes to the initial configuration of *existing* access control rules, these will only take effect for *new installations of your plugin*. Any existing installation **will not** be updated with the latest configuration.

Updating existing capability configuration for an installed site is not recommended as it may have already been modified by an administrator.

View example

\[path/to/plugintype]/pluginname/db/access.php

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
 * Plugin capabilities for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$capabilities=[
// Ability to use the plugin.
'plugintype/pluginname:useplugininstance'=>[
'riskbitmask'=>RISK_XSS,
'captype'=>'write',
'contextlevel'=>CONTEXT_COURSE,
'archetypes'=>[
'manager'=>CAP_ALLOW,
'editingteacher'=>CAP_ALLOW,
],
],
];
```

### db/install.php[​](#dbinstallphp "Direct link to db/install.php")

#### Post-installation hook

##### File path: /db/install.php

The `db/install.php` file allows you define a post-installation hook, which is called immediately after the initial creation of your database schema.

caution

This file is not used at all after the *initial* installation of your plugin.

It is *not called* during any upgrade.

### db/uninstall.php[​](#dbuninstallphp "Direct link to db/uninstall.php")

#### Pre-uninstallation hook

##### File path: /db/uninstall.php

The `db/uninstall.php` file allows you define a pre-uninstallation hook, which is called immediately before all table and data from your plugin are removed.

### db/events.php[​](#dbeventsphp "Direct link to db/events.php")

#### Event observer definitions

##### File path: /db/events.php

Moodle supports a feature known as _ [Event observers](https://docs.moodle.org/dev/Events_API#Event_observers) _ to allow components to make changes when certain events take place.

The `db/events.php` file allows you define any event subscriptions that your plugin needs to listen for.

Event subscriptions are a convenient way to observe events generated elsewhere in Moodle.

Communication between components

You *should not* use event subscriptions to subscribe to events belonging to other plugins, without defining a dependency upon that plugin.

See the [Component communication principles](https://moodledev.io/general/development/policies/component-communication#event-observers) documentation for a description of some of the risks of doing so.

View example

\[path/to/plugintype]/pluginname/db/events.php

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
 * Event observer definitions for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$observers=[
[
'eventname'=>'\core\event\course_module_created',
'callback'=>'\plugintype_pluginname\event\observer\course_module_created::store',
'priority'=>1000,
],
];
```

### db/messages.php[​](#dbmessagesphp "Direct link to db/messages.php")

#### Message provider configuration

##### File path: /db/messages.php

The `db/messages.php` file allows you to declare the messages that your plugin sends.

See the [Message API](https://moodledev.io/docs/5.1/apis/core/message) documentation for further information.

View example

\[path/to/plugintype]/pluginname/db/messages.php

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
 * Message provider configuration for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$messageproviders=[
'things'=>[
'defaults'=>[
'airnotifier'=>MESSAGE_PERMITTED+MESSAGE_DEFAULT_ENABLED,
],
],
];
```

### db/services.php[​](#dbservicesphp "Direct link to db/services.php")

#### Web service function declarations

##### File path: /db/services.php

View example

\[path/to/plugintype]/pluginname/db/services.php

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
 * Web service function declarations for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$functions=[
'plugintype_pluginname_create_things'=>[
'classname'=>'plugintype_pluginname\external\create_things',
'description'=>'Create a new thing',
'type'=>'write',
'ajax'=>true,
'services'=>[
MOODLE_OFFICIAL_MOBILE_SERVICE,
],
],
];
```

### db/tasks.php[​](#dbtasksphp "Direct link to db/tasks.php")

#### Task schedule configuration

##### File path: /db/tasks.php

The `db/tasks.php` file contains the initial schedule configuration for each of your plugins *scheduled* tasks. Adhoc tasks are not run on a regular schedule and therefore are not described in this file.

Editing the schedule for an existing task

If an existing task is edited, it will only be updated in the database if the administrator has not customised the schedule of that task in any way.

The following fields also accept a value of `R`, which indicates that Moodle should choose a random value for that field:

- minute
- hour
- dayofweek
- day

See [db/tasks.php](https://moodledev.io/docs/5.1/apis/commonfiles/db-tasks.php) for full details of the file format.

View example

\[path/to/plugintype]/pluginname/db/tasks.php

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
 * Task schedule configuration for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$tasks=[
[
'classname'=>'mod_example\task\do_something',
'blocking'=>0,
'minute'=>'30',
'hour'=>'17',
'day'=>'*',
'month'=>'1,7',
'dayofweek'=>'0',
],
];
```

### db/renamedclasses.php[​](#dbrenamedclassesphp "Direct link to db/renamedclasses.php")

#### Renamed classes

##### File path: /db/renamedclasses.php

Details of classes that have been renamed to fit in with autoloading. See [forum discussion](https://moodle.org/mod/forum/discuss.php?d=262403) for details.

note

Adding renamed or moved classes to `renamedclasses.php` is only necessary when the class is part of the component's API where it can be reused by other components, especially by third-party plugins. This is to maintain backwards-compatibility in addition to autoloading purposes.

If the renamed or moved class is private/internal to the component and is not subject for external use, there is no need to add it to `renamedclasses.php`.

View example

\[path/to/plugintype]/pluginname/db/renamedclasses.php

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
 * Renamed classes for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL')||die;

$renamedclasses=[
'old_class_name'=>'fully_qualified\\new\\name',

// Examples:
'assign_header'=>'mod_assign\\output\\header',
'\assign_header'=>'mod_assign\\output\\header',
'\assign'=>'mod_assign\\assignment',

// Incorrect:
// The new class name should _not_ have a leading \.
'assign_header'=>'\\mod_assign\\output\\header',
];
```

### db/legacyclasses.php[​](#dblegacyclassesphp "Direct link to db/legacyclasses.php")

#### Legacy classes

##### File path: /db/legacyclasses.php

Details of legacy classes that have been moved to the classes directory to support autoloading but are not yet named properly.

note

Adding classes to `db/legacyclasses.php` is only necessary when the class is part of a *public* API, or the class name cannot be changed.

View example

\[path/to/plugintype]/pluginname/db/legacyclasses.php

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
 * Legacy classes for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL')||die;

$legacyclasses=[
'old_class_name'=>'path/within/classes/directory.php',

// Examples:
\coding_exception::class=>'exception/coding_exception.php',
\moodle_exception::class=>'exception/moodle_exception.php',

// Example loading a class from a different subsystem.
// This should typically only be used in core.
\cache::class=>[
'core_cache',// The name of the subsystem to load from.
'cache.php',// The file name within that filesystem's classes directory.
],
];
```

### classes/[​](#classes "Direct link to classes/")

#### Autoloaded classes

##### File path: /classes/

Moodle supports, and recommends, the use of autoloaded PHP classes.

By placing files within the `classes` directory or appropriate sub-directories, and with the correct PHP Namespace, and class name, Moodle is able to autoload classes without the need to manually require, or include them.

Details on these rules and conventions are available in the following documentation:

- [Coding style - namespace conventions](https://moodledev.io/general/development/policies/codingstyle#namespaces)
- [Automatic class loading](https://docs.moodle.org/dev/Automatic_class_loading)

### cli/[​](#cli "Direct link to cli/")

#### CLI scripts

##### File path: /cli/

For plugins which make use of [CLI scripts](https://docs.moodle.org/dev/CLI_scripts), the convention is that these are placed into the `cli` folder to make their purpose clear, and easy to find.

caution

All CLI scripts **must** declare themselves as being a CLI script by defining the `CLI_SCRIPT` constant to true before including `config.php`.

View example

\[path/to/plugintype]/pluginname/cli/

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
 * Example CLI script for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

define('CLI_SCRIPT',true);

require_once(__DIR__.'/../../config.php');
require_once("{$CFG->libdir}/clilib.php");

// Your CLI features go here.
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

Full details on how to create settings are available in the [Admin settings](https://moodledev.io/docs/5.1/apis/subsystems/admin) documentation.

### amd/[​](#amd "Direct link to amd/")

#### AMD JavaScript Modules

##### File path: /amd/src/example.js

JavaScript in Moodle is written in the ESM format, and transpiled into AMD modules for deployment.

The [Moodle JavaScript Guide](https://moodledev.io/docs/5.1/guides/javascript) has detailed information and examples on writing JavaScript in Moodle. Further information is also available in the [JavaScript Modules](https://moodledev.io/docs/5.1/guides/javascript/modules) documentation.

caution

Although the AMD module format is supported, all new JavaScript is written in the EcmaScript Module (ESM) format.

View example

\[path/to/plugintype]/pluginname/amd/src/example.js

```
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
 * Example module for the plugintype_pluginname plugin.
 *
 * @module   plugintype_pluginname/example
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

import{fetchThings}from'./repository';

exportconstupdateThings=(thingData)=>{
returnfetchThings(thingData);
};
```

### yui/[​](#yui "Direct link to yui/")

#### YUI JavaScript Modules

##### File path: /yui/

In older versions of Moodle, JavaScript was written in the YUI format. This is being phased out in favour of [JavaScript Modules](https://moodledev.io/docs/5.1/guides/javascript/modules), although some older uses still remain in Moodle core.

- [YUI/Modules](https://moodledev.io/docs/5.1/guides/javascript/yui/modules)
- [YUI](https://moodledev.io/docs/5.1/guides/javascript/yui)

caution

New YUI code will not be accepted into Moodle core, except for new plugins for the [Atto editor](https://moodledev.io/docs/5.1/apis/plugintypes/atto).

### backup/[​](#backup "Direct link to backup/")

#### Plugin Backup configuration

##### File path: /backup/

If your plugin stores data then you may need to implement the Backup feature which allows the activity to backed up, restored, and duplicated.

For more information on Backup and restore, see the following:

- [Backup 2.0 for developers](https://docs.moodle.org/dev/Backup_2.0_for_developers)
- [Restore 2.0 for developers](https://docs.moodle.org/dev/Restore_2.0_for_developers)

### styles.css[​](#stylescss "Direct link to styles.css")

#### CSS style sheet for your plugin

##### File path: /styles.css

Plugins may define a '/styles.css' to provide plugin-specific styling. See the following for further documentation:

- [Plugin contribution checklist#CSS styles](https://moodledev.io/general/community/plugincontribution/checklist#css-styles)
- [CSS Coding Style](https://docs.moodle.org/dev/CSS_Coding_Style)

Avoid custom styles where possible

Rather than writing custom CSS for your plugin, where possible apply Bootstrap classes to the DOM elements in your output. These will be easier to maintain and will adopt most colour, branding, and other customisations applied to a theme.

### pix/icon.svg[​](#pixiconsvg "Direct link to pix/icon.svg")

#### Plugins icons

##### File path: /pix/

Plugins can provide icons in several formats, and most plugin types require that a default icon be provided.

Where a browser supports it, the `svg` format is used, falling back to `png` formats when an SVG is unavailable.

Full details of the correct naming, sizing, and design guidelines for icons in Moodle can be found in the [Moodle icons](https://docs.moodle.org/dev/Moodle_icons) documentation.

### thirdpartylibs.xml[​](#thirdpartylibsxml "Direct link to thirdpartylibs.xml")

#### Details of third-party libraries included in the plugin

##### File path: /thirdpartylibs.xml

Details of all third-party libraries should be declared in the `thirdpartylibs.xml` file.

This information is used to generate ignore file configuration for linting tools. For Moodle core it is also used to generate library information as part of release notes and credits.

Within the XML the `location` is a file, or directory, relative to your plugin's root.

Licensing

The license of any third-party code included in your plugin, and within the `thirdpartylibs.xml` file **must** be [compatible with the GNU GPLv3](http://www.gnu.org/licenses/license-list.html#GPLCompatibleLicenses).

See the [Third Party Libraries](https://docs.moodle.org/dev/Third_Party_Libraries) documentation for further information.

View example

\[path/to/plugintype]/pluginname/thirdpartylibs.xml

```
<?xml version="1.0"?>
<libraries>
<library>
<location>javascript/html5shiv.js</location>
<name>Html5Shiv</name>
<version>3.6.2</version>
<license>Apache</license>
<licenseversion>2.0</licenseversion>
</library>
<library>
<location>vendor/guzzle/guzzle/</location>
<name>guzzle</name>
<version>v3.9.3</version>
<license>MIT</license>
<licenseversion></licenseversion>
</library>
</libraries>
```

### readme\_moodle.txt[​](#readme_moodletxt "Direct link to readme_moodle.txt")

#### Third-party library import instructions

##### File path: /\*/readme\_moodle.txt

When importing a third-party library into your plugin, it is advisable to create a `readme_moodle.txt` file detailing relevant information, including:

- Download URLs
- Build instructions

### upgrade.txt[​](#upgradetxt "Direct link to upgrade.txt")

#### Significant changes for each version of your plugin

##### File path: /\*/upgrade.txt

Each component and subsystem may make use of an `upgrade.txt` file in the top level folder. A section title is used to identify the Moodle version where the change was introduced, and significant changes for that version relating to that component or subsystem are noted.

For example, given an API change is applied for the upcoming Moodle version 4.1 which is still in the **main** branch (4.1dev), the version number on the `upgrade.txt`'s section title will be set to **4.1**.

Example 1: Change applied to the main branch

```
== 4.1 ==
An API change to empower educators!
```

#### Changes applied to multiple branches[​](#changes-applied-to-multiple-branches "Direct link to Changes applied to multiple branches")

When changes are integrated to multiple branches, for example a stable version and the main branch, then the relevant versions used to describe the change in the `upgrade.txt` file should be the next version to be released *for each branch*. The **main** branch should always use the next major version.

For example, if a change is applied to the **MOODLE\_400\_STABLE** during the development of Moodle 4.0.2, and the **main** branch during the development of Moodle 4.1, then the relevant versions will be **4.0.2** and **4.1**, respectively. The section title for the **main** branch will be the same as the one in Example 1. The section title for the **MOODLE\_400\_STABLE** branch will indicate the next upcoming minor version (4.0.2 in this case):

Example 2: Patch applied to main and MOODLE\_400\_STABLE

```
== 4.0.2 ==
An API change to empower educators!
```

#### Mentioning other Moodle versions the change applies to[​](#mentioning-other-moodle-versions-the-change-applies-to "Direct link to Mentioning other Moodle versions the change applies to")

Multiple versions within the section title are **not** allowed. However, developers may note the Moodle versions that the change applies to within the upgrade note text itself.

Example 3a: main (4.1dev)

```
== 4.1 ==
An API change to empower educators! (This was fixed in 4.1 and 4.0.2)
```

Example 3b: MOODLE\_400\_STABLE

```
== 4.0.2 ==
An API change to empower educators! (This was fixed in 4.1 and 4.0.2)
```

Example 3c: (INCORRECT) Multiple versions on the section title

```
== 4.1, 4.0.2 ==
An API change to empower educators!
```

#### Exception during parallel development[​](#exception-during-parallel-development "Direct link to Exception during parallel development")

When Moodle is developing two major versions in parallel, for example Moodle 3.11.0, and Moodle 4.0.0, then the version in the earliest of the major version development branches will be used for both branches.

For example, given we are in a parallel development situation with **MOODLE\_311\_STABLE** (3.11dev) and **main** (4.0dev), with Moodle 3.11 as the next upcoming major Moodle version. If an API change is applied to **MOODLE\_311\_STABLE**, the version number on the section title will be **3.11** for both **main** and **MOODLE\_400\_STABLE** branches.

Example 4a: main (4.0dev)

```
== 3.11 ==
An API change to empower educators!
```

Example 4b: MOODLE\_311\_STABLE (3.11dev)

```
== 3.11 ==
An API change to empower educators!
```

### environment.xml[​](#environmentxml "Direct link to environment.xml")

#### Plugin-specific environment requirements

##### File path: /environment.xml

A plugin can declare its own environment requirements, in addition to those declared by Moodle core. These may includes features such as PHP extension requirements, version requirements, and similar items.

Further information on this file and its format can be found in the [Environment checking](https://docs.moodle.org/dev/Environment_checking) documentation.

View example

\[path/to/plugintype]/pluginname/environment.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<COMPATIBILITY_MATRIX>
<PLUGINname="plugintype_pluginname">
<PHP_EXTENSIONS>
<PHP_EXTENSIONname="soap"level="required">
</PHP_EXTENSION>
</PHP_EXTENSIONS>
</PLUGIN>
</COMPATIBILITY_MATRIX>
```

### README[​](#readme "Direct link to README")

#### Plugin Information for Administrators

##### File path: /README

We recommend that you include any additional information for your plugin in a project readme file. Ideally this should act as an offline version of all information in your plugin's page in the [Plugins directory](https://moodledev.io/general/community/plugincontribution/pluginsdirectory).

We recommend creating your readme file in either a `README.md`, or `README.txt` format.

### CHANGES[​](#changes "Direct link to CHANGES")

#### Plugin changelog

##### File path: /CHANGES

If your plugin includes a changelog in its root directory, this will be used to automatically pre-fill the release notes field when uploading new versions of your plugin to the [Plugins directory](https://moodledev.io/general/community/plugincontribution/pluginsdirectory). This file can be in any of the following locations:

- `CHANGES.md`: as a markdown file; or
- `CHANGES.txt`: as a text file; or
- `CHANGES.html`: as an HTML file; or
- `CHANGES`: as a text file.

## See also[​](#see-also "Direct link to See also")

- [Moodle architecture](https://docs.moodle.org/dev/Moodle_architecture) - general overview of Moodle code architecture
- [Plugin types](https://moodledev.io/docs/5.1/apis/plugintypes) - list of all supported plugin types
- [Moodle plugins directory](https://moodle.org/plugins/) - repository of contributed plugins for Moodle
- [Moodle plugin skeleton generator](https://moodle.org/plugins/tool_pluginskel) - allows to quickly generate code skeleton for a new plugin
- [Checklist for plugin contributors](https://moodledev.io/general/community/plugincontribution/checklist) - read before submitting a plugin