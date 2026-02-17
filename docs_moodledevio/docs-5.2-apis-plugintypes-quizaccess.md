---
title: Quiz access rule sub-plugins | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/plugintypes/quizaccess
source: sitemap
fetched_at: 2026-02-17T15:44:49.090765-03:00
rendered_js: false
word_count: 1
summary: This document defines a PHP class for implementing overridable quiz access rules in Moodle, detailing the methods required to manage custom plugin settings within override forms and database tables.
tags:
    - moodle
    - quiz-access-rule
    - overrides
    - plugin-development
    - php-class
    - moodle-api
category: reference
---

\[path/to/quizaccessrule]/pluginname/rule.php

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
 * Rule definition class with override for the quizaccessrule_pluginname plugin.
 *
 * @package   quizaccessrule_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

usemod_quiz\form\edit_override_form;
usemod_quiz\local\access_rule_base;
usemod_quiz\local\rule_overridable;
useMoodleQuickForm;

classquizaccess_pluginnameextendsaccess_rule_baseimplementsrule_overridable{

/**
     * All of the below rule_overridable interface functions will need to be implemented.
     */

publicstaticfunctionadd_override_form_fields(edit_override_form$quizform,MoodleQuickForm$mform):void{
// Use the $mform to add the rule override fields...
$mform->addElement(
'select',
'plgn_setting1',
get_string('plgn_setting1','quizaccess_pluginname'),
['A','B','C'],
);

$mform->addElement(
'select',
'plgn_setting2',
get_string('plgn_setting2','quizaccess_pluginname'),
['1','2','3'],
);
}

publicstaticfunctionget_override_form_section_header():array{
// Return the label and content of the section header in an array.
return['name'=>'pluginname','title'=>get_string('pluginname','quizaccess_pluginname')];
}

publicstaticfunctionget_override_form_section_expand(edit_override_form$quizform):bool{
// Determine if rule section in override form should load expanded.
// Should typically return true if the quiz has existing rule settings.
global$DB;
return$DB->record_exists('quizaccess_pluginname',['quiz'=>$quizform->get_quiz()->id]);
}

publicstaticfunctionvalidate_override_form_fields(array$errors,
array$data,array$files,edit_override_form$quizform):array{
// Check and push to $errors array...
return$errors;
}

publicstaticfunctionsave_override_settings(array$override):void{
// Save $override data to plugin settings table...
global$DB;

$plgnoverride=(object)[
'overrideid'=>$override['overrideid'],
'setting1'=>$override['plgnm_setting1'],
'setting2'=>$override['plgnm_setting2'],
];

if($plgnoverrideid=$DB->get_field('quizaccess_pluginname_overrides','id',['overrideid'=>$override['overrideid']])){
$plgnoverride->id=$plgnoverrideid;
$DB->update_record('quizaccess_pluginname_overrides',$plgnoverride);
}else{
$DB->insert_record('quizaccess_pluginname_overrides',$plgnoverride);
}
}

publicstaticfunctiondelete_override_settings($quizid,$overrides):void{
// Remove $overrides from $quiz.
global$DB;
$ids=array_column($overrides,'id');
list($insql,$inparams)=$DB->get_in_or_equal($ids);
$DB->delete_records_select('quizaccess_pluginname_overrides',"id $insql",$inparams);
}

publicstaticfunctionget_override_setting_keys():array{
// Return string array of all override form setting keys.
return['plgnm_setting1','plgnm_setting2'];
}

publicstaticfunctionget_override_required_setting_keys():array{
// Return string array of override form setting keys that are required.
return['plgnm_setting1'];
}

publicstaticfunctionget_override_settings_sql($overridetablename):array{
// Return an array of selects, joins and parameters to be used to query relevant rule overrides...
return[
"plgnm.setting1 plgnm_setting1, plgnm.setting2 plgnm_setting2",
"LEFT JOIN {quizaccess_pluginname_overrides} plgnm ON plgnm.overrideid = {$overridetablename}.id",
[],
];
}

publicstaticfunctionadd_override_table_fields($override,$fields,$values,$context):array{
// Extend the override table view by adding fields and values that display the rule's overrides.
if(!empty($override->plgnm_setting1)){
$fields[]=get_string('pluginname','quizaccess_pluginname');
$values[]="{$override->plgnm_setting1}, {$override->plgnm_setting2}";
}
return[$fields,$values];
}
}
```