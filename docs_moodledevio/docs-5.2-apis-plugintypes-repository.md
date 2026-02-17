---
title: Repository plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/plugintypes/repository
source: sitemap
fetched_at: 2026-02-17T15:44:51.095091-03:00
rendered_js: false
word_count: 4033
summary: This document outlines the essential structure and required files for developing Moodle repository plugins to integrate external content services. It covers prerequisites, directory layout, and the implementation of mandatory files like version.php and lib.php.
tags:
    - moodle-development
    - repository-plugin
    - plugin-architecture
    - file-management
    - php-development
    - plugin-structure
category: guide
---

Repository plugin allow Moodle to bring contents into Moodle from external repositories.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before starting coding, it is necessary to know how to use repository administration pages and how to use the file picker.

The 2 different parts to write in order to implement a full repository:

1. Administration - You can customise the way administrators and users can configure their repositories.
2. File picker integration - The core of your plugin, it will manage communication between Moodle and the repository service, and also the file picker display.

## File structure[​](#file-structure "Direct link to File structure")

Repository plugins are located in the `/repository` directory.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

View an example directory layout for the `repository_pluginname` plugin.

```
 repository/pluginname/
 |-- db
 |   `-- access.php
 |-- lang
 |   `-- en
 |       `-- repository_pluginname.php
 |-- lib.php
 |-- pix
 |   `-- icon.png
 `-- version.php
```

Some of the important files for the repository plugintype are described below. See the [common plugin files](https://moodledev.io/docs/5.2/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

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

public/repository/pluginname/version.php

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
 * Version metadata for the repository_pluginname plugin.
 *
 * @package   repository_pluginname
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

### lang/en/repository\_pluginname.php[​](#langenrepository_pluginnamephp "Direct link to lang/en/repository_pluginname.php")

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

public/repository/pluginname/lang/en/plugintype\_pluginname.php

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
 * Languages configuration for the repository_pluginname plugin.
 *
 * @package   repository_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['pluginname']='Example repository';
$string['configplugin']='Configuration for Example repository';
$string['pluginname_help']='A repository description';
```

### lib.php[​](#libphp "Direct link to lib.php")

#### Global plugin functions

##### File path: /lib.php

