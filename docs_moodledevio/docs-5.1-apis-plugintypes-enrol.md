---
title: Enrolment plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/plugintypes/enrol
source: sitemap
fetched_at: 2026-02-17T15:34:58.297327-03:00
rendered_js: false
word_count: 1683
summary: This document explains the architecture and development requirements for Moodle enrolment plugins, including database interactions, required file structures, and the implementation of base classes.
tags:
    - moodle
    - enrolment-plugins
    - php-development
    - plugin-architecture
    - plugin-development
category: guide
---

Moodle provides a number of ways of managing course enrolment, called enrolment plugins. Each course can decide its enabled enrolment plugins instances and any enrolment plugin can define a workflow the user must follow in order to enrol in the course.

Course enrolment information is stored in tables **enrol**, **user\_enrolments** and optionally other custom database tables defined by individual enrolment plugins. By default user enrolments are protected and can not be modified manually by teachers but only via the specific enrolment plugin.

Enrolment gives users following privileges:

- User with active enrolment may enter course, other users need either temporary guest access right or moodle/course:view capability.
- "My courses" shows list of active enrolments for current user.
- Course participation - some activities restrict participation to enrolled users only. The behaviour is defined independently by each activity, for example only enrolled users with submit capability may submit assignments, the capability alone is not enough.
- Only enrolled users may be members of groups.
- Gradebook tracks grades of all enrolled users, visibility of grades is controlled by role membership.

caution

Enrolments and role assignments are separate concepts, you may be enrolled and not have any role and you may have a role in course and not be enrolled. Roles at course context level and below may be controlled by enrolment plugins.

## File structure[​](#file-structure "Direct link to File structure")

All enrolment plugin files must be located inside the **enrol/pluginname** folder.

View an example directory layout for the `enrol_pluginname` plugin.

```
 enrol/pluginname/
 |-- db
 |   `-- access.php
 |-- lang
 |   `-- en
 |       `-- enrol_pluginname.php
 `-- lib.php
 `-- version.php
```

Some of the important files for the format plugintype are described below. See the [common plugin files](https://moodledev.io/docs/5.1/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

### lib.php[​](#libphp "Direct link to lib.php")

#### Global plugin functions

##### File path: /lib.php

The plugin lib.php must contain the plugin base class.

View example

public/enrol/pluginname/lib.php

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
 * Plugin functions for the enrol_pluginname plugin.
 *
 * @package   enrol_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

classenrol_pluginname_pluginextendsenrol_plugin{

// Enrolment plugins can define many workflows to handle enrolment
// depending on the overridden methods. See the methods section for more information.
}
```

Enrolment plugins must extend `enrol_plugin` base class which is defined at the end of lib/enrollib.php. This base class contains all standard methods to define the plugin workflow.

### lang/en/enrol\_pluginname.php[​](#langenenrol_pluginnamephp "Direct link to lang/en/enrol_pluginname.php")

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

public/enrol/pluginname/lang/en/plugintype\_pluginname.php

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
 * Languages configuration for the enrol_pluginname plugin.
 *
 * @package   enrol_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$string['fee:config']='Configure enrolment on payment enrol instances';
$string['fee:manage']='Manage enrolled users';
$string['fee:unenrol']='Unenrol users from course';
$string['fee:unenrolself']='Unenrol self from course';
$string['pluginname']='Enrolment on payment';
$string['pluginname_desc']='The enrolment on payment enrolment method allows you to set up courses requiring a payment. If the fee for any course is set to zero, then students are not asked to pay for entry. There is a site-wide fee that you set here as a default for the whole site and then a course setting that you can set for each course individually. The course fee overrides the site fee.';
$string['privacy:metadata']='The enrolment on payment enrolment plugin does not store any personal data.';
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

// Enrol anybody.
'enrol/pluginname:enrol'=>[
'captype'=>'write',
'contextlevel'=>CONTEXT_COURSE,
'archetypes'=>[
'manager'=>CAP_ALLOW,
'editingteacher'=>CAP_ALLOW,
],
],

