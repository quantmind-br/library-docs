---
title: Activity modules | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/plugintypes/mod
source: sitemap
fetched_at: 2026-02-17T14:55:32.265634-03:00
rendered_js: false
word_count: 1616
summary: Explains the fundamental structure, file layout, and mandatory configuration files required to develop activity modules for the Moodle learning platform.
tags:
    - moodle
    - activity-modules
    - plugin-development
    - file-structure
    - database-schema
    - access-control
category: guide
---

Activity modules are a fundamental course feature and are usually the primary delivery method for learning content in Moodle.

The plugintype of an Activity module is `mod`, and the frankenstyle name of a plugin is therefore `mod_[modname]`.

All activity module plugins are located in the `/mod/` folder of Moodle.

note

The term `[modname]` is used as a placeholder in this documentation and should be replaced with the name of your activity module.

## Folder layout[​](#folder-layout "Direct link to Folder layout")

Activity modules reside in the `/mod` directory.

Each module is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

Below is an example of the file structure for the `folder` plugin.

View an example directory layout for the `folder` plugin.

```
.
├── backup
│   ├── moodle1
│   │   └── lib.php
│   └── moodle2
│       ├── backup_folder_activity_task.class.php
│       ├── backup_folder_stepslib.php
│       ├── restore_folder_activity_task.class.php
│       └── restore_folder_stepslib.php
├── classes
│   ├── analytics
│   │   └── indicator
│   │       ├── activity_base.php
│   │       ├── cognitive_depth.php
│   │       └── social_breadth.php
│   ├── content
│   │   └── exporter.php
│   ├── event
│   │   ├── all_files_downloaded.php
│   │   ├── course_module_instance_list_viewed.php
│   │   ├── course_module_viewed.php
│   │   └── folder_updated.php
│   ├── external.php
│   ├── privacy
│   │   └── provider.php
│   └── search
│       └── activity.php
├── db
│   ├── access.php
│   ├── install.php
│   ├── install.xml
│   ├── log.php
│   ├── services.php
│   └── upgrade.php
├── download_folder.php
├── edit.php
├── edit_form.php
├── index.php
├── lang
│   └── en
│       └── folder.php
├── lib.php
├── locallib.php
├── mod_form.php
├── module.js
├── phpunit.xml
├── pix
│   ├── icon.png
│   └── icon.svg
├── readme.txt
├── renderer.php
├── settings.php
├── styles.css
├── tests
│   ├── backup
│   │   └── restore_date_test.php
│   ├── behat
│   │   └── folder_activity_completion.feature
│   ├── event
│   │   └── events_test.php
│   ├── externallib_test.php
│   ├── generator
│   │   └── lib.php
│   ├── generator_test.php
│   ├── lib_test.php
│   ├── phpunit.xml
│   └── search
│       └── search_test.php
├── version.php
└── view.php
```

## Standard Files and their Functions[​](#standard-files-and-their-functions "Direct link to Standard Files and their Functions")

There are several files that are crucial to Moodle. These files are used to install your module and then integrate it into Moodle. Each file has a particular function, some of the files are optional, and are only created if you want to use the functionality it offers. Below are the list of most commonly used files.

### Backup Folder[​](#backup-folder "Direct link to Backup Folder")

#### Plugin Backup configuration

##### File path: /backup/

If your plugin stores data then you may need to implement the Backup feature which allows the activity to backed up, restored, and duplicated.

For more information on Backup and restore, see the following:

