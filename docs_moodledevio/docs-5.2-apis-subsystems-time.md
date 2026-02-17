---
title: Time API | Moodle Developer Resources
url: https://moodledev.io/docs/5.2/apis/subsystems/time
source: sitemap
fetched_at: 2026-02-17T15:46:37.950727-03:00
rendered_js: false
word_count: 829
summary: This document explains how Moodle manages and displays time using its internal APIs, detailing the distinction between system and user time and the use of the clock interface for time manipulation.
tags:
    - moodle-api
    - time-management
    - php
    - unix-timestamp
    - timezone-handling
    - dependency-injection
    - psr-20
category: api
---

Internally Moodle always stores all times in unixtime format, which is a format independent of timezones.

The Time API is then used to display the correct date and time depending on user and site timezones.

tip

The Unix Time format is defined as the number of seconds since the Unix epoch, which began on January 1 1970 at 00:00:00 UTC.

## Classifications of Time[​](#classifications-of-time "Direct link to Classifications of Time")

In Moodle there are 2 cases to consider when working with time:

### System Time[​](#system-time "Direct link to System Time")

In Moodle, the term 'System Time' is used to describe dates on the server, for example times when executing scheduled tasks, performing background tasks, and so on. That is, anything which does not depend on the timezone of any specific user.

### User Time[​](#user-time "Direct link to User Time")

The term 'User Time' is used for times which are user-specific. That is that they are in the user's time zone.

You will see these when displaying dates and times to the user in their current timezone (which may be different for each user).

## The Time APIs[​](#the-time-apis "Direct link to The Time APIs")

The main APIs for time in Moodle are the `\core\clock` class, which allows you to fetch and manipulate the current time; and the `core_date` class, which handles PHP `DateTimeZone` objects for either user time or server time as needed. You can then use the PHP `DateTime` classes to manipulate the time. You can also fetch a timestamp with `DateTime::getTimestamp()`.

### Fetching and manipulating the current time[​](#fetching-and-manipulating-the-current-time "Direct link to Fetching and manipulating the current time")

