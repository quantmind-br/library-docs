---
title: Conditional activities API | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/apis/core/conditionalactivities
source: sitemap
fetched_at: 2026-02-17T15:02:07.609705-03:00
rendered_js: false
word_count: 469
summary: This document explains the Conditional Activities API, detailing how to manage activity availability through the condition_info class by fetching, updating, or deleting restricted access conditions.
tags:
    - moodle
    - conditional-activities-api
    - activity-availability
    - condition-info
    - php-api
    - course-module
category: api
---

The Conditional Activities API allowsyou to specify whether to hide, or show, an activity when a series of conditions associated with it are met.

note

This should not be confused with the [completion API](https://moodledev.io/docs/4.4/apis/core/activitycompletion) which is used to mark if an activity is completed or not. The Conditional Activities API is used to handle the *availability* of an activity, whilst the Completion API helps to track the *progress* of student in an activity.

## Files[​](#files "Direct link to Files")

The main file containing all key functions is located at `lib/conditionlib.php`..

## Functions and Examples[​](#functions-and-examples "Direct link to Functions and Examples")

The class `condition_info` defined in `lib/conditionlib.php` is the main conditional API in Moodle. Following are some important methods of the above mentioned class.

```
fill_availability_conditions($cm)
get_full_course_module()
add_completion_condition($cmid,$requiredcompletion)
add_grade_condition($gradeitemid,$min,$max,$updateinmemory=false)
wipe_conditions()
get_full_information($modinfo=null)
is_available($information,$grabthelot=false,$userid=0,$modinfo=null)
show_availability()
update_cm_from_form($cm,$fromform,$wipefirst=true)
```

The basic functionality of these methods can be classified as:-

1. Fetching information related to conditions
2. Adding/Updating conditional clauses to activities
3. Deleting conditions attached to activities

The following functions are normally used to fetch information regarding conditions associated with activities:

```
get_full_course_module();
get_full_information($modinfo=null);
is_available($information,$grabthelot=false,$userid=0,$modinfo=null);
show_availability();
```

#### get\_full\_course\_module()[​](#get_full_course_module "Direct link to get_full_course_module()")

This method can fetches and returns all necessary information as a course module object which are required to determine the availability conditions.

Example:-

```
$cm->id=$id;
$test=newcondition_info($cm,CONDITION_MISSING_EVERYTHING);
$fullcm=$test->get_full_course_module();
```

#### get\_full\_information()[​](#get_full_information "Direct link to get_full_information()")

This function returns a string which describes the various conditions in place for the activity in the given context.Some possible outputs can be:-

```
 a) From 13:05 on 14 Oct until 12:10 on 17Oct(exact, exact)
 b) From 14 Oct until 12:11 on 17Oct(midnight, exact)
 c) From 13:05 on 14 Oct until 17Oct(exact, midnight 18 Oct)
```

Please refer to the inline documentation in the code for detailed explanation of the logic and all possible cases.

Example:-

```
$ci=newcondition_info($mod);
$fullinfo=$ci->get_full_information();
```

#### is\_available()[​](#is_available "Direct link to is_available()")

This function is used to check if a given course module is currently available or not. A thing worth noting is that this doesn't take "visibility settings" and `viewhiddenactivities` capability into account. That is these settings should be properly checked after the result of is\_available(), before dumping any data to the user.

Example:-

```
$ci=newcondition_info((object)['id'=>$cmid],CONDITION_MISSING_EVERYTHING);
$bool=$ci->is_available($text,false,0);
```

#### show\_availability()[​](#show_availability "Direct link to show_availability()")

This function is used to check if information regarding availability of the current module should be shown to the user or not.

Example:-

```
$ci=newcondition_info((object)['id'=>$cmid],CONDITION_MISSING_EVERYTHING);
$bool=$ci->show_availability();
```

### Adding/Updating conditional clauses to activities[​](#addingupdating-conditional-clauses-to-activities "Direct link to Adding/Updating conditional clauses to activities")

```
fill_availability_conditions($cm);
add_completion_condition($cmid,$requiredcompletion);
add_grade_condition($gradeitemid,$min,$max,$updateinmemory=false);
update_cm_from_form($cm,$fromform,$wipefirst=true)
```

#### fill\_availability\_conditions()[​](#fill_availability_conditions "Direct link to fill_availability_conditions()")

This function adds any extra availability conditions to given course module object.

```
$rawmods=get_course_mods($courseid);
if(empty($rawmods)){
die;
}
if($sections=$DB->get_records("course_sections",["course"=>$courseid],"section ASC")){
foreach($sectionsas$section){
if(!empty($section->sequence)){
$sequence=explode(",",$section->sequence);
foreach($sequenceas$seq){
if(empty($rawmods[$seq])){
continue;
}
if(!empty($CFG->enableavailability)){
condition_info::fill_availability_conditions($rawmods[$seq]);
// Do something.
}
}
}
}
}
}
```

#### add\_completion\_condition()[​](#add_completion_condition "Direct link to add_completion_condition()")

In Moodle availability condition of a Module or activity can depend on another activity. For example activity B will not be unlocked until activity A is successfully completed. To add such inter-dependent conditions, this function is used.

Example:-

```
$test1=newcondition_info((object)['id'=>$cmid],CONDITION_MISSING_EVERYTHING);
$test1->add_completion_condition(13,3);
```

#### add\_grade\_condition()[​](#add_grade_condition "Direct link to add_grade_condition()")

This function is used to add a grade related restriction to an activity based on the grade secured in another activity. In the following example a minimum grade of 0.4 is required on gradeitem 666 to unlock the current activity in context.

Example:-

```
$test1=newcondition_info((object)['id'=>$cmid],CONDITION_MISSING_EVERYTHING);
$test1->add_grade_condition(666,0.4,null,true);
```

#### update\_cm\_from\_form()[​](#update_cm_from_form "Direct link to update_cm_from_form()")

This function is used to update availability conditions from a user submitted form.

Example:-

```
$fromform=$mform->get_data();
if(!empty($fromform->update)){
if(!empty($course->groupmodeforce)or!isset($fromform->groupmode)){
$fromform->groupmode=$cm->groupmode;// Keep the original.
}

// update course module first
$cm->groupmode=$fromform->groupmode;
$cm->groupingid=$fromform->groupingid;
$cm->groupmembersonly=$fromform->groupmembersonly;

$completion=newcompletion_info($course);
if($completion->is_enabled()){
// Update completion settings.
$cm->completion=$fromform->completion;
$cm->completiongradeitemnumber=$fromform->completiongradeitemnumber;
$cm->completionview=$fromform->completionview;
$cm->completionexpected=$fromform->completionexpected;
}
if(!empty($CFG->enableavailability)){
$cm->availablefrom=$fromform->availablefrom;
$cm->availableuntil=$fromform->availableuntil;
$cm->showavailability=$fromform->showavailability;
condition_info::update_cm_from_form($cm,$fromform,true);
}
// Do something else with the data.
}
```

### Deleting conditions attached to activities[​](#deleting-conditions-attached-to-activities "Direct link to Deleting conditions attached to activities")

we have a simple function wipe\_conditions() that can erase all conditions associated with the current activity. consider an example:-

```
$ci=newcondition_info($cm,CONDITION_MISSING_EVERYTHING,false);
$ci->wipe_conditions();
```

## See Also[​](#see-also "Direct link to See Also")

- [Conditional activities Adding module support](https://docs.moodle.org/dev/Conditional_activities_Adding_module_support)
- [Conditional activities](https://docs.moodle.org/dev/Conditional_activities) - original specification for this feature.

### User documentation[​](#user-documentation "Direct link to User documentation")

- [How to make a new availability condition plugin](https://moodledev.io/docs/4.4/apis/plugintypes/availability).
- [Conditional Activities](https://docs.moodle.org/en/Conditional_activities)
- [Conditional Activities Settings](https://docs.moodle.org/en/Conditional_activities_settings)
- [Using Conditional Activities](https://docs.moodle.org/en/Using_Conditional_activities)