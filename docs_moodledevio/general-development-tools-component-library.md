---
title: Component Library | Moodle Developer Resources
url: https://moodledev.io/general/development/tools/component-library
source: sitemap
fetched_at: 2026-02-17T16:01:23.285366-03:00
rendered_js: false
word_count: 316
summary: This document introduces the Moodle Component Library, explaining how developers can access and build it to ensure UI consistency through reusable components. It provides step-by-step instructions for installation and outlines the requirements for documenting new interface elements.
tags:
    - moodle
    - ui-components
    - component-library
    - front-end-development
    - bootstrap
    - theme-development
category: guide
---

The Component Library is a tool designed for developers to identify frequently used user interface (UI) components and encourage their reuse within Moodle. It includes both components from `Twitter Bootstrap` and Moodle itself. The library provides an organized display of these components, showcasing them with your current Moodle theme.

This tool aims to assist developers working on Moodle themes, core features, and extensions by providing easy access to the UI components, which ultimately helps in creating more efficient and consistent user interfaces.

## Who should use the Component Library?[​](#who-should-use-the-component-library "Direct link to Who should use the Component Library?")

The Component Library is useful for:

- Visual designers
- Front-end developers
- UX developers
- Anyone working on core Moodle code or creating Moodle extensions.

## Getting started[​](#getting-started "Direct link to Getting started")

### Where is the Component Library?[​](#where-is-the-component-library "Direct link to Where is the Component Library?")

The library is built into Moodle but is only visible to developers. To access it, navigate to:

- **Site administration → Development → UI Component library**

If you can't see "**UI Component library**," you'll need to build it first (instructions below). You can also access the online version of the library at [Component Library online](http://componentlibrary.moodle.com/admin/tool/componentlibrary/docspage.php/library/getting-started/).

### Building the Component Library[​](#building-the-component-library "Direct link to Building the Component Library")

`Hugo` tooling is used to create the Component Library, as is the `Twitter Bootstrap` framework. It includes the necessary `Bootstrap` libraries that correspond to the version used by Moodle.

To build the Component Library, follow these steps:

1. **Install NodeJS dependencies** (refer to the [Grunt documentation](https://moodledev.io/general/development/tools/nodejs#grunt) for installation instructions).
2. Once the dependencies are installed, run the following command in your console:

This will build the Component Library.

## What should be documented?[​](#what-should-be-documented "Direct link to What should be documented?")

The main goal of the Component Library is to enhance UI consistency across Moodle. New UI components should be documented within the library whenever:

- A new Moodle feature is created or updated, especially when it involves UI elements.
- A UI component becomes available for reuse in a plugin that offers sub-plugins.
- Documentation for other UI features will also be welcomed, ensuring that the library grows and helps developers in their work.