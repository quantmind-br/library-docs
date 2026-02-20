---
title: Date and Time Output Classes | Moodle Developer Resources
url: https://moodledev.io/docs/5.1/apis/subsystems/output/humandate
source: sitemap
fetched_at: 2026-02-17T15:36:56.061775-03:00
rendered_js: false
word_count: 108
summary: This document explains how to use the humandate and humantimeperiod classes in Moodle to render timestamps and time ranges in human-readable formats. It details how to implement these classes for displaying dates like Today or Yesterday with optional styling and links.
tags:
    - moodle-development
    - date-formatting
    - php-classes
    - ui-rendering
    - human-readable-time
    - timestamp-display
category: reference
---

The `humandate` and `humantimeperiod` classes in Moodle are designed to render timestamps and time periods in a human-readable format. These classes provide functionality to display dates as "Today", "Yesterday", "Tomorrow", and apply alert styling if the date is near the current date.

Both classes can be used as a normal output class in Moodle. Each class represent way of show dates and time in a human readable way:

The `humandate` class is used to render a single timestamp as a human-readable date.

This will output "Today" if the timestamp is for the current day.

```
usecore_calendar\output\humandate;

$renderer=$PAGE->get_renderer('core','output');
$timestamp=(\core\di::get(\core\clock::class))->time();

// Basic example.
$humandate=humandate::create_from_timestamp($timestamp);
echo$renderer->render($humandate);

// Example adding a link to the date.
$humandate=humandate::create_from_timestamp(
timestamp:$timestamp,
link:newcore\url('/calendar/view.php',['view'=>'day','time'=>$timestamp]),
);
echo$renderer->render($humandate);

// Example showing only the time.
$humandate=humandate::create_from_timestamp(
timestamp:$timestamp,
timeonly:true,
);
echo$renderer->render($humandate);
```

The `humantimeperiod` class is used to render a time period in a human-readable format.

```
usecore_calendar\output\humantimeperiod;

$renderer=$PAGE->get_renderer('core','output');
$starttimestamp=(\core\di::get(\core\clock::class))->time();
$endtimestamp=$starttimestamp+HOURSECS;

// Basic example.
$humantimeperiod=humantimeperiod::create_from_timestamp($starttimestamp,$endtimestamp);
echo$renderer->render($humantimeperiod);

// Example adding a link to the date.
$humantimeperiod=humantimeperiod::create_from_timestamp(
starttimestamp:$starttimestamp,
endtimestamp:$endtimestamp,
link:newcore\url('/calendar/view.php',['view'=>'day','time'=>$starttimestamp]),
);
echo$renderer->render($humantimeperiod);
```