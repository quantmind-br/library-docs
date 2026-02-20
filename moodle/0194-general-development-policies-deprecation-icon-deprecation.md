---
title: Icon deprecation | Moodle Developer Resources
url: https://moodledev.io/general/development/policies/deprecation/icon-deprecation
source: sitemap
fetched_at: 2026-02-17T15:59:10.806285-03:00
rendered_js: false
word_count: 337
summary: This document explains the procedures for deprecating and removing icons in Moodle 4.5 and later, covering registration methods for core and plugins as well as testing for deprecated icons using Behat.
tags:
    - moodle
    - icon-deprecation
    - plugin-development
    - behat-testing
    - core-development
category: guide
---

Since Moodle 4.5, it's possible to safely deprecate and remove icons.

When should icons be removed?

There are situations where deprecation does not make sense. For example when a whole functionality is being removed, or a very specific icon is no longer used by the code. If it is very unlikely that the icon is used by any other code, it can simply be removed without the full deprecation process.

## How it works[​](#how-it-works "Direct link to How it works")

A new method, `get_deprecated_icons()`, has been added to the `icon_system` class. All deprecated icons should be registered through this method. Plugins can implement a callback to `pluginname_get_deprecated_icons()` to register their deprecated icons too.

## How to deprecate an icon[​](#how-to-deprecate-an-icon "Direct link to How to deprecate an icon")

To deprecate an icon, follow these steps:

1. Add the deprecated icon to the proper `get_deprecated_icons()` method (`lib/classes/output/icon_system_fontawesome.php` for core icons and `pluginname_get_deprecated_icons()` for plugins), under the comment for the current version `// Deprecated since Moodle X.Y.`
2. Add a comment to the removed icon explaining why it has been deprecated.

note

If there is no section for the current version in the `get_deprecated_icons()` method, it should be added. See [Final deprecation](#final-deprecation).

**Example 1: Deprecate core icon**

lib/classes/output/icon\_system\_fontawesome.php

```
#[\Override]
publicfunctionget_deprecated_icons():array{
// Add deprecated core icons to parent deprecated icons.
returnarray_merge(
parent::get_deprecated_icons(),
[
//
// Deprecated since Moodle 4.5.
//
'core:a/em1_bwgreater',
],
);
}
```

**Example 2: Deprecate plugin icon**

pluginname\_get\_deprecated\_icons() callback

```
/**
     * Get the list of deprecated icons.
     *
     * @return array with the deprecated key icons.
     */
functionmod_forum_get_deprecated_icons():array{
return[
//
// Deprecated since Moodle 4.5.
//
'mod_forum:t/unsubscribed',
];
}
```

## Final deprecation[​](#final-deprecation "Direct link to Final deprecation")

When adding icons to the `get_deprecated_icons()` method, it is important to add it under the comment with the version when the code was deprecated. If that comment still doesn't exist, it should be added:

Add a comment in the get\_deprecated\_icons() method

```
[
//
// Deprecated since Moodle 4.5.
//
];
```

And alongside with that, a new issue should be created in the tracker to remove the deprecated SCSS code with the title `Remove icons deprecated in X.Y` and in the epic `X.[Y+4]` deprecations.

After 4 major versions, the deprecated icons will be removed from the `get_deprecated_icons()` methods.

## Check deprecated icons in Behat tests[​](#check-deprecated-icons-in-behat-tests "Direct link to Check deprecated icons in Behat tests")

Behat tests are now checking for deprecated icons. When running Behat tests, the following message will be displayed:

```
Run optional tests:
[...]
- Icon deprecations: Yes
```

If deprecated icons are being used, the test will fail with the following message:

```
Deprecated icon in use. Enable $CFG->debugdisplay for detailed debugging information in the console (Exception)
```

This check can be disabled by using the `--no-icon-deprecations option` flag in the behat CLI.

```
php admin/tool/behat/cli/init.php --no-icon-deprecations
```