---
title: Moodle 1.9.15 | Moodle Developer Resources
url: https://moodledev.io/general/releases/1.9/1.9.15
source: sitemap
fetched_at: 2026-02-17T16:03:47.058507-03:00
rendered_js: false
word_count: 197
summary: This document details the release notes for Moodle 1.9.15, highlighting critical security updates, general bug fixes, and the end-of-support status for this legacy version.
tags:
    - moodle-1-9-15
    - release-notes
    - security-advisory
    - bug-fixes
    - software-maintenance
    - legacy-software
category: reference
---

Unsupported Moodle Version

**This version of Moodle is no longer supported and will not receive fixes for security risks.**  
You are encouraged to [**upgrade**](https://docs.moodle.org/en/Upgrading) to a supported version of Moodle.

Release date: 28th November, 2011

Bug-fixing for general core bugs in 1.9.x has ended. Support continues for serious security issues, which is reflected in this release.

Here is [the full list of fixed issues in 1.9.15](http://moodle.atlassian.net/secure/IssueNavigator!executeAdvanced.jspa?jqlQuery=project%20%3D%20mdl%20and%20resolution%20%3D%20fixed%20AND%20fixVersion%20in%20%28%221.9.15%22%29%20ORDER%20BY%20priority%20DESC&runQuery=true&clear=true).

## Security issues[​](#security-issues "Direct link to Security issues")

- [MSA-11-0045](http://moodle.org/mod/forum/discuss.php?d=191751) - Potential to masquerade through MNet
- [MSA-11-0046](http://moodle.org/mod/forum/discuss.php?d=191752) - Insecure authentication transmission
- [MSA-11-0047](http://moodle.org/mod/forum/discuss.php?d=191754) - Possible injection attack in Calendar
- [MSA-11-0048](http://moodle.org/mod/forum/discuss.php?d=191755) - Password loss issue
- [MSA-11-0049](http://moodle.org/mod/forum/discuss.php?d=191756) - Network restriction ineffective with MNet
- [MSA-11-0054](http://moodle.org/mod/forum/discuss.php?d=191762) - Personal information leak

PLEASE NOTE: The fix for MSA-11-0054 was mistakenly not included in the first November 28 build of 1.9.15 (Nov 28) but was included in the builds on December 2. If you grabbed the build very early then you might not have that fix.

## Fixes and improvements[​](#fixes-and-improvements "Direct link to Fixes and improvements")

- [MDL-29529](https://moodle.atlassian.net/browse/MDL-29529) - Fixed database error when assignments were sorted by status
- [MDL-16553](https://moodle.atlassian.net/browse/MDL-16553) - Student can see response file for Advanced uploading assignment with no grade
- [MDL-29991](https://moodle.atlassian.net/browse/MDL-29991) - Moodle 1.9 servers still expect the "confirmed" field from MNet

## Translations[​](#translations "Direct link to Translations")

- [French version of this page](https://docs.moodle.org/19/fr/Notes_de_mise_%C3%A0_jour_de_Moodle_1.9.15)
- [Notas de Moodle 1.9.15](https://docs.moodle.org/es/Notas_de_Moodle_1.9.15)