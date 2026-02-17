---
title: Block plugins | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/plugintypes/blocks
source: sitemap
fetched_at: 2026-02-17T15:11:54.047421-03:00
rendered_js: false
word_count: 2077
summary: This document outlines the file structure and mandatory components required to develop block plugins in Moodle, covering the block definition class, access control, and metadata files.
tags:
    - moodle-development
    - block-plugins
    - plugin-architecture
    - php
    - access-control
    - moodle-api
category: guide
---

Block plugins allow you to show supplemental information, and features, within different parts of Moodle.

## File structure[​](#file-structure "Direct link to File structure")

Blocks plugins are located in the `/blocks` directory.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

View an example directory layout for the `block_pluginname` plugin.

```
 blocks/pluginname/
 |-- db
 |   `-- access.php
 |-- lang
 |   `-- en
 |       `-- block_pluginname.php
 |-- pix
 |   `-- icon.png
 |-- block_pluginname.php
 |-- edit_form.php (optional)
 `-- version.php
```

### block\_pluginname.php[​](#block_pluginnamephp "Direct link to block_pluginname.php")

#### Block definition class

##### File path: /block\_pluginname.php

This file will hold the class definition for the block, and is used both to manage it as a plugin and to render it onscreen.

View example

public/blocks/pluginname/block\_pluginname.php

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
 * Block definition class for the block_pluginname plugin.
 *
 * @package   block_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

classblock_pluginnameextendsblock_base{

/**
     * Initialises the block.
     *
     * @return void
     */
publicfunctioninit(){
$this->title=get_string('pluginname','block_pluginname');
}

/**
     * Gets the block contents.
     *
     * @return string The block HTML.
     */
publicfunctionget_content(){
global$OUTPUT;

if($this->content!==null){
return$this->content;
}

$this->content=newstdClass();
$this->content->footer='';

// Add logic here to define your template data or any other content.
$data=['YOUR DATA GOES HERE'];

$this->content->text=$OUTPUT->render_from_template('block_yourplugin/content',$data);

return$this->content;
}

/**
     * Defines in which pages this block can be added.
     *
     * @return array of the pages where the block can be added.
     */
publicfunctionapplicable_formats(){
return[
'admin'=>false,
'site-index'=>true,
'course-view'=>true,
'mod'=>false,
'my'=>true,
];
}
}
```

info

The `init` method is essential for all blocks, and its purpose is to give values to any class member variables that need instantiating.

### db/access.php[​](#dbaccessphp "Direct link to db/access.php")

#### Plugin capabilities

##### File path: /db/access.php

The `db/access.php` file contains the **initial** configuration for a plugin's access control rules.

