---
title: Frankenstyle component names | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/codingstyle/frankenstyle
source: sitemap
fetched_at: 2026-02-17T15:59:01.535981-03:00
rendered_js: false
word_count: 670
summary: This document defines the Frankenstyle naming convention used in Moodle to uniquely identify plugins and core subsystems across code, files, and databases.
tags:
    - moodle-development
    - frankenstyle-naming
    - plugin-development
    - naming-conventions
    - core-subsystems
    - coding-standards
category: concept
---

The term 'Frankenstyle component names' refers to the naming convention that is used to uniquely identify a Moodle plugin based on the type of plugin and its name. They are used throughout the Moodle code (with a notable exception being the css class names in the themes).

## Format[​](#format "Direct link to Format")

Frankenstyle component names have a prefix and then a folder name, separated by an underscore.

1. The prefix is determined by the type of plugin. For example, the prefix for an activity module is **mod**.
2. The name is the folder name of the plugin, always lower case. For example, the name for Quiz is **quiz**.

So the frankenstyle component name for the quiz module is **mod\_quiz**.

## Plugin types[​](#plugin-types "Direct link to Plugin types")

See [Plugin types](https://moodledev.io/docs/5.2/apis/plugintypes) page for the list of all supported plugin types in Moodle and their frankenstyle prefix.

To get a definitive list in your version of Moodle 2.x, use a small Moodle script with `print_object(get_plugin_types());`.

## Core subsystems[​](#core-subsystems "Direct link to Core subsystems")

Subsystems in Moodle are not plugins themselves but can be referred to using **core\_\[subsystem.]** where the subsystem defined in get\_core\_subsystems().

Other places that you may see these being used include:

- the PHP Namespace used to autoload classes
- the prefix used in JavaScript module names
- the prefix used in template names
- the `@package` parameter in phpdocs
- the [webservice function names](https://docs.moodle.org/dev/Web_services_Roadmap)

Core subsystems can provide own strings via a file stored in `lang/en/{subsystemname}.php`. Some of them have a dedicated location with libraries, autoloaded classes and other resources.

Core subsystemFrankenstyle component nameLocationAccesscore\_accessAdministrationcore\_admin/adminAntiviruscore\_antivirus/lib/antivirusAuthenticationcore\_auth/authConditional availabilitycore\_availability/availabilityBackup and restorecore\_backup/backup/util/uiBadgescore\_badges/badgesBlockscore\_block/blocksBloggingcore\_blog/blogBulk users operationscore\_bulkusersCachingcore\_cache/cacheCalendarcore\_calendar/calendarCohortscore\_cohort/cohortCommentcore\_comment/commentCompetency based educationcore\_competency/competencyCompletioncore\_completion/completionCountriescore\_countriesCoursecore\_course/courseCurrenciescore\_currenciesDatabase transfercore\_dbtransferDebuggingcore\_debugText editorscore\_editor/lib/editorEducation fieldscore\_edufieldsEnrolcore\_enrol/enrolError reportingcore\_errorFavouritescore\_favourites/favouritesFile pickercore\_filepickerFiles managementcore\_files/filesUser filteringcore\_filtersFormscore\_form/lib/formGradescore\_grades/gradeAdvanced gradingcore\_grading/grade/gradingGroupscore\_group/groupHelpcore\_helpHubcore\_hubIMS CCcore\_imsccInstallercore\_installISO 6392core\_iso6392Language pack configurationcore\_langconfigLicensecore\_licenseMaths librarycore\_mathslibMediacore\_mediaMessagingcore\_message/messageMIME typescore\_mimetypesMNetcore\_mnet/mnetDashboardcore\_my/myUser notescore\_notes/notesPage typescore\_pagetypePictures and iconscore\_pixPlagiarismcore\_plagiarism/plagiarismPlugins managementcore\_pluginPortfoliocore\_portfolio/portfolioPrivacycore\_privacy/privacyCourse publishingcore\_publish/course/publishQuestion bank enginecore\_question/questionRatingscore\_rating/ratingSite registrationcore\_register/admin/registrationRepositorycore\_repository/repositoryRSScore\_rss/rssRolescore\_role/admin/rolesGlobal searchcore\_search/searchTabular data display/download (deprecated)core\_tableTaggingcore\_tag/tagTimezonescore\_timezonesUsercore\_user/userUser keycore\_userkeyWeb servicecore\_webservice/webservice

## Usage[​](#usage "Direct link to Usage")

Frankenstyle component names are used in:

### Function names[​](#function-names "Direct link to Function names")

All plugin functions must start with full frankenstyle prefix.

Activity modules

For backwards compatibility modules may also use `modulename_` as prefix.

warning

Something about global functions not being recommended. Please use an autoloaded class.

### Class names[​](#class-names "Direct link to Class names")

All the component classes must be placed under the classes directory, which allows them to be ([auto-loaded](https://docs.moodle.org/dev/Automatic_class_loading)). These should be placed in a namespace according to their frankenstyle component name, and having a natural name, for example a discussion class in the forum activity should be in the `mod_forum` namespace and may have a class name of `dicussion` - `\mod_forum\discussion`.

Non-namespaced classes

The use of non-namespaced classes using only the frankenstyle prefix is now deprecated.

See [Coding style](https://moodledev.io/general/development/policies/codingstyle#namespaces) for more information.

For example, the class. name `mod_forum_example` should be written as `mod_forum\example`.

### Constants[​](#constants "Direct link to Constants")

All plugin constants must start with uppercase frankenstyle prefix, for example `MOD_FORUM_XXXX`.

note

The use of constants is not recommended and, where possible, a class constant on an autoloaded class should be used.

This allows uses of the constant to autoload the content without needing to manually require any files.

### Table names[​](#table-names "Direct link to Table names")

All table names for a plugin must begin with its frankenstyle name (after the standard Moodle table prefix).

warning

The exception to this rule is Moodle activities which (for historical reasons) do not have plugin type `mod_` as a prefix to the plugin name.

Examples:

- `local_coolreport`
- `local_coolreport_users`
- `forum` - for the mod\_forum component

### Plugin configuration table[​](#plugin-configuration-table "Direct link to Plugin configuration table")

In the **config\_plugins** table, column **plugin**, the frankenstyle name is used.

### Capabilities[​](#capabilities "Direct link to Capabilities")

All capabilities for a plugin use the frankenstyle name, except with a / instead of a \_.

For example:

- `mod/quiz:viewattempt`
- `block/library:readbook`

### Language files[​](#language-files "Direct link to Language files")

The main language file for each plugin (with the notable exception of activity modules) is the frankenstyle component name.

For example:

- `/blocks/participants/lang/en/block_participants.php`
- `/mod/quiz/lang/en/quiz.php`

### Renderers[​](#renderers "Direct link to Renderers")

### Module Subplugins[​](#module-subplugins "Direct link to Module Subplugins")

It is possible to extend modules without having to change the basic module's code. See [Subplugins](https://docs.moodle.org/dev/Subplugins) for details.

### Other places (TODO)[​](#other-places-todo "Direct link to Other places (TODO)")

- @package declarations in phpdocs, see [Coding style#PHPDoc](https://moodledev.io/general/development/policies/codingstyle#phpdoc)
- [web service function names](https://docs.moodle.org/dev/Web_services_Roadmap)
- [Moodle Plugins database](http://moodle.org)
- JS module names
- Template names

Please add more as they come up.

## Theme name variants[​](#theme-name-variants "Direct link to Theme name variants")

Themes are typically a derivatives of some other theme. Where this is the case, you should *avoid* including the parent theme name in your theme's name.

## See also[​](#see-also "Direct link to See also")

- [Plugins](https://docs.moodle.org/dev/Plugins)
- [Subplugins](https://docs.moodle.org/dev/Subplugins)
- [Core APIs](https://moodledev.io/docs/5.2/apis)
- [Automatic class loading](https://docs.moodle.org/dev/Automatic_class_loading)