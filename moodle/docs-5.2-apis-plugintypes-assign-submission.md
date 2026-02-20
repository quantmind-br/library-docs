---
title: Assign submission plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/plugintypes/assign/submission
source: sitemap
fetched_at: 2026-02-17T15:44:01.856243-03:00
rendered_js: false
word_count: 1710
summary: This document explains how to develop assignment submission plugins for Moodle by detailing the required file structure, naming constraints, and essential class methods.
tags:
    - moodle-development
    - assignment-plugin
    - submission-plugin
    - plugin-structure
    - php-development
category: guide
---

An assignment submission plugin is used to display custom form fields to a student when they are editing their assignment submission. It also has full control over the display the submitted assignment to graders and students.

tip

For a good reference implementation, see the [onlinetext](https://github.com/moodle/moodle/tree/main/mod/assign/submission/onlinetext) submission plugin included with core because it uses most of the features of submission plugins.

## File structure[​](#file-structure "Direct link to File structure")

Assignment Feedback plugins are located in the `/mod/assign/submission` directory. A plugin should not include any custom files outside of it's own plugin folder.

Plugin naming

The plugin name should be no longer than 36 (11 before Moodle 4.3) characters - this is because the database tables for a submission plugin must be prefixed with `assignsubmission_[pluginname]` (17 chars + X) and the table names can be no longer than 53 (28 before Moodle 4.3) chars due to a limitation with PostgreSQL.

If a plugin requires multiple database tables, the plugin name will need to be shorter to allow different table names to fit under the 53 character limit (28 before Moodle 4.3).

Note: If your plugin is intended to work with versions of Moodle older than 4.3, then the plugin name must be 11 characters or shorter, and table names must be 28 characters or shorter.

Each plugin is in a separate subdirectory and consists of a number of *mandatory files* and any other files the developer is going to use.

important

Some of the important files are described below. See the [common plugin files](https://moodledev.io/docs/5.2/apis/commonfiles) documentation for details of other files which may be useful in your plugin.

View an example directory layout for the `assignfeedback_file` plugin.

```
mod/assign/submission/file
├── backup
│   └── moodle2
│       ├── backup_assignsubmission_file_subplugin.class.php
│       └── restore_assignsubmission_file_subplugin.class.php
├── classes
│   ├── event
│   │   ├── assessable_uploaded.php
│   │   ├── submission_created.php
│   │   └── submission_updated.php
│   └── privacy
│       └── provider.php
├── db
│   ├── access.php
│   └── install.xml
├── lang
│   └── en
│       └── assignsubmission_file.php
├── lib.php
├── locallib.php
├── settings.php
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

Full details on how to create settings are available in the [Admin settings](https://moodledev.io/docs/5.2/apis/subsystems/admin) documentation.

All submission plugins should include one setting named 'default' to indicate if the plugin should be enabled by default when creating a new assignment.

View example

\[path/to/assignsubmission]/file/settings.php

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
 * Plugin settings for the assignsubmission_file plugin.
 *
 * @package   assignsubmission_file
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

// Note: This is on by default.
$settings->add(
newadmin_setting_configcheckbox('assignsubmission_file/default',
newlang_string('default','assignsubmission_file'),
newlang_string('default_help','assignsubmission_file'),
1
)
);

if(isset($CFG->maxbytes)){
$name=newlang_string('maximumsubmissionsize','assignsubmission_file');
$description=newlang_string('configmaxbytes','assignsubmission_file');

$element=newadmin_setting_configselect(
'assignsubmission_file/maxbytes',
$name,
$description,
1048576,
get_max_upload_sizes($CFG->maxbytes)
);
$settings->add($element);
}
```

info

This example from the submission\_file plugin also checks to see if there is a maxbytes setting for this moodle installation and, if found, adds a new admin setting to the settings page.

### locallib.php[​](#locallibphp "Direct link to locallib.php")

#### Global support functions

##### File path: /locallib.php

This is where all the functionality for this plugin is defined. We will step through this file and describe each part as we go.

```
classassign_submission_fileextendsassign_submission_plugin{
```

All submission plugins MUST define a class with the component name of the plugin that extends assign\_submission\_plugin.

#### get\_name()[​](#get_name "Direct link to get_name()")

```
publicfunctionget_name(){
returnget_string('file','assignsubmission_file');
}
```

Get name is abstract in submission\_plugin and must be defined in your new plugin. Use the language strings to make your plugin translatable.

#### get\_settings()[​](#get_settings "Direct link to get_settings()")

```
publicfunctionget_settings(MoodleQuickForm$mform){
global$CFG,$COURSE;

$defaultmaxfilesubmissions=$this->get_config('maxfilesubmissions');
$defaultmaxsubmissionsizebytes=$this->get_config('maxsubmissionsizebytes');

$settings=[];
$options=[];
for($i=1;$i<=ASSIGNSUBMISSION_FILE_MAXFILES;$i++){
$options[$i]=$i;
}

$name=get_string('maxfilessubmission','assignsubmission_file');
$mform->addElement('select','assignsubmission_file_maxfiles',$name,$options);
$mform->addHelpButton(
'assignsubmission_file_maxfiles',
'maxfilessubmission',
'assignsubmission_file'
);
$mform->setDefault('assignsubmission_file_maxfiles',$defaultmaxfilesubmissions);
$mform->disabledIf('assignsubmission_file_maxfiles','assignsubmission_file_enabled','notchecked');

$choices=get_max_upload_sizes(
$CFG->maxbytes,
$COURSE->maxbytes,
get_config('assignsubmission_file','maxbytes')
);

$settings[]=[
'type'=>'select',
'name'=>'maxsubmissionsizebytes',
'description'=>get_string('maximumsubmissionsize','assignsubmission_file'),
'options'=>$choices,
'default'=>$defaultmaxsubmissionsizebytes,
];

$name=get_string('maximumsubmissionsize','assignsubmission_file');
$mform->addElement('select','assignsubmission_file_maxsizebytes',$name,$choices);
$mform->addHelpButton(
'assignsubmission_file_maxsizebytes',
'maximumsubmissionsize',
'assignsubmission_file'
);
$mform->setDefault('assignsubmission_file_maxsizebytes',$defaultmaxsubmissionsizebytes);
$mform->disabledIf(
'assignsubmission_file_maxsizebytes',
'assignsubmission_file_enabled',
'notchecked'
);
}
```

The "get\_settings" function is called when building the settings page for the assignment. It allows this plugin to add a list of settings to the form. Notice that the settings are prefixed by the plugin name which is good practice to avoid conflicts with other plugins.

#### save\_settings()[​](#save_settings "Direct link to save_settings()")

```
publicfunctionsave_settings(stdClass$data){
$this->set_config('maxfilesubmissions',$data->assignsubmission_file_maxfiles);
$this->set_config('maxsubmissionsizebytes',$data->assignsubmission_file_maxsizebytes);
returntrue;
}
```

The "save\_settings" function is called when the assignment settings page is submitted, either for a new assignment or when editing an existing one. For settings specific to a single instance of the assignment you can use the assign\_plugin::set\_config function shown here to save key/value pairs against this assignment instance for this plugin.

#### get\_form\_elements()[​](#get_form_elements "Direct link to get_form_elements()")

```
publicfunctionget_form_elements($submission,MoodleQuickForm$mform,stdClass$data){
if($this->get_config('maxfilesubmissions')<=0){
returnfalse;
}

$fileoptions=$this->get_file_options();
$submissionid=$submission?$submission->id:0;

$data=file_prepare_standard_filemanager(
$data,
'files',
$fileoptions,
$this->assignment->get_context(),
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$submissionid
);

$mform->addElement(
'filemanager',
'files_filemanager',
html_writer::tag('span',$this->get_name(),['class'=>'accesshide']),
null,
$fileoption
);

returntrue;
}
```

The get\_form\_elements function is called when building the submission form. It functions identically to the get\_settings function except that the submission object is available (if there is a submission) to associate the settings with a single submission. This example also shows how to use a filemanager within a submission plugin. The function must return true if it has modified the form otherwise the assignment will not include a header for this plugin.

#### save()[​](#save "Direct link to save()")

```
publicfunctionsave(stdClass$submission,stdClass$data){
global$USER,$DB;

$fileoptions=$this->get_file_options();

$data=file_postupdate_standard_filemanager(
$data,
'files',
$fileoptions,
$this->assignment->get_context(),
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$submission->id
);

$filesubmission=$this->get_file_submission($submission->id);

// Plagiarism code event trigger when files are uploaded.

$fs=get_file_storage();
$files=$fs->get_area_files(
$this->assignment->get_context()->id,
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$submission->id,
'id',
false
);

$count=$this->count_files($submission->id,ASSIGNSUBMISSION_FILE_FILEAREA);

// Send files to event system.
// This lets Moodle know that an assessable file was uploaded (eg for plagiarism detection).
$eventdata=newstdClass();
$eventdata->modulename='assign';
$eventdata->cmid=$this->assignment->get_course_module()->id;
$eventdata->itemid=$submission->id;
$eventdata->courseid=$this->assignment->get_course()->id;
$eventdata->userid=$USER->id;
if($count>1){
$eventdata->files=$files;
}
$eventdata->file=$files;
$eventdata->pathnamehashes=array_keys($files);
events_trigger('assessable_file_uploaded',$eventdata);

if($filesubmission){
$filesubmission->numfiles=$this->count_files($submission->id,
ASSIGNSUBMISSION_FILE_FILEAREA);
return$DB->update_record('assignsubmission_file',$filesubmission);
}else{
$filesubmission=newstdClass();
$filesubmission->numfiles=$this->count_files($submission->id,
ASSIGNSUBMISSION_FILE_FILEAREA);
$filesubmission->submission=$submission->id;
$filesubmission->assignment=$this->assignment->get_instance()->id;
return$DB->insert_record('assignsubmission_file',$filesubmission)>0;
}
```

The "save" function is called to save a user submission. The parameters are the submission object and the data from the submission form. This example calls `file_postupdate_standard_filemanager` to copy the files from the draft file area to the filearea for this submission, it then uses the event api to trigger an assessable\_file\_uploaded event for the plagiarism api. It then records the number of files in the plugin specific "assignsubmission\_file" table.

#### get\_files()[​](#get_files "Direct link to get_files()")

```
publicfunctionget_files($submission){
$result=[];
$fs=get_file_storage();

$files=$fs->get_area_files(
$this->assignment->get_context()->id,
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$submission->id,
'timemodified',
false
);

foreach($filesas$file){
$result[$file->get_filename()]=$file;
}
return$result;
}
```

If this submission plugin produces one or more files, it should implement "get\_files" so that the portfolio API can export a list of all the files from all of the plugins for this assignment submission. This is also used by the offline grading feature in the assignment.

#### view\_summary()[​](#view_summary "Direct link to view_summary()")

```
publicfunctionview_summary(stdClass$submission,&$showviewlink){
$count=$this->count_files($submission->id,ASSIGNSUBMISSION_FILE_FILEAREA);

// Show we show a link to view all files for this plugin.
$showviewlink=$count>ASSIGNSUBMISSION_FILE_MAXSUMMARYFILES;
if($count<=ASSIGNSUBMISSION_FILE_MAXSUMMARYFILES){
return$this->assignment->render_area_files(
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$submission->id
);
}

returnget_string('countfiles','assignsubmission_file',$count);
}
```

The view\_summary function is called to display a summary of the submission to both markers and students. It counts the number of files submitted and if it is more that a set number, it only displays a count of how many files are in the submission - otherwise it uses a helper function to write the entire list of files. This is because we want to keep the summaries really short so they can be displayed in a table. There will be a link to view the full submission on the submission status page.

#### view()[​](#view "Direct link to view()")

```
publicfunctionview($submission){
return$this->assignment->render_area_files(
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$submission->id
);
}
```

The view function is called to display the entire submission to both markers and students. In this case it uses the helper function in the assignment class to write the list of files.

#### submission\_summary\_for\_email()[​](#submission_summary_for_email "Direct link to submission_summary_for_email()")

```
#[\Override]
publicfunctionsubmission_summary_for_messages(stdClass$submission):array{
global$PAGE;

$onlinetextsubmission=$this->get_onlinetext_submission($submission->id);
if(!$onlinetextsubmission||!$onlinetextsubmission->onlinetext){
return['',''];
}

$renderer=$PAGE->get_renderer('mod_assign');
$templatecontext=['wordcount'=>count_words($onlinetextsubmission->onlinetext)];
return[
// Mustache strips off all trailing whitespace, but we want a newline at the end.
$renderer->render_from_template(
'assignsubmission_onlinetext/notification_text',$templatecontext)."\n",
$renderer->render_from_template(
'assignsubmission_onlinetext/notification_html',$templatecontext),
];
}
```

This method produces a summary of what was submitted, in a form suitable to include in messages (for example, the 'You have submitted' confirmation). Moodle messages can be plain text or HTML, so you need to prepare both. It is recommended to use templates so themes can override it if they want to. As you produce your output, think about the fact that multiple Submission plugins may be in use at the same time, in which case your summary will appear alongside other summaries.

#### can\_upgrade()[​](#can_upgrade "Direct link to can_upgrade()")

```
publicfunctioncan_upgrade($type,$version){
$uploadsingle_type='uploadsingle';
$upload_type='upload';

if(($type==$uploadsingle_type||$type==$upload_type)&&$version>=2011112900){
returntrue;
}
returnfalse;
}
```

The can\_upgrade function is used to identify old "Assignment 2.2" subtypes that can be upgraded by this plugin. This plugin supports upgrades from the old "upload" and "uploadsingle" assignment subtypes.

#### upgrade\_settings()[​](#upgrade_settings "Direct link to upgrade_settings()")

```
publicfunctionupgrade_settings(context$oldcontext,stdClass$oldassignment,&$log){
global$DB;

if($oldassignment->assignmenttype=='uploadsingle'){
$this->set_config('maxfilesubmissions',1);
$this->set_config('maxsubmissionsizebytes',$oldassignment->maxbytes);
returntrue;
}

if($oldassignment->assignmenttype=='upload'){
$this->set_config('maxfilesubmissions',$oldassignment->var1);
$this->set_config('maxsubmissionsizebytes',$oldassignment->maxbytes);

// Advanced file upload uses a different setting to do the same thing.
$DB->set_field(
'assign',
'submissiondrafts',
$oldassignment->var4,
['id'=>$this->assignment->get_instance()->id]
);

// Convert advanced file upload "hide description before due date" setting.
$alwaysshow=0;
if(!$oldassignment->var3){
$alwaysshow=1;
}
$DB->set_field(
'assign',
'alwaysshowdescription',
$alwaysshow,
['id'=>$this->assignment->get_instance()->id]
);
returntrue;
}
}
```

This function is called once per assignment instance to upgrade the settings from the old assignment to the new mod\_assign. In this case it sets the `maxbytes`, `maxfiles` and `alwaysshowdescription` configuration settings.

#### upgrade()[​](#upgrade "Direct link to upgrade()")

```
publicfunctionupgrade($oldcontext,$oldassignment,$oldsubmission,$submission,&$log){
global$DB;

$filesubmission=(object)[
'numfiles'=>$oldsubmission->numfiles,
'submission'=>$submission->id,
'assignment'=>$this->assignment->get_instance()->id,
];

if(!$DB->insert_record('assign_submission_file',$filesubmission)>0){
$log.=get_string('couldnotconvertsubmission','mod_assign',$submission->userid);
returnfalse;
}

// now copy the area files
$this->assignment->copy_area_files_for_upgrade(
$oldcontext->id,
'mod_assignment',
'submission',
$oldsubmission->id,
// New file area
$this->assignment->get_context()->id,
'mod_assign',
ASSIGN_FILEAREA_SUBMISSION_FILES,
$submission->id
);

returntrue;
}
```

The "upgrade" function upgrades a single submission from the old assignment type to the new one. In this case it involves copying all the files from the old filearea to the new one. There is a helper function available in the assignment class for this (Note: the copy will be fast as it is just adding rows to the files table). If this function returns false, the upgrade will be aborted and rolled back.

#### get\_editor\_fields()[​](#get_editor_fields "Direct link to get_editor_fields()")

```
publicfunction(){
return[
'onlinetext'=>get_string('pluginname','assignsubmission_comments'),
];
}
```

This example is from assignsubmission\_onlinetext. If the plugin uses a text-editor it is ideal if the plugin implements "get\_editor\_fields". This allows the portfolio to retrieve the text from the plugin when exporting the list of files for a submission. This is required because the text is stored in the plugin specific table that is only known to the plugin itself. If a plugin supports multiple text areas it can return the name of each of them here.

#### get\_editor\_text()[​](#get_editor_text "Direct link to get_editor_text()")

```
publicfunctionget_editor_text($name,$submissionid){
if($name=='onlinetext'){
$onlinetextsubmission=$this->get_onlinetext_submission($submissionid);
if($onlinetextsubmission){
return$onlinetextsubmission->onlinetext;
}
}

return'';
}
```

This example is from assignsubmission\_onlinetext. If the plugin uses a text-editor it is ideal if the plugin implements "get\_editor\_text". This allows the portfolio to retrieve the text from the plugin when exporting the list of files for a submission. This is required because the text is stored in the plugin specific table that is only known to the plugin itself. The name is used to distinguish between multiple text areas in the one plugin.

#### get\_editor\_format()[​](#get_editor_format "Direct link to get_editor_format()")

```
publicfunctionget_editor_format($name,$submissionid){
if($name=='onlinetext'){
$onlinetextsubmission=$this->get_onlinetext_submission($submissionid);
if($onlinetextsubmission){
return$onlinetextsubmission->onlineformat;
}
}

return0;
}
```

This example is from assignsubmission\_onlinetext. For the same reason as the previous function, if the plugin uses a text editor, it is ideal if the plugin implements "get\_editor\_format". This allows the portfolio to retrieve the text from the plugin when exporting the list of files for a submission. This is required because the text is stored in the plugin specific table that is only known to the plugin itself. The name is used to distinguish between multiple text areas in the one plugin.

#### is\_empty()[​](#is_empty "Direct link to is_empty()")

```
publicfunctionis_empty(stdClass$submission){
return$this->count_files($submission->id,ASSIGNSUBMISSION_FILE_FILEAREA)==0;
}
```

If a plugin has no submission data to show - it can return true from the is\_empty function. This prevents a table row being added to the submission summary for this plugin. It is also used to check if a student has tried to save an assignment with no data.

#### submission\_is\_empty()[​](#submission_is_empty "Direct link to submission_is_empty()")

```
publicfunctionsubmission_is_empty(){
global$USER;
$fs=get_file_storage();

// Get a count of all the draft files, excluding any directories.
$files=$fs->get_area_files(
context_user::instance($USER->id)->id,
'user',
'draft',
$data->files_filemanager,
'id',
false
);

returncount($files)==0;
}
```

Determine if a submission is empty. This is distinct from is\_empty() in that it is intended to be used to determine if a submission made before saving is empty.

#### get\_file\_areas()[​](#get_file_areas "Direct link to get_file_areas()")

```
publicfunctionget_file_areas(){
return[ASSIGNSUBMISSION_FILE_FILEAREA=>$this->get_name()];
}
```

A plugin should implement get\_file\_areas if it supports saving of any files to moodle - this allows the file areas to be browsed by the moodle file manager.

#### copy\_submission()[​](#copy_submission "Direct link to copy_submission()")

```
publicfunctioncopy_submission(stdClass$sourcesubmission,stdClass$destsubmission){
global$DB;

// Copy the files across.
$contextid=$this->assignment->get_context()->id;
$fs=get_file_storage();
$files=$fs->get_area_files(
$contextid,
'assignsubmission_file',
ASSIGNSUBMISSION_FILE_FILEAREA,
$sourcesubmission->id,
'id',
false
);
foreach($filesas$file){
$fieldupdates=['itemid'=>$destsubmission->id];
$fs->create_file_from_storedfile($fieldupdates,$file);
}

// Copy the assignsubmission_file record.
if($filesubmission=$this->get_file_submission($sourcesubmission->id)){
unset($filesubmission->id);
$filesubmission->submission=$destsubmission->id;
$DB->insert_record('assignsubmission_file',$filesubmission);
}
returntrue;
}
```

Since Moodle 2.5 - a students submission can be copied to create a new submission attempt. Plugins should implement this function if they store data associated with the submission (most plugins).

#### format\_for\_log()[​](#format_for_log "Direct link to format_for_log()")

```
publicfunctionformat_for_log(stdClass$submission){
// Format the information for each submission plugin add_to_log
$filecount=$this->count_files($submission->id,ASSIGNSUBMISSION_FILE_FILEAREA);
return' the number of file(s) : '.$filecount." file(s).<br>";
}
```

The format\_for\_log function lets a plugin produce a really short summary of a submission suitable for adding to a log message.

#### delete\_instance()[​](#delete_instance "Direct link to delete_instance()")

```
publicfunctiondelete_instance(){
global$DB;
// Will throw exception on failure
$DB->delete_records('assignsubmission_file',[
'assignment'=>$this->assignment->get_instance()->id,
]);

returntrue;
}
```

The delete\_instance function is called when a plugin is deleted. Note only database records need to be cleaned up - files belonging to fileareas for this assignment will be automatically cleaned up.

## Useful classes[​](#useful-classes "Direct link to Useful classes")

A submission plugin has access to a number of useful classes in the assignment module. See the phpdocs (or the code) for more information on these classes.

### assign\_plugin[​](#assign_plugin "Direct link to assign_plugin")

This abstract class is the base class for all assignment plugins (feedback or submission plugins).

It provides access to the assign class which represents the current assignment instance through "$this-&gt;assignment".

### assign\_submission\_plugin[​](#assign_submission_plugin "Direct link to assign_submission_plugin")

This is the base class all assignment submission plugins must extend. It contains a small number of additional function that only apply to submission plugins.

### assign[​](#assign "Direct link to assign")

This is the main class for interacting with the assignment module.

It contains public functions that are useful for listing users, loading and updating submissions, loading and updating grades, displaying users etc.

## Other features[​](#other-features "Direct link to Other features")

### Add calendar events[​](#add-calendar-events "Direct link to Add calendar events")

Submission plugins can add events to the Moodle calendar without side effects. These will be hidden and deleted in line with the assignment module. For example:

```
// Add release date to calendar.
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

This code should be placed in the `save_settings()` method of your assign\_submission\_plugin class.