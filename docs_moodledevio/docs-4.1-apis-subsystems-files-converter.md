---
title: File Converters | Moodle Developer Resources
url: https://moodledev.io/docs/4.1/apis/subsystems/files/converter
source: sitemap
fetched_at: 2026-02-17T14:56:28.813886-03:00
rendered_js: false
word_count: 392
summary: This document provides an overview of Moodle's file converter API, explaining how to initiate file conversions, track their status, and retrieve the resulting files.
tags:
    - moodle
    - file-conversion
    - api-documentation
    - file-management
    - php
    - document-processing
category: api
---

Users are able to submit a wide range of files, and it is a common requirement to convert these to alternative formats.

The most obvious example of this in Moodle core is in the `assignfeedback_editpdf` plugin which allows for conversion from a variety of document types into PDF to facilitate annotation.

The file converters distributed with Moodle currently are:

- Unoconv
- Google Drive

The file converter API allows for conversion via multiple plugins and will automatically fallback to another suitable plugin upon failure.

The API is designed to be called asynchronously as many cloud services offering document conversion offer an asynchronous API themselves.

## Using the file converter API[​](#using-the-file-converter-api "Direct link to Using the file converter API")

A file conversion is performed by the `core_files\converter` API and a single conversion is represented by the `core\files\conversion` class.

Individual file conversions should always be accessed by the `core_files\converter` API.

A file conversion is fetched or created by calling the `start_conversion` function on the converter API and passing in an existing `stored_file` record, along with the target format.

Starting a new conversion

```
$converter=new\core_files\converter();
$conversion=$converter->start_conversion($file,'pdf');
```

If an existing file conversion matching the file and target format exists, the conversion record for this file will be returned, otherwise a new conversion is created and returned.

To force a fresh conversion, a third boolean parameter can be passed, though this should not normally be necessary.

Forcing a conversion to be performed again

```
$converter=new\core_files\converter();
$conversion=$converter->start_conversion($file,'pdf',true);
```

### Polling for updates on an existing conversion[​](#polling-for-updates-on-an-existing-conversion "Direct link to Polling for updates on an existing conversion")

When the `start_conversion` function is called, it automatically polls for any update on the conversion so it should not normally be necessary to poll the status separately.

It is however possible to do so:

Polling the API for the status of a conversino

```
$converter=new\core_files\converter();
$conversion=$converter->start_conversion($file,'pdf');
$converter->poll_conversion($conversion);
```

### Checking status of a conversion[​](#checking-status-of-a-conversion "Direct link to Checking status of a conversion")

File conversions can have one of four states:

- `STATUS_PENDING` - The conversion has not yet started;
- `STATUS_IN_PROGRESS` - A conversion has been picked up by a file converter and is currently in progress;
- `STATUS_COMPLETE` - The conversion was successful and the converted file is available; and
- `STATUS_FAILED` - All attempts to convert the file have failed.

The conversion API provides a way to check the status of the conversion with the `$conversion->get_status()` function:

Fetching status

```
$converter=new\core_files\converter();
$conversion=$converter->start_conversion($file,'pdf');

switch($conversion->get_status()){
case\core_files\conversion::STATUS_COMPLETE:
// The file is ready. Do something with it.
case\core_files\conversion::STATUS_PENDING:
case\core_files\conversion::STATUS_IN_PROGRESS:
// Conversion still ongoing. Display spinner to the user.
case\core_files\conversion::STATUS_FAILED:
// Permanent failure - handle to the user.
}
```

### Fetching the target file[​](#fetching-the-target-file "Direct link to Fetching the target file")

Following a conversion, the target file is stored as a `stored_file` record and can be fetched for consumption elsewhere in your API:

Fetching the new file

```
if($conversion->get_status()===\core_files\conversion::STATUS_COMPLETE){
$file=$conversion->get_destfile();
}
```

## See also[​](#see-also "Direct link to See also")

- Creating a new [file converter plugin](https://moodledev.io/docs/4.1/apis/plugintypes/fileconverter)