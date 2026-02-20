---
title: Moodle 4.5 | Moodle Developer Resources
url: https://moodledev.io/general/releases/4.5
source: sitemap
fetched_at: 2026-02-17T16:16:52.686006-03:00
rendered_js: false
word_count: 2232
summary: This document provides the release notes for Moodle 4.5, outlining essential server and client requirements as well as major user experience improvements. It serves as a technical reference for administrators and developers preparing for a platform upgrade or installation.
tags:
    - moodle-4-5
    - release-notes
    - system-requirements
    - php-compatibility
    - database-configuration
    - ux-improvements
    - software-update
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported for general bug fixes.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 7 October 2024

Here is [the full list of fixed issues in 4.5.0](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%224.5%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

If you are upgrading from a previous version, please see [Upgrading](https://docs.moodle.org/405/en/Upgrading) in the user docs.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software and operating systems up-to-date.

- Moodle upgrade: Moodle 4.1.2 or later.
- PHP version: minimum PHP 8.1.0 *Note: minimum PHP version was increased in Moodle 4.4*. PHP 8.3.x is supported too. See [PHP](https://moodledev.io/general/development/policies/php) for details.
- PHP extension **sodium** is required. See [Environment - PHP extension sodium](https://docs.moodle.org/en/Environment_-_PHP_extension_sodium).
- PHP setting **max\_input\_vars** must be &gt;= 5000. For further details, see [Environment - max input vars](https://docs.moodle.org/en/Environment_-_max_input_vars).
- PHP variants: Only 64-bit versions of PHP are supported. *Note: Changed since 4.1*.

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)13 (last increased in Moodle 4.2)Latest[MySQL](http://www.mysql.com/)8.0 (last increased in Moodle 4.2)Latest[MariaDB](https://mariadb.org/)10.6.7 (last increased in Moodle 4.2)Latest[Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)[8.0](#aurora-mysql-compatibility-version)Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2017Latest[Oracle Database](http://www.oracle.com/us/products/database/overview/index.html)19c (last increased in Moodle 4.4)Latest

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

### Course hierarchy improvements[​](#course-hierarchy-improvements "Direct link to Course hierarchy improvements")

- [MDL-82385](https://moodle.atlassian.net/browse/MDL-82385) - Course hierarchy support for the mobile app
- [MDL-81767](https://moodle.atlassian.net/browse/MDL-81767) - Add a mod\_subsection button to the add activity button
- [MDL-81771](https://moodle.atlassian.net/browse/MDL-81771) - Display delegated sections in course Activity report
- [MDL-81765](https://moodle.atlassian.net/browse/MDL-81765) - Add mod\_subsection to core
- [MDL-81766](https://moodle.atlassian.net/browse/MDL-81766) - Display mod\_subsection activity card like a subsection in the course page
- [MDL-81769](https://moodle.atlassian.net/browse/MDL-81769) - Allow mod\_subsection to override the activity actions dropdown
- [MDL-82495](https://moodle.atlassian.net/browse/MDL-82495) - Display sections in user Outline report and Complete report
- [MDL-82376](https://moodle.atlassian.net/browse/MDL-82376) - Implement an alternative to the move icon in the course index
- [MDL-81648](https://moodle.atlassian.net/browse/MDL-81648) - Allow the delegate plugin to add new breadcrumb nodes
- [MDL-81681](https://moodle.atlassian.net/browse/MDL-81681) - Make section page header reactive
- [MDL-82357](https://moodle.atlassian.net/browse/MDL-82357) - Prevent subsection from being moved into another subsection
- [MDL-82324](https://moodle.atlassian.net/browse/MDL-82324) - Show dropzones into the section page when the section is empty
- [MDL-82146](https://moodle.atlassian.net/browse/MDL-82146) - Display delegated sections in Logs report
- [MDL-80191](https://moodle.atlassian.net/browse/MDL-80191) - Enable delegate plugins to include delegated sections in the backup
- [MDL-82478](https://moodle.atlassian.net/browse/MDL-82478) - Add "Delete" option to subsection page
- [MDL-82480](https://moodle.atlassian.net/browse/MDL-82480) - Add "Move" option to subsection action menu
- [MDL-81683](https://moodle.atlassian.net/browse/MDL-81683) - Add subsections to the move activity modal
- [MDL-81725](https://moodle.atlassian.net/browse/MDL-81725) - Display subsections in the course index
- [MDL-81798](https://moodle.atlassian.net/browse/MDL-81798) - Prevent the course to try creating mod\_subsection instances once the section limit is reached
- [MDL-82510](https://moodle.atlassian.net/browse/MDL-82510) - Add new action menu for subsections

### Assignment improvements - phase 1[​](#assignment-improvements---phase-1 "Direct link to Assignment improvements - phase 1")

#### Assignment settings[​](#assignment-settings "Direct link to Assignment settings")

- [MDL-80741](https://moodle.atlassian.net/browse/MDL-80741) - Remove redundant "Never" option from "Additional attempts" in assignment settings
- [MDL-80743](https://moodle.atlassian.net/browse/MDL-80743) - New option in "Additional Attempts" setting to enable unconditional automatic attempts in assignment

#### Assignment submissions page[​](#assignment-submissions-page "Direct link to Assignment submissions page")

- [MDL-80747](https://moodle.atlassian.net/browse/MDL-80747) - Revamp the submission status filter on the assignment submissions page
- [MDL-80750](https://moodle.atlassian.net/browse/MDL-80750) - Implement a "sticky" footer on the assignment submissions page
- [MDL-82195](https://moodle.atlassian.net/browse/MDL-82195) - Add a link to the submissions page in the assignment's secondary navigation
- [MDL-80748](https://moodle.atlassian.net/browse/MDL-80748) - Make the table header "sticky" on the assignment submissions page
- [MDL-82681](https://moodle.atlassian.net/browse/MDL-82681) - Enhance the "marker" and "active participants" filters on the assignment submissions page
- [MDL-80746](https://moodle.atlassian.net/browse/MDL-80746) - Revamp the initials filter on the assignment submissions page
- [MDL-82295](https://moodle.atlassian.net/browse/MDL-82295) - Introduce new contextual menus for the editing options on the submissions page
- [MDL-80744](https://moodle.atlassian.net/browse/MDL-80744) - Implement user search filter on the assignment submissions page
- [MDL-82508](https://moodle.atlassian.net/browse/MDL-82508) - Revamp the workflow filter on the assignment submissions page
- [MDL-80745](https://moodle.atlassian.net/browse/MDL-80745) - Revamp the group selector on the assignment submissions page

## Other major features[​](#other-major-features "Direct link to Other major features")

### Add AI subsystem to LMS[​](#add-ai-subsystem-to-lms "Direct link to Add AI subsystem to LMS")

- [MDL-82627](https://moodle.atlassian.net/browse/MDL-82627) - AI subsystem MVP
- [MDL-80891](https://moodle.atlassian.net/browse/MDL-80891) - AI placement: Text Editor (image and text)
- [MDL-80890](https://moodle.atlassian.net/browse/MDL-80890) - AI placement: Course Assistance
- [MDL-80894](https://moodle.atlassian.net/browse/MDL-80894) - AI provider plugin: Open AI
- [MDL-82411](https://moodle.atlassian.net/browse/MDL-82411) - AI provider plugin: Azure AI
- [MDL-82609](https://moodle.atlassian.net/browse/MDL-82609) - AI provider action settings

### Add SMS subsystem and gateway plugin type[​](#add-sms-subsystem-and-gateway-plugin-type "Direct link to Add SMS subsystem and gateway plugin type")

- [MDL-81924](https://moodle.atlassian.net/browse/MDL-81924) - SMS subsystem MVP
- [MDL-80960](https://moodle.atlassian.net/browse/MDL-80960) - Create SMS API skeleton and gateway plugin type
- [MDL-80961](https://moodle.atlassian.net/browse/MDL-80961) - Implement AWS SMS gateway plugin and hook SMS MFA into SMS API
- [MDL-81732](https://moodle.atlassian.net/browse/MDL-81732) - Create UI for SMS gateway instance management

### Implement Open Badges 3.0[​](#implement-open-badges-30 "Direct link to Implement Open Badges 3.0")

- [MDL-43938](https://moodle.atlassian.net/browse/MDL-43938) - Allow duplicate badge names
- [MDL-82057](https://moodle.atlassian.net/browse/MDL-82057) - Import/Copy badges into other courses
- [MDL-82503](https://moodle.atlassian.net/browse/MDL-82503) - Merge "Manage badges" and "Course badges" reports
- [MDL-82168](https://moodle.atlassian.net/browse/MDL-82168) - Improve badges workflow: Move enable badge action to a modal
- [MDL-72354](https://moodle.atlassian.net/browse/MDL-72354) - Show always issuer details when creating/editing badges

### Notification Improvements - phase 2[​](#notification-improvements---phase-2 "Direct link to Notification Improvements - phase 2")

- [MDL-79716](https://moodle.atlassian.net/browse/MDL-79716) - New notification: Upcoming Assignment Due
- [MDL-79718](https://moodle.atlassian.net/browse/MDL-79718) - New notification: Upcoming Quiz Open
- [MDL-79733](https://moodle.atlassian.net/browse/MDL-79733) - New notification: Assignment overdue
- [MDL-79734](https://moodle.atlassian.net/browse/MDL-79734) - New notification: Assignments due in 7 days

### Enhance icons utilising Font Awesome 6[​](#enhance-icons-utilising-font-awesome-6 "Direct link to Enhance icons utilising Font Awesome 6")

- [MDL-82500](https://moodle.atlassian.net/browse/MDL-82500) - Enhance the call to action on the My Courses page
- [MDL-82211](https://moodle.atlassian.net/browse/MDL-82211) - Update icon\_map with the latest icons from Font Awesome 6 (plugins)
- [MDL-82212](https://moodle.atlassian.net/browse/MDL-82212) - Provide a mechanism to deprecate and detect deprecated icons
- [MDL-82497](https://moodle.atlassian.net/browse/MDL-82497) - Update icon\_map with the latest icons from Font Awesome 6 (core)
- [MDL-82498](https://moodle.atlassian.net/browse/MDL-82498) - Update pix/s emoticons with the emojis from the emoji-data library
- [MDL-82938](https://moodle.atlassian.net/browse/MDL-82938) - Consistent table sorting icons in report builder editor
- [MDL-80562](https://moodle.atlassian.net/browse/MDL-80562) - Reports converted to use report builder should use an ellipsis for the actions menu
- [MDL-82210](https://moodle.atlassian.net/browse/MDL-82210) - Add support to Font Awesome families
- [MDL-82476](https://moodle.atlassian.net/browse/MDL-82476) - Remove non-SVG icons
- [MDL-81589](https://moodle.atlassian.net/browse/MDL-81589) - Use Font Awesome icons in global search

### BigBlueButton[​](#bigbluebutton "Direct link to BigBlueButton")

- [MDL-82520](https://moodle.atlassian.net/browse/MDL-82520) - Create New Setting to Show/Hide Presentation File on Activity Page
- [MDL-82872](https://moodle.atlassian.net/browse/MDL-82872) - Extend meeting\_events with subplugins
- [MDL-82854](https://moodle.atlassian.net/browse/MDL-82854) - Log for analytics callback should store the raw data
- [MDL-82447](https://moodle.atlassian.net/browse/MDL-82447) - Remove mobile plugin from BigBlueButton plugin

### Quiz and questions[​](#quiz-and-questions "Direct link to Quiz and questions")

- [MDL-72397](https://moodle.atlassian.net/browse/MDL-72397) - Improve question category management UI
- [MDL-76665](https://moodle.atlassian.net/browse/MDL-76665) - Allow admins to deactivate Safe Exam Browser templates even if used in existing quizzes
- [MDL-78662](https://moodle.atlassian.net/browse/MDL-78662) - Allow filtered content in answers for Drag-and-drop questions
- [MDL-79546](https://moodle.atlassian.net/browse/MDL-79546) - Enable regrading for selected questions in quiz
- [MDL-80489](https://moodle.atlassian.net/browse/MDL-80489) - Help text for "Choices" section during Drag-and-drop into text question creation
- [MDL-82659](https://moodle.atlassian.net/browse/MDL-82659) - New Safe Exam Browser quiz setting capabilities for controlling manual config and SEB client config
- [MDL-81075](https://moodle.atlassian.net/browse/MDL-81075) - Provide an option to disable "sticky" defaults when creating questions
- [MDL-82587](https://moodle.atlassian.net/browse/MDL-82587) - Log changes to the version of questions used in quiz

### Report builder[​](#report-builder "Direct link to Report builder")

- [MDL-52046](https://moodle.atlassian.net/browse/MDL-52046) - Provide option to bulk delete cohorts
- [MDL-76889](https://moodle.atlassian.net/browse/MDL-76889) - Create "Competencies" custom report source
- [MDL-81330](https://moodle.atlassian.net/browse/MDL-81330) - Add Cohort condition and filter to Course Participants source
- [MDL-79496](https://moodle.atlassian.net/browse/MDL-79496) - Convert manage tokens report to system report
- [MDL-80123](https://moodle.atlassian.net/browse/MDL-80123) - Convert/improve the admin presets listing page
- [MDL-82331](https://moodle.atlassian.net/browse/MDL-82331) - Support custom report date filter by minute
- [MDL-82529](https://moodle.atlassian.net/browse/MDL-82529) - Allow to filter by custom fields within the Cohort report page
- [MDL-81433](https://moodle.atlassian.net/browse/MDL-81433) - Return custom report tags in external methods for retrieving reports
- [MDL-81399](https://moodle.atlassian.net/browse/MDL-81399) - Custom user reporting by timezone and language
- [MDL-82466](https://moodle.atlassian.net/browse/MDL-82466) - Format the output of the "Days taking course" report completion columns
- [MDL-81168](https://moodle.atlassian.net/browse/MDL-81168) - Ensure all filters that accept numeric data also handle localised floats
- [MDL-82175](https://moodle.atlassian.net/browse/MDL-82175) - Get rid of the task log popup window and make it a normal page
- [MDL-82114](https://moodle.atlassian.net/browse/MDL-82114) - Add plugin/area filters to Files custom report source
- [MDL-82512](https://moodle.atlassian.net/browse/MDL-82512) - Add "Author" report filter to the files report entity/source
- [MDL-76392](https://moodle.atlassian.net/browse/MDL-76392) - System reports should be allowed to define aggregation to allow re-use of entities
- [MDL-81754](https://moodle.atlassian.net/browse/MDL-81754) - Consistent comparison field labels in report filters
- [MDL-82463](https://moodle.atlassian.net/browse/MDL-82463) - Improve column types for numeric columns that don't produce numeric output

### TinyMCE 6[​](#tinymce-6 "Direct link to TinyMCE 6")

- [MDL-81212](https://moodle.atlassian.net/browse/MDL-81212) - Tiny/RecordRTC: Add Screen-recorder button
- [MDL-81111](https://moodle.atlassian.net/browse/MDL-81111) - Tiny/RecordRTC: TinyMCE conversion - add "Pause" button for recording A/V

### Content bank and H5P[​](#content-bank-and-h5p "Direct link to Content bank and H5P")

- [MDL-74590](https://moodle.atlassian.net/browse/MDL-74590) - Add Custom Fields to Content Bank
- [MDL-76242](https://moodle.atlassian.net/browse/MDL-76242) - Hide/show unlisted content on contentbank and filepicker

### Usability improvements[​](#usability-improvements "Direct link to Usability improvements")

- [MDL-26675](https://moodle.atlassian.net/browse/MDL-26675) - Unable to return to the RSS block settings after adding a new RSS feed
- [MDL-82339](https://moodle.atlassian.net/browse/MDL-82339) - User tours setup: text input boxes should be big enough so typical content is not truncated
- [MDL-81250](https://moodle.atlassian.net/browse/MDL-81250) - Display the full names instead of the short names for the course dropdown filter in the calendar
- [MDL-81872](https://moodle.atlassian.net/browse/MDL-81872) - Course reset: Improve form wording and remove advanced elements
- [MDL-81866](https://moodle.atlassian.net/browse/MDL-81866) - Course reset: Move Reset button to sticky and improve the workflow
- [MDL-81742](https://moodle.atlassian.net/browse/MDL-81742) - Improve feedback activity "Edit questions" navigation
- [MDL-81743](https://moodle.atlassian.net/browse/MDL-81743) - Improve feedback activity "Edit questions" questions UI
- [MDL-81503](https://moodle.atlassian.net/browse/MDL-81503) - Improve the section error page when the ID is not correct
- [MDL-77661](https://moodle.atlassian.net/browse/MDL-77661) - Use danger button for the Reset actions in Database activity
- [MDL-73232](https://moodle.atlassian.net/browse/MDL-73232) - Inform teacher about maxsections setting to understand why they cannot add more topics/weeks
- [MDL-54105](https://moodle.atlassian.net/browse/MDL-54105) - Ability to set default grade options for assignments
- [MDL-60957](https://moodle.atlassian.net/browse/MDL-60957) - Show assignment extension date in calendar

## Other Highlights[​](#other-highlights "Direct link to Other Highlights")

### Functional changes[​](#functional-changes "Direct link to Functional changes")

- [MDL-63753](https://moodle.atlassian.net/browse/MDL-63753) - Show stealth activity links to non-editing teachers
- [MDL-81506](https://moodle.atlassian.net/browse/MDL-81506) - Allow teacher to edit manual course welcome message
- [MDL-63015](https://moodle.atlassian.net/browse/MDL-63015) - Lock the feedback form when previewing
- [MDL-80858](https://moodle.atlassian.net/browse/MDL-80858) - Add numeric field type for course custom fields
- [MDL-81741](https://moodle.atlassian.net/browse/MDL-81741) - Create a new feedback activity "Questions" secondary menu item
- [MDL-77195](https://moodle.atlassian.net/browse/MDL-77195) - Support multilang for the shibboleth login button
- [MDL-81321](https://moodle.atlassian.net/browse/MDL-81321) - Remove "View templates" link from the sticky footer in the Database fields page
- [MDL-72424](https://moodle.atlassian.net/browse/MDL-72424) - Remove non-functional role switch check in Feedback module

### For administrators[​](#for-administrators "Direct link to For administrators")

- [MDL-80967](https://moodle.atlassian.net/browse/MDL-80967) - Login page: Give the option to hide the login form with only a configuration
- [MDL-77544](https://moodle.atlassian.net/browse/MDL-77544) - Include start and end dates with External database course creation
- [MDL-81533](https://moodle.atlassian.net/browse/MDL-81533) - Availability restriction info default change
- [MDL-82066](https://moodle.atlassian.net/browse/MDL-82066) - Allow plugins to hook into/extend site default homepage options
- [MDL-81942](https://moodle.atlassian.net/browse/MDL-81942) - Respect defaulthomepage setting for guests
- [MDL-82532](https://moodle.atlassian.net/browse/MDL-82532) - Capability to allow/prevent view of profile images

### Performance[​](#performance "Direct link to Performance")

- [MDL-66151](https://moodle.atlassian.net/browse/MDL-66151) - Allow session stores to fully manage the session
- [MDL-78030](https://moodle.atlassian.net/browse/MDL-78030) - Make tablelib and reports faster by combining count query into main query
- [MDL-64325](https://moodle.atlassian.net/browse/MDL-64325) - Improve final grade calculation performance for grade items and categories

## Security improvements[​](#security-improvements "Direct link to Security improvements")

- [MDL-58353](https://moodle.atlassian.net/browse/MDL-58353) - Empower users to be able to log out other sessions during password reset
- [MDL-75850](https://moodle.atlassian.net/browse/MDL-75850) - Add the ability to configure automatic EXIF data removal from uploaded images
- [MDL-82231](https://moodle.atlassian.net/browse/MDL-82231) - Public path checker should check for new UPGRADING.md files
- [MDL-81940](https://moodle.atlassian.net/browse/MDL-81940) - Replace the RC4 encryption methods with a standard library
- [MDL-82585](https://moodle.atlassian.net/browse/MDL-82585) - Final removal of long since unused proxy scripts in Feedback

## For developers[​](#for-developers "Direct link to For developers")

- [MDL-81125](https://moodle.atlassian.net/browse/MDL-81125) - Introduce tooling for upgrade note management
- [MDL-80797](https://moodle.atlassian.net/browse/MDL-80797) - Add support for local plugins to add or reorder secondary navigation menu items in course navigation using hooks API
- [MDL-81807](https://moodle.atlassian.net/browse/MDL-81807) - Implement automatic download and update of GeoIP database via scheduled task
- [MDL-81816](https://moodle.atlassian.net/browse/MDL-81816) - Refactor theme-color-level() function renamed in Bootstrap 5
- [MDL-75671](https://moodle.atlassian.net/browse/MDL-75671) - Refactor utility classes for layout and spacing renamed in Bootstrap 5

### Web service modernisation[​](#web-service-modernisation "Direct link to Web service modernisation")

- [MDL-81031](https://moodle.atlassian.net/browse/MDL-81031) - Initial implementation of the Routing system
- [MDL-81903](https://moodle.atlassian.net/browse/MDL-81903) - Add new exception API
- [MDL-80275](https://moodle.atlassian.net/browse/MDL-80275) - Allow ABORT\_AFTER\_CONFIG to include autoload tooling
- [MDL-82778](https://moodle.atlassian.net/browse/MDL-82778) - Refactor core/fetch

### Break apart core monolith \*lib.php files[​](#break-apart-core-monolith-libphp-files "Direct link to Break apart core monolith *lib.php files")

- [MDL-81919](https://moodle.atlassian.net/browse/MDL-81919) - Break apart lib/setuplib.php
- [MDL-82156](https://moodle.atlassian.net/browse/MDL-82156) - Add check to \\core\_component for some key autoloadable classes
- [MDL-82183](https://moodle.atlassian.net/browse/MDL-82183) - Break apart lib/output*
- [MDL-81960](https://moodle.atlassian.net/browse/MDL-81960) - Break apart lib/weblib.php
- [MDL-82158](https://moodle.atlassian.net/browse/MDL-82158) - Break apart cache/lib.php classes
- [MDL-82191](https://moodle.atlassian.net/browse/MDL-82191) - Deprecate unused libs (lib/soaplib.php, lib/tokeniserlib.php)
- [MDL-82427](https://moodle.atlassian.net/browse/MDL-82427) - Split filterlib.php
- [MDL-82287](https://moodle.atlassian.net/browse/MDL-82287) - Trim lib/deprecatedlib.php
- [MDL-81920](https://moodle.atlassian.net/browse/MDL-81920) - Split out the emoticon/lang string classes from moodlelib

### Web service additions and updates[​](#web-service-additions-and-updates "Direct link to Web service additions and updates")

- [MDL-70854](https://moodle.atlassian.net/browse/MDL-70854) - New API to allow adhoc tasks to communicate a progress bar / status back to the calling page
- [MDL-82105](https://moodle.atlassian.net/browse/MDL-82105) - New web service to retrieve information about a badge (core\_badges\_get\_badge)
- [MDL-78293](https://moodle.atlassian.net/browse/MDL-78293) - New web service to allow managing private files
- [MDL-74050](https://moodle.atlassian.net/browse/MDL-74050) - New web service to allow removing submissions
- [MDL-81699](https://moodle.atlassian.net/browse/MDL-81699) - Web service core\_course\_get\_courses\_by\_field should support a new parameter (sectionid) to be able to retrieve the course that has the indicated section
- [MDL-82234](https://moodle.atlassian.net/browse/MDL-82234) - Update the tool\_mobile\_get\_public\_config web service to return the new option to hide the login form

### Deprecations[​](#deprecations "Direct link to Deprecations")

- [MDL-82935](https://moodle.atlassian.net/browse/MDL-82935) - Remove $straction from filter/manage.php
- [MDL-82223](https://moodle.atlassian.net/browse/MDL-82223) - Final deprecation of availability restrictions renderer
- [MDL-72353](https://moodle.atlassian.net/browse/MDL-72353) - Final deprecation of save\_selected\_report()
- [MDL-76690](https://moodle.atlassian.net/browse/MDL-76690) - Final deprecation of Report builder methods deprecated in 4.1
- [MDL-74939](https://moodle.atlassian.net/browse/MDL-74939) - Final deprecation of "local/views" namespace used for navigation
- [MDL-74484](https://moodle.atlassian.net/browse/MDL-74484) - Final deprecation of print\_error()
- [MDL-71748](https://moodle.atlassian.net/browse/MDL-71748) - Final deprecation of reset\_caches
- [MDL-72620](https://moodle.atlassian.net/browse/MDL-72620) - Final deprecation of repository\_skydrive importing feature
- [MDL-74843](https://moodle.atlassian.net/browse/MDL-74843) - Final deprecation of \\core\\task\\manager::ensure\_adhoc\_task\_qos
- [MDL-73956](https://moodle.atlassian.net/browse/MDL-73956) - Final deprecation of function "forum\_update\_subscriptions\_button"
- [MDL-75022](https://moodle.atlassian.net/browse/MDL-75022) - Final deprecation of core\_backup\\copy
- [MDL-71326](https://moodle.atlassian.net/browse/MDL-71326) - Final deprecation of plagiarism functions (4.4)
- [MDL-73284](https://moodle.atlassian.net/browse/MDL-73284) - Final deprecation of MESSAGE\_DEFAULT\_LOGGEDOFF / MESSAGE\_DEFAULT\_LOGGEDIN
- [MDL-73976](https://moodle.atlassian.net/browse/MDL-73976) - Final deprecation of print\_course\_request\_buttons
- [MDL-75025](https://moodle.atlassian.net/browse/MDL-75025) - Final deprecation of base\_controller::set\_copy/get\_copy
- [MDL-73165](https://moodle.atlassian.net/browse/MDL-73165) - Final deprecation of should\_display\_main\_logo() in renderer.php
- [MDL-77167](https://moodle.atlassian.net/browse/MDL-77167) - Remove deprecation layer for [MDL-70990](https://moodle.atlassian.net/browse/MDL-70990) (YUI Events)
- [MDL-81914](https://moodle.atlassian.net/browse/MDL-81914) - Remove deprecated "\\core\_competency\\invalid\_persistent\_exception"
- [MDL-82301](https://moodle.atlassian.net/browse/MDL-82301) - Remove legacy tabs.php file from Feedback module
- [MDL-82547](https://moodle.atlassian.net/browse/MDL-82547) - Remove usage of, and deprecation layer for, inplace editable jQuery events
- [MDL-78776](https://moodle.atlassian.net/browse/MDL-78776) - Expunge MyISAM code, strings, docs

### Component API updates[​](#component-api-updates "Direct link to Component API updates")

- [core](https://github.com/moodle/moodle/blob/v4.5.0/lib/UPGRADING.md)
- [core\_admin](https://github.com/moodle/moodle/blob/v4.5.0/admin/UPGRADING.md)
- [core\_availability](https://github.com/moodle/moodle/blob/v4.5.0/availability/UPGRADING.md)
- [core\_backup](https://github.com/moodle/moodle/blob/v4.5.0/backup/util/ui/UPGRADING.md)
- [core\_badges](https://github.com/moodle/moodle/blob/v4.5.0/badges/UPGRADING.md)
- [core\_cache](https://github.com/moodle/moodle/blob/v4.5.0/cache/UPGRADING.md)
- [core\_communication](https://github.com/moodle/moodle/blob/v4.5.0/communication/UPGRADING.md)
- [core\_completion](https://github.com/moodle/moodle/blob/v4.5.0/completion/UPGRADING.md)
- [core\_course](https://github.com/moodle/moodle/blob/v4.5.0/course/UPGRADING.md)
- [core\_courseformat](https://github.com/moodle/moodle/blob/v4.5.0/course/format/UPGRADING.md)
- [core\_customfield](https://github.com/moodle/moodle/blob/v4.5.0/customfield/UPGRADING.md)
- [core\_external](https://github.com/moodle/moodle/blob/v4.5.0/lib/external/UPGRADING.md)
- [core\_files](https://github.com/moodle/moodle/blob/v4.5.0/files/UPGRADING.md)
- [core\_filters](https://github.com/moodle/moodle/blob/v4.5.0/filter/UPGRADING.md)
- [core\_form](https://github.com/moodle/moodle/blob/v4.5.0/lib/form/UPGRADING.md)
- [core\_grades](https://github.com/moodle/moodle/blob/v4.5.0/grade/UPGRADING.md)
- [core\_message](https://github.com/moodle/moodle/blob/v4.5.0/message/UPGRADING.md)
- [core\_question](https://github.com/moodle/moodle/blob/v4.5.0/question/UPGRADING.md)
- [core\_report](https://github.com/moodle/moodle/blob/v4.5.0/report/UPGRADING.md)
- [core\_reportbuilder](https://github.com/moodle/moodle/blob/v4.5.0/reportbuilder/UPGRADING.md)
- [core\_role](https://github.com/moodle/moodle/blob/v4.5.0/admin/roles/UPGRADING.md)
- [core\_sms](https://github.com/moodle/moodle/blob/v4.5.0/sms/UPGRADING.md)
- [core\_table](https://github.com/moodle/moodle/blob/v4.5.0/lib/table/UPGRADING.md)
- [core\_user](https://github.com/moodle/moodle/blob/v4.5.0/user/UPGRADING.md)
- [availability](https://github.com/moodle/moodle/blob/v4.5.0/availability/condition/UPGRADING.md)
- [customfield\_number](https://github.com/moodle/moodle/blob/v4.5.0/customfield/field/number/UPGRADING.md)
- [customfield\_select](https://github.com/moodle/moodle/blob/v4.5.0/customfield/field/select/UPGRADING.md)
- [editor\_tiny](https://github.com/moodle/moodle/blob/v4.5.0/lib/editor/tiny/UPGRADING.md)
- [factor\_sms](https://github.com/moodle/moodle/blob/v4.5.0/admin/tool/mfa/factor/sms/UPGRADING.md)
- [gradereport\_grader](https://github.com/moodle/moodle/blob/v4.5.0/grade/report/grader/UPGRADING.md)
- [gradereport\_singleview](https://github.com/moodle/moodle/blob/v4.5.0/grade/report/singleview/UPGRADING.md)
- [gradereport\_user](https://github.com/moodle/moodle/blob/v4.5.0/grade/report/user/UPGRADING.md)
- [mod](https://github.com/moodle/moodle/blob/v4.5.0/mod/UPGRADING.md)
- [mod\_assign](https://github.com/moodle/moodle/blob/v4.5.0/mod/assign/UPGRADING.md)
- [mod\_bigbluebuttonbn](https://github.com/moodle/moodle/blob/v4.5.0/mod/bigbluebuttonbn/UPGRADING.md)
- [mod\_data](https://github.com/moodle/moodle/blob/v4.5.0/mod/data/UPGRADING.md)
- [mod\_feedback](https://github.com/moodle/moodle/blob/v4.5.0/mod/feedback/UPGRADING.md)
- [mod\_quiz](https://github.com/moodle/moodle/blob/v4.5.0/mod/quiz/UPGRADING.md)
- [qbank\_managecategories](https://github.com/moodle/moodle/blob/v4.5.0/question/bank/managecategories/UPGRADING.md)
- [report\_eventlist](https://github.com/moodle/moodle/blob/v4.5.0/report/eventlist/UPGRADING.md)
- [report\_log](https://github.com/moodle/moodle/blob/v4.5.0/report/log/UPGRADING.md)
- [repository\_onedrive](https://github.com/moodle/moodle/blob/v4.5.0/repository/onedrive/UPGRADING.md)
- [theme](https://github.com/moodle/moodle/blob/v4.5.0/theme/UPGRADING.md)
- [theme\_boost](https://github.com/moodle/moodle/blob/v4.5.0/theme/boost/UPGRADING.md)
- [tool](https://github.com/moodle/moodle/blob/v4.5.0/admin/tool/UPGRADING.md)
- [tool\_behat](https://github.com/moodle/moodle/blob/v4.5.0/admin/tool/behat/UPGRADING.md)
- [tool\_oauth2](https://github.com/moodle/moodle/blob/v4.5.0/admin/tool/oauth2/UPGRADING.md)