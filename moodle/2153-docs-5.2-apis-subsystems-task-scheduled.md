---
title: Scheduled tasks | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/task/scheduled
source: sitemap
fetched_at: 2026-02-17T15:46:36.45397-03:00
rendered_js: false
word_count: 0
summary: This document defines the configuration structure for scheduling background tasks within a Moodle plugin, including execution timing and task class associations.
tags:
    - moodle
    - scheduled-tasks
    - plugin-development
    - php
    - task-configuration
    - backend
category: configuration
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
 * Task schedule configuration for the plugintype_pluginname plugin.
 *
 * @package   plugintype_pluginname
 * @copyright Year, You Name <your@email.address>
 * @license   http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

$tasks=[
[
'classname'=>'mod_example\task\do_something',
'blocking'=>0,
'minute'=>'30',
'hour'=>'17',
'day'=>'*',
'month'=>'1,7',
'dayofweek'=>'0',
],
];
```