// Manage enrolments of users.
'enrol/pluginname:manage'=>[
'captype'=>'write',
'contextlevel'=>CONTEXT_COURSE,
'archetypes'=>[
'manager'=>CAP_ALLOW,
'editingteacher'=>CAP_ALLOW,
],
],

// Unenrol anybody (including self) - watch out for data loss.
'enrol/pluginname:unenrol'=>[
'captype'=>'write',
'contextlevel'=>CONTEXT_COURSE,
'archetypes'=>[
'manager'=>CAP_ALLOW,
'editingteacher'=>CAP_ALLOW,
],
],

// Unenrol self - watch out for data loss.
'enrol/pluginname:unenrolself'=>[
'captype'=>'write',
'contextlevel'=>CONTEXT_COURSE,
'archetypes'=>[],
],
];
```

Depending on the enrolment workflow, the access.php file should define the following capabilities:

- **enrol/xxx:enrol** - used when `enrol_plugin::allow_enrol()` returns true.
- **enrol/xxx:unenrol** - used when `enrol_plugin::allow_unenrol()` or `enrol_plugin::allow_unenrol_user()` returns true.
- **enrol/xxx:manage** - used when `enrol_plugin::allow_manage()` returns true.
- **enrol/xxx:unenrolself** - used when plugin support self-unenrolment.
- **enrol/xxx:config** - used when plugin allows user to modify instance properties. Automatic synchronisation plugins do not usually need this capability.

See [enrolment API methods](#enrolment-api-methods) for more information.

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

public/enrol/pluginname/version.php

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
 * Version metadata for the enrol_pluginname plugin.
 *
 * @package   enrol_pluginname
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

## User enrolment process[​](#user-enrolment-process "Direct link to User enrolment process")

Manual enrolment plugins are the simplest way to handle user enrolments. In the core *enrol\_manual*, users with necessary permissions may enrol or unenrol users manually. In the *enrol\_flatfile* plugin allows automation of enrolment and unenrolment actions.

Fully automatic plugins are configured at the system level, they synchronise user enrolments with information stored in external systems (for example *enrol\_ldap*, *enrol\_database* and *enrol\_category*). Some non-interactive plugins may require configuration of enrolment instances (for example *enrol\_cohort*).

Interactive enrolment plugins require user interaction during enrolment (for example: *enrol\_self* and *enrol\_fee*). These plugins need to override `enrol_plugin::show_enrolme_link()`, `enrol_plugin::enrol_page_hook()` and to implement adding and editing of enrol instance.

## Enrolment expiration and suspending[​](#enrolment-expiration-and-suspending "Direct link to Enrolment expiration and suspending")

User has active enrolment if all following conditions are met:

- User has record in `user_enrolments` table,
- User enrolment already started,
- User enrolment is not past timeend,
- User enrolment has active status,
- Enrol instance has active status in `enrol` table,
- Enrol plugin is enabled.

Most synchronisation plugins include a setting called *External unenrol action*. It is used to decide what happens when previously enrolled user is not supposed to be enrolled any more. Enrol plugins can provide schedulled tasks to synchronize enrolments.

Plugins that set `timeend` in `user_enrolments` table may want to specify expiration action and optional expiration notification using `enrol_plugin::process_expirations()` and `enrol_plugin::send_expiry_notifications()` methods.

## Enrolment API methods.[​](#enrolment-api-methods "Direct link to Enrolment API methods.")

Each enrolment plugin can define the enrolment workflow by overriding some of the `enrol_plugin` methods.

### enrol\_plugin::get\_user\_enrolment\_actions(): array[​](#enrol_pluginget_user_enrolment_actions-array "Direct link to enrol_plugin::get_user_enrolment_actions(): array")

By default, all enrolment plugins will have *editing enrolment* and *user unenrolment* actions. However, some plugins may override this method to add extra actions.

View example

```
/**
 * Gets an array of the user enrolment actions
 *
 * @param course_enrolment_manager $manager
 * @param stdClass $userenrolment
 * @return array An array of user_enrolment_actions
 */