This file contains the main repository class definition, which must extend the core `\repository` class. By extending the base class and overriding some of the class methods, the plugin can configure standard features and behaviours. See [Administration API](https://moodledev.io/docs/5.2/apis/subsystems/admin) for more information.

View example

public/repository/pluginname/lib.php

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
 * Plugin functions for the repository_pluginname plugin.
 *
 * @package   repository_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL')||die();

require_once($CFG->dirroot.'/repository/lib.php');

classrepository_pluginnameextendsrepository{
/**
     * Get file listing.
     *
     * This is a mandatory method for any repository.
     *
     * See repository::get_listing() for details.
     *
     * @param string $encodedpath
     * @param string $page
     * @return array the list of files, including meta information
     */
publicfunctionget_listing($encodedpath='',$page=''){
// This methods
returnarray('list'=>[]);
}

/**
     * Is this repository used to browse moodle files?
     *
     * @return boolean
     */
publicfunctionhas_moodle_files(){
returntrue;
}

/**
     * Tells how the file can be picked from this repository.
     *
     * @return int
     */
publicfunctionsupported_returntypes(){
returnFILE_INTERNAL|FILE_REFERENCE;
}

/**
     * Which return type should be selected by default.
     *
     * @return int
     */
publicfunctiondefault_returntype(){
returnFILE_INTERNAL;
}


/**
     * Optional method for searching files in the repository.
     *
     * @param string $search
     * @param int $page
     * @return array the list of found files.
     */
publicfunctionsearch($search,$page=0){
$ret=[];
$ret['nologin']=true;
// The found files list.
$ret['list']=[];
return$ret;
}
}
```

### db/access.php[​](#dbaccessphp "Direct link to db/access.php")

#### Plugin capabilities

##### File path: /db/access.php

The `db/access.php` file contains the **initial** configuration for a plugin's access control rules.

Access control is handled in Moodle by the use of Roles, and Capabilities. You can read more about these in the [Access API](https://moodledev.io/docs/5.2/apis/subsystems/access) documentation.

Changing initial configuration

If you make changes to the initial configuration of *existing* access control rules, these will only take effect for *new installations of your plugin*. Any existing installation **will not** be updated with the latest configuration.

Updating existing capability configuration for an installed site is not recommended as it may have already been modified by an administrator.

View example

public/repository/pluginname/db/access.php

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
 * Plugin capabilities for the repository_pluginname plugin.
 *
 * @package   repository_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$capabilities=[
// Ability to use the plugin.
'repository/pluginname:view'=>[
'captype'=>'read',
'contextlevel'=>CONTEXT_MODULE,
'archetypes'=>[
'coursecreator'=>CAP_ALLOW,
'editingteacher'=>CAP_ALLOW,
'manager'=>CAP_ALLOW
]
],
];
```

## Repository API methods[​](#repository-api-methods "Direct link to Repository API methods")

Repository plugins can present, store, and link files in different ways depending on the type of remote system that the repository connects to.

Some of the key API functions are described below.

### supported\_returntypes(): int[​](#supported_returntypes-int "Direct link to supported_returntypes(): int")

Return any combination of the following values:

- `FILE_INTERNAL` - the file is stored within the Moodle file system.
- `FILE_EXTERNAL` - the file is stored in the external repository. It is not stored within the Moodle file system. When accessing the file it is returned from the remote system.
- `FILE_REFERENCE` - the file stays in the external repository but may be cached locally. In that case it should be synchronised automatically, as required, with any changes to the external original.
- `FILE_CONTROLLED_LINK` - the file remains in the external repository, and ownership of the file in the remote system is changed to the [system account in the external repository](https://docs.moodle.org//en/OAuth_2_services). When the file is accessed, the system account is responsible for granting access to users.

<!--THE END-->

- Setting options example
- View code

> The return types that your plugin supports will be presented as options to the user when they are adding a file from the file picker. The `FILE_EXTERNAL` option is not reflected in this list as this is an internal feature of your API.
> 
> ![Supported returntypes options settings](data:image/png;base64,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)

The return values influence the choices offered to a user when selecting a file in file picker. Consider the screenshot above, which is from the dialogue that appears directly after choosing (but before uploading) a file in mod\_resource. The three options result from `FILE_INTERNAL`, `FILE_REFERENCE`, and `FILE_CONTROLLED_LINK` being present. `FILE_REFERENCE` corresponds to the "alias/shortcut" option.

The option `FILE_EXTERNAL` is never reflected in the file picker for mod\_resource, so its absence or presence in supported\_returntypes() is never reflected here. However, `FILE_EXTERNAL` is the only return type supported by mod\_url: For mod\_url, file picker will only(!) list repositories that support `FILE_EXTERNAL`.

This implies that a plugin that uses a file picker is able to narrow the set of supported return types. For example, assignsubmission\_file disallows `FILE_EXTERNAL` and `FILE_REFERENCE`.

In the end, which type is used by Moodle depends on the choices made by the end user (for example inserting a link, will result in `FILE_EXTERNAL`-related functions being used, using a 'shortcut/alias' will result in the '`FILE_REFERENCE`'-related functions being used).

### supported\_filetypes()[​](#supported_filetypes "Direct link to supported_filetypes()")

If your plugin only supports certian file types, then you should implement the optional `supported_filetypes()` method.

This method is used to hide repositories when they don't support certain file types - for example, if a user is inserting a video then any repository which does not support videos will not be shown.

Supported file types can be specified using standard mimetypes (such as `image/gif`) or file groups (such as `web_image`). For a full list of the supported mimetypes and groups, see the [`core_filetypes`](https://github.com/moodle/moodle/blob/v4.0.0/lib/classes/filetypes.php#L47) class.

- All files
- Filter mimetypes
- Filter file groups

```
functionsupported_filetypes(){
// Allow any kind of file.
return'*';
}
```

### Course and User Repository Instances.[​](#course-and-user-repository-instances "Direct link to Course and User Repository Instances.")

A system-wide instance of a repository is created when it is enabled. It is also possible to support both course, and user specific repositories.. This can be achieved by setting the `enablecourseinstances` and `enableuserinstances` options. There are three ways that this can be done:

1. Define **$string\['enablecourseinstances']** and **$string\['enableuserinstances']** in your plugin's language file. You can check an example in the [filesystem repository](https://github.com/moodle/moodle/blob/v4.0.0/repository/filesystem/lang/en/repository_filesystem.php).
2. The plugin must provide a **get\_instance\_option\_names** method which returns at least one instance option name. This method defined the specific instances options, if none instance attribute is needed, the system will not allow the plugin to define course and user instances. Note, you must not define the form fields for these options in the **type\_config\_form()** function. For example, [filesystem repository](https://github.com/moodle/moodle/blob/v4.0.0/repository/filesystem/lib.php#L439).
3. Several 'core' repositories use the **db/install.php** to create the original repository instance by constructing an instance of the **repository\_type** class. The options can be defined in the array passed as the second parameter to the constructor. For example [Wikipedia repository](https://github.com/moodle/moodle/blob/v4.0.0/repository/wikimedia/db/install.php).

### Developer-defined API[​](#developer-defined-api "Direct link to Developer-defined API")

These are settings that are configured for the whole Moodle site and not per instance of your plugin. All of these are optional, without them there will be no configuration options in the Site administration &gt; Plugins &gt; Repositories &gt; pluginname page.

#### get\_type\_option\_names(): array[​](#get_type_option_names-array "Direct link to get_type_option_names(): array")

This function must be declared static

Optional. Return an array of string. These strings are setting names. These settings are shared by all instances. Parent function returns an array with a single item - pluginname.

View example

```
publicstaticfunctionget_type_option_names(){
returnarray_merge(parent::get_type_option_names(),['rootpath']);
}
```

#### type\_config\_form($mform, $classname='repository')[​](#type_config_formmform-classnamerepository "Direct link to type_config_form($mform, $classname='repository')")

This function must be declared static

Optional. This is for modifying the Moodle form displaying the plugin settings. The [Form Definition](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition) documentation has details of all the types of elements you can add to the settings form.

View example

For example, to display the standard repository plugin settings along with the custom ones use:

```
publicstaticfunctiontype_config_form($mform,$classname='repository'){
parent::type_config_form($mform);

$rootpath=get_config('repository_pluginname','rootpath');
$mform->addElement('text','rootpath',get_string('rootpath','repository_pluginname'),array('size'=>'40'));
$mform->setDefault('rootpath',$rootpath);
}
```

#### type\_form\_validation($mform, $data, $errors)[​](#type_form_validationmform-data-errors "Direct link to type_form_validation($mform, $data, $errors)")

This function must be declared static

Optional. Use this function if you need to validate some variables submitted by plugin settings form. To use it, check through the associative array of data provided ('settingname' =&gt; value) for any errors. Then push the items to $error array in the format ("fieldname" =&gt; "human readable error message") to have them highlighted in the form.

```
publicstaticfunctiontype_form_validation($mform,$data,$errors){
if(!is_dir($data['rootpath'])){
$errors['rootpath']=get_string('invalidrootpath','repository_pluginname');
}
return$errors;
}
```

### Instance settings[​](#instance-settings "Direct link to Instance settings")

These functions relate to a specific instance of your plugin (for example the URL and login details to access a specific webdav repository). All of these are optional, without them, the instance settings form will only contain a single 'name' field.

#### get\_instance\_option\_names(): array[​](#get_instance_option_names-array "Direct link to get_instance_option_names(): array")

This function must be declared static

Optional. Return an array of strings. These strings are setting names. These settings are specific to an instance.

If the function returns an empty array, the API will consider that the plugin displays only one repository in the file picker.

Parent function returns an empty array. This is equivalent to **get\_type\_option\_names()**, but for a specific instance.

View example

```
publicstaticfunctionget_instance_option_names(){
return['fs_path'];// From repository_filesystem
}
```

#### instance\_config\_form($mform)[​](#instance_config_formmform "Direct link to instance_config_form($mform)")

This function must be declared static

Optional. This is for modifying the Moodle form displaying the settings specific to an instance. This is equivalent to **type\_config\_form($mform, $classname)** but for instances. The [Form Definition](https://docs.moodle.org/dev/lib/formslib.php_Form_Definition) documentation has details of all the types of elements you can add to the settings form.

View example

For example, to add a required text box called email\_address:

```
publicstaticfunctionget_instance_option_names(){
$mform->addElement(
'text',
'email_address',
get_string('emailaddress','repository_pluginname')
);
$mform->addRule('email_address',$strrequired,'required',null,'client');
}
```

note

**mform** has by default a name text box (cannot be removed).

#### instance\_form\_validation($mform, $data, $errors)[​](#instance_form_validationmform-data-errors "Direct link to instance_form_validation($mform, $data, $errors)")

This function must be declared static

Optional. This allows us to validate what has been submitted in the instance configuration form. This is equivalent to ''type\_form\_validation($mform, $data, $errors), but for instances. For example:

```
publicstaticfunctioninstance_form_validation($mform,$data,$errors){
if(empty($data['email_address'])){
$errors['email_address']=get_string('invalidemailsettingname','repository_flickr_public');
}
}
```

#### Getting / updating settings[​](#getting--updating-settings "Direct link to Getting / updating settings")

Both global and instance settings can be retrieved, from within the plugin, via **$this-&gt;get\_option('settingname')** and updated via **$this-&gt;set\_option(array('settingname' =&gt; 'value'))**.

note

You cannot call **$this** from static methods. If you need access the non static variables, you may have to store the values in the **\_construct()** method into private static variables.

#### plugin\_init()[​](#plugin_init "Direct link to plugin_init()")

This function must be declared static.

Optional. This function is called when the administrator adds the plugin. So unless the administrator deletes the plugin and re-adds it, it should be called only once.

Parent function does nothing.

### Example of using the settings[​](#example-of-using-the-settings "Direct link to Example of using the settings")

As an example, let's create a Flickr plugin for accessing a public flickr account. The plugin will be called "Flickr Public".

Firstly the skeleton:

repository/flickr\_public/lib.php

```
<?php
/**
 * repository_flickr_public class
 * Moodle user can access public flickr account
 *
 * @license http://www.gnu.org/copyleft/gpl.html GNU Public License
*/
classrepository_flickr_publicextendsrepository{
}
```

Then consider the question "What does my plugin do?"

In the Moodle file picker, we want to display some flickr public repositories directly linked to a flickr public account. For example **My Public Flickr Pictures**, and also ''My Friend's Flickr Pictures''. When the user clicks on one of these repositories, the public pictures are displayed in the file picker.

In order to access to a flickr public account, the plugin needs to know the email address of the Flickr public account owner. So the administrator will need to set an email address for every repository. Let's add an "email address" setting to every repository. To do so you need to override:

- **get\_instance\_option\_names** returing \['email\_address'].
- **instance\_config\_form** adding a text box called 'email\_address' into the form.

So at this moment all our Flickr Public Repositories will have a specific email address. However this is not enough. In order to communicate with Flickr, Moodle needs to know a Flickr API key [https://www.flickr.com/services/api/](https://www.flickr.com/services/api/). This API key is the same for any repository. We could add it with the email address setting but the administrator would have to enter the same API key for every repository. Hopefully the administrator can add settings to the plugin level, impacting all repositories. To do so you need to override:

- **get\_type\_option\_names** returing \['api\_key'].
- **type\_config\_form** adding the api\_key text input element into the form.

At this point we have created everything necessary for the administration pages. But let's go further. It would be good if the user can enter any "Flickr public account email address" in the file picker. In fact we want to display in the file picker a Flickr Public repository that the Moodle administrator can never delete. Let's add:

- **plugin\_init** using **repository::static\_function** to create a default repository instance.

That's all - the administration part of our Flickr Public plugin is done. For your information, Box.net, Flickr, and Flickr Public all have similar administration APIs.

##### File path: /lib.php

The `lib.php` file is a legacy file which acts as a bridge between Moodle core, and the plugin. In recent plugins it is should only used to define callbacks and related functionality which currently is not supported as an auto-loadable class.

All functions defined in this file **must** meet the requirements set out in the relevant section of the [Coding style](https://moodledev.io/general/development/policies/codingstyle#functions-and-methods).

Performance impact

Moodle core often loads all the `lib.php` files of a given plugin types. For performance reasons, it is strongly recommended to keep this file as small as possible and have just required code implemented in it. All the plugin's internal logic should be implemented in the auto-loaded classes.

View example

public/repository/pluginname/lib.php

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
 * Plugin functions for the repository_pluginname plugin.
 *
 * @package   repository_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL')||die();

require_once($CFG->dirroot.'/repository/lib.php');

classrepository_flickr_publicextendsrepository{

// User specific settings.

/**
     * Options names.
     *
     * Tell the API that the repositories have specific settings: "email address"
     *
     * @return string[] of options.
     */
publicstaticfunctionget_instance_option_names(){
return['email_address'];
}

/**
     * Repository configuration form.
     *
     * Add an "email address" text box to the create/edit repository instance Moodle form
     *
     * @param moodleform $mform Moodle form
     */
publicstaticfunctioninstance_config_form($mform){
$mform->addElement(
'text',
'email_address',
get_string('emailaddress','repository_flickr_public')
);
$mform->addRule(
'email_address',
get_string('required'),
'required',
null,
'client'
);
}

// Global repository plugin settings.

/**
     * Repository global settings names.
     *
     * We tell the API that the repositories have general settings: "api_key"
     *
     * @return string[] of options.
     */
publicstaticfunctionget_type_option_names(){
returnarray('api_key');
}

/**
     * Repository global settings form.
     *
     * We add an "api key" text box to the create/edit repository plugin Moodle form (also called a Repository type Moodle form)
     *
     * @param moodleform $mform Moodle form
     */
publicfunctiontype_config_form($mform){
//the following line is needed in order to retrieve the API key value from the database when Moodle displays the edit form
$api_key=get_config('flickrpublic','api_key');

$mform->addElement(
'text',
'api_key',
get_string('apikey','repository_flickr_public'),
['value'=>$api_key,'size'=>'40']
);
$mform->addRule(
'api_key',
get_string('required'),
'required',
null,
'client'
);
}

// Method called when the repostiroy plugin is installed.

/**
     * Plugin init method.
     *
     * this function is only called one time, when the Moodle administrator add the Flickr Public Plugin into the Moodle site.
     */
publicstaticfunctionplugin_init(){
//here we create a default repository instance. The last parameter is 1 in order to set the instance as readonly.
repository::static_function(
'flickrpublic',
'create',
'flickrpublic',
0,
context_system::instance(),
['name'=>'default instance','email_address'=>null],
1
);
}
}
```

## Repository APIs[​](#repository-apis "Direct link to Repository APIs")

### Quick Start[​](#quick-start "Direct link to Quick Start")

The File Picker uses Ajax calls to present the repository content. In order to integrate a repository with the the Ajax callbacks there are several possibilities:

- When a plugin requires a special user login (for example OAuth) the plugin must detect user session in the `constructor()` function, and use `print_login()` if required.
- For plugins that need to connect to a remote repository the connections can be done into the `get_listing()` or `constructor()` function.
- To retrieve the file that the user selected from a remote server, the plugin must rewrite the `get_file()` method.
- To provide search feature the plugin must rewrite the `search()` method.

All those methods are described below.

### Functions you MUST override[​](#functions-you-must-override "Direct link to Functions you MUST override")

These functions cover the basics of initialising your plugin each time the repository is accessed and listing the files available to the user from within the plugin.

#### \_\_construct($repositoryid, $context=SYSCONTEXTID, $options=array(), $readonly=0)[​](#__constructrepositoryid-contextsyscontextid-optionsarray-readonly0 "Direct link to __construct($repositoryid, $context=SYSCONTEXTID, $options=array(), $readonly=0)")

Should be overridden to do any initialisation required by the repository, including:

- logging in via optional\_param, if required - see 'print\_login', below
- getting any options from the database

The possible items in the $options array are:

- 'ajax' - bool, true if the user is using the AJAX filepicker
- mimetypes' - array of accepted mime types, or '\*' for all types

Calling parent::\_\_construct($repositoryid, $context, $options, $readonly); is essential and will set up various required member variables:

- this-&gt;id - the repository instance id (the ID of the entry in mdl\_repository\_instances)
- this-&gt;context - the context in which the repository instance can be found
- this-&gt;instance - the repository instance record (from mdl\_repository\_instances)
- this-&gt;readonly - whether or not the settings can be changed
- this-&gt;options - the above options, combined with the settings saved in the database
- this-&gt;name - as specified by $this-&gt;get\_name()
- this-&gt;returntypes - as specified by $this-&gt;supported\_returntypes()

#### get\_listing($path="", $page="")[​](#get_listingpath-page 'Direct link to get_listing($path="", $page="")')

This function will return a list of files to be displayed to the user, the list must be a array.

View example

```
/**
 * Get file listing.
 *
 * This is a mandatory method for any repository.
 *
 * See repository::get_listing() for details.
 *
 * @param string $encodedpath
 * @param string $page
 * @return array the list of files, including meta information
 */
publicfunctionget_listing($encodedpath='',$page=''){
// This methods
return[
//this will be used to build navigation bar.
'path'=>[
[
'name'=>'root'
'path'=>'/'
],
[
'name'=>'subfolder',
'path'=>'/subfolder'
],
],
'manage'=>'http://webmgr.moodle.com',
'list'=>[
[
'title'=>'filename1',
'date'=>'1340002147',
'size'=>'10451213',
'source'=>'http://www.moodle.com/dl.rar',
],
[
'title'=>'folder',
'date'=>'1340002147',
'size'=>'0',
'children'=>[],
],
],
];
}
```

Amongst other details, this returns a **title** for each file (to be displayed in the filepicker) and the **source** for the file (which will be included in the request to 'download' the file into Moodle or to generate a link to the file). Directories return a **children** value, which is either an empty array (if 'dynload' is specified) or an array of the files and directories contained within it.

The full specification of list element

```
// Example of a list array with all the element types.
{
// 'path' is used to build navigation bar to show the current folder, so you need to include all parents folders
// array(array('name'=>'root','path'=>'/'), array('name'=>'subfolder', 'path'=>'/subfolder'))
// This will result in: /root/subfolder as current directory
"path": (array),// this will be used to build navigation bar,

// 'dynload' tells file picker to fetch list dynamically.
// When user clicks the folder, it will send a ajax request to server side.
// Default value is false but note that non-Javascript file picker always acts as if dynload was set to true
"dynload": (bool),// use dynamic loading,

// If you are using pagination, 'page' and 'pages' parameters should be set.
// It is not recommended to use pagination and subfolders at the same time, the tree view mode can not handle it correctly
"page": (int),// which page is this list,
"pages": (int),// how many pages. If number of pages is unknown but we know that the next page exists repository may return -1,
"manage": (string),// url to file manager for the external repository, if specified will display link in file picker,
"help": (string),// url to the help window, if specified will display link in file picker,
"nologin": (bool),// requires login, default false, if set to true the login link will be removed from file picker,
"norefresh": (bool),// no refresh button, default false,
"logouttext": (string),// in case of nologin=false can substitute the text 'Logout' for logout link in file picker,
"nosearch": (bool),// no search link, default false, if set to true the search link will be removed from file picker,
"issearchresult": (bool),// tells that this listing is the result of search,
// for repositories that actually upload a file: set 'upload' option to display an upload form in file picker
"upload":{// upload manager
"label": (string),// label of the form element,
"id": (string) // id of the form element,
},
// 'list' is used by file picker to build a file/folder tree
"list":{
{// file
"title": (string),// file name,
"shorttitle": (string),// optional, if you prefer to display a short title
"date": (int),// UNIX timestamp, default value for datemodified and datecreated,
"datemodified": (int),// UNIX timestamp when the file was last modified [      'datecreated' => (int) UNIX timestamp when the file was last created [2.3+](2.3+],
"size": (int),// file size in bytes,
"thumbnail": (string),// url to thumbnail for the file,
"thumbnail_width": (int),// the width of the thumbnail image,
"thumbnail_height": (int),// the height of the thumbnail image,
"source": (string),// plugin-dependent unique path to the file (id, url, path, etc.),
"url": (moodle_url),// the accessible url of file,
"icon": (string),// url to icon of the image (24x24px), if omitted the moodle filetype icon will be used [      'realthumbnail' => (string) url to image preview to be lazy-loaded when scrolled to it (if it requires to be generated and can not be returned as 'thumbnail') [2.3+](2.3+],
"realicon": (string),// url to image preview in icon size (24x24) [      'author' => (string) default value for file author,
"license": (string),// default value for license (short name, see class license_manager),
"image_height": (int),// if the file is an image, image height in pixels, null otherwise [2.3+](2.3+],
"image_width":  (int) // if the file is an image, image width in pixels, null otherwise [    ),
},
{// folder - similar to file, has also 'path' and 'children' but no 'source' or 'url'
"title": (string),// folder name,
"shorttitle": (string),// optional, if you prefer to display a short title
"path": (string),// path to this folder. In case of dynload=true (and for non-JS filepicker) the value will be passed to repository_xxx::get_listing() in order to retrieve children
"date": (int),
"datemodified": (int),
"datecreated": (int),
"thumbnail": (string),
"icon":,// see above,
"children":[
// presence of this attribute actually tells file picker that this is a folder. In case of dynload=true, it should be empty array
// otherwise it is a nested list of contained files and folders
]
}
},
// The 'object' tag can be used to embed an external web page or application within the filepicker
"object":{
"type": (string),// e.g. 'text/html', 'application/x-shockwave-flash'
"src": (string),// the website address to embed in the object
}
}
```

### Dynamically loading[​](#dynamically-loading "Direct link to Dynamically loading")

Some repositories contain many files which cannot load in one time, in this case, we need dynamically loading to fetch them step by step, files in subfolder won't be listed until user click the folder in file picker treeview.

As a plug-in developer, if you set dynload flag as **true**, you should return files and folders (set children as a null array) in current path only instead of building the whole file tree.

The use of the **object** tag, instead of returning a **list** of files, allows you to embed an external file chooser within the repository panel. See [Repository plugins embedding external file chooser](https://docs.moodle.org/dev/Repository_plugins_embedding_external_file_chooser) for details about how to do this.

### User login (optional)[​](#user-login-optional "Direct link to User login (optional)")

If our plugin allows a user to log in to a remote service, you can support this using the `print_login()` and `check_login` function, which are desribed below.

#### print\_login[​](#print_login "Direct link to print_login")

For plugins which need to support login to a remote service, the `print_login()` function can be used to return an array of the form elements needed to support the login.

View example

note

It is important to note that the repository login can be called on both Ajax and non ajax requests. For this reason the `print_login()` should check for `$this->options['ajax']` to know if it should return an array or the full login HTML form.

```
publicfunctionprint_login(){// From repository_pluginname
global$OUTPUT;

if($this->options['ajax']){
$user_field=(object)[
'label'=>get_string('username','repository_pluginname'),
'id'=>'pluginname_username',
'type'=>'text',
'name'=>'al_username',
];

$passwd_field=(object)[
'label'=>get_string('password','repository_pluginname'),
'id'=>'pluginname_password',
'type'=>'password',
'name'=>'al_password',
];

$ret=[];
$ret['login']=[$user_field,$passwd_field];
return$ret;
}else{// Non-AJAX login form - directly output the form elements.
// Print the login form HTML including the input username and password fields.
$loginform=newrepository_pluginname\output\login();
echo$OUTPUT->render($loginform);
// Example of a login form:
// <label> Username </label>
// <input type="text" name="al_username" />
// <label> Password </label>
// <input type="password" name="al_password" />
// <input type="submit" value="Enter" />
}
}
```

This will help to generate a form by file picker which contains user name and password input elements.

If your login form is static and never changes, you can add `$ret['allowcaching']) = true;` and filepicker will not send the request to the server every time user opens the login/search form.

For plugins that do not fully process the login via a popup window, the submitted details can be retrieved, from within the `__construct` function, via `$submitted = optional_param('fieldname', [PARAM_INT/PARAM_TEXT)`.

View example

lib/alfresco/lib.php

```
publicfunction__construct($repositoryid,$context=SYSCONTEXTID,$options=[]){
global$SESSION;

/* Skipping code that is not relevant to user login */

$this->alfresco=newAlfresco_Repository($this->options['alfresco_url']);
$this->username=optional_param('al_username','',PARAM_RAW);
$this->password=optional_param('al_password','',PARAM_RAW);
try{
// deal with user logging in.
if(empty($SESSION->{$this->sessname})&&!empty($this->username)&&!empty($this->password)){
$this->ticket=$this->alfresco->authenticate($this->username,$this->password);
$SESSION->{$this->sessname}=$this->ticket;
}else{
if(!empty($SESSION->{$this->sessname})){
$this->ticket=$SESSION->{$this->sessname};
}
}
$this->user_session=$this->alfresco->createSession($this->ticket);
$this->store=newSpacesStore($this->user_session);
}catch(Exception$e){
$this->logout();
}
$this->current_node=null;

/* Skipping code that is not relevant to user login */

}
```

Many types include a single element of type 'popup' with the param 'url' pointing at the URL used to authenticate the repo instance.

View example

Code taken from repository\_boxnet

```
publicfunctionprint_login(){
$ticket=$this->boxclient->getTicket();
if($this->options['ajax']){
$loginbtn=(object)[
'type'=>'popup',
'url'=>' https://www.box.com/api/1.0/auth/'.$ticket->get_oauth_tokens(),
];
$result=[];
$result['login']=[$loginbtn];
return$result;
}else{
// Print the login form HTML including the input username, password and ticket fields.
$loginform=newrepository_boxnet\output\login($ticket);
echo$OUTPUT->render($loginform);
// Example of a login form:
// <label> Username </label>
// <input type="text" name="boxusername" />
// <label> Password </label>
// <input type="password" name="boxpassword" />
// <input type="hidden" name="ticket" value="{$ticket->get_oauth_tokens()}" />
// <input type="submit" value="Enter" />
}
}
```

#### check\_login(): bool[​](#check_login-bool "Direct link to check_login(): bool")

This function will return a boolean value to tell Moodle whether the user has logged in. By default, this function will return true.

```
publicfunctioncheck_login():bool{
global$SESSION;
return!empty($SESSION->{$this->sessname});
}
```

#### logout[​](#logout "Direct link to logout")

When a user clicks the logout button in file picker, this function will be called. You may clean up the session or disconnect the connection with remote server here. After this the code should return something suitable to display to the user (usually the results of calling **$this-&gt;print\_login()**):

lib/alfresco/lib.php

```
publicfunctionlogout(){
global$SESSION;
unset($SESSION->{$this->sessname});
return$this->print_login();
}
```

### Transferring files to Moodle (optional)[​](#transferring-files-to-moodle-optional "Direct link to Transferring files to Moodle (optional)")

These functions all relate to transferring the files into Moodle, once they have been chosen in the filepicker. All of them are optional and have default implementations which are often suitable to use as they are.

#### get\_file\_reference($source)[​](#get_file_referencesource "Direct link to get_file_reference($source)")

This function takes $source as in user input, parses and cleans it (recommended to call clean\_param()). It prepares the reference to the file in repository-specific format that would be passed on to methods get\_file(), get\_link(), get\_moodle\_file(), get\_file\_by\_reference() and/or stored in DB in case of creating a shortcut to file. For the most of repositories it is just clean $source value. For has\_moodle\_files-repositories this function also changes encoding.

#### get\_file($url, $filename = "")[​](#get_fileurl-filename-- 'Direct link to get_file($url, $filename = "")')

For FILE\_INTERNAL or FILE\_REFERENCE this function is called at the point when the user has clicked on the file and then on 'select this file' to add it to the filemanager / editor element. It does the actual transfer of the file from the repository and onto the Moodle server. The default implementation is to download the $url via CURL. The $url parameter is the $reference returned by get\_file\_reference (above, but usually the same as the 'source' returned by 'get\_listing'). The $filename should usually be processed by $path = $this-&gt;prepare\_file($filename), giving the full 'path' where the file should be saved locally. This function then returns an array, containing:

- path - the local path where the file was saved
- url - the $url param passed into the function

<!--THE END-->

- Basic example
- repository\_aquella example

```
publicfunctionget_file($url,$filename=''){
// Default implementation from the base 'repository' class
$path=$this->prepare_file($filename);// Generate a unique temporary filename
$curlobject=newcurl();
$result=$curlobject->download_one($url,null,['filepath'=>$path,'timeout'=>self::GETFILE_TIMEOUT]);
if($result!==true){
thrownewmoodle_exception('errorwhiledownload','repository','',$result);
}
return['path'=>$path,'url'=>$url];
}
```

#### get\_link($url)[​](#get_linkurl "Direct link to get_link($url)")

Used with `FILE_EXTERNAL` to convert a reference (from 'get\_file\_reference', but ultimately from the output of 'get\_listing') into a URL that can be used directly by the end-user's browser. Usually just returns the original $url, but may need further transformation based on the internal implementation of the repository plugin.

#### get\_file\_source\_info($source)[​](#get_file_source_infosource "Direct link to get_file_source_info($source)")

Takes the 'source' field from 'get\_listing' (as returned by the user's browser) and returns the value to be stored in files.source field in DB (regardless whether file is picked as a copy or by reference). It indicates where the file came from. It is advised to include either full URL here or indication of the repository. Examples: 'Dropbox: /filename.jpg', '[http://fullurl.com/path/file](http://fullurl.com/path/file)', etc.

This value will be used to display warning message if reference can not be restored from backup. Also it can (although not has to) be used in get\_reference\_details() to produce the human-readable reference source in the fileinfo dialogue in the file manager.

### Search functions (optional)[​](#search-functions-optional "Direct link to Search functions (optional)")

These functions allow you to implement search functionality within your repository.

#### print\_search[​](#print_search "Direct link to print_search")

When a user clicks the search button on file picker, this function will be called to return a search form. By default, it will create a form with single search bar - you can override it to create a advanced search form.

A custom search form must include the following:

- A text field element named **s**, this is where users will type in their search criteria
- A hidden element named **repo\_id** and the value must be the id of the repository instance
- A hidden element named **ctx\_id** and the value must be the context id of the repository instance
- A hidden element named **sesskey** and the value must be the session key

View example

The default implementation in class 'repository'

```
publicfunctionprint_search(){
global$PAGE;
$renderer=$PAGE->get_renderer('core','files');
return$renderer->repository_default_searchform();
// The default search HTML from repository/renderer.php:
// <div class="fp-def-search"><input name="s" value='.get_string('search', 'repository').' /></div>;
}
```

#### search($search\_text, $page = 0)[​](#searchsearch_text-page--0 "Direct link to search($search_text, $page = 0)")

Return the results of doing the search. Any additional parameters from the search form can be retrieved by $param = optional\_param('paramname', [PARAM\_INT / PARAM\_TEXT);.

The return should return an array containing:

- list - with the same layout as the 'list' element in 'get\_listing'

View example

Example from repoistory\_googledocs

```
publicfunctionsearch($search_text,$page=0){
$gdocs=newgoogle_docs($this->googleoauth);
return[
'dynload'=>true,
'list'=>$gdocs->get_file_list($search_text),
];
}
```

#### global\_search()[​](#global_search "Direct link to global_search()")

Return true if should be included in a search throughout all repositories (currently not available via the UI)

### Repository support for returning file as alias/shortcut[​](#repository-support-for-returning-file-as-aliasshortcut "Direct link to Repository support for returning file as alias/shortcut")

It is possible to link to the file from external (or internal) repository by reference. In UI it is called "create alias/shortcut". This creates a row in `files` table but the contents of the file is not stored. Although it may be cached by repository if developer wants to.

Make sure that function supported\_returntypes() returns FILE\_REFERENCE among other types.

Note that external file is synchronised by moodle when UI wants to show the file size.

#### get\_reference\_file\_lifetime()[​](#get_reference_file_lifetime "Direct link to get_reference_file_lifetime()")

Return minimum number of seconds before checking for changes to the file (default implementation = 1 day)

```
publicfunctionget_reference_file_lifetime($ref){
returnDAYSECS;// One day, 60 * 60 * 24 seconds.
}
```

#### sync\_individual\_file(stored\_file $storedfile)[​](#sync_individual_filestored_file-storedfile "Direct link to sync_individual_file(stored_file $storedfile)")

Called after the file has reached the 'lifetime' specified above to see if it should now be synchronised (default implementation is to return true)

```
publicfunctionsync_individual_file(stored_file$storedfile){
returntrue;
}
```

#### get\_reference\_details($reference, $filestatus = 0)[​](#get_reference_detailsreference-filestatus--0 "Direct link to get_reference_details($reference, $filestatus = 0)")

Returns human-readable information about where the original file is stored (to be displayed in the filepicker properties box).

This is usually prefixed with the repository name, and a semicolon. For example: `Myrepository: http://url.to.file`.

- `$reference` is the 'source' output by `get_listing`
- `$filestatus` can be either `0` (OK - default) or `666` (source file missing).

View example

lib.php

```
publicfunctionget_reference_details($reference,$filestatus=0){
if(!$filestatus){
// Replace the line below by any method your plugin have to check a reference.
$details=example_external_server::get_details_by_reference($reference);
return$this->get_name().': '.$details->filename;
}else{
returnget_string('lostsource','repository','');
}
}
```

#### get\_file\_by\_reference($reference)[​](#get_file_by_referencereference "Direct link to get_file_by_reference($reference)")

Returns up-to-date information about the original file, only called when the 'lifetime' is reached and 'sync\_individual\_file' returns true.

- For image files - download the file and return either $ret-&gt;filepath (full path on the server), $ret-&gt;handle (open handle to the file) or $ret-&gt;content (raw data from the file) to allow the file to be saved into the Moodle filesystem and the thumbnail to be updated
- For non-image files - avoid downloading the file (if possible) and just return $ret-&gt;filesize to update that information
- For missing / inaccessible files - return null Remember this function may be called quite a lot, as the filemanager often wants to know the filesize.

View example

/lib.php

```
publicfunctionget_file_by_reference($reference){
global$USER;
// Replace the line below by any method your plugin have to check a reference.
$details=example_external_server::get_details_by_reference($reference->reference));
if(!isset($details->url)||!($url=$this->appendtoken($details->url))){
// Occurs when the user isn't known.
returnnull;
}

// Download the file details.
$return=null;
$cookiepathname=$this->prepare_file($USER->id.'_'.uniqid('',true).'.cookie');
$headparams=['followlocation'=>true,'timeout'=>self::SYNCFILE_TIMEOUT];
$curlobject=newcurl(['cookie'=>$cookiepathname]);

if(file_extension_in_typegroup($ref->filename,'web_image')){
// The file is an image - download and return the file path.
$path=$this->prepare_file('');
$result=$curlobject->download_one($url,null,$headparams);
if($result===true){
$return=(object)['filepath'=>$path];
}
}else{
// The file is not an image - just get the file details.

$result=$curlobject->head($url,$headparams);
}

// Delete cookie jar.
if(file_exists($cookiepathname)){
unlink($cookiepathname);
}

$this->connection_result($ccurlobject->get_errno());
$curlinfo=$ccurlobject->get_info();
if($return===null&&isset($curlinfo['http_code']('list']))&&
$curlinfo['http_code']==200&&
array_key_exists('download_content_length',$curlinfo)&&
$curlinfo['download_content_length']('http_code'])>=0){
// We received a correct header and at least can tell the file size.
$return=(object)['filesize'=>$curlinfo['download_content_length']];
}
return$return;
}
```

#### send\_file($storedfile, $lifetime=86400, $filter=0, $forcedownload=false, array $options = null)[​](#send_filestoredfile-lifetime86400-filter0-forcedownloadfalse-array-options--null "Direct link to send_file($storedfile, $lifetime=86400, $filter=0, $forcedownload=false, array $options = null)")

Send the requested file back to the user's browser. The 'reference' for the file can be found via $storedfile-&gt;get\_reference(). If the file is not found / no longer exists, the function 'send\_file\_not\_found()' should be used. Otherwise the file should be output directly, via the most appropriate method:

- Use a 'Location: ' header to redirect to the external URL
- Download the file and cache within the Moodle filesystem (possibly using '$this-&gt;import\_external\_file\_contents()'), then call 'send\_stored\_file'.

note

It is up to the repository developer to decide whether to actually download the file or to return a locally cached copy instead.

View example

/lib.php

```
publicfunctionsend_file($stored_file,$lifetime=86400,$filter=0,$forcedownload=false,array$options=null){
// Replace the line below by any method your plugin have to check a reference.
$details=example_external_server::get_details_by_reference($stored_file->get_reference()));
$url=$this->appendtoken($details->url);
if($url){
header('Location: '.$url);
}else{
send_file_not_found();
}
}
```

An example of caching files within the Moodle filesystem can be found in repository\_dropbox.