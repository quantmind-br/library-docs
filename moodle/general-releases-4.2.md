---
title: Moodle 4.2 | Moodle Developer Resources
url: https://moodledev.io/general/releases/4.2
source: sitemap
fetched_at: 2026-02-17T16:15:45.622305-03:00
rendered_js: false
word_count: 1524
summary: This document provides the release notes for Moodle 4.2.0, detailing the minimum server and database requirements, browser compatibility, and significant feature enhancements.
tags:
    - moodle-release
    - server-requirements
    - php-compatibility
    - database-requirements
    - ux-improvements
    - browser-support
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 24 April 2023

Here is [the full list of fixed issues in 4.2.0](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%224.2%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

If you are upgrading from a previous version, please see [Upgrading](https://docs.moodle.org/en/Upgrading) in the user docs.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software and operating systems up-to-date.

- Moodle upgrade: Moodle 3.11.8 or later.
- PHP version: minimum PHP 8.0.0 *Note: minimum PHP version has increased since Moodle 4.1*. PHP 8.2.x is supported too (since Moodle 4.2.3). See [PHP](https://moodledev.io/general/development/policies/php) for details.
- PHP extension **sodium** is required. See [Environment - PHP extension sodium](https://docs.moodle.org/en/Environment_-_PHP_extension_sodium).
- PHP extension **exif** is recommended.
- PHP setting **max\_input\_vars** must be &gt;= 5000. For further details, see [Environment - max input vars](https://docs.moodle.org/en/Environment_-_max_input_vars).
- PHP variants: Only 64-bit versions of PHP are supported. *Note: Changed since 4.1*.

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)13 (increased since Moodle 4.1)Latest[MySQL](http://www.mysql.com/)8.0 (increased since Moodle 4.1)Latest[MariaDB](https://mariadb.org/)10.6.7 (increased since Moodle 4.1)Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2017Latest[Oracle Database](http://www.oracle.com/us/products/database/overview/index.html)19Latest

## Client requirements[​](#client-requirements "Direct link to Client requirements")

### Browser support[​](#browser-support "Direct link to Browser support")

Moodle is compatible with any standards compliant web browser. We regularly test Moodle with the following browsers:

Desktop:

- Chrome
- Firefox
- Safari
- Edge

info

Note: Moodle 4.2 does NOT support Internet Explorer.

Mobile:

- MobileSafari
- Google Chrome

For the best experience and optimum security, we recommend that you keep your browser up to date.

## Major UX improvements[​](#major-ux-improvements "Direct link to Major UX improvements")

### Gradebook[​](#gradebook "Direct link to Gradebook")

- [MDL-77030](https://moodle.atlassian.net/browse/MDL-77030) - Display feedback in the Grader report
- [MDL-76149](https://moodle.atlassian.net/browse/MDL-76149) - Implement "records per page" selector in the Grader report
- [MDL-75274](https://moodle.atlassian.net/browse/MDL-75274) - Ability to collapse/expand items (columns) in the Grader report
- [MDL-76147](https://moodle.atlassian.net/browse/MDL-76147) - Implement dropdown menu for the header actions in the Grader report table
- [MDL-77029](https://moodle.atlassian.net/browse/MDL-77029) - Revamp the column sorting in the Grader report
- [MDL-77032](https://moodle.atlassian.net/browse/MDL-77032) - Collapsible grade categories in the Gradebook setup
- [MDL-76143](https://moodle.atlassian.net/browse/MDL-76143) - Implement search functionality in the Grader report
- [MDL-77033](https://moodle.atlassian.net/browse/MDL-77033) - Indicators when the state of a grade item or category is changed in the Gradebook setup
- [MDL-76150](https://moodle.atlassian.net/browse/MDL-76150) - General styling improvements to the Grader report
- [MDL-76146](https://moodle.atlassian.net/browse/MDL-76146) - Move grade actions (hide, show, lock, grade analysis) to dropdown menu in the Grader report table
- [MDL-77031](https://moodle.atlassian.net/browse/MDL-77031) - General styling improvements to the Gradebook setup
- [MDL-76139](https://moodle.atlassian.net/browse/MDL-76139) - Implement a new group selector in the Grader report

### Database activity[​](#database-activity "Direct link to Database activity")

- [MDL-76360](https://moodle.atlassian.net/browse/MDL-76360) - Improve the look and feel of the Database fields page
- [MDL-76357](https://moodle.atlassian.net/browse/MDL-76357) - Make sticky footer more prominent and noticeable
- [MDL-75498](https://moodle.atlassian.net/browse/MDL-75498) - Add ##otherfields##, \[\[FIELD#name]] and \[\[FIELD#description]] tags to the database templates
- [MDL-75337](https://moodle.atlassian.net/browse/MDL-75337) - Change Delete buttons' style on Database to 'danger' button

### Course hierarchy[​](#course-hierarchy "Direct link to Course hierarchy")

- [MDL-76990](https://moodle.atlassian.net/browse/MDL-76990) - Recover move right/left functionality removed/hidden for 4.0
- [MDL-76997](https://moodle.atlassian.net/browse/MDL-76997) - Add an option for admins to reset indentation for courses on the site
- [MDL-76992](https://moodle.atlassian.net/browse/MDL-76992) - Apply indentation on the course index
- [MDL-76991](https://moodle.atlassian.net/browse/MDL-76991) - New course format setting to enable/disable course indentation in Weeks and Topics

## Other Major features[​](#other-major-features "Direct link to Other Major features")

### TinyMCE 6 improvements and setting as the default editor[​](#tinymce-6-improvements-and-setting-as-the-default-editor "Direct link to TinyMCE 6 improvements and setting as the default editor")

- [MDL-76866](https://moodle.atlassian.net/browse/MDL-76866) - Make TinyMCE the default editor
- [MDL-77308](https://moodle.atlassian.net/browse/MDL-77308) - Remove the legacy TinyMCE editor from core (editor\_tinymce)
- [MDL-76867](https://moodle.atlassian.net/browse/MDL-76867) - Allow Moodle TinyMCE plugins to be disabled
- [MDL-76520](https://moodle.atlassian.net/browse/MDL-76520) - Add a TinyMCE link plugin

### MoodleNet integration - phase 1[​](#moodlenet-integration---phase-1 "Direct link to MoodleNet integration - phase 1")

- [MDL-75316](https://moodle.atlassian.net/browse/MDL-75316) - Implement LMS foundation for sharing content to MoodleNet (share activities)
- [MDL-75650](https://moodle.atlassian.net/browse/MDL-75650) - Add OAuth 2.0 Authorization Server Metadata support to issuers and create MoodleNet issuer

### Bulk course activity editing[​](#bulk-course-activity-editing "Direct link to Bulk course activity editing")

- [MDL-76783](https://moodle.atlassian.net/browse/MDL-76783) - The basic bulk section and activity selection UI
- [MDL-76850](https://moodle.atlassian.net/browse/MDL-76850) - Add bulk duplicate activity action
- [MDL-76893](https://moodle.atlassian.net/browse/MDL-76893) - Add bulk activity move action
- [MDL-76848](https://moodle.atlassian.net/browse/MDL-76848) - Add bulk availability edit action
- [MDL-76894](https://moodle.atlassian.net/browse/MDL-76894) - Add bulk section move
- [MDL-76895](https://moodle.atlassian.net/browse/MDL-76895) - Add fast selections to the bulk editing
- [MDL-76851](https://moodle.atlassian.net/browse/MDL-76851) - Add bulk delete action
- [MDL-74989](https://moodle.atlassian.net/browse/MDL-74989) - Migrate delete activity course tools to the new reactive actions
- [MDL-74987](https://moodle.atlassian.net/browse/MDL-74987) - Migrate duplicate activity course tools to the new reactive actions

### BigBlueButton[​](#bigbluebutton "Direct link to BigBlueButton")

- [MDL-74664](https://moodle.atlassian.net/browse/MDL-74664) - Option to restrict recording formats viewable by everyone
- [MDL-75753](https://moodle.atlassian.net/browse/MDL-75753) - Add support for SHA256 (and longer) to BigBlueButton
- [MDL-76551](https://moodle.atlassian.net/browse/MDL-76551) - Option to show profile pictures of participants in BBB sessions
- [MDL-75334](https://moodle.atlassian.net/browse/MDL-75334) - Create a set of test courses which include BigBlueButton activities

### Quiz and questions[​](#quiz-and-questions "Direct link to Quiz and questions")

- [MDL-35745](https://moodle.atlassian.net/browse/MDL-35745) - There must be a way to get a "Never submitted" quiz attempt back to the "In progress" state
- [MDL-74609](https://moodle.atlassian.net/browse/MDL-74609) - Quiz: allow the displayed question numbers to be customised
- [MDL-71261](https://moodle.atlassian.net/browse/MDL-71261) - Quiz user override should only get enrolled users

### Report builder[​](#report-builder "Direct link to Report builder")

- [MDL-77056](https://moodle.atlassian.net/browse/MDL-77056) - Add relative date filter option to select dates before given period
- [MDL-74145](https://moodle.atlassian.net/browse/MDL-74145) - Create API for report bulk actions
- [MDL-76154](https://moodle.atlassian.net/browse/MDL-76154) - Add files to custom blog reporting
- [MDL-77062](https://moodle.atlassian.net/browse/MDL-77062) - Add more filters/conditions fields in course\_completion entity
- [MDL-77201](https://moodle.atlassian.net/browse/MDL-77201) - Allow report column callbacks to define how aggregated data is displayed
- [MDL-76479](https://moodle.atlassian.net/browse/MDL-76479) - Custom report time filter should support last/current/next hour
- [MDL-76933](https://moodle.atlassian.net/browse/MDL-76933) - Create "User badges" custom report source

### Content bank and H5P[​](#content-bank-and-h5p "Direct link to Content bank and H5P")

- [MDL-67789](https://moodle.atlassian.net/browse/MDL-67789) - Add support to "Save content state" in mod\_h5pactivity
- [MDL-77049](https://moodle.atlassian.net/browse/MDL-77049) - Customise H5P styles via Raw SCSS theme setting

### Assignment[​](#assignment "Direct link to Assignment")

- [MDL-45301](https://moodle.atlassian.net/browse/MDL-45301) - Option to set PDF font in course settings for generated PDF files
- [MDL-55929](https://moodle.atlassian.net/browse/MDL-55929) - Messaging from Assignment

### Usability improvements[​](#usability-improvements "Direct link to Usability improvements")

- [MDL-75596](https://moodle.atlassian.net/browse/MDL-75596) - Adding new activities should be possible anywhere in a section
- [MDL-62839](https://moodle.atlassian.net/browse/MDL-62839) - Deselect "Accept grades from this tool" by default for new LTI instances
- [MDL-75908](https://moodle.atlassian.net/browse/MDL-75908) - Links added in the navbar should receive focus/active behaviour (custommenuitems) on the Boost theme
- [MDL-31235](https://moodle.atlassian.net/browse/MDL-31235) - Support text format for marking guide criteria and levels
- [MDL-40600](https://moodle.atlassian.net/browse/MDL-40600) - Add ability to duplicate a course section
- [MDL-74465](https://moodle.atlassian.net/browse/MDL-74465) - Display block configuration form in a popup
- [MDL-68347](https://moodle.atlassian.net/browse/MDL-68347) - Add a way to find which users were created during course restore process
- [MDL-76377](https://moodle.atlassian.net/browse/MDL-76377) - Improve links to moodle.org / moodle.academy (course creators/teachers)
- [MDL-76418](https://moodle.atlassian.net/browse/MDL-76418) - Have a way to get the permalink to a course section

## Other Highlights[​](#other-highlights "Direct link to Other Highlights")

### Functional changes[​](#functional-changes "Direct link to Functional changes")

- [MDL-74272](https://moodle.atlassian.net/browse/MDL-74272) - Reassess the inclusion of the plugin name on the course page
- [MDL-77291](https://moodle.atlassian.net/browse/MDL-77291) - Show text and media elements (aka labels) in the course index also in non edit mode
- [MDL-75594](https://moodle.atlassian.net/browse/MDL-75594) - Change course module creation to support parameter for inserting modules at any place in the section
- [MDL-77387](https://moodle.atlassian.net/browse/MDL-77387) - Copy course UI - enrol a user such as editingteacher in the copied course
- [MDL-76312](https://moodle.atlassian.net/browse/MDL-76312) - Subscribers list should ordered by name
- [MDL-76386](https://moodle.atlassian.net/browse/MDL-76386) - Provide option to have group count before names when adding users to group
- [MDL-77130](https://moodle.atlassian.net/browse/MDL-77130) - Add cohort custom fields functionality
- [MDL-70226](https://moodle.atlassian.net/browse/MDL-70226) - Default tab in the activity chooser should be recommended activities

### For administrators[​](#for-administrators "Direct link to For administrators")

- [MDL-68093](https://moodle.atlassian.net/browse/MDL-68093) - Membership in some groups should be hidden from some roles for FERPA/ADA compliance
- [MDL-77406](https://moodle.atlassian.net/browse/MDL-77406) - Log every time a user adds a file to a draft area
- [MDL-73503](https://moodle.atlassian.net/browse/MDL-73503) - Add filtering by section to report\_progress
- [MDL-65471](https://moodle.atlassian.net/browse/MDL-65471) - Optionally allow CLI PHP upgrade.php --no-outage
- [MDL-77370](https://moodle.atlassian.net/browse/MDL-77370) - New setting for the "Services and support" URL
- [MDL-74874](https://moodle.atlassian.net/browse/MDL-74874) - Mark readonly sessions as no longer experimental
- [MDL-61789](https://moodle.atlassian.net/browse/MDL-61789) - Allow to choose custom profile fields from OAuth 2 field mappings
- [MDL-70975](https://moodle.atlassian.net/browse/MDL-70975) - Add new options to admin/cli/adhoc\_task.php and from admin web UI
- [MDL-77385](https://moodle.atlassian.net/browse/MDL-77385) - CLI Script to enable or disable the emailstop flag
- [MDL-64153](https://moodle.atlassian.net/browse/MDL-64153) - Allow administrator to override sqlsrv connection options
- [MDL-72775](https://moodle.atlassian.net/browse/MDL-72775) - Add a new status check for the cron task API to watch very long running tasks

### Performance[​](#performance "Direct link to Performance")

- [MDL-70687](https://moodle.atlassian.net/browse/MDL-70687) - Redis session lock expiration should default shorter than session timeout
- [MDL-77232](https://moodle.atlassian.net/browse/MDL-77232) - Optimize LTI 1.3 gradesync task
- [MDL-72559](https://moodle.atlassian.net/browse/MDL-72559) - The core plugin\_functions cache should be allowed to be stored locally
- [MDL-77186](https://moodle.atlassian.net/browse/MDL-77186) - Add a keep-alive setting to admin/cli/cron.php
- [MDL-76129](https://moodle.atlassian.net/browse/MDL-76129) - Improve upgrade/install performance relating to capabilities and settings
- [MDL-75667](https://moodle.atlassian.net/browse/MDL-75667) - Improve speed of admin/blocks.php by combining db counts

## Security improvements[​](#security-improvements "Direct link to Security improvements")

- [MDL-76722](https://moodle.atlassian.net/browse/MDL-76722) - Add encrypted mobile notifications support (also see [MDL-77893](https://moodle.atlassian.net/browse/MDL-77893))
- [MDL-76755](https://moodle.atlassian.net/browse/MDL-76755) - Improve default coverage of "cURL blocked hosts list" by including 127.0.0.0/8

## For developers[​](#for-developers "Direct link to For developers")

- [MDL-76135](https://moodle.atlassian.net/browse/MDL-76135) - Import the Guzzle library in LMS
- [MDL-76989](https://moodle.atlassian.net/browse/MDL-76989) - Upgrade Font Awesome to 6.3.0
- [MDL-76219](https://moodle.atlassian.net/browse/MDL-76219) - Switch from Box/Spout to OpenSpout/OpenSpout
- [MDL-73144](https://moodle.atlassian.net/browse/MDL-73144) - Allow use of dartsass for scss compilation
- [MDL-76134](https://moodle.atlassian.net/browse/MDL-76134) - Build a reusable filter output component
- [MDL-71096](https://moodle.atlassian.net/browse/MDL-71096) - All APIs should be listed in code
- [MDL-77714](https://moodle.atlassian.net/browse/MDL-77714) - Remove Travis support from core
- [MDL-72609](https://moodle.atlassian.net/browse/MDL-72609) - Convert pendingPromise to native Promise
- [MDL-76583](https://moodle.atlassian.net/browse/MDL-76583) - Move lib/externallib.php to namespaced classes and fix coding style, etc

### Migration away from YUI3[​](#migration-away-from-yui3 "Direct link to Migration away from YUI3")

- [MDL-77172](https://moodle.atlassian.net/browse/MDL-77172) - Migrate moodle-tool\_capability-search to ESM
- [MDL-77171](https://moodle.atlassian.net/browse/MDL-77171) - Migrate moodle-core-tooltip and moodle-core-popuphelp to ESM
- [MDL-77009](https://moodle.atlassian.net/browse/MDL-77009) - Replace moodle-tool\_monitor-dropdown with ESM or generic
- [MDL-58615](https://moodle.atlassian.net/browse/MDL-58615) - Remove YUI CDN support
- [MDL-77007](https://moodle.atlassian.net/browse/MDL-77007) - Remove auth-passwordunmask YUI module
- [MDL-69164](https://moodle.atlassian.net/browse/MDL-69164) - Convert question/qengine.js to AMD modules

### Web service additions and updates[​](#web-service-additions-and-updates "Direct link to Web service additions and updates")

- [MDL-77643](https://moodle.atlassian.net/browse/MDL-77643) - Return via tool\_mobile\_get\_config site location settings to properly display the user time zone in the app

### Core plugins removed[​](#core-plugins-removed "Direct link to Core plugins removed")

- [MDL-72350](https://moodle.atlassian.net/browse/MDL-72350) - Remove Assignment 2.2 (mod\_assignment) from core
- [MDL-77163](https://moodle.atlassian.net/browse/MDL-77163) - Remove cachestore\_mongodb from core
- [MDL-77161](https://moodle.atlassian.net/browse/MDL-77161) - Remove cachestore\_memcached from core

### Deprecations[​](#deprecations "Direct link to Deprecations")

- [MDL-52805](https://moodle.atlassian.net/browse/MDL-52805) - Final deprecation of legacy log store
- [MDL-76898](https://moodle.atlassian.net/browse/MDL-76898) - Quiz: final deprecations for things deprecated before 3.10

### Component API updates[​](#component-api-updates "Direct link to Component API updates")

- [admin/tool/generator/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Ftool%2Fgenerator%2Fupgrade.txt)
- [admin/tool/lp/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Ftool%2Flp%2Fupgrade.txt)
- [admin/tool/mobile/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Ftool%2Fmobile%2Fupgrade.txt)
- [admin/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Fupgrade.txt)
- [analytics/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Danalytics%2Fupgrade.txt)
- [auth/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dauth%2Fupgrade.txt)
- [availability/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Davailability%2Fupgrade.txt)
- [blocks/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dblocks%2Fupgrade.txt)
- [cache/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcache%2Fupgrade.txt)
- [cohort/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcohort%2Fupgrade.txt)
- [comment/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcomment%2Fupgrade.txt)
- [course/format/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcourse%2Fformat%2Fupgrade.txt)
- [course/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcourse%2Fupgrade.txt)
- [customfield/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcustomfield%2Fupgrade.txt)
- [enrol/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Denrol%2Fupgrade.txt)
- [grade/report/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dgrade%2Freport%2Fupgrade.txt)
- [group/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dgroup%2Fupgrade.txt)
- [lib/editor/tinymce/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Feditor%2Ftinymce%2Fupgrade.txt)
- [lib/editor/tiny/plugins/accessibilitychecker/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Feditor%2Ftiny%2Fplugins%2Faccessibilitychecker%2Fupgrade.txt)
- [lib/editor/tiny/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Feditor%2Ftiny%2Fupgrade.txt)
- [lib/form/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Fform%2Fupgrade.txt)
- [lib/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Fupgrade.txt)
- [lib/xapi/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Fxapi%2Fupgrade.txt)
- [message/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmessage%2Fupgrade.txt)
- [mod/assignment/type/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fassignment%2Ftype%2Fupgrade.txt)
- [mod/assign/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fassign%2Fupgrade.txt)
- [mod/bigbluebuttonbn/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fbigbluebuttonbn%2Fupgrade.txt)
- [mod/data/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fdata%2Fupgrade.txt)
- [mod/feedback/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Ffeedback%2Fupgrade.txt)
- [mod/h5pactivity/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fh5pactivity%2Fupgrade.txt)
- [mod/lti/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Flti%2Fupgrade.txt)
- [mod/quiz/accessrule/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fquiz%2Faccessrule%2Fupgrade.txt)
- [mod/quiz/report/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fquiz%2Freport%2Fupgrade.txt)
- [mod/quiz/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fquiz%2Fupgrade.txt)
- [mod/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fupgrade.txt)
- [mod/workshop/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fworkshop%2Fupgrade.txt)
- [plagiarism/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dplagiarism%2Fupgrade.txt)
- [question/engine/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dquestion%2Fengine%2Fupgrade.txt)
- [question/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dquestion%2Fupgrade.txt)
- [reportbuilder/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dreportbuilder%2Fupgrade.txt)
- [report/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dreport%2Fupgrade.txt)
- [search/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dsearch%2Fupgrade.txt)
- [theme/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dtheme%2Fupgrade.txt)
- [user/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Duser%2Fupgrade.txt)
- [webservice/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dwebservice%2Fupgrade.txt)