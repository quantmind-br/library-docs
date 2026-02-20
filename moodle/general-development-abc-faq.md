---
title: Developer FAQ | Moodle Developer Resources
url: https://moodledev.io/general/development/abc/faq
source: sitemap
fetched_at: 2026-02-17T15:58:45.34125-03:00
rendered_js: false
word_count: 786
summary: This document serves as an introductory FAQ and resource guide for new Moodle developers, providing essential information on environment setup, coding standards, and core development processes. It directs users toward technical resources for database management, plugin creation, and community support channels.
tags:
    - moodle-development
    - getting-started
    - plugin-development
    - database-api
    - coding-standards
    - developer-resources
category: guide
---

## Help for new coders[​](#help-for-new-coders "Direct link to Help for new coders")

### Where can I download Moodle?[​](#where-can-i-download-moodle "Direct link to Where can I download Moodle?")

There are various ways you can download and install Moodle on your system.

- Visit our [download page](https://download.moodle.org/)
- Clone from [Moodle's Git repository](https://github.com/moodle/moodle) or find out more about using [Git for developers](https://moodledev.io/docs/5.2/guides/git)

### Where can I start?[​](#where-can-i-start "Direct link to Where can I start?")

This very website is a great place to find out more how you can be a Moodle developer. Navigate the various sections to find out more.

- [Guides](https://moodledev.io/docs/5.2) for Developer Documentation
- [Community](https://moodledev.io/general/community/contribute) for more information on how you can contribute
- [Coding](https://moodledev.io/general/development/gettingstarted) for Moodle coding standards
- [Process](https://moodledev.io/general/development/process) to learn how the development cycle works

#### Extend your learning[​](#extend-your-learning "Direct link to Extend your learning")

- [Moodle Academy](https://moodle.academy/) online courses
- MoodleBites for Developers online courses [Level 1](https://www.moodlebites.com/mod/page/view.php?id=24546) and [Level 2](https://www.moodlebites.com/mod/page/view.php?id=19542)

### Who can I ask for help?[​](#who-can-i-ask-for-help "Direct link to Who can I ask for help?")

The Moodle community is an active group of teachers and developers that have most likely encountered many of the same questions you might have. We encourage you to reach out and get involved in the available ways provided on our [Support channels](https://moodledev.io/general/channels) page.

### How do I create a patch?[​](#how-do-i-create-a-patch "Direct link to How do I create a patch?")

If you have made some changes to the code that you would like to share with the community, learn how to [create a patch](https://moodledev.io/docs/5.2/guides/git#preparing-a-patch).

### How do I assign an issue to myself?[​](#how-do-i-assign-an-issue-to-myself "Direct link to How do I assign an issue to myself?")

Before you can become the assignee on an issue you must work on an issue and have it integrated, and closed. Typically this may be with the help of another developer.

When working on this issue it is important that you **do not** set the assignee at all so that it can be easily discovered and you can be promoted within the Tracker.

### How do I create a module or plugin?[​](#how-do-i-create-a-module-or-plugin "Direct link to How do I create a module or plugin?")

Use the following resources to help get you started with modules and plugins.

- [Plugin tutorial](https://docs.moodle.org/dev/Tutorial)
- [Plugin types](https://moodledev.io/docs/5.2/apis/plugintypes)

### Is there any information on backup and restore?[​](#is-there-any-information-on-backup-and-restore "Direct link to Is there any information on backup and restore?")

Learn how to use Moodle's [backup](https://moodledev.io/docs/5.2/apis/subsystems/backup) and [restore](https://moodledev.io/docs/5.2/apis/subsystems/backup/restore) APIs.

### How can I customise Moodle with my own plugin?[​](#how-can-i-customise-moodle-with-my-own-plugin "Direct link to How can I customise Moodle with my own plugin?")

[Local plugins](https://moodledev.io/docs/5.2/apis/plugintypes/local) are a great way to customise Moodle when no standard plugin fits.

## Moodle's database[​](#moodles-database "Direct link to Moodle's database")

### Where can I see a schema for the structure of the Moodle database?[​](#where-can-i-see-a-schema-for-the-structure-of-the-moodle-database "Direct link to Where can I see a schema for the structure of the Moodle database?")

[Database schema introduction](https://moodledev.io/docs/5.2/apis/core/dml/database-schema) gives a high level overview of the database schema.

Because of Moodle's modular nature, there is no single, detailed representation of the full database schema. Instead, the tables for each part of Moodle are defined in a database-neutral XML format in each part of Moodle (see [XMLDB](https://moodledev.io/general/development/tools/xmldb)). Look for files called `install.xml` located in folders called `db` throughout your Moodle installation.

Alternatively, log in as an administrator on your Moodle site and go to *Site administration -&gt; Development -&gt; XMLDB editor*. Use the *Doc* link to see automatically generated documentation built from `install.xml` files.

See also [XMLDB documentation](https://docs.moodle.org/dev/XMLDB).

### How do I find out the currently-logged-on user?[​](#how-do-i-find-out-the-currently-logged-on-user "Direct link to How do I find out the currently-logged-on user?")

The global object `$USER` contains various properties pertaining to the currently logged in user. Here are just a few examples.

- First name `$USER->firstname`
- Last name `$USER->lastname`
- User ID `$USER->id`

### How do I find out the current course?[​](#how-do-i-find-out-the-current-course "Direct link to How do I find out the current course?")

Just like the global object `$USER`, there is a global object called `$COURSE` which contains details about a course.

- Course ID `$COURSE->id`
- Course name `$COURSE->fullname`

### How do I insert/retrieve records in the database?[​](#how-do-i-insertretrieve-records-in-the-database "Direct link to How do I insert/retrieve records in the database?")

Use the global `$DB` object, as described in the [Data manipulation API](https://moodledev.io/docs/5.2/apis/core/dml) documentation, to insert and retrieve data without having to create your own database connection.

### How do I get/set configuration settings?[​](#how-do-i-getset-configuration-settings "Direct link to How do I get/set configuration settings?")

#### config table[​](#config-table "Direct link to config table")

To get config values you would typically access the global `$CFG` object directly, which is automatically created by the core Moodle scripts. To set these **main** config values use `set_config($name, $value)`. The values are stored in the Moodle *config* database table, but these functions take care of cacheing on your behalf, so you should always use these rather than fetching the records directly.

#### config\_plugin table[​](#config_plugin-table "Direct link to config_plugin table")

There is also a second table of config settings specifically for plugins called *config\_plugin*. These are not automatically loaded into the `$CFG` object. To get these you would use `get_config($plugin, $name)`. To set them use `set_config($name, $value, $plugin)`.

On top of those global configuration values, individual blocks may also have a configuration object associated with it (the data is serialised and stored in the *block\_instance* table). Within blocks, this data is automatically loaded into the *config* attribute of the block.

### How do I migrate my Moodle site?[​](#how-do-i-migrate-my-moodle-site "Direct link to How do I migrate my Moodle site?")

There may be times when you need to move your Moodle site from one server to another. Find out all about [migrating your Moodle site](https://docs.moodle.org/en/Moodle_migration).

## Learn more[​](#learn-more "Direct link to Learn more")

For a comprehensive introduction to developing with Moodle, complete the [Developer pathway course](https://moodle.academy/course/index.php?categoryid=4) over at [Moodle Academy](https://moodle.academy/) where you will learn:

- How to set up your Moodle development environment
- Understand Moodle's modular architecture
- How to update Moodle plugins
- Moodle security essentials
- Implement accessibility features
- How to unit test your Moodle site