The `\core\clock` Interface was added in Moodle 4.4 and is available via [Dependency Injection](https://moodledev.io/docs/5.2/apis/core/di). It provides a [clock implementation](https://moodledev.io/docs/5.2/apis/core/clock) which is consistent with the [PSR-20: Clock](https://www.php-fig.org/psr/psr-20/) interfaces.

This is the recommended approach for fetching the current time and should be used instead of native implementations such as `time()`, and `new \DateTime();`.

Fetching the clock

```
$clock=\core\di::get(\core\clock::class);
```

Why use the Clock?

By using the clock interface fetched via Dependency Injection, it becomes easier to test different conditions within your code. For example you can inject a custom implementation of the clock which simulates a 5 minute gap between creation of different records, and allows you to test features such as sorting.

You can read more on [Unit testing](https://moodledev.io/docs/5.2/apis/core/clock#unit-testing) with the Clock API.

The clock interface's `now()` method returns a `\DateTimeImmutable` object representing the current time:

Fetching the current DateTime

```
$now=\core\di::get(\core\clock::class)->now();
```

This can be further modified using the [`add`](https://www.php.net/manual/en/datetimeimmutable.add.php), [`sub`](https://www.php.net/manual/en/datetimeimmutable.sub.php), and [`modify`](https://www.php.net/manual/en/datetimeimmutable.modify.php) methods, for example:

Fetch the DateTime for 24 hours time

```
$tomorrow=\core\di::get(\core\clock::class)
->now()
->modify('+1 day');
```

The Unix Timestamp can be fetched for the DateTime Object using the `getTimestamp()` method:

Fetching the timestamp

```
$tomorrow=\core\di::get(\core\clock::class)
->now()
->modify('+1 day')
->getTimestamp();
```

Modifying the DateTime object

The object returned from the `\core\clock::now()` method is an instance of `\DateTimeImmutable`.

Calling any of the modifier methods (`add()`, `sub()`, or `modify()`) will not modify the object, but will return a new object with the updated time.

```
$today=\core\di::get(\core\clock::class)
->now();

$tomorrow=$today->modify('+1 day');

$today!==$tomorrow;
```

The `\core\time` interface also provides a helper to fetch the current Unix Timestamp in a single operation:

Fetching the current Unix Timestamp

```
$now=\core\di::get(\core\clock::class)->time();
```

### Displaying time[​](#displaying-time "Direct link to Displaying time")

Moodle provides a range of methods to display a Unix Timestamp in the relevant Language and Timezone.

1. Time API's for current user
   
   - `userdate` - Given a Unix Timestamp, return a formatted string that represents a date in the user's time.
     
     note
     
     The format required by this function is the [`strftime()`](https://www.php.net/manual/en/function.strftime.php) format, not the more common format used by `date()`.
   - `usergetmidnight` - Given a Unix Timestamp, return the Unix Timestamp of the most recent midnight for the current user.
   - `usertimezone` - Return the current user's timezone
   - `make_timestamp` - Given date-time, it produces a Unix Timestamp for current user.
2. System Time API
   
   - `format_time` - Format a date or time period in seconds as weeks, days, hours, and so on, as needed
   - `dst_offset_on` - Calculates the Daylight Saving Offset for a given Unix Timestamp
   - `find_day_in_month` - Calculates when the day appears in specific month
   - `days_in_month` - Calculate number of days in a given month
   - `dayofweek` - Calculate the position in the week of a specific calendar day
3. Older legacy date/time functions. Do not use in new code.
   
   - `usergetdate` - Given a Unix Timestamp, returns an array that represents the date-time in user time
   - `usertime` - Appends the users timezone offset to an integer timestamp

## Glossary[​](#glossary "Direct link to Glossary")

### Timezone[​](#timezone "Direct link to Timezone")

Moodle supports the following timezone formats:

1. UTC (specifically UTC−11 to UTC+11)
2. Time offsets from UTC (int +-(0-13) or float +-(0.5-12.5))
3. World timezones (Australia/Perth)

### Location[​](#location "Direct link to Location")

Timezone depends on [Location](https://docs.moodle.org/en/Location) of the user and can be forced upon by administrator.

### DST[​](#dst "Direct link to DST")

DST is abbreviation of **Daylight Saving Time** (also known as "Day light saving" and "Summer Time"). Many countries, and sometimes just certain regions of countries, adopt daylight saving time during part of the year. Moodle automatically calculates DST for current user, depending on user location.

## Examples[​](#examples "Direct link to Examples")

### Create DateTime with date/time from a Unix Timestamp[​](#create-datetime-with-datetime-from-a-unix-timestamp "Direct link to Create DateTime with date/time from a Unix Timestamp")

```
$date=newDateTime();
$date->setTimestamp(intval($unixtime);
echouserdate($date->getTimestamp());
```

### Time API's for current user[​](#time-apis-for-current-user "Direct link to Time API's for current user")

Prints the current date and time in the user's timezone:

```
$now=\core\di::get(\core\clock::class)->time();
echouserdate($now);
```

To manually specify the display format, use one of the formatting strings defined in the `core_langconfig` component of the user's language. For example, to display just the date without the time, use:

```
echouserdate(
\core\di::get(\core\clock::class)->time(),
get_string('strftimedaydate','core_langconfig'),
);
```

You can also use the `DateTime` class to obtain the timestamp:

```
$date=\core\di::get(\core\clock::class)
->now()
->modify('+1 day')
->setTime(0,0,0);

echouserdate(
$date->getTimestamp(),
get_string('strftimedatefullshort','core_langconfig'),
);
```

### System Time API[​](#system-time-api "Direct link to System Time API")

Find the day of the week for the first day in this month.

```
$now=\core\di::get(\core\clock::class)->now();

$year=$now->format('Y');
$month=$now->format('m');

$firstdayofmonth=$now->setDate($year,$month,1);
$dayofweek=$firstdayofmonth->format('N');
echo$dayofweek;
```

## See also[​](#see-also "Direct link to See also")

- [Php DateTime class](https://www.php.net/manual/en/class.datetime)
- [Core APIs](https://moodledev.io/docs/5.2/apis)