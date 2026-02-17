---
title: Moodle 2.1 | Moodle Developer Resources
url: https://moodledev.io/general/releases/2.1
source: sitemap
fetched_at: 2026-02-17T16:04:27.131799-03:00
rendered_js: false
word_count: 568
summary: This document outlines the major features, security updates, and technical changes introduced in the Moodle 2.1 release. It provides guidance on upgrading from previous versions and details specific API modifications for developers.
tags:
    - moodle-2-1
    - release-notes
    - question-engine
    - mobile-support
    - backup-restore
    - api-changes
    - upgrade-guide
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

## Moodle 2.1[​](#moodle-21 "Direct link to Moodle 2.1")

Released: 1st July 2011

### Major new features[​](#major-new-features "Direct link to Major new features")

#### New question engine[​](#new-question-engine "Direct link to New question engine")

- Moodle question system has been rewritten to make it much more robust and to support lots of new possible functionality.
- See summary of changes at the [New question engine](https://docs.moodle.org/dev/Moodle_2.1_release_notes/New_question_engine) page and more details in the tracker [MDL-20636](https://moodle.atlassian.net/browse/MDL-20636).
- Warning: This change requires a major database upgrade. If you have a lot of question attempts in your site, you probably need to [plan your upgrade in stages](https://docs.moodle.org/21/en/Upgrading_to_Moodle_2.1#Planning_the_question_engine_upgrade), using some extra code that is not in the core system.
- Backward compatibility warning: *Random short-answer matching* question type was moved out of the main Moodle distribution.

#### Ability to restore the course contents from Moodle 1.9 backup files[​](#ability-to-restore-the-course-contents-from-moodle-19-backup-files "Direct link to Ability to restore the course contents from Moodle 1.9 backup files")

- Course backup files created in Moodle 1.9 can be now restored during the normal restore process.
- No user data (like forum posts, grades, submissions, ...) are supported yet. Blocks are not restored yet.
- See [MDL-22414](https://moodle.atlassian.net/browse/MDL-22414) for details.

#### Support for mobile devices[​](#support-for-mobile-devices "Direct link to Support for mobile devices")

- Moodle 2.1 comes with a built-in web service designed for mobile applications (required to run the official [Moodle app](https://docs.moodle.org/dev/Mobile_app))
- See [MDL-27551](https://moodle.atlassian.net/browse/MDL-27551) and [Enable mobile web services documentation](https://docs.moodle.org/en/Enable_mobile_web_services) for details
- [MDL-25394](https://moodle.atlassian.net/browse/MDL-25394) Improved Support for Mobile Themes and Browser Detection

### Other highlights[​](#other-highlights "Direct link to Other highlights")

- [MDL-11288](https://moodle.atlassian.net/browse/MDL-11288) Ability to copy (or clone) an activity
- [MDL-27428](https://moodle.atlassian.net/browse/MDL-27428) Ability to navigate navigation/settings menu and dock with keyboard
- [MDL-26784](https://moodle.atlassian.net/browse/MDL-26784) Improved plugins check/overview page
- [MDL-27500](https://moodle.atlassian.net/browse/MDL-27500) Upgraded TinyMCE to the latest version 3.4.2
- [MDL-26105](https://moodle.atlassian.net/browse/MDL-26105) User friendly block settings and help information
- [MDL-27251](https://moodle.atlassian.net/browse/MDL-27251) New performance setting for calculating an appropriate timeout during large cURL requests
- [MDL-25805](https://moodle.atlassian.net/browse/MDL-25805) Friendlier navigation for parent roles to see mentees in courses
- [MDL-27577](https://moodle.atlassian.net/browse/MDL-27577) Daylight saving should be calculated for users having string timezone
- [MDL-27171](https://moodle.atlassian.net/browse/MDL-27171) Messaging Improvements: Site administrators can now control which message delivery methods can be used for each message type. (In 2.0 students could switch off notifications. In 2.1 this can be overidden)

### Security issues[​](#security-issues "Direct link to Security issues")

There were no significant security issues fixed in this release.

### Upgrading[​](#upgrading "Direct link to Upgrading")

When upgrading to Moodle 2.1, you must first upgrade to Moodle 1.9 or (preferably) 2.0. We advise that you test the upgrade first on a COPY of your production site, to make sure it works as you expect.

Please also check that you have PHP 5.3.2 or later, as the minimum required version has increased since Moodle 2.0.

For further information, see [Upgrading to Moodle 2.1](https://docs.moodle.org/21/en/Upgrading_to_Moodle_2.1).

### For developers: API changes[​](#for-developers-api-changes "Direct link to For developers: API changes")

- The new question engine changes the API for question types. See [Developing a Question Type](https://docs.moodle.org/dev/Developing_a_Question_Type).
- The new question engine changes the API for activity modules that use the question bank. See [Using the question engine from module](https://docs.moodle.org/dev/Using_the_question_engine_from_module).
- There is a new API available for activity modules to support restore of 1.9 backup files. See [Backup 1.9 conversion for developers](https://docs.moodle.org/dev/Backup_1.9_conversion_for_developers)
- The Messaging API now allows plugin creators to specify default message providers for message outputs. See [Messaging 2.0 improvements#Adding new message type](https://docs.moodle.org/dev/Messaging_2.0_improvements#Adding_new_message_type)
- [MDL-28166](https://moodle.atlassian.net/browse/MDL-28166) Note that the two events triggered by the quiz module (quiz\_attempt\_started and quiz\_attempt\_submitted) changed slightly to follow a more consistent naming scheme. We do not believe they were used much, so we decided to fix them now, so we could have a nice, stable API in the future.

## See also[​](#see-also "Direct link to See also")

- [User documentation of new features in Moodle 2.1](https://docs.moodle.org/21/en/Category:New_features)

## Translations[​](#translations "Direct link to Translations")

- [Notas de Moodle 2.1](https://docs.moodle.org/es/Notas_de_Moodle_2.1)
- [Notes de mise à jour de Moodle 2.1](https://docs.moodle.org/fr/Notes_de_mise_%C3%A0_jour_de_Moodle_2.1)