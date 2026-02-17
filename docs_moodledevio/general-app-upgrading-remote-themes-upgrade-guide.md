---
title: Moodle App Remote Themes Upgrade Guide | Moodle Developer Resources
url: https://moodledev.io/general/app/upgrading/remote-themes-upgrade-guide
source: sitemap
fetched_at: 2026-02-17T15:55:25.717146-03:00
rendered_js: false
word_count: 1029
summary: This document provides instructions for migrating custom CSS styles and remote themes between different versions of the Moodle App, covering breaking changes and framework upgrades.
tags:
    - moodle-app
    - css-migration
    - remote-themes
    - ionic-framework
    - theme-customization
    - version-upgrade
category: guide
---

In the following guide, you will learn how to migrate your styles from an older version of the app.

However, keep in mind that not all your users will be using the latest version. We recommend that you keep your old CSS rules for older versions as indicated in the [Before starting the migration](#before-starting-the-migration) section. By doing so, users who haven't updated the app will continue seeing the same styles they had until now.

Depending on which version of the app you're upgrading from, you'll need to go through multiple version upgrades. This guide is divided by version ranges, so you should be able to start with your current version and build up from there.

### Before starting the migration[​](#before-starting-the-migration "Direct link to Before starting the migration")

We recommend prepending all conflicting CSS rules with the specific version they are targeting.

For example, for a CSS stylesheet that targets both 4.0 and 4.1 versions, you should do the following:

```
html.moodleapp-4-1{
--ion-color-primary:red;
}

body.moodle-app-4-0{
--ion-color-primary:green;
}
```

You can use these classes to target specific major and patch versions as well, so for example version 4.1.0 ships with `moodleapp-4`, `moodleapp-4-1`, and `moodleapp-4-1-0` classes. You can also use ionic versions to filter styles, such as `ionic5` or `ionic8`.

caution

Notice that mode and version classes moved from the `body` tag to the `html` tag in version 4.1. Learn more about this when [upgrading from 4.0 to 4.1](#40-to-41).

### How to upgrade my theme[​](#how-to-upgrade-my-theme "Direct link to How to upgrade my theme")

You can follow the same process that is documented in the [Moodle App Remote Themes](https://moodledev.io/general/app/customisation/remote-themes#how-can-you-create-your-own-theme) page.

Make sure to read it in order to understand how to style your application for newer versions of the app. If you're upgrading your styles, it is likely that the documentation has been updated since you read it. So we recommend taking a look even if you're already familiar with Remote Themes.

## 4.4 to 4.5[​](#44-to-45 "Direct link to 4.4 to 4.5")

Ionic version has been upgraded to v8 (from v7). This shouldn't have any direct impact on remote themes, but please verify that they continue to function correctly.

## 4.3 to 4.4[​](#43-to-44 "Direct link to 4.3 to 4.4")

Ionic version has been upgraded to v7 (from v5). This shouldn't have any direct impact in remote themes; but make sure that they are still working properly.

## 4.2 to 4.3[​](#42-to-43 "Direct link to 4.2 to 4.3")

The only change to keep in mind for this release is that Font Awesome icons were upgraded to version 6.4.0. This shouldn't affect Remote Themes directly, but given that it affects the visuals aspects of the app, it could potentially be relevant.

## 4.1 to 4.2[​](#41-to-42 "Direct link to 4.1 to 4.2")

The only change to keep in mind for this release is that Font Awesome icons were upgraded to version 6.3.0. This shouldn't affect Remote Themes directly, but given that it affects the visuals aspects of the app, it could potentially be relevant.

## 4.0 to 4.1[​](#40-to-41 "Direct link to 4.0 to 4.1")

There is only one thing to look after when upgrading to 4.1, so it should be a relatively quick process.

### Mode classes[​](#mode-classes "Direct link to Mode classes")

Starting in 4.1, mode and version classes have been moved from the `body` tag to the `html` tag. This change arose from [a bug on derived CSS variables](https://moodle.atlassian.net/browse/MOBILE-4127), and it should be fairly straightforward to make.

4.0

```
body{
--core-header-toolbar-background:red;
}

body.dark{
--core-header-toolbar-background:green;
}
```

4.1

```
html{
--core-header-toolbar-background:red;
}

html.dark{
--core-header-toolbar-background:green;
}
```

info

In order to avoid breaking existing styles, version 4.1 will continue adding version classes both to `body` and `html` tags. But using the classes from the `body` tag is considered a deprecated approach, and won't be supported in future versions. So we recommend that you update your Remote Themes now.

## 3.9.5 to 4.0[​](#395-to-40 "Direct link to 3.9.5 to 4.0")

There haven't been any breaking changes from 3.9.5 to 4.0 in terms of theming functionality, but the UI of the application has changed drastically so we recommend going over all the customisations to see that they are still relevant in the new version.

## 3.9.4 to 3.9.5[​](#394-to-395 "Direct link to 3.9.4 to 3.9.5")

This upgrade requires more changes than usual because the Moodle App was upgraded the underlying Ionic framework from version 3 to version 5, which introduced many breaking changes.

### Windows Phone[​](#windows-phone "Direct link to Windows Phone")

Starting with this version, Windows Phone is no longer supported so you should remove all styles using Ionic classes ending with `-wp` since they are no longer necessary.

### CSS variables[​](#css-variables "Direct link to CSS variables")

Starting with this version, it is possible to use [CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) to make easier customisations, so it's likely that you won't need to override as many styles as before.

You can see some examples in the sections below, and you can also look at [the theme file](https://github.com/moodlehq/moodleapp/blob/latest/src/theme/theme.light.scss) to find some of the main variables of the app.

### Colors[​](#colors "Direct link to Colors")

The main color in the app is Moodle Orange, but you can now change it by using the `--primary` variable. This will probably reduce the CSS you are applying right now, but this only covers the main color.

For other colors, check out [the colors section in the main documentation](https://moodledev.io/general/app/customisation/remote-themes#working-with-colors).

#### Border width and color (new)[​](#border-width-and-color-new "Direct link to Border width and color (new)")

On the header toolbar, we've added a bottom border that you can disable.

3.9.5

```
ion-header ion-toolbar{
--core-header-toolbar-border-width:2px;/* Use 0 to disable it */
--core-header-toolbar-border-color:yellow;
}
```

#### Background[​](#background "Direct link to Background")

3.9.4

```
.toolbar-background-md,.toolbar-background-ios{
background:red;
}
```

3.9.5

```
ion-header ion-toolbar{
--core-header-toolbar-background:red;
}
```

#### Text and buttons[​](#text-and-buttons "Direct link to Text and buttons")

3.9.4

```
.toolbar-title-md,
.toolbar-title-ios{
color:red;
font-weight: normal;
}
```

3.9.5

```
ion-header ion-toolbar{
--core-header-toolbar-color:red;
}

ion-header ion-toolbar.in-toolbar h1,
ion-header ion-toolbar.in-toolbar h2{
font-weight: normal;
}
```

### Bottom tab bar (main menu)[​](#bottom-tab-bar-main-menu "Direct link to Bottom tab bar (main menu)")

#### Background[​](#background-1 "Direct link to Background")

3.9.4

```
.tabs-md.tabbar,
.tabs-ios.tabbar{
background:red;
}
```

3.9.5

```
ion-tab-bar.mainmenu-tabs{
--core-bottom-tabs-background:red;
--core-bottom-tabs-background-selected:transparent;
}
```

#### Tab icon color[​](#tab-icon-color "Direct link to Tab icon color")

3.9.4

```
.tabs-md.tab-button-icon,
.tabs-ios.tab-button-icon{
color:blue;
}
```

3.9.5

```
ion-tab-bar.mainmenu-tabs{
--core-bottom-tabs-color:blue;
}
```

#### Selected tab icon color[​](#selected-tab-icon-color "Direct link to Selected tab icon color")

3.9.4

```
tabs-md .tab-button[.tab-button-icon,
.tabs-ios.tab-button[aria-selected=true](aria-selected=true]).tab-button-icon{
color:red;
}
```

3.9.5

```
ion-tab-bar.mainmenu-tabs{
--core-bottom-tabs-color-selected:red;
}
```

#### Badge color and text[​](#badge-color-and-text "Direct link to Badge color and text")

3.9.4

```
core-ion-tabs .tab-badge.badge{
color:white;
background:red;
}
```

3.9.5

```
ion-tab-bar.mainmenu-tabs{
--core-bottom-tabs-badge-text-color:white;
--core-bottom-tabs-badge-color:red;
}
```

### Top tabs[​](#top-tabs "Direct link to Top tabs")

#### Tabs background[​](#tabs-background "Direct link to Tabs background")

3.9.4

```
.core-tabs-bar{
background-color:red;
}
```

3.9.5

```
core-tabs, core-tabs-outlet{
--core-tabs-background:red;
}
```

#### Individual tab background[​](#individual-tab-background "Direct link to Individual tab background")

3.9.4

```
.core-tabs-bar.tab-slide{
background-color:red;
}
```

3.9.5

```
core-tabs, core-tabs-outlet{
--core-tab-background:red;
}
```

#### Unselected tab styles[​](#unselected-tab-styles "Direct link to Unselected tab styles")

3.9.4

```
.core-tabs-bar.tab-slide{
color:red;
border-bottom-color:red;
}
```

3.9.5

```
core-tabs, core-tabs-outlet{
--core-tab-color:red;
}
```

#### Selected tab styles[​](#selected-tab-styles "Direct link to Selected tab styles")

3.9.4

```
.core-tabs-bar.tab-slide[aria-selected=true]{
color:red;
border-bottom-color:red;
font-weigth: normal;
}
```

3.9.5

```
core-tabs, core-tabs-outlet{
--core-tab-color-active:red;
--core-tab-border-color-active:red;
--core-tab-font-weight-active: bold;
}
```

### Items[​](#items "Direct link to Items")

#### Items background color[​](#items-background-color "Direct link to Items background color")

3.9.4

```
ion-item{
background:red;
}
```

3.9.5

```
body{
--ion-item-background:red;
}
```

#### Item divider background color[​](#item-divider-background-color "Direct link to Item divider background color")

3.9.4

```
.item-divider-md,
.item-divider-ios{
background:red;
color:yellow;
}
```

3.9.5

```
body{
--item-divider-background:red;
--item-divider-color:yellow;
}
```

#### Empty divider background[​](#empty-divider-background "Direct link to Empty divider background")

3.9.5

```
body{
--spacer-background:red;
}
```

### Progress bar[​](#progress-bar "Direct link to Progress bar")

3.9.5

```
core-progress-bar{
--core-progressbar-height:8px;
--core-progressbar-color:red;
--core-progressbar-text-color:black;
--core-progressbar-background:white;
}
```

### More page[​](#more-page "Direct link to More page")

#### Icons[​](#icons "Direct link to Icons")

The icons in the More page can now easily change their color:

3.9.4

```
page-core-mainmenu-more ion-icon{
color:red;
}
```

3.9.5

```
page-core-mainmenu-more{
--core-more-icon:red;
}
```

To change a color on a particular icon, you'll have to use the class of each handler. For example, to change the color of the folder icon on the menu item named Files:

3.9.4

```
page-core-mainmenu-more .ion-md-folder,
page-core-mainmenu-more .ion-ios-folder{
color:red;
}
```

3.9.5

```
page-core-mainmenu-more .addon-privatefiles-handler ion-icon{\
color:red!important;
}
```

#### Item border color[​](#item-border-color "Direct link to Item border color")

3.9.4

```
page-core-mainmenu-more .item-block.item-ios.item-inner,
page-core-mainmenu-more .item-block.item-md.item-inner{
border-bottom-color:red;
}
```

3.9.5

```
page-core-mainmenu-more{
--core-more-item-border:red;
}
```

The dividers background color can now be overridden using `--spacer-background`:

3.9.5

```
page-core-mainmenu-more{
--spacer-background:blue;
}
```

### Login page[​](#login-page "Direct link to Login page")

You can now personalise some colors in the Login page, but keep in mind that this only includes the credentials page (the one after you select the site).

3.9.5

```
body{
--core-login-background:red;
--core-login-text-color:blue;
--core-login-input-background:green;
--core-login-input-color:yellow;
}
```

### Messages page[​](#messages-page "Direct link to Messages page")

Message discussion page, including chat activity and comments:

3.9.5

```
body{
--addon-messages-message-bg:white;
--addon-messages-message-activated-bg: gray-light;
--addon-messages-message-note-text: gray-dark;
--addon-messages-message-mine-bg: gray-light;
--addon-messages-message-mine-activated-bg:gray;
--addon-messages-discussion-badge:orange;
--addon-messages-discussion-badge-text:white;
}
```

You can also make some modifications on the input field:

3.9.5

```
body{
--core-send-message-input-background: gray-light;
--core-send-message-input-color:black;
}
```

### Full example[​](#full-example "Direct link to Full example")

This is a full example showcasing how to handle multiple versions:

3.9.4 and 3.9.5

```
/* ----- Ionic 5 styles ----- */

body.ionic5{
--core-header-toolbar-background:red;
}

/* Dark mode */
body.ionic5.dark{
--core-header-toolbar-background:blue;
}

/* iOS only */
html.ios body.ionic5{
--core-link-color:green;
}

/* Android only */
html.md body.ionic5{
--core-link-color:yellow;
}


/* ----- Ionic 3 styles (legacy) ----- */

body:not(.ionic5).toolbar-background{
border-color:#004C9C;
background:#004C9C;
}
```

As you can see we recommend to always add `body.ionic*` to start the CSS selectors, you can also use `:root body.ionic5` or even `html` before `body`.