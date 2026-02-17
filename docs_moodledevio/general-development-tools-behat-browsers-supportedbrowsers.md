---
title: Working combinations of OS+Browser+selenium | Moodle Developer Resources
url: https://moodledev.io/general/development/tools/behat/browsers/supportedbrowsers
source: sitemap
fetched_at: 2026-02-17T16:01:05.241763-03:00
rendered_js: false
word_count: 1000
summary: This document provides a compatibility matrix of supported operating systems, browsers, and Selenium driver versions for various Moodle releases to ensure successful automated testing.
tags:
    - moodle
    - selenium
    - behat
    - browser-compatibility
    - automated-testing
    - web-drivers
    - operating-systems
category: reference
---

As OS, Browsers and Selenium keeps updating, some combination might fail on different Moodle releases.

Following combinations have been tested at the time of release of Moodle version and will be supported for that combination.

## Moodle 3.9 and up[​](#moodle-39-and-up "Direct link to Moodle 3.9 and up")

OS

Browser

Selenium Server

Browser Driver

Notes

Linux - Debian Stretch/Buster

Firefox 83.0

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[Geckodriver 0.30.0](https://github.com/mozilla/geckodriver/releases/tag/v0.30.0)

Linux - Debian Stretch/Buster

Chrome 86

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[86.0.4240.22](https://chromedriver.storage.googleapis.com/?path=86.0.4240.22%2F)

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

MacOS X

Firefox 83.0

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[Geckodriver 0.30.0](https://github.com/mozilla/geckodriver/releases/tag/v0.30.0)

MacOS X

Chrome 86

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[86.0.4240.22](https://chromedriver.storage.googleapis.com/?path=86.0.4240.22%2F)

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

Windows

Firefox 83.0

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[Geckodriver 0.30.0](https://github.com/mozilla/geckodriver/releases/tag/v0.30.0)

Windows

Chrome 86

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[86.0.4240.22](https://chromedriver.storage.googleapis.com/?path=86.0.4240.22%2F)

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

note

Many of the combinations below, for older versions of Moodle 3.5 and up, should continue working acceptably well for Moodle 3.9 and up. Just the those listed above are actively being used now (CI infrastructure, developers...), hence, verified to be running ok. Feel free to add more relevant working combinations!

## Moodle 3.5 and up[​](#moodle-35-and-up "Direct link to Moodle 3.5 and up")

OS

Browser

Selenium Server

Chrome Driver

IE Driver

Notes

Linux - Debian Stretch/Buster

Firefox 47.0.1

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

N/A

N/A

Requires special behat config ([more info here](https://docs.moodle.org/dev/Actual_Selenium_with_old_Firefox_47.0.1))

Linux - Debian Stretch/Buster

Chrome 66

[3.11.0](https://selenium-release.storage.googleapis.com/3.11/selenium-server-standalone-3.11.0.jar)

[2.38](http://chromedriver.storage.googleapis.com/?path=2.38%2F)

N/A

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

MacOS X

Firefox 47.0.1

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

N/A

N/A

Requires special behat config ([more info here](https://docs.moodle.org/dev/Actual_Selenium_with_old_Firefox_47.0.1))

MacOS X

Chrome 72

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[2.46](http://chromedriver.storage.googleapis.com/?path=2.46%2F)

N/A

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

Windows

Firefox 47.0.1

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

N/A

N/A

Requires special behat config ([more info here](https://docs.moodle.org/dev/Actual_Selenium_with_old_Firefox_47.0.1))

Windows

Chrome 72

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[72.0.3626.69](https://chromedriver.storage.googleapis.com/?path=72.0.3626.69%2F)

N/A

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

note

Many of the combinations below, for Moodle 3.1 and up, should continue working acceptably well for Moodle 3.5 and up. Just the those listed above are actively being used now (CI infrastructure, developers...), hence, verified to be running ok. Feel free to add more relevant working combinations!

## Moodle 3.4[​](#moodle-34 "Direct link to Moodle 3.4")

OS

Browser

Selenium Server

Chrome Driver

IE Driver

Notes

Linux - Debian Stretch

Firefox 47.0.1

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

N/A

N/A

Requires special behat config ([more info here](https://docs.moodle.org/dev/Actual_Selenium_with_old_Firefox_47.0.1))

Linux - Debian Stretch

Chrome 66

[3.11.0](https://selenium-release.storage.googleapis.com/3.11/selenium-server-standalone-3.11.0.jar)

[2.38](http://chromedriver.storage.googleapis.com/?path=2.38%2F)

N/A

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

MacOS X

Firefox 47.0.1

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

N/A

N/A

Requires special behat config ([more info here](https://docs.moodle.org/dev/Actual_Selenium_with_old_Firefox_47.0.1))

MacOS X

Chrome 72

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[2.46](http://chromedriver.storage.googleapis.com/?path=2.46%2F)

N/A

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

Windows

Chrome 72

[3.141.59](https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar)

[72.0.3626.69](https://chromedriver.storage.googleapis.com/?path=72.0.3626.69%2F)

N/A

Any other valid combination should work ok, normally.  
(Here there is a [good list](https://github.com/SeleniumHQ/docker-selenium/releases) of them, as reference)

Chrome &gt;=76 can be used since Moodle 20190909 builds.

Chrome &gt;=93 can be used since Moodle 20210916 builds and requires to exclude the @skip\_chrome\_zerosize [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108) tags till the browser issue is fixed.

## Moodle 3.2 and 3.3[​](#moodle-32-and-33 "Direct link to Moodle 3.2 and 3.3")

OS

Browser

Selenium Server

Chrome Driver

IE Driver

Linux - Ubuntu 16.04

Firefox 47.0.1

[2.53.1](http://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.1.jar)

N/A

N/A

Linux - Ubuntu 16.04

[Chrome 53.0](https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F403380%2Fchrome-linux.zip?generation=1467337264475000&alt=media)

[3.0.1](http://selenium-release.storage.googleapis.com/?path=3.0%2F)

[2.25](http://chromedriver.storage.googleapis.com/?path=2.25%2F)

N/A

Linux - Ubuntu 16.04

Phantomjs 2.1.1

2.53.1

N/A

N/A

Windows 7/10

Firefox 47.0.1

2.53.1

N/A

N/A

Windows 7/10

Chrome v53.0

[3.0.1](http://selenium-release.storage.googleapis.com/?path=3.0%2F)

[2.25](http://chromedriver.storage.googleapis.com/?path=2.25%2F)

N/A

MacOS X

Firefox 47.0.1

2.53.1

N/A

N/A

MacOS X

[Chrome v53.0](http://www.slimjet.com/chrome/google-chrome-old-version.php)

[3.0.1](http://selenium-release.storage.googleapis.com/?path=3.0%2F)

[2.25](http://chromedriver.storage.googleapis.com/?path=2.25%2F)

N/A

## Moodle 3.1[​](#moodle-31 "Direct link to Moodle 3.1")

OS

Browser

Selenium Server

Chrome Driver

IE Driver

Linux - Ubuntu 16.04

[Firefox 47.0.1](https://download.mozilla.org/?product=firefox-47.0.1-SSL&os=linux64&lang=en-GB)

[2.53.1](http://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.1.jar)

N/A

N/A

Linux - Ubuntu 16.04

[Chrome 51.0](https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F386249%2Fchrome-linux.zip?generation=1460160957434000&alt=media)

2.53.1

2.22

N/A

Linux - Ubuntu 16.04

Phantomjs 2.1.1

2.53.1

N/A

N/A

Windows 7/10

Firefox 47.0.1

2.53.1

N/A

N/A

Windows 7/10

Chrome v51.0

2.53.1

2.22

N/A

MacOS X

Firefox 47.0.1

2.53.1

N/A

N/A

MacOS X

Chrome v51.0

2.53.1

2.22

N/A

MacOS X

PhantomJS 2.1.1

2.53.1

N/A

N/A

## Moodle 3.0 and lower[​](#moodle-30-and-lower "Direct link to Moodle 3.0 and lower")

OS

Browser

Selenium Server

Chrome Driver

IE Driver

Linux - Ubuntu 14.10

Firefox 42.0

2.47.1

N/A

N/A

Linux - Ubuntu 14.10

Chrome 46.0

2.47.1

2.19.346067

N/A

Linux - Ubuntu 14.10

Phantomjs 2.0.0

2.47.1

N/A

N/A

Windows 7/10

Firefox 41.0

2.47.1

N/A

N/A

Windows 7/10

Chrome 47.0

2.47.1

2.20

N/A

MacOS X

Firefox 41.0

2.47.1

N/A

N/A

MacOS X

Chrome 46.0

2.47.1

2.20

N/A

MacOS X

Chrome 48.0

2.51.0

2.21

N/A

MacOS X

PhantomJS - 2.0.0 & 2.1.1

2.48.2

N/A

N/A