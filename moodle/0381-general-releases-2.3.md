---
title: Moodle 2.3 | Moodle Developer Resources
url: https://moodledev.io/general/releases/2.3
source: sitemap
fetched_at: 2026-02-17T16:05:20.212115-03:00
rendered_js: false
word_count: 2309
summary: This document provides the release notes for Moodle 2.3, outlining system requirements, major feature updates, and improvements to file management, course pages, and activity modules.
tags:
    - moodle
    - release-notes
    - system-requirements
    - lms-features
    - software-update
    - legacy-version
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 25th June 2012

Here is [the full list of fixed issues in 2.3](https://moodle.atlassian.net/issues/?jql=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%222.3%22%29%20ORDER%20BY%20priority%20DESC).

Many thanks to [everyone that worked on the new features in this release](http://moodle.org/dev/contributions.php?version=2.3.x), including those from [Moodle HQ](http://moodle.com/hq/team), [The Open University](http://www.open.ac.uk/), [NetSpot](http://www.netspot.com.au/), [Synergy Learning](http://www.synergy-learning.com/), [Lancaster University Network Services](http://www.luns.net.uk/), [Catalyst IT](http://catalyst.net.nz/), [CV&A Consulting](http://www.cvaconsulting.com/) (funded by [ESADE](http://www.esade.edu) and [IL3-UB](http://www.il3.ub.edu)) and others. More details can be found below under each major feature, or look at the list of bugs fixed above.

A special thanks to our incredible **'Integration Team**' from Moodle HQ who worked tirelessly with all developers to review, test and help finish code for inclusion in Moodle core:

- Eloy Lafuente
- Sam Hemelryk
- Dan Poltawski
- Aparup Bannerjee

Finally, thanks to all our testers both within Moodle HQ and from the whole community, who have contributed to producing our most exciting and stable release yet!

### Requirements[​](#requirements "Direct link to Requirements")

- Minimum browser: Firefox 4, Internet Explorer 8 (IE 10 required for drag and drop of files from outside the browser into Moodle) , Safari 5, Google Chrome 11, Opera 9
- Moodle upgrade: Moodle 2.2 or later (if upgrading from earlier versions, you must upgrade to 2.2 as a first step)
- Minimum DB versions: Postgres 8.3, MySQL 5.1.33 ([MDL-33984](https://moodle.atlassian.net/browse/MDL-33984)), MSSQL 2005 or Oracle 10.2
- Minimum PHP version: PHP 5.3.2

### Major new features[​](#major-new-features "Direct link to Major new features")

#### Files usability[​](#files-usability "Direct link to Files usability")

- [MDL-31907](https://moodle.atlassian.net/browse/MDL-31907) - A nicer-looking file picker with fewer clicks.
- Images now display as true thumbnails in the file picker and file manager.
- Other files have pretty icons for most file types.
- Files view can be easily toggled between icons view or a table view with sizes and dates, or a hierarchical list view.
- You can now drag and drop files directly from your desktop straight into file areas!
- File info (eg license information, sizes, dates) can be easily edited and viewed in a popup dialogue.
- Files can be created as "aliases/shortcuts" of other files. This allows you to, for example, use a single file in your private files area multiple times in all your courses. If you update the original file then all the aliases will automatically update!
- Aliases are easily identifiable in the file manager interface.

Credits to Moodle HQ: Marina Glancy, Barbara Ramiro, Martin Dougiamas, David Mudrak, Dongsheng Cai and others.

#### Repository improvements[​](#repository-improvements "Direct link to Repository improvements")

- [MDL-32117](https://moodle.atlassian.net/browse/MDL-32117) - New [EQUELLA repository](https://docs.moodle.org/23/en/EQUELLA_repository) enabling users to make aliases (shortcuts) to EQUELLA files.
- [MDL-28666](https://moodle.atlassian.net/browse/MDL-28666) - If a repository supports it then it's possible to make an alias/shortcut to a file in an external repository. If the file is updated in the repository, then this change is reflected in Moodle. The file remains under Moodle access control however, and the original URL is not usually revealed. In the 2.3 core release, this is supported by private files, server files, file system, Box.net and EQUELLA repositories.
- The repository plugin is now able to take over the whole right-hand pane of the file picker and provide its own searching/browsing interface.
- [MDL-31675](https://moodle.atlassian.net/browse/MDL-31675) - Server files repository now available for database, forum and glossary activities.

Credits to Moodle HQ: Dongsheng Cai, Marina Glancy, Martin Dougiamas, Petr Skoda

#### Improvements to course pages[​](#improvements-to-course-pages "Direct link to Improvements to course pages")

- [MDL-32476](https://moodle.atlassian.net/browse/MDL-32476) - Courses can now choose to show sections on individual pages
- [MDL-31052](https://moodle.atlassian.net/browse/MDL-31052) - All AJAX editing on the course pages has been modernised and cleaned up (YUI3). It's on by default now too.
- [MDL-31263](https://moodle.atlassian.net/browse/MDL-31263) - Blocks can be dragged and dropped around the page (again)
- [MDL-30617](https://moodle.atlassian.net/browse/MDL-30617) - An optional new popup ["Activity chooser"](https://docs.moodle.org/23/en/Course_homepage) has been added with full introduction, examples and links about each activity or resource module.
- [MDL-22504](https://moodle.atlassian.net/browse/MDL-22504) - You can now drag files straight into the course page and they will be added as resources.
- [MDL-31215](https://moodle.atlassian.net/browse/MDL-31215) - You can edit the name of any activity or resource directly on the course page without entering the settings (works particularly well with drag and drop).
- [MDL-32771](https://moodle.atlassian.net/browse/MDL-32771) - You can now add/remove sections directly from the [course page](https://docs.moodle.org/23/en/Course_homepage).
- [MDL-32770](https://moodle.atlassian.net/browse/MDL-32770) - With paged sections, navigation is possible between sections (previous, next, main).

Credits to: Andrew Nicols and Ruslan Kabalin (LUNS) Davo Smith (Synergy Learning), Dan Poltawski and Martin Dougiamas (Moodle HQ)

![File drag and drop](https://moodledev.io/assets/images/dragandrop-41f7cf22314e990d930f3783c567eae9.png)

![Activity chooser](https://moodledev.io/assets/images/activity_chooser-80ea2cc000638349b4547fc9d17db4ef.png)

#### Assignment module[​](#assignment-module "Direct link to Assignment module")

- [MDL-26997](https://moodle.atlassian.net/browse/MDL-26997) - Complete rewrite of the assignment module from scratch, by [NetSpot](http://www.netspot.com.au/) (Moodle Partner in Australia)
- Assignment subtypes are no longer needed. New plugins are possible for
- Old Assignment module is still installed, and works, but is not necessary

Credits to Netspot: Damyon Wiese, Raymond Wijaya, Minh-Tam Nguyen

- [Upgrade Tool](https://docs.moodle.org/23/en/Upgrade_tool) is provided to upgrade from old assigments
- [MDL-31731](https://moodle.atlassian.net/browse/MDL-31731) - New [marking guide](https://docs.moodle.org/23/en/Marking_guide) advanced grading method, where a teacher enters a comment per criterion and a mark up to a maximum

Credits to Dan Marsden Catalyst IT (development); Lightwork Team at Massey University (concept); NetSpot Innovation Grant (funding)

#### Book module[​](#book-module "Direct link to Book module")

- [MDL-32709](https://moodle.atlassian.net/browse/MDL-32709) - The most popular third-party resource module ever, [Book](https://docs.moodle.org/23/en/Book_module) finally joins core. Welcome!

Credits to Petr Škoda, Moodle HQ

#### Quiz module[​](#quiz-module "Direct link to Quiz module")

- [MDL-3030](https://moodle.atlassian.net/browse/MDL-3030) - More robust handling of quiz attempts that are not submitted by the deadline.
- [MDL-3054](https://moodle.atlassian.net/browse/MDL-3054) & [MDL-11047](https://moodle.atlassian.net/browse/MDL-11047) - There is now an option for teacher to force students to answer the quiz questions strictly in order. As part of this, the quiz remembers which page the student was last on, and will take them back there when they resume an attempt.

Credits to Tim Hunt, The Open University and Charles Fulton, Lafayette College

#### SCORM module[​](#scorm-module "Direct link to SCORM module")

- [MDL-29745](https://moodle.atlassian.net/browse/MDL-29745) - New [SCORM graph report](https://docs.moodle.org/23/en/Using_SCORM) plugin (credits to Ankit Agarwal, Moodle HQ and Dan Marsden, Catalyst IT)
- [MDL-32937](https://moodle.atlassian.net/browse/MDL-32937) - You can now drag a SCORM package straight into the course page and it will be added as SCORM activity (credits to Christopher Tombleson and Dan Marsden, Catalyst IT, and Davo Smith, Synergy Learning)

#### Workshop module[​](#workshop-module "Direct link to Workshop module")

- [MDL-26099](https://moodle.atlassian.net/browse/MDL-26099) - [Option to make the workshop switch to the assessment phase](https://docs.moodle.org/23/en/Workshop_settings) automatically after the submissions deadline (including automatic allocation of submissions for assessment)
- [MDL-25660](https://moodle.atlassian.net/browse/MDL-25660) - Workshop submission deadlines are shown in the calendar
- [MDL-27508](https://moodle.atlassian.net/browse/MDL-27508) - Improved support for pagination and filtering workshop submissions by group
- [MDL-32638](https://moodle.atlassian.net/browse/MDL-32638) - Workshop supports file browsing via Server files repository (including improved access control when serving submission files)

Credits to David Mudrak, Moodle HQ

#### Available update notifications[​](#available-update-notifications "Direct link to Available update notifications")

- [MDL-20438](https://moodle.atlassian.net/browse/MDL-20438) - Admins are sent [notification of any updates available](https://docs.moodle.org/23/en/Notifications) for core code and for any contributed plugins installed on the site (from the [plugins directory](http://moodle.org/plugins)). Admins can also check for available updates using buttons on the notifications and plugins overview pages.

Credits to David Mudrak, Moodle HQ

### Other highlights[​](#other-highlights "Direct link to Other highlights")

#### Google Docs and Picasa plugins requirement[​](#google-docs-and-picasa-plugins-requirement "Direct link to Google Docs and Picasa plugins requirement")

- [MDL-29857](https://moodle.atlassian.net/browse/MDL-29857) - Due to a change in Google's service, Moodle has switched to a more secure and more user-friendly system for communicating with Google called 'OAuth 2.0'. An administrator must register their site with Google, as described in [Google OAuth 2.0 setup](https://docs.moodle.org/23/en/Google_OAuth_2.0_setup) in order to obtain a client ID and secret for use in configuring all Google Docs and Picasa plugins (the Google Docs and Picasa repositories and the Google Docs and Picasa portfolios).

Credits to Dan Poltawski, Moodle HQ

#### IMS Common Cartridge 1.1 Export[​](#ims-common-cartridge-11-export "Direct link to IMS Common Cartridge 1.1 Export")

- [MDL-33079](https://moodle.atlassian.net/browse/MDL-33079) - In Moodle 2.2 we introduced IMS CC import. Well, now you can also export to that format, via the normal Backup menu. Just look for the IMS CC checkbox.

#### Miscellaneous[​](#miscellaneous "Direct link to Miscellaneous")

- [MDL-31121](https://moodle.atlassian.net/browse/MDL-31121) - Option in [file resource settings](https://docs.moodle.org/23/en/File_module_settings) to display file size and/or type on course page (credits to Sam Marshall, The Open University)
- [MDL-32009](https://moodle.atlassian.net/browse/MDL-32009) - Admin option for uninstalling messaging outputs and report of messaging output statuses on plugins overview page
- [MDL-29941](https://moodle.atlassian.net/browse/MDL-29941) - Admin option to enable a [CSS optimiser](https://docs.moodle.org/23/en/CSS_optimiser) that analyses and refactors CSS before caching it
- [MDL-24419](https://moodle.atlassian.net/browse/MDL-24419) - [Conditional activities setting](https://docs.moodle.org/23/en/Conditional_activities_settings) enabling teachers to restrict access to a course section using similar logic to Conditional Activities (with thanks to the [University of New South Wales](http://www.unsw.edu.au/) for funding and [NetSpot](http://www.netspot.com.au/) for developing this feature and Sam Marshall at the [OU](http://www.open.ac.uk) for integrating it to core)
- [MDL-26901](https://moodle.atlassian.net/browse/MDL-26901) - Option to add extra fonts to the [TinyMCE HTML editor](https://docs.moodle.org/23/en/Text_editor)
- [MDL-31315](https://moodle.atlassian.net/browse/MDL-31315) - When editing a form, a warning will be displayed if trying to navigate away with content edited
- [MDL-33401](https://moodle.atlassian.net/browse/MDL-33401) - Managers are now allowed the capability to edit blocks (moodle/block:edit) by default for new installs. This does not affect existing installations.
- [MDL-32005](https://moodle.atlassian.net/browse/MDL-32005) - New group and groupings ID number setting for matching groups and groupings against external systems (credits to Andrew Nicols, LUNS)
- [MDL-30482](https://moodle.atlassian.net/browse/MDL-30482) - New [view glossary entries capability](https://docs.moodle.org/23/en/Capabilities/mod/glossary:view)
- [MDL-31158](https://moodle.atlassian.net/browse/MDL-31158) - New [recover grades default setting](https://docs.moodle.org/23/en/Grade_settings)
- [MDL-11378](https://moodle.atlassian.net/browse/MDL-11378) - New [SMTP security email setting](https://docs.moodle.org/23/en/Messaging_settings)
- [MDL-31654](https://moodle.atlassian.net/browse/MDL-31654) - When uploading users with custom profile menu fields, fields are now uploaded by value rather than by index. Such values are now validated.
- [MDL-33122](https://moodle.atlassian.net/browse/MDL-33122) - In a fresh install, more repositories are enabled by default. Default enabled repositories are Server files, Recent files, Upload a file, URL downloader, Private files, Wikimedia and YouTube.
- [MDL-27469](https://moodle.atlassian.net/browse/MDL-27469) - SCORM activities now correctly work with activity completion.
- [MDL-22895](https://moodle.atlassian.net/browse/MDL-22895) - Calendar events for a course are backed up and restored.
- [MDL-19125](https://moodle.atlassian.net/browse/MDL-19125) - The ability to add activities/resources to a course is now controlled by capabilities.
- [MDL-31014](https://moodle.atlassian.net/browse/MDL-31014) - The Glossary approval page now has a new page format.
- [MDL-29615](https://moodle.atlassian.net/browse/MDL-29615) - A setting has been added that prevents users from overriding their default email address with another in their messaging settings.
- [MDL-31854](https://moodle.atlassian.net/browse/MDL-31854) - The total grade column is now more prominent on the Quiz grades report.
- [MDL-29624](https://moodle.atlassian.net/browse/MDL-29624) - [Media embedding settings](https://docs.moodle.org/23/en/Media_embedding), applicable in a number of areas, are now applied consistently across the site. These settings are now available in *Settings &gt; Site admin &gt; Appearance &gt; Media embedding*. (credits to Sam Marshall, The Open University)
- [MDL-27212](https://moodle.atlassian.net/browse/MDL-27212) - On the Tags page, redundant anchor links have been removed.
- [MDL-31351](https://moodle.atlassian.net/browse/MDL-31351) - The Splash theme has been updated.
- [MDL-31985](https://moodle.atlassian.net/browse/MDL-31985) - Text and binary field size removed from XMLDB

### Security issues[​](#security-issues "Direct link to Security issues")

All security issues that were fixed in 2.2.x and 2.1.x were also fixed in 2.3.

### For developers: API changes[​](#for-developers-api-changes "Direct link to For developers: API changes")

Abbreviated descriptions of API changes are always kept up to date in the "upgrade.txt" within each plugin area. We do this so that the information is always exactly right for the version of Moodle you are using. Changes in this release:

- [Blocks](https://github.com/moodle/moodle/blob/v2.3.0/blocks/upgrade.txt)
- [Course formats](https://github.com/moodle/moodle/blob/v2.3.0/course/format/upgrade.txt)
- [Filters](https://github.com/moodle/moodle/blob/v2.3.0/filter/upgrade.txt)
- [Activity modules](https://github.com/moodle/moodle/blob/v2.3.0/mod/upgrade.txt)
- [Quiz access rules](https://github.com/moodle/moodle/blob/v2.3.0/mod/quiz/accessrule/upgrade.txt)
- [Quiz reports](https://github.com/moodle/moodle/blob/v2.3.0/mod/quiz/report/upgrade.txt)
- [Portfolio plugins](https://github.com/moodle/moodle/blob/v2.3.0/portfolio/upgrade.txt)
- [Question behaviour plugins](https://github.com/moodle/moodle/blob/v2.3.0/question/behaviour/upgrade.txt)
- [Question behaviour plugins](https://github.com/moodle/moodle/blob/v2.3.0/question/format/upgrade.txt)
- [Question types](https://github.com/moodle/moodle/blob/v2.3.0/question/type/upgrade.txt)
- [Repository plugins](https://github.com/moodle/moodle/blob/v2.3.0/repository/upgrade.txt)
- [Themes](https://github.com/moodle/moodle/blob/v2.3.0/theme/upgrade.txt)

#### Core API changes[​](#core-api-changes "Direct link to Core API changes")

- [MDL-31902](https://moodle.atlassian.net/browse/MDL-31902) All xxx\_get\_participants() functions are removed from core
- As a part of [MDL-32471](https://moodle.atlassian.net/browse/MDL-32471), the signature of send\_stored\_file() has been [modified](http://git.moodle.org/gw?p=moodle.git%3Ba%3Dcommitdiff%3Bh%3D796495fed29f12e4a81bd406558d8eeffd0e64ac). The last two parameters $filename and $dontdie were replaced with a single array containing additional options for the file serving. The pluginfile callbacks in plugins are supposed to transfer these options from the caller to send\_stored\_file() - see the note below.
- [MDL-28666](https://moodle.atlassian.net/browse/MDL-28666) Files API changes, added ability to create file reference using file\_storage::create\_file\_from\_reference() method, update file record attributes using stored\_file class
- [MDL-28666](https://moodle.atlassian.net/browse/MDL-28666) Repository API changes, added new APIs repository::get\_file\_reference(), repository::get\_file\_by\_reference(), repository::get\_reference\_details(), repository::send\_file(), the new APIs make serving files from external repository possible
- [MDL-33446](https://moodle.atlassian.net/browse/MDL-33446) Make sure that areas in your plugins where you DON'T want content to change have support for file references turned OFF. Some areas in Moodle core that do not support references are assignment submissions, workshop submissions, forum posts, and quiz essay questions - this is so that students are not able to update files from outside Moodle after any due date
- AJAX Flags: [MDL-32509](https://moodle.atlassian.net/browse/MDL-32509) and [MDL-32908](https://moodle.atlassian.net/browse/MDL-32908) The $CFG-&gt;enablecourseajax and $USER-&gt;ajax fields have been removed. The fields was not widely respected and all 'advanced JavaScript' should work in a progressive enhancement and accessible way. A site wide flag still exists but may be phased out in the future.
- [MDL-27982](https://moodle.atlassian.net/browse/MDL-27982) problematic non-standardised unsigned number support was removed from the database abstraction layer, all number columns in MySQL databases are automatically converted to signed, all other databases were already using signed numbers
- [MDL-31985](https://moodle.atlassian.net/browse/MDL-31985) problematic text field size support was removed was removed from the database abstraction layer, all text columns in MySQL databases are automatically converted to big sizes, all other databases were already using only one text size

#### Plugin API changes[​](#plugin-api-changes "Direct link to Plugin API changes")

- As a part of [MDL-32471](https://moodle.atlassian.net/browse/MDL-32471), the API of the plugin function xyz\_pluginfile() has been extended. There is a new array parameter passed to these callbacks containing additional options for the file serving. The array should be re-passed to send\_stored\_file(). The change is pretty trivial - see [examples](http://git.moodle.org/gw?p=moodle.git%3Ba%3Dcommitdiff%3Bh%3D261cbbacc15ef1732a357d689908c91c15e0617a).
- Activity modules can now declare support for course drag and drop upload [Implementing Course drag and drop upload support in a module](https://docs.moodle.org/dev/Implementing_Course_drag_and_drop_upload_support_in_a_module)

#### Webservice changes[​](#webservice-changes "Direct link to Webservice changes")

Few changes could break existing web service clients in 2.3 - untill this version we tried not to break anything. However these changes will make the client's developer life easier, so we prefered to do them now than later. Please take in consideration these improvements and retest your clients:

- [Error codes and Warnings](https://docs.moodle.org/dev/Errors_handling_in_web_services)
- All text fields have an additional format field as parameter and return value ([MDL-32581](https://moodle.atlassian.net/browse/MDL-32581))
- Thanks to the increasing number of contributions, we improved our [contributor web service guide](https://docs.moodle.org/dev/How_to_contribute_a_web_service_function_to_core)
- From 2.3, all web service functions integrated in master will land (when possible) in supported minor versions (e.g. 2.3.1, 2.3.2...).
- Many [fixes](http://moodle.atlassian.net/browse/MDL-31253) and new [API functions](http://moodle.atlassian.net/browse/MDL-29934).

#### Unit tests[​](#unit-tests "Direct link to Unit tests")

We have switched completely to using [PHPUnit](https://moodledev.io/general/development/tools/phpunit) for all our unit tests now. All existing simpletests have been rewritten, and new tests have been added.

We intend to move towards a completely unit-test-driven development methodology (where the tests are written first!) for significant new code, and we also encourage all developers to implement unit tests covering at least the core features of their code.

Moodle HQ run these tests on an automated basis for all new code submitted for integration, as well as on each weekly release.

Some bug fixes and improvements in [core](http://moodle.atlassian.net/browse/MDL-30247) and in the [plugin](http://moodle.atlassian.net/browse/CONTRIB-3348). Hub administrators must update their hub to the most recent version regarding [CONTRIB-3646](https://moodle.atlassian.net/browse/CONTRIB-3646).

## See also[​](#see-also "Direct link to See also")

- [User documentation of new features in Moodle 2.3](https://docs.moodle.org/23/en/Category:New_features)
- [Upgrading to Moodle 2.3](https://docs.moodle.org/23/en/Upgrading_to_Moodle_2.3) - information for admins who are upgrading from earlier versions

## Translations[​](#translations "Direct link to Translations")

- [Notes de mise à jour de Moodle 2.3](https://docs.moodle.org/fr/Notes_de_mise_%C3%A0_jour_de_Moodle_2.3)