---
title: Geolocation & Intl | Camoufox
url: https://camoufox.com/fingerprint/geolocation/
source: sitemap
fetched_at: 2026-03-09T16:48:07.605674-03:00
rendered_js: false
word_count: 172
summary: This document describes various properties available for configuration, detailing their types, descriptions, and associated required keys for functionality.
tags:
    - configuration-properties
    - geolocation
    - locale-settings
    - timezone
    - data-types
category: reference
---

* * *

## [#](#properties)Properties

PropertyTypeDescriptionRequired Keys`geolocation:latitude`doubleLatitude to use.`geolocation:longitude``geolocation:longitude`doubleLongitude to use.`geolocation:latitude``geolocation:accuracy`doubleAccuracy in meters. This will be calculated automatically using the decminal percision of `geolocation:latitude` & `geolocation:longitude` if not set. `timezone`strSet a custom TZ timezone (e.g. "America/Chicago"). This will also change `Date()` to return the local time. `locale:language`strSpoof the Intl API and system language (e.g. "en")`locale:region``locale:region`strSpoof the Intl API and system region (e.g. "US").`locale:language``locale:script`strSet a custom script (e.g. "Latn"). Will be set automatically if not specified. `locale:all`strList of all accepted locale values (separated by comma). The first item should match the Intl API. If not passed, it will default to the locale used in the Intl API in the format `"en-US, en"`. 

The **Required Keys** are keys that must also be set for the property to work.

* * *

##### Note

- Location permission prompts will be accepted automatically if `geolocation:latitude` and `geolocation:longitude` are set.
- `timezone` **must** be set to a valid TZ identifier. See [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for a list of valid timezones.
- `locale:language` & `locale:region` **must** be set to valid locale values. See [here](https://simplelocalize.io/data/locales/) for a list of valid locale-region values.