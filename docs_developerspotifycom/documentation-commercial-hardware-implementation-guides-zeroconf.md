---
title: ZeroConf API | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/zeroconf
source: crawler
fetched_at: 2026-02-27T23:41:26.68991-03:00
rendered_js: true
word_count: 1669
summary: This document provides the technical specifications and implementation requirements for the Spotify Connect ZeroConf API, enabling hardware devices to handle local network discovery and secure user authentication.
tags:
    - spotify-connect
    - zeroconf
    - api-specification
    - hardware-integration
    - mdns
    - authentication
    - network-discovery
category: api
---

The Spotify Connect ZeroConf API is an HTTP interface used for announcing and securely logging in to a hardware device. It enables a Spotify client, such as an iOS or Android device, to perform a login to a hardware device without the user entering a password.

The server providing the ZeroConf API can either be running inside the eSDK itself, or be implemented by a Spotify hardware partner. If the builtin ZeroConf server is enabled (see [SpConfig::zeroconf\_serve](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig)) and working satisfactorily on the hardware device, *no ZeroConf implementation is needed* from the Spotify hardware partner. Otherwise, it *must be implemented* to support the Spotify Connect feature.

Implementing the ZeroConf API, when not using the internal builtin ZeroConf service, requires:

- a HTTP server
- a JSON encoding and decoding library
- a mDNS discovery service compatible with Apple's Bonjour.

The partner must then implement the behavior described in this document and hook it up appropriately with the calls to the Spotify Embedded API and their own integration code.

If SSL is supported by the web server, the ZeroConf API should be accessible via HTTPS. When HTTPS is enabled, it is preferred that non-secure HTTP access is disabled.

This is the ZeroConf process:

- The Spotify desktop/smartphone *client* and the hardware *device* connect to the same network.
- The *device's* ZeroConf API service is discovered by the *client* using a service discovery protocol.
- The *client* logs in to the *device* using the ZeroConf API via HTTP.
- The *device* is now ready to be used with Spotify Connect!

## Discovery Service

The hardware device must use mDNS/DNS-SD in a way compatible with Apple's Bonjour, to advertise its IP address, the port of its HTTP service, and the path to the ZeroConf API implementation on the web server.

The DNS-SD service type is `_spotify-connect._tcp`.

- A `SRV` record should be specified with the IP address and port
- A `TXT` record should be provided with `CPath=<path to ZeroConf implementation>`. If a ZeroConf implementation is reachable on `http://host:port/zeroconf`, the TXT record shall be `CPath=/zeroconf`.

## ZeroConf API

See the appendix for error codes and corresponding error strings.

- Requests are made over HTTP using the GET or POST method.
  
  - All requests are answered by a response.
  - Every valid request has the action variable.
  - The `application/x-www-form-urlencoded` encoding is used for POST requests.
- Responses are JSON objects (with Content-Type: `application/json`).
- HTTP status code should match corresponding status from HTTP Status section.
- All strings **must** support UTF-8 character encoding. All strings returned by the Spotify Embedded SDK will be in UTF-8 encoding.
- If requests are handled on their own thread, keep in mind that the Embedded SDK is not thread-safe. You need to ensure that no two threads invoke SDK APIs at the same time. See threading.
- If ZeroConf is turned off on a device that is inactive (ie a slave in a multiroom configuration), mDNS should be turned off. It's not enough to just turn off the webserver endpoints - they will still be hit by clients, spending unnecessary effort.

**Mandatory fields in all responses:**

FieldRequiredTypeDescriptionstatusYesIntegerA code indicating the result of the operationstatusStringYesStringThe string describing the status codespotifyErrorYesIntegerThe last error code returned by a Spotify API call or the SpCallbackError() callbackresponseSourceYesStringThe entity responding on the zeroconf message, i.e. your company name or name of the service. \[1]

**Success example:**

`1`

`{`

`2`

`"status": 101,`

`3`

`"statusString": "OK",`

`4`

`"spotifyError": 0,`

`5`

`"responseSource": "Company name", "other data depending on action"`

`6`

`}`

**Failure example:**

`1`

`{`

`2`

`"status": 402,`

`3`

`"statusString": "ERROR-SPOTIFY-ERROR",`

`4`

`"spotifyError": -119,`

`5`

`"responseSource": "Company name"}`

`6`

`}`

### Add User

The API does not use any passwords. Only the user name and credentials blob are needed when logging in to Spotify.

Login should be performed by calling `SpConnectionLoginZeroConf()` with the data in this message.

Before sending a response, the application must do the following:

- If a user's credentials are already stored, the existing user must be logged out using `SpConnectionLogout()` and the stored data must be deleted from persistent storage (same as resetusers resetUsers request).
- Verify that SpConnectionLoginZeroConf() returns #kSpErrorOk (and fail the request if it returns something else).
- Verify that login is successful by waiting for the #kSpConnectionNotifyLoggedIn event (and fail the request if SpCallbackError() is invoked).

