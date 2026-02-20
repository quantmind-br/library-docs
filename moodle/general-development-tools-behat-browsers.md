---
title: Browsers | Moodle Developer Resources
url: https://moodledev.io/general/development/tools/behat/browsers
source: sitemap
fetched_at: 2026-02-17T16:00:59.624963-03:00
rendered_js: false
word_count: 455
summary: This document provides instructions for configuring and running Behat acceptance tests across different web browsers using Selenium drivers and PhantomJS. It covers driver installation, operating system-specific setup, and browser compatibility for specific test features.
tags:
    - behat
    - acceptance-testing
    - selenium-drivers
    - phantomjs
    - browser-compatibility
    - moodle-development
category: guide
---

This page complements [Behat](https://moodledev.io/general/development/tools/behat) providing info about how to run the acceptance tests suite in different browsers.

## Drivers[​](#drivers "Direct link to Drivers")

There are [Selenium drivers](http://docs.seleniumhq.org/projects/webdriver/) to run acceptance tests in different browsers:

- Firefox - [https://code.google.com/p/selenium/wiki/FirefoxDriver](https://code.google.com/p/selenium/wiki/FirefoxDriver)
- Chrome - [https://code.google.com/p/selenium/wiki/ChromeDriver](https://code.google.com/p/selenium/wiki/ChromeDriver)
- Safari - [https://code.google.com/p/selenium/wiki/SafariDriver](https://code.google.com/p/selenium/wiki/SafariDriver)
- Internet Explorer - [https://code.google.com/p/selenium/wiki/InternetExplorerDriver](https://code.google.com/p/selenium/wiki/InternetExplorerDriver)
- Microsoft Edge - [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- PhantomJS (Webkit) - [http://phantomjs.org/](http://phantomjs.org/)
- IPhone - [https://code.google.com/p/selenium/wiki/IPhoneDriver](https://code.google.com/p/selenium/wiki/IPhoneDriver)

Each driver should be downloaded and Selenium .jar should be started specifying the path to the driver; depending on the driver there could be other requirements.

### PhantomJS[​](#phantomjs "Direct link to PhantomJS")

PhantomJS is different as it is a headless browser as it is quite faster than other drivers, it doesn't need a GUI to run and can execute JS, it doesn't even need to be used through Selenium (you can do it though, but it's not officially supported) and you can do it

- Download PhantomJS: [http://phantomjs.org/download.html](http://phantomjs.org/download.html)
- Run the following command
  
  ```
  /path/to/your/phantomjs/bin/phantomjs --webdriver=4444
  ```

Note that 4444 is the default port used by Selenium, so you must specify another one if you want to run them together and specify the port in `$CFG->behat_config`.

### Examples[​](#examples "Direct link to Examples")

Selenium in Linux (firefox by default + chrome)

```
   java -jar /opt/selenium-server-standalone.jar -Dwebdriver.chrome.driver=/opt/chromedriver
```

Selenium in OSx (firefox & safari by default + chrome)

```
  java -jar /Users/moodle/Downloads/selenium-server-standalone.jar -Dwebdriver.chrome.driver=/Users/moodle/Downloads/chromedriver
```

Selenium in Windows (started using git bash) (firefox by default + chrome + internet explorer)

```
  java -jar /c/seleniumdrivers/selenium-server-standalone.jar -Dwebdriver.chrome.driver=/c/seleniumdrivers/chromedriver.exe -Dwebdriver.ie.driver=/c/seleniumdrivers/IEDriverServer.exe
```

PhantomJS

```
  /path/to/your/phantomjs/bin/phantomjs --webdriver=4444
```

## Compatibility[​](#compatibility "Direct link to Compatibility")

Not all the drivers can execute all of Moodle's step definitions; we tagged the step definitions that are using features not supported by all browsers and also limitations that some browsers have; refer to the following table to know which browsers can run which tags:

| | File uploads (@\_file\_upload) | Browser dialogs (@\_alert) | Switch window (@\_switch\_window) | Switch frame (@\_switch\_iframe) | Bugs in chrome (@skip\_chrome\_zerosize) | Bug in phantomjs (@\_bug\_phantomjs) | |------------------------------|-------------------------------------------------------------------|---------------------------------|--------------------------------|----------------------------------------|------------------------------------| | Firefox | Yes | Yes | Yes | Yes | Yes | Yes | | Chrome | Yes | Yes | Yes | Yes | No (see [MDL-71108](https://moodle.atlassian.net/browse/MDL-71108)) | Yes | | Internet Explorer | Yes | Yes | No | Yes | Yes | Yes | | Safari | Yes | No | No | Yes | Yes | Yes | | PhantomJS | No | No | Yes | Yes | Yes | No |

Note that, to skip some tag, you must prepend it with the `~` (logical NOT) character. Examples:

- Run all tests but `@_alert</tt> ones: <tt>--tags '~@_alert'`
- Run all chrome tests but `@skip_chrome_zerosize` ones: `--tags '@javascript&&~@skip_chrome_zerosize'`

## Working combinations of OS+Browser+selenium[​](#working-combinations-of-osbrowserselenium "Direct link to Working combinations of OS+Browser+selenium")

As OS, Browsers and Selenium keeps updating, some combination of OS+Browser+Selenium will not work on specific moodle version.

We try to support the latest version of these combinations but they are not always BC and hence may not work with older releases. Please refer to [Working combinations of OS+Browser+selenium](https://moodledev.io/general/development/tools/behat/browsers/supportedbrowsers) to ensure you have correct combination of them to run acceptance test.