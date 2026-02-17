---
title: Time API | Moodle Developer Resources
url: https://moodledev.io/docs/4.4/apis/subsystems/time
source: sitemap
fetched_at: 2026-02-17T15:05:03.604073-03:00
rendered_js: false
word_count: 637
summary: This document explains how Moodle's Time API manages and displays date-time information across different timezones using the core_date class. It details the distinction between system and user time while providing functions for safe timestamp manipulation and formatting.
tags:
    - moodle
    - time-api
    - timezone-handling
    - php-datetime
    - unixtime
    - daylight-savings
    - core-date
category: api
---

Version: 4.4

Internally Moodle always stores all times in unixtime format (number of seconds since epoch) which is independent of timezones.

The Time API is used to display proper date-time depending on user or site timezones.

## Functions[​](#functions "Direct link to Functions")

There is a class in Moodle to handle most needs of working with times. There are 2 cases to consider when working with time:

System Time

This is when you are dealing with dates on the server e.g. executing scheduled tasks, performing background tasks - anything which does not depend on the timezone of any specific user.

User Time

This is when you are manipulating dates and times and you need to display them to the user in their current timezone (which may be different for each user).

The main API for time is in the class "core\_date" which will give you php DateTimeZone objects for either user time or server time as needed. You can then use the php datetime classes to manipulate the time. When finished manipulating the time, get a timestamp with DateTime::getTimestamp().

Example: Get the current server time + 1 day.

```
$tomorrow=newDateTime("1 day",core_date::get_server_timezone_object());
```

Get a timestamp for storing in the database:

```
$tomorrowint=$tomorrow->getTimestamp();
```

Get a timestamp for 3pm tomorrow in the current users timezone.

```
$time=newDateTime("now",core_date::get_user_timezone_object());
$time->add(newDateInterval("P1D"));
$time->setTime(15,0,0);

$timestamp=$time->getTimestamp();
```

danger

Never add or subtract timestamps for any reason - you will get it wrong (DST is a killer)!

Other functions related to time api can be found in lib/moodlelib.php.

1. Time API's for current user
   
   - **make\_timestamp** - Given date-time, it produces a GMT timestamp for current user.
   - **userdate** - Gets formatted string that represents a date in user time (note that the format required by this function is the [strftime()](https://www.php.net/manual/en/function.strftime.php) format, not the more common format used by date())
   - **usertime** - Given a GMT timestamp (seconds since epoch), offsets it by the timezone. eg 3pm in India is 3pm GMT - 5.5 * 3600 seconds
   - **usergetdate** - Given a timestamp in GMT, returns an array that represents the date-time in user time
   - **usergetmidnight** - Given a date, return the GMT timestamp of the most recent midnight for the current user.
   - **usertimezone** - Returns current user's timezone
2. System Time API
   
   - **format\_time** - Format a date/time (seconds) as weeks, days, hours etc as needed
   - **dst\_offset\_on** - Calculates the Daylight Saving Offset for a given date/time (timestamp)
   - **find\_day\_in\_month** - Calculates when the day appears in specific month
   - **days\_in\_month** - Calculate number of days in a given month
   - **dayofweek** - Calculate the position in the week of a specific calendar day
3. Older legacy date/time functions. Do not use in new code.
   
   - **usertime** - Appends the users timezone offset to an integer timestamp
   - **get\_timezone\_offset** - Systems's timezone difference from GMT in seconds
   - **get\_user\_timezone\_offset** - Returns user's timezone difference from GMT in hours
   - **dst\_changes\_for\_year** - Calculates the required DST change and returns a Timestamp Array

## Glossary[​](#glossary "Direct link to Glossary")

### Timezone[​](#timezone "Direct link to Timezone")

Moodle supports following timezone formats:

1. UTC (specifically UTC−11 to UTC+11)
2. Time offsets from UTC (int +-(0-13) or float +-(0.5-12.5))
3. World timezones (Australia/Perth)

### Location[​](#location "Direct link to Location")

Timezone depends on [Location](https://docs.moodle.org/en/Location) of the user and can be forced upon by administrator.

### DST[​](#dst "Direct link to DST")

DST is abbreviation of **Daylight Saving Time** (also known as "Day light saving" and "Summer Time"). Many countries, and sometimes just certain regions of countries, adopt daylight saving time during part of the year. Moodle automatically calculates DST for current user, depending on user location.

## Examples[​](#examples "Direct link to Examples")

### Create DateTime with date/time from a unixtime (number of seconds)[​](#create-datetime-with-datetime-from-a-unixtime-number-of-seconds "Direct link to Create DateTime with date/time from a unixtime (number of seconds)")

```
$date=newDateTime();
$date->setTimestamp(intval($unixtime);
echouserdate($date->getTimestamp());
```

### Time API's for current user[​](#time-apis-for-current-user "Direct link to Time API's for current user")

Prints the current date and time in the user's timezone:

```
$now=time();
echouserdate($now);
```

To manually specify the display format, use one of the formatting strings defined in the `core_langconfig` component of the user's language. For example, to display just the date without the time, use:

```
echouserdate(time(),get_string('strftimedaydate','core_langconfig'));
```

You can also use the `DateTime` class to obtain the timestamp:

```
$date=newDateTime("tomorrow",core_date::get_user_timezone_object());
$date->setTime(0,0,0);
echouserdate($date->getTimestamp(),get_string('strftimedatefullshort','core_langconfig'));
```

### System Time API[​](#system-time-api "Direct link to System Time API")

Find the day of the week for the first day in this month.

```
$now=newDateTime("now",core_date::get_server_timezone_object());

$year=$now->format('Y');
$month=$now->format('m');

$now->setDate($year,$month,1);
$dayofweek=$now->format('N');
echo$dayofweek;
```

## See also[​](#see-also "Direct link to See also")

- [Php DateTime class](https://www.php.net/manual/en/class.datetime)
- [Core APIs](https://moodledev.io/docs/4.4/apis)