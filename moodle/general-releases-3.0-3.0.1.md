---
title: Moodle 3.0.1 | Moodle Developer Resources
url: https://moodledev.io/general/releases/3.0/3.0.1
source: sitemap
fetched_at: 2026-02-17T16:08:31.51731-03:00
rendered_js: false
word_count: 402
summary: Detailed release notes for Moodle 3.0.1 highlighting its support for PHP 7.0 and the resulting improvements in system performance and memory usage.
tags:
    - moodle-release
    - php-7
    - performance-benchmarks
    - release-notes
    - bug-fixes
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 21 December 2015

Here is [the full list of fixed issues in 3.0.1](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%223.0.1%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

## Highlights[​](#highlights "Direct link to Highlights")

Moodle 3.0.1 is a special release outside of the normal release schedule. The main highlight is support of PHP 7.0. This is the new major version of the programming language Moodle is written in; it has significantly better performance but at the same time lots of changes in the engine. Please note that Moodle 2.9 will show errors if run on PHP 7.

Before upgrading to PHP 7 version on production servers, you are recommended to **test all plugins thoroughly**. See [Moodle and PHP7](https://docs.moodle.org/dev/Moodle_and_PHP7) for developer documentation.

PHP 7 was released on 3 December 2015 and is still very young. Not all libraries and/or drivers are available yet for PHP 7. For example, **there are no drivers for SQL\*Server**. Other drivers required by your plugins may also be missing.

**PHP 7 compatibility makes Moodle faster**

![php7 time logging in.png](https://moodledev.io/assets/images/php7_time_logging_in-ffdafc1c84a0c3e85cd53017ca562ffe.png)

![course-time-300x177.png](data:image/png;base64,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)

20% faster when logging in*

59% faster when loading the course page*

**PHP 7 compatibility significantly reduces memory used**

![php7 memory logging in.png](https://moodledev.io/assets/images/php7_memory_logging_in-77795af5374d6c2cce562de320b74a87.png)

![php7 memory viewing course.png](data:image/png;base64,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)

42% less memory used when logging in*

38% less memory used when viewing a course*

: * Test results obtained on a test Moodle instance with one course in topics format with over 100 activities and resources.

## Other fixes and improvements[​](#other-fixes-and-improvements "Direct link to Other fixes and improvements")

- [MDL-44330](https://moodle.atlassian.net/browse/MDL-44330) - When using assignment grading in several tabs the links to individual students grades work correctly
- [MDL-37834](https://moodle.atlassian.net/browse/MDL-37834) - Excel can be used to edit the assignment offline grading worksheet
- [MDL-42571](https://moodle.atlassian.net/browse/MDL-42571) - Edit PDF: Fixed bug with viewing a second PDF on the assignment grading page
- [MDL-43069](https://moodle.atlassian.net/browse/MDL-43069) - Assignment grading: "Submission comments" fail to expand if you hide the "file submissions" column
- [MDL-37308](https://moodle.atlassian.net/browse/MDL-37308) - Uploaded PNG images preserve transparency when resized
- [MDL-49490](https://moodle.atlassian.net/browse/MDL-49490) - Fixed export to portfolio link in assignment with additional files
- [MDL-52194](https://moodle.atlassian.net/browse/MDL-52194) - Fixed Flowplayer not working with insecure configuration of request\_order

## For developers[​](#for-developers "Direct link to For developers")

- [MDL-51582](https://moodle.atlassian.net/browse/MDL-51582) - Switch to grunt to compile LESS as recess is no longer maintained

## Security issues[​](#security-issues "Direct link to Security issues")

There are no security issues in this release. Security issues will be included in Moodle 3.0.2 which is due for release in January 2016.

## Translations[​](#translations "Direct link to Translations")

- [Notes de mise à jour de Moodle 3.0.1](https://docs.moodle.org/fr/Notes_de_mise_%C3%A0_jour_de_Moodle_3.0.1)
- [Notas de Moodle 3.0.1](https://docs.moodle.org/es/Notas_de_Moodle_3.0.1)