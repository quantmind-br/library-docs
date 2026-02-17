---
title: Moodle 5.0 | Moodle Developer Resources
url: https://moodledev.io/general/releases/5.0
source: sitemap
fetched_at: 2026-02-17T16:17:11.823584-03:00
rendered_js: false
word_count: 2149
summary: This document details the release notes for Moodle 5.0.0, including updated system requirements, database compatibility changes, and new features like AI integration and SMS notifications.
tags:
    - moodle-5-0
    - release-notes
    - system-requirements
    - php-8-2
    - database-compatibility
    - ai-features
    - ux-improvements
category: reference
---

Release date: 14 April 2025

Here is [the full list of fixed issues in 5.0.0](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%225.0%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

If you are upgrading from a previous version, please see [Upgrading](https://docs.moodle.org/500/en/Upgrading) in the user docs.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software and operating systems up-to-date.

- Moodle upgrade: Moodle 4.2.3 or later.
- PHP version: minimum PHP 8.2.0 *Note: minimum PHP version has increased in this Moodle version*. PHP 8.3.x and 8.4.x are supported too. See [PHP](https://moodledev.io/general/development/policies/php) for details.
- PHP extension **sodium** is required. See [Environment - PHP extension sodium](https://docs.moodle.org/en/Environment_-_PHP_extension_sodium).
- PHP setting **max\_input\_vars** must be &gt;= 5000. For further details, see [Environment - max input vars](https://docs.moodle.org/en/Environment_-_max_input_vars).
- PHP variants: Only 64-bit versions of PHP are supported. *Note: Changed since 4.1*.

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)14 (increased in this Moodle version)Latest[MySQL](http://www.mysql.com/)8.4 (increased in this Moodle version)Latest[MariaDB](https://mariadb.org/)10.11.0 (increased in this Moodle version)Latest[Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)[8.0](#aurora-mysql-compatibility-version)Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2017Latest

Please note that Oracle Database is no longer supported from Moodle LMS 5.0.

Database prefixes

Since Moodle 4.3, the maximum length for the database prefix (`$CFG->prefix`) is 10 characters. Installation or upgrade won't be possible with longer prefixes.

Important

For all requirements it is recommended to use the latest point release of that version as a minimum.

In some cases earlier versions of a requirement may be noted, but may be pre-release versions.

#### Aurora MySQL compatibility version[​](#aurora-mysql-compatibility-version "Direct link to Aurora MySQL compatibility version")

This system requires configuration using standard MySQL version numbers (for example, 8.0) rather than Aurora's internal versioning (for example, 3.x) to maintain compatibility with MySQL client tools, version-dependent features, and database detection methods.

## Client requirements[​](#client-requirements "Direct link to Client requirements")

### Browser support[​](#browser-support "Direct link to Browser support")

Moodle is compatible with any standards compliant web browser. We regularly test Moodle with the following browsers:

Desktop:

- Chrome
- Firefox
- Safari
- Edge

Mobile:

- MobileSafari
- Google Chrome

For the best experience and optimum security, we recommend that you keep your browser up to date.

## Major UX improvements[​](#major-ux-improvements "Direct link to Major UX improvements")

### New centralised course overview page[​](#new-centralised-course-overview-page "Direct link to New centralised course overview page")

- [MDL-83873](https://moodle.atlassian.net/browse/MDL-83873) - Create a "human date" output classes
- [MDL-83872](https://moodle.atlassian.net/browse/MDL-83872) - Add on-demand overview tables to the overview page
- [MDL-83892](https://moodle.atlassian.net/browse/MDL-83892) - Migrate Feedback activity index to course overview integration
- [MDL-83871](https://moodle.atlassian.net/browse/MDL-83871) - Create a basic course activities overview page
- [MDL-84469](https://moodle.atlassian.net/browse/MDL-84469) - Set the fallback overview report for activities without integration
- [MDL-84555](https://moodle.atlassian.net/browse/MDL-84555) - Add purpose colour to activity icons in course activities overview and default activity completion form
- [MDL-83888](https://moodle.atlassian.net/browse/MDL-83888) - Migrate Assign index to course overview integration
- [MDL-83901](https://moodle.atlassian.net/browse/MDL-83901) - Migrate Workshop activity index to course overview integration
- [MDL-83869](https://moodle.atlassian.net/browse/MDL-83869) - Create a generic collapsable section output component
- [MDL-84602](https://moodle.atlassian.net/browse/MDL-84602) - Add alert counting to activity overview items
- [MDL-84346](https://moodle.atlassian.net/browse/MDL-84346) - Make the completion button styles more generic

## Other major features[​](#other-major-features "Direct link to Other major features")

### AI new features and improvements[​](#ai-new-features-and-improvements "Direct link to AI new features and improvements")

- [MDL-83006](https://moodle.atlassian.net/browse/MDL-83006) - New provider plugin - Ollama
- [MDL-82942](https://moodle.atlassian.net/browse/MDL-82942) - New course placement - Explain
- [MDL-82977](https://moodle.atlassian.net/browse/MDL-82977) - Support multiple provider instances
- [MDL-82980](https://moodle.atlassian.net/browse/MDL-82980) - Per model settings
- [MDL-83216](https://moodle.atlassian.net/browse/MDL-83216) - Provider ordering
- [MDL-83395](https://moodle.atlassian.net/browse/MDL-83395) - Reporting - AI usage for admins
- [MDL-83396](https://moodle.atlassian.net/browse/MDL-83396) - Reporting - AI policy acceptance

### Implement Open Badges 3.0[​](#implement-open-badges-30 "Direct link to Implement Open Badges 3.0")

- [MDL-83909](https://moodle.atlassian.net/browse/MDL-83909) - Remove the image author's fields in badges
- [MDL-83884](https://moodle.atlassian.net/browse/MDL-83884) - Move form files from badges to badges/classes/form
- [MDL-84577](https://moodle.atlassian.net/browse/MDL-84577) - Review the badge creation form, to reorganise the fields and remove/improve tooltips
- [MDL-82905](https://moodle.atlassian.net/browse/MDL-82905) - In the badges report, display criteria as a list only if there are multiple items
- [MDL-82904](https://moodle.atlassian.net/browse/MDL-82904) - Display empty column in the badges report when no criteria is set

### SMS notification provider & initial notifications[​](#sms-notification-provider--initial-notifications "Direct link to SMS notification provider & initial notifications")

- [MDL-81015](https://moodle.atlassian.net/browse/MDL-81015) - Add support for sending SMS notifications asynchronously
- [MDL-83518](https://moodle.atlassian.net/browse/MDL-83518) - SMS notifications: Implement SMS as a new notification method and set up for assignment notifications
- [MDL-79329](https://moodle.atlassian.net/browse/MDL-79329) - Implement Modica SMS gateway plugin

### Enhance icons utilising Font Awesome 6[​](#enhance-icons-utilising-font-awesome-6 "Direct link to Enhance icons utilising Font Awesome 6")

- [MDL-83087](https://moodle.atlassian.net/browse/MDL-83087) - Replace the more actions menu in course/index.php with ellipsis
- [MDL-83639](https://moodle.atlassian.net/browse/MDL-83639) - Update custom icons
- [MDL-83933](https://moodle.atlassian.net/browse/MDL-83933) - Switch import and export icons
- [MDL-82460](https://moodle.atlassian.net/browse/MDL-82460) - Deprecate unused pix icons

### TinyMCE text editor[​](#tinymce-text-editor "Direct link to TinyMCE text editor")

- [MDL-80953](https://moodle.atlassian.net/browse/MDL-80953) - Make TinyMCE less strict for onclick JavaScript action (consistent with Atto's handling)
- [MDL-78428](https://moodle.atlassian.net/browse/MDL-78428) - Improve media adding user experience
- [MDL-84125](https://moodle.atlassian.net/browse/MDL-84125) - Add TinyMCE Premium accessibility plugin
- [MDL-84126](https://moodle.atlassian.net/browse/MDL-84126) - Disable plugins by role

### Course improvements[​](#course-improvements "Direct link to Course improvements")

- [MDL-83725](https://moodle.atlassian.net/browse/MDL-83725) - Improve the way activity icons are colourised
- [MDL-83673](https://moodle.atlassian.net/browse/MDL-83673) - Add throttle to the course page scroll event handling and prevent unnecessary updates
- [MDL-83562](https://moodle.atlassian.net/browse/MDL-83562) - Remove the "movehere" elements from the course page
- [MDL-82351](https://moodle.atlassian.net/browse/MDL-82351) - Make social format compatible with the new course editor
- [MDL-82349](https://moodle.atlassian.net/browse/MDL-82349) - Migrate frontpage to the new course editor

### Upgrade Boost theme to use Bootstrap 5.x[​](#upgrade-boost-theme-to-use-bootstrap-5x "Direct link to Upgrade Boost theme to use Bootstrap 5.x")

- [MDL-84324](https://moodle.atlassian.net/browse/MDL-84324) - Add jQuery compatibility for Bootstrap 5
- [MDL-81825](https://moodle.atlassian.net/browse/MDL-81825) - Refactor "Screen reader" classes/functions renamed in Bootstrap 5
- [MDL-80519](https://moodle.atlassian.net/browse/MDL-80519) - Create a compatibility layer for Bootstrap v4 &gt; v5 SCSS
- [MDL-84450](https://moodle.atlassian.net/browse/MDL-84450) - Create a compatibility helper for Boostrap v4 &gt; v5 data-attributes
- [MDL-75669](https://moodle.atlassian.net/browse/MDL-75669) - Upgrade the Boost theme with Bootstrap 5.x

### Quiz and Question bank[​](#quiz-and-question-bank "Direct link to Quiz and Question bank")

- [MDL-71378](https://moodle.atlassian.net/browse/MDL-71378) - Make shared question banks more manageable and usable
- [MDL-77713](https://moodle.atlassian.net/browse/MDL-77713) - Question version options when previewing - put latest version first
- [MDL-84576](https://moodle.atlassian.net/browse/MDL-84576) - Give non-editing teacher role the "Use questions" capabilities by default to support shared question banks
- [MDL-83862](https://moodle.atlassian.net/browse/MDL-83862) - Add question bank filter - Modified time
- [MDL-83861](https://moodle.atlassian.net/browse/MDL-83861) - Add question bank filter - Question ID number
- [MDL-83860](https://moodle.atlassian.net/browse/MDL-83860) - Add question bank filter - Question name
- [MDL-83859](https://moodle.atlassian.net/browse/MDL-83859) - Add question bank filter - Question type
- [MDL-83883](https://moodle.atlassian.net/browse/MDL-83883) - Add question bank filter - Status
- [MDL-83881](https://moodle.atlassian.net/browse/MDL-83881) - Add question bank filter - Modifier and Owner
- [MDL-84247](https://moodle.atlassian.net/browse/MDL-84247) - Improve Missing Question Type handling in question bank
- [MDL-84302](https://moodle.atlassian.net/browse/MDL-84302) - Improve Missing Question Type handling in quiz
- [MDL-68806](https://moodle.atlassian.net/browse/MDL-68806) - New quiz attempt states and asynchronous attempt creation
- [MDL-84191](https://moodle.atlassian.net/browse/MDL-84191) - Add question bank filter - question text and feedback

### BigBlueButton[​](#bigbluebutton "Direct link to BigBlueButton")

- [MDL-84412](https://moodle.atlassian.net/browse/MDL-84412) - Change the BigBlueButtonBN activity icon
- [MDL-84245](https://moodle.atlassian.net/browse/MDL-84245) - Add manual grade functionality to BigBlueButton plugin
- [MDL-83766](https://moodle.atlassian.net/browse/MDL-83766) - Change order subplugin classes are retrieved by BigBlueButton

### Report builder[​](#report-builder "Direct link to Report builder")

- [MDL-77270](https://moodle.atlassian.net/browse/MDL-77270) - Add ability to duplicate a custom report
- [MDL-83552](https://moodle.atlassian.net/browse/MDL-83552) - Add custom fields to Report builder

### Assignment[​](#assignment "Direct link to Assignment")

- [MDL-84387](https://moodle.atlassian.net/browse/MDL-84387) - Improve assignment submission confirmation by including a list of submitted files
- [MDL-84733](https://moodle.atlassian.net/browse/MDL-84733) - Enhance assignment notification message customisation with additional data fields available for custom strings
- [MDL-75292](https://moodle.atlassian.net/browse/MDL-75292) - Add "Graded" option to the status filter on the assignment submissions page

### Accessibility improvements[​](#accessibility-improvements "Direct link to Accessibility improvements")

- [MDL-60910](https://moodle.atlassian.net/browse/MDL-60910) - Drag and drop onto image, using transparent pictures
- [MDL-78453](https://moodle.atlassian.net/browse/MDL-78453) - Allow users to enter a long description for complex images

### Usability improvements[​](#usability-improvements "Direct link to Usability improvements")

- [MDL-73909](https://moodle.atlassian.net/browse/MDL-73909) - Notification settings toggle switches should save automatically
- [MDL-83108](https://moodle.atlassian.net/browse/MDL-83108) - Add new option in the Insert H5P plugin to enable auto-play of embedded H5P content in the app
- [MDL-82944](https://moodle.atlassian.net/browse/MDL-82944) - Messaging should warn if you try to navigate to another page with an un-sent message
- [MDL-84142](https://moodle.atlassian.net/browse/MDL-84142) - Homogenise output of the enrolment methods on the course enrolment page
- [MDL-81744](https://moodle.atlassian.net/browse/MDL-81744) - Improve feedback activity "Template" page UI
- [MDL-84208](https://moodle.atlassian.net/browse/MDL-84208) - Use collapsable sections in the default activity completion page
- [MDL-81759](https://moodle.atlassian.net/browse/MDL-81759) - Course import pagelayout is different to the rest of pages

## Other Highlights[​](#other-highlights "Direct link to Other Highlights")

### Feature removals[​](#feature-removals "Direct link to Feature removals")

The following features are removed from Moodle LMS 5.0 onwards. Please see [Important changes in the upcoming Moodle 5.0](https://moodle.org/mod/forum/discuss.php?d=467339) for more information.

- [MDL-83282](https://moodle.atlassian.net/browse/MDL-83282) - Remove Atto text editor
- [MDL-83172](https://moodle.atlassian.net/browse/MDL-83172) - Remove Oracle database support
- [MDL-82457](https://moodle.atlassian.net/browse/MDL-82457) - Remove Chat and Survey from core
- [MDL-78778](https://moodle.atlassian.net/browse/MDL-78778) - Remove the auth\_cas plugin
- [MDL-84107](https://moodle.atlassian.net/browse/MDL-84107) - Remove mlbackend\_php plugin from core
- [MDL-84652](https://moodle.atlassian.net/browse/MDL-84652) - Remove all MNet plugins
- [MDL-84265](https://moodle.atlassian.net/browse/MDL-84265) - Remove DML/DDL SQLite support
- [MDL-83703](https://moodle.atlassian.net/browse/MDL-83703) - Remove support for legacy subplugins.php

### Functional changes[​](#functional-changes "Direct link to Functional changes")

- [MDL-70556](https://moodle.atlassian.net/browse/MDL-70556) - Increase course fullname database field length beyond 254 characters
- [MDL-75196](https://moodle.atlassian.net/browse/MDL-75196) - Improve mod\_data link processing for backup
- [MDL-83265](https://moodle.atlassian.net/browse/MDL-83265) - Salutation in Course-Approved-Email
- [MDL-80984](https://moodle.atlassian.net/browse/MDL-80984) - Implement generic penalties in gradebook
- [MDL-84356](https://moodle.atlassian.net/browse/MDL-84356) - Include course link variable in the course welcome message
- [MDL-81714](https://moodle.atlassian.net/browse/MDL-81714) - Make re-grading of course final grades asynchronous
- [MDL-84139](https://moodle.atlassian.net/browse/MDL-84139) - Add an option to display title for the enrol\_fee enrolment
- [MDL-82034](https://moodle.atlassian.net/browse/MDL-82034) - Make mod\_subsection enabled by default
- [MDL-82555](https://moodle.atlassian.net/browse/MDL-82555) - Section links block should show section names without numbers

### For administrators[​](#for-administrators "Direct link to For administrators")

- [MDL-81780](https://moodle.atlassian.net/browse/MDL-81780) - Ad-hoc tasks improvements - display fail delay and allow it to be reset
- [MDL-83399](https://moodle.atlassian.net/browse/MDL-83399) - Allow site admins to login as each other
- [MDL-83850](https://moodle.atlassian.net/browse/MDL-83850) - Activity Completion Report: Add "Completed date/time" header to the exported spreadsheet
- [MDL-74149](https://moodle.atlassian.net/browse/MDL-74149) - tool\_usertours: Filters to exclude categories and courses
- [MDL-81790](https://moodle.atlassian.net/browse/MDL-81790) - The "Logs" section at the activity "More" menu should direct users to a dedicated activity logs page
- [MDL-81070](https://moodle.atlassian.net/browse/MDL-81070) - Display contacts' names in the course search result for admins
- [MDL-82450](https://moodle.atlassian.net/browse/MDL-82450) - Clarify the scheduled task table "Fail delay" value
- [MDL-83119](https://moodle.atlassian.net/browse/MDL-83119) - search\_solr: Implement check on connectivity, space usage

### Performance[​](#performance "Direct link to Performance")

- [MDL-84844](https://moodle.atlassian.net/browse/MDL-84844) - Improve mod\_subsection performance in course editing operations
- [MDL-82584](https://moodle.atlassian.net/browse/MDL-82584) - Workshop get\_users\_with\_capability\_sql method optimisation
- [MDL-83718](https://moodle.atlassian.net/browse/MDL-83718) - Improve report builder table performance by combining count and select

## Security improvements[​](#security-improvements "Direct link to Security improvements")

- [MDL-83942](https://moodle.atlassian.net/browse/MDL-83942) - Allow admins to make a default tag collection not searchable
- [MDL-82958](https://moodle.atlassian.net/browse/MDL-82958) - User index page errors should be more generic
- [MDL-84011](https://moodle.atlassian.net/browse/MDL-84011) - Switch from PHP serialization to JSON in Wikimedia repository

### Multi-factor Authentication improvements[​](#multi-factor-authentication-improvements "Direct link to Multi-factor Authentication improvements")

- [MDL-83516](https://moodle.atlassian.net/browse/MDL-83516) - Improve MFA admin setup - factor table improvements
- [MDL-79958](https://moodle.atlassian.net/browse/MDL-79958) - Improve MFA admin setup - default factor and explanations of factors on their settings pages
- [MDL-81551](https://moodle.atlassian.net/browse/MDL-81551) - Inform user that reading MFA security token was successful during setup
- [MDL-81285](https://moodle.atlassian.net/browse/MDL-81285) - Provide a clear failure when MFA security key not supported for browsers

## For developers[​](#for-developers "Direct link to For developers")

- [MDL-63219](https://moodle.atlassian.net/browse/MDL-63219) - Add support for Moodle filters to primary/custom menus
- [MDL-79843](https://moodle.atlassian.net/browse/MDL-79843) - Introduce mechanism for plugin type deprecation
- [MDL-83473](https://moodle.atlassian.net/browse/MDL-83473) - Replacement of extern\_server\_course function in course/view.php by hooks API
- [MDL-72526](https://moodle.atlassian.net/browse/MDL-72526) - Change course format output classes to use protected properties instead of private
- [MDL-81745](https://moodle.atlassian.net/browse/MDL-81745) - Replace feedback activity drag and drop YUI module with SortableList
- [MDL-82565](https://moodle.atlassian.net/browse/MDL-82565) - Add support for routing of regular pages
- [MDL-82313](https://moodle.atlassian.net/browse/MDL-82313) - Contrib database activity field icons should display in field type column

### Web service additions and updates[​](#web-service-additions-and-updates "Direct link to Web service additions and updates")

- [MDL-78449](https://moodle.atlassian.net/browse/MDL-78449) - Support groups in mod\_choice\_get\_choice\_results web service
- [MDL-83026](https://moodle.atlassian.net/browse/MDL-83026) - External functions that return badges should include the course name
- [MDL-82775](https://moodle.atlassian.net/browse/MDL-82775) - Return total number of attempts in mod\_h5pactivity\_get\_user\_attempts web service

### Deprecations[​](#deprecations "Direct link to Deprecations")

- [MDL-77668](https://moodle.atlassian.net/browse/MDL-77668) - Deprecate grade\_edit\_tree\_column\_select class
- [MDL-71472](https://moodle.atlassian.net/browse/MDL-71472) - Deprecate add\_select\_with\_email
- [MDL-83035](https://moodle.atlassian.net/browse/MDL-83035) - Deprecate behat\_admin\_presets custom steps
- [MDL-84657](https://moodle.atlassian.net/browse/MDL-84657) - Deprecate calendar\_add\_month()
- [MDL-83477](https://moodle.atlassian.net/browse/MDL-83477) - Deprecate core:t/collapsedcaret icon
- [MDL-83764](https://moodle.atlassian.net/browse/MDL-83764) - Deprecate externservercourse.php feature
- [MDL-84449](https://moodle.atlassian.net/browse/MDL-84449) - Deprecate imagecopybicubic (lib/gdlib.php)
- [MDL-82342](https://moodle.atlassian.net/browse/MDL-82342) - Deprecate pre-4.0 course editor web services
- [MDL-84673](https://moodle.atlassian.net/browse/MDL-84673) - Deprecate print\_graded\_users\_selector()
- [MDL-80995](https://moodle.atlassian.net/browse/MDL-80995) - Deprecate setup\_factor (tool\_mfa\\output\\renderer)
- [MDL-82341](https://moodle.atlassian.net/browse/MDL-82341) - Deprecate the old course JavaScript and YUI modules
- [MDL-84267](https://moodle.atlassian.net/browse/MDL-84267) - Deprecate unused comment related capabilities in data module
- [MDL-84617](https://moodle.atlassian.net/browse/MDL-84617) - Deprecation legacy/deprecated calendar functions
- [MDL-78489](https://moodle.atlassian.net/browse/MDL-78489) - Final deprecation of availability\_more amd module and availability::availability\_info() method
- [MDL-81328](https://moodle.atlassian.net/browse/MDL-81328) - Final deprecation of book\_get\_nav\_classes
- [MDL-79434](https://moodle.atlassian.net/browse/MDL-79434) - Final deprecation of calendar functions deprecated in Moodle 4.3
- [MDL-78926](https://moodle.atlassian.net/browse/MDL-78926) - Final deprecation of core\_course\\output\\activity\_information output class
- [MDL-80116](https://moodle.atlassian.net/browse/MDL-80116) - Final deprecation of course editing functions deprecated in Moodle 4.4 from the course hierarchy project
- [MDL-81185](https://moodle.atlassian.net/browse/MDL-81185) - Final deprecation of enrol\_self\_plugin::get\_welcome\_email\_contact()
- [MDL-83095](https://moodle.atlassian.net/browse/MDL-83095) - Final deprecation of functions in blocks/tag\_youtube/block\_tag\_youtube.php
- [MDL-76561](https://moodle.atlassian.net/browse/MDL-76561) - Final deprecation of functions in lib/deprecatedlib.php initially deprecated in Moodle version 4.0 or earlier
- [MDL-75189](https://moodle.atlassian.net/browse/MDL-75189) - Final deprecation of functions in mod/data/lib.php
- [MDL-79907](https://moodle.atlassian.net/browse/MDL-79907) - Final deprecation of grade\_structure::get\_element\_type\_string(), grade\_structure::get\_element\_header(), grade\_structure::get\_element\_icon(), grade\_structure::get\_activity\_link()
- [MDL-78890](https://moodle.atlassian.net/browse/MDL-78890) - Final deprecation of gradereport\_grader::get\_right\_avg\_row()
- [MDL-81155](https://moodle.atlassian.net/browse/MDL-81155) - Final deprecation of grouplist in report\_log\_renderable
- [MDL-77621](https://moodle.atlassian.net/browse/MDL-77621) - Final deprecation of lib/cronlib.php
- [MDL-75875](https://moodle.atlassian.net/browse/MDL-75875) - Final deprecation of single\_button $primary parameter
- [MDL-81509](https://moodle.atlassian.net/browse/MDL-81509) - Final deprecation of task\_base::is\_blocking and set\_blocking
- [MDL-78605](https://moodle.atlassian.net/browse/MDL-78605) - Final deprecation of token\_table::col\_token()
- [MDL-78090](https://moodle.atlassian.net/browse/MDL-78090) - Final deprecations in Moodle 5.0 core\_question
- [MDL-78304](https://moodle.atlassian.net/browse/MDL-78304) - Final deprecations in Moodle 5.0 MNet
- [MDL-78118](https://moodle.atlassian.net/browse/MDL-78118) - Final removal of custom report elements deprecated in 4.3
- [MDL-78711](https://moodle.atlassian.net/browse/MDL-78711) - Final removal of edit\_default\_completion()
- [MDL-78780](https://moodle.atlassian.net/browse/MDL-78780) - Final removal of grade ::get\_lang\_string helper methods
- [MDL-79214](https://moodle.atlassian.net/browse/MDL-79214) - Final removal of htmllize\_tree() in mod/folder
- [MDL-78635](https://moodle.atlassian.net/browse/MDL-78635) - Final removal of libxml\_disable\_entity\_loader helpers
- [MDL-79124](https://moodle.atlassian.net/browse/MDL-79124) - Final removal of old user preference AJAX APIs
- [MDL-78869](https://moodle.atlassian.net/browse/MDL-78869) - Final removal of OpenSSL encryption library fallbacks
- [MDL-80944](https://moodle.atlassian.net/browse/MDL-80944) - Final removal of quiz\_delete\_override and quiz\_delete\_all\_overrides
- [MDL-80430](https://moodle.atlassian.net/browse/MDL-80430) - Final removal of report builder default table alias support
- [MDL-78706](https://moodle.atlassian.net/browse/MDL-78706) - Final removal of repository get\_file\_size
- [MDL-79086](https://moodle.atlassian.net/browse/MDL-79086) - Final removal of share\_activity method in MoodleNet
- [MDL-79162](https://moodle.atlassian.net/browse/MDL-79162) - Final removal of table badges methods
- [MDL-80491](https://moodle.atlassian.net/browse/MDL-80491) - Final removal of update\_communication method in enrollib
- [MDL-84036](https://moodle.atlassian.net/browse/MDL-84036) - Finally remove deprecated external functions
- [MDL-76564](https://moodle.atlassian.net/browse/MDL-76564) - Remove Behat steps deprecated in Moodle versions 4.4 or earlier
- [MDL-81230](https://moodle.atlassian.net/browse/MDL-81230) - Remove deprecated adhoc tasks in BigBlueButton
- [MDL-83765](https://moodle.atlassian.net/browse/MDL-83765) - Remove deprecated functions in action\_menu class
- [MDL-84742](https://moodle.atlassian.net/browse/MDL-84742) - Remove empty file enrol/self/bulkchangeforms.php
- [MDL-77107](https://moodle.atlassian.net/browse/MDL-77107) - Remove grades and grade report Behat steps deprecated in 4.2
- [MDL-82937](https://moodle.atlassian.net/browse/MDL-82937) - Remove legacy tabs.php file from Lesson module
- [MDL-76566](https://moodle.atlassian.net/browse/MDL-76566) - Remove old classes renamed in Moodle versions 4.4 or earlier
- [MDL-82825](https://moodle.atlassian.net/browse/MDL-82825) - Remove php-enum library
- [MDL-80156](https://moodle.atlassian.net/browse/MDL-80156) - Remove SCSS deprecated in 4.4
- [MDL-76565](https://moodle.atlassian.net/browse/MDL-76565) - Remove strings deprecated in Moodle versions 4.4 or earlier
- [MDL-61232](https://moodle.atlassian.net/browse/MDL-61232) - Retire admin/process\_email.php
- [MDL-84674](https://moodle.atlassian.net/browse/MDL-84674) - Trim old deprecations Moodle 4.0 or earlier

### Component API updates[​](#component-api-updates "Direct link to Component API updates")

- [core](https://github.com/moodle/moodle/blob/v5.0.0/lib/UPGRADING.md)
- [core\_adminpresets](https://github.com/moodle/moodle/blob/v5.0.0/admin/presets/UPGRADING.md)
- [core\_ai](https://github.com/moodle/moodle/blob/v5.0.0/ai/UPGRADING.md)
- [core\_analytics](https://github.com/moodle/moodle/blob/v5.0.0/analytics/UPGRADING.md)
- [core\_auth](https://github.com/moodle/moodle/blob/v5.0.0/auth/UPGRADING.md)
- [core\_backup](https://github.com/moodle/moodle/blob/v5.0.0/backup/util/ui/UPGRADING.md)
- [core\_badges](https://github.com/moodle/moodle/blob/v5.0.0/badges/UPGRADING.md)
- [core\_block](https://github.com/moodle/moodle/blob/v5.0.0/blocks/UPGRADING.md)
- [core\_calendar](https://github.com/moodle/moodle/blob/v5.0.0/calendar/UPGRADING.md)
- [core\_completion](https://github.com/moodle/moodle/blob/v5.0.0/completion/UPGRADING.md)
- [core\_course](https://github.com/moodle/moodle/blob/v5.0.0/course/UPGRADING.md)
- [core\_courseformat](https://github.com/moodle/moodle/blob/v5.0.0/course/format/UPGRADING.md)
- [core\_customfield](https://github.com/moodle/moodle/blob/v5.0.0/customfield/UPGRADING.md)
- [core\_enrol](https://github.com/moodle/moodle/blob/v5.0.0/enrol/UPGRADING.md)
- [core\_files](https://github.com/moodle/moodle/blob/v5.0.0/files/UPGRADING.md)
- [core\_form](https://github.com/moodle/moodle/blob/v5.0.0/lib/form/UPGRADING.md)
- [core\_grades](https://github.com/moodle/moodle/blob/v5.0.0/grade/UPGRADING.md)
- [core\_mnet](https://github.com/moodle/moodle/blob/v5.0.0/mnet/UPGRADING.md)
- [core\_portfolio](https://github.com/moodle/moodle/blob/v5.0.0/portfolio/UPGRADING.md)
- [core\_question](https://github.com/moodle/moodle/blob/v5.0.0/question/UPGRADING.md)
- [core\_reportbuilder](https://github.com/moodle/moodle/blob/v5.0.0/reportbuilder/UPGRADING.md)
- [core\_repository](https://github.com/moodle/moodle/blob/v5.0.0/repository/UPGRADING.md)
- [core\_sms](https://github.com/moodle/moodle/blob/v5.0.0/sms/UPGRADING.md)
- [core\_tag](https://github.com/moodle/moodle/blob/v5.0.0/tag/UPGRADING.md)
- [core\_user](https://github.com/moodle/moodle/blob/v5.0.0/user/UPGRADING.md)
- [aiplacement\_courseassist](https://github.com/moodle/moodle/blob/v5.0.0/ai/placement/courseassist/UPGRADING.md)
- [block\_site\_main\_menu](https://github.com/moodle/moodle/blob/v5.0.0/blocks/site_main_menu/UPGRADING.md)
- [block\_social\_activities](https://github.com/moodle/moodle/blob/v5.0.0/blocks/social_activities/UPGRADING.md)
- [editor\_tiny](https://github.com/moodle/moodle/blob/v5.0.0/lib/editor/tiny/UPGRADING.md)
- [enrol\_guest](https://github.com/moodle/moodle/blob/v5.0.0/enrol/guest/UPGRADING.md)
- [enrol\_self](https://github.com/moodle/moodle/blob/v5.0.0/enrol/self/UPGRADING.md)
- [format\_topics](https://github.com/moodle/moodle/blob/v5.0.0/course/format/topics/UPGRADING.md)
- [gradereport](https://github.com/moodle/moodle/blob/v5.0.0/grade/report/UPGRADING.md)
- [gradereport\_grader](https://github.com/moodle/moodle/blob/v5.0.0/grade/report/grader/UPGRADING.md)
- [mlbackend\_php](https://github.com/moodle/moodle/blob/v5.0.0/undefined/UPGRADING.md)
- [mnetservice](https://github.com/moodle/moodle/blob/v5.0.0/undefined/UPGRADING.md)
- [mnetservice\_enrol](https://github.com/moodle/moodle/blob/v5.0.0/undefined/UPGRADING.md)
- [mod](https://github.com/moodle/moodle/blob/v5.0.0/mod/UPGRADING.md)
- [mod\_assign](https://github.com/moodle/moodle/blob/v5.0.0/mod/assign/UPGRADING.md)
- [mod\_book](https://github.com/moodle/moodle/blob/v5.0.0/mod/book/UPGRADING.md)
- [mod\_choice](https://github.com/moodle/moodle/blob/v5.0.0/mod/choice/UPGRADING.md)
- [mod\_data](https://github.com/moodle/moodle/blob/v5.0.0/mod/data/UPGRADING.md)
- [mod\_feedback](https://github.com/moodle/moodle/blob/v5.0.0/mod/feedback/UPGRADING.md)
- [mod\_folder](https://github.com/moodle/moodle/blob/v5.0.0/mod/folder/UPGRADING.md)
- [mod\_h5pactivity](https://github.com/moodle/moodle/blob/v5.0.0/mod/h5pactivity/UPGRADING.md)
- [mod\_imscp](https://github.com/moodle/moodle/blob/v5.0.0/mod/imscp/UPGRADING.md)
- [mod\_lesson](https://github.com/moodle/moodle/blob/v5.0.0/mod/lesson/UPGRADING.md)
- [mod\_lti](https://github.com/moodle/moodle/blob/v5.0.0/mod/lti/UPGRADING.md)
- [mod\_quiz](https://github.com/moodle/moodle/blob/v5.0.0/mod/quiz/UPGRADING.md)
- [mod\_wiki](https://github.com/moodle/moodle/blob/v5.0.0/mod/wiki/UPGRADING.md)
- [qbank](https://github.com/moodle/moodle/blob/v5.0.0/question/bank/UPGRADING.md)
- [qbank\_bulkmove](https://github.com/moodle/moodle/blob/v5.0.0/question/bank/bulkmove/UPGRADING.md)
- [report\_insights](https://github.com/moodle/moodle/blob/v5.0.0/report/insights/UPGRADING.md)
- [report\_log](https://github.com/moodle/moodle/blob/v5.0.0/report/log/UPGRADING.md)
- [theme\_boost](https://github.com/moodle/moodle/blob/v5.0.0/theme/boost/UPGRADING.md)
- [tool\_admin\_presets](https://github.com/moodle/moodle/blob/v5.0.0/admin/tool/admin_presets/UPGRADING.md)
- [tool\_behat](https://github.com/moodle/moodle/blob/v5.0.0/admin/tool/behat/UPGRADING.md)
- [tool\_brickfield](https://github.com/moodle/moodle/blob/v5.0.0/admin/tool/brickfield/UPGRADING.md)
- [tool\_lp](https://github.com/moodle/moodle/blob/v5.0.0/admin/tool/lp/UPGRADING.md)
- [tool\_mfa](https://github.com/moodle/moodle/blob/v5.0.0/admin/tool/mfa/UPGRADING.md)
- [tool\_mobile](https://github.com/moodle/moodle/blob/v5.0.0/admin/tool/mobile/UPGRADING.md)