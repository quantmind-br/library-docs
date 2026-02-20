---
title: Unit Testing | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/subsystems/external/testing
source: sitemap
fetched_at: 2026-02-17T15:36:26.484856-03:00
rendered_js: false
word_count: 0
summary: This document provides unit test implementations for Moodle external functions, demonstrating how to verify user capabilities and process web service return values.
tags:
    - moodle
    - php-unit
    - external-functions
    - unit-testing
    - web-services
    - capability-check
category: tutorial
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
 * Unit tests for the get_fruit function of the kitchen.
 *
 * @package    mod_kitchen
 * @category   external
 * @copyright  20XX Your Name
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

namespacemod_kitchen\external;

defined('MOODLE_INTERNAL')||die();

global$CFG;
require_once($CFG->dirroot.'/webservice/tests/helpers.php');

classget_fruit_testextendsexternallib_advanced_testcase{

/**
     * Test the execute function when capabilities are present.
     *
     * @covers \mod_fruit\external\get_fruit::execute
     */
publicfunctiontest_capabilities():void{
$this->resetAfterTest(true);

$course=$this->getDataGenerator()->create_course();
$cm=$this->getDataGenerator()->create_module('mod_kitchen',[
'course'=>$course->id,
]);

// Set the required capabilities by the external function
$contextid=context_module::instance($cm->cmid)->id;
$roleid=$this->assignUserCapability('moodle/CAPABILITYNAME',$contextid);

// Call the external service function.
$returnvalue=get_fruit::execute([
'course'=>$course->id,
'cmid'=>$cm->id,
]);

// We need to execute the return values cleaning process to simulate
// the web service server.
$returnvalue=\core_external\external_api::clean_returnvalue(
get_fruit::execute_returns(),
$returnvalue
);

// Assert that there was a response.
// The actual response is tested in other tests.
$this->assertNotNull($returnvalue);
}

/**
     * Test the execute function when capabilities are missing.
     *
     * @covers \mod_fruit\external\get_fruit::execute
     */
publicfunctiontest_capabilities_missing():void{
global$USER;

$this->resetAfterTest(true);

$course=$this->getDataGenerator()->create_course();
$cm=$this->getDataGenerator()->create_module('mod_kitchen',[
'course'=>$course->id,
]);

// Set the required capabilities by the external function
$contextid=context_module::instance($cm->cmid)->id;
$this->unassignUserCapability('moodle/CAPABILITYNAME',$contextid,$roleid);

$params=[PARAM1,PARAM2,...];

// Call without required capability
$this->expectException(required_capability_exception::class);
get_fruit::execute([
'course'=>$course->id,
'cmid'=>$cm->id,
]);
}
}
```