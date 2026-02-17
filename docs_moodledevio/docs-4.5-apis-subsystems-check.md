---
title: Check API | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/subsystems/check
source: sitemap
fetched_at: 2026-02-17T15:13:17.809493-03:00
rendered_js: false
word_count: 1833
summary: This document describes the Moodle Check API, a framework for conducting runtime tests to verify system health, security, and configuration. It explains the various types of checks, their possible result states, and how developers can create custom checks for their plugins.
tags:
    - moodle-development
    - check-api
    - runtime-testing
    - system-health
    - plugin-development
    - monitoring
category: api
---

A *Check* is a runtime test to make sure that something is working well. You can think of Checks as similar and complimentary to the [PHPUnit](https://moodledev.io/general/development/tools/phpunit) and [Acceptance testing](https://moodledev.io/general/development/tools/behat) but the next layer around them, and performed at run time rather than development, or build time.

Like other forms of testing the tests themselves should be easy to read, to reason about, and to confirm as valid.

note

Many types of runtime checks cannot be unit tested, and often the checks **are** the test.

Checks can be used for a variety of purposes including:

- configuration checks
- security checks
- status checks
- performance checks
- health checks

Moodle has had various types of checks and reports for a long time but they were inconsistent and not machine readable. In Moodle 3.9 they were unified under a single Check API which also enabled plugins to cleanly define their own additional checks. Some examples include:

- a password policy plugin could add a security check
- a custom authentication plugin can add a check that the upstream identity system can be connected to
- a MUC store plugin could add a performance check Having these centralized and with a consistent contract makes it much easier to ensure the whole system is running smoothly. This makes it possible for an external integration with monitoring systems such as Nagios / Icinga. The Check API is exposed as an NPRE compliance cli script:

## Result states of a check[​](#result-states-of-a-check "Direct link to Result states of a check")

StatusMeaningExampleN/AThis check doesn't apply - but we may still want to expose the checksecure cookies setting is disabled because site is not httpsOkA component is configured, working and fast.ldap can bind and return value with low latencyInfoA component is OK, and we may want to alert the admin to something non urgent such as a deprecation, or something which needs to be checked manually.UnknownWe don't yet know the state. eg it may be very expensive so it is run using the Task API and we are waiting for the answer. NOTE: unknown is generally a bad thing and is semantically treated as an error. It is better to have a result of Unknown until the first result happens, and from then on it is Ok, or perhaps Warning or Error if the last known result is getting stale. If you are caching or showing a stale result you should expose the time of this in the result summary text.A complex user security report is still running for the first time.WarningSomething is not ideal and should be addressed, eg usability or the speed of the site may be affected, but it may self heal (eg a load spike)auth\_ldap could bind but was slower than normalErrorSomething is wrong with a component and a feature is not workingauth\_ldap could not connect, so users cannot start new sessionsCriticalAn error which is affecting everyone in a major wayCannot read site data or the database, the whole site is down

How the various states are then leveraged is a local decision. A typical policy might be that health checks with a status of 'Error' or 'Critical' will page a system administrator 24/7, while 'Warning' only pages during business hours.

## Check types and reports[​](#check-types-and-reports "Direct link to Check types and reports")

Checks are broken down into types, which roughly map to a step in the life cycle of your Moodle System.

### Environmental checks[​](#environmental-checks "Direct link to Environmental checks")

Available from */admin/environment.php*, environmental checks make sure that a Moodle instance is fully configured.

This page is a potential candidate to move to the new Check API but it slightly more complex than the other checks so it hasn't been tackled yet. It would be a deeper change and this is intrinsically part of the install and upgrade system. It is not as critical to refactor as it is already possible for a plugin to declare its own checks, via either declarative [Environment checking](https://docs.moodle.org/dev/Environment_checking) or programmatically with a custom check:

### Configuration checks[​](#configuration-checks "Direct link to Configuration checks")

Available from */admin/index.php?cache=1*, the Admin notifications page performs a mixture of checks, including security, status, and performance checks.

None of these checks are as exhaustive as the checks in the reports below. It also does additional checks including whether the web services for the Moodle Mobile App are enabled, and whether the site has been registered.

### Security checks (security)[​](#security-checks-security "Direct link to Security checks (security)")

Available from */report/security/index.php*, these checks make sure that a Moodle instance is hardened correctly for your needs.

For more information see [MDL-67776](https://moodle.atlassian.net/browse/MDL-67776).

### Status checks (status)[​](#status-checks-status "Direct link to Status checks (status)")

Available from */report/status/index.php*, a status check is an 'in the moment' test and covers operational tests such as 'can moodle connect to ldap'. The main core status checks are that cron is running regularly and there has been no failed tasks.

Important

It is critical to understand that Status checks are conceptually defined at the level of the application and not at a lower host level such as a docker container or node in a cluster. Checks should be defined so that whichever instance you ask you should get a consistent answer. DO NOT use the Status Checks to detect containers which need to be reaped or restarted. If you do, any status errors may mean all containers will simultaneously be marked for reaping.

An additional status check is likely the most common type of check a plugin would define. Especially a plugin that connects to a 3rd party service. If the concept of 'OK' requires some sort of threshold, eg network response within 500ms, then that threshold should be managed by the plugin and optionally exposed as a admin setting. The plugin may choose to have different thresholds for Warning / Error / Critical. When designing a new Status Check be mindful that it needs to be actionable, for instance if you are asserting that a remote domain is available and it goes down, which then alerts your infrastructure team, there isn't much they can do about it if it isn't their domain. If it is borderline then make things like this configurable so that each site has to option of tune their own policies of what should be considered an issue or not.

For more information see [MDL-47271](https://moodle.atlassian.net/browse/MDL-47271).

### Performance checks (performance)[​](#performance-checks-performance "Direct link to Performance checks (performance)")

Available from */report/performance/index.php*, each check might simply check for certain settings which are known to slow things down, or it might actually do some sort of test like multiple reads and writes to the db or filesystem to get a performance metric.

## Implementing a new check[​](#implementing-a-new-check "Direct link to Implementing a new check")

### A check class[​](#a-check-class "Direct link to A check class")

And make a new check class in `mod/myplugin/classes/check/foobar.php` and the only mandatory method is `get_result()`. By default it will use a set language string but you can override the `get_name()` method to reuse an existing string.

mod/myplugin/lang/en/myplugin.php

```
$string['checkfoobar']='Check the foos to make sure they are barred';
```

mod/myplugin/classes/check/foobar

```
<?php
namespacemod_myplugin\check;
usecore\check\check;
usecore\check\result;

classfoobarextendscheck{

publicfunctionget_action_link():?\action_link{
$url=new\moodle_url('/mod/myplugin/dosomething.php');
returnnew\action_link($url,get_string('sitepolicies','admin'));
}

publicfunctionget_result():result{
if(some_check()){
$status=result::ERROR;
$summary=get_string('check_foobar_error','mod_myplugin');
}else{
$status=result::OK;
$summary=get_string('check_foobar_ok','mod_myplugin');
}
$details=get_string('check_details','mod_myplugin');
returnnewresult($status,$summary,$details);
}
}
```

### The result summary[​](#the-result-summary "Direct link to The result summary")

The summary could change depending on the result of the check but for a simple check might be a fixed string, not html. Try to keep the summary to 1 line as this might typically be the thing which gets passed through to a paging system and could be truncated.

### The details[​](#the-details "Direct link to The details")

Unlike the summary the details is allowed and encouraged to be html. Often it will be a bullet list, or a table of the things that it asserted which make up the check.

### The action link[​](#the-action-link "Direct link to The action link")

The action link is the place to go to help fix the issue. It should be as specific as possibly, such as a deep link into an admin settings page, and can include hash anchors.

### lib.php callback[​](#libphp-callback "Direct link to lib.php callback")

First decide if and when your new check(s) should be shown. Should it be present if your plugin is disabled? If you do not want it show if disabled then do not return it in callback below. If you do want it to show when disabled, but a check result doesn't make much sense, then you can return a value of NA.

Next decide on what type of check it should be which determines what report it will be included in. Some checks might make sense to be reused with more than one report, eg it could be in both Status and Performance.

Implement the right callback in lib.php for the report you want to add it to, and return an array (usually with only 1 item) of check objects:

/mod/myplugin/lib.php

```
functionmod_myplugin_security_checks():array{
return[new\mod_myplugin\check\foobar()];
}
```

### Multiple instances of checks[​](#multiple-instances-of-checks "Direct link to Multiple instances of checks")

Checks have been designed to be dynamic so you can return different checks depending on configuration, so auth\_ldap would not return a check if the plugin is not enabled. Hypothetically if auth\_ldap could be configured with 5 ldap servers then you could return 5 independent checks for each remote connection, each with different labels and information.

If you plan to return multiple instances of a check class, make sure that each instance has a unique id.

```
functionmod_myplugin_security_checks():array{
return[
new\mod_myplugin\check\foobar('one'),
new\mod_myplugin\check\foobar('two'),
];
}
```

Set the internal id in a way which is unique across all instances in your components namespace:

```
namespacemod_myplugin\check;

classfoobarextends\core\check\check{
protected$id='';

publicfunction__construct($id){
$this->id="foobar{$id}";
}

publicfunctionget_id():string{
return$this->id;
}
...
}
```

### Make checks as fast as practical[​](#make-checks-as-fast-as-practical "Direct link to Make checks as fast as practical")

As many checks will be run and compiled into a report we want the checks themselves to be simple and as fast as possible. For instance an auth\_ldap check while authenticating an end user could have a timeout of 60 seconds, and the check could warn if it takes more than 2 seconds. But the check could have a hard timeout of say 5 seconds and have a result status of ERROR for 5 or more seconds.

### Lazy loading expensive result details[​](#lazy-loading-expensive-result-details "Direct link to Lazy loading expensive result details")

Checks can provide details on a check, such as the complete list of bad records. Generally this type of information might be expensive to produce so you can defer this lookup until get\_details() is called specifically rather than setting this in the constructor. It will only be loaded on demand and shown when you drill down into the check details page.

```
<?php

namespacemod_myplugin\check;

classfoobarextends\core\check\check{
publicfunctionget_result():result{
returnnewfoobar_result();
}
}
```

```
classfoobar_resultextends\core\check\result{
...
publicfunctionget_details():string{
// Do expensive lookups in here.
}
}
```

For a real example see:

[https://github.com/moodle/moodle/blob/main/lib/classes/check/access/riskxss\_result.php](https://github.com/moodle/moodle/blob/main/lib/classes/check/access/riskxss_result.php)

### Asynchronous checks[​](#asynchronous-checks "Direct link to Asynchronous checks")

Some checks are by their nature asynchronous. For instance having moodle send an email to itself and then having it processed by the inbound mail handler to make it's properly configured (see [MDL-48800](https://moodle.atlassian.net/browse/MDL-48800)). In cases like these please make sure the age or staleness of the check is shown in the summary, and you should also consider turning the result status into a warning if the result is too old. If appropriate make the threshold a configurable admin setting.

## Reusing checks inside admin setting pages[​](#reusing-checks-inside-admin-setting-pages "Direct link to Reusing checks inside admin setting pages")

Quite often you have a plugin that includes some sort of status check in the admin settings page where you configure the plugin. For example you can add the api keys for a service and it shows you right in the settings page if the connection settings work.

You can re-use the Check api to get this nice feature for free:

```
$temp->add(newadmin_setting_check(
'antivirus/checkantivirus',
new\core\check\environment\antivirus(),
));
```

info

These checks are performed asynchronously, and only if the check is visible, so will not slow down the whole admin tree which is often a downside of implementing this manually.

You can also use checks which are not linked into one of the reports. This means you can check the connection while configuring the plugin, but before it is enabled, and only add the check to the status report page once the plugin is enabled.

## See also[​](#see-also "Direct link to See also")

- [Performance overview](https://docs.moodle.org/en/Performance_overview) user docs