---
title: Enrolment API | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/enrol
source: sitemap
fetched_at: 2026-02-17T15:45:26.487687-03:00
rendered_js: false
word_count: 886
summary: This document explains the technical implementation of the enrolment API, covering the distinction between enrolments and role assignments, core API functions, and plugin-specific methods for managing user course participation.
tags:
    - moodle-development
    - enrolment-api
    - user-management
    - plugin-methods
    - course-participation
category: api
---

The enrolment API gives access to the enrolment methods and also to [enrolment plugins](https://moodledev.io/docs/5.2/apis/plugintypes/enrol) instances.

## Difference between user enrolment and role assignment[​](#difference-between-user-enrolment-and-role-assignment "Direct link to Difference between user enrolment and role assignment")

Users enrolled in a course have at least one record in `user_enrolments` table. This table has the relation between courses and users **through an enrolment plugin instance**. However, `user_enrolments` does not contain information about the user role in the course, only information about:

- **Enrolment plugin instance**
- **Enrolment status** (active or suspended).
- **Enrolment Start and end dates**.

The specific role assignments are related to the context, not only to course (as activities and other pages can use its own). The specific roles of a user are stored in the `role_assignments` table. This table stores:

- The **user role id** in the **context**
- The **component item** that assigned the role. In the case of a regular course, the *component* is the name of the enrolment plugin and the *item id* is the specific plugin instance.

### What is enrolment?[​](#what-is-enrolment "Direct link to What is enrolment?")

Enrolled users may fully participate in a course. Active user enrolment allows user to enter course. Only enrolled users may be group members. Grades are stored only for enrolled users.

### Unenrolment[​](#unenrolment "Direct link to Unenrolment")

Unenrolment is irreversible operation that purges user participation information. Full unenrolment is suitable only if you do not need to preserve all course participation information including user grades.

### Enrolment status[​](#enrolment-status "Direct link to Enrolment status")

Instead of full unenrolment it is usually better to only *suspend* user enrolment. If there are other ways to enter the course (such guest access) it is recommended to remove user roles at the same time.

Enrolments have two states defined by two constants:

- `ENROL_USER_ACTIVE` the enrolment is active
- `ENROL_USER_SUSPENDED` the enrolment is suspended

### Activity participation[​](#activity-participation "Direct link to Activity participation")

Activity developers decide the enrolment related behaviour of module.

There are some general guidelines:

- Only users with active enrolments should receive notifications.
- Activities should display enrolled users with some capability as participants.
- By default only users with active enrolments should be displayed in reports.
- There should be option to display all enrolled users including suspended enrolments.
- For performance reasons invisible participation data should be purged on unenrolment.
- Contributions visible by other participants should be kept after unenrolment (such as forum posts).

## API functions[​](#api-functions "Direct link to API functions")

### is\_enrolled()[​](#is_enrolled "Direct link to is_enrolled()")

Use this method to determine if a user is enrolled into a course. This method returns true for students and teachers, but false for administrators and other managers.

caution

User enrolments can be either active or suspended, suspended users can not enter the course (unless there is some kind of guest access allowed or have `moodle/course:view` capability) and are usually hidden in the UI.

```
functionis_enrolled(
context$context,
stdClass$user=null,
string$withcapability='',
bool$onlyactive=false
)
```

Good example is choice module where we have one slot for each participant, people that are not enrolled are not allowed to vote `is_enrolled($context, $USER, 'mod/choice:choose')`. Another example is assignment where users need to be enrolled and have capability to submit assignments `is_enrolled($this->context, $USER, 'mod/assignment:submit')`.

### get\_enrolled\_users()[​](#get_enrolled_users "Direct link to get_enrolled_users()")

Returns the list of enrolled users. This method allows to filter the result by capability, pagination or state.

```
functionget_enrolled_users(
context$context,
string$withcapability='',
int$groupid=0,
string$userfields='u.*',
?string$orderby=null,
int$limitfrom=0,
int$limitnum=0,
bool$onlyactive=false
)
```

View example

Get all users who are able to submit an assignment:

```
$submissioncandidates=get_enrolled_users($modcontext,'mod/assign:submit');
```

### count\_enrolled\_users()[​](#count_enrolled_users "Direct link to count_enrolled_users()")

This method is used to get the total count of enrolments of a context. As `get_enrolled_users` this methods allow several filters like capability, group id or counting only active enrollments.

```
functioncount_enrolled_users(
context$context,
string$withcapability='',
int$groupid=0,
bool$onlyactive=false
)
```

### get\_enrolled\_sql()[​](#get_enrolled_sql "Direct link to get_enrolled_sql()")

SQL `select from get_enrolled_sql()` is often used for performance reasons as it can be used in joins to get specific information for enrolled users only.

```
functionget_enrolled_sql(
context$context,
string$withcapability='',
int$groupid=0,
bool$onlyactive=false,
bool$onlysuspended,
int$enrolid=0
)
```

### enrol\_get\_plugin(): enrol\_plugin[​](#enrol_get_plugin-enrol_plugin "Direct link to enrol_get_plugin(): enrol_plugin")

Returns the enrolment plugin base class with the given name.

View example

```
$instance=$DB->get_record('enrol',['courseid'=>$course->id,'enrol'=>'manual']);
$enrolplugin=enrol_get_plugin($instance->enrol);
$enrolplugin->enrol_user($instance,$user->id,$role->id,$timestart,$timeend);
```

note

As can be seen in the example, to use the plugin enrol\_user and unenrol\_user methods you need to get the instance record of the plugin first.

## Enrolment plugin methods[​](#enrolment-plugin-methods "Direct link to Enrolment plugin methods")

Once you use `enrol_get_plugin` function to get the enrolment plugin instance, you can use that class to modify the enrolments.

### $enrol\_plugin-&gt;enrol\_user()[​](#enrol_plugin-enrol_user "Direct link to $enrol_plugin->enrol_user()")

Using this method you can enrol a user into a course.

The method takes the following parameters:

- Enrol plugin instance record
- User id
- Role id
- Optional enrolment start and end timestamps
- Optional enrolment status (ENROL\_USER\_ACTIVE or ENROL\_USER\_SUSPENDED)
- If the enrol must try to recover the previous user enrolment grades (if any)

```
$enrolplugin->enrol_user($instance,$user->id,$role->id,$timestart,$timeend,ENROL_USER_ACTIVE);
```

### $enrol\_plugin-&gt;unenrol\_user()[​](#enrol_plugin-unenrol_user "Direct link to $enrol_plugin->unenrol_user()")

Unenrol a user from a course enrolment method.

note

Other enrolment methods can define other roles to the same user.

The method takes the following parameters:

- Enrol plugin instance record
- User id

```
$enrolplugin->unenrol_user($instance,$user->id);
```

### $enrol\_plugin-&gt;update\_user\_enrol()[​](#enrol_plugin-update_user_enrol "Direct link to $enrol_plugin->update_user_enrol()")

Updates a user enrolment **status** and the **start or end dates**.

The method takes the following parameters:

- Enrol plugin instance record
- User id
- Optional enrolment start and end timestamps
- Optional enrolment status (ENROL\_USER\_ACTIVE or ENROL\_USER\_SUSPENDED)

```
$enrolplugin->update_user_enrol($instance,$user->id,$timestart,$timeend,ENROL_USER_SUSPENDED);
```

### $enrol\_plugin-&gt;add\_default\_instance()[​](#enrol_plugin-add_default_instance "Direct link to $enrol_plugin->add_default_instance()")

Add a new enrolment instance to a specific course an returns the instance id. This method will create a new instance record in the `enrol` table with the default values.

The method takes the following parameters:

- Course id

```
$enrolplugin->add_default_instance($course->id);
```

### $enrol\_plugin-&gt;add\_custom\_instance()[​](#enrol_plugin-add_custom_instance "Direct link to $enrol_plugin->add_custom_instance()")

Add a new enrolment instance to a specific course with custom settings an returns the instance id. This method will create a new instance record in the `enrol` table with the specified settings.

The method takes the following parameters:

- Course object
- Array of instance settings

```
$enrolplugin->add_custom_instance($course,$settings);
```

### $enrol\_plugin-&gt;delete\_instance()[​](#enrol_plugin-delete_instance "Direct link to $enrol_plugin->delete_instance()")

Remove an enrolment instance form a course and invalidate all related user enrolments.

The method takes the following parameters:

- Enrol plugin instance record

```
$enrolplugin->delete_instance($instance);
```

### $enrol\_plugin-&gt;is\_csv\_upload\_supported()[​](#enrol_plugin-is_csv_upload_supported "Direct link to $enrol_plugin->is_csv_upload_supported()")

Checks whether enrolment plugin is supported in CSV course upload. Defaults to false. Override this function in your enrolment plugin if you want it to be supported in CSV course upload.

## See also[​](#see-also "Direct link to See also")

- [Enrolment plugins](https://moodledev.io/docs/5.2/apis/plugintypes/enrol)