- [Backup 2.0 for developers](https://docs.moodle.org/dev/Backup_2.0_for_developers)
- [Restore 2.0 for developers](https://docs.moodle.org/dev/Restore_2.0_for_developers)

### `access.php` - Capability defaults[​](#accessphp---capability-defaults "Direct link to accessphp---capability-defaults")

#### Plugin capabilities

##### File path: /db/access.php

The `db/access.php` file contains the **initial** configuration for a plugin's access control rules.

Access control is handled in Moodle by the use of Roles, and Capabilities. You can read more about these in the [Access API](https://moodledev.io/docs/4.1/apis/subsystems/access) documentation.

Changing initial configuration

If you make changes to the initial configuration of *existing* access control rules, these will only take effect for *new installations of your plugin*. Any existing installation **will not** be updated with the latest configuration.

Updating existing capability configuration for an installed site is not recommended as it may have already been modified by an administrator.

For activities the following capabilities are *required*:

- `mod/[modname]:addinstance`: Controls whether a user may create a new instance of the activity
- `mod/[modname]:view`: Controls whether a user may view an instance of the activity

The example below shows the recommended configuration for the `addinstance` and `view` capabilities.

This configuration will allow:

- editing teachers and managers to create new instances, but not non-editing teachers.
- all roles to view the activity.

important

Granting the view capability to archetypes like `guest` does not allow any user to view all activities. Users are still subject to standard access controls like course enrolment.

For further information on what each attribute in that capabilities array means visit [NEWMODULE Adding capabilities](https://docs.moodle.org/dev/NEWMODULE_Adding_capabilities).

View example

public/mod/\[modname]/db/access.php

```
<?php
$capabilities=[
'mod/[modname]:addinstance'=>[
'riskbitmask'=>RISK_XSS,
'captype'=>'write',
'contextlevel'=>CONTEXT_COURSE,
'archetypes'=>[
'editingteacher'=>CAP_ALLOW,
'manager'=>CAP_ALLOW,
],
'clonepermissionsfrom'=>'moodle/course:manageactivities',
],
'mod/[modname]:view'=>[
'captype'=>'read',
'contextlevel'=>CONTEXT_MODULE,
'archetypes'=>[
'guest'=>CAP_ALLOW,
'student'=>CAP_ALLOW,
'teacher'=>CAP_ALLOW,
'editingteacher'=>CAP_ALLOW,
'manager'=>CAP_ALLOW,
],
],
];
```

### `events.php` - Event observers[​](#eventsphp---event-observers "Direct link to eventsphp---event-observers")

&lt; DbEventsPHP /&gt;

### `install.xml` - Database installation[​](#installxml---database-installation "Direct link to installxml---database-installation")

#### Database schema

##### File path: /db/install.xml

The `install.xml` file is used to define any database tables, fields, indexes, and keys, which should be created for a plugin during its initial installation.

caution

When creating or updating the `install.xml` you **must** use the built-in [XMLDB editor](https://docs.moodle.org/dev/XMLDB_Documentation) within Moodle.

Moodle requires that you create a table for your plugin whose name exactly matches the plugin name. For example, the `certificate` activity module *must* have a database table named `certificate`. Certain fields within this table are also *required*:

Field namePropertiesKeys / IndexesNotes`id``INT(10), auto sequence`primary key for the table`course``INT(10)`foreign key to the `course` table`name``CHAR(255)`Holds the user-specified name of the activity instance`timemodified``INT(10)`The timestamp of when the activity was last modified`intro``TEXT`A standard field to hold the user-defined activity description (see `FEATURE_MOD_INTRO`)`introformat``INT(4)`A standard field to hold the format of the field

### `upgrade.php` - Upgrade steps[​](#upgradephp---upgrade-steps "Direct link to upgradephp---upgrade-steps")

#### Upgrade steps

##### File path: /db/upgrade.php

The `db/upgrade.php` file contains upgrade steps, including database schema changes, changes to settings, and other steps which must be performed during upgrade.

See the [Upgrade API](https://moodledev.io/docs/4.1/guides/upgrade) documentation for further information.

Generating Database Schema changes

When making changes to the database schema you **must** use the build-in [XMLDB editor](https://docs.moodle.org/dev/XMLDB_Documentation) within Moodle. This can be used to generate php upgrade steps.

The [install.xml](https://moodledev.io/docs/4.1/apis/commonfiles#dbinstallxml) schema must match the schema generated by the upgrade at all times.

To create an upgrade step you must:

1. Use the [XMLDB editor](https://moodledev.io/general/development/tools/xmldb) to create the definition of the new fields
2. Update the `install.xml` from the XMLDB editor
3. Generate the PHP upgrade steps from within the XMLDB Editor
4. Update the version number in your `version.php`

tip

In many cases you will be able to combine multiple upgrade steps into a single version change.

When a version number increment is detected during an upgrade, the `xmldb_[pluginname]_upgrade` function is called with the old version number as the first argument.

See the [Upgrade API](https://moodledev.io/docs/4.1/guides/upgrade) documentation for more information on the upgrade process.

View example

public/mod/\[modname]/db/upgrade.php

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
 * Upgrade steps for the mod_[modname] plugin.
 *
 * @package   mod_[modname]
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
}
```

### `mobile.php` - Moodle Mobile Remote Add-ons[​](#mobilephp---moodle-mobile-remote-add-ons "Direct link to mobilephp---moodle-mobile-remote-add-ons")

#### MoodleMobile version of the plugin

##### File path: /db/mobile.php

The Moodle Mobile remote add-on is the mobile app version of the plugin that will be loaded when a user accesses the plugin on the app.

A plugin can include several Mobile add-ons. Each add-on must indicate a unique name.

See the [Moodle App Plugins development guide](https://moodledev.io/general/app/development/plugins-development-guide) for more information on configuring your plugin for the Moodle App.

### `/lang/en/mod_[modname].php` - Language string definitions[​](#langenmod_modnamephp---language-string-definitions "Direct link to langenmod_modnamephp---language-string-definitions")

#### Language files

##### File path: /lang/en/\[modname].php

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

public/mod/\[modname]/lang/en/\[modname].php

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
 * Languages configuration for the mod_[modname] plugin.
 *
 * @package   mod_[modname]
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['pluginname']='The name of your activity';
```

### `lib.php` - Library functions[​](#libphp---library-functions "Direct link to libphp---library-functions")

#### Global plugin functions

##### File path: /lib.php

The `lib.php` file is a legacy file which acts as a bridge between Moodle core, and the plugin. In recent plugins it is should only used to define callbacks and related functionality which currently is not supported as an auto-loadable class.

All functions defined in this file **must** meet the requirements set out in the relevant section of the [Coding style](https://moodledev.io/general/development/policies/codingstyle#functions-and-methods).

Performance impact

Moodle core often loads all the `lib.php` files of a given plugin types. For performance reasons, it is strongly recommended to keep this file as small as possible and have just required code implemented in it. All the plugin's internal logic should be implemented in the auto-loaded classes.

For an Activity, you *must* define the following three functions, which are described below:

mod/\[modname]/lib.php

```
function[modname]_add_instance($instancedata,$mform=null):int;
function[modname]_update_instance($instancedata,$mform):bool;
function[modname]_delete_instance($id):bool;
```

- The `[modname]_add_instance()` function is called when the activity creation form is submitted. This function is only called when adding an activity and should contain any logic required to add the activity.
- The `[modname]_update_instance()` function is called when the activity editing form is submitted.
- The `[modname]_delete_instance()` function is called when the activity deletion is confirmed. It is responsible for removing all data associated with the instance.

note

The `lib.php` file is one of the older parts of Moodle and functionality is gradually being migrated to class-based function calls.

### `mod_form.php` - Instance create/edit form[​](#mod_formphp---instance-createedit-form "Direct link to mod_formphp---instance-createedit-form")

#### Activity creation/editing form

##### File path: /mod\_form.php

This file is used when adding/editing a module to a course. It contains the elements that will be displayed on the form responsible for creating/installing an instance of your module. The class in the file should be called `mod_[modname]_mod_form`.

warning

The `mod_[modname]_mod_form` is a current exception to the class autoloading rules.

This will be addressed in [MDL-74472](https://moodle.atlassian.net/browse/MDL-74472).

info

The following example gives a sample implementation of the creation form. It does **not** contain the full file.

View example

public/mod/\[modname]/mod\_form.php

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
 * Activity creation/editing form for the mod_[modname] plugin.
 *
 * @package   mod_[modname]
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

require_once($CFG->dirroot.'/course/moodleform_mod.php');
require_once($CFG->dirroot.'/mod/certificate/lib.php');

classmod_certificate_mod_formextendsmoodleform_mod{

functiondefinition(){
global$CFG,$DB,$OUTPUT;

$mform=&$this->_form;

$mform->addElement('text','name',get_string('certificatename','certificate'),['size'=>'64']);
$mform->setType('name',PARAM_TEXT);
$mform->addRule('name',null,'required',null,'client');

$ynoptions=[
0=>get_string('no'),
1=>get_string('yes'),
];
$mform->addElement('select','usecode',get_string('usecode','certificate'),$ynoptions);
$mform->setDefault('usecode',0);
$mform->addHelpButton('usecode','usecode','certificate');

$this->standard_coursemodule_elements();

$this->add_action_buttons();
}

}
```

### `index.php` - Instance list[​](#indexphp---instance-list "Direct link to indexphp---instance-list")

#### Activity index

##### File path: /index.php

The `index.php` should be used to list all instances of an activity that the current user has access to in the specified course.

View example

public/mod/\[modname]/index.php

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
 * Activity index for the mod_[modname] plugin.
 *
 * @package   mod_[modname]
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

require_once('../../config.php');

// The `id` parameter is the course id.
$id=required_param('id',PARAM_INT);

// Fetch the requested course.
$course=$DB->get_record('course',['id'=>$id],'*',MUST_EXIST);

// Require that the user is logged into the course.
require_course_login($course);

$modinfo=get_fast_modinfo($course);

foreach($modinfo->get_instances_of('[modinfo]')as$instanceid=>$cm){
// Display information about your activity.
}
```

### `view.php` - View an activity[​](#viewphp---view-an-activity "Direct link to viewphp---view-an-activity")

#### Activity view page

##### File path: /view.php

Moodle will automatically generate links to view the activity using the `/view.php` page and passing in an `id` value. The `id` passed is the course module ID, which can be used to fetch all remaining data for the activity instance.

View example

\[path/to/plugintype]/pluginname/view.php

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
 * Activity view page for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

require('../../config.php');

$id=required_param('id',PARAM_INT);
[$course,$cm]=get_course_and_cm_from_cmid($id,'[modname]');
$instance=$DB->get_record('[modname]',['id'=>$cm->instance],'*',MUST_EXIST);
```

### `version.php`[​](#versionphp "Direct link to versionphp")

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

public/mod/\[modname]/version.php

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
 * Version metadata for the mod_[modname] plugin.
 *
 * @package   mod_[modname]
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

## See also[​](#see-also "Direct link to See also")

- [Tutorial](https://docs.moodle.org/dev/Tutorial)
- [Module visibility and display](https://docs.moodle.org/dev/Module_visibility_and_display)