Access control is handled in Moodle by the use of Roles, and Capabilities. You can read more about these in the [Access API](https://moodledev.io/docs/4.5/apis/subsystems/access) documentation.

Changing initial configuration

If you make changes to the initial configuration of *existing* access control rules, these will only take effect for *new installations of your plugin*. Any existing installation **will not** be updated with the latest configuration.

Updating existing capability configuration for an installed site is not recommended as it may have already been modified by an administrator.

View example

public/blocks/pluginname/db/access.php

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
 * Plugin capabilities for the block_pluginname plugin.
 *
 * @package   block_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$capabilities=[
'block/pluginname:myaddinstance'=>[
'captype'=>'write',
'contextlevel'=>CONTEXT_SYSTEM,
'archetypes'=>[
'user'=>CAP_ALLOW
],
'clonepermissionsfrom'=>'moodle/my:manageblocks'
],
'block/pluginname:addinstance'=>[
'riskbitmask'=>RISK_SPAM|RISK_XSS,
'captype'=>'write',
'contextlevel'=>CONTEXT_BLOCK,
'archetypes'=>[
'editingteacher'=>CAP_ALLOW,
'manager'=>CAP_ALLOW
],
'clonepermissionsfrom'=>'moodle/site:manageblocks'
],
];
```

### lang/en/block\_pluginname.php[​](#langenblock_pluginnamephp "Direct link to lang/en/block_pluginname.php")

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

public/blocks/pluginname/lang/en/plugintype\_pluginname.php

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
 * Languages configuration for the block_pluginname plugin.
 *
 * @package   block_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['pluginname']='Pluginname block';
$string['pluginname']='Pluginname';
$string['pluginname:addinstance']='Add a new pluginname block';
$string['pluginname:myaddinstance']='Add a new pluginname block to the My Moodle page';
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

public/blocks/pluginname/version.php

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
 * Version metadata for the block_pluginname plugin.
 *
 * @package   block_pluginname
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

### edit\_form.php[​](#edit_formphp "Direct link to edit_form.php")

#### Block edit form class

##### File path: /edit\_form.php

This file is only needed if your plugin has a specific configuration form. It is not required for most plugins. We can extend this configuration form, and add custom preferences fields, so that users can better tailor our block to a given task or page.

View example

public/blocks/pluginname/edit\_form.php

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
 * Block edit form class for the block_pluginname plugin.
 *
 * @package   block_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

classblock_pluginname_edit_formextendsblock_edit_form{
protectedfunctionspecific_definition($mform){
// Section header title according to language file.
$mform->addElement('header','config_header',get_string('blocksettings','block'));
// A sample string variable with a default value.
$mform->addElement('text','config_text',get_string('blockstring','block_pluginname'));
$mform->setDefault('config_text','default value');
$mform->setType('config_text',PARAM_TEXT);
}
}
```

The example below adds a text attribute to the block instance settings.

caution

All your field names need to start with **"config\_"**, otherwise they will not be saved and will not be available within the block via $this-&gt;config.

## Creating a new block plugin[​](#creating-a-new-block-plugin "Direct link to Creating a new block plugin")

The easiest way to create a new block plugin is by using the latest version of [Tool Pluginskel](https://moodle.org/plugins/tool_pluginskel). You can use the following yaml file to generate a basic block skeleton.

View pluginskel recipe

```
## This is an example recipe file that you can use as a template for your own plugins.
## See the list of all files it would generate:
##
##     php generate.php example.yaml --list-files
##
## View a particular file contents without actually writing it to the disk:
##
##     php generate.php example.yaml --file=version.php
##
## To see the full list of options, run:
##
##     php generate.php --help
##
---
## Frankenstyle component name.
component: block_pluginname

## Human readable name of the plugin.
name: Example block

## Human readable release number.
release:"0.1.0"

## Plugin version number, e.g. 2016062100. Will be set to current date if left empty.
#version: 2016121200

## Required Moodle version, e.g. 2015051100 or "2.9".
requires:"3.11"

## Plugin maturity level. Possible options are MATURIY_ALPHA, MATURITY_BETA,
## MATURITY_RC or MATURIY_STABLE.
maturity: MATURITY_BETA

## Copyright holder(s) of the generated files and classes.
copyright: Year, You Name <your@email.address>

## Features flags can control generation of optional files/code fragments.
features:
readme:true
license:true

## Privacy API implementation
privacy:
haspersonaldata:false
uselegacypolyfill:false

block_features:
## Creates the file edit_form.php
edit_form:true

## Allows multiple instances of the block on the same course.
instance_allow_multiple:false

## Choose where to display the block.
applicable_formats:
-page: all
allowed:false
-page: course-view
allowed:true
-page: course-view-social
allowed:false

## Backup the block plugin.
backup_moodle2:
restore_task:true
restore_stepslib:true
backup_stepslib:true
settingslib:true
backup_elements:
-name: elt
restore_elements:
-name: elt
path: /path/to/file

## Capabilities defined by the plugin.
capabilities:
## Required by block plugins.
-name: myaddinstance
title: Add a new pluginname block to the My dashboard
captype: write
contextlevel: CONTEXT_SYSTEM
archetypes:
-role: user
permission: CAP_ALLOW
clonepermissionsfrom: moodle/my:manageblocks

-name: addinstance
title: Add a new pluginname block
captype: write
contextlevel: CONTEXT_BLOCK
archetypes:
-role: editingteacher
permission: CAP_ALLOW
-role: manager
permission: CAP_ALLOW
clonepermissionsfrom: moodle/site:manageblocks

## Explicitly added strings
lang_strings:
-id: mycustomstring
text: You can add 'extra' strings via the recipe file.
-id: mycustomstring2
text: Another string with {$a->some} placeholder.
```

## Block base class API methods[​](#block-base-class-api-methods "Direct link to Block base class API methods")

All blocks must provide a main class that extends the core block class. However, there are two different types of blocks:

- `block_base` - The default base class for content blocks.
- `block_list` - For blocks that displays a list items.

Depending on your plugin needs your main class in `blocks/pluginname/block_pluginname.php` must extend either `block_base` or `block_list`.

### Block class attributes[​](#block-class-attributes "Direct link to Block class attributes")

Once the block instance is created, there are several $this attributes that can be used:

- `$this->config` The block instance configuration. By default it is an empty object but if the block has an [edit\_form.php](#edit_formphp) file, it will be an object with the form data.
- `$this->content` This variable holds all the actual content that is displayed inside each block. Valid values for it are either NULL or an object of class stdClass, which must have specific member variables depending on the extended block base class.
- `$this->page` The page object that the block is being displayed on.
- `$this->context` The context object that the block is being displayed in.
- `$this->title` The title of the block.

### init()[​](#init "Direct link to init()")

The init method is called before the block is displayed. It is essential for all blocks, and its purpose is to give values to any class member variables that need instantiating. However, it is called before $this-&gt;config is set, if your plugin needs some configation value to define global attributes like the block title, it should be done in the specialization method.

### specialization()[​](#specialization "Direct link to specialization()")

This function is called on your subclass right after an instance is loaded. It is used to customize the title and other block attributes depending on the page type, context, configuration, etc.

View example

Example of a specialization method using the instance configuration.

```
functionspecialization(){
if(isset($this->config->title)){
$this->title=format_string($this->config->title,true,['context'=>$this->context]);
}else{
$this->title=get_string('newhtmlblock','block_html');
}
}
```

### get\_content(): string[​](#get_content-string "Direct link to get_content(): string")

In order to get our block to actually display something on screen, we need to add one more method to our class (before the final closing brace in our file) inside of the block\_pluginname.php script.

- block\_base block
- block\_list block

```
classblock_pluginnameextendsblock_base{

// (...)

publicfunctionget_content(){
if($this->content!==null){
return$this->content;
}

$this->content=newstdClass;
$this->content->text='The content of pluginname block';
$this->content->footer='Footer here...';

return$this->content;
}
}
```

caution

The get\_content can be called several times during the page rendering. To prevent your class from calculating it every time your plugin should check if $this-&gt;content is already defined at the beginning of the method.

tip

If the block content is empty (an empty string) the block will not be displayed. In the case of an extending block\_base block this means empty the `$this->content->text` and the `$this->content->footer` values. In a block\_list block, the `$this->content->items` array should be empty. Moodle performs this check by calling the block's `is_empty()` method, and if the block is indeed empty then it is not displayed at all.

### applicable\_formats(): array[​](#applicable_formats-array "Direct link to applicable_formats(): array")

Blocks can be added to any kind of page. However, some blocks may only be displayed on certain page types. This method is used to define the page types that the block can be displayed on. See [Limit the block to specific contexts](#limit-the-block-to-specific-contexts) section below for more information.

### instance\_allow\_multiple()[​](#instance_allow_multiple "Direct link to instance_allow_multiple()")

By default, only one instance of each block plugin can be added to a page. However, if your plugin allows multiple instances you can overrdie the instance\_allow\_multiple method.

View example

```
publicfunctioninstance_allow_multiple(){
returntrue;
}
```

note

Even if a block itself allows multiple instances in the same page, the administrator still has the option of disallowing such behavior. This setting can be set separately for each block from the Administration / Configuration / Blocks page.

Using this method each block instance can decide if the standard block header is shown or not. This method will be ignored in edit mode.

View example

```
publicfunctionhide_header(){
returntrue;
}
```

### html\_attributes(): array[​](#html_attributes-array "Direct link to html_attributes(): array")

The block base class can inject extra HTML attributes to the block wrapper. This is useful for example to add a class to the block wrapper when the block is being displayed in a specific context.

By default, each block section in the page will use a standard `block` class and the specific `block_pluginname` class. However, if you want to add a class to the block wrapper, you can override html\_attributes to alter those attrributes.

View example

```
publicfunctionhtml_attributes(){
// Get default values.
$attributes=parent::html_attributes();
// Append our class to class attribute.
$attributes['class'].=' block_'.$this->name();
return$attributes;
}
```

This results in the block having all its normal HTML attributes, as inherited from the base block class, plus our additional class name. We can now use this class name to change the style of the block, add JavaScript events to it via YUI, and so on. And for one final elegant touch, we have not set the class to the hard-coded value "block\_simplehtml", but instead used the Blocks/Appendix\_A#name.28.29| name() method to make it dynamically match our block's name.

### instance\_config\_save(): stdClass[​](#instance_config_save-stdclass "Direct link to instance_config_save(): stdClass")

An optional method to modify the instance configuration before it is saved. See [add instance configuration settings](#add-instance-configuration-settings) section below for more information.

### has\_config(): bool[​](#has_config-bool "Direct link to has_config(): bool")

An optional method to tell Moodle that the block has a global configuration settings form. See [enabling Global Configuration](#enabling-global-configuration) section below for more information.

## Add instance configuration settings[​](#add-instance-configuration-settings "Direct link to Add instance configuration settings")

By default, block instances have no configuration settings. If you want to add some, you can add them by adding a few methods and classes to your block.

### Create an edit\_form.php file[​](#create-an-edit_formphp-file "Direct link to Create an edit_form.php file")

To have a configuration form, you need to add an [edit\_form.php](#edit_formphp) file into your plugin. After defining the configuration, your block's base instance will have all your settings in its [$this-&gt;config attribute](#block-class-attributes). See the [edit\_form.php section above](#edit_formphp) for an example.

caution

Note that $this-&gt;config is available in all block methods **except the init() one**. This is because init() is called immediately as the block is being created, with the purpose of setting things up. Use [specialization](#specialization) instead.

note

You cannot use the 'checkbox' element in the form (once set it will stay set). You must use advcheckbox instead.

### Optional instance\_config\_save method[​](#optional-instance_config_save-method "Direct link to Optional instance_config_save method")

By default, all config\_* settings will be stored in the `block_instances` table. The complete form data will be encoded in base64 before storing it in the `configdata` field. Every time a block instance is initialized all that data will be decoded in the [$this-&gt;config attribute](#block-class-attributes).

However, for some cases like the Atto HTML editor, you may want to store them in the database instead, or to alter the config data before storing it. In that case you can create a instance\_config\_save method.

View example

```
publicfunctioninstance_config_save($data,$nolongerused=false){
// Example of add new data.
$data->somenewattribute='Some new value';

// Example of alter the current data.
$data->text='Some new text';

// Call the parent method to the data inside block_instance.configdata.
returnparent::instance_config_save($data,$nolongerused);
}
```

## Add global settings to the block plugin[​](#add-global-settings-to-the-block-plugin "Direct link to Add global settings to the block plugin")

Apart from the specific block instance configuration, the block plugin can use global settings to customize its behavior. Those settings can only be set in the site administration and are a great way to customize the behavior of all blocks on a site.

note

Global settings are not part of the block instance and should be accessed via the global get\_config method. For example:

```
$settingvalue=get_config('block_pluginname','settingname');
```

### create a settings.php file[​](#create-a-settingsphp-file "Direct link to create a settings.php file")

Implementing such configuration for our block is quite similar to implementing the [instance configuration](#add-instance-configuration-settings). To enable global configuration for the block, your plugin should contain **/blocks/simplehtml/settings.php** file. This file will populate the global admin form with form field definitions for each setting. See [Common files: settings.php](https://moodledev.io/docs/4.5/apis/commonfiles#settingsphp) for more information.

### Enabling Global Configuration[​](#enabling-global-configuration "Direct link to Enabling Global Configuration")

While in other Moodle pulgins the existence of a settings.php is enough to enable global configuration, for the blocks plugins it is mandatory to override the has\_config method in the base class.

View example

```
function has_config() {
    return true;
}
```

## Limit the block to specific contexts[​](#limit-the-block-to-specific-contexts "Direct link to Limit the block to specific contexts")

Some blocks are useful in some circumstances, but not in others. An example of this would be the "Social Activities" block, which is useful in courses with the "social" course format, but not courses with the "weeks" format. Moodle allows us to declare in which pages a block is available on. The information is given to Moodle as a standard associative array, with each key corresponding to a page format and defining a boolean value (true/false) that declares whether the block should be allowed to appear in that page format.

Each page in Moodle can define it's own page type name. However, there are some conventions:

- `all` value is used as a catch-all option. This means that if a block returns `['all' => true]` it can be used in any kind of page.
- `site-index` - Moodle frontpage.
- `course-view` - Course page, independent from the course format.
- `course-view-FORMATNAME` - Course page, with the "FORMATNAME" course format. For example, course-view-weeks is for courses with weeks format.
- `mod` - Any activity page, independent from the module.
- `mod-MODNAME-view` - Activity page, with the "MODNAME" activity. For example, mod-forum-view is for forums.
- `my` - The Moodle dashboard page.
- `admin` - Any administration page.

View example

```
publicfunctionapplicable_formats(){
return[
'admin'=>false,
'site-index'=>false,
'course-view'=>true,
'mod'=>true,
'my'=>false
];
}
```