publicfunctionget_user_enrolment_actions(course_enrolment_manager$manager,$userenrolment){
$actions=parent::get_user_enrolment_actions($manager,$userenrolment);
$context=$manager->get_context();
$instance=$userenrolment->enrolmentinstance;
$params=$manager->get_moodlepage()->url->params();
$params['ue']=$userenrolment->id;

// Edit enrolment action.
if($this->allow_manage($instance)&&has_capability("enrol/{$instance->enrol}:something",$context)){
$title=get_string('newaction','enrol');
$icon=newpix_icon('t/edit','');
$url=newmoodle_url('/enrol/pluginname/something.php',$params);
$actions[]=newuser_enrolment_action($icon,$title,$url);
}

return$actions;
}
```

### enrol\_plugin::allow\_unenrol(): bool[​](#enrol_pluginallow_unenrol-bool "Direct link to enrol_plugin::allow_unenrol(): bool")

This method returns true if other code allowed to unenrol everybody from one instance. This method is used on course reset and manual unenrol.

note

The unenrol action will allow resetif all following conditions are met:

- The method `enrol_plugin::allow_unenrol()` returns true
- The current user has the `enrol/pluginname:unenrol` capability.

View example

```
publicfunctionallow_unenrol(stdClass$instance){
// Add any extra validation here.
returntrue;
}
```

### enrol\_plugin::allow\_unenrol\_user(): bool[​](#enrol_pluginallow_unenrol_user-bool "Direct link to enrol_plugin::allow_unenrol_user(): bool")

This method returns true if other code allowed to unenrol a specific user from one instance.

tip

If `allow_unenrol_user` is not overridden, the default behaviour is to call `allow_unenrol()` method.

note

The unenrol action will be displayed if all following conditions are met:

- The method `enrol_plugin::allow_unenrol_user()` returns true
- The current user has the `enrol/pluginname:unenrol` capability.

View example

```
publicfunctionallow_unenrol_user(stdClass$instance,stdClass$userenrolment){
// Add any extra validation here.
returntrue;
}

```

It is quite common in enrolment plugins to allow unenrol only if the user enrolment is suspended (for example: *enrol\_database*, *enrol\_flatfile*, *enrol\_meta*).

View suspended enrolment example

```
publicfunctionallow_unenrol_user(stdClass$instance,stdClass$userenrolment){
if($userenrolment->status==ENROL_USER_SUSPENDED){
returntrue;
}
returnfalse;
}
```

### enrol\_plugin::allow\_enrol(): bool[​](#enrol_pluginallow_enrol-bool "Direct link to enrol_plugin::allow_enrol(): bool")

Define if the enrol plugin is compatible with manual enrolments.

note

The edit manual enrolment action will be displayed if if all following conditions are met:

- The method `enrol_plugin::allow_enrol()` returns true
- The current user has the `enrol/pluginname:enrol` capability.

View example

```
publicfunctionallow_enrol(stdClass$instance){
// Add any extra validation here.
returntrue;
}
```

### enrol\_plugin::enrol\_user()[​](#enrol_pluginenrol_user "Direct link to enrol_plugin::enrol_user()")

This method is the plugin enrolment hook. It will be called when user is enrolled in the course using one of the plugin instances. It is used to alter the enrolment data (for example altering the dates or the role) and also to throw exceptions if some external condions are not met.

View example

```
/**
 * Enrol a user using a given enrolment instance.
 *
 * @param stdClass $instance the plugin instance
 * @param int $userid the user id
 * @param int $roleid the role id
 * @param int $timestart enrolment start timestamp
 * @param int $timeend enrolment end timestamp
 * @param int $status default to ENROL_USER_ACTIVE for new enrolments, no change by default in updates
 * @param bool $recovergrades restore grade history
 */
