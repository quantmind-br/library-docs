---
title: Moodle 3.6 | Moodle Developer Resources
url: https://moodledev.io/general/releases/3.6
source: sitemap
fetched_at: 2026-02-17T16:12:41.132683-03:00
rendered_js: false
word_count: 1420
summary: This document provides the release notes for Moodle 3.6, outlining system requirements, browser compatibility, and major new features including messaging improvements and GDPR compliance tools.
tags:
    - moodle-3-6
    - release-notes
    - server-requirements
    - database-compatibility
    - gdpr-compliance
    - messaging-features
    - learning-management-system
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 3 December 2018

Here is [the full list of fixed issues in 3.6](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%223.6%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

See our [New features page](https://docs.moodle.org/36/en/New_features) in the user documentation for an introduction to Moodle 3.6 with screenshots.

If you are upgrading from a previous version, please see [Upgrading](https://docs.moodle.org/en/Upgrading) in the user docs. *In particular, for sites using a custom theme or login form, from 3.6 onwards, the login form must include a new login token field. See [Login token](https://docs.moodle.org/dev/Login_token) for details.*

note

You are recommended to use [Moodle 3.6.1](https://moodledev.io/general/releases/3.6/3.6.1), as it includes a messaging regression fix.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software and operating systems up-to-date.

- Moodle upgrade: Moodle 3.1 or later
- PHP version: minimum PHP 7.0.0 *Note: minimum PHP version has increased since Moodle 3.3*. PHP 7.1.x, 7.2.x and 7.3.x (since Moodle 3.6.4) are supported too. See [Moodle and PHP](https://moodledev.io/general/development/policies/php) for details.
- PHP extension **intl** is required since Moodle 3.4 (it was recommended in 2.0 onwards)

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)9.411.x - note that 12.x is not yet supported ([MDL-67414](https://moodle.atlassian.net/browse/MDL-67414))[MySQL](http://www.mysql.com/)5.6Latest[MariaDB](https://mariadb.org/)5.5.31Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2008Latest[Oracle Database](http://www.oracle.com/us/products/database/overview/index.html)11.2Latest

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

For the best experience and optimum security, we recommend that you keep your browser up to date. [https://www.whatismybrowser.com/](https://www.whatismybrowser.com/)

Note: Legacy browsers with known compatibility issues with Moodle 3.6:

- Internet Explorer 10 and below
- Safari 7 and below

## Major features[​](#major-features "Direct link to Major features")

### Dashboard and Course overview[​](#dashboard-and-course-overview "Direct link to Dashboard and Course overview")

- [MDL-63044](https://moodle.atlassian.net/browse/MDL-63044) and [MDL-63337](https://moodle.atlassian.net/browse/MDL-63337) - New [Course overview](https://docs.moodle.org/36/en/Course_overview) and [Timeline block](https://docs.moodle.org/36/en/Timeline_block)
- [MDL-63062](https://moodle.atlassian.net/browse/MDL-63062) - New [Recently accessed courses block](https://docs.moodle.org/36/en/Recently_accessed_courses_block)
- [MDL-63063](https://moodle.atlassian.net/browse/MDL-63063) - New [Recently accessed items block](https://docs.moodle.org/36/en/Recently_accessed_items_block)
- [MDL-63457](https://moodle.atlassian.net/browse/MDL-63457) - Option to hide courses in the course overview block
- [MDL-63058](https://moodle.atlassian.net/browse/MDL-63058) - Option to star/unstar courses in the course overview block
- [MDL-63064](https://moodle.atlassian.net/browse/MDL-63064) - New [Starred courses block](https://docs.moodle.org/36/en/Starred_courses_block)
- [MDL-63352](https://moodle.atlassian.net/browse/MDL-63352) - Dashboard retains user preferences for view options
- [MDL-63793](https://moodle.atlassian.net/browse/MDL-63793) - Course overview block retains user preferences for the number of courses to show
- [MDL-61161](https://moodle.atlassian.net/browse/MDL-61161) - Grace period when displaying "In progress" courses in course overview block
- [MDL-63040](https://moodle.atlassian.net/browse/MDL-63040) - Removal of Dashboard page header

### GDPR and Privacy[​](#gdpr-and-privacy "Direct link to GDPR and Privacy")

Note that some of these GDPR improvements have also been backported to Moodle 3.5.3, 3.4.6 and 3.3.9.

- [MDL-63116](https://moodle.atlassian.net/browse/MDL-63116) - Data requests bulk actions
- [MDL-62309](https://moodle.atlassian.net/browse/MDL-62309) - Option to make site policies required or optional
- [MDL-61652](https://moodle.atlassian.net/browse/MDL-61652) - Capabilities for controlling who can download SAR data
- [MDL-62563](https://moodle.atlassian.net/browse/MDL-62563) - Data deletion of existing deleted users
- [MDL-63897](https://moodle.atlassian.net/browse/MDL-63897) - Pre-processing stage removed from data requests process
- [MDL-62558](https://moodle.atlassian.net/browse/MDL-62558) - Data retention summary (read-only)
- [MDL-63726](https://moodle.atlassian.net/browse/MDL-63726) - Option to remove the "Data retention summary" link in the footer
- [MDL-62491](https://moodle.atlassian.net/browse/MDL-62491) - HTML data request export format
- [MDL-63401](https://moodle.atlassian.net/browse/MDL-63401) - User expiry improvements
- [MDL-63619](https://moodle.atlassian.net/browse/MDL-63619) - Data purpose and category inheritance improvements
- [MDL-62560](https://moodle.atlassian.net/browse/MDL-62560) - Different data retention strategies for different roles in a purpose
- [MDL-62554](https://moodle.atlassian.net/browse/MDL-62554) - Ability to configure data registry to use module type defaults
- [MDL-63009](https://moodle.atlassian.net/browse/MDL-63009) - Site mentioned in email notifications of data requests
- [MDL-6074](https://moodle.atlassian.net/browse/MDL-6074) - Option to hide your name in the [online users block](https://docs.moodle.org/36/en/Online_users_block)

### Messaging[​](#messaging "Direct link to Messaging")

- **[MDL-57272](https://moodle.atlassian.net/browse/MDL-57272) and [MDL-63280](https://moodle.atlassian.net/browse/MDL-63280) - Group messaging**
- [MDL-63303](https://moodle.atlassian.net/browse/MDL-63303) - New messaging UI with [messaging drawer](https://docs.moodle.org/36/en/Messaging)
- [MDL-63279](https://moodle.atlassian.net/browse/MDL-63279) - Option to [disable site-wide messaging](https://docs.moodle.org/36/en/Messaging_settings)
- [MDL-63214](https://moodle.atlassian.net/browse/MDL-63214) - Privacy setting for restricting who can message you
  
  - The new 'Allow site-wide messaging' setting is disabled by default for new installs but enabled for upgraded sites if *$CFG-&gt;keepmessagingallusersenabled = true;* is defined in config.php
- [MDL-63213](https://moodle.atlassian.net/browse/MDL-63213) - Option to star messaging conversations
- [MDL-63283](https://moodle.atlassian.net/browse/MDL-63283) - Notifications not sent for group conversations
- [MDL-63281](https://moodle.atlassian.net/browse/MDL-63281) - Group members synchronised with messaging conversations members

### Assignment[​](#assignment "Direct link to Assignment")

- [MDL-27520](https://moodle.atlassian.net/browse/MDL-27520) - Assignment feedback can include media or other files

### Quiz[​](#quiz "Direct link to Quiz")

- [MDL-62610](https://moodle.atlassian.net/browse/MDL-62610) - Improved quiz statistics report usability for randomized questions
- [MDL-62708](https://moodle.atlassian.net/browse/MDL-62708) - Option to add ID numbers to questions and question categories
- [MDL-63738](https://moodle.atlassian.net/browse/MDL-63738) - Single questions can be exported from the question bank

### Workshop[​](#workshop "Direct link to Workshop")

- [MDL-60820](https://moodle.atlassian.net/browse/MDL-60820) - Teachers can specify workshop submission types

### Repositories[​](#repositories "Direct link to Repositories")

- [MDL-58943](https://moodle.atlassian.net/browse/MDL-58943) - Nextcloud integration, with a [Nextcloud repository](https://docs.moodle.org/36/en/Nextcloud_repository) and [OAuth 2 Nextcloud service](https://docs.moodle.org/36/en/OAuth_2_Nextcloud_service)

### Open Badges[​](#open-badges "Direct link to Open Badges")

- [MDL-58454](https://moodle.atlassian.net/browse/MDL-58454) - Support for Open Badges v2.0

### Performance[​](#performance "Direct link to Performance")

- [MDL-54035](https://moodle.atlassian.net/browse/MDL-54035) - Performance improvements to cache flags
- [MDL-47962](https://moodle.atlassian.net/browse/MDL-47962) - Glossary auto-linking filter performance improvements

### Usability improvements[​](#usability-improvements "Direct link to Usability improvements")

- [MDL-51177](https://moodle.atlassian.net/browse/MDL-51177) - atto\_htmlplus implemented to improve Atto editor HTML indenting
- [MDL-45170](https://moodle.atlassian.net/browse/MDL-45170) - Copy and paste of images from one WYSIWYG window to another
- [MDL-61388](https://moodle.atlassian.net/browse/MDL-61388) - Forum actions announced by screen reader when completed
- [MDL-62899](https://moodle.atlassian.net/browse/MDL-62899) - Global search displays a relevant icon next to link in results
- [MDL-46415](https://moodle.atlassian.net/browse/MDL-46415) - SVG/high resolution emoticons
- [MDL-58000](https://moodle.atlassian.net/browse/MDL-58000) - Larger badge images are used

### Experimental[​](#experimental "Direct link to Experimental")

- [MDL-53566](https://moodle.atlassian.net/browse/MDL-53566) - [Context freezing](https://docs.moodle.org/36/en/Context_freezing) - setting read-only access for categories, courses, activities and their content

## Other highlights[​](#other-highlights "Direct link to Other highlights")

### Functional changes[​](#functional-changes "Direct link to Functional changes")

- [MDL-17943](https://moodle.atlassian.net/browse/MDL-17943) - 'Resend confirmation email' button on login page
- [MDL-14274](https://moodle.atlassian.net/browse/MDL-14274) - IF conditions in grade calculations
- [MDL-37624](https://moodle.atlassian.net/browse/MDL-37624) - Calendar entries location support
- [MDL-36754](https://moodle.atlassian.net/browse/MDL-36754) - Images are displayed in forum notification emails
- [MDL-59259](https://moodle.atlassian.net/browse/MDL-59259) - Course format options may be specified in upload courses CSV file
- [MDL-41265](https://moodle.atlassian.net/browse/MDL-41265) - Page resource option to show/hide "Last modified"
- [MDL-61378](https://moodle.atlassian.net/browse/MDL-61378) - Forum post HTML structure improvements
- [MDL-59454](https://moodle.atlassian.net/browse/MDL-59454) - Option to download the list of course participants
- [MDL-60520](https://moodle.atlassian.net/browse/MDL-60520) - Analytics models can use different machine learning backends
- [MDL-61573](https://moodle.atlassian.net/browse/MDL-61573) - User menu: customusermenuitems map Font Awesome icons for non pix/t folders
- [MDL-62320](https://moodle.atlassian.net/browse/MDL-62320) - JSON added to the default MIME types list
- [MDL-63431](https://moodle.atlassian.net/browse/MDL-63431) - Atto media plugin title global attribute support
- [MDL-60435](https://moodle.atlassian.net/browse/MDL-60435) - Shibboleth authentication identity providers
- [MDL-59169](https://moodle.atlassian.net/browse/MDL-59169) - Grader report saves after edit with multiple tabs
- [MDL-62960](https://moodle.atlassian.net/browse/MDL-62960) - Drag and drop of course events respects the course start date

### Security issues[​](#security-issues "Direct link to Security issues")

- [MSA-18-0020](https://moodle.org/mod/forum/discuss.php?d=378731) Login CSRF vulnerability in login form. Note that this fix has previously been disclosed following the release of Moodle 3.5.3, 3.4.6, 3.3.9 and 3.1.15.

### For administrators[​](#for-administrators "Direct link to For administrators")

- [MDL-62334](https://moodle.atlassian.net/browse/MDL-62334) - 'Add a new course' link in Site administration
- [MDL-63253](https://moodle.atlassian.net/browse/MDL-63253) - Admin search results provide location of the found matching page
- [MDL-63772](https://moodle.atlassian.net/browse/MDL-63772) - Capability to control use of Atto Record RTC
- [MDL-63708](https://moodle.atlassian.net/browse/MDL-63708) - New blocks supported by the mobile app can be disabled
- [MDL-52953](https://moodle.atlassian.net/browse/MDL-52953) - Legacy log store deprecation
- [MDL-59429](https://moodle.atlassian.net/browse/MDL-59429) - Log changes to site administrators
- [MDL-62651](https://moodle.atlassian.net/browse/MDL-62651) - adhoc task runner
- [MDL-62777](https://moodle.atlassian.net/browse/MDL-62777) - Site upgrades via CLI display new default settings
- [MDL-63603](https://moodle.atlassian.net/browse/MDL-63603) - Indian Rupee added to [PayPal enrolment](https://docs.moodle.org/36/en/PayPal_enrolment) currencies
- [MDL-60514](https://moodle.atlassian.net/browse/MDL-60514) - Set Path to PHP CLI in order to display 'Run now' for [Scheduled tasks](https://docs.moodle.org/36/en/Scheduled_tasks)
- [MDL-61041](https://moodle.atlassian.net/browse/MDL-61041) - Assignment upgrade helper tool removed from core.

## For developers[​](#for-developers "Direct link to For developers")

- [MDL-55188](https://moodle.atlassian.net/browse/MDL-55188) - Old Events API final deprecation
- [MDL-54741](https://moodle.atlassian.net/browse/MDL-54741) - Phase 2 of deprecation of functions in lib/deprecatedlib.php
- [MDL-51803](https://moodle.atlassian.net/browse/MDL-51803) - Reusable element for drag and drop sortable table or list
- [MDL-63329](https://moodle.atlassian.net/browse/MDL-63329) - memcache session handler removal
- [MDL-63658](https://moodle.atlassian.net/browse/MDL-63658) - New Favourites subsystem
- [MDL-63729](https://moodle.atlassian.net/browse/MDL-63729) - Badges web services return new fields and data added by the Open Badges v2.0 specification
- [MDL-50812](https://moodle.atlassian.net/browse/MDL-50812) - core\_useragent::get\_browser\_version\_classes distinguishes between different browsers

### Privacy API update[​](#privacy-api-update "Direct link to Privacy API update")

In addition to existing requirements, any plugin which implements the plugin provider interface must also implement the `\core_privacy\local\request\core_userlist_provider` interface. Two new methods need to be implemented:

- [get users in context()](https://moodledev.io/docs/5.2/apis/subsystems/privacy#retrieving-the-users-in-a-context)
- [delete data for users()](https://moodledev.io/docs/5.2/apis/subsystems/privacy#delete-personal-information-for-several-users-in-a-specific-context)

However, the two above methods are not required for plugins that [implement the `null provider`](https://moodledev.io/docs/5.2/apis/subsystems/privacy#plugins-which-do-not-store-personal-data) only (i.e. which do not store personal data).

Note that these changes are also required for latest Moodle 3.4.6 and 3.5.3 versions.

### Behat scenario files[​](#behat-scenario-files "Direct link to Behat scenario files")

- [MDL-57281](https://moodle.atlassian.net/browse/MDL-57281) - The behat step `I navigate to "ITEM" node in "MAINNODE > PATH"` has been deprecated and throws an exception with details on how to replace it. The recommended replacement steps work in all recent Moodle versions. The updated Behat will pass with Moodle 3.4 too.

### Login token[​](#login-token "Direct link to Login token")

If your plugin provides an alternative login form (e.g. it is a theme replacing the default login form template / renderer), the login form must include a new login token field. For details of required changes, see [Login token](https://docs.moodle.org/dev/Login_token). Note that this also affects latest stable branches too.

### New core functions[​](#new-core-functions "Direct link to New core functions")

- `userdate_htmltime()`

### New callback hooking points in page layouts[​](#new-callback-hooking-points-in-page-layouts "Direct link to New callback hooking points in page layouts")

- `standard_after_main_region_html` - A new general purpose callback hooking point in the page layout. Used for example by the new messaging drawer UI.

### Component APIs upgrades[​](#component-apis-upgrades "Direct link to Component APIs upgrades")

Please refer to the upgrade.txt files in the relevant component directory for changes in this particular Moodle release.

- [admin/tool/log/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/admin/tool/log/upgrade.txt)
- [admin/tool/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/admin/tool/upgrade.txt)
- [auth/shibboleth/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/auth/shibboleth/upgrade.txt)
- [auth/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/auth/upgrade.txt)
- [badges/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/badges/upgrade.txt)
- [blocks/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/blocks/upgrade.txt)
- [cache/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/cache/upgrade.txt)
- [calendar/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/calendar/upgrade.txt)
- [course/format/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/course/format/upgrade.txt)
- [course/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/course/upgrade.txt)
- [enrol/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/enrol/upgrade.txt)
- [filter/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/filter/upgrade.txt)
- [grade/grading/form/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/grade/grading/form/upgrade.txt)
- [grade/report/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/grade/report/upgrade.txt)
- [grade/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/grade/upgrade.txt)
- [lib/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/lib/upgrade.txt)
- [media/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/media/upgrade.txt)
- [message/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/message/upgrade.txt)
- [mod/assign/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/assign/upgrade.txt)
- [mod/feedback/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/feedback/upgrade.txt)
- [mod/forum/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/forum/upgrade.txt)
- [mod/quiz/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/quiz/upgrade.txt)
- [mod/scorm/report/basic/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/scorm/report/basic/upgrade.txt)
- [mod/scorm/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/scorm/upgrade.txt)
- [mod/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/upgrade.txt)
- [mod/workshop/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/mod/workshop/upgrade.txt)
- [question/format/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/question/format/upgrade.txt)
- [report/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/report/upgrade.txt)
- [tag/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/tag/upgrade.txt)
- [theme/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/theme/upgrade.txt)
- [user/upgrade.txt](https://github.com/moodle/moodle/blob/v3.6.0/user/upgrade.txt)

## Translations[​](#translations "Direct link to Translations")

- [Notes de mise à jour de Moodle 3.6](https://docs.moodle.org/fr/Notes_de_mise_%C3%A0_jour_de_Moodle_3.6)
- [Notas de Moodle 3.6](https://docs.moodle.org/es/Notas_de_Moodle_3.6)