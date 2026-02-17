---
title: Troubleshooting Moodle App Plugins Development | Moodle Developer Resources
url: https://moodledev.io/general/app/development/plugins-development-guide/troubleshooting
source: sitemap
fetched_at: 2026-02-17T15:54:54.744298-03:00
rendered_js: false
word_count: 190
summary: This document provides solutions for common troubleshooting issues encountered during Moodle app plugin development, specifically addressing Web Service response types and data structure limitations.
tags:
    - moodle-app
    - plugin-development
    - troubleshooting
    - web-services
    - core-site-plugins-call-ws
    - data-handling
category: guide
---

## Plugin changes are not picked up in the app[​](#plugin-changes-are-not-picked-up-in-the-app "Direct link to Plugin changes are not picked up in the app")

Remember to go through the list of tips in the [Seeing plugin changes in the app](https://moodledev.io/general/app/development/plugins-development-guide#seeing-plugin-changes-in-the-app) section.

## Invalid response received[​](#invalid-response-received "Direct link to Invalid response received")

You might get this error when using the [core-site-plugins-call-ws](https://moodledev.io/general/app/development/plugins-development-guide/api-reference#core-site-plugins-call-ws) directive or similar.

By default, the app expects all Web Service calls to return an object. If your Web Service returns another type, you need to specify it using the `preSets` attribute in the directive.

For example, if your Web Service returns a boolean you should specify it like this:

```
<ion-buttoncore-site-plugins-call-wsname="local_sample_submit"[preSets]="{ typeExpected: 'boolean' }">
    {{ 'plugin.local_sample.submit' | translate }}
</ion-button>
```

Similarly, if the Web Service returns `null` you need to tell the app not to expect any result using `preSets`:

```
<ion-buttoncore-site-plugins-call-wsname="local_sample_submit"[preSets]="{ responseExpected: false }">
    {{ 'plugin.local_sample.submit' | translate }}
</ion-button>
```

## I can't return an object or array in `otherdata`[​](#i-cant-return-an-object-or-array-in-otherdata "Direct link to i-cant-return-an-object-or-array-in-otherdata")

If you try to return an object or an array in any field inside `otherdata` in [content responses](https://moodledev.io/general/app/development/plugins-development-guide/api-reference#content-responses), the Web Service call will fail with the following error:

```
Scalar type expected, array or object received
```

Each field in `otherdata` must be a string, number or boolean; it cannot be an object or array. If you need to send complex values, you can use `json_encode`:

```
'otherdata'=>['data'=>json_encode($data)],
```

The app will parse the string and it will be available as an array or object.