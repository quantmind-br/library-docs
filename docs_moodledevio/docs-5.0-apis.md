---
title: API Guides | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis
source: sitemap
fetched_at: 2026-02-17T15:23:44.767691-03:00
rendered_js: false
word_count: 1482
summary: This document provides a comprehensive overview of Moodle's core APIs essential for plugin development, covering key systems like data manipulation, access control, and output rendering.
tags:
    - moodle-api
    - plugin-development
    - core-subsystems
    - php-framework
    - moodle-dev
category: reference
---

Moodle has a number of core APIs that provide tools for Moodle scripts.

They are essential when writing [Moodle plugins](https://docs.moodle.org/dev/Plugins).

## Most-used General API[​](#most-used-general-api "Direct link to Most-used General API")

These APIs are critical and will be used by nearly every Moodle plugin.

### Access API (access)[​](#access-api-access "Direct link to Access API (access)")

The [Access API](https://moodledev.io/docs/5.0/apis/subsystems/access) gives you functions so you can determine what the current user is allowed to do, and it allows modules to extend Moodle with new capabilities.

### Data manipulation API (dml)[​](#data-manipulation-api-dml "Direct link to Data manipulation API (dml)")

The [Data manipulation API](https://moodledev.io/docs/5.0/apis/core/dml) allows you to read/write to databases in a consistent and safe way.

### File API (files)[​](#file-api-files "Direct link to File API (files)")

The [File API](https://moodledev.io/docs/5.0/apis/subsystems/files) controls the storage of files in connection to various plugins.

### Form API (form)[​](#form-api-form "Direct link to Form API (form)")

The [Form API](https://moodledev.io/docs/5.0/apis/subsystems/form) defines and handles user data via web forms.

### Logging API (log)[​](#logging-api-log "Direct link to Logging API (log)")

The [Events API](https://docs.moodle.org/dev/Events_API) allows you to log events in Moodle, while [Logging 2](https://docs.moodle.org/dev/Logging_2) describes how logs are stored and retrieved.

### Navigation API (navigation)[​](#navigation-api-navigation "Direct link to Navigation API (navigation)")

The [Navigation API](https://moodledev.io/docs/5.0/apis/core/navigation) allows you to manipulate the navigation tree to add and remove items as you wish.

### Page API (page)[​](#page-api-page "Direct link to Page API (page)")

The [Page API](https://docs.moodle.org/dev/Page_API) is used to set up the current page, add JavaScript, and configure how things will be displayed to the user.

### Output API (output)[​](#output-api-output "Direct link to Output API (output)")

The [Output API](https://moodledev.io/docs/5.0/apis/subsystems/output) is used to render the HTML for all parts of the page.

### String API (string)[​](#string-api-string "Direct link to String API (string)")

The [String API](https://docs.moodle.org/dev/String_API) is how you get language text strings to use in the user interface. It handles any language translations that might be available.

### Upgrade API (upgrade)[​](#upgrade-api-upgrade "Direct link to Upgrade API (upgrade)")

The [Upgrade API](https://moodledev.io/docs/5.0/guides/upgrade) is how your module installs and upgrades itself, by keeping track of its own version.

### Moodlelib API (core)[​](#moodlelib-api-core "Direct link to Moodlelib API (core)")

The [Moodlelib API](https://docs.moodle.org/dev/Moodlelib_API) is the central library file of miscellaneous general-purpose Moodle functions. Functions can over the handling of request parameters, configs, user preferences, time, login, mnet, plugins, strings and others. There are plenty of defined constants too.

## Other General API[​](#other-general-api "Direct link to Other General API")

### Admin settings API (admin)[​](#admin-settings-api-admin "Direct link to Admin settings API (admin)")

The [Admin settings](https://moodledev.io/docs/5.0/apis/subsystems/admin) API deals with providing configuration options for each plugin and Moodle core.

### Admin presets API (adminpresets)[​](#admin-presets-api-adminpresets "Direct link to Admin presets API (adminpresets)")

The [Admin presets API](https://docs.moodle.org/dev/AdminPresetsAPI) allows plugins to make some decisions/implementations related to the Site admin presets.

### Analytics API (analytics)[​](#analytics-api-analytics "Direct link to Analytics API (analytics)")

The [Analytics API](https://moodledev.io/docs/5.0/apis/subsystems/analytics) allow you to create prediction models and generate insights.

### Availability API (availability)[​](#availability-api-availability "Direct link to Availability API (availability)")

The [Availability API](https://moodledev.io/docs/5.0/apis/subsystems/availability) controls access to activities and sections.

### Backup API (backup)[​](#backup-api-backup "Direct link to Backup API (backup)")

The [Backup API](https://moodledev.io/docs/5.0/apis/subsystems/backup) defines exactly how to convert course data into XML for backup purposes, and the [Restore API](https://moodledev.io/docs/5.0/apis/subsystems/backup/restore) describes how to convert it back the other way.

### Cache API (cache)[​](#cache-api-cache "Direct link to Cache API (cache)")

The [The Moodle Universal Cache (MUC)](https://docs.moodle.org/dev/The_Moodle_Universal_Cache_%28MUC%29) is the structure for storing cache data within Moodle. [Cache API](https://moodledev.io/docs/5.0/apis/subsystems/muc) explains some of what is needed to use a cache in your code.

### Calendar API (calendar)[​](#calendar-api-calendar "Direct link to Calendar API (calendar)")

The [Calendar API](https://moodledev.io/docs/5.0/apis/core/calendar) allows you to add and modify events in the calendar for user, groups, courses, or the whole site.

### Check API (check)[​](#check-api-check "Direct link to Check API (check)")

The [Check API](https://moodledev.io/docs/5.0/apis/subsystems/check) allows you to add security, performance or health checks to your site.

The [Comment API](https://docs.moodle.org/dev/Comment_API) allows you to save and retrieve user comments, so that you can easily add commenting to any of your code.

### Communication API (communication)[​](#communication-api-communication "Direct link to Communication API (communication)")

The [Communication API](https://moodledev.io/docs/5.0/apis/subsystems/communication) provides access to the messaging system and other communication providers (such as Matrix).

### Competency API (competency)[​](#competency-api-competency "Direct link to Competency API (competency)")

The [Competency API](https://docs.moodle.org/dev/Competency_API) allows you to list and add evidence of competencies to learning plans, learning plan templates, frameworks, courses and activities.

### Data definition API (ddl)[​](#data-definition-api-ddl "Direct link to Data definition API (ddl)")

The [Data definition API](https://moodledev.io/docs/5.0/apis/core/dml/ddl) is what you use to create, change and delete tables and fields in the database during upgrades.

### Editor API[​](#editor-api "Direct link to Editor API")

The [Editor API](https://moodledev.io/docs/5.0/apis/subsystems/editor) is used to control HTML text editors.

### Enrolment API (enrol)[​](#enrolment-api-enrol "Direct link to Enrolment API (enrol)")

The [Enrolment API](https://moodledev.io/docs/5.0/apis/subsystems/enrol) deals with course participants.

### Events API (event)[​](#events-api-event "Direct link to Events API (event)")

The [Events API](https://docs.moodle.org/dev/Events_API) allows to define "events" with payload data to be fired whenever you like, and it also allows you to define handlers to react to these events when they happen. This is the recommended form of inter-plugin communication. This also forms the basis for logging in Moodle.

### Hooks API[​](#hooks-api "Direct link to Hooks API")

The [Hooks API](https://moodledev.io/docs/5.0/apis/core/hooks) allows core and plugins to communicate indirectly with other plugins.

### Experience API (xAPI)[​](#experience-api-xapi "Direct link to Experience API (xAPI)")

The Experience API (xAPI) is an e-learning standard that allows learning content and learning systems to speak to each other. The [Experience API (xAPI)](https://docs.moodle.org/dev/Experience_API_%28xAPI%29) allows any plugin to generate and handle xAPI standard statements.

### External functions API (external)[​](#external-functions-api-external "Direct link to External functions API (external)")

The [External functions API](https://moodledev.io/docs/5.0/apis/subsystems/external/functions) allows you to create fully parametrised methods that can be accessed by external programs (such as [Web services](https://moodledev.io/docs/5.0/apis/subsystems/external)).

### Favourites API[​](#favourites-api "Direct link to Favourites API")

The [Favourites API](https://moodledev.io/docs/5.0/apis/subsystems/favourites) allows you to mark items as favourites for a user and manage these favourites. This is often referred to as 'Starred'.

### H5P API (h5p)[​](#h5p-api-h5p "Direct link to H5P API (h5p)")

The [H5P API](https://docs.moodle.org/dev/H5P_API) allows plugins to make some decisions/implementations related to the [H5P integration](https://docs.moodle.org/dev/H5P).

### Lock API (lock)[​](#lock-api-lock "Direct link to Lock API (lock)")

The [Lock API](https://moodledev.io/docs/5.0/apis/core/lock) lets you synchronise processing between multiple requests, even for separate nodes in a cluster.

### Message API (message)[​](#message-api-message "Direct link to Message API (message)")

The [Message API](https://moodledev.io/docs/5.0/apis/core/message) lets you post messages to users. They decide how they want to receive them.

### Media API (media)[​](#media-api-media "Direct link to Media API (media)")

The [Media](https://docs.moodle.org/dev/Media_players#Using_media_players) API can be used to embed media items such as audio, video, and Flash.

### My profile API[​](#my-profile-api "Direct link to My profile API")

The [My profile API](https://docs.moodle.org/dev/My_profile_API) is used to add things to the profile page.

### OAuth 2 API (oauth2)[​](#oauth-2-api-oauth2 "Direct link to OAuth 2 API (oauth2)")

The [OAuth 2 API](https://docs.moodle.org/dev/OAuth_2_API) is used to provide a common place to configure and manage external systems using OAuth 2.

### Payment API (payment)[​](#payment-api-payment "Direct link to Payment API (payment)")

The [Payment API](https://docs.moodle.org/dev/Payment_API) deals with payments.

### Preference API (preference)[​](#preference-api-preference "Direct link to Preference API (preference)")

The [Preference API](https://moodledev.io/docs/5.0/apis/core/preference) is a simple way to store and retrieve preferences for individual users.

### Portfolio API (portfolio)[​](#portfolio-api-portfolio "Direct link to Portfolio API (portfolio)")

The [Portfolio API](https://docs.moodle.org/dev/Portfolio_API) allows you to add portfolio interfaces on your pages and allows users to package up data to send to their portfolios.

### Privacy API (privacy)[​](#privacy-api-privacy "Direct link to Privacy API (privacy)")

The [Privacy API](https://moodledev.io/docs/5.0/apis/subsystems/privacy) allows you to describe the personal data that you store, and provides the means for that data to be discovered, exported, and deleted on a per-user basis. This allows compliance with regulation such as the General Data Protection Regulation (GDPR) in Europe.

### Rating API (rating)[​](#rating-api-rating "Direct link to Rating API (rating)")

The [Rating API](https://docs.moodle.org/dev/Rating_API) lets you create AJAX rating interfaces so that users can rate items in your plugin. In an activity module, you may choose to aggregate ratings to form grades.

### Report builder API (reportbuilder)[​](#report-builder-api-reportbuilder "Direct link to Report builder API (reportbuilder)")

The [Report builder API](https://moodledev.io/docs/5.0/apis/core/reportbuilder) allows you to create reports in your plugin, as well as providing custom reporting data which users can use to build their own reports.

The [RSS API](https://docs.moodle.org/dev/RSS_API) allows you to create secure RSS feeds of data in your module.

### Search API (search)[​](#search-api-search "Direct link to Search API (search)")

The [Search API](https://docs.moodle.org/dev/Search_API) allows you to index contents in a search engine and query the search engine for results.

### Tag API (tag)[​](#tag-api-tag "Direct link to Tag API (tag)")

The [Tag API](https://moodledev.io/docs/5.0/apis/subsystems/tag) allows you to store tags (and a tag cloud) to items in your module.

### Task API (task)[​](#task-api-task "Direct link to Task API (task)")

The [Task API](https://moodledev.io/docs/5.0/apis/subsystems/task) lets you run jobs in the background. Either once off, or on a regular schedule.

### Time API (time)[​](#time-api-time "Direct link to Time API (time)")

The [Time API](https://moodledev.io/docs/5.0/apis/subsystems/time) takes care of translating and displaying times between users in the site.

### Testing API (test)[​](#testing-api-test "Direct link to Testing API (test)")

The testing API contains the Unit test API ([PHPUnit](https://moodledev.io/general/development/tools/phpunit)) and Acceptance test API ([Acceptance testing](https://moodledev.io/general/development/tools/behat)). Ideally all new code should have unit tests written FIRST.

This is a rather informal grouping of miscellaneous [User-related APIs](https://moodledev.io/docs/5.0/apis/core/user) relating to sorting and searching lists of users.

### Web services API (webservice)[​](#web-services-api-webservice "Direct link to Web services API (webservice)")

The [Web services API](https://moodledev.io/docs/5.0/apis/subsystems/external/writing-a-service) allows you to expose particular functions (usually external functions) as web services.

### Badges API (badges)[​](#badges-api-badges "Direct link to Badges API (badges)")

The \[[https://docs.moodle.org/dev/OpenBadges\_User\_Documentation](https://docs.moodle.org/dev/OpenBadges_User_Documentation) Badges] user documentation (is a temp page until we compile a proper page with all the classes and APIs that allows you to manage particular badges and OpenBadges Backpack).

### Custom fields API (customfield)[​](#custom-fields-api-customfield "Direct link to Custom fields API (customfield)")

The [Custom fields API](https://moodledev.io/docs/5.0/apis/core/customfields) allows you to configure and add custom fields for different entities

## Activity module APIs[​](#activity-module-apis "Direct link to Activity module APIs")

Activity modules are the most important plugin in Moodle. There are several core APIs that service only Activity modules.

### Activity completion API (completion)[​](#activity-completion-api-completion "Direct link to Activity completion API (completion)")

The [Activity completion API](https://moodledev.io/docs/5.0/apis/core/activitycompletion) is to indicate to the system how activities are completed.

### Advanced grading API (grading)[​](#advanced-grading-api-grading "Direct link to Advanced grading API (grading)")

The [Advanced grading API](https://moodledev.io/docs/5.0/apis/core/grading) allows you to add more advanced grading interfaces (such as rubrics) that can produce simple grades for the gradebook.

### Conditional activities API (condition) - deprecated in 2.7[​](#conditional-activities-api-condition---deprecated-in-27 "Direct link to Conditional activities API (condition) - deprecated in 2.7")

The deprecated [Conditional activities API](https://moodledev.io/docs/5.0/apis/core/conditionalactivities) used to provide conditional access to modules and sections in Moodle 2.6 and below. It has been replaced by the [Availability API](https://moodledev.io/docs/5.0/apis/subsystems/availability).

### Groups API (group)[​](#groups-api-group "Direct link to Groups API (group)")

The [Groups API](https://moodledev.io/docs/5.0/apis/subsystems/group) allows you to check the current activity group mode and set the current group.

### Gradebook API (grade)[​](#gradebook-api-grade "Direct link to Gradebook API (grade)")

The [Gradebook API](https://docs.moodle.org/dev/Gradebook_API) allows you to read and write from the gradebook. It also allows you to provide an interface for detailed grading information.

### Plagiarism API (plagiarism)[​](#plagiarism-api-plagiarism "Direct link to Plagiarism API (plagiarism)")

The [Plagiarism API](https://moodledev.io/docs/5.0/apis/subsystems/plagiarism) allows your activity module to send files and data to external services to have them checked for plagiarism.

### Question API (question)[​](#question-api-question "Direct link to Question API (question)")

The [Question API](https://docs.moodle.org/dev/Question_API) (which can be divided into the Question bank API and the Question engine API), can be used by activities that want to use questions from the question bank.

## See also[​](#see-also "Direct link to See also")

- [Plugins](https://docs.moodle.org/dev/Plugins) - plugin types also have their own APIs
- [Callbacks](https://docs.moodle.org/dev/Callbacks) - list of all callbacks in Moodle
- [Coding style](https://moodledev.io/general/development/policies/codingstyle) - general information about writing PHP code for Moodle
- [Session locks](https://docs.moodle.org/dev/Session_locks)