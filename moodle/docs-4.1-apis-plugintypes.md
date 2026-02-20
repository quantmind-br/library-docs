---
title: Plugin types | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/plugintypes
source: sitemap
fetched_at: 2026-02-17T14:55:02.380677-03:00
rendered_js: false
word_count: 892
summary: This document provides an overview of the Moodle plugin system, including mandatory naming conventions, common file structures, and a comprehensive reference list of available plugin types.
tags:
    - moodle-development
    - plugin-architecture
    - frankenstyle
    - naming-conventions
    - moodle-plugins
category: reference
---

Moodle is a powerful, and very extensible, Learning Management System. One of its core tenets is its extensibility, and this is primarily achieved through the development of plugins.

A wider range of plugin types are available and these should be selected depending on your needs.

## Things you can find in all plugins[​](#things-you-can-find-in-all-plugins "Direct link to Things you can find in all plugins")

Although there are many different types of plugin, there are some things that work the same way in all plugin types. Please see the [Plugin files](https://moodledev.io/docs/4.1/apis/commonfiles) documentation that describes common files which are found in many plugin types.

## Naming conventions[​](#naming-conventions "Direct link to Naming conventions")

Plugins typically have at least two names:

- The friendly name, shown to users, and
- A machine name used internally.

The machine name must meet the following rules:

- It must start with a lowercase latin letter
- It may contain only lowercase latin letters, numbers, and underscores
- It must end with a lowercase latin letter, or a number
- The hyphen, and minus character `-` are not allowed

If a plugin does not meet these requirements then it will be silently ignored.

tip

Plugin name validation takes place in `core_component::is_valid_plugin_name()` and the following regular expression is used:

```
/^[a-z](?:[a-z0-9_](?!__))*[a-z0-9]+$/
```

Activity module exception

The underscore character is not supported in activity modules for legacy reasons.

Plugin typeComponent name ([Frankenstyle](https://moodledev.io/general/development/policies/codingstyle/frankenstyle))Moodle pathDescriptionMoodle versions[Activity modules](https://moodledev.io/docs/4.1/apis/plugintypes/mod)mod/modActivity modules are essential types of plugins in Moodle as they provide activities in courses. For example: Forum, Quiz and Assignment.1.0+[Antivirus plugins](https://moodledev.io/docs/4.1/apis/plugintypes/antivirus)antivirus/lib/antivirusAntivirus scanner plugins provide functionality for virus scanning user uploaded files using third-party virus scanning tools in Moodle. For example: ClamAV.3.1+[Assignment submission plugins](https://moodledev.io/docs/4.1/apis/plugintypes/assign/submission)assignsubmission/mod/assign/submissionDifferent forms of assignment submissions2.3+[Assignment feedback plugins](https://moodledev.io/docs/4.1/apis/plugintypes/assign/feedback)assignfeedback/mod/assign/feedbackDifferent forms of assignment feedbacks2.3+[Book tools](https://moodledev.io/docs/4.1/apis/plugintypes/mod_book)booktool/mod/book/toolSmall information-displays or tools that can be moved around pages2.1+[Course Custom fields](https://moodledev.io/docs/4.1/apis/plugintypes/customfield)customfield/customfield/fieldCustom field types, used in Custom course fields3.7+[Database fields](https://moodledev.io/docs/4.1/apis/plugintypes/mod_data/fields)datafield/mod/data/fieldDifferent types of data that may be added to the Database activity module1.6+[Database presets](https://moodledev.io/docs/4.1/apis/plugintypes/mod_data/presets)datapreset/mod/data/presetPre-defined templates for the Database activity module1.6+[LTI sources](https://docs.moodle.org/dev/External_tool_source)ltisource/mod/lti/sourceLTI providers can be added to external tools easily through the external tools interface see [Documentation on External Tools](https://docs.moodle.org/en/External_tool). This type of plugin is specific to LTI providers that need a plugin that can register custom handlers to process LTI messages2.7+[File Converters](https://moodledev.io/docs/4.1/apis/plugintypes/fileconverter)fileconverter/files/converterAllow conversion between different types of user-submitted file. For example from .doc to PDF.3.2+[LTI services](https://docs.moodle.org/dev/LTI_services)ltiservice/mod/lti/serviceAllows the implementation of LTI services as described by the IMS LTI specification2.8+[Machine learning backends](https://moodledev.io/docs/4.1/apis/plugintypes/mlbackend)mlbackend/lib/mlbackendPrediction processors for analytics API3.4+[Forum reports](https://moodledev.io/docs/4.1/apis/plugintypes/mod_forum)forumreport/mod/forum/reportDisplay various reports in the forum activity3.8+[Quiz reports](https://docs.moodle.org/dev/Quiz_reports)quiz/mod/quiz/reportDisplay and analyse the results of quizzes, or just plug miscellaneous behaviour into the quiz module1.1+[Quiz access rules](https://docs.moodle.org/dev/Quiz_access_rules)quizaccess/mod/quiz/accessruleAdd conditions to when or where quizzes can be attempted, for example only from some IP addresses, or student must enter a password first2.2+[SCORM reports](https://docs.moodle.org/dev/SCORM_reports)scormreport/mod/scorm/reportAnalysis of SCORM attempts2.2+[Workshop grading strategies](https://docs.moodle.org/dev/Workshop_grading_strategies)workshopform/mod/workshop/formDefine the type of the grading form and implement the calculation of the grade for submission in the [Workshop](https://docs.moodle.org/dev/Workshop) module2.0+[Workshop allocation methods](https://docs.moodle.org/dev/Workshop_allocation_methods)workshopallocation/mod/workshop/allocationDefine ways how submissions are assigned for assessment in the [Workshop](https://docs.moodle.org/dev/Workshop) module2.0+[Workshop evaluation methods](https://docs.moodle.org/dev/Workshop_evaluation_methods)workshopeval/mod/workshop/evalImplement the calculation of the grade for assessment (grading grade) in the [Workshop](https://docs.moodle.org/dev/Workshop) module2.0+[Blocks](https://moodledev.io/docs/4.1/apis/plugintypes/blocks)block/blocksSmall information-displays or tools that can be moved around pages2.0+[Question types](https://docs.moodle.org/dev/Question_types)qtype/question/typeDifferent types of question (for example multiple-choice, drag-and-drop) that can be used in quizzes and other activities1.6+[Question behaviours](https://docs.moodle.org/dev/Question_behaviours)qbehaviour/question/behaviourControl how student interact with questions during an attempt2.1+[Question import/export formats](https://docs.moodle.org/dev/Question_formats)qformat/question/formatImport and export question definitions to/from the question bank1.6+[Text filters](https://moodledev.io/docs/4.1/apis/plugintypes/filter)filter/filterAutomatically convert, highlight, and transmogrify text posted into Moodle.1.4+[Editors](https://moodledev.io/docs/4.1/apis/subsystems/editor)editor/lib/editorAlternative text editors for editing content2.0+[Atto editor plugins](https://moodledev.io/docs/4.1/apis/plugintypes/atto)atto/lib/editor/atto/pluginsExtra functionality for the Atto text editor2.7+[TinyMCE editor plugins](https://moodledev.io/docs/4.1/apis/plugintypes/tiny/legacy)tinymce/lib/editor/tinymce/pluginsExtra functionality for the TinyMCE text editor.2.4+[Enrolment plugins](https://moodledev.io/docs/4.1/apis/plugintypes/enrol)enrol/enrolWays to control who is enrolled in courses2.0+[Authentication plugins](https://docs.moodle.org/dev/Authentication_plugins)auth/authAllows connection to external sources of authentication2.0+[Admin tools](https://moodledev.io/general/projects/api/admin-tools)tool/admin/toolProvides utility scripts useful for various site administration and maintenance tasks2.2+[Log stores](https://moodledev.io/docs/4.1/apis/plugintypes/logstore)logstore/admin/tool/log/storeEvent logs storage back-ends2.7+[Availability conditions](https://moodledev.io/docs/4.1/apis/plugintypes/availability)availability/availability/conditionConditions to restrict user access to activities and sections.2.7+[Calendar types](https://docs.moodle.org/dev/Calendar_types)calendartype/calendar/typeDefines how dates are displayed throughout Moodle2.6+[Messaging consumers](https://docs.moodle.org/dev/Messaging_consumers)message/message/outputRepresent various targets where messages and notifications can be sent to (email, sms, jabber, ...)2.0+[Course formats](https://moodledev.io/docs/4.1/apis/plugintypes/format)format/course/formatDifferent ways of laying out the activities and blocks in a course1.3+[Data formats](https://docs.moodle.org/dev/Data_formats)dataformat/dataformatFormats for data exporting and downloading3.1+[User profile fields](https://docs.moodle.org/dev/User_profile_fields)profilefield/user/profile/fieldAdd new types of data to user profiles1.9+[Reports](https://docs.moodle.org/dev/Reports)report/reportProvides useful views of data in a Moodle site for admins and teachers2.2+[Course reports](https://docs.moodle.org/dev/Course_reports)coursereport/course/reportReports of activity within the courseUp to 2.1 (for 2.2+ see [Reports](https://docs.moodle.org/dev/Reports))[Gradebook export](https://docs.moodle.org/dev/Gradebook_export)gradeexport/grade/exportExport grades in various formats1.9+[Gradebook import](https://docs.moodle.org/dev/Gradebook_import)gradeimport/grade/importImport grades in various formats1.9+[Gradebook reports](https://docs.moodle.org/dev/Gradebook_reports)gradereport/grade/reportDisplay/edit grades in various layouts and reports1.9+[Advanced grading methods](https://docs.moodle.org/dev/Grading_methods)gradingform/grade/grading/formInterfaces for actually performing grading in activity modules (for example Rubrics)2.2+[MNet services](https://docs.moodle.org/dev/MNet_services)mnetservice/mnet/serviceAllows to implement remote services for the [MNet](https://docs.moodle.org/dev/MNet) environment (deprecated, use web services instead)2.0+[Webservice protocols](https://docs.moodle.org/dev/Webservice_protocols)webservice/webserviceDefine new protocols for web service communication (such as SOAP, XML-RPC, JSON, REST ...)2.0+[Repository plugins](https://moodledev.io/docs/4.1/apis/plugintypes/repository)repository/repositoryConnect to external sources of files to use in Moodle2.0+[Portfolio plugins](https://docs.moodle.org/dev/Portfolio_plugins)portfolio/portfolioConnect external portfolio services as destinations for users to store Moodle content1.9+[Search engines](https://docs.moodle.org/dev/Search_engines)search/search/engineSearch engine backends to index Moodle's contents.3.1+[Media players](https://docs.moodle.org/dev/Media_players)media/media/playerPluggable media players3.2+[Plagiarism plugins](https://docs.moodle.org/dev/Plagiarism_plugins)plagiarism/plagiarismDefine external services to process submitted files and content2.0+[Cache store](https://docs.moodle.org/dev/Cache_store)cachestore/cache/storesCache storage back-ends.2.4+[Cache locks](https://docs.moodle.org/dev/Cache_locks)cachelock/cache/locksCache lock implementations.2.4+[Themes](https://docs.moodle.org/dev/Themes)theme/themeChange the look of Moodle by changing the the HTML and the CSS.2.0+[Local plugins](https://moodledev.io/docs/4.1/apis/plugintypes/local)local/localGeneric plugins for local customisations2.0+[Content bank content types](https://docs.moodle.org/dev/Content_bank_content_types)contenttype/contentbank/contenttypeContent types to upload, create or edit in the content bank and use all over the Moodle site3.9+[H5P libraries](https://docs.moodle.org/dev/H5P_libraries)h5plib/h5p/h5plibPlugin type for the particular versions of the H5P integration library.3.9+[Question bank plugins](https://moodledev.io/docs/4.1/apis/plugintypes/qbank)qbank/question/bankPlugin type for extending question bank functionality.4.0+

Obtaining the list of plugin types known to your Moodle

You can get an exact list of valid plugin types for your Moodle version using the following example:

/plugintypes.php

```
<?php
define('CLI_SCRIPT',true);
require('config.php');

$pluginman=core_plugin_manager::instance();

foreach($pluginman->get_plugin_types()as$type=>$dir){
$dir=substr($dir,strlen($CFG->dirroot));
printf(
"%-20s %-50s %s".PHP_EOL,
$type,
$pluginman->plugintype_name_plural($type),
$dir)
;
}
```

## See also[​](#see-also "Direct link to See also")

- [Guidelines for contributing code](https://docs.moodle.org/dev/Guidelines_for_contributed_code)
- [Core APIs](https://moodledev.io/docs/4.1/apis)
- [Frankenstyle](https://moodledev.io/general/development/policies/codingstyle/frankenstyle)
- [Moodle Plugins directory](http://moodle.org/plugins)
- [Tutorial](https://docs.moodle.org/dev/Tutorial) to help you learn how to write plugins for Moodle from start to finish, while showing you how to navigate the most important developer documentation along the way.