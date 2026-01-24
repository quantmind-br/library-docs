---
title: UI elements in content
url: https://docs.docker.com/contribute/ui/
source: llms
fetched_at: 2026-01-24T14:07:04.925589794-03:00
rendered_js: false
word_count: 315
summary: This guide provides standards for writing about user interface elements, including formatting rules, consistent terminology, and instructional best practices.
tags:
    - technical-writing
    - style-guide
    - ui-elements
    - documentation-standards
    - formatting-guidelines
category: guide
---

Table of contents

* * *

Use this guide when writing documentation that refers to buttons, fields, menus, dialogs, or other user interface (UI) elements. It explains how to format UI terms, write task-focused instructions, and refer to common UI patterns consistently and clearly.

## [Format UI element names](#format-ui-element-names)

Use bold formatting for the visible names of UI elements:

- Buttons
- Dialogs
- Windows
- Tabs
- Menu items
- List items
- Form labels
- Section headings

For example:

*Select **Create**, then fill out the **Name** field.*

Do not bold product names or features unless they appear exactly as a label in the UI.

### [Capitalization](#capitalization)

- Follow the capitalization as it appears in the UI.
- If UI labels are all uppercase or inconsistent, use sentence case in your docs for readability.

## [Write task-focused instructions](#write-task-focused-instructions)

When possible, guide users based on what they’re trying to do, not just what they should select. This makes docs more goal-oriented and adaptable to UI changes.

Do thisAvoid thisExpand the **Advanced options** section.Select the zippy to expand the **Advanced options** section.Choose a base image for your container.Select a dropdown and pick something.

## [Use correct prepositions with UI elements](#use-correct-prepositions-with-ui-elements)

Choose the right preposition based on the type of UI element you're referencing.

PrepositionUse with...Example**in**dialogs, fields, lists, menus, panes, windowsIn the **Name** field, enter your project name.**on**pages, tabs, toolbarsOn the **Settings** tab, select **General**.

## [Use consistent UI element terms](#use-consistent-ui-element-terms)

Use these standard terms when referring to elements in Docker products:

Preferred TermUse When Referring To...**button**A clickable action element (e.g., **Start**)**field**A place to enter text or select a value**menu** / **menu item**A drop-down or navigation option**drop-down**A drop-down menu item**context switcher**Specific to toggling on cloud mode**tab**A selectable view within a window or page**dialog**A popup window for confirmations or options**section**A logical grouping of content on a page**list** / **list item**A scrollable list of selectable entries**toggle**A binary control (on/off)**checkbox**A multi-select control**tooltip**Text that appears on hover

Finally, instead of saying “click the control,” say “select the **Create** button.”