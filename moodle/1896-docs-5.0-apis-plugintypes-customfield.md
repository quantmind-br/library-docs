---
title: Custom fields | Moodle Developer Resources
url: https://moodledev.io/docs/5.0/apis/plugintypes/customfield
source: sitemap
fetched_at: 2026-02-17T15:25:29.882668-03:00
rendered_js: false
word_count: 0
summary: This document defines the field controller class for a Moodle custom field plugin, specifying how to configure the field's settings via a form definition.
tags:
    - moodle-development
    - custom-fields
    - php-class
    - plugin-configuration
    - moodle-api
    - form-elements
category: reference
---

```
<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Field configuration for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

namespacecustomfield_myfield;

classfield_controllerextends\core_customfield\field_controller{

/** @var string Plugin type */
constTYPE='radio';

/**
     * Add fields for editing a checkbox field.
     *
     * @param \MoodleQuickForm $mform
     */
publicfunctionconfig_form_definition(\MoodleQuickForm$mform){
$mform->addElement(
'header',
'header_specificsettings',
get_string('specificsettings','customfield_checkbox')
);
$mform->setExpanded('header_specificsettings',true);

$mform->addElement(
'selectyesno',
'configdata[checkbydefault]',
get_string('checkedbydefault','customfield_checkbox')
);
$mform->setType('configdata[checkbydefault]',PARAM_BOOL);
}
}
```