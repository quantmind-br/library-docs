---
title: Clock | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/core/clock
source: sitemap
fetched_at: 2026-02-17T15:34:01.613805-03:00
rendered_js: false
word_count: 451
summary: This document explains how to use the PSR-20 compatible Clock interface in Moodle to manage time through dependency injection. It provides instructions for replacing standard time functions and mocking clock behavior to improve the reliability of unit tests.
tags:
    - moodle-development
    - psr-20
    - dependency-injection
    - unit-testing
    - clock-interface
    - mock-objects
    - php-development
category: guide
---

Moodle supports use of a [PSR-20](https://php-fig.org/psr/psr-20/) compatible Clock interface, which should be accessed using Dependency Injection.

This should be used instead of `time()` to fetch the current time. This allows unit tests to mock time and therefore to test a variety of cases such as events happening at the same time, or setting an explicit time.

Recommended usage

We recommend that the Clock Interface is used consistently in your code instead of using the standard `time()` method.

## Usage[​](#usage "Direct link to Usage")

The usage of the Clock extends the PSR-20 Clock Interface and adds a new convenience method, `\core\clock::time(): int`, to simplify replacement of the global `time()` method.

### Usage in standard classes[​](#usage-in-standard-classes "Direct link to Usage in standard classes")

Where the calling code is not instantiated via Dependency Injection itself, the simplest way to fetch the clock is using `\core\di::get(\core\clock::class)`, for example:

Usage in legacy code

```
$clock=\core\di::get(\core\clock::class);

// Fetch the current time as a \DateTimeImmutable.
$clock->now();

// Fetch the current time as a Unix Time Stamp.
$clock->time();
```

### Usage via Constructor Injection[​](#usage-via-constructor-injection "Direct link to Usage via Constructor Injection")

The recommended approach is to have the Dependency Injector inject into the constructor of a class.

Usage in injected classes

```
namespacemod_example;

classpost{
publicfunction__construct(
protectedreadonly\core\clock$clock,
protectedreadonly\moodle_database$db,
)

publicfunctioncreate_thing(\stdClass$data):\stdClass{
$data->timecreated=$this->clock->time();

$data->id=$this->db->insert_record('example_thing',$data);

return$data;
}
}
```

When using DI to fetch the class, the dependencies will automatically added to the constructor arguments:

Obtaining the injected class

```
$post=\core\di::get(post::class);
```

## Unit testing[​](#unit-testing "Direct link to Unit testing")

One of the most useful benefits to making consistent use of the Clock interface is to mock data within unit tests.

When testing code which makes use of the Clock interface, you can replace the standard system clock implementation with a testing clock which suits your needs.

Container Reset

The DI container is automatically reset at the end of every test, which ensures that your clock does not bleed into subsequent tests.

Moodle provides two standard test clocks, but you are welcome to create any other, as long as it implements the `\core\clock` interface.

warning

When mocking the clock, you *must* do so *before* fetching your service.

Any injected value within your service will persist for the lifetime of that service.

Replacing the clock after fetching your service will have *no* effect.

### Incrementing clock[​](#incrementing-clock "Direct link to Incrementing clock")

The incrementing clock increases the time by one second every time it is called. It can also be instantiated with a specific start time if preferred.

A helper method, `mock_clock_with_incrementing(?int $starttime = null): \core\clock`, is provided within the standard testcase:

Obtaining the incrementing clock

```
classmy_testextends\advanced_testcase{
publicfunctiontest_create_thing():void{
// This class inserts data into the database.
$this->resetAfterTest(true);

$clock=$this->mock_clock_with_incrementing();

$post=\core\di::get(post::class);
$posta=$post->create_thing((object)[
'name'=>'a',
]);
$postb=$post->create_thing((object)[
'name'=>'a',
]);

// The incrementing clock automatically advanced by one second each time it is called.
$this->assertGreaterThan($postb->timecreated,$posta->timecreated);
$this->assertLessThan($clock->time(),$postb->timecreated);
}
}
```

It is also possible to specify a start time for the clock;

Setting the start time

```
$clock=$this->mock_clock_with_incrementing(12345678);
```

### Frozen clock[​](#frozen-clock "Direct link to Frozen clock")

The frozen clock uses a time which does not change, unless manually set. This can be useful when testing code which must handle time-based resolutions.

A helper method, `mock_clock_with_frozen(?int $time = null): \core\clock`, is provided within the standard testcase:

Obtaining and using the frozen clock

```
classmy_testextends\advanced_testcase{
publicfunctiontest_create_thing():void{
// This class inserts data into the database.
$this->resetAfterTest(true);

$clock=$this->mock_clock_with_frozen();

$post=\core\di::get(post::class);
$posta=$post->create_thing((object)[
'name'=>'a',
]);
$postb=$post->create_thing((object)[
'name'=>'a',
]);

// The frozen clock keeps the same time.
$this->assertEquals($postb->timecreated,$posta->timecreated);
$this->assertEquals($clock->time(),$postb->timecreated);

// The time can be manually set.
$clock->set_to(12345678);
$postc=$post->create_thing((object)[
'name'=>'a',
]);

// The frozen clock keeps the same time.
$this->assertEquals(12345678,$postc->timecreated);

// And can also be bumped.
$clock->set_to(0);
$this->assertEquals(0,$clock->time());

// Bump the current time by 1 second.
$clock->bump();
$this->assertEquals(1,$clock->time());

// Bump by 4 seconds.
$clock->bump(4);
$this->assertEquals(5,$clock->time());
}
}
```

### Custom clock[​](#custom-clock "Direct link to Custom clock")

If the standard cases are not suitable for you, then you can create a custom clock and inject it into the DI container.

Creating a custom clock

```
classmy_clockimplements\core\clock{
publicint$time;

publicfunction__construct(){
$this->time=time();
}

publicfunctionnow():\DateTimeImmutable{
$time=new\DateTimeImmutable('@'.$this->time);
$this->time=$this->time+=5;

return$time;
}

publicfunctiontime():int{
return$this->now()->getTimestamp();
}
}

classmy_testextends\advanced_testcase{
publicfunctiontest_my_thing():void{
$clock=newmy_clock();
        \core\di:set(\core\clock::class,$clock);

$post=\core\di::get(post::class);
$posta=$post->create_thing((object)[
'name'=>'a',
]);
}
}
```