publicfunctionenrol_user(
stdClass$instance,
$userid,
$roleid=null,
$timestart=0,
$timeend=0,
$status=null,
$recovergrades=null
){
// Add validations here.

parent::enrol_user(
$instance,
$userid,
$roleid,
$timestart,
$timeend,
$status,
$recovergrades
);
}
```

### enrol\_plugin:allow\_manage(): bool[​](#enrol_plugin-bool "Direct link to enrol_plugin-bool")

Return true if plugin allows manual modification of user enrolments from other code. False is usually returned from plugins that synchronise data with external systems, otherwise the manual changes would be reverted immediately upon synchronisation.

note

The edit enrolment action in the participants list will be displayed if if all following conditions are met:

- The method `allow_manage` returns true
- The current user has the `enrol/pluginname:manage` capability.

View example

```
publicfunctionallow_manage(stdClass$instance){
// Add any extra validation here.
returntrue;
}
```

### enrol\_plugin::roles\_protected(): bool[​](#enrol_pluginroles_protected-bool "Direct link to enrol_plugin::roles_protected(): bool")

Enrolment plugins can protect roles from being modified by any other plugin. Returning false will allow users to remove all roles assigned by this plugin. By default, this method returns true.

:::

View example

```
publicfunctionroles_protected(){
// Add any extra validation here if necessary.
returnfalse;
}
```

### enrol\_plugin:find\_instance(): stdClass[​](#enrol_pluginfind_instance-stdclass "Direct link to enrol_pluginfind_instance-stdclass")

Returns enrolment instance in a given course matching provided data. If enrol plugin implements this method, then it is supported in CSV course upload.

note

So far following enrol plugins implement this method: *enrol\_manual*, *enrol\_self*, *enrol\_guest*, *enrol\_cohort*. Method must be capable to uniquely identify instance in a course using provided data in order to implement this method. For example, *enrol\_cohort* uses `cohortID` together with `roleID` to identify instance. For some methods (like *enrol\_lti* or *enrol\_payment*) it is not possible to uniquely identify instance in a course using provided data, so such methods will not be supported in CSV course upload.

The only exception is *enrol\_self* - although it is not possible to uniquely identify enrolment instance in a course using provided data, it is still supported in CSV course upload. For *enrol\_self* method `find_instance()` returns the first available enrolment instance in a course.

View example

```
publicfunctionfind_instance(array$enrolmentdata,int$courseid):?stdClass{
global$DB;
$instances=enrol_get_instances($courseid,false);

$instance=null;
if(isset($enrolmentdata['cohortidnumber'])&&isset($enrolmentdata['role'])){
$cohortid=$DB->get_field('cohort','id',['idnumber'=>$enrolmentdata['cohortidnumber']]);
$roleid=$DB->get_field('role','id',['shortname'=>$enrolmentdata['role']]);
if($cohortid&&$roleid){
foreach($instancesas$i){
if($i->enrol=='cohort'&&$i->customint1==$cohortid&&$i->roleid==$roleid){
$instance=$i;
break;
}
}
}
}
return$instance;
}
```

## Standard Editing UI[​](#standard-editing-ui "Direct link to Standard Editing UI")

Moodle participants page has a standard editing UI for manual enrolments. To integrate a plugin into the start UI you need to implement the following methods:

- `enrol_plugin::use_standard_editing_ui()`
- `enrol_plugin::edit_instance_form()`
- `enrol_plugin::edit_instance_validation()`
- `enrol_plugin::can_add_instance()`
- `enrol_plugin::add_instance()`

This means that the following functions from the plugin will be called to build the add/edit form, perform validation of the data and add standard navigation links to the manage enrolments page and course navigation.

View example

```
<?php
classenrol_guest_pluginextendsenrol_plugin{

/**
     * We are a good plugin and don't invent our own UI/validation code path.
     *
     * @return boolean
     */
publicfunctionuse_standard_editing_ui(){
returntrue;
}

/**
     * Returns true if the current user can add a new instance of enrolment plugin in course.
     * @param int $courseid
     * @return boolean
     */
publicfunctioncan_add_instance($courseid){
global$DB;

$context=context_course::instance($courseid,MUST_EXIST);

if(!has_capability('moodle/course:enrolconfig',$context)){
returnfalse;
}

if(!has_capability('enrol/pluginname:config',$context)){
returnfalse;
}

// In this example we only allow one instance per course.
if($DB->record_exists('enrol',['courseid'=>$courseid,'enrol'=>'pluginname'])){
returnfalse;
}

returntrue;
}

/**
     * Add elements to the edit instance form.
     *
     * @param stdClass $instance
     * @param MoodleQuickForm $mform
     * @param context $context
     * @return bool
     */
publicfunctionedit_instance_form($instance,MoodleQuickForm$mform,$context){
$options=[
'example1'=>get_string('example1','enrol_pluginname'),
'example2'=>get_string('example2','enrol_pluginname'),
];
$mform->addElement(
'select',
'customchar1',
get_string('something','enrol_pluginname'),
$options
);
$mform->setDefault('customchar1',$this->get_config('something'));

$mform->addElement(
'text',
'customtext1',
get_string('extraname','enrol_pluginname')
);
}

/**
     * Perform custom validation of the data used to edit the instance.
     *
     * @param array $data array of ("fieldname"=>value) of submitted data
     * @param array $files array of uploaded files "element_name"=>tmp_file_path
     * @param object $instance The instance loaded from the DB
     * @param context $context The context of the instance we are editing
     * @return array of "element_name"=>"error_description" if there are errors,
     *         or an empty array if everything is OK.
     */
publicfunctionedit_instance_validation($data,$files,$instance,$context){
$errors=[];

// Do some validation.
if($data['customchar1']!='example2'&&empty($data['customtext1'])){
$errors['customtext1']=get_string('missing_extraname','enrol_pluginname');
}

return$errors;
}

/**
     * Add new instance of enrol plugin.
     * @param object $course the course object
     * @param array $fields instance fields
     * @return int id of new instance, null if can not be created
     */
publicfunctionadd_instance($course,array$fields=null){
// Add $fields calculations here.
$instanceid=parent::add_instance($course,$fields);
// Insert elements to the enrolment plugins tables if needed.
return$instanceid;
}
}
```

## Sending a welcome email[​](#sending-a-welcome-email "Direct link to Sending a welcome email")

Some enrol methods has the support for sending welcome mesages to users. To grant the enrol messages are consistent acorrs enrolments methods, the enrol API provides the `enrol_send_welcome_email_options` function. This method returns a list of all possible options for sending welcome email when the user enrol in a course and each option has a respective constant defined on **enrollib.php**:

```
define('ENROL_DO_NOT_SEND_EMAIL',0);// Do not send the welcome email.
define('ENROL_SEND_EMAIL_FROM_COURSE_CONTACT',1);// Send welcome email from course contact.
define('ENROL_SEND_EMAIL_FROM_KEY_HOLDER',2);// Send welcome email from course key holder.
define('ENROL_SEND_EMAIL_FROM_NOREPLY',3);// Send welcome email from no reply.
```

View example

```
classenrol_pluginname_pluginextendsenrol_plugin{

// (...)

publicfunctionedit_instance_form($instance,MoodleQuickForm$mform,$context){
$mform->addElement(
'select',
'customint4',
get_string('sendcoursewelcomemessage','enrol_pluginname'),
enrol_send_welcome_email_options()
);
}

/**
     * Enrol a user using a given enrolment instance.
     *
     * @param stdClass $instance the plugin instance
     * @param int $userid the user id
     * @param int $roleid the role id
     * @param int $timestart enrolment start timestamp
     * @param int $timeend enrolment end timestamp
     * @param int $status default to ENROL_USER_ACTIVE for new enrolments
     * @param bool $recovergrades restore grade history
     */
publicfunctionenrol_user(
stdClass$instance,
$userid,
$roleid=null,
$timestart=0,
$timeend=0,
$status=null,
$recovergrades=null
){
parent::enrol_user(
$instance,
$userid,
$roleid,
$timestart,
$timeend,
$status,
$recovergrades
);
// Send welcome message.
if($instance->customint4!=ENROL_DO_NOT_SEND_EMAIL){
$this->email_welcome_message($instance,core_user::get_user($userid));
}
}
}
```

## See also[​](#see-also "Direct link to See also")

- [Enrolment API](https://moodledev.io/docs/5.1/apis/subsystems/enrol)