---
title: Moodle 4.3 | Moodle Developer Resources
url: https://moodledev.io/general/releases/4.3
source: sitemap
fetched_at: 2026-02-17T16:16:09.631809-03:00
rendered_js: false
word_count: 2245
summary: This document outlines the technical requirements, supported software versions, and major feature updates for Moodle 4.3, including UX improvements and new integration capabilities.
tags:
    - moodle-4-3
    - release-notes
    - server-requirements
    - database-compatibility
    - ux-improvements
    - gradebook
    - lti-tools
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 9 October 2023

Here is [the full list of fixed issues in 4.3.0](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%224.3%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

If you are upgrading from a previous version, please see [Upgrading](https://docs.moodle.org/en/Upgrading) in the user docs.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software and operating systems up-to-date.

- Moodle upgrade: Moodle 3.11.8 or later.
- PHP version: minimum PHP 8.0.0 *Note: minimum PHP version has increased since Moodle 4.1*. PHP 8.2.x is supported too. See [PHP](https://moodledev.io/general/development/policies/php) for details.
- PHP extension **sodium** is required. See [Environment - PHP extension sodium](https://docs.moodle.org/en/Environment_-_PHP_extension_sodium).
- PHP setting **max\_input\_vars** must be &gt;= 5000. For further details, see [Environment - max input vars](https://docs.moodle.org/en/Environment_-_max_input_vars).
- PHP variants: Only 64-bit versions of PHP are supported. *Note: Changed since 4.1*.

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)13 (increased since Moodle 4.1)Latest[MySQL](http://www.mysql.com/)8.0 (increased since Moodle 4.1)Latest[MariaDB](https://mariadb.org/)10.6.7 (increased since Moodle 4.1)Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2017Latest[Oracle Database](http://www.oracle.com/us/products/database/overview/index.html)19Latest

Note that, since Moodle 4.3, the maximum length for the database prefix (`$CFG->prefix`) is 10 characters. Installation or upgrade won't be possible with longer prefixes.

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

### Gradebook[​](#gradebook "Direct link to Gradebook")

- [MDL-77638](https://moodle.atlassian.net/browse/MDL-77638) - Create a modal form for basic addition of grade categories in Gradebook setup
- [MDL-78217](https://moodle.atlassian.net/browse/MDL-78217) - Improve the overriding of weights in the Gradebook setup
- [MDL-77447](https://moodle.atlassian.net/browse/MDL-77447) - Make the grade item status indicators consistent across the Gradebook reports
- [MDL-77639](https://moodle.atlassian.net/browse/MDL-77639) - Create a modal form for basic addition of outcomes in Gradebook setup
- [MDL-77035](https://moodle.atlassian.net/browse/MDL-77035) - Improve the UI related to the bulk move functionality in Gradebook setup
- [MDL-77637](https://moodle.atlassian.net/browse/MDL-77637) - Create a modal form for basic addition of grade item in Gradebook setup
- [MDL-78100](https://moodle.atlassian.net/browse/MDL-78100) - Add an option to clear all applied filters in the grader report

### Activity cards redesign[​](#activity-cards-redesign "Direct link to Activity cards redesign")

- [MDL-78283](https://moodle.atlassian.net/browse/MDL-78283) - Add radio dropdown interaction to group mode icon
- [MDL-78279](https://moodle.atlassian.net/browse/MDL-78279) - Create new details dropdown components
- [MDL-78282](https://moodle.atlassian.net/browse/MDL-78282) - Add radio dropdown interaction to availability badge
- [MDL-78280](https://moodle.atlassian.net/browse/MDL-78280) - Add details dropdown to completion criteria badge
- [MDL-78288](https://moodle.atlassian.net/browse/MDL-78288) - Add access restriction quickform direct link button to restrictions details dropdown
- [MDL-78200](https://moodle.atlassian.net/browse/MDL-78200) - Add the group mode indicator to the activity card
- [MDL-78954](https://moodle.atlassian.net/browse/MDL-78954) - Improve action menu subpanel aesthetics and effects
- [MDL-78826](https://moodle.atlassian.net/browse/MDL-78826) - Improve accessibility of keyboard control for the generic dropdowns
- [MDL-78607](https://moodle.atlassian.net/browse/MDL-78607) - Improve section and activity settings form to load access restrictions
- [MDL-78665](https://moodle.atlassian.net/browse/MDL-78665) - Create a generic submenu for status selection
- [MDL-78286](https://moodle.atlassian.net/browse/MDL-78286) - Add completion quickform direct link button to completion details dropdown
- [MDL-78207](https://moodle.atlassian.net/browse/MDL-78207) - Implement activity card information badge integration
- [MDL-78203](https://moodle.atlassian.net/browse/MDL-78203) - Add group mode option to activity actions submenu
- [MDL-78201](https://moodle.atlassian.net/browse/MDL-78201) - Create the groupmode state actions
- [MDL-78199](https://moodle.atlassian.net/browse/MDL-78199) - Improve activity card styling
- [MDL-78744](https://moodle.atlassian.net/browse/MDL-78744) - Refactor 'activity\_information' output class
- [MDL-78289](https://moodle.atlassian.net/browse/MDL-78289) - Improve the student completion criteria display format
- [MDL-78204](https://moodle.atlassian.net/browse/MDL-78204) - Add "show more" / "show less" options for access restrictions on course page
- [MDL-78291](https://moodle.atlassian.net/browse/MDL-78291) - Modify the availability activity action menu to open in a subpanel

## Other major features[​](#other-major-features "Direct link to Other major features")

### Messaging phase 1 - Integrate chat services[​](#messaging-phase-1---integrate-chat-services "Direct link to Messaging phase 1 - Integrate chat services")

- [MDL-77576](https://moodle.atlassian.net/browse/MDL-77576) - Matrix integration MVP - Matrix is available for use in courses
- [MDL-78619](https://moodle.atlassian.net/browse/MDL-78619) - Add a custom link communication provider
- [MDL-76704](https://moodle.atlassian.net/browse/MDL-76704) - Admin settings to control Matrix room creation for Courses
- [MDL-77357](https://moodle.atlassian.net/browse/MDL-77357) - Create dynamic form fields feature for communication plugins
- [MDL-77252](https://moodle.atlassian.net/browse/MDL-77252) - Add banners to indicate room creation status to teachers
- [MDL-78129](https://moodle.atlassian.net/browse/MDL-78129) - Allow teachers, managers and admins to moderate their courses' Matrix rooms
- [MDL-77917](https://moodle.atlassian.net/browse/MDL-77917) - Allow versioned APIs for clients in Matrix provider

### LTI external tools - Improve configuration and management in courses[​](#lti-external-tools---improve-configuration-and-management-in-courses "Direct link to LTI external tools - Improve configuration and management in courses")

- [MDL-78575](https://moodle.atlassian.net/browse/MDL-78575) - Centralised page to view and manage preconfigured LTI external tools in a course
- [MDL-78909](https://moodle.atlassian.net/browse/MDL-78909) - Enable setting whether a preconfigured tool appears in the activity chooser in a course
- [MDL-78916](https://moodle.atlassian.net/browse/MDL-78916) - Simplify the creation of an LTI external tool activity in a course
- [MDL-78576](https://moodle.atlassian.net/browse/MDL-78576) - Improve deletion of course preconfigured LTI tools

### Multi-factor Authentication[​](#multi-factor-authentication "Direct link to Multi-factor Authentication")

- [MDL-78509](https://moodle.atlassian.net/browse/MDL-78509) - MFA in core
- [MDL-78534](https://moodle.atlassian.net/browse/MDL-78534) - Improve 2nd factor verify flow
- [MDL-79051](https://moodle.atlassian.net/browse/MDL-79051) - Improve email template

### MoodleNet integration - Phase 2[​](#moodlenet-integration---phase-2 "Direct link to MoodleNet integration - Phase 2")

- [MDL-75318](https://moodle.atlassian.net/browse/MDL-75318) - Allow teachers to share courses to MoodleNet (all activities)
- [MDL-78267](https://moodle.atlassian.net/browse/MDL-78267) - Add ability for teachers to customise courses shared to MoodleNet
- [MDL-75502](https://moodle.atlassian.net/browse/MDL-75502) - Implement share progress page for content shared to MoodleNet
- [MDL-77296](https://moodle.atlassian.net/browse/MDL-77296) - Record MoodleNet share progress data in a consumable format

### Default site completion criteria settings[​](#default-site-completion-criteria-settings "Direct link to Default site completion criteria settings")

- [MDL-78528](https://moodle.atlassian.net/browse/MDL-78528) - Redesign the Default activity completion page
- [MDL-78517](https://moodle.atlassian.net/browse/MDL-78517) - Homogenise the course completion conditions
- [MDL-78531](https://moodle.atlassian.net/browse/MDL-78531) - Create a new 'Courses &gt; Default settings' section in Site administration
- [MDL-78530](https://moodle.atlassian.net/browse/MDL-78530) - Consider the default site completion settings during activity creation
- [MDL-78527](https://moodle.atlassian.net/browse/MDL-78527) - Improve the completion conditions form
- [MDL-78633](https://moodle.atlassian.net/browse/MDL-78633) - Use tertiary navigation selector in Course completion settings
- [MDL-79093](https://moodle.atlassian.net/browse/MDL-79093) - Order activities by display name in Default activity completion

### TinyMCE 6[​](#tinymce-6 "Direct link to TinyMCE 6")

- [MDL-75268](https://moodle.atlassian.net/browse/MDL-75268) - Create TinyMCE Premium plugins integration
- [MDL-78613](https://moodle.atlassian.net/browse/MDL-78613) - Add source code formatting and styling
- [MDL-75963](https://moodle.atlassian.net/browse/MDL-75963) - Add "Code highlighter" filter to display coding style properly
- [MDL-77979](https://moodle.atlassian.net/browse/MDL-77979) - TinyMCE tool for preventing auto-linking
- [MDL-79066](https://moodle.atlassian.net/browse/MDL-79066) - Add fullscreen button

### BigBlueButton[​](#bigbluebutton "Direct link to BigBlueButton")

- [MDL-76710](https://moodle.atlassian.net/browse/MDL-76710) - Add support for BigBlueButton Subplugins
- [MDL-78062](https://moodle.atlassian.net/browse/MDL-78062) - Add backup support for BigBlueButton Subplugins
- [MDL-78960](https://moodle.atlassian.net/browse/MDL-78960) - BigBlueButton Subplugin : allow action\_url\_addons to know about the instance

### Quiz and questions[​](#quiz-and-questions "Direct link to Quiz and questions")

- [MDL-76629](https://moodle.atlassian.net/browse/MDL-76629) - Add sticky student name column in Quiz results table
- [MDL-74054](https://moodle.atlassian.net/browse/MDL-74054) - Give teachers more flexibility to customise their own view of the question bank
- [MDL-72321](https://moodle.atlassian.net/browse/MDL-72321) - Better searching/filtering in the question bank, so more flexible randomisation in quizzes
- [MDL-77218](https://moodle.atlassian.net/browse/MDL-77218) - Quiz/questions preview: explanatory text that preview settings only affect the preview
- [MDL-77564](https://moodle.atlassian.net/browse/MDL-77564) - Quiz display options: make it possible to completely hide the grade information
- [MDL-77127](https://moodle.atlassian.net/browse/MDL-77127) - Allow students to hide the timer in a timed quiz
- [MDL-77745](https://moodle.atlassian.net/browse/MDL-77745) - Anywhere a teacher views questions, display version information
- [MDL-78823](https://moodle.atlassian.net/browse/MDL-78823) - Implement qbank plugin enabled/disabled events
- [MDL-77872](https://moodle.atlassian.net/browse/MDL-77872) - Increase the width of Quiz editing page to improve usability

### Report builder[​](#report-builder "Direct link to Report builder")

- [MDL-78117](https://moodle.atlassian.net/browse/MDL-78117) - Create a custom report filter on context level
- [MDL-76471](https://moodle.atlassian.net/browse/MDL-76471) - Create a report builder filter for "enrolment name"
- [MDL-76900](https://moodle.atlassian.net/browse/MDL-76900) - Separate course participant enrol/role elements to new report entities
- [MDL-78879](https://moodle.atlassian.net/browse/MDL-78879) - Support "not" / inversion of category conditions in report builder
- [MDL-75810](https://moodle.atlassian.net/browse/MDL-75810) - Add tag support to badges custom report source
- [MDL-76902](https://moodle.atlassian.net/browse/MDL-76902) - Create "Course categories" custom report source
- [MDL-78755](https://moodle.atlassian.net/browse/MDL-78755) - Course participants report source should show active enrolments by default
- [MDL-77700](https://moodle.atlassian.net/browse/MDL-77700) - Include user in custom report for comments on blog entries
- [MDL-76295](https://moodle.atlassian.net/browse/MDL-76295) - Implement default report sorting in all report sources
- [MDL-78835](https://moodle.atlassian.net/browse/MDL-78835) - Include custom fields in report group/grouping entities
- [MDL-78741](https://moodle.atlassian.net/browse/MDL-78741) - Allow reporting/filtering on context path and parent
- [MDL-77532](https://moodle.atlassian.net/browse/MDL-77532) - Include custom fields in cohort report entity
- [MDL-77061](https://moodle.atlassian.net/browse/MDL-77061) - Add search and filter function in Manage Badges page
- [MDL-78532](https://moodle.atlassian.net/browse/MDL-78532) - Create a new Web Service to retrieve system reports (core\_reportbuilder\_retrieve\_system\_report)
- [MDL-77067](https://moodle.atlassian.net/browse/MDL-77067) - Indicate where report audiences are used in schedules
- [MDL-77614](https://moodle.atlassian.net/browse/MDL-77614) - Reports shouldn't allow adding new entities whose name was already added

### Content bank and H5P[​](#content-bank-and-h5p "Direct link to Content bank and H5P")

- [MDL-76338](https://moodle.atlassian.net/browse/MDL-76338) - Enable content to be copied in content bank
- [MDL-77667](https://moodle.atlassian.net/browse/MDL-77667) - Display full course name in content bank for selection
- [MDL-74773](https://moodle.atlassian.net/browse/MDL-74773) - Contentbank: add notification when updating

### Accessibility improvements[​](#accessibility-improvements "Direct link to Accessibility improvements")

- [MDL-75762](https://moodle.atlassian.net/browse/MDL-75762) - Retain course page position when pressing back button from activity/resource
- [MDL-74869](https://moodle.atlassian.net/browse/MDL-74869) - Activity icon colours should be SCSS variables so they are easy to override

### Usability improvements[​](#usability-improvements "Direct link to Usability improvements")

- [MDL-71212](https://moodle.atlassian.net/browse/MDL-71212) - Add course kebab menu with 'Collapse all' and 'Expand all' options to course index
- [MDL-78474](https://moodle.atlassian.net/browse/MDL-78474) - Enable users to personalise the name for the resource "Text and media area"
- [MDL-76203](https://moodle.atlassian.net/browse/MDL-76203) - Add support for BDI tag in HTML Purifier
- [MDL-74679](https://moodle.atlassian.net/browse/MDL-74679) - Allow students to send Q&A forum post notifications with no editing-time delay
- [MDL-77793](https://moodle.atlassian.net/browse/MDL-77793) - Remove the legacy theme selector
- [MDL-63759](https://moodle.atlassian.net/browse/MDL-63759) - Replace geoIP lookup with openstreetmap
- [MDL-76982](https://moodle.atlassian.net/browse/MDL-76982) - Add floating previous/next buttons to navigate book chapters
- [MDL-73464](https://moodle.atlassian.net/browse/MDL-73464) - Focus on chapter content when navigating to next/previous Book chapter
- [MDL-76270](https://moodle.atlassian.net/browse/MDL-76270) - Enable/disable group messaging in bulk
- [MDL-78184](https://moodle.atlassian.net/browse/MDL-78184) - Improve user flow for connecting to a open badges backpack
- [MDL-44190](https://moodle.atlassian.net/browse/MDL-44190) - Select current course by default when restoring a single activity from within a course or activity
- [MDL-78630](https://moodle.atlassian.net/browse/MDL-78630) - A notification should be displayed when a user's account is locked/unlocked
- [MDL-78579](https://moodle.atlassian.net/browse/MDL-78579) - Glossary should display number of entries pending approval
- [MDL-78503](https://moodle.atlassian.net/browse/MDL-78503) - Web service tokens: Add a Last Access column at the table view
- [MDL-79042](https://moodle.atlassian.net/browse/MDL-79042) - MathJax: Notify when we finish rendering all the equations

## Other Highlights[​](#other-highlights "Direct link to Other Highlights")

### Functional changes[​](#functional-changes "Direct link to Functional changes")

- [MDL-48762](https://moodle.atlassian.net/browse/MDL-48762) - Restrict access to course based on start and end date
- [MDL-40084](https://moodle.atlassian.net/browse/MDL-40084) - Export related files in database activity export
- [MDL-73325](https://moodle.atlassian.net/browse/MDL-73325) - Enable support for tagging badges
- [MDL-45452](https://moodle.atlassian.net/browse/MDL-45452) - Completion report: Date format for "Excel-compatible format" CSV export updated to use Excel compatible format
- [MDL-75802](https://moodle.atlassian.net/browse/MDL-75802) - A (teacher) user should not be able to un-enrol themselves via bulk un-enrolment
- [MDL-67186](https://moodle.atlassian.net/browse/MDL-67186) - Add custom fields to groups and groupings
- [MDL-73839](https://moodle.atlassian.net/browse/MDL-73839) - Allow using cohort enrolment when uploading course via CSV
- [MDL-78972](https://moodle.atlassian.net/browse/MDL-78972) - Update 'Delete' colour in activity action menu
- [MDL-78341](https://moodle.atlassian.net/browse/MDL-78341) - Improve the progress bar rendering to re-align with bootstrap
- [MDL-78175](https://moodle.atlassian.net/browse/MDL-78175) - Move role renaming settings to a participant -&gt; enrolments page

### For administrators[​](#for-administrators "Direct link to For administrators")

- [MDL-69489](https://moodle.atlassian.net/browse/MDL-69489) - Enable Admins to restrict LTI Tools to specific Categories
- [MDL-77443](https://moodle.atlassian.net/browse/MDL-77443) - Event Monitor: Course and activity name variables for event monitoring rules
- [MDL-78993](https://moodle.atlassian.net/browse/MDL-78993) - Remove the $CFG-&gt;svgicons setting
- [MDL-67529](https://moodle.atlassian.net/browse/MDL-67529) - GDPR: Option to filter which courses are included in data requests
- [MDL-78312](https://moodle.atlassian.net/browse/MDL-78312) - User selectors: add an 'exact match only' option
- [MDL-77260](https://moodle.atlassian.net/browse/MDL-77260) - Make it easier to find a specific component in event monitoring tool
- [MDL-78468](https://moodle.atlassian.net/browse/MDL-78468) - Remove the legacy theme settings enabledevicedetection and devicedetectregex
- [MDL-79090](https://moodle.atlassian.net/browse/MDL-79090) - Enable and disable scheduled tasks from the CLI
- [MDL-71421](https://moodle.atlassian.net/browse/MDL-71421) - Move php-sodium recommendation back to requirement
- [MDL-78132](https://moodle.atlassian.net/browse/MDL-78132) - Improve the workflow for creating badge backpack
- [MDL-76104](https://moodle.atlassian.net/browse/MDL-76104) - Add Moodle filters support to user tours
- [MDL-78019](https://moodle.atlassian.net/browse/MDL-78019) - Log every time a user deletes a file from the draft area

### Mobile[​](#mobile "Direct link to Mobile")

- [MDL-79242](https://moodle.atlassian.net/browse/MDL-79242) - Improve the UX for first time users of the Android app via the Google Play install referrer API
- [MDL-74263](https://moodle.atlassian.net/browse/MDL-74263) - Enable guest access with password support on the app

### Performance[​](#performance "Direct link to Performance")

- [MDL-46279](https://moodle.atlassian.net/browse/MDL-46279) - Refactor SCORM database schema to improve performance
- [MDL-78212](https://moodle.atlassian.net/browse/MDL-78212) - Allow MySQL database driver to set MySQL options for MYSQLI\_CLIENT\_COMPRESS
- [MDL-77797](https://moodle.atlassian.net/browse/MDL-77797) - Make LaTeX files cached public immutable so can be served by a CDN

## Security improvements[​](#security-improvements "Direct link to Security improvements")

- [MDL-54704](https://moodle.atlassian.net/browse/MDL-54704) - SSL support for connection to Postgres and MySQL Database
- [MDL-67390](https://moodle.atlassian.net/browse/MDL-67390) - Update password hashing to SHA-512
- [MDL-72622](https://moodle.atlassian.net/browse/MDL-72622) - Support TLS connections for Redis
- [MDL-76656](https://moodle.atlassian.net/browse/MDL-76656) - Web service tokens should be read-once
- [MDL-50160](https://moodle.atlassian.net/browse/MDL-50160) - HTTP only cookies (cookiehttponly) default set to on and UI setting removed
- [MDL-67774](https://moodle.atlassian.net/browse/MDL-67774) - Specify password peppers in config.php
- [MDL-53368](https://moodle.atlassian.net/browse/MDL-53368) - Captcha available on login page
- [MDL-69958](https://moodle.atlassian.net/browse/MDL-69958) - Support /.well-known/password-change requests from password managers
- [MDL-78801](https://moodle.atlassian.net/browse/MDL-78801) - Add Auto logout settings for the mobile app
- [MDL-78698](https://moodle.atlassian.net/browse/MDL-78698) - Deprecate random\_bytes\_emulate function
- [MDL-78571](https://moodle.atlassian.net/browse/MDL-78571) - Media: Allow Vimeo do not track option
- [MDL-62401](https://moodle.atlassian.net/browse/MDL-62401) - Embed YouTube videos with nocookie extension
- [MDL-75372](https://moodle.atlassian.net/browse/MDL-75372) - Add logging for URLs which fail the cURL security helper blocking

## For developers[​](#for-developers "Direct link to For developers")

- [MDL-76405](https://moodle.atlassian.net/browse/MDL-76405) - Prepare Moodle for PHP 8.2
- [MDL-74954](https://moodle.atlassian.net/browse/MDL-74954) - Hooks as replacement for some one-to-many lib.php callbacks based on PSR-14
- [MDL-79088](https://moodle.atlassian.net/browse/MDL-79088) - Create hooks for adding items to the site primary navigation
- [MDL-79338](https://moodle.atlassian.net/browse/MDL-79338) - Add support for hook callback redirection in tests
- [MDL-79144](https://moodle.atlassian.net/browse/MDL-79144) - Allow hooks to define tags
- [MDL-77863](https://moodle.atlassian.net/browse/MDL-77863) - Convert hard coded colours to use variables to make theme customisation easier
- [MDL-43195](https://moodle.atlassian.net/browse/MDL-43195) - New Creative Commons Licenses version 4
- [MDL-32278](https://moodle.atlassian.net/browse/MDL-32278) - Lib: improve print\_object to handle recursion, produce prettier output
- [MDL-78109](https://moodle.atlassian.net/browse/MDL-78109) - Cache: Remove harmful requirelockingwrite/requirelockingread options
- [MDL-77353](https://moodle.atlassian.net/browse/MDL-77353) - Create generic core\_user functions for generating and displaying user details
- [MDL-78316](https://moodle.atlassian.net/browse/MDL-78316) - Convert IconSystem to ESM
- [MDL-74301](https://moodle.atlassian.net/browse/MDL-74301) - Upgrade Eslint and audit rules
- [MDL-78467](https://moodle.atlassian.net/browse/MDL-78467) - Cache: Improve cache locking API
- [MDL-77991](https://moodle.atlassian.net/browse/MDL-77991) - Create a new generic select and search style element
- [MDL-78266](https://moodle.atlassian.net/browse/MDL-78266) - Break core/templates into smaller, constituent parts
- [MDL-78884](https://moodle.atlassian.net/browse/MDL-78884) - Remove sized files for MIME icons and update them with new SVG files
- [MDL-79039](https://moodle.atlassian.net/browse/MDL-79039) - MathJax: Rewrite old JavaScript to AMD module
- [MDL-78934](https://moodle.atlassian.net/browse/MDL-78934) - Move from (archived) Goutte to BrowserKit
- [MDL-67271](https://moodle.atlassian.net/browse/MDL-67271) - Add missing SVG files for FontAwesome images
- [MDL-79031](https://moodle.atlassian.net/browse/MDL-79031) - Add a JavaScript event for filters to trigger when they have finished rendering
- [MDL-78306](https://moodle.atlassian.net/browse/MDL-78306) - Convert core/modal and remaining legacy uses to ESM

### Web service additions and updates[​](#web-service-additions-and-updates "Direct link to Web service additions and updates")

- [MDL-74570](https://moodle.atlassian.net/browse/MDL-74570) - New web service core\_badges\_get\_user\_badge
- [MDL-74568](https://moodle.atlassian.net/browse/MDL-74568) - New web service mod\_chat\_view\_sessions
- [MDL-78844](https://moodle.atlassian.net/browse/MDL-78844) - New web service to check access to a system report
- [MDL-56020](https://moodle.atlassian.net/browse/MDL-56020) - New Web Services for global search

### Deprecations[​](#deprecations "Direct link to Deprecations")

- [MDL-61165](https://moodle.atlassian.net/browse/MDL-61165) - Remove support for Legacy cron
- [MDL-78561](https://moodle.atlassian.net/browse/MDL-78561) - Deprecate grade\_helper:get\_lang\_string method
- [MDL-77174](https://moodle.atlassian.net/browse/MDL-77174) - Deprecate moodle-core-notification-confirm
- [MDL-79134](https://moodle.atlassian.net/browse/MDL-79134) - Deprecate MD5 for included user passwords in Backup
- [MDL-79313](https://moodle.atlassian.net/browse/MDL-79313) - Deprecate unused \\calendar\_top\_controls()
- [MDL-78328](https://moodle.atlassian.net/browse/MDL-78328) - Deprecate forum\_print\_discussion\_header
- [MDL-71067](https://moodle.atlassian.net/browse/MDL-71067) - Final deprecation of whitelist properties in coverage\_info
- [MDL-69530](https://moodle.atlassian.net/browse/MDL-69530) - Final deprecation of \\core\_h5p\\file\_storage::EDITOR\_FILEAREA constant
- [MDL-78012](https://moodle.atlassian.net/browse/MDL-78012) - Final deprecation of badge backpack methods from 3.11
- [MDL-71183](https://moodle.atlassian.net/browse/MDL-71183) - Final deprecation of \\core\_course\_renderer::course\_section\_cm\_completion()
- [MDL-71196](https://moodle.atlassian.net/browse/MDL-71196) - Final deprecation of \*\_get\_completion\_state() callbacks
- [MDL-71331](https://moodle.atlassian.net/browse/MDL-71331) - Final deprecation of course\_section\_add\_cm\_control\_nonajax()
- [MDL-71494](https://moodle.atlassian.net/browse/MDL-71494) - Final deprecation of the $extradetails parameter in mod\_feedback\\output\\summary constructor

### Component API updates[​](#component-api-updates "Direct link to Component API updates")

- [admin/tool/behat/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Ftool%2Fbehat%2Fupgrade.txt)
- [admin/tool/dataprivacy/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Ftool%2Fdataprivacy%2Fupgrade.txt)
- [admin/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dadmin%2Fupgrade.txt)
- [availability/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Davailability%2Fupgrade.txt)
- [backup/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dbackup%2Fupgrade.txt)
- [badges/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dbadges%2Fupgrade.txt)
- [cache/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcache%2Fupgrade.txt)
- [calendar/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcalendar%2Fupgrade.txt)
- [communication/provider/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcommunication%2Fprovider%2Fupgrade.txt)
- [communication/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcommunication%2Fupgrade.txt)
- [completion/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcompletion%2Fupgrade.txt)
- [course/format/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcourse%2Fformat%2Fupgrade.txt)
- [course/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcourse%2Fupgrade.txt)
- [customfield/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dcustomfield%2Fupgrade.txt)
- [enrol/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Denrol%2Fupgrade.txt)
- [filter/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dfilter%2Fupgrade.txt)
- [grade/report/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dgrade%2Freport%2Fupgrade.txt)
- [grade/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dgrade%2Fupgrade.txt)
- [group/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dgroup%2Fupgrade.txt)
- [h5p/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dh5p%2Fupgrade.txt)
- [lib/form/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Fform%2Fupgrade.txt)
- [lib/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Fupgrade.txt)
- [lib/xapi/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dlib%2Fxapi%2Fupgrade.txt)
- [mod/assign/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fassign%2Fupgrade.txt)
- [mod/bigbluebuttonbn/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fbigbluebuttonbn%2Fupgrade.txt)
- [mod/data/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fdata%2Fupgrade.txt)
- [mod/feedback/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Ffeedback%2Fupgrade.txt)
- [mod/forum/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fforum%2Fupgrade.txt)
- [mod/imscp/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fimscp%2Fupgrade.txt)
- [mod/lti/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Flti%2Fupgrade.txt)
- [mod/quiz/report/statistics/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fquiz%2Freport%2Fstatistics%2Fupgrade.txt)
- [mod/quiz/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fquiz%2Fupgrade.txt)
- [mod/resource/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fresource%2Fupgrade.txt)
- [mod/scorm/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dmod%2Fscorm%2Fupgrade.txt)
- [question/bank/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dquestion%2Fbank%2Fupgrade.txt)
- [question/type/calculated/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dquestion%2Ftype%2Fcalculated%2Fupgrade.txt)
- [question/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dquestion%2Fupgrade.txt)
- [reportbuilder/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dreportbuilder%2Fupgrade.txt)
- [repository/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Drepository%2Fupgrade.txt)
- [theme/boost/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dtheme%2Fboost%2Fupgrade.txt)
- [theme/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Dtheme%2Fupgrade.txt)
- [user/upgrade.txt](https://git.moodle.org/gw?p=moodle.git%3Ba%3Dblob%3Bf%3Duser%2Fupgrade.txt)