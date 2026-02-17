---
title: Plugins directory API | Moodle Developer Resources
url: https://moodledev.io/general/community/plugincontribution/pluginsdirectory/api
source: sitemap
fetched_at: 2026-02-17T15:58:01.607592-03:00
rendered_js: false
word_count: 402
summary: This document describes the web services API for the Moodle.org Plugins directory, covering authentication methods and functions for managing plugin releases. It explains how to programmatically retrieve a list of maintained plugins and submit new versions using specific web service calls.
tags:
    - moodle-plugins
    - web-services
    - api-authentication
    - plugin-management
    - automation
    - rest-api
category: api
---

The Plugins directory at [http://moodle.org/plugins](http://moodle.org/plugins) exposes some of its features via web services layer, allowing the community to develop custom tools and integrations with other services such as GitHub Actions or Travis CI.

## Access token[​](#access-token "Direct link to Access token")

To use the web service described below, the caller (client) authenticates itself with an access token. In almost all cases, developers use their own personal token and let the scripts (clients) work on behalf of them.

The easiest way to obtain the access token (and some other useful information) is to visit *Plugins &gt; API access* page at moodle.org through the side Navigation block.

The token can be alternatively obtained via the *Preferences &gt; Security keys* or programmatically via `login/token.php` script at moodle.org (however, tokens obtain that way have very short expiration in contrast with the ones generated at the dedicated page).

## Plugins maintenance service[​](#plugins-maintenance-service "Direct link to Plugins maintenance service")

The Plugins maintenance service (`plugins_maintenance`) provides functions for the plugins maintainers. The service is declared as:

```
'Plugins maintenance'=>[
'functions'=>[
'local_plugins_get_maintained_plugins',
'local_plugins_add_version',
],
'shortname'=>'plugins_maintenance',
'requiredcapability'=>'local/plugins:editownplugins',
'enabled'=>true,
'restrictedusers'=>0,
'downloadfiles'=>true,
'uploadfiles'=>true,
],
```

### Getting the list of maintained plugins[​](#getting-the-list-of-maintained-plugins "Direct link to Getting the list of maintained plugins")

The first external function `local_plugins_get_maintained_plugins` allows to read the list of all plugins and their recent versions the caller is maintainer of. It does not expect any parameters and its return structure is described as follows:

```
returnnewexternal_multiple_structure(
newexternal_single_structure([
'id'=>newexternal_value(PARAM_INT,'Internal plugin identifier'),
'name'=>newexternal_value(PARAM_TEXT,'Name of the plugin'),
'shortdescription'=>newexternal_value(PARAM_TEXT,'Short description'),
'description'=>newexternal_value(PARAM_RAW,'Description'),
'descriptionformat'=>newexternal_format_value('description'),
'frankenstyle'=>newexternal_value(PARAM_PLUGIN,'Full component frankenstyle name'),
'type'=>newexternal_value(PARAM_ALPHANUMEXT,'Plugin type'),
'websiteurl'=>newexternal_value(PARAM_URL,'Website URL'),
'sourcecontrolurl'=>newexternal_value(PARAM_URL,'Source control URL'),
'bugtrackerurl'=>newexternal_value(PARAM_URL,'Bug tracker URL'),
'discussionurl'=>newexternal_value(PARAM_URL,'Discussion URL'),
'timecreated'=>newexternal_value(PARAM_INT,'Timestamp of plugin submission'),
'approved'=>newexternal_value(PARAM_INT,'Approval status'),
'visible'=>newexternal_value(PARAM_BOOL,'Visibility status'),
'aggdownloads'=>newexternal_value(PARAM_INT,'Stats aggregataion - downloads'),
'aggfavs'=>newexternal_value(PARAM_INT,'Stats aggregataion - favourites'),
'aggsites'=>newexternal_value(PARAM_INT,'Stats aggregataion - sites'),
'statusamos'=>newexternal_value(PARAM_INT,'AMOS registration status'),
'viewurl'=>newexternal_value(PARAM_URL,'View URL'),
'currentversions'=>newexternal_multiple_structure(
newexternal_single_structure([
'id'=>newexternal_value(PARAM_INT,'Internal version identifier'),
'version'=>newexternal_value(PARAM_INT,'Version number'),
'releasename'=>newexternal_value(PARAM_TEXT,'Release name'),
'releasenotes'=>newexternal_value(PARAM_RAW,'Release notes'),
'releasenotesformat'=>newexternal_format_value('releasenotes'),
'maturity'=>newexternal_value(PARAM_INT,'Maturity code'),
'changelogurl'=>newexternal_value(PARAM_URL,'Change log URL'),
'altdownloadurl'=>newexternal_value(PARAM_URL,'Alternative download URL'),
'md5sum'=>newexternal_value(PARAM_TEXT,'MD5 hash of the ZIP content'),
'vcssystem'=>newexternal_value(PARAM_ALPHA,'Version control system'),
'vcssystemother'=>newexternal_value(PARAM_TEXT,'Name of the other version control system'),
'vcsrepositoryurl'=>newexternal_value(PARAM_URL,'Version control system URL'),
'vcsbranch'=>newexternal_value(PARAM_TEXT,'Name of the branch with this version'),
'vcstag'=>newexternal_value(PARAM_TEXT,'Name of the tag with this version'),
'timecreated'=>newexternal_value(PARAM_INT,'Timestamp of version release'),
'approved'=>newexternal_value(PARAM_INT,'Approval status'),
'visible'=>newexternal_value(PARAM_BOOL,'Visibility status'),
'supportedmoodle'=>newexternal_value(PARAM_TEXT,'Comma separated list of support Moodle versions'),
'downloadurl'=>newexternal_value(PARAM_URL,'Download URL'),
'viewurl'=>newexternal_value(PARAM_URL,'View URL'),
'smurfresult'=>newexternal_value(PARAM_TEXT,'Code prechecks results summary'),
])
),
])
);
```

Example cURL client fetching the list of maintained plugins

```
#!/bin/bash

# Replace this with your own service access token.
TOKEN="d41d8cd98f00b204e9800998ecf8427e"

CURL="curl -s"
ENDPOINT=https://moodle.org/webservice/rest/server.php
FUNCTION=local_plugins_get_maintained_plugins

${CURL} ${ENDPOINT} --data-urlencode "wstoken=${TOKEN}" --data-urlencode "wsfunction=${FUNCTION}" \
    --data-urlencode "moodlewsrestformat=json" | jq
```

### Releasing a new version[​](#releasing-a-new-version "Direct link to Releasing a new version")

The second function `local_plugins_add_version` allows to release a new version to the plugin. The input parameters are described as:

```
returnnewexternal_function_parameters([
// The pluginid or frankenstyle must be provided (in this order of precedence).
'pluginid'=>newexternal_value(PARAM_INT,'Internal identifier of the plugin',VALUE_DEFAULT,null),
'frankenstyle'=>newexternal_value(PARAM_PLUGIN,'Full component name of the plugin',VALUE_DEFAULT,null),
// ZIP can be specified by draft area itemid (with single file in it), content or URL (in this order of precedence).
'zipdrafitemtid'=>newexternal_value(PARAM_INT,'Itemid of user draft area with uploaded ZIP',VALUE_DEFAULT,null),
'zipcontentsbase64'=>newexternal_value(PARAM_RAW,'ZIP file contents encoded with MIME base64',VALUE_DEFAULT,null),
'zipurl'=>newexternal_value(PARAM_URL,'ZIP file URL',VALUE_DEFAULT,null),
// Following params may be auto-detected from the ZIP content.
'version'=>newexternal_value(PARAM_INT,'Version number',VALUE_DEFAULT,null),
'releasename'=>newexternal_value(PARAM_TEXT,'Release name',VALUE_DEFAULT,null),
'releasenotes'=>newexternal_value(PARAM_RAW,'Release notes',VALUE_DEFAULT,null),
'releasenotesformat'=>newexternal_format_value('releasenotes',VALUE_DEFAULT,FORMAT_MOODLE),
'maturity'=>newexternal_value(PARAM_INT,'Maturity code',VALUE_DEFAULT,null),
'supportedmoodle'=>newexternal_value(PARAM_TEXT,'Comma separated list of supported Moodle versions',
VALUE_DEFAULT,null),
// Other optional properties.
'changelogurl'=>newexternal_value(PARAM_URL,'Change log URL',VALUE_DEFAULT,null),
'altdownloadurl'=>newexternal_value(PARAM_URL,'Alternative download URL',VALUE_DEFAULT,null),
'vcssystem'=>newexternal_value(PARAM_ALPHA,'Version control system',VALUE_DEFAULT,null),
'vcssystemother'=>newexternal_value(PARAM_TEXT,'Name of the other version control system',VALUE_DEFAULT,null),
'vcsrepositoryurl'=>newexternal_value(PARAM_URL,'Version control system URL',VALUE_DEFAULT,null),
'vcsbranch'=>newexternal_value(PARAM_TEXT,'Name of the branch with this version',VALUE_DEFAULT,null),
'vcstag'=>newexternal_value(PARAM_TEXT,'Name of the tag with this version',VALUE_DEFAULT,null),
]);
```

The API has been designed so that:

- The actual ZIP can be taken from pre-uploaded file (standard way of using `webservice/upload.php`), or submitting the file contents directly, or providing an URL the ZIP should be fetched from.
- As many as possible parameters (such as list of supported Moodle versions, release name, release notes etc) default to the values specified in the ZIP itself.
- So it should be enough to specify just the plugin (either by numerical ID number of frankenstyle) and the ZIP with the new version. All other values are optional and can be used to override the auto-detected ones.

When successful, the external function's response is described as:

```
returnnewexternal_single_structure([
'id'=>newexternal_value(PARAM_INT,'Internal identifier of the newly created version'),
'md5sum'=>newexternal_value(PARAM_TEXT,'MD5 hash of the ZIP content'),
'timecreated'=>newexternal_value(PARAM_INT,'Timestamp of version release'),
'downloadurl'=>newexternal_value(PARAM_URL,'Download URL'),
'viewurl'=>newexternal_value(PARAM_URL,'View URL'),
'warnings'=>newexternal_multiple_structure(
newexternal_value(PARAM_RAW,'Validation warnings')
),
]);
```

Example CLI script to release a new version of a plugin

```
#!/bin/bash

# Replace this with your own service access token.
TOKEN="d41d8cd98f00b204e9800998ecf8427e"

# Set the full component name of the plugin.
PLUGIN=mod_subcourse
# Path to the ZIP fle with the new version.
ZIP=version.zip

CURL="curl -s"
HOST="https://moodle.org/"
ENDPOINT_REST="${HOST}/webservice/rest/server.php"
ENDPOINT_UPLOAD="${HOST}/webservice/upload.php"

ITEMID=$(${CURL} -F data=@${ZIP} "${ENDPOINT_UPLOAD}?token=${TOKEN}" | jq --raw-output '.[0].itemid')

${CURL} ${ENDPOINT_REST} --data-urlencode "wstoken=${TOKEN}" --data-urlencode "wsfunction=${FUNCTION}" --data-urlencode "moodlewsrestformat=json" \
    --data-urlencode "frankenstyle=${PLUGIN}" --data-urlencode "zipdrafitemtid=${ITEMID}" | jq
```

### GitHub Actions[​](#github-actions "Direct link to GitHub Actions")

A new workflow can be configured at GitHub Actions to automatically release a new version in the Plugins directory once a tag is pushed to the repository. Please see [https://github.com/moodlehq/moodle-plugin-release](https://github.com/moodlehq/moodle-plugin-release) for details.

- [Access token](#access-token)
- [Plugins maintenance service](#plugins-maintenance-service)
  
  - [Getting the list of maintained plugins](#getting-the-list-of-maintained-plugins)
  - [Releasing a new version](#releasing-a-new-version)
  - [GitHub Actions](#github-actions)