---
title: Moodle 5.3 | Moodle Developer Resources
url: https://moodledev.io/general/releases/5.3
source: sitemap
fetched_at: 2026-02-17T16:17:31.217012-03:00
rendered_js: false
word_count: 321
summary: This document outlines the release timeline and system requirements for Moodle 5.3.0, including supported PHP versions, database servers, and web browsers.
tags:
    - moodle
    - release-notes
    - system-requirements
    - server-configuration
    - database-compatibility
    - browser-support
category: reference
---

Unreleased Moodle Version

**This version of Moodle has not yet been released.**  
The code freeze date for this release is 24 August 2026.

Release date: 5 October 2026

Here is [the full list of fixed issues in 5.3.0](https://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20AND%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%225.3%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

If you are upgrading from a previous version, please see [Upgrading](https://docs.moodle.org/en/Upgrading) in the user docs.

## Server requirements[​](#server-requirements "Direct link to Server requirements")

These are just the minimum supported versions. We recommend keeping all of your software and operating systems up-to-date.

- Moodle upgrade: Moodle 4.5 or later.
- PHP version: minimum PHP 8.3.0 *Note: minimum PHP version was increased in Moodle 5.2*. PHP 8.4.x is supported too. See [PHP](https://moodledev.io/general/development/policies/php) for details.
- PHP extension **sodium** is required. See [Environment - PHP extension sodium](https://docs.moodle.org/en/Environment_-_PHP_extension_sodium).
- PHP setting **max\_input\_vars** must be &gt;= 5000. For further details, see [Environment - max input vars](https://docs.moodle.org/en/Environment_-_max_input_vars).
- PHP variants: Only 64-bit versions of PHP are supported. *Note: Changed since 4.1*.

### Database requirements[​](#database-requirements "Direct link to Database requirements")

Moodle supports the following database servers. Again, version numbers are just the minimum supported version. We recommend running the latest stable version of any software.

DatabaseMinimum versionRecommended[PostgreSQL](http://www.postgresql.org/)15 (last increased in Moodle 5.1)Latest[MySQL](http://www.mysql.com/)8.4 (last increased in Moodle 5.0)Latest[MariaDB](https://mariadb.org/)10.11.0 (last increased in Moodle 5.0)Latest[Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)[8.0](#aurora-mysql-compatibility-version)Latest[Microsoft SQL Server](http://www.microsoft.com/en-us/server-cloud/products/sql-server/)2017Latest

Please note that Oracle Database is no longer supported from Moodle LMS 5.0.

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