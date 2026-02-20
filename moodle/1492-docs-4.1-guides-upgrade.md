---
title: Plugin Upgrades | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/guides/upgrade
source: sitemap
fetched_at: 2026-02-17T14:57:29.423582-03:00
rendered_js: false
word_count: 1290
summary: This document explains the Moodle Upgrade API and the necessary file structure for managing plugin installations and database schema migrations. It details the roles of versioning, installation XML, and upgrade scripts in maintaining plugin lifecycle and data consistency.
tags:
    - moodle-development
    - upgrade-api
    - database-migration
    - plugin-management
    - version-control
    - xmldb-editor
    - moodle-plugins
category: api
---

The Upgrade API is a core API which allows your plugin to manage features of its own installation, and upgrade. Every plugin includes a [version](https://moodledev.io/docs/4.1/apis/commonfiles/version.php) which allows the Upgrade API to apply only the required changes.

Correct use of this API allows Moodle to automatically create, and handle upgrades for, your database tables and other core features during an upgrade.

## Key files[​](#key-files "Direct link to Key files")

This process is controlled by three primary files within your plugin, and a number of additional optional files for optional features:

- [version.php](https://moodledev.io/docs/4.1/apis/commonfiles/version.php): This records the version of the plugin code. You must increase version in version.php after any change in the `/db/` folder, any change in JavaScript code, any new auto-loaded class, any new setting and also after any change in language pack, because a new version triggers the upgrade procedure and resets all caches.
- db/install.xml: This file describes the database tables that will be created during installation. It is only used during the initial installation of the plugin.
- db/upgrade.php: This file is used during the upgrade process when upgrading from an older version of the plugin installed upgrades to the latest version.

### version.php[​](#versionphp "Direct link to version.php")

The version.php file describes the current version of the plugin, and additional features such as its maturity, any dependencies or requirements, and a release name.

See the documentation on [version.php](https://moodledev.io/docs/4.1/apis/commonfiles/version.php) for further information on the features of this file.

### db/install.xml[​](#dbinstallxml "Direct link to db/install.xml")

The install.xml file describes the database tables that will be created when the plugin is installed.

important

The content of the `install.xml` file **must** be created and maintained using the [XMLDB Editor](https://moodledev.io/general/development/tools/xmldb).

### db/upgrade.php[​](#dbupgradephp "Direct link to db/upgrade.php")

The upgrade.php file describes the steps used to migrate the plugin from one version to a newer version. Moodle only supports the upgrade of plugins. **Plugins can not be downgraded**.

important

The content of the `upgrade.php` file **must** be created and maintained using the [XMLDB Editor](https://moodledev.io/general/development/tools/xmldb).

The following example shows the structure of the upgrade.php file:

Example upgrade.php file

```
<?php

function xmldb_[plugintype]_[pluginname]_upgrade($oldversion):bool{
global$CFG,$DB;

$dbman=$DB->get_manager();// Loads ddl manager and xmldb classes.

if($oldversion<2019031200){
// Perform the upgrade from version 2019031200 to the next version.

// The content of this section should be generated using the XMLDB Editor.
}

if($oldversion<2019031201){
// Perform the upgrade from version 2019031201 to the next version.

// The content of this section should be generated using the XMLDB Editor.
}

// Everything has succeeded to here. Return true.
returntrue;
}
```

## Upgrade code restrictions[​](#upgrade-code-restrictions "Direct link to Upgrade code restrictions")

During an upgrade, restrictions are placed on the functions that your upgrade code may call. This is because Moodle has not been fully update and some APIs may have code in place relating to a future database or data format.

- All upgrade code may use the [basic database API](https://moodledev.io/docs/4.1/apis/core/dml).
- In a **plugin**, upgrade code should not call **any plugin functions**. For example, if your plugin has a function that changes frog settings to 'green', and you need to do this during upgrade, then you **must not** call this function; instead, manually update the database rows so that the frog settings become green). However, **you *may* call core functions** rather than making core changes in database.
- In **core**, upgrade code should not even call **any core functions**. For example, if you need to add a calendar event, this should be done by inserting into a database table rather than calling a function to add the event. Certain functions marked with a comment such as `set_config` and `get_config` are excepted.

Rationale for these rules

During core upgrade the state is as follows:

- Core data: **Old**.
- Plugin data: **Old**.

Core functions expect core data to be in the Current state, so it is not safe to call them, unless the following is present in the function's docblock: "NOTE: this function is called from lib/db/upgrade.php".

During plugin upgrade the state is as follows:

- Core data: **Current**. (Because core upgrade runs before plugin upgrade.)
- Plugin data: **Old**.

Core functions are now safe to call because the core data is in Current state. But plugin functions, which expect data to be in the Current state, are not safe.

## Summary[​](#summary "Direct link to Summary")

The first time a user installs any version of your plugin, the install.xml file will be used to create all the required database tables. Therefore install.xml should always contain the definition of the up-to-date database structure. Moodle recognises this situation because there is a version.php file on disc, but there is no (*plugintype*\_*pluginname*, version) value in the config\_plugins table.

If the user already had a version of your plugin installed, and then upgrades to a newer version, Moodle will detect this because the version.php file will contain a newer version number than the (*plugintype*\_*pluginname*, version) value in the mdl\_config\_plugins table. In this case, Moodle will run the code in the upgrade.php file, passing in the old version number, so that the correct bits of upgrade can be run, as controlled by the if ($oldversion &lt; XXXXXXXXXX) blocks of code.

The contents of the install.xml and upgrade.php files should be generated using the XMLDB editor.

## Other things that can be in the db folder[​](#other-things-that-can-be-in-the-db-folder "Direct link to Other things that can be in the db folder")

See the documentation on other [common files](https://moodledev.io/docs/4.1/apis/commonfiles) that may be of use to you, in particular the following may be useful:

- [install.php](https://moodledev.io/docs/4.1/apis/commonfiles#dbinstallphp)
- [uninstall.php](https://moodledev.io/docs/4.1/apis/commonfiles#dbuninstallphp)
- [access.php](https://moodledev.io/docs/4.1/apis/commonfiles#dbaccessphp)
- [events.php](https://moodledev.io/docs/4.1/apis/commonfiles#dbeventsphp)
- [messages.php](https://moodledev.io/docs/4.1/apis/commonfiles#dbmessagesphp)
- [services.php](https://moodledev.io/docs/4.1/apis/commonfiles#dbservicesphp)
- [subplugins.json](https://docs.moodle.org/dev/Subplugins#db.2Fsubplugins.json)
- [Language files](https://moodledev.io/docs/4.1/apis/commonfiles#langenplugintype_pluginnamephp)

## Upgrade API Cheat-sheet[​](#upgrade-api-cheat-sheet "Direct link to Upgrade API Cheat-sheet")

The Upgrade API is related to *a lot* of different files and APIs (including access, event, log, webservice, and so on) as it's the API used to install and upgrade all of those areas in the context of a specific Moodle component. The previous sections have tried to list all those dependencies when possible.

The Upgrade API makes *very intensive use* of other APIs, including [DDL](https://moodledev.io/docs/4.1/apis/core/dml/ddl), [DML](https://moodledev.io/docs/4.1/apis/core/dml), and a range of tools in order to proceed with the required changes for the upgrade.

In addition to the relevant files located in the db folder, a number of functions can also be defined:

- **xmldb\_(main|[frankenstyle](https://moodledev.io/general/development/policies/codingstyle/frankenstyle))\_install()**: to be used in install.php files.
- **xmldb\_(main|frankenstyle)\_uninstall()**: to be used in uninstall.php files.
- **xmldb\_(main|frankenstyle)\_upgrade()**: to be used in upgrade.php files.

info

Some of these functions have variants depending on whether they are being called from core code, or a plugin.

When called from core, the `main` variant should be used, otherwise the frankenstyle name of teh component should be used.

For example, if you are defining an installation behaviour in the install.php script of a block named `block_exampke`, you would have an install.php similar to the following:

blocks/example/db/install.php

```
<?php
// ...

functionxmldb_block_example_install(){
// ...
}
```

We highly recommend looking at existing uses of these files within plugins included with Moodle core to understand some fo the more complex examples.

### Upgrade helpers[​](#upgrade-helpers "Direct link to Upgrade helpers")

Several functions are also available to call from within the upgrade.php script:

- **upgrade\_set\_timeout()**: Used to increase timeouts before performing a long-running upgrade step
- **upgrade\_(main|mod|block|plugin)\_savepoint()**: Used to mark an upgrade step as completed, and to reset timeouts. This ensures that an upgrade step is only executed once.

## Moodle core database upgrades within stable branches[​](#moodle-core-database-upgrades-within-stable-branches "Direct link to Moodle core database upgrades within stable branches")

In Moodle core, one of the standard simple rules is not to make any database changes on a stable branch. You only need to read this section in the rare situations where a database change on the stable branch is unavoidable.

Advanced

Suppose, in order to fix a bug, you need to make a database change in the Moodle 4.0 stable branch (and the main branch targetting Moodle 4.1). The root of the problem is that people may upgrade their Moodle in three different ways, which

- Upgrade from &lt;=4.0.2 to 4.0.3 - this executes the upgrade script on the 4.0 branch.
- Upgrade from &lt;=4.0.2 directly to &gt;=4.1 - this executes the upgrade script on the main branch.
- Upgrade from 4.0.3 to &gt;=4.1 - in this case, you must ensure that the upgrade on main is not executed.

The normal way to do this is ensure that your database upgrade is idempotent. That is, it does not matter if you do it twice. So for example, instead of doing

An example of incorrect behaviour

Creating a table without checks

```
$dbman->create_table($table);
```

you should do

An example of correct behaviour

Ensure that the table does not exist before creating it

```
if(!$dbman->table_exists($table)){
$dbman->create_table($table);
}
```

You should also think about what version numbers to put in your version.php file on each branch. Above all, test carefully.

## See also[​](#see-also "Direct link to See also")

- [Core APIs](https://moodledev.io/docs/4.1/apis)
- [XMLDB Documentation](https://docs.moodle.org/dev/XMLDB_Documentation)
- [Coding guidelines](https://moodledev.io/general/development/policies)
- [DDL functions](https://moodledev.io/docs/4.1/apis/core/dml/ddl)
- [install.xml file documentation](https://docs.moodle.org/dev/XMLDB_defining_an_XML_structure)