The encrypted blob received in this ZeroConf message **must not** be saved. On a successful login, the SpCallbackConnectionNewCredentials() callback will be invoked with the credentials to save to persistent storage.

The user's credentials **must not** be saved to persistent storage unless the login is successful.

The status **must not** be returned until a #kSpConnectionNotifyLoggedIn or SpCallbackError() event is received.

If any required field is not specified, the response must be an error of type InvalidArguments, and the login function **must not** be called.

**HTTP method:** `POST`.

**Extra parameters:**

FieldRequiredTypeDescriptionuserNameYesStringUser name to loginblobYesStringEncrypted credentials blob for the userclientKeyYesStringDecryption key provided by clientloginIdNoStringLogin ID for this addUser requestversionNoStringSpotify client ZeroConf API version number, ie "2.10.0". Can be used to handle compatibility issuestokenTypeYesStringToken type provided by the client

**Return:** only status.

### Get Information

**HTTP method:** `GET`.

**Extra parameters:**

FieldRequiredTypeDescriptionversionNoStringSpotify client ZeroConf API version number, ie "2.10.0". May be used to handle compatibility issues

**Return:**

FieldRequiredTypeDescriptionversionYesStringZeroConf API version number: "2.10.0"deviceIDYesStringThe `SpZeroConfVars::device_id` field returned by `SpZeroConfGetVars()`. \[1] `deviceID` has to be unique enough to be used for identification on a local network.publicKeyYesStringThe `SpZeroConfVars::public_key` field returned by `SpZeroConfGetVars()` \[1]remoteNameYesStringThe `SpZeroConfVars::remote_name` field returned by `SpZeroConfGetVars()`\[1]deviceTypeNoStringThe `SpZeroConfVars::device_type` field returned by `SpZeroConfGetVars()`\[1]brandDisplayNameYesStringUser-facing brand name of the device \[2]modelDisplayNameNoStringUser-facing model name of the device \[2]libraryVersionYesStringThe `SpZeroConfVars::library_version` field returned by `SpZeroConfGetVars()` \[1]resolverVersionYesStringThe `SpZeroConfVars::resolver_version` field returned by `SpZeroConfGetVars()`\[1]groupStatusYesStringThe `SpZeroConfVars::group_status` field returned by `SpZeroConfGetVars()` \[1]tokenTypeYesStringThe `SpZeroConfVars::token_type` field returned by `SpZeroConfGetVars()` \[1]clientIDYesStringThe `SpZeroConfVars::client_id` field returned by `SpZeroConfGetVars()` \[1]productIDYesIntegerThe `SpZeroConfVars::product_id` field returned by `SpZeroConfGetVars()`\[1]scopeYesIntegerThe `SpZeroConfVars::scope` field returned by `SpZeroConfGetVars()`\[1]availabilityYesStringThe `SpZeroConfVars::availability` field returned by `SpZeroConfGetVars()` \[1]aliasesNoArrayThe `SpZeroConfVars::aliases` field returned by `SpZeroConfGetVars()` \[1]supported\_drm\_media\_formatsNoArrayThe `SpZeroConfVars::supported_drm_media_formats` field returned by `SpZeroConfGetVars()`supported\_capabilitiesNoIntegerBitmasked integer representing list of device capabilities. The `SpZeroConfVars::supported_capabilities` field returned by `SpZeroConfGetVars()`

