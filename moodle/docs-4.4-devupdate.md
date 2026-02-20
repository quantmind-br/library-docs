---
title: Moodle 4.4 developer update | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/devupdate
source: sitemap
fetched_at: 2026-02-17T15:05:08.924847-03:00
rendered_js: false
word_count: 2023
summary: This document outlines the key architectural and API updates for developers in Moodle 4.4, including the introduction of Dependency Injection and PHP 8.0 Attribute support.
tags:
    - moodle-4-4
    - dependency-injection
    - php-attributes
    - hooks-api
    - string-formatting
    - tasks-api
    - moodle-development
category: reference
---

This page highlights the important changes that are coming in Moodle 4.4 for developers.

## Core changes[​](#core-changes "Direct link to Core changes")

### Dependency Injection[​](#dependency-injection "Direct link to Dependency Injection")

Support for PSR-11 compatible Containers has been introduced and can be accessed via the `\core\di` class. Read the [full documentation](https://moodledev.io/docs/4.4/apis/core/di) for information on how to use Moodle's DI infrastructure.

### Attributes[​](#attributes "Direct link to Attributes")

PHP 8.0 introduced support for the Attribute language feature and Moodle is beginning to make use of this in small but helpful ways.

To simplify this adoption, a new `\core\attribute_helper` class has been created with methods to quickly and easily fetch the `\ReflectionAttribute` for any relevant attributes.

The new methods can search for an attribute using a reference, which can be:

- a string, whose name represents a global function, a class, or a class combined with a method, property, constant, or enum
- an instantiated object
- an array whose first value is either a string or object, and whose optional second value is a child of the first value

Fetching attributes

```
<?php

usecore\attribute_helper;
use core\attribute\{label, tags};

// Get a label on the \some_function_name() method.
$label=attribute_helper::one_from('some_function_name',label::class)?->newInstance();

// Get an instance of a label on the \example class.
$label=attribute_helper::one_from(example::class,label::class)?->newInstance();

// Get an instance of a label on an instance of the \example class.
$example=newexample();
$label=attribute_helper::one_from($example,label::class)?->newInstance();

// Get an instance of a label on a constant, property, or method of the \example class.
$label=attribute_helper::one_from([example::class,'some_child'],label::class)?->newInstance();

// Get an instance of a label on a constant, property, or method of an instance of the \example class.
$example=newexample();
$label=attribute_helper::one_from([$example,'some_child'],label::class)?->newInstance();
```

Other variations of the above are also possible.

### Hooks[​](#hooks "Direct link to Hooks")

#### Hook interfaces[​](#hook-interfaces "Direct link to Hook interfaces")

Attribute-based alternatives to the `\core\hook\described_hook`, and `\core\hook\deprecated_callback_replacement` interfaces are now supported.

- the `\core\attribute\label` attribute can be used to add a string-based description of the hook.
- the `\core\attribute\tags` attribute can be used to add one or more tags to describe the hook.
- the `\core\attribute\hook\replaces_callbacks` attribute can be used to add one or more replaced callbacks.

```
<?php

namespacecore\hook;

usecore\attribute;

#[attribute\label('This is a description of the hook')]
#[attribute\tags('examples','navigation','authentication')]
#[attribute\hook\replaces_callbacks('an_old_callback_that_is_replaced_here')]
classbefore_navigation_render{
publicfunction__construct(
publicreadonly\navigation_node$navigation,
){
}
}
```

tip

It is still possible to use the `\core\hook\described_hook` and `\core\hook\deprecated_callback_replacement` interfaces. The attribute approach is provided as a more light-weight alternative.

#### Callable notation[​](#callable-notation "Direct link to Callable notation")

When specifying the callback for a hook, you can now do so using the callable array notation, for example:

- Array notation
- String notation
- Alternate string notation (discouraged)

```
$callbacks=[
[
'hook'=>'test_plugin\\hook\\hook',
// Array notation:
'callback'=>[\test_plugin\callbacks::class,'test1'],
],
];
```

Callbacks in earlier versions of Moodle

If writing a callback for Moodle 4.3, you **must** use the string notation.

### String formatting[​](#string-formatting "Direct link to String formatting")

#### Deprecation of format\_* parameters[​](#deprecation-of-format_-parameters "Direct link to Deprecation of format_* parameters")

A number of legacy features and ways of calling `format_text`, and `format_string` now emit deprecation notices. These were all deprecated a long time ago but did not emit:

- Changes to `format_string`:
  
  - The `$options` array *must not* be a `\context` or `\core\context` object. This was never supported and behaviour was previously undetected
  - Unknown values passed to the `$options` parameter will now emit appropriate debugging notices
- Changes to `format_text`:
  
  - The fourth parameter, `$courseiddonotuse` now emits a deprecation notice if provided. This was deprecated for Moodle 2.0 in [MDL-22001](https://moodle.atlassian.net/browse/MDL-22001)
  - The `smiley` option now emits a deprecation notice. This was deprecated for Moodle 2.0.
  - The `nocache` option now emits a deprecation notice. This was deprecated for Moodle 2.3 in [MDL-34347](https://moodle.atlassian.net/browse/MDL-34347)
  - The use of `FORMAT_WIKI` as a source format now throws an exception. Previously it added debugging information to the rendered content. This was deprecated in Moodle 1.5.
  - Unknown values passed to the `$options` parameter will now emit appropriate debugging notices

#### New \\core\\formatting class[​](#new-coreformatting-class "Direct link to New \core\formatting class")

A new `\core\formatting` class has been introduced with new `format_string()`, and `format_text()` methods.

These methods no longer user the `array $options` style configuration, instead expanding options into method parameters.

note

The existing `\format_string()`, and `\format_text()` methods remain in place, and are *not currently deprecated*. At this time *you do* not need to migrate to the APIs.

New \\core\\formatting methods

```
namespacecore;

classformatting{
publicfunctionformat_string(
?string$string,
bool$striplinks=true,
?context$context=null,
bool$filter=true,
bool$escape=true,
):string;

publicfunctionformat_text(
?string$text,
string$format=FORMAT_MOODLE,
?context$context=null,
bool$trusted=false,
?bool$clean=null,
bool$filter=true,
bool$para=true,
bool$newlines=true,
bool$overflowdiv=false,
bool$blanktarget=false,
bool$allowid=false,
):string;
}
```

If choosing to use these new methods you **must** use Dependency Injection either via injection into the class, or via the `\core\di` container. You **must not** instantiate the `\core\formatting` class directly.

- Usage via Dependency Injection
- Usage via the \\core\\di container

Usage in an injected class

```
namespacecore;

classexample{
publicfunction__construct(
protectedreadonly\core\formatting$formatter,
){
}

publicfunctiondo_something(string$input):string{
return$this->formatter->format_string($input,...);
}
}
```

Named Parameters

- Recommended usage
- Alternative approach

It is *strongly recommended* that you make use of named parameters for all but the first argument when calling them, rather than using positional arguments.

Named arguments

```
$formatter=\core\di::get(\core\formatting::class);

$formatter->format_string(
"The content to be formatted",
context:\core\context\course::instance($courseid),
filter:false,
);

$formatter->format_text(
"The content to be formatted",
context:\core\context\course::instance($courseid),
filter:false,
blanktarget:true,
);
```

### Tasks API[​](#tasks-api "Direct link to Tasks API")

Support for tasks which block all other tasks has been removed. The ability to configure a task as blocking is no longer supported and will not work.

This functionality had the ability to cause significant performance issues, and contained a number of serious bugs.

caution

If you are using this functionality in older versions of Moodle you are advised to move away from it as soon as possible in all Moodle versions.

The behaviour of the task runner has been changed to limit the number of retries allowed before a failing *adhoc* task is removed. Scheduled tasks are not affected.

The default value for the maximum retry limit on an Ad-hoc task is **12**.

Retries can be entirely disabled by passing a value of `0`, for example:

```
$task=newexample_task();
// This task wil not be retried at all.
$task->set_attempts_available(0);
\core\task\manager::queue_task($task);
```

See the [detailed documentation](https://moodledev.io/docs/4.4/apis/subsystems/task/adhoc#retrying-failing-tasks) on how to use these new APIs.

### JavaScript[​](#javascript "Direct link to JavaScript")

A new JS module, `core/dropzone`, has been introduced to provide a standardised way to create a Drop-zone in Moodle. Read the [full documentation](https://moodledev.io/docs/4.4/guides/javascript#dropzone) for information on how to use it.

## Parameters[​](#parameters "Direct link to Parameters")

### API Change[​](#api-change "Direct link to API Change")

Parameter constants, and the cleaning of values using these parameters, has been moved to a new enum in `\core\param`.

The enum contains relevant associated methods for fetching, validating, and cleaning the content of values, for example:

Examples of enum-based parameters

```
// Clean an existing variable.
$value=\core\param::ALPHANUMEXT->clean($value);
$value=\core\param::ALPHANUMEXT->validate_param($value);
$value=\core\param::ALPHANUMEXT->clean_param_array($value);

// Require a param (replaced required_param).
$value=\core\param::ALPHANUMEXT->required_param('someparamname');
$value=\core\param::ALPHANUMEXT->optional_param('someparamname','defaultvalue');
$value=\core\param::ALPHANUMEXT->required_param_array('someparamname');
$value=\core\param::ALPHANUMEXT->optional_param_array('someparamname',[]);
```

note

The existing `PARAM_*` constants, and related methods (`required_param`, `optional_param()`, `clean_param()`, and so on) remain in place, and are *not currently deprecated*. At this time *you do* not need to migrate to the APIs.

### Deprecations[​](#deprecations "Direct link to Deprecations")

A number of deprecated parameter types have been deprecated, these include:

- `PARAM_CLEAN`
- `PARAM_INTEGER`
- `PARAM_NUMBER`
- `PARAM_ACTION`
- `PARAM_FORMAT`
- `PARAM_MULTILANG`
- `PARAM_CLEANFILE`

These param types have all been deprecated since Moodle 2.0.

## Introduction of `deprecated` attribute[​](#introduction-of-deprecated-attribute "Direct link to introduction-of-deprecated-attribute")

A new `\core\attribute\deprecated` attribute, and related `\core\deprecation` class have been introduced to provide a standardised way to emit deprecation notices.

The attribute can be applied to:

- classes, traits, interfaces, and enums
- enum cases
- global functions
- class constants, properties, and methods

The attribute can be used to specify information including:

- the version that a feature was deprecated
- the relevant MDL
- the reason for deprecation
- any replacement
- whether the deprecation is final

The `\core\deprecation` class contains helper methods to inspect for use of the deprecated attribute and allows usage including:

- checking if a feature is deprecated
- emitting a deprecation notice if a feature is deprecated

Examples of usage

```
// A method which has been initially deprecated and should show debugging.
/** @deprecated since 4.3 */
#[\core\attribute\deprecated(replacement:'random_bytes',since:'4.3')]
functionrandom_bytes_emulate($length){
\core\deprecation::emit_deprecation_if_present(__FUNCTION__);
returnrandom_bytes($length);
}

// A method which has been finally deprecated and should throw an exception.
/** @deprecated since 2.7 */
#[\core\attribute\deprecated(replacement:'Events API',since:'2.3',final:true)]
functionadd_to_log(){
\core\deprecation::emit_deprecation_if_present(__FUNCTION__);
}

// Checking when an enum case is deprecated:
\core\deprecation::is_deprecated(\core\param::RAW);// Returns false.
\core\deprecation::is_deprecated(\core\param::INTEGER);// Returns true.

// Checking if a class is deprecated:
\core\deprecation::is_deprecated(\core\task\manager::class);// Returns false.

// Checking if an instantiated class is deprecated:
\core\deprecation::is_deprecated(new\moodle_url('/example/'));

// Checking if a class method is deprecated:
\core\deprecation::is_deprecated([\moodle_url::class,'out']);
\core\deprecation::is_deprecated([new\moodle_url('/example/'),'out']);
```

This functionality is intended to simplify deprecation of features such as constants, enums, and related items which are called from centralised APIs and difficult to detect as deprecated.

This functionality does not replace the phpdoc `@deprecated` docblock.

### Clock interface[​](#clock-interface "Direct link to Clock interface")

Moodle now supports use of a PSR-20 compliant Clock Interface, accessed via Dependency Injection.

See the [detailed documentation](https://moodledev.io/docs/4.4/apis/core/clock) on how to use this new interface.

## Enrolment[​](#enrolment "Direct link to Enrolment")

### Meta enrolment support in CSV course upload[​](#meta-enrolment-support-in-csv-course-upload "Direct link to Meta enrolment support in CSV course upload")

It is now possible to use meta enrolment when uploading courses using CSV file. Here is an example of CSV file that can be used to upload a course with meta enrolment:

Example of CSV for meta enrolment

```
shortname,fullname,category_idnumber,enrolment_1,enrolment_1_metacoursename
course1,Course 1,CAT1,meta,course2
```

### Support for multiple instances in csv course upload[​](#support-for-multiple-instances-in-csv-course-upload "Direct link to Support for multiple instances in csv course upload")

It is now possible to upload a CSV file with multiple enrol instances of the same type in same course. This is useful for example when you want to enrol users in a course using two different cohorts.

To support this, a new method has been added to allow the UI to locate existing enrolment instances:

```
/**
 * Finds matching instances for a given course.
 *
 * @param array $enrolmentdata enrolment data.
 * @param int $courseid Course ID.
 * @return stdClass|null Matching instance
 */
publicfunctionfind_instance(
array$enrolmentdata,
int$courseid,
):?stdClass;
```

If your enrolment plugins supports multiple instances within the same course, you should implement [this method](https://moodledev.io/docs/4.4/apis/plugintypes/enrol#enrol_pluginfind_instance-stdclass).

Format of the CSV file

Each line of the CSV should only have data for *one* enrolment instance.

best-example.csv

```
shortname,fullname,category_idnumber,enrolment_1,enrolment_1_role,enrolment_1_cohortidnumber
C1,Course 1,CAT1,cohort,student,CV1
C1,Course 1,CAT1,cohort,teacher,CV4
```

warning

If a single line format is used, only the *final* enrolment instance will be updated. For example in the following example only the second enrolment instance will be updated:

not-recommended-example.csv

```
shortname,fullname,category,summary,enrolment_1,enrolment_1_role,enrolment_2,enrolment_2_role
shortname,fullname,category,summary,cohort,student,cohort,teacher
```

## Refactoring BS4 features dropped in BS5[​](#refactoring-bs4-features-dropped-in-bs5 "Direct link to Refactoring BS4 features dropped in BS5")

Some of the Bootstrap 4 classes will be deprecated or dropped in its version 5. To prepare for this, some of the current Bootstrap 4 classes usages have been replaced with version 5 compatible classes. This will help us to upgrade to Bootstrap 5 in the future.

See more information in [Bootstrap 5 migration](https://moodledev.io/docs/4.4/guides/bs5migration).

## New course section page[​](#new-course-section-page "Direct link to New course section page")

The new course/section.php page is designed exclusively for displaying individual section content. It only requires `sectionid`, eliminating the need for the legacy `sectionnumber`.

Enhancements to this page:

- The General section will no longer appear above the selected section, ensuring a focused display of content for the specified section id.
- Regardless of the Course layout ("All sections on one page" vs "One section per page"), all section names in the main course page content will now link to the new page (excluding editing mode).
- The `$CFG->linkcoursesections` setting has been entirely removed. Initially used for the Classic theme to empower admins in deciding whether section names in the Navigation block should be linked, this setting is now obsolete. With the introduction of the course/section.php page, dedicated to displaying content for any single section, and a convenient link from the main course page, users can seamlessly focus on section content without the need for this setting.
- The methods `core_courseformat\base::set_section_number()` and `core_courseformat\base::get_section_number()` have been deprecated and replaced by `core_courseformat\base::set_sectionnum()` and `core_courseformat\base::get_sectionnum()`. The new methods use the null value when all the sections must be displayed (instead of 0). That way, section 0 (General), can be displayed on a single page too.

## Activity icons[​](#activity-icons "Direct link to Activity icons")

### New designs[​](#new-designs "Direct link to New designs")

The activity icons have been updated to prioritize readability and transform the existing filled square shapes with white icons into outlined colored icons against a transparent background. This modification ensures that the icons are not only more accessible but also easily distinguishable for users. When upgrading the SVG files, the .png files have been removed.

Considerations for creating/updating SVG icons

- Please make sure that the icons are filled with `#212529` and that the background is transparent.
- The icons should be 24x24px. It's recommended to define width and height into the SVG files to guarantee that the icons are displayed correctly.

![New activity icons](https://moodledev.io/assets/images/activity-icons-d6ebc5a5be4e1ed6641e13a561f15aa9.png)

### Activity purposes[​](#activity-purposes "Direct link to Activity purposes")

Since Moodle 4.0, in places like the course page and the activity chooser icons have a more prominent role which is defined using the `FEATURE_MOD_PURPOSE` feature flag.

The available activity purposes for this feature are:

- Administration (`MOD_PURPOSE_ADMINISTRATION`)
- Assessment (`MOD_PURPOSE_ASSESSMENT`)
- Collaboration (`MOD_PURPOSE_COLLABORATION`)
- Communication (`MOD_PURPOSE_COMMUNICATION`)
- Interactive content (`MOD_PURPOSE_INTERACTIVECONTENT`)
- Resource (`MOD_PURPOSE_CONTENT`)
- Other (`MOD_PURPOSE_OTHER`)

Changes in purposes for Moodle 4.4

- `MOD_PURPOSE_INTERFACE` has been deprecated, so it's not recommended to use it.
- `MOD_PURPOSE_INTERACTIVECONTENT` has been added. In core, it's used for activities like H5P, Lesson, SCORM and IMS package.

### Branded icons[​](#branded-icons "Direct link to Branded icons")

A new callback, `<modname>_is_branded()` has been added to the modules. Branded icons are displayed with their original colours and they are not affected by the activity purpose colours. By default, none of the modules are branded.

```
/**
 * Whether the activity is branded.
 * This information is used, for instance, to decide if a filter should be applied to the icon or not.
 *
 * @return bool True if the activity is branded, false otherwise.
 */
functionh5pactivity_is_branded():bool{
returntrue;
}
```

## PHPUnit 9.6 update[​](#phpunit-96-update "Direct link to PHPUnit 9.6 update")

### Intention[​](#intention "Direct link to Intention")

The main goal of this minor update, from **PHPUnit 9.5 to 9.6**, is to start informing to developers in advance about the functionality that has been deprecated in the 9.x series and will be removed completely with the next PHPUnit 10.x update.

### Deprecated stuff[​](#deprecated-stuff "Direct link to Deprecated stuff")

Here you can find all the functionality that has been deprecated in PHPUnit 9.x and needs to be fixed, converted or removed in order to allow the tests to continue working once Moodle gets upgraded to PHPUnit 10.x:

- A number of attribute-related assertions have been deprecated, will be removed with PHPUnit 10. Alternatives for *some* of them are available (Ref. [MDL-81281](https://moodle.atlassian.net/browse/MDL-81281)):
  
  - `assertClassHasAttribute()`
  - `assertClassNotHasAttribute()`
  - `assertClassHasStaticAttribute()`
  - `assertClassNotHasStaticAttribute()`
  - `assertObjectHasAttribute()` =&gt; `assertObjectHasProperty()`
  - `assertObjectNotHasAttribute()` =&gt; `assertObjectNotHasProperty()`
- A number of deprecation, notice, warning and error expectations have been deprecated, will be removed with PHPUnit 10. No alternative exists. A working replacement is available in the linked issue, hopefully there aren't many cases (Ref. [MDL-81266](https://moodle.atlassian.net/browse/MDL-81266)):
  
  - `expectDeprecation()`
  - `expectDeprecationMessage()`
  - `expectDeprecationMessageMatches()`
  - `expectError()`
  - `expectErrorMessage()`
  - `expectErrorMessageMatches()`
  - `expectNotice()`
  - `expectNoticeMessage()`
  - `expectNoticeMessageMatches()`
  - `expectWarning()`
  - `expectWarningMessage()`
  - `expectWarningMessageMatches()`
- The `->withConsecutive()` functionality on PHPUnit mocks has been **silently** deprecated, will be removed with PHPUnit 10. Note that this won't affect PHPUnit 9.6 runs and an alternative path will be proposed in the linked issue, part of the PHPUnit 10 epic (Ref. [MDL-81308](https://moodle.atlassian.net/browse/MDL-81308)).
- `PHPUnit\Framework\TestCase::getMockClass()` has been deprecated, will be removed with PHPUnit 10. No clear alternative exists and won't be investigated, because there aren't cases in core.
- Cannot use the `Test` suffix on abstract test case classes anymore. Proceed to rename them to end with `TestCase` instead.

The list of plugins which are shipped with Moodle core is now available in a JSON format and located at `/lib/plugins.json`.

The schema for this format can be found at `/lib/plugins.schema.json`.

See [Developer metadata](https://moodledev.io/general/development/tools/metadata) for more information on available metadata.

## Previous versions[​](#previous-versions "Direct link to Previous versions")

- [Moodle 4.3 developer update](https://681863b064dd25000810c5f2--moodledevdocs.netlify.app/docs/4.3/devupdate)
- [Moodle 4.2 developer update](https://672834180938720008adb671--moodledevdocs.netlify.app/docs/4.2/devupdate)
- [Moodle 4.1&4.0 developer update](https://moodledev.io/docs/4.1/devupdate)