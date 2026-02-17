---
title: Moodle 3.3 | Moodle Developer Resources
url: https://moodledev.io/general/releases/3.3
source: sitemap
fetched_at: 2026-02-17T16:11:20.569115-03:00
rendered_js: false
word_count: 1525
summary: This document provides the release notes for Moodle 3.3, detailing the server requirements, browser compatibility, and major feature updates for teachers and administrators. It serves as a technical reference for system requirements and functional changes introduced in this version.
tags:
    - moodle-3-3
    - release-notes
    - system-requirements
    - server-configuration
    - software-update
    - database-compatibility
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 15 May 2017

Here is [the full list of fixed issues in 3.3](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%223.3%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

See our [New Features page](https://docs.moodle.org/33/en/New_features) for a more user-friendly introduction to Moodle 3.3 with screenshots.

If you are upgrading from previous version, make sure you read the [Upgrading](https://docs.moodle.org/33/en/Upgrading) documentation.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software up-to-date.

- Moodle upgrade: Moodle 2.7 or later (if upgrading from earlier versions, you must upgrade to 2.7.14 as a first step)
- PHP version: minimum PHP 5.6.5. *Note: minimum PHP version has increased since Moodle 3.1*. PHP 7.0.x and 7.1.x are supported but have some [engine limitations](https://docs.moodle.org/dev/Moodle_and_PHP7#Can_I_use_PHP7_yet.3F).
- PHP extensions **openssl** and **fileinfo** are now required in Moodle 3.3 (they were recommended in 3.2)
- If you use PostgreSQL the minimum supported version is now 9.3 (was 9.1 in Moodle 3.2)
- (Recommendation only) If you use MySQL or MariaDB, make sure your database supports full UTF-8 (utf8mb4) if you install a new instance of Moodle. CLI script may be used to convert to utf8mb4 if you're upgrading. You may choose to keep using 'utf8\_\*', but then a warning will show that the database isn't using full UTF-8 support and suggest moving to 'utf8mb4\_unicode\_ci'. See [MySQL full unicode support](https://docs.moodle.org/en/MySQL_full_unicode_support) for details.

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)9.3Latest[MySQL](http://www.mysql.com/)5.5.31Latest[MariaDB](https://mariadb.org/)5.5.31Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2008Latest[Oracle Database](http://www.oracle.com/us/products/database/overview/index.html)10.2Latest

## Client requirements[​](#client-requirements "Direct link to Client requirements")

### Browser support[​](#browser-support "Direct link to Browser support")

Moodle is compatible with any standards compliant web browser. We regularly test Moodle with the following browsers:

Desktop:

- Chrome
- Firefox
- Safari
- Edge
- Internet Explorer

Mobile:

- MobileSafari
- Google Chrome

For the best experience and optimum security, we recommend that you keep your browser up to date. [https://whatbrowser.org](https://whatbrowser.org)

Note: Legacy browsers with known compatibility issues with Moodle 3.3:

- Internet Explorer 10 and below
- Safari 7 and below

## Major features[​](#major-features "Direct link to Major features")

### Highlights[​](#highlights "Direct link to Highlights")

- [MDL-55611](https://moodle.atlassian.net/browse/MDL-55611) - New [Course overview](https://docs.moodle.org/33/en/Course_overview) dashboard block featuring timeline of events
- [MDL-58220](https://moodle.atlassian.net/browse/MDL-58220) - Make use of [OAuth 2 services](https://docs.moodle.org/33/en/OAuth_2_services) to allow users to [authenticate with Google G-Suite or Microsoft Office accounts](https://docs.moodle.org/33/en/OAuth_2_authentication) and manage files from associated drives
- [MDL-39913](https://moodle.atlassian.net/browse/MDL-39913) - New [Assignment setting](https://docs.moodle.org/33/en/Assignment_settings) for restricting submission file types
- [MDL-4782](https://moodle.atlassian.net/browse/MDL-4782) - ["Stealth mode"](https://docs.moodle.org/33/en/Stealth_activities) for resources/activities in a course - not displayed on the course page but available for students
- [MDL-40759](https://moodle.atlassian.net/browse/MDL-40759) - New Font Awesome icon font for all icons in Moodle

### For teachers[​](#for-teachers "Direct link to For teachers")

- [MDL-58138](https://moodle.atlassian.net/browse/MDL-58138) - [Activity completion settings](https://docs.moodle.org/33/en/Activity_completion_settings) for setting activity completion defaults and bulk editing of completion requirements
- [MDL-48771](https://moodle.atlassian.net/browse/MDL-48771) - [Quiz activity](https://docs.moodle.org/33/en/Building_Quiz): Option to delete multiple questions
- [MDL-53814](https://moodle.atlassian.net/browse/MDL-53814) - Quiz activity: Question type icons are displayed in the quiz manual grading overview
- [MDL-55459](https://moodle.atlassian.net/browse/MDL-55459) - [Assignment activity](https://docs.moodle.org/33/en/Assignment_settings): Annotated PDF comments are collapsible
- [MDL-23919](https://moodle.atlassian.net/browse/MDL-23919) - [Database activity](https://docs.moodle.org/33/en/Database_activity_settings): The setting "Required entries" is now an activity completion condition
- [MDL-57769](https://moodle.atlassian.net/browse/MDL-57769) - Topic and weeks course formats: After a course is created, sections can be added and removed only from the course page (it is no longer possible to have "orphaned" activities)
- [MDL-46929](https://moodle.atlassian.net/browse/MDL-46929), [MDL-57456](https://moodle.atlassian.net/browse/MDL-57456), [MDL-57457](https://moodle.atlassian.net/browse/MDL-57457) - [Forum posts](https://docs.moodle.org/33/en/Using_Forum), [glossary entries](https://docs.moodle.org/33/en/Using_Glossary) and [book chapters](https://docs.moodle.org/33/en/Book_settings) may be tagged
- [MDL-56251](https://moodle.atlassian.net/browse/MDL-56251) - For courses in weekly format, a new [course setting](https://docs.moodle.org/33/en/Course_settings) allows for the course end date to be calculated automatically
- [MDL-47354](https://moodle.atlassian.net/browse/MDL-47354) - Allow the page size in the Single view report to be configurable

### Backup and restore[​](#backup-and-restore "Direct link to Backup and restore")

- [MDL-34859](https://moodle.atlassian.net/browse/MDL-34859) - Add site defaults for all restore settings, improve UI around "Overwrite course configuration" select
- [MDL-40838](https://moodle.atlassian.net/browse/MDL-40838) - Allow to restore non-default enrollment methods without restoring users
- [MDL-57769](https://moodle.atlassian.net/browse/MDL-57769) - When restoring/importing big courses in Weeks and Topics formats into small existing courses ajust the number of sections automatically

### For administrators[​](#for-administrators "Direct link to For administrators")

Please read carefully: [Possible issues that may affect you in Moodle 3.3](https://docs.moodle.org/33/en/Upgrading#Possible_issues_that_may_affect_you_in_Moodle_3.3)

- [MDL-46375](https://moodle.atlassian.net/browse/MDL-46375) - Support for storing files not on the local drive (there are no open-source solutions at the moment, developer's help is required to implement custom cloud storage)
- [MDL-55528](https://moodle.atlassian.net/browse/MDL-55528), [MDL-58280](https://moodle.atlassian.net/browse/MDL-58280) - New [document converter](https://docs.moodle.org/33/en/Document_converters) plugin type allows alternatives to unoconv, such as the [Google Drive converter](https://docs.moodle.org/33/en/Google_Drive_converter)
- [MDL-55980](https://moodle.atlassian.net/browse/MDL-55980) - Run individual scheduled tasks from web interface
- [MDL-57896](https://moodle.atlassian.net/browse/MDL-57896) - CLI wrapper for get\_config() and set\_config() methods
- [MDL-57789](https://moodle.atlassian.net/browse/MDL-57789) - Use Cache-Control: immutable when serving files
- [MDL-37765](https://moodle.atlassian.net/browse/MDL-37765) - New capability to bypass access restrictions, separated from capability to view hidden activities
- [MDL-57913](https://moodle.atlassian.net/browse/MDL-57913) - Convert external database authentication synchronisation to scheduled task

#### Plugins removal and deprecation[​](#plugins-removal-and-deprecation "Direct link to Plugins removal and deprecation")

- The repository Skydrive is deprecated; please migrate to the newer [OneDrive repository](https://docs.moodle.org/33/en/OneDrive_repository)
- The Dashboard block Course overview is replaced with a new block [Course overview](https://docs.moodle.org/33/en/Course_overview) which is a different plugin. If you want to use the old block, you need to download and install it from [https://moodle.org/plugins/block\_course\_overview](https://moodle.org/plugins/block_course_overview)

### Mobile app support[​](#mobile-app-support "Direct link to Mobile app support")

- [MDL-57410](https://moodle.atlassian.net/browse/MDL-57410) - Allow admins to add new external links to pages in the main menu of the Mobile app
- [MDL-57408](https://moodle.atlassian.net/browse/MDL-57408) - Add new settings for allowing renaming strings in the Mobile app
- [MDL-49423](https://moodle.atlassian.net/browse/MDL-49423) - Add new settings for disabling Mobile app functionalities
- [MDL-57759](https://moodle.atlassian.net/browse/MDL-57759) - Allow offline attempts via the Mobile app in the lesson module
- [MDL-57162](https://moodle.atlassian.net/browse/MDL-57162) - Support Native App install banners for Android as well as iOS for the mobile app

### Other improvements[​](#other-improvements "Direct link to Other improvements")

- [MDL-33483](https://moodle.atlassian.net/browse/MDL-33483) - Google Docs repository: Save Doc files in different formats to RTF
- [MDL-42266](https://moodle.atlassian.net/browse/MDL-42266) - Improve the list of maximum file size options for file uploads
- [MDL-51853](https://moodle.atlassian.net/browse/MDL-51853) - Calendar subscriptions from imported files should be editable
- [MDL-41729](https://moodle.atlassian.net/browse/MDL-41729) - Add ability to change passwords for users using Shibboleth
- [MDL-57572](https://moodle.atlassian.net/browse/MDL-57572), [MDL-57570](https://moodle.atlassian.net/browse/MDL-57570), [MDL-57355](https://moodle.atlassian.net/browse/MDL-57355) - Redis and static caches performance improvements if igbinary library is installed
- [MDL-56808](https://moodle.atlassian.net/browse/MDL-56808) - SCORM module: Performance improvements when running SCORM 1.2 packages
- [MDL-57686](https://moodle.atlassian.net/browse/MDL-57686) - Add support for PDO databases in external database authentication
- [MDL-57638](https://moodle.atlassian.net/browse/MDL-57638) - RSS Block: RSS feeds are more heavily cached and correctly respect skip values

### For developers[​](#for-developers "Direct link to For developers")

- [MDL-55528](https://moodle.atlassian.net/browse/MDL-55528) - New plugin type 'fileconverter' for file conversions, unoconv is now a plugin that can be replaced with scalable commercial solutions (see [File Converters](https://moodledev.io/docs/5.2/apis/plugintypes/fileconverter))
- [MDL-40759](https://moodle.atlassian.net/browse/MDL-40759) - Font Awesome icon font is used for all icons in Moodle (see [Moodle icons](https://docs.moodle.org/dev/Moodle_icons#Font_awesome_icons))
- [MDL-46375](https://moodle.atlassian.net/browse/MDL-46375) - Support for storing files not on the local drive is implemented by allowing to override functionality of file\_storage and stored\_file classes (see [File System API](https://docs.moodle.org/dev/File_System_API))
- [MDL-12689](https://moodle.atlassian.net/browse/MDL-12689) - Convert all authentication plugins to use settings.php (see [upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/auth/upgrade.txt))
- [MDL-53978](https://moodle.atlassian.net/browse/MDL-53978) - Add extra plugin callbacks for every major stage of page render (see [commit](https://github.com/moodle/moodle/commit/5ebd1fb9768969956c9131df4274f9cdff7f0134))
- [MDL-58138](https://moodle.atlassian.net/browse/MDL-58138) - Course modules may provide additional callbacks to participate in bulk editing of activities completion rules in a course
- [MDL-58220](https://moodle.atlassian.net/browse/MDL-58220) - Better office integration
- [MDL-45584](https://moodle.atlassian.net/browse/MDL-45584) - Multiple caches can be instantiated with the same definition but with different identifiers
- [MDL-57769](https://moodle.atlassian.net/browse/MDL-57769) - Course formats: Attribute 'numsections' was removed from topics and weeks, other course formats may want to implement similar changes
- [MDL-55956](https://moodle.atlassian.net/browse/MDL-55956) - Priority field for the calendar events allowing to specify the priority of overrides
- [MDL-58566](https://moodle.atlassian.net/browse/MDL-58566) - New methods for retrieving calendar events
- [MDL-55941](https://moodle.atlassian.net/browse/MDL-55941) - New element to select first name of first/last names is implemented in tablelib or can be used by developers elsewhere ([template](https://github.com/moodle/moodle/blob/v3.3.0/lib/templates/initials_bar.mustache))
- [MDL-56519](https://moodle.atlassian.net/browse/MDL-56519) - Lint behat .feature files
- [MDL-57273](https://moodle.atlassian.net/browse/MDL-57273) - New classes (core\\persistent, core\\form\\persistent, core\\external\\exporter, \\core\\external\\persistent\_exporter) used to represent a data-model and export that data in a standard format for webservices (previously was used in competencies) (see [Persistent form](https://docs.moodle.org/dev/Persistent_form), [Persistent](https://docs.moodle.org/dev/Persistent), [Exporter](https://docs.moodle.org/dev/Exporter))
- [MDL-57490](https://moodle.atlassian.net/browse/MDL-57490) - Removed several legacy JS functions from `javascript-static.js`
- [MDL-57690](https://moodle.atlassian.net/browse/MDL-57690) - mcore YUI rollup is no longer included on every single Moodle page (see [//moodle.org/mod/forum/discuss.php?d=346520 forum post](https://docs.moodle.org/https///moodle.org/mod/forum/discuss.php?d=346520_forum_post))

#### Upgrading plugins[​](#upgrading-plugins "Direct link to Upgrading plugins")

**1. Check for changes in core APIs**

Read lib/upgrade.txt to check for the deprecations and core API changes, make sure you applied them to your plugin. Note that entries there are not sorted by priority but rather by integration time. Below is the list of upgrade.txt files that contain information about upgrading from Moodle 3.2 to Moodle 3.3 (note that if you upgrade from earlier versions there may be more files):

- [lib/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/lib/upgrade.txt) changes to various core APIs, deprecations, functions removal
- [admin/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/admin/upgrade.txt) changes to administration-related functions
- [cache/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/cache/upgrade.txt) changes to Cache API
- [calendar/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/calendar/upgrade.txt) changes to Calendar API
- [competency/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/competency/upgrade.txt) changes to Competency API
- [course/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/course/upgrade.txt) changes to course-related functions

For the next releases we are thinking about improving the format of upgrade.txt notes, please have your say on policy issue [MDL-58879](https://moodle.atlassian.net/browse/MDL-58879)

**2. Check for changes in the API of your plugin type**

Below is the list of plugin types that had API changes between Moodle 3.2 and 3.3:

- [auth/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/auth/upgrade.txt) Authentication plugins
- [blocks/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/blocks/upgrade.txt) Block plugins
- [course/format/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/course/format/upgrade.txt) Course format plugins
- [enrol/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/enrol/upgrade.txt) Enrolment method plugins
- [media/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/media/upgrade.txt) Media player plugins
- [mod/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/mod/upgrade.txt) Activity module plugins
- [question/type/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/question/type/upgrade.txt) Question types plugins
- [repository/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/repository/upgrade.txt) Repository plugins
- [theme/upgrade.txt](https://github.com/moodle/moodle/blob/v3.3.0/theme/upgrade.txt) Themes

**3. Check for changes in the depended plugins**

If your plugin depends on another plugin or calls methods from another plugin, read upgrade.txt in this plugin directory (if it exists). Below is the list of standard plugins that had changes between Moodle 3.2 and 3.3:

Due to changes in Authentication plugins settings all standard auth plugins were updated: [auth\_cas](https://github.com/moodle/moodle/blob/v3.3.0/auth/cas/upgrade.txt), [auth\_db](https://github.com/moodle/moodle/blob/v3.3.0/auth/db/upgrade.txt), [auth\_email](https://github.com/moodle/moodle/blob/v3.3.0/auth/email/upgrade.txt), [auth\_fc](https://github.com/moodle/moodle/blob/v3.3.0/auth/fc/upgrade.txt), [auth\_imap](https://github.com/moodle/moodle/blob/v3.3.0/auth/imap/upgrade.txt), [auth\_ldap](https://github.com/moodle/moodle/blob/v3.3.0/auth/ldap/upgrade.txt), [auth\_manual](https://github.com/moodle/moodle/blob/v3.3.0/auth/manual/upgrade.txt), [auth\_mnet](https://github.com/moodle/moodle/blob/v3.3.0/auth/mnet/upgrade.txt), [auth\_nntp](https://github.com/moodle/moodle/blob/v3.3.0/auth/nntp/upgrade.txt), [auth\_none](https://github.com/moodle/moodle/blob/v3.3.0/auth/none/upgrade.txt), [auth\_pam](https://github.com/moodle/moodle/blob/v3.3.0/auth/pam/upgrade.txt), [auth\_pop3](https://github.com/moodle/moodle/blob/v3.3.0/auth/pop3/upgrade.txt), [auth\_shibboleth](https://github.com/moodle/moodle/blob/v3.3.0/auth/shibboleth/upgrade.txt)

Other standard plugins that were updated in 3.3: [tool\_lp](https://github.com/moodle/moodle/blob/v3.3.0/admin/tool/lp/upgrade.txt), [tool\_mobile](https://github.com/moodle/moodle/blob/v3.3.0/admin/tool/mobile/upgrade.txt), [enrol\_ldap](https://github.com/moodle/moodle/blob/v3.3.0/enrol/ldap/upgrade.txt), [mod\_assign](https://github.com/moodle/moodle/blob/v3.3.0/mod/assign/upgrade.txt), [mod\_data](https://github.com/moodle/moodle/blob/v3.3.0/mod/data/upgrade.txt), [mod\_feedback](https://github.com/moodle/moodle/blob/v3.3.0/mod/feedback/upgrade.txt), [mod\_forum](https://github.com/moodle/moodle/blob/v3.3.0/mod/forum/upgrade.txt), [mod\_lesson](https://github.com/moodle/moodle/blob/v3.3.0/mod/lesson/upgrade.txt)

**4. Do a smoke test of your plugin with developer debugging mode**

**5. Run all behat and phpunit tests**

## Translations[​](#translations "Direct link to Translations")

- [Notes de mise à jour de Moodle 3.3](https://docs.moodle.org/fr/Notes_de_mise_%C3%A0_jour_de_Moodle_3.3)
- [Notas de Moodle 3.3](https://docs.moodle.org/es/Notas_de_Moodle_3.3)