\[1]**Note** The application is responsible for properly escaping special characters in the strings returned by [SpZeroConfGetVars](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spzeroconfgetvars) before sending them as part of the JSON response. See the [JSON standard](http://www.json.org/) for the requirements.

\[2]**Note** Other Spotify clients may present **brandDisplayName** and the optional **modelDisplayName** to the user in the **Connect** menu and in other places. These strings may contain UTF-8 characters. The limitations of [SpConfig::brand\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) and [SpConfig::model\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) do *not* apply. However, during the certification process, we will verify that the fields are set to reasonable values that do not confuse users and can be displayed correctly by other Spotify clients.

**Example:**

Request:

`1`

`GET http://192.168.10.1:8080/cpath?action=getInfo&version=2.10.0`

Response from device without aliases. The field `"remoteName"` defines the name to be displayed for the device.

`1`

`{`

`2`

`"status": 101,`

`3`

`"statusString": "OK",`

`4`

`"spotifyError": 0,`

`5`

`"responseSource": "Company name",`

`6`

`"version": "2.10.0",`

`7`

`"deviceID": "0007F537F5ED",`

`8`

`"deviceType": "SPEAKER",`

`9`

`"remoteName": "John's \"Super\" Speaker",`

`10`

`"publicKey": "<some-string>",`

`11`

`"brandDisplayName": "Foo Corp™",`

`12`

`"modelDisplayName": "X-2000 Portátil",`

`13`

`"libraryVersion": "master-v2.15.1-g7890abcd",`

`14`

`"resolverVersion": "1",`

`15`

`"groupStatus": "GROUP",`

`16`

`"tokenType": "accesstoken",`

`17`

`"clientID": "<some-other-string>",`

`18`

`"productID": 0,`

`19`

`"scope": "streaming",`

`20`

`"availability": "",`

`21`

`"supported_drm_media_formats": [`

`22`

`{"drm": 0, "formats": 35},`

`23`

`{"drm": 1, "formats": 35},`

`24`

`{"drm": 3, "formats": 1168}`

`25`

`],`

`26`

`"supported_capabilities": 1`

`27`

`}`

Response from a device using device aliases. In this case, the field `remoteName` should be empty in the response as the displayed name for respective alias is defined in the `aliases` field.

`1`

`{`

`2`

`"status": 101,`

`3`

`"statusString": "OK",`

`4`

`"spotifyError": 0,`

`5`

`"responseSource": "Company name",`

`6`

`"version": "2.10.0",`

`7`

`"deviceID": "0007F537F5ED",`

`8`

`"deviceType": "SPEAKER",`

`9`

`"remoteName": "",`

`10`

`"publicKey": "<some-string>",`

`11`

`"brandDisplayName": "Foo Corp™",`

`12`

`"modelDisplayName": "X-2000 Portátil",`

`13`

`"libraryVersion": "master-v2.15.1-g7890abcd",`

`14`

`"resolverVersion": "1",`

`15`

`"groupStatus": "NONE",`

`16`

`"tokenType": "accesstoken",`

`17`

`"clientID": "<some-other-string>",`

`18`

`"productID": 0,`

`19`

`"scope": "streaming",`

`20`

`"availability": "",`

`21`

`"aliases": [`

`22`

`{`

`23`

`"name": "alias-one",`

`24`

`"id": "1",`

`25`

`"isGroup": "true"`

`26`

`},`

`27`

`{`

`28`

`"name": "alias-two",`

`29`

`"id": "2",`

`30`

`"isGroup": "false"`

`31`

`}`

`32`

`],`

`33`

`"supported_drm_media_formats": [`

`34`

`{"drm": 0, "formats": 35},`

`35`

`{"drm": 1, "formats": 35},`

`36`

`{"drm": 3, "formats": 1168}`

`37`

`],`

`38`

`"supported_capabilities": 1`

`39`

`}`

### Reset Users

The currently logged in user (if any) should be logged out using [SpConnectionLogout](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionlogout). All user credentials should be deleted from the device's local storage. Any other persistent data related to ZeroConf should be cleared to factory-reset defaults.

**HTTP method:** POST.

**Extra parameters:** none.

**Return:** only status.

## Device Aliases

Using ZeroConf, it is possible to announce multiple "virtual devices" from a device. This allows the eSDK device to expose, for instance, multiroom zones as ZeroConf devices.

**Note** There is no built-in support for multiroom audio forwarding in the eSDK. This feature enables an integration to announce partner supplied multiroom audio routing configurations directly in the Spotify app.

Device aliases will show up as separate devices in the Spotify app. When a device is selected for playback, you will know which alias from the `device_alias_index` parameter in the [SpCallbackSelectedDeviceAliasChanged](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackselecteddevicealiaschanged) callback.

### Device Aliases using built-in ZeroConf

If the built-in ZeroConf server is used, there is already support for device aliases, up to a maximum of `SP_MAX_DEVICE_ALIASES`. Simply configure the alias names in [SpConfig::device\_aliases](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig),

for example:

`1`

`SpError err;`

`2`

`struct SpConfig config;`

`3`

`4`

`memset(&config, 0, sizeof(config));`

`5`

`6`

`...`

`7`

`config.device_aliases[0].display_name = "My Speaker";`

`8`

`config.device_aliases[1].display_name = "Kitchen + Dining";`

`9`

`config.device_aliases[2].display_name = "Upper floor";`

`10`

`11`

`config.display_name = NULL; // No display name is used because aliases are defined`

`12`

`...`

`13`

`14`

`err = SpInit(&config);`

When using [SpConfig::device\_aliases](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig), [SpConfig::display\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) is not used.

## Appendix

### HTTP Status codes

The following table shows the different responses returned by the HTTP server to a client's request:

Status nameStatusHTTP status code \[1]Status stringResponse toUsageOk101200OKAllSuccessful operationBad102400ERROR-BAD-REQUESTAllWeb server problem or critically malformed requestUnknown103500ERROR-UNKNOWNAllFallback when no other error appliesNotImplemented104501ERROR-NOT-IMPLEMENTEDAllServer does not implement this featureLoginFailed202200ERROR-LOGIN-FAILEDaddUserSpotify returned error when trying to loginMissingAction301400ERROR-MISSING-ACTIONAllWeb request has no action parameterInvalidAction302400ERROR-INVALID-ACTIONAllWeb request has unrecognized action parameterInvalidArguments303400ERROR-INVALID-ARGUMENTSAllIncorrect or insufficient arguments supplied for requested actionSpotifyError402200ERROR-SPOTIFY-ERRORAllA Spotify API call returned an error not covered by other error messages

\[1]**Note** It is permissible to send HTTP status code 200 in all cases, as long as a valid JSON reply is returned that contains the **status**, **statusString**, and **spotifyError** strings.