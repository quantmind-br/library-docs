---
title: Plugin QA prechecks | Moodle Developer Resources
url: https://moodledev.io/general/community/plugincontribution/guardians/qaprechecks
source: sitemap
fetched_at: 2026-02-17T15:57:53.229818-03:00
rendered_js: false
word_count: 382
summary: This document explains the process and technical requirements for performing quality assurance (QA) prechecks on Moodle plugins submitted for community approval. It details the test environment setup, step-by-step review workflow, and specific criteria for evaluating plugin stability and metadata.
tags:
    - moodle-plugins
    - quality-assurance
    - plugin-approval
    - testing-environment
    - community-contribution
    - plugin-review
category: guide
---

Plugin QA prechecks are for testing the functionality of plugins submitted for approval in the Moodle Plugins directory. Together with [code prechecks](https://moodledev.io/general/community/plugincontribution/codeprechecks), they are part of the plugin [approval process](https://moodledev.io/general/community/plugincontribution#sharing-code-in-the-plugins-directory).

Moodle community members with experience in setting up a local Moodle test environment can help with plugin QA prechecks. If you would like to help, please contact David Mudrák [david@moodle.com](mailto:david@moodle.com)

## QA environment setup[​](#qa-environment-setup "Direct link to QA environment setup")

To perform plugin QA prechecks, you need to have a test Moodle site (normally the latest stable version) installed locally. Your test site should have

- Developer debugging enabled with debugging messages displayed in order to report all PHP notices, warnings and errors spotted during plugin installation and usage.
- `$CFG->prefix` set to a non-default value, such as "m\_" or "mqa\_". This allows to catch cases when the default "mdl\_" prefix is hard-coded in PHP.

In addition, if possible the site should run on the PostgreSQL database engine to catch potential MySQL-specific SQL statements in the code.

## Process[​](#process "Direct link to Process")

1. Choose a plugin needing an initial review from the [list of plugins awaiting approval](https://moodle.org/plugins/report/index.php?report=pendingapproval_plugins) (access restricted to members of the [Plugins guardians](https://moodledev.io/general/community/plugincontribution/guardians) group).
2. To show that you are going to perform the QA prechecks, set yourself as the plugin approval issue assignee (CONTRIB-xxx as mentioned at the plugin page comments area).
3. Download and install it on your test site then perform the QA prechecks as listed below.
4. Add a comment to the plugin approval issue with your findings using the 'Plugin QA checklist' canned response.
5. If you detect any problems with the plugin, add a comment to the plugin page asking the plugin developer to look at the plugin approval issue.
6. Once everything is fine, add a comment to the plugin approval issue 'Congratulations, your plugin passes the metadata and usability checks. :-) Coding checks will be done soon.'

## QA prechecks[​](#qa-prechecks "Direct link to QA prechecks")

1. Does the plugin have all the appropriate metadata as described in the [Plugin contribution checklist](https://moodledev.io/general/community/plugincontribution/checklist)?
2. Does the plugin install nicely and not break or otherwise negatively affect the site functionality (anti-regression test)? This also checks that all eventual dependencies are already available in the plugins directory.
3. If possible (e.g. if no complex integration with an external system is needed), test the actual functionality of the plugin to see it works as described (feature test).

<!--THE END-->

- [QA environment setup](#qa-environment-setup)
- [Process](#process)
- [QA prechecks](#qa-prechecks)