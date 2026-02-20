---
title: 7 docs tagged with "core_form" | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/tags/core-form
source: sitemap
fetched_at: 2026-02-17T15:29:59.473419-03:00
rendered_js: false
word_count: 321
summary: This document provides a technical overview of the Moodle Form API, covering advanced UI elements, specialized input controllers, and techniques for managing dynamic form data.
tags:
    - moodle-api
    - form-management
    - ui-elements
    - web-forms
    - moodle-development
category: api
---

## [Advanced elements](https://moodledev.io/docs/5.1/apis/subsystems/form/advanced/advanced-elements)

Form elements can be marked as 'advanced'. This has the effect that they are hidden initially.

## [Checkbox controller](https://moodledev.io/docs/5.1/apis/subsystems/form/advanced/checkbox-controller)

The checkbox controller allows developers to group checkboxes together and add a link or button to check, or uncheck, all of the checkboxes at once.

## [Choice Dropdown](https://moodledev.io/docs/5.1/apis/subsystems/form/fields/choicedropdown)

The choicedropdown form field creates a dropdown list with multiple options. It is different from a standard select dropdown in that each option can have extra icons and descriptions. This field is often used in forms to facilitate the selection of a non-trivial option that demands additional information.

## [Form Usage](https://moodledev.io/docs/5.1/apis/subsystems/form/usage)

Moodle's Form API is an extension of the Pear HTMLQuickForm API, which is no longer supported. Some documentation for the upstream library is available in the PEAR package page, including a short tutorial. A longer tutorial is also available, courtesy of the Internet Archive.

## [Forms API](https://moodledev.io/docs/5.1/apis/subsystems/form)

Form are created using the Form API. The Form API supports most standard HTML elements, including checkboxes, radio buttons, text boxes, and so on, adding additional accessibility and security features to them.

## [No submit button](https://moodledev.io/docs/5.1/apis/subsystems/form/advanced/no-submit-button)

The moodleform 'nosubmitbutton\_pressed()' method allows you to detect if a button on your form has been pressed that is a submit button but that has been defined as a button that doesn't result in a processing of all the form data but will result in some form 'sub action' and then having the form redisplayed. This is useful for example to have an 'Add' button to add some option to a select box in the form etc. You define a button as a no submit button as in the example below (in definition()). This example adds a text box and a submit button in a group.

## [Repeat elements](https://moodledev.io/docs/5.1/apis/subsystems/form/advanced/repeat-elements)

The Form API includes the ability to repeat a group of form elements. This is useful where you need to have an unknown quantity of item data, for example possible answers in a quiz question.