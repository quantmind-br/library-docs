---
title: jQuery | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/guides/javascript/jquery
source: sitemap
fetched_at: 2026-02-17T15:05:22.663147-03:00
rendered_js: false
word_count: 371
summary: This document outlines Moodle's policy and technical methods for incorporating jQuery and jQuery UI, emphasizing that native ES6 modules are preferred for modern development.
tags:
    - moodle
    - javascript
    - jquery
    - jquery-ui
    - amd-modules
    - es6-modules
    - frontend
category: guide
---

The use of jQuery in new code is strongly discouraged and is not generally accepted in core. Specific exceptions to this rule are made on a case-by-case basis, generally when interfacing with legacy code which expects to be passed a jQuery object.

Moodle has supported the use of native ES6-style modules and constructs since Moodle 3.8. These are transpiled into supported code.

This page explains the recommended way to use jQuery in core and plugins, although other [older](https://docs.moodle.org/dev/jQuery_pre2.9) methods of including jQuery will still work these are no longer considered to be supported.

## Why do we need JQuery?[​](#why-do-we-need-jquery "Direct link to Why do we need JQuery?")

important

**We do not need jQuery and its use is discouraged**. The following is legacy documentation and no longer current advice.

JQuery is useful for handling browser inconsistencies, and for utility functions that would otherwise be duplicated all over the code. Some particular things that JQuery is good at are:

- DOM Manipulations
- Promises ($.Deferred)
- Ajax

## How to use JQuery[​](#how-to-use-jquery "Direct link to How to use JQuery")

JQuery is available via an AMD Module import and is available to all AMD JavaScript.

To make use of JQuery, either list it as a dependency of your module, or use a require call to load it.

### As a dependency of a module[​](#as-a-dependency-of-a-module "Direct link to As a dependency of a module")

- ES6 Imports
- AMD Dependency
- AMD Requirement

mod/yourplugin/amd/src/yourwidget.js

```
importjQueryfrom'jquery';

jQuery('.example').hide();
```

## What about JQuery UI ?[​](#what-about-jquery-ui- "Direct link to What about JQuery UI ?")

JQuery UI is a separate project containing a library of reusable widgets that relies on JQuery. JQuery UI is available for plugins to use, but it **must not** be used in core code, and is *highly discouraged* in plugin usage.

The problems with JQuery UI include:

- It uses an entirely different theme system for CSS that does not work well with Moodle themes
- It introduces CSS conflicts with bootstrap
- The widgets have some accessibility features - but only if used in a very specific way which is not well documented

We **do not** recommend use of jQuery as it is highly likely to break Bootstrap.

If you *still* want to use JQuery UI in your plugin, you *must* include it via the page requirements using the `jquery_plugin()` function.

```
$PAGE->requires->jquery_plugin('ui');
```

Please note that this *must* be called before any content is output.

## See also[​](#see-also "Direct link to See also")

- [JavaScript Modules](https://moodledev.io/docs/4.4/guides/javascript/modules)
- [Useful core JavaScript modules](https://docs.moodle.org/dev/Useful_core_Javascript_modules)
- [jQuery in Moodle before Moodle 2.9](https://docs.moodle.org/dev/jQuery_pre2.9)
- [jQuery Documentation](http://jquery.com)
- [jQuery UI Documentation](http://jqueryui.com)