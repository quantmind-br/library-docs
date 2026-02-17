---
title: Assign feedback plugins | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/apis/plugintypes/assign/feedback
source: sitemap
fetched_at: 2026-02-17T15:02:47.89873-03:00
rendered_js: false
word_count: 1390
summary: This document provides a technical guide on creating Moodle assignment feedback plugins, detailing the mandatory file structure, naming conventions, and core class methods required for implementation.
tags:
    - moodle-development
    - assignment-feedback
    - plugin-architecture
    - php-development
    - moodle-api
    - grading-interface
category: guide
---

An assignment feedback plugin can do many things including providing feedback to students about a submission. The grading interface for the assignment module provides many hooks that allow plugins to add their own entries and participate in the grading workflow.

tip

For a good reference implementation, see the [file](https://github.com/moodle/moodle/tree/main/mod/assign/feedback/file) feedback plugin included with core because it uses most of the features of feedback plugins.

## File structure[​](#file-structure "Direct link to File structure")

Assignment Feedback plugins are located in the `/mod/assign/feedback` directory. A plugin should not include any custom files outside of it's own plugin folder.

Plugin naming

The plugin name should be no longer than 38 (13 before Moodle 4.3) characters - this is because the database tables for a submission plugin must be prefixed with `assignfeedback_[pluginname]` (15 chars + X) and the table names can be no longer than 53 (28 before Moodle 4.3) chars due to a limitation with PostgreSQL.

If a plugin requires multiple database tables, the plugin name will need to be shorter to allow different table names to fit under the 53 character limit (28 before Moodle 4.3).

Note: If your plugin is intended to work with versions of Moodle older than 4.3, then the plugin name must be 13 characters or shorter, and table names must be 28 characters or shorter.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

important

Some of the important files are described below. See the [common plugin files](https://moodledev.io/docs/4.4/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

View an example directory layout for the `assignfeedback_file` plugin.

```
mod/assign/feedback/file
├── backup
│   └── moodle2
│       ├── backup_assignfeedback_file_subplugin.class.php
│       └── restore_assignfeedback_file_subplugin.class.php
├── classes
│   └── privacy
│       └── provider.php
├── db
│   ├── access.php
│   ├── install.php
│   ├── install.xml
│   └── upgrade.php
├── importzipform.php
├── importziplib.php
├── lang
│   └── en
│       └── assignfeedback_file.php
├── lib.php
├── locallib.php
├── settings.php
├── uploadzipform.php
└── version.php
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

Full details on how to create settings are available in the [Admin settings](https://moodledev.io/docs/4.4/apis/subsystems/admin) documentation.

All feedback plugins should include one setting named 'default' to indicate if the plugin should be enabled by default when creating a new assignment.

View example

\[path/to/assignfeedback]/file/settings.php

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
 * Plugin settings for the assignfeedback_file plugin.
 *
 * @package   assignfeedback_file
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$settings->add(
newadmin_setting_configcheckbox(
'assignfeedback_file/default',
newlang_string('default','assignfeedback_file'),
newlang_string('default_help','assignfeedback_file'),
0
)
);
```

### locallib.php[​](#locallibphp "Direct link to locallib.php")

#### Global support functions

##### File path: /locallib.php

This is where all the functionality for this plugin is defined. We will step through this file and describe each part as we go.

```
classassign_feedback_fileextendsassign_feedback_plugin{
```

#### get\_name()[​](#get_name "Direct link to get_name()")

All feedback plugins MUST define a class with the component name of the plugin that extends assign\_feedback\_plugin.

```
publicfunctionget_name(){
returnget_string('file','assignfeedback_file');
}
```

This function is abstract in the parent class (feedback\_plugin) and must be defined in your new plugin. Use the language strings to make your plugin translatable.

#### get\_settings()[​](#get_settings "Direct link to get_settings()")

```
publicfunctionget_settings(MoodleQuickForm$mform){
$mform->addElement(
'assignfeedback_file_fileextensions',
get_string('allowedfileextensions','assignfeedback_file')
);
$mform->setType('assignfeedback_file_fileextensions',PARAM_FILE);
}
```

This function is called when building the settings page for the assignment. It allows this plugin to add a list of settings to the form. Notice that the settings should be prefixed by the plugin name which is good practice to avoid conflicts with other plugins. (None of the core feedback plugins have any instance settings, so this example is fictional).

#### save\_settings()[​](#save_settings "Direct link to save_settings()")

```
publicfunctionsave_settings(stdClass$data){
$this->set_config('allowedfileextensions',$data->allowedfileextensions);
returntrue;
}
```

This function is called when the assignment settings page is submitted, either for a new assignment or when editing an existing one. For settings specific to a single instance of the assignment you can use the assign\_plugin::set\_config function shown here to save key/value pairs against this assignment instance for this plugin.

#### get\_form\_elements\_for\_user()[​](#get_form_elements_for_user "Direct link to get_form_elements_for_user()")

```
publicfunctionget_form_elements_for_user(
$grade,
MoodleQuickForm$mform,
stdClass$data,
$userid
){
$fileoptions=$this->get_file_options();
$gradeid=$grade?$grade->id:0;
$elementname="files_{$userid}";

$data=file_prepare_standard_filemanager(
$data,
$elementname,
$fileoptions,
$this->assignment->get_context(),
'assignfeedback_file',
ASSIGNFEEDBACK_FILE_FILEAREA,
$gradeid
);
$mform->addElement(
'filemanager',
"{$elementname}_filemanager",
html_writer::tag(
'span',
$this->get_name(),
['class'=>'accesshide']
),
null,
$fileoptions
);

returntrue;
}
```

This function is called when building the feedback form. It functions identically to the get\_settings function except that the grade object is available (if there is a grade) to associate the settings with a single grade attempt. This example also shows how to use a filemanager within a feedback plugin. The function must return true if it has modified the form otherwise the assignment will not include a header for this plugin. Notice there is an older version of this function "get\_form\_elements" which does not accept a userid as a parameter - this version is less useful - not recommended.

#### is\_feedback\_modified()[​](#is_feedback_modified "Direct link to is_feedback_modified()")

```
publicfunctionis_feedback_modified(stdClass$grade,stdClass$data){
$commenttext='';
if($grade){
$feedbackcomments=$this->get_feedback_comments($grade->id);
if($feedbackcomments){
$commenttext=$feedbackcomments->commenttext;
}
}

if($commenttext==$data->assignfeedbackcomments_editor[]('text')){
returnfalse;
}else{
returntrue;
}
}
```

This function is called before feedback is saved. If feedback has not been modified then the save() method is not called. This function takes the grade object and submitted data from the grading form. In this example we are comparing the existing text comments made with the new ones. This function must return a boolean; True if the feedback has been modified; False if there has been no modification made. If this method is not overwritten then it will default to returning True.

#### save()[​](#save "Direct link to save()")

```
publicfunctionsave(stdClass$grade,stdClass$data){
global$DB;

$fileoptions=$this->get_file_options();

$userid=$grade->userid;
$elementname='files_'.$userid;

$data=file_postupdate_standard_filemanager(
$data,
$elementname,
$fileoptions,
$this->assignment->get_context(),
'assignfeedback_file',
ASSIGNFEEDBACK_FILE_FILEAREA,
$grade->id
);

$filefeedback=$this->get_file_feedback($grade->id);
if($filefeedback){
$filefeedback->numfiles=$this->count_files($grade->id,ASSIGNFEEDBACK_FILE_FILEAREA);
return$DB->update_record('assignfeedback_file',$filefeedback);
}else{
$filefeedback=newstdClass();
$filefeedback->numfiles=$this->count_files($grade->id,ASSIGNFEEDBACK_FILE_FILEAREA);
$filefeedback->grade=$grade->id;
$filefeedback->assignment=$this->assignment->get_instance()->id;
return$DB->insert_record('assignfeedback_file',$filefeedback)>0;
}
}
```

This function is called to save a graders feedback. The parameters are the grade object and the data from the feedback form. This example calls `file_postupdate_standard_filemanager` to copy the files from the draft file area to the filearea for this feedback. It then records the number of files in the plugin specific `assignfeedback_file` table.

#### view\_summary()[​](#view_summary "Direct link to view_summary()")

```
publicfunctionview_summary(stdClass$grade,&$showviewlink){
$count=$this->count_files($grade->id,ASSIGNFEEDBACK_FILE_FILEAREA);
// show a view all link if the number of files is over this limit
$showviewlink=$count>ASSIGNFEEDBACK_FILE_MAXSUMMARYFILES;

if($count<=ASSIGNFEEDBACK_FILE_MAXSUMMARYFILES){
return$this->assignment->render_area_files(
'assignfeedback_file',
ASSIGNFEEDBACK_FILE_FILEAREA,
$grade->id
);
}else{
returnget_string('countfiles','assignfeedback_file',$count);
}
}
```

This function is called to display a summary of the feedback to both markers and students. It counts the number of files and if it is more that a set number, it only displays a count of how many files are in the feedback - otherwise it uses a helper function to write the entire list of files. This is because we want to keep the summaries really short so they can be displayed in a table. There will be a link to view the full feedback on the submission status page.

#### view()[​](#view "Direct link to view()")

```
publicfunctionview(stdClass$grade){
return$this->assignment->render_area_files(
'assignfeedback_file',
ASSIGNFEEDBACK_FILE_FILEAREA,
$grade->id
);
}
```

This function is called to display the entire feedback to both markers and students. In this case it uses the helper function in the assignment class to write the list of files.

#### can\_upgrade()[​](#can_upgrade "Direct link to can_upgrade()")

```
publicfunctioncan_upgrade($type,$version){

if(($type=='upload'||$type=='uploadsingle')&&$version>=2011112900){
returntrue;
}
returnfalse;
}
```

This function is used to identify old "Assignment 2.2" subtypes that can be upgraded by this plugin. This plugin supports upgrades from the old "upload" and "uploadsingle" assignment subtypes.

```
publicfunctionupgrade_settings(context$oldcontext,stdClass$oldassignment,&$log){
// first upgrade settings (nothing to do)
returntrue;
}
```

This function is called once per assignment instance to upgrade the settings from the old assignment to the new mod\_assign. In this case it returns true as there are no settings to upgrade.

```
publicfunctionupgrade(
context$oldcontext,
stdClass$oldassignment,
stdClass$oldsubmission,
stdClass$grade,
&$log
){
global$DB;

// now copy the area files
$this->assignment->copy_area_files_for_upgrade(
$oldcontext->id,
'mod_assignment',
'response',
$oldsubmission->id,
// New file area
$this->assignment->get_context()->id,
'assignfeedback_file',
ASSIGNFEEDBACK_FILE_FILEAREA,
$grade->id
);

// now count them!
$filefeedback=newstdClass();
$filefeedback->numfiles=$this->count_files($grade->id,ASSIGNFEEDBACK_FILE_FILEAREA);
$filefeedback->grade=$grade->id;
$filefeedback->assignment=$this->assignment->get_instance()->id;
if(!$DB->insert_record('assignfeedback_file',$filefeedback)>0){
$log.=get_string('couldnotconvertgrade','mod_assign',$grade->userid);
returnfalse;
}
returntrue;
}
```

This function upgrades a single submission from the old assignment type to the new one. In this case it involves copying all the files from the old filearea to the new one. There is a helper function available in the assignment class for this (Note: the copy will be fast as it is just adding rows to the files table). If this function returns false, the upgrade will be aborted and rolled back.

#### is\_empty()[​](#is_empty "Direct link to is_empty()")

```
publicfunctionis_empty(stdClass$submission){
return$this->count_files($submission->id,ASSIGNSUBMISSION_FILE_FILEAREA)==0;
}
```

If a plugin has no data to show then this function should return true from the `is_empty()` function. This prevents a table row from being added to the feedback summary for this plugin. It is also used to check if a grader has tried to save feedback with no data.

#### get\_file\_areas()[​](#get_file_areas "Direct link to get_file_areas()")

```
publicfunctionget_file_areas(){
return[ASSIGNFEEDBACK_FILE_FILEAREA=>$this->get_name()];
}
```

A plugin should implement `get_file_areas` if it supports saving of any files to moodle - this allows the file areas to be browsed by the moodle file manager.

#### delete\_instance()[​](#delete_instance "Direct link to delete_instance()")

```
publicfunctiondelete_instance(){
global$DB;
// will throw exception on failure
$DB->delete_records('assignfeedback_file',[
'assignment'=>$this->assignment->get_instance()->id,
]);

returntrue;
}
```

This function is called when a plugin is deleted. Note only database records need to be cleaned up - files belonging to fileareas for this assignment will be automatically cleaned up.

#### Gradebook features[​](#gradebook-features "Direct link to Gradebook features")

```
publicfunctionformat_for_gradebook(stdClass$grade){
returnFORMAT_MOODLE;
}

publicfunctiontext_for_gradebook(stdClass$grade){
return'';
}
```

Only one feedback plugin can push comments to the gradebook. Usually this is the feedback\_comments plugin - but it can be configured to be any feedback plugin. If the current plugin is the plugin chosen to generate comments for the gradebook, the comment text and format will be taken from these two functions.

```
/**
 * Override to indicate a plugin supports quickgrading
 *
 * @return boolean - True if the plugin supports quickgrading
 */
publicfunctionsupports_quickgrading(){
returnfalse;
}

/**
 * Get quickgrading form elements as html
 *
 * @param int $userid The user id in the table this quickgrading element relates to
 * @param mixed $grade grade or null - The grade data. May be null if there are no grades for this user (yet)
 * @return mixed - A html string containing the html form elements required for quickgrading or false to indicate this plugin does not support quickgrading
 */
publicfunctionget_quickgrading_html($userid,$grade){
returnfalse;
}

/**
 * Has the plugin quickgrading form element been modified in the current form submission?
 *
 * @param int $userid The user id in the table this quickgrading element relates to
 * @param stdClass $grade The grade
 * @return boolean - true if the quickgrading form element has been modified
 */
publicfunctionis_quickgrading_modified($userid,$grade){
returnfalse;
}

/**
 * Save quickgrading changes
 *
 * @param int $userid The user id in the table this quickgrading element relates to
 * @param stdClass $grade The grade
 * @return boolean - true if the grade changes were saved correctly
 */
publicfunctionsave_quickgrading_changes($userid,$grade){
returnfalse;
}
```

These 4 functions can be implemented to allow a plugin to support quick-grading. The feedback comments plugin is the only example of this in core.

```
/**
 * Run cron for this plugin
 */
publicstaticfunctioncron(){
}
```

A plugin can run code when cron runs by implementing this method.

```
/**
 * Return a list of the grading actions supported by this plugin.
 *
 * A grading action is a page that is not specific to a user but to the whole assignment.
 * @return array - An array of action and description strings.
 *                 The action will be passed to grading_action.
 */
publicfunctionget_grading_actions(){
return[];
}

/**
 * Show a grading action form
 *
 * @param string $gradingaction The action chosen from the grading actions menu
 * @return string The page containing the form
 */
publicfunctiongrading_action($gradingaction){
return'';
}
```

Grading actions appear in the select menu above the grading table and apply to the whole assignment. An example is "Upload grading worksheet". When a grading action is selected, the grading\_action will be called with the action that was chosen (so plugins can have multiple entries in the list).

```
/**
 * Return a list of the batch grading operations supported by this plugin.
 *
 * @return array - An array of action and description strings.
 *                 The action will be passed to grading_batch_operation.
 */
publicfunctionget_grading_batch_operations(){
return[];
}

/**
 * Show a batch operations form
 *
 * @param string $action The action chosen from the batch operations menu
 * @param array $users The list of selected userids
 * @return string The page containing the form
 */
publicfunctiongrading_batch_operation($action,$users){
return'';
}
```

These two callbacks allow adding entries to the batch grading operations list (where you select multiple users in the table and choose e.g. "Lock submissions" for every user). The action is passed to "grading\_batch\_operation" so that multiple entries can be supported by a plugin.

## Other features[​](#other-features "Direct link to Other features")

### Add calendar events[​](#add-calendar-events "Direct link to Add calendar events")

From Moodle 3.1 onwards, feedback plugins can add events to the Moodle calendar without side effects. These will be hidden and deleted in line with the assignment module. For example:

```
// Add release date to calendar
$calendarevent=newstdClass();
$calendarevent->name=get_string('calendareventname','assignsubmission_something');
$calendarevent->description=get_string('calendareventdesc','assignsubmission_something');
$calendarevent->courseid=$courseid;
$calendarevent->groupid=0;
$calendarevent->userid=$userid;
$calendarevent->modulename='assign';
$calendarevent->instance=$instanceid;
$calendarevent->eventtype='something_release';// For activity module's events, this can be used to set the alternative text of the event icon. Set it to 'pluginname' unless you have a better string.
$calendarevent->timestart=$releasedate;
$calendarevent->visible=true;
$calendarevent->timeduration=0;

calendar_event::create($calendarevent);
```