---
title: API Reference eSDK 3.194.32 | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194
source: crawler
fetched_at: 2026-02-27T23:41:40.735375-03:00
rendered_js: true
word_count: 21108
summary: This document provides a technical index of the Spotify Embedded SDK header file, outlining available macros, data structures, callbacks, and functions for integrating Spotify playback and connectivity into embedded devices.
tags:
    - spotify-embedded-sdk
    - c-api
    - spotify-connect
    - embedded-systems
    - audio-streaming
    - device-integration
category: api
---

## Main

* * *

`1`

`#include "spotify_embedded.h"`

- [Macros and Constants](#main-macros-and-constants)
- [Data Structures](#main-data-structures)
- [Typedefs](#main-typedefs)
- [Enumerations](#main-enumerations)
- [Functions](#main-functions)

## Macros and Constants

* * *

[Return to header index](#main)

[SP\_API\_VERSION](#sp_api_version) 70 [SP\_RECOMMENDED\_MEMORY\_BLOCK\_SIZE](#sp_recommended_memory_block_size) 1024 * 1024 [SP\_MAX\_BRAND\_NAME\_LENGTH](#sp_max_brand_name_length) 32 [SP\_MAX\_MODEL\_NAME\_LENGTH](#sp_max_model_name_length) 30 [SP\_MAX\_CLIENT\_ID\_LENGTH](#sp_max_client_id_length) 32 [SP\_MAX\_OS\_VERSION\_LENGTH](#sp_max_os_version_length) 64 [SP\_MAX\_DISPLAY\_NAME\_LENGTH](#sp_max_display_name_length) 64 [SP\_MAX\_UNIQUE\_ID\_LENGTH](#sp_max_unique_id_length) 64 [SP\_MAX\_USERNAME\_LENGTH](#sp_max_username_length) 64 [SP\_MAX\_DEVICE\_ALIASES](#sp_max_device_aliases) 8 [SP\_NO\_ALIAS\_SELECTED](#sp_no_alias_selected) -1 [SP\_MAX\_METADATA\_NAME\_LENGTH](#sp_max_metadata_name_length) 255 [SP\_MAX\_METADATA\_URI\_LENGTH](#sp_max_metadata_uri_length) 127 [SP\_MAX\_TRACK\_UID\_LENGTH](#sp_max_track_uid_length) 64 [SP\_MAX\_METADATA\_IMAGE\_URL\_LENGTH](#sp_max_metadata_image_url_length) 255 [SP\_PLAYER\_COOKIE\_LENGTH](#sp_player_cookie_length) 32 [SP\_MAX\_PLAYBACK\_ID\_LENGTH](#sp_max_playback_id_length) 32 [SP\_MAX\_PUBLIC\_KEY\_LENGTH](#sp_max_public_key_length) 149 [SP\_MAX\_DEVICE\_ID\_LENGTH](#sp_max_device_id_length) 64 [SP\_MAX\_DEVICE\_TYPE\_LENGTH](#sp_max_device_type_length) 15 [SP\_MAX\_VERSION\_LENGTH](#sp_max_version_length) 30 [SP\_MAX\_GROUP\_STATUS\_LENGTH](#sp_max_group_status_length) 15 [SP\_MAX\_TOKEN\_TYPE\_LENGTH](#sp_max_token_type_length) 30 [SP\_MAX\_SCOPE\_LENGTH](#sp_max_scope_length) 64 [SP\_MAX\_CLIENT\_KEY\_LENGTH](#sp_max_client_key_length) 511 [SP\_MAX\_ZEROCONF\_BLOB\_LENGTH](#sp_max_zeroconf_blob_length) 2047 [SP\_MAX\_LOGIN\_ID\_LENGTH](#sp_max_login_id_length) 64 [SP\_MAX\_AVAILABILITY\_LENGTH](#sp_max_availability_length) 15 [SP\_MAX\_PARTNER\_NAME\_LENGTH](#sp_max_partner_name_length) 48 [SP\_MAX\_FILENAME\_LENGTH](#sp_max_filename_length) 63 [SP\_PRESET\_BUFFER\_SIZE](#sp_preset_buffer_size) 2064 [SP\_ZEROCONF\_DISABLED](#sp_zeroconf_disabled) 0 [SP\_ZEROCONF\_SERVE](#sp_zeroconf_serve) 1 [SP\_ZEROCONF\_SERVE\_HTTP\_ONLY](#sp_zeroconf_serve_http_only) 2 [SP\_ZEROCONF\_SERVE\_MDNS\_ONLY](#sp_zeroconf_serve_mdns_only) 3 [SP\_SCOPE\_STREAMING](#sp_scope_streaming) "streaming" [SP\_DEVICE\_ALIAS\_ATTRIBUTE\_GROUP](#sp_device_alias_attribute_group) 1 [SP\_GLOBAL\_ATTRIBUTE\_VOICE](#sp_global_attribute_voice) 2 [SP\_MAX\_SUPPORTED\_FORMATS](#sp_max_supported_formats) 8 [SP\_PLAYBACK\_RESTRICTION\_ALREADY\_PAUSED](#sp_playback_restriction_already_paused) 1 [SP\_PLAYBACK\_RESTRICTION\_NOT\_PAUSED](#sp_playback_restriction_not_paused) 2 [SP\_PLAYBACK\_RESTRICTION\_LICENSE\_DISALLOW](#sp_playback_restriction_license_disallow) 4 [SP\_PLAYBACK\_RESTRICTION\_AD\_DISALLOW](#sp_playback_restriction_ad_disallow) 8 [SP\_PLAYBACK\_RESTRICTION\_NO\_PREV\_TRACK](#sp_playback_restriction_no_prev_track) 16 [SP\_PLAYBACK\_RESTRICTION\_NO\_NEXT\_TRACK](#sp_playback_restriction_no_next_track) 32 [SP\_PLAYBACK\_RESTRICTION\_UNKNOWN](#sp_playback_restriction_unknown) 64 [SP\_PLAYBACK\_RESTRICTION\_ENDLESS\_CONTEXT](#sp_playback_restriction_endless_context) 128

## Data Structures

* * *

[Return to header index](#main)

[SpPlaybackRestrictions](#spplaybackrestrictions) Playback restrictions.[SpMetadata](#spmetadata) Track metadata.[SpFormat](#spformat) Mapping of which media formats are supported in which DRM.[SpZeroConfDeviceAlias](#spzeroconfdevicealias) ZeroConf DeviceAlias.[SpZeroConfVars](#spzeroconfvars) ZeroConf variables.[SpSampleFormat](#spsampleformat) Sample format of the audio data sent in SpCallbackPlaybackAudioData[SpPlaybackCallbacks](#spplaybackcallbacks) Callbacks to be registered with SpRegisterPlaybackCallbacks[SpDebugCallbacks](#spdebugcallbacks) Callbacks to be registered with SpRegisterDebugCallbacks[SpConnectionCallbacks](#spconnectioncallbacks) Callbacks to be registered with SpRegisterConnectionCallbacks[SpDeviceAlias](#spdevicealias) Device alias definition.[SpConfig](#spconfig) Configuration.[SpDeviceAliasCallbacks](#spdevicealiascallbacks) Callbacks to be registered with SpRegisterDeviceAliasCallbacks

## Typedefs

* * *

[Return to header index](#main)

[SpCallbackError](#spcallbackerror) Callback for reporting errors to the application.[SpCallbackPlaybackNotify](#spcallbackplaybacknotify) Callback for notifying the application about playback-related events.[SpCallbackPlaybackSeek](#spcallbackplaybackseek) Callback to notify the application of a change in the playback position.[SpCallbackPlaybackApplyVolume](#spcallbackplaybackapplyvolume) Callback to notify the application of a volume change using Spotify Connect.[SpCallbackSavePreset](#spcallbacksavepreset) Callback for receiving preset tokens.[SpCallbackConnectionNotify](#spcallbackconnectionnotify) Callback for notifying the application about events related to the connection to Spotify[SpCallbackConnectionNewCredentials](#spcallbackconnectionnewcredentials) Callback for passing a login blob to the application.[SpCallbackConnectionMessage](#spcallbackconnectionmessage) Callback for sending a message to the user.[SpCallbackDebugMessage](#spcallbackdebugmessage) Callback for sending debug messages/trace logs.[SpCallbackSelectedDeviceAliasChanged](#spcallbackselecteddevicealiaschanged) Callback for receiving selected device alias from the backend.[SpCallbackDeviceAliasesUpdateDone](#spcallbackdevicealiasesupdatedone) Callback for knowing when the device alias list has been updated after call to SpSetDeviceAliases

## Enumerations

* * *

[Return to header index](#main)

[SpError](#sperror) [SpAPIReturnCode](#spapireturncode) [SpPlaybackBitrate](#spplaybackbitrate) [SpPlaybackNotification](#spplaybacknotification) [SpConnectionNotification](#spconnectionnotification) [SpDeviceType](#spdevicetype) [SpMetadataTrack](#spmetadatatrack) [SpConnectivity](#spconnectivity) [SpContent](#spcontent) [SpMediaType](#spmediatype) [SpAudioQuality](#spaudioquality) [SpDrmFormat](#spdrmformat) [SpReDeliveryMode](#spredeliverymode)

## Functions

* * *

[Return to header index](#main)

[SpInit](#spinit) Initialize the library.[SpFree](#spfree) Shut down the library.[SpGetLibraryVersion](#spgetlibraryversion) Retrieve a version string for the library.[SpConnectionSetConnectivity](#spconnectionsetconnectivity) Set the type of network connection of the device.[SpConnectionGetConnectivity](#spconnectiongetconnectivity) Get the connectivity that was set with SpConnectionSetConnectivity[SpConnectionLoginBlob](#spconnectionloginblob) Log in a user to Spotify using a credentials blob.[SpConnectionLoginPassword](#spconnectionloginpassword) Log in a user to Spotify using a password.[SpConnectionLoginOauthToken](#spconnectionloginoauthtoken) Log in a user to Spotify using a Spotify OAuth token.[SpConnectionLogout](#spconnectionlogout) Log the user out of Spotify[SpConnectionIsLoggedIn](#spconnectionisloggedin) Is the user logged in to Spotify[SpConnectionGetAckId](#spconnectiongetackid) Get last Ack ID.[SpGetCanonicalUsername](#spgetcanonicalusername) Get the canonical username of the logged in user.[SpSetDisplayName](#spsetdisplayname) Set the display name for the application/device.[SpSetVolumeSteps](#spsetvolumesteps) Set the volume steps the device is capable of.[SpSetDeviceIsGroup](#spsetdeviceisgroup) Control if the device represents a group.[SpEnableConnect](#spenableconnect) Enable Connect functionality for this device.[SpDisableConnect](#spdisableconnect) Disable Connect functionality for this device.[SpGetSelectedDeviceAlias](#spgetselecteddevicealias) Return the currently selected device alias.[SpPumpEvents](#sppumpevents) Allow the library to perform asynchronous tasks and process events.[SpRegisterConnectionCallbacks](#spregisterconnectioncallbacks) Register callbacks related to the connection to Spotify[SpRegisterDebugCallbacks](#spregisterdebugcallbacks) Register a callback that receives debug messages/trace logs.[SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks) Register playback-related callbacks.[SpGetMetadata](#spgetmetadata) Retrieve metadata for a track in the current track list.[SpGetMetadataImageURL](#spgetmetadataimageurl) Return the HTTP URL to an image file from a spotify:image: URI.[SpGetPlayerCookie](#spgetplayercookie) Obtain player cookie for current playback.[SpPlaybackPlay](#spplaybackplay) Start or resume playback.[SpPlaybackPause](#spplaybackpause) Pause playback.[SpPlaybackSkipToNext](#spplaybackskiptonext) Skip playback to the next track in the track list.[SpPlaybackSkipToPrev](#spplaybackskiptoprev) Skip playback to the previous track in the track list.[SpPlaybackSeek](#spplaybackseek) Seek to a position within the current track.[SpPlaybackSeekRelative](#spplaybackseekrelative) Seek a relative amount of time within the current track.[SpPlaybackGetPosition](#spplaybackgetposition) Get the current playback position within the track.[SpPlaybackUpdateVolume](#spplaybackupdatevolume) Request a change to the playback volume.[SpPlaybackGetVolume](#spplaybackgetvolume) Get the playback volume level.[SpPlaybackIsPlaying](#spplaybackisplaying) Is the playback status playing or paused.[SpPlaybackIsAdPlaying](#spplaybackisadplaying) Is the the current track an Ad or not.[SpPlaybackIsShuffled](#spplaybackisshuffled) Is "shuffle" mode enabled.[SpPlaybackIsRepeated](#spplaybackisrepeated) Is "repeat" mode enabled.[SpPlaybackGetRepeatMode](#spplaybackgetrepeatmode) What "repeat" mode is on.[SpPlaybackIsActiveDevice](#spplaybackisactivedevice) Is the device the active playback device.[SpPlaybackEnableShuffle](#spplaybackenableshuffle) Enable or disable "shuffle" mode.[SpPlaybackEnableRepeat](#spplaybackenablerepeat) Enable or disable "repeat" mode.[SpPlaybackCycleRepeatMode](#spplaybackcyclerepeatmode) Cycle through the available repeat modes.[SpPlaybackSetBitrate](#spplaybacksetbitrate) Change the bitrate at which compressed audio data is delivered.[SpPlaybackSetAvailableToPlay](#spplaybacksetavailabletoplay) Allow or disallow the device to start playback.[SpPlaybackIsAvailableToPlay](#spplaybackisavailabletoplay) Is the device available for playback.[SpPlaybackSetDeviceInactive](#spplaybacksetdeviceinactive) Set the device inactive.[SpPlaybackIsDeviceControllable](#spplaybackisdevicecontrollable) Is the device controllable.[SpPlaybackSetDeviceControllable](#spplaybacksetdevicecontrollable) Allow or disallow the device to be controllable.[SpPlaybackIncreaseUnderrunCount](#spplaybackincreaseunderruncount) Increase the underrun counter of the current track.[SpPlaybackSetBandwidthLimit](#spplaybacksetbandwidthlimit) Set a limit on the download speed.[SpPlaybackSetRedeliveryMode](#spplaybacksetredeliverymode) Activates redelivery of audio data on play or resume playback.[SpPlaybackIsRedeliveryModeActivated](#spplaybackisredeliverymodeactivated) Gets the status of redelivery mode.[SpPresetSubscribe](#sppresetsubscribe) Subscribe to receive "preset" tokens for use with SpPlayPreset[SpPresetUnsubscribe](#sppresetunsubscribe) Unsubscribe from a previously subscribed preset.[SpPlayPreset](#spplaypreset) Recall and play a saved or default preset.[SpZeroConfGetVars](#spzeroconfgetvars) Get variables for ZeroConf, mainly the "getInfo" request.[SpZeroConfAnnouncePause](#spzeroconfannouncepause) Temporarily pause ZeroConf mDNS annoucements.[SpZeroConfAnnounceResume](#spzeroconfannounceresume) Resume ZeroConf mDNS annoucement after calling SpZeroConfAnnouncePause[SpConnectionLoginZeroConf](#spconnectionloginzeroconf) Log in a user to Spotify using a ZeroConf credentials blob.[SpGetBrandName](#spgetbrandname) [SpGetModelName](#spgetmodelname) [SpRegisterDeviceAliasCallbacks](#spregisterdevicealiascallbacks) Register callbacks related to device aliases.[SpSetDeviceAliases](#spsetdevicealiases) Update the device alias definitions.[SpRestrictDrmMediaFormats](#sprestrictdrmmediaformats) [SpRestoreDrmMediaFormats](#sprestoredrmmediaformats)

## Macros and Constants

* * *

### SP\_API\_VERSION

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_API_VERSION 70`

The version of the API defined in this header file.

**See also**

- [SpInit](#spinit)

### SP\_RECOMMENDED\_MEMORY\_BLOCK\_SIZE

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_RECOMMENDED_MEMORY_BLOCK_SIZE 1024 * 1024`

Minimum recommended size of the buffer [SpConfig::memory\_block](#spconfig)

### SP\_MAX\_BRAND\_NAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_BRAND_NAME_LENGTH 32`

Maximum length of the brand name string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_MODEL\_NAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_MODEL_NAME_LENGTH 30`

Maximum length of the model name string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_CLIENT\_ID\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_CLIENT_ID_LENGTH 32`

Maximum length of the client id string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_OS\_VERSION\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_OS_VERSION_LENGTH 64`

Maximum length of the os version string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_DISPLAY\_NAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_DISPLAY_NAME_LENGTH 64`

Maximum length of the device display name (not counting terminating NULL)

**See also**

- [SpSetDisplayName](#spsetdisplayname)
- [SpConfig](#spconfig)
- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_UNIQUE\_ID\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_UNIQUE_ID_LENGTH 64`

Maximum length of the device's unique ID (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_USERNAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_USERNAME_LENGTH 64`

Maximum length of usernames (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)
- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_DEVICE\_ALIASES

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_DEVICE_ALIASES 8`

Maximum number of device aliases that can be configured.

**See also**

- [SpConfig](#spconfig)

### SP\_NO\_ALIAS\_SELECTED

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_NO_ALIAS_SELECTED -1`

A value to use for alias\_index when aliases are not used.

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_METADATA\_NAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_METADATA_NAME_LENGTH 255`

Maximum length of display names in track metadata (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

**Notes:**

- It is possible that metadata will be truncted to less than this length. Applications requiring full length metadata should request it from the Spotify web APIs [https://developer.spotify.com/documentation/web-api/](https://developer.spotify.com/documentation/web-api/)

### SP\_MAX\_METADATA\_URI\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_METADATA_URI_LENGTH 127`

Maximum length of URIs in track metadata (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

### SP\_MAX\_TRACK\_UID\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_TRACK_UID_LENGTH 64`

Maximum length of Track UID in track metadata (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

### SP\_MAX\_METADATA\_IMAGE\_URL\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_METADATA_IMAGE_URL_LENGTH 255`

Maximum length of URLs (not counting terminating NULL)

**See also**

- [SpGetMetadataImageURL](#spgetmetadataimageurl)

### SP\_PLAYER\_COOKIE\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYER_COOKIE_LENGTH 32`

Length of player cookie (not including terminating null)

**See also**

- [SpGetPlayerCookie](#spgetplayercookie)

### SP\_MAX\_PLAYBACK\_ID\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_PLAYBACK_ID_LENGTH 32`

Maximum length of Playback-Id (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

### SP\_MAX\_PUBLIC\_KEY\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_PUBLIC_KEY_LENGTH 149`

Maximum length of the public key used in ZeroConf logins (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_DEVICE\_ID\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_DEVICE_ID_LENGTH 64`

Maximum length of the device ID used for ZeroConf logins (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_DEVICE\_TYPE\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_DEVICE_TYPE_LENGTH 15`

Maximum length of the device type string (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_VERSION\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_VERSION_LENGTH 30`

Maximum length of the library version string (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_GROUP\_STATUS\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_GROUP_STATUS_LENGTH 15`

Maximum length of the group status string (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_TOKEN\_TYPE\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_TOKEN_TYPE_LENGTH 30`

Maximum length of the token type used for OAuth logins (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_SCOPE\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_SCOPE_LENGTH 64`

Maximum length of the scope used for OAuth login (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_CLIENT\_KEY\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_CLIENT_KEY_LENGTH 511`

Maximum length of the client key. (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_ZEROCONF\_BLOB\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_ZEROCONF_BLOB_LENGTH 2047`

Maximum length of the zeroconf blob. (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_LOGIN\_ID\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_LOGIN_ID_LENGTH 64`

Maximum length of the login ID used for ZeroConf logins (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_AVAILABILITY\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_AVAILABILITY_LENGTH 15`

Maximum length of the availability string (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_PARTNER\_NAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_PARTNER_NAME_LENGTH 48`

Maximum length of the Partner Name (TSP\_PARTNER\_NAME) (not counting terminating NULL) The longest partner name when this was written was "imagination\_technologies\_mips" at 29 characters.

### SP\_MAX\_FILENAME\_LENGTH

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_FILENAME_LENGTH 63`

Maximum length of filename fields (not counting terminating NULL)

### SP\_PRESET\_BUFFER\_SIZE

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PRESET_BUFFER_SIZE 2064`

Maximum length of the preset blob returned by SpGetPreset

### SP\_ZEROCONF\_DISABLED

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_ZEROCONF_DISABLED 0`

Value for [SpConfig::zeroconf\_serve](#spconfig) when disabling builtin ZeroConf stack. Complete ZeroConf stack must be run externally.

**See also**

- [SpInit](#spinit)

### SP\_ZEROCONF\_SERVE

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_ZEROCONF_SERVE 1`

Value for [SpConfig::zeroconf\_serve](#spconfig) when activating complete builtin ZeroConf stack.

**See also**

- [SpInit](#spinit)

### SP\_ZEROCONF\_SERVE\_HTTP\_ONLY

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_ZEROCONF_SERVE_HTTP_ONLY 2`

Value for [SpConfig::zeroconf\_serve](#spconfig) when activating builtin ZeroConf http server only while running the ZeroConf mDNS server externally.

**See also**

- [SpInit](#spinit)

### SP\_ZEROCONF\_SERVE\_MDNS\_ONLY

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_ZEROCONF_SERVE_MDNS_ONLY 3`

Value for [SpConfig::zeroconf\_serve](#spconfig) when activating builtin ZeroConf mDNS server only while running the ZeroConf http server externally.

**See also**

- [SpInit](#spinit)

### SP\_SCOPE\_STREAMING

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_SCOPE_STREAMING "streaming"`

Value for [SpConfig::scope](#spconfig) when implementing a basic streaming device.

### SP\_DEVICE\_ALIAS\_ATTRIBUTE\_GROUP

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_DEVICE_ALIAS_ATTRIBUTE_GROUP 1`

Set this bit in the device alias attributes integer (SpDeviceAlias::attributes) to mark a device alias as representing a group.

**Notes:**

- [SpSetDeviceIsGroup](#spsetdeviceisgroup) also sets group status, but only for the currently selected alias.

### SP\_GLOBAL\_ATTRIBUTE\_VOICE

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_GLOBAL_ATTRIBUTE_VOICE 2`

Set this bit in the global attributes integer (SpConfig::global\_attributes) to mark that this device supports voice.

### SP\_MAX\_SUPPORTED\_FORMATS

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_MAX_SUPPORTED_FORMATS 8`

**See also**

- [SpFormat](#spformat)
- [SpConfig::supported\_drm\_media\_formats](#spconfig)

### SP\_PLAYBACK\_RESTRICTION\_ALREADY\_PAUSED

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_ALREADY_PAUSED 1`

The track is already paused.

### SP\_PLAYBACK\_RESTRICTION\_NOT\_PAUSED

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_NOT_PAUSED 2`

The track is already playing.

### SP\_PLAYBACK\_RESTRICTION\_LICENSE\_DISALLOW

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_LICENSE_DISALLOW 4`

Licensing rules disallow this action.

### SP\_PLAYBACK\_RESTRICTION\_AD\_DISALLOW

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_AD_DISALLOW 8`

Action can't be performed while an ad is playing.

### SP\_PLAYBACK\_RESTRICTION\_NO\_PREV\_TRACK

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_NO_PREV_TRACK 16`

There is no track before the current one in the currently playing context.

### SP\_PLAYBACK\_RESTRICTION\_NO\_NEXT\_TRACK

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_NO_NEXT_TRACK 32`

There is no track after the current one in the currently playing context.

### SP\_PLAYBACK\_RESTRICTION\_UNKNOWN

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_UNKNOWN 64`

The action is restricted, but no reason is provided This means that eSDK has not retrieved the restrictions from the backend yet and therefore the action is not allowed right now. As soon as eSDK retrieves the information, the notification [kSpPlaybackNotifyMetadataChanged](#spplaybacknotification) will be sent, and the application can check the field again.

### SP\_PLAYBACK\_RESTRICTION\_ENDLESS\_CONTEXT

[Return to Main macros and constants](#main-macros-and-constants)

`1`

`#define SP_PLAYBACK_RESTRICTION_ENDLESS_CONTEXT 128`

The action is restricted for context level reasons.

## Data Structures

* * *

### SpPlaybackRestrictions

[Return to Main data structures](#main-data-structures)

Playback restrictions.

`1`

`struct SpPlaybackRestrictions {`

`2`

`uint32_t disallow_pausing_reasons;`

`3`

`uint32_t disallow_resuming_reasons;`

`4`

`uint32_t disallow_seeking_reasons;`

`5`

`uint32_t disallow_peeking_prev_reasons;`

`6`

`uint32_t disallow_peeking_next_reasons;`

`7`

`uint32_t disallow_skipping_prev_reasons;`

`8`

`uint32_t disallow_skipping_next_reasons;`

`9`

`uint32_t disallow_toggling_repeat_context_reasons;`

`10`

`uint32_t disallow_toggling_repeat_track_reasons;`

`11`

`uint32_t disallow_toggling_shuffle_reasons;`

`12`

`};`

*uint32\_t* disallow\_pausing\_reasonsBitfield of reasons the pause action is unavailable.*uint32\_t* disallow\_resuming\_reasonsBitfield of reasons the resume action is unavailable.*uint32\_t* disallow\_seeking\_reasonsBitfield of reasons seeking is unavailable.*uint32\_t* disallow\_peeking\_prev\_reasonsBitfield of reasons peeking on the previous track is unavailable.*uint32\_t* disallow\_peeking\_next\_reasonsBitfield of reasons peeking on the next track is unavailable.*uint32\_t* disallow\_skipping\_prev\_reasonsBitfield of reasons skipping to the previous track is unavailable.*uint32\_t* disallow\_skipping\_next\_reasonsBitfield of reasons skipping to the next track is unavailable.*uint32\_t* disallow\_toggling\_repeat\_context\_reasonsBitfield of reasons setting repeat context is not allowed.*uint32\_t* disallow\_toggling\_repeat\_track\_reasonsBitfield of reasons setting repeat track is not allowed.*uint32\_t* disallow\_toggling\_shuffle\_reasonsBitfield of reasons toggling shuffle is not allowed.

### SpMetadata

[Return to Main data structures](#main-data-structures)

Track metadata.

**See also**

- [SpGetMetadata](#spgetmetadata)

`1`

`struct SpMetadata {`

`2`

`char playback_source;`

`3`

`char playback_source_uri;`

`4`

`char track;`

`5`

`char track_uri;`

`6`

`char artist;`

`7`

`char artist_uri;`

`8`

`char album;`

`9`

`char album_uri;`

`10`

`char album_cover_uri;`

`11`

`char original_track_uri;`

`12`

`uint32_t duration_ms;`

`13`

`int32_t index;`

`14`

`char track_uid;`

`15`

`uint32_t original_index;`

`16`

`uint32_t bitrate;`

`17`

`struct SpPlaybackRestrictions playback_restrictions;`

`18`

`char playback_id;`

`19`

`enum SpContent content_type;`

`20`

`enum SpMediaType media_type;`

`21`

`enum SpAudioQuality audio_quality;`

`22`

`};`

*char* playback\_sourceDisplay name of the playback source. E.g., the name of the playlist from which playback was initiated (UTF-8-encoded)*char* playback\_source\_uriSpotify URI of the playback source (in the form "spotify:xxxxxx:xxxxxxx...")*char* trackDisplay name of the track (UTF-8-encoded)*char* track\_uriSpotify URI of the track (in the form "spotify:track:xxxxxxx...")*char* artistDisplay name of the artist of the track (UTF-8-encoded)*char* artist\_uriSpotify URI of the artist of the track (in the form "spotify:artist:xxxxxxx...")*char* albumDisplay name of the track's album (UTF-8-encoded)*char* album\_uriSpotify URI of the track's album (in the form "spotify:album:xxxxxxx...")*char* album\_cover\_uriSpotify URI of the album's cover art image (in the form "spotify:image:xxxxxxx...")*char* original\_track\_uriSpotify URI of the original track before relinking (in the form "spotify:track:xxxxxxx...")*uint32\_t* duration\_msPlayback duration of the track in milliseconds.*int32\_t* indexIndex of the track in the currently playing context.*char* track\_uidTrack UID of the track in the currently playing context.*uint32\_t* original\_indexIndex of the track in the original (unchanged) playing context.*uint32\_t* bitrateThe bitrate of the track in kbps. 0 means "unplayable".*struct* [SpPlaybackRestrictions](#spplaybackrestrictions) playback\_restrictionsRestrictions that apply to playback and transitions related to this track.*char* playback\_idPlayback-id of this playback of this specific track.*enum* [SpContent](#spcontent) content\_typeContent type of this track.*enum* [SpMediaType](#spmediatype) media\_typeMedia type of this track.*enum* [SpAudioQuality](#spaudioquality) audio\_qualityAudio quality of this track.

### SpFormat

[Return to Main data structures](#main-data-structures)

Mapping of which media formats are supported in which DRM.

**See also**

- [SpConfig](#spconfig)

`1`

`struct SpFormat {`

`2`

`enum SpDrmFormat drm;`

`3`

`uint64_t media;`

`4`

`};`

*enum* [SpDrmFormat](#spdrmformat) drmDRM format which the integration supports.uint64\_t mediaSupported media formats for a DRM.

### SpZeroConfDeviceAlias

[Return to Main data structures](#main-data-structures)

ZeroConf DeviceAlias.

This structure contains information about a single device alias, as returned by [SpZeroConfGetVars](#spzeroconfgetvars)

**See also**

- [SpZeroConfGetVars](#spzeroconfgetvars)

`1`

`struct SpZeroConfDeviceAlias {`

`2`

`uint32_t id;`

`3`

`int is_group;`

`4`

`char display_name;`

`5`

`};`

*uint32\_t* idString to be sent in the "id" field of the alias in the "getInfo" response.*int* is\_groupBoolean (0 = "false", 1 = "true") to be sent in the "isGroup" field of the alias in the "getInfo" response.*char* display\_nameString to be sent in the "name" field of the alias in the "getInfo" response.

### SpZeroConfVars

[Return to Main data structures](#main-data-structures)

ZeroConf variables.

This structure contains the fields that the application needs for ZeroConf, mainly what to send in the response to the "getInfo" request. See the ZeroConf manual for more information.

**See also**

- [SpZeroConfGetVars](#spzeroconfgetvars)

`1`

`struct SpZeroConfVars {`

`2`

`char public_key;`

`3`

`char device_id;`

`4`

`char remote_name;`

`5`

`char device_type;`

`6`

`char library_version;`

`7`

`int resolver_version;`

`8`

`char group_status;`

`9`

`int webserver_current_port;`

`10`

`char token_type;`

`11`

`char client_id;`

`12`

`char scope;`

`13`

`char availability;`

`14`

`uint32_t product_id;`

`15`

`struct SpZeroConfDeviceAlias aliases;`

`16`

`uint32_t alias_count;`

`17`

`struct SpFormat supported_drm_media_formats;`

`18`

`uint64_t supported_capabilities;`

`19`

`};`

*char* public\_keyString to be sent in the "publicKey" field of the "getInfo" response\[\*].*char* device\_idString to be sent in the "deviceID" field of the "getInfo" response\[\*].*char* remote\_nameString to be sent in the "remoteName" field of the "getInfo" response\[\*].*char* device\_typeString to be sent in the "deviceType" field of the "getInfo" response\[\*].*char* library\_versionString to be sent in the "libraryVersion" field of the "getInfo" response\[\*].*int* resolver\_versionInteger to be sent as string in the "resolverVersion" field of the "getInfo" response\[\*].*char* group\_statusString to be sent in the "groupStatus" field of the "getInfo" response\[\*].*int* webserver\_current\_portCurrent internal ZeroConf webserver port number. To be used when running an external mDNS server together with an internal webserver.*char* token\_typeString to be sent in the "tokenType" field of the "getInfo" response\[\*].*char* client\_idString to be sent in the "clientID" field of the "getInfo" response\[\*].*char* scopeString to be sent in the "scope" field of the "getInfo" response\[\*].*char* availabilityString to be sent in the "availability" field of the "getInfo" response\[\*].*uint32\_t* product\_idInteger to be sent in the "productID" field of the "getInfo" response\[\*].*struct* [SpZeroConfDeviceAlias](#spzeroconfdevicealias) aliasesArray of SpZeroConfDeviceAlias to be sent in the "aliases" field of the "getInfo" response\[\*].*uint32\_t* alias\_countNumber of valid items in aliases array.*struct* [SpFormat](#spformat) supported\_drm\_media\_formatsArray of SpFormat to be sent in the "supported\_drm\_media\_formats" field of the "getInfo" response\[\*].uint64\_t supported\_capabilitiesInteger representing a bitmask to be sent in the "supported\_capabilities" field of the "getInfo" response\[\*].

### SpSampleFormat

[Return to Main data structures](#main-data-structures)

Sample format of the audio data sent in SpCallbackPlaybackAudioData

**Notes:**

- The contents of this should be ignored when SpCallbackPlaybackAudioData is invoked with sample\_count = 0.

`1`

`struct SpSampleFormat {`

`2`

`int channels;`

`3`

`int sample_rate;`

`4`

`int replay_gain_mdb;`

`5`

`};`

*int* channelsNumber of channels (1 = mono, 2 = stereo)*int* sample\_rateSample rate in Hz (such as 22050, 44100 or 48000)*int* replay\_gain\_mdbIf audio playback is normalized, this value is the suggested replay gain adjustment in milli-dBs (1000 = +1 dB, -1000 = -1 dB, 0 = no change)

### SpPlaybackCallbacks

[Return to Main data structures](#main-data-structures)

Callbacks to be registered with [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpPlaybackCallbacks {`

`2`

`SpCallbackPlaybackNotify on_notify;`

`3`

`SpCallbackPlaybackSeek on_seek;`

`4`

`SpCallbackPlaybackApplyVolume on_apply_volume;`

`5`

`SpCallbackSavePreset on_save_preset;`

`6`

`};`

[SpCallbackPlaybackNotify](#spcallbackplaybacknotify) on\_notifyNotification callback.[SpCallbackPlaybackSeek](#spcallbackplaybackseek) on\_seekSeek position callback.[SpCallbackPlaybackApplyVolume](#spcallbackplaybackapplyvolume) on\_apply\_volumeApply volume callback.[SpCallbackSavePreset](#spcallbacksavepreset) on\_save\_presetPreset token callback.

### SpDebugCallbacks

[Return to Main data structures](#main-data-structures)

Callbacks to be registered with [SpRegisterDebugCallbacks](#spregisterdebugcallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpDebugCallbacks {`

`2`

`SpCallbackDebugMessage on_message;`

`3`

`};`

[SpCallbackDebugMessage](#spcallbackdebugmessage) on\_messageDebug message callback.

### SpConnectionCallbacks

[Return to Main data structures](#main-data-structures)

Callbacks to be registered with [SpRegisterConnectionCallbacks](#spregisterconnectioncallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpConnectionCallbacks {`

`2`

`SpCallbackConnectionNotify on_notify;`

`3`

`SpCallbackConnectionNewCredentials on_new_credentials;`

`4`

`SpCallbackConnectionMessage on_message;`

`5`

`};`

[SpCallbackConnectionNotify](#spcallbackconnectionnotify) on\_notifyNotification callback.[SpCallbackConnectionNewCredentials](#spcallbackconnectionnewcredentials) on\_new\_credentialsCredentials blob callback.[SpCallbackConnectionMessage](#spcallbackconnectionmessage) on\_messageConnection message callback.

### SpDeviceAlias

[Return to Main data structures](#main-data-structures)

Device alias definition.

This *struct* is used to define (optional) device aliases. It's a part of the [SpConfig](#spconfig) *struct* which will be passed to [SpInit](#spinit) to initialize the eSDK.

`1`

`struct SpDeviceAlias {`

`2`

`const char *display_name;`

`3`

`uint32_t attributes;`

`4`

`};`

*const* *char* * display\_nameA UTF-8 encoded display name for an alias of the application/device.*uint32\_t* attributesAttributes for this device alias.

### SpConfig

[Return to Main data structures](#main-data-structures)

Configuration.

**See also**

- [SpInit](#spinit)

`1`

`struct SpConfig {`

`2`

`int api_version;`

`3`

`void *memory_block;`

`4`

`uint32_t memory_block_size;`

`5`

`const char *unique_id;`

`6`

`const char *display_name;`

`7`

`uint32_t global_attributes;`

`8`

`struct SpDeviceAlias device_aliases;`

`9`

`const char *brand_name;`

`10`

`const char *brand_display_name;`

`11`

`const char *model_name;`

`12`

`const char *model_display_name;`

`13`

`const char *client_id;`

`14`

`uint32_t product_id;`

`15`

`const char *scope;`

`16`

`const char *os_version;`

`17`

`enum SpDeviceType device_type;`

`18`

`enum SpPlaybackBitrate max_bitrate;`

`19`

`SpCallbackError error_callback;`

`20`

`void *error_callback_context;`

`21`

`int zeroconf_serve;`

`22`

`const char *host_name;`

`23`

`int zeroconf_port;`

`24`

`int zeroconf_port_range;`

`25`

`struct SpFormat supported_drm_media_formats;`

`26`

`};`

*int* api\_versionThe version of the API contained in this header file. Must be set to SP\_API\_VERSION.*void* * memory\_blockPointer to a memory block to be used by the library.*uint32\_t* memory\_block\_sizeSize of the memory\_block buffer in bytes.*const* *char* * unique\_idA NULL-terminated character string that uniquely identifies the device (such as a MAC address)*const* *char* * display\_nameA UTF-8-encoded display name for the application/device.*uint32\_t* global\_attributesThe global attributes is a bitfield where each attribute is OR:ed together and stored in this integer.*struct* [SpDeviceAlias](#spdevicealias) device\_aliasesDevice alias definitions. These are optional, if you don't want to define aliases this array must be zeroed.*const* *char* * brand\_nameA NULL-terminated string containing the brand name of the hardware device (for hardware integrations)*const* *char* * brand\_display\_nameA UTF-8-encoded brand name of the hardware device (for hardware integrations). Should be very similar to brand\_name.*const* *char* * model\_nameA NULL-terminated string containing the model name of the hardware device (for hardware integrations)*const* *char* * model\_display\_nameA UTF-8-encoded model name of the hardware device (for hardware integrations)*const* *char* * client\_idA NULL-terminated string containing the client id of the application.*uint32\_t* product\_idAn integer enumerating the product for this partner.*const* *char* * scopeA NULL-terminated string containing the OAuth scope requested when authenticating with the Spotify backend.*const* *char* * os\_versionA NULL-terminated string containing the os version running on the hardware.*enum* [SpDeviceType](#spdevicetype) device\_typeThe device type that best describes this product.*enum* [SpPlaybackBitrate](#spplaybackbitrate) max\_bitrateThe maximum bitrate to use for playback.[SpCallbackError](#spcallbackerror) error\_callbackPointer to a callback function that will receive error notifications.*void* * error\_callback\_contextApplication-defined pointer that will be passed unchanged as the context argument to the error\_callback callback.*int* zeroconf\_serveNot applicable in this eSDK configuration.*const* *char* * host\_nameNot applicable in this eSDK configuration.*int* zeroconf\_portNot applicable in this eSDK configuration.*int* zeroconf\_port\_rangeNot applicable in this eSDK configuration.*struct* [SpFormat](#spformat) supported\_drm\_media\_formats

### SpDeviceAliasCallbacks

[Return to Main data structures](#main-data-structures)

Callbacks to be registered with [SpRegisterDeviceAliasCallbacks](#spregisterdevicealiascallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpDeviceAliasCallbacks {`

`2`

`SpCallbackSelectedDeviceAliasChanged on_selected_device_alias_changed;`

`3`

`SpCallbackDeviceAliasesUpdateDone on_device_aliases_update_done;`

`4`

`};`

[SpCallbackSelectedDeviceAliasChanged](#spcallbackselecteddevicealiaschanged) on\_selected\_device\_alias\_changedSelected device alias updated callback.[SpCallbackDeviceAliasesUpdateDone](#spcallbackdevicealiasesupdatedone) on\_device\_aliases\_update\_doneDevice alias list updated.

## Typedefs

* * *

### SpCallbackError()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackError)(SpError error, void *context)`

Callback for reporting errors to the application.

To register this callback, set the field [SpConfig::error\_callback](#spconfig) when invoking the function [SpInit](#spinit)

**Parameters**

\[in][SpError](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sperror) errorError code\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackPlaybackNotify()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackPlaybackNotify)(enum SpPlaybackNotification event, void *context)`

Callback for notifying the application about playback-related events.

To register this callback, use the function [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks)

**Parameters**

\[in]`enum` [SpPlaybackNotification](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spplaybacknotification) eventType of event\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackPlaybackSeek()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackPlaybackSeek)(uint32_t position_ms, void *context)`

Callback to notify the application of a change in the playback position.

To register this callback, use the function [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks) This callback is invoked when [SpPlaybackSeek](#spplaybackseek) is invoked or when the user seeks to a position within the track using Spotify Connect.

**Parameters**

\[in]`uint32_t` position\_msNew position within the track in milliseconds\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackPlaybackApplyVolume()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackPlaybackApplyVolume)(uint16_t volume, uint8_t remote, void *context)`

Callback to notify the application of a volume change using Spotify Connect.

To register this callback, use the function [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks) This callback is invoked in two cases: When the user changes the playback volume using Spotify Connect. When the application invoked [SpPlaybackUpdateVolume](#spplaybackupdatevolume) In both cases, the application is responsible for applying the new volume to its audio output. The application should never invoke [SpPlaybackUpdateVolume](#spplaybackupdatevolume) from this callback, as this might result in an endless loop.

**Parameters**

\[in]uint16\_t volumeVolume in the range 0 (silence) to 65535 (max volume)\[in]uint8\_t remoteSet to 1 if the volume was changed using Spotify Connect, 0 otherwise\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackSavePreset()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef uint8_t(* SpCallbackSavePreset)(int preset_id, uint32_t playback_position, const uint8_t *buffer, size_t buff_size, SpError error, void *context)`

Callback for receiving preset tokens.

To register this callback, use the function [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks) After subscribing to receive preset tokens for the currently playing context, this callback will be called periodically with an updated token that can be used to restore playback at a later time with [SpPlayPreset](#spplaypreset) This token must be saved to persistent storage, and must replace any previous token for the same preset. The rate at which this callback is called may vary based on the type of context playing. It will typically be called once per playing track, but may be called more or less often to satisfy the requirements of the expected Spotify user experience.

**Parameters**

\[in]`int` preset\_idThe value specified to [SpPresetSubscribe](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sppresetsubscribe)\[in]`uint32_t` playback\_positionCurrent playback time in milliseconds. This must be saved persistently with the preset token, and specified when calling [SpPlayPreset](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spplaypreset)\[in]`const` uint8\_t * bufferThe buffer provided to [SpPresetSubscribe](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sppresetsubscribe) filled with the binary preset token to save. This may be NULL if an error has occurred.\[in]size\_t buff\_sizeThe number of binary bytes in buffer to save.\[in][SpError](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sperror) errorAn error code if a problem occurred, or [kSpErrorOk](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sperror)\[in]`void` * contextThe context provided when the callback was registered.

**See also**

- [SpPresetSubscribe](#sppresetsubscribe)
- [SpPresetUnsubscribe](#sppresetunsubscribe)

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackConnectionNotify()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackConnectionNotify)(enum SpConnectionNotification event, void *context)`

Callback for notifying the application about events related to the connection to Spotify

To register this callback, use the function [SpRegisterConnectionCallbacks](#spregisterconnectioncallbacks)

**Parameters**

\[in]`enum` [SpConnectionNotification](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spconnectionnotification) eventType of event\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackConnectionNewCredentials()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackConnectionNewCredentials)(const char *credentials_blob, const char *username, void *context)`

Callback for passing a login blob to the application.

To register this callback, use the function [SpRegisterConnectionCallbacks](#spregisterconnectioncallbacks) The application may save the credentials\_blob for subsequent logins using the function [SpConnectionLoginBlob](#spconnectionloginblob) The application should also discard any credentials blobs for this user that it received previously, either through this callback or through ZeroConf (see the ZeroConf manual). Note: If credentials\_blob is an empty string, the application MUST delete any existing saved credentials for the account, and must not attempt to login again with the empty credentials. This happens when a permanent logout is requested.

**Parameters**

\[in]`const` `char` * credentials\_blobCredentials to be passed to [SpConnectionLoginBlob](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spconnectionloginblob)\[in]`const` `char` * usernameuser name to be passed to [SpConnectionLoginBlob](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spconnectionloginblob)\[in]`void` * contextContext pointer that was passed when registering the callback

**See also**

- [SpConnectionLoginBlob](#spconnectionloginblob)

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackConnectionMessage()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackConnectionMessage)(const char *message, void *context)`

Callback for sending a message to the user.

To register this callback, use the function [SpRegisterConnectionCallbacks](#spregisterconnectioncallbacks) This callback is invoked when Spotify wants to display a message to the user. The message is meant to be displayed to the user as is and should not be interpreted by the application (the format of the messages may change without notice). If the application does not have a graphical user interface, it can safely ignore this callback.

**Parameters**

\[in]`const` `char` * messageMessage to be displayed to the user.\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackDebugMessage()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackDebugMessage)(const char *debug_message, void *context)`

Callback for sending debug messages/trace logs.

To register this callback, use the function [SpRegisterDebugCallbacks](#spregisterdebugcallbacks) In special builds of the library, this callback receives debug messages that the application may write to its logs. The application should not interpret the messages (the format of the messages may change without notice).

**Parameters**

\[in]`const` `char` * debug\_messageMessage to be logged\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackSelectedDeviceAliasChanged()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackSelectedDeviceAliasChanged)(uint32_t alias_index, void *context)`

Callback for receiving selected device alias from the backend.

To register this callback, use the function [SpRegisterDeviceAliasCallbacks](#spregisterdevicealiascallbacks) This callback is invoked whenever the selected device alias is updated. This can happen when, for example, the user selects an alias from Spotify Connect device picker.

**Parameters**

\[in]`uint32_t` alias\_indexIndex of the device alias which was selected\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackDeviceAliasesUpdateDone()

[Return to Main Typedefs](#main-typedefs)

`1`

`typedef void(* SpCallbackDeviceAliasesUpdateDone)(SpError error_code, void *context)`

Callback for knowing when the device alias list has been updated after call to [SpSetDeviceAliases](#spsetdevicealiases)

To register this callback, use the function [SpRegisterDeviceAliasCallbacks](#spregisterdevicealiascallbacks) This callback is invoked when the operation started by call to [SpSetDeviceAliases](#spsetdevicealiases) has finished.

**Parameters**

\[in][SpError](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sperror) error\_codeif the update was successful, the value is [kSpErrorOk](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sperror)\[in]`void` * contextContext pointer that was passed when registering the callback

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

## Enumerations

* * *

### SpError

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpError {`

`2`

`kSpErrorOk,`

`3`

`kSpErrorFailed,`

`4`

`kSpErrorInitFailed,`

`5`

`kSpErrorWrongAPIVersion,`

`6`

`kSpErrorNullArgument,`

`7`

`kSpErrorInvalidArgument,`

`8`

`kSpErrorUninitialized,`

`9`

`kSpErrorAlreadyInitialized,`

`10`

`kSpErrorLoginBadCredentials,`

`11`

`kSpErrorNeedsPremium,`

`12`

`kSpErrorTravelRestriction,`

`13`

`kSpErrorApplicationBanned,`

`14`

`kSpErrorGeneralLoginError,`

`15`

`kSpErrorUnsupported,`

`16`

`kSpErrorNotActiveDevice,`

`17`

`kSpErrorAPIRateLimited,`

`18`

`kSpErrorReentrancyDetected,`

`19`

`kSpErrorMultiThreadingDetected,`

`20`

`kSpErrorTryAgain,`

`21`

`kSpErrorDuringLogout,`

`22`

`kSpErrorPermanentConnectionError,`

`23`

`kSpErrorEntropyFailure,`

`24`

`kSpErrorZeroConfErrorStart,`

`25`

`kSpErrorZeroConfBadRequest,`

`26`

`kSpErrorZeroConfUnknown,`

`27`

`kSpErrorZeroConfNotImplemented,`

`28`

`kSpErrorZeroConfNotInstalled,`

`29`

`kSpErrorZeroConfNotLoaded,`

`30`

`kSpErrorZeroConfNotAuthorized,`

`31`

`kSpErrorZeroConfCannotLoad,`

`32`

`kSpErrorZeroConfSystemUpdateRequired,`

`33`

`kSpErrorZeroConfSpotifyUpdateRequired,`

`34`

`kSpErrorZeroConfLoginFailed,`

`35`

`kSpErrorZeroConfInvalidPublicKey,`

`36`

`kSpErrorZeroConfMissingAction,`

`37`

`kSpErrorZeroConfInvalidAction,`

`38`

`kSpErrorZeroConfInvalidArguments,`

`39`

`kSpErrorZeroConfNoSpotifySession,`

`40`

`kSpErrorZeroConfSpotifyError,`

`41`

`kSpErrorPlaybackErrorStart,`

`42`

`kSpErrorGeneralPlaybackError,`

`43`

`kSpErrorPlaybackRateLimited,`

`44`

`kSpErrorPlaybackCappingLimitReached,`

`45`

`kSpErrorAdIsPlaying,`

`46`

`kSpErrorCorruptTrack,`

`47`

`kSpErrorContextFailed,`

`48`

`kSpErrorPrefetchItemUnavailable,`

`49`

`kSpAlreadyPrefetching,`

`50`

`kSpStorageReadError,`

`51`

`kSpStorageWriteError,`

`52`

`kSpPrefetchDownloadFailed,`

`53`

`kSpErrorBusy,`

`54`

`kSpErrorUnavailable,`

`55`

`kSpErrorNotAllowed,`

`56`

`kSpErrorNetworkRequired,`

`57`

`kSpErrorNotLoggedIn,`

`58`

`kSpErrorInProgress,`

`59`

`kSpErrorPlaybackInitiation,`

`60`

`kSpErrorPresetFailed,`

`61`

`kSpErrorInvalidRequest,`

`62`

`kSpErrorInvalidTrackId,`

`63`

`kSpErrorIncorrectMsPlayed,`

`64`

`kSpErrorDeviceNotControllable,`

`65`

`kSpErrorPlaybackInitiationTimeout,`

`66`

`};`

kSpErrorOkThe operation was successful.kSpErrorFailedThe operation failed due to an unspecified issue.kSpErrorInitFailedThe library could not be initialized.kSpErrorWrongAPIVersionThe library could not be initialized because of an incompatible API version.kSpErrorNullArgumentAn unexpected NULL pointer was passed as an argument to a function.kSpErrorInvalidArgumentAn unexpected argument value was passed to a function.kSpErrorUninitializedA function was invoked before SpInit or after SpFree was called.kSpErrorAlreadyInitializedSpInit was called more than once.kSpErrorLoginBadCredentialsLogin to Spotify failed because of invalid credentials.kSpErrorNeedsPremiumThe operation requires a Spotify Premium account.kSpErrorTravelRestrictionThe Spotify user is not allowed to log in from this country.kSpErrorApplicationBannedThe application has been banned by SpotifykSpErrorGeneralLoginErrorAn unspecified login error occurred.kSpErrorUnsupportedThe operation is not supported.kSpErrorNotActiveDeviceThe operation is not supported if the device is not the active playback device.kSpErrorAPIRateLimitedThe API has been rate-limited.kSpErrorReentrancyDetectedThe eSDK API was used from a callback.kSpErrorMultiThreadingDetectedThe eSDK API was used from multiple threads.kSpErrorTryAgainThe eSDK API cannot be performed right now.kSpErrorDuringLogoutLogout failed during SpFree call.kSpErrorPermanentConnectionErrorPermanent connection error. eSDK ceased attempts to reconnect.kSpErrorEntropyFailureFailed to get cryptographic random data from the platform.kSpErrorZeroConfErrorStartError range reserved for ZeroConf-related errors.kSpErrorZeroConfBadRequestZeroConf Web server problem or critically malformed request.kSpErrorZeroConfUnknownFallback when no other ZeroConf error applies.kSpErrorZeroConfNotImplementedZeroConf device does not implement this feature.kSpErrorZeroConfNotInstalledSpotify not installed (where applicable)kSpErrorZeroConfNotLoadedSpotify not loaded (where applicable)kSpErrorZeroConfNotAuthorizedSpotify client not authorized to play.kSpErrorZeroConfCannotLoadSpotify cannot be loaded (where applicable)kSpErrorZeroConfSystemUpdateRequiredDevice system needs update (where applicable)kSpErrorZeroConfSpotifyUpdateRequiredSpotify client application needs update.kSpErrorZeroConfLoginFailedSpotify returned error when trying to login.kSpErrorZeroConfInvalidPublicKeyZeroConf login failed due to an invalid public key.kSpErrorZeroConfMissingActionZeroConf HTTP request has no action parameter.kSpErrorZeroConfInvalidActionZeroConf HTTP request has unrecognized action parameter.kSpErrorZeroConfInvalidArgumentsIncorrect or insufficient ZeroConf arguments supplied for requested action.kSpErrorZeroConfNoSpotifySessionAttempted Spotify action but no valid Spotify session is available (where applicable)kSpErrorZeroConfSpotifyErrorA Spotify API call returned an error not covered by other error messages.kSpErrorPlaybackErrorStartError range reserved for playback-related errors.kSpErrorGeneralPlaybackErrorAn unspecified playback error occurred.kSpErrorPlaybackRateLimitedThe application has been rate-limited.kSpErrorPlaybackCappingLimitReachedThe Spotify user has reached a capping limit that is in effect in this country and/or for this track.kSpErrorAdIsPlayingCannot change track while ad is playing.kSpErrorCorruptTrackThe track is (temporarily) corrupt in the Spotify catalogue.kSpErrorContextFailedUnable to read all tracks from the playing context.kSpErrorPrefetchItemUnavailableThe item that was being prefetched was unavailable, and cannot be fetched. This could be due to an invalid URI, changes in track availability, or geographical limitations. This is a permanent error, and the item should not be tried again.kSpAlreadyPrefetchingAn item is already actively being prefetched. You must stop the current prefetch request to start another one. This error is only relevant for builds with offline storage enabled.kSpStorageReadErrorA permanent error was encountered while reading to a registered file storage callback. This error is only relevant for builds with offline storage enabled.kSpStorageWriteErrorA permanent error was encountered while writing to a registered file storage callback. This error is only relevant for builds with offline storage enabled.kSpPrefetchDownloadFailedPrefetched item was not fully downloaded or failed. If error happens prefetch can be retried. This error is only relevant for builds with offline storage enabled.kSpErrorBusyCurrent API call cannot be completed because eSDK is busy. Same API call should be done sometime later with same arguments.kSpErrorUnavailableCurrent API call cannot be completed because the said operation is not available at the moment.kSpErrorNotAllowedThis eSDK API is not allowed due to current license restrictions.kSpErrorNetworkRequiredCurrent API call cannot be completed since it's not connected to SpotifykSpErrorNotLoggedInCurrent API call cannot be completed without being logged in.kSpErrorInProgressUsed in callbacks to notify the application that the action is not yet complete.kSpErrorPlaybackInitiationUsed in SpCallbackError callback to notify the application that playback initiation failed.kSpErrorPresetFailedUsed in SpCallbackError callback to notify the application that recalling and playing a preset failed.kSpErrorInvalidRequestUsed in SpCallbackError callback to notify the application that the request was rejected as invalid.kSpErrorInvalidTrackIdUsed in SpCallbackError callback to notify the application that an invalid track\_id was used.kSpErrorIncorrectMsPlayedUsed in SpCallbackError callback to notify the application that an incorrect value for ms\_played was reported.kSpErrorDeviceNotControllableThe operation is not allowed since the device is not controllable.kSpErrorPlaybackInitiationTimeoutThe playback initiation operation timed out.

### SpAPIReturnCode

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpAPIReturnCode {`

`2`

`kSpAPINoError,`

`3`

`kSpAPITryAgain,`

`4`

`kSpAPIDNSLookupError,`

`5`

`kSpAPIGenericError,`

`6`

`kSpAPINotSupported,`

`7`

`kSpAPIEOF,`

`8`

`kSpAPINotFound,`

`9`

`};`

kSpAPINoErrorThis code should be used when API call was successful.kSpAPITryAgainThis code means operation cannot be performed right now. Same API call should be done sometime later with same arguments.kSpAPIDNSLookupErrorUse to notify about any DNS lookup error that cannot be retried.kSpAPIGenericErrorAPI call has failed.kSpAPINotSupportedRequested feature is not supported by platform.kSpAPIEOFEnd of file/socket reached.kSpAPINotFoundRequested resource does not exist.

### SpPlaybackBitrate

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpPlaybackBitrate {`

`2`

`kSpPlaybackBitrateDefault,`

`3`

`kSpPlaybackBitrateLow,`

`4`

`kSpPlaybackBitrateNormal,`

`5`

`};`

kSpPlaybackBitrateDefaultSet bitrate to the default (currently High).kSpPlaybackBitrateLowSet bitrate to low. Corresponds to e.g. 96 kbit/s ogg/vorbis.kSpPlaybackBitrateNormalSet bitrate to normal. Corresponds to e.g. 160 kbit/s ogg/vorbis.

### SpPlaybackNotification

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpPlaybackNotification {`

`2`

`kSpPlaybackNotifyPlay,`

`3`

`kSpPlaybackNotifyPause,`

`4`

`kSpPlaybackNotifyTrackChanged,`

`5`

`kSpPlaybackNotifyNext,`

`6`

`kSpPlaybackNotifyPrev,`

`7`

`kSpPlaybackNotifyShuffleOn,`

`8`

`kSpPlaybackNotifyShuffleOff,`

`9`

`kSpPlaybackNotifyRepeatOn,`

`10`

`kSpPlaybackNotifyRepeatOff,`

`11`

`kSpPlaybackNotifyBecameActive,`

`12`

`kSpPlaybackNotifyBecameInactive,`

`13`

`kSpPlaybackNotifyLostPermission,`

`14`

`kSpPlaybackNotifyAudioDeliveryDone,`

`15`

`kSpPlaybackNotifyContextChanged,`

`16`

`kSpPlaybackNotifyMetadataChanged,`

`17`

`kSpPlaybackNotifyNetworkRequired,`

`18`

`kSpPlaybackNotifyTrackDownloadStalled,`

`19`

`kSpPlaybackNotifyQueuedTrackAccepted,`

`20`

`};`

kSpPlaybackNotifyPlayPlayback has started or has resumed.kSpPlaybackNotifyPausePlayback has been paused.kSpPlaybackNotifyTrackChangedThe current track or its metadata has changed.kSpPlaybackNotifyNextPlayback has skipped to the next track.kSpPlaybackNotifyPrevPlayback as skipped to the previous track.kSpPlaybackNotifyShuffleOn"Shuffle" was switched onkSpPlaybackNotifyShuffleOff"Shuffle" was switched offkSpPlaybackNotifyRepeatOn"Repeat" was switched onkSpPlaybackNotifyRepeatOff"Repeat" was switched offkSpPlaybackNotifyBecameActiveThis device has become the active playback device.kSpPlaybackNotifyBecameInactiveThis device is no longer the active playback device.kSpPlaybackNotifyLostPermissionThis device has temporarily lost permission to stream audio from SpotifykSpPlaybackNotifyAudioDeliveryDoneThe library will not send any more audio data.kSpPlaybackNotifyContextChangedPlayback changed to a different Spotify context.kSpPlaybackNotifyMetadataChangedMetadata is changed.kSpPlaybackNotifyNetworkRequiredPlayback is not allowed without network.kSpPlaybackNotifyTrackDownloadStalledDownload of the current track stalled due to network outage.kSpPlaybackNotifyQueuedTrackAcceptedQueued track is accepted by the playback-service.

### SpConnectionNotification

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpConnectionNotification {`

`2`

`kSpConnectionNotifyLoggedIn,`

`3`

`kSpConnectionNotifyLoggedOut,`

`4`

`kSpConnectionNotifyTemporaryError,`

`5`

`kSpConnectionNotifyDisconnect,`

`6`

`kSpConnectionNotifyReconnect,`

`7`

`kSpConnectionNotifyProductTypeChanged,`

`8`

`kSpConnectionNotifyZeroConfVarsChanged,`

`9`

`kSpConnectionNotifyTransmittingData,`

`10`

`};`

kSpConnectionNotifyLoggedInThe user has successfully logged in to SpotifykSpConnectionNotifyLoggedOutThe user has been logged out of SpotifykSpConnectionNotifyTemporaryErrorA temporary connection error occurred. The library will automatically retry.kSpConnectionNotifyDisconnectThe connection to Spotify has been lost.kSpConnectionNotifyReconnectThe connection to Spotify has been (re-)established.kSpConnectionNotifyProductTypeChangedThe connected user account type has changed (became premium, for example).kSpConnectionNotifyZeroConfVarsChangedThe SpZeroConfVars has changed.kSpConnectionNotifyTransmittingDataThe eSDK is transmitting data.

### SpDeviceType

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpDeviceType {`

`2`

`kSpDeviceTypeComputer,`

`3`

`kSpDeviceTypeTablet,`

`4`

`kSpDeviceTypeSmartphone,`

`5`

`kSpDeviceTypeSpeaker,`

`6`

`kSpDeviceTypeTV,`

`7`

`kSpDeviceTypeAVR,`

`8`

`kSpDeviceTypeSTB,`

`9`

`kSpDeviceTypeAudioDongle,`

`10`

`kSpDeviceTypeGameConsole,`

`11`

`kSpDeviceTypeCastVideo,`

`12`

`kSpDeviceTypeCastAudio,`

`13`

`kSpDeviceTypeAutomobile,`

`14`

`kSpDeviceTypeSmartwatch,`

`15`

`kSpDeviceTypeChromebook,`

`16`

`};`

kSpDeviceTypeComputerLaptop or desktop computer device.kSpDeviceTypeTabletTablet PC device.kSpDeviceTypeSmartphoneSmartphone device.kSpDeviceTypeSpeakerSpeaker device.kSpDeviceTypeTVTelevision device.kSpDeviceTypeAVRAudio/Video receiver device.kSpDeviceTypeSTBSet-Top Box device.kSpDeviceTypeAudioDongleAudio dongle device.kSpDeviceTypeGameConsoleGame console device.kSpDeviceTypeCastVideoChromecast Video.kSpDeviceTypeCastAudioChromecast Audio.kSpDeviceTypeAutomobileAutomobile.kSpDeviceTypeSmartwatchSmartwatch.kSpDeviceTypeChromebookChromebook.

### SpMetadataTrack

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpMetadataTrack {`

`2`

`kSpMetadataTrackBeforePrevious,`

`3`

`kSpMetadataTrackPrevious,`

`4`

`kSpMetadataTrackCurrent,`

`5`

`kSpMetadataTrackNext,`

`6`

`kSpMetadataTrackAfterNext,`

`7`

`};`

kSpMetadataTrackBeforePreviousIndex of the before previous track in the track list.kSpMetadataTrackPreviousIndex of the previous track in the track list.kSpMetadataTrackCurrentIndex of the current track in the track list.kSpMetadataTrackNextIndex of the next track in the track list.kSpMetadataTrackAfterNextIndex of the after next track in the track list.

### SpConnectivity

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpConnectivity {`

`2`

`kSpConnectivityNone,`

`3`

`kSpConnectivityWired,`

`4`

`kSpConnectivityWireless,`

`5`

`kSpConnectivityMobile,`

`6`

`};`

kSpConnectivityNoneThe device is not connected to the network.kSpConnectivityWiredThe device is connected to a wired network.kSpConnectivityWirelessThe device is connected to a wireless network.kSpConnectivityMobileThe device uses a mobile data connection.

### SpContent

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpContent {`

`2`

`kSpContentUnknown,`

`3`

`kSpContentMusicTrack,`

`4`

`kSpContentShowEpisode,`

`5`

`kSpContentAd,`

`6`

`};`

kSpContentUnknownUnknown content type.kSpContentMusicTrackMusic track.kSpContentShowEpisodePodcast show episode.kSpContentAdAdvertisement.

### SpMediaType

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpMediaType {`

`2`

`kSpMediaTypeAudio,`

`3`

`kSpMediaTypeVideo,`

`4`

`};`

kSpMediaTypeAudioAudio media type.kSpMediaTypeVideoVideo media type.

### SpAudioQuality

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpAudioQuality {`

`2`

`kSpAudioQualityUnknown,`

`3`

`kSpAudioQualityLow,`

`4`

`kSpAudioQualityNormal,`

`5`

`kSpAudioQualityHigh,`

`6`

`kSpAudioQualityVeryHigh,`

`7`

`};`

kSpAudioQualityUnknownUnknown audio quality.kSpAudioQualityLowLow audio quality.kSpAudioQualityNormalNormal audio quality (e.g. 96 kbps ogg/vorbis)kSpAudioQualityHighHigh audio quality (e.g. 160 kbps ogg/vorbis)kSpAudioQualityVeryHighVery high audio quality (e.g. 320 kbps ogg/vorbis)

### SpDrmFormat

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpDrmFormat {`

`2`

`kSpDrmFormatUnknown,`

`3`

`kSpDrmFormatUnencrypted,`

`4`

`kSpDrmFormatFairPlay,`

`5`

`kSpDrmFormatWidevine,`

`6`

`kSpDrmFormatPlayReady,`

`7`

`};`

kSpDrmFormatUnknownUnknown DRM.kSpDrmFormatUnencryptedNo DRM, unencrypted.kSpDrmFormatFairPlayFairPlay.kSpDrmFormatWidevineWidevine.kSpDrmFormatPlayReadyPlayReady.

### SpReDeliveryMode

[Return to Main enumerations](#main-enumerations)

`1`

`enum SpReDeliveryMode {`

`2`

`kSpRedeliveryModeActivated,`

`3`

`kSpRedeliveryModeDeactivated,`

`4`

`};`

kSpRedeliveryModeActivatedRedelivery is activated.kSpRedeliveryModeDeactivatedRedelivery is deactivated.

## Functions

* * *

### SpInit()

[Return to Main functions](#main-functions)

`1`

`SpError SpInit(struct SpConfig *conf)`

Initialize the library.

**Parameters**

\[in]`struct` [SpConfig](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spconfig) * confConfiguration parameters

**Returns**

Returns an error code

### SpFree()

[Return to Main functions](#main-functions)

Shut down the library.

If a user is currently logged in, the application should first call [SpConnectionLogout](#spconnectionlogout) and wait for the [kSpConnectionNotifyLoggedOut](#spconnectionnotification) event, otherwise [SpFree](#spfree) may take several seconds.

**Returns**

Returns an error code

### SpGetLibraryVersion()

[Return to Main functions](#main-functions)

`1`

`const char * SpGetLibraryVersion(void)`

Retrieve a version string for the library.

**Returns**

Version string

**Notes:**

- This API can be invoked from a callback.

### SpConnectionSetConnectivity()

[Return to Main functions](#main-functions)

`1`

`SpError SpConnectionSetConnectivity(enum SpConnectivity connectivity)`

Set the type of network connection of the device.

When the application detects that the device has lost network connection, it should call this function with [kSpConnectivityNone](#spconnectivity) When network connection is restored, the application should call this function with one of the other values of [SpConnectivity](#spconnectivity) The library will then immediately retry to reconnect to Spotify (rather than waiting for the next retry timeout). The library may use the type of network connection to adapt its streaming and buffering strategies. Currently, however, all types of network connection are treated the same.

**Parameters**

**Returns**

Returns an error code

### SpConnectionGetConnectivity()

[Return to Main functions](#main-functions)

`1`

`enum SpConnectivity SpConnectionGetConnectivity(void)`

Get the connectivity that was set with [SpConnectionSetConnectivity](#spconnectionsetconnectivity)

The library does not detect the type of network connection by itself. It only updates it if the application calls [SpConnectionSetConnectivity](#spconnectionsetconnectivity) If [SpConnectionSetConnectivity](#spconnectionsetconnectivity) was never called, the connection defaults to [kSpConnectivityWired](#spconnectivity)

**Returns**

Type of connection

**Notes:**

- This API can be invoked from a callback.

### SpConnectionLoginBlob()

[Return to Main functions](#main-functions)

`1`

`SpError SpConnectionLoginBlob(const char *username, const char *credentials_blob)`

Log in a user to Spotify using a credentials blob.

**Parameters**

\[in]`const` `char` * usernameSpotify username. UTF-8 encoded. Must not be longer than [SP\_MAX\_USERNAME\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_username_length) bytes (not UTF-8-encoded characters), not counting the terminating NULL. (For users that log in via Facebook, this is an email address.)\[in]`const` `char` * credentials\_blobCredentials blob received via ZeroConf or in the callback [SpCallbackConnectionNewCredentials](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spcallbackconnectionnewcredentials) Note: if the credentials\_blob is an empty string, this function should not be called or it will return [kSpErrorFailed](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sperror)

**Returns**

Returns an error code

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:
- The blob can only be used for subsequent logins as long as the value of [SpConfig::unique\_id](#spconfig) does not change. If [SpConfig::unique\_id](#spconfig) has changed since the blob was received, this function returns an error and you will receive a debug message similar to "Parsing ZeroConf blob failed with code -3".

### SpConnectionLoginPassword()

[Return to Main functions](#main-functions)

`1`

`SpError SpConnectionLoginPassword(const char *username, const char *password)`

Log in a user to Spotify using a password.

Returns [kSpErrorGeneralLoginError](#sperror) if a connection is not present. For logging in offline please use [SpConnectionLoginBlob](#spconnectionloginblob) Applications must not store the password. Instead, they should implement the callback [SpCallbackConnectionNewCredentials](#spcallbackconnectionnewcredentials) and store the credentials blob that they receive for subsequent logins using the function [SpConnectionLoginBlob](#spconnectionloginblob)

**Parameters**

\[in]`const` `char` * usernameSpotify username. UTF-8 encoded. Must not be longer than [SP\_MAX\_USERNAME\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_username_length) bytes (not UTF-8-encoded characters), not counting the terminating NULL. (For users that log in via Facebook, this is an email address.)\[in]`const` `char` * passwordPassword

**Returns**

Returns an error code

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:
- Spotify Connect-enabled hardware devices must not use this function. Such devices must implement the ZeroConf and use the function [SpConnectionLoginBlob](#spconnectionloginblob) instead.

### SpConnectionLoginOauthToken()

[Return to Main functions](#main-functions)

`1`

`SpError SpConnectionLoginOauthToken(const char *oauth_token)`

Log in a user to Spotify using a Spotify OAuth token.

For subsequent logins the [SpCallbackConnectionNewCredentials](#spcallbackconnectionnewcredentials) callback should be implemented and the received credentials blob should be stored and used. (Note that the OAuth access token itself expires after a short time. The credentials blob returned by the callback allows you to re-login even after the token has expired.)

**Parameters**

**Returns**

Returns an error code

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:
- Spotify Connect-enabled hardware devices that implement the ZeroConf stack must use the function [SpConnectionLoginBlob](#spconnectionloginblob) instead.

### SpConnectionLogout()

[Return to Main functions](#main-functions)

`1`

`SpError SpConnectionLogout(void)`

Log the user out of Spotify

**Returns**

Returns an error code

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The logout is performed asynchronously. The logout is complete when the callback [SpCallbackConnectionNotify](#spcallbackconnectionnotify) is called with the event [kSpConnectionNotifyLoggedOut](#spconnectionnotification)

### SpConnectionIsLoggedIn()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpConnectionIsLoggedIn(void)`

Is the user logged in to Spotify

**Returns**

1: The user is logged in 0: The user is not logged in

**See also**

- [kSpConnectionNotifyLoggedIn](#spconnectionnotification)
- [kSpConnectionNotifyLoggedOut](#spconnectionnotification)
- [SpConnectionLoginBlob](#spconnectionloginblob)
- [SpConnectionLogout](#spconnectionlogout)

**Notes:**

- This API can be invoked from a callback.

### SpConnectionGetAckId()

[Return to Main functions](#main-functions)

`1`

`const char * SpConnectionGetAckId(void)`

Get last Ack ID.

**Notes:**

- This function is deprecated and should not be used.

### SpGetCanonicalUsername()

[Return to Main functions](#main-functions)

`1`

`const char * SpGetCanonicalUsername(void)`

Get the canonical username of the logged in user.

This function returns the canonical username of the logged in user, which is the unique username used for identifying a specific user for things like playlists and the Spotify Web API. This username might differ from the username used to login. A user can login with an e-mail address or non-canonical unicode. This function will return the canonicalized version of the username after a successful login.

**Returns**

Returns a string containing the username, or NULL if no user is logged in.

**Notes:**

- The canonical username should not be stored persistently. Always store the username as provided by the user, not the canonicalized version.
- This API can be invoked from a callback.

### SpSetDisplayName()

[Return to Main functions](#main-functions)

`1`

`SpError SpSetDisplayName(const char *display_name)`

Set the display name for the application/device.

This function can be used to change the display name that was passed to [SpInit](#spinit) in the field [SpConfig::display\_name](#spconfig)

**Parameters**

\[in]`const` `char` * display\_nameA UTF-8-encoded display name

**Returns**

Returns an error code

**Notes:**

- The display name is not allowed to be an empty string.

### SpSetVolumeSteps()

[Return to Main functions](#main-functions)

`1`

`SpError SpSetVolumeSteps(uint32_t steps)`

Set the volume steps the device is capable of.

This function will indicate the number of intermediate steps from ´min\_volume´ to ´max\_volume´ that the device supports. If there's no volume control ability it must be set to zero to inform that no volume control is possible at all. The default number of steps if this function is not called is 16.

**Parameters**

\[in]`uint32_t` stepsthe number of volume steps the device can support. 0 means no volume steps at all. The max value that is possible to set is 65535.

**Returns**

Returns an error code

**Notes:**

- There's no commitment from the other Connect clients to respect the volume steps. It's important to call this function passing zero if no volume control is possible though.

### SpSetDeviceIsGroup()

[Return to Main functions](#main-functions)

`1`

`SpError SpSetDeviceIsGroup(int is_group)`

Control if the device represents a group.

A group is a number of devices all playing back the same sound synchronized. Setting this status correctly will allow Spotify clients to display the correct metadata for this device.

**Parameters**

\[in]`int` is\_group0: Indicate that this device is a single stand-alone device. 1: Indicate that this device represents a group.

**Notes:**

- If device aliases are used, this function should not be used to set the group status. Instead, [SpSetDeviceAliases](#spsetdevicealiases) should be used to update group status individually for each alias.

### SpEnableConnect()

[Return to Main functions](#main-functions)

`1`

`SpError SpEnableConnect(void)`

Enable Connect functionality for this device.

A device with enabled Connect functionality will show up in other devices' Connect pickers, and will be able to both control them and be controlled. The Spotify embedded library will enable Connect functionality by default

### SpDisableConnect()

[Return to Main functions](#main-functions)

`1`

`SpError SpDisableConnect(void)`

Disable Connect functionality for this device.

A device that disables Connect will not be able to control playback on other devices, or be controlled by them.

### SpGetSelectedDeviceAlias()

[Return to Main functions](#main-functions)

`1`

`int SpGetSelectedDeviceAlias(void)`

Return the currently selected device alias.

**Returns**

The currently selected device alias or -1 if no alias selected.

### SpPumpEvents()

[Return to Main functions](#main-functions)

`1`

`SpError SpPumpEvents(void)`

Allow the library to perform asynchronous tasks and process events.

Note: The suggested time interval to call this function is 10ms. This function should not be called from a callback. A typical usage pattern looks like this:

**Returns**

Returns an error code

### SpRegisterConnectionCallbacks()

[Return to Main functions](#main-functions)

`1`

`SpError SpRegisterConnectionCallbacks(struct SpConnectionCallbacks *cb, void *context)`

Register callbacks related to the connection to Spotify

**Parameters**

\[in]`struct` [SpConnectionCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spconnectioncallbacks) * cbStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

### SpRegisterDebugCallbacks()

[Return to Main functions](#main-functions)

`1`

`SpError SpRegisterDebugCallbacks(struct SpDebugCallbacks *cb, void *context)`

Register a callback that receives debug messages/trace logs.

These callbacks can be registered before [SpInit](#spinit) has been called, in order to receive debug logs that occur during initialization.

**Parameters**

\[in]`struct` [SpDebugCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdebugcallbacks) * cbStructure with pointers to individual callback functions.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callback.

**Returns**

Returns an error code

### SpRegisterPlaybackCallbacks()

[Return to Main functions](#main-functions)

`1`

`SpError SpRegisterPlaybackCallbacks(struct SpPlaybackCallbacks *cb, void *context)`

Register playback-related callbacks.

**Parameters**

\[in]`struct` [SpPlaybackCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spplaybackcallbacks) * cbStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

### SpGetMetadata()

[Return to Main functions](#main-functions)

`1`

`SpError SpGetMetadata(struct SpMetadata *metadata, int relative_index)`

Retrieve metadata for a track in the current track list.

**Parameters**

\[out]`struct` [SpMetadata](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spmetadata) * metadataStructure to be filled with the metadata for the track\[in]`int` relative\_indexTrack index relative to the current track. Some relative indices are defined in the `enum` [SpMetadataTrack](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spmetadatatrack)

**Returns**

Returns an error code. Returns kSpErrorFailed if relative\_index is out of range.

**Notes:**

- This API can be invoked from a callback.
- Be aware that many APIs that change the currently playing context are asynchronous, and the changes will not be immediately reflected in the metadata returned by [SpGetMetadata](#spgetmetadata) For example, when calling [SpPlaybackSkipToNext](#spplaybackskiptonext) [SpPlaybackEnableShuffle](#spplaybackenableshuffle) etc., the metadata returned by [SpGetMetadata](#spgetmetadata) might be unchanged while the command is being processed (which involves network communication). The notification [kSpPlaybackNotifyMetadataChanged](#spplaybacknotification) will be sent as soon as [SpGetMetadata](#spgetmetadata) would return a different result for any relative\_index defined in the *enum* [SpMetadataTrack](#spmetadatatrack)

### SpGetMetadataImageURL()

[Return to Main functions](#main-functions)

`1`

`SpError SpGetMetadataImageURL(const char *image_uri, char *image_url, size_t image_url_size)`

Return the HTTP URL to an image file from a spotify:image: URI.

**Parameters**

\[in]`const` `char` * image\_uriimage URI returned in [SpMetadata::album\_cover\_uri](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spmetadata)\[out]`char` * image\_urlPointer to a buffer that will be filled with HTTP URL.\[in]size\_t image\_url\_sizesize of the image\_url buffer. [SP\_MAX\_METADATA\_IMAGE\_URL\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_metadata_image_url_length) is the max amount od data that can be returned in image\_url.

**Returns**

Returns an error code. Returns kSpErrorFailed if the buffer is not big enough.

**Notes:**

- This API can be invoked from a callback.

### SpGetPlayerCookie()

[Return to Main functions](#main-functions)

`1`

`SpError SpGetPlayerCookie(char *player_cookie, size_t player_cookie_size)`

Obtain player cookie for current playback.

The obtained player cookie can then be used to get more detailed metadata for current playback from Spotify's backend using Spotify Web API.

**Parameters**

\[out]`char` * player\_cookiePointer to a buffer where the player cookie will be copied. This buffer will be reset even if there is no player cookie available.\[in]size\_t player\_cookie\_sizeSize of the player\_cookie buffer. Player cookie length is defined [SP\_PLAYER\_COOKIE\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_player_cookie_length) and the buffer should be at least SP\_PLAYER\_COOKIE\_LENGTH+1 in size.

**Returns**

Returns an error code. Returns kSpErrorUnsupported if the build configuration doesn't support player cookies.

**Notes:**

- Experimental, subject to change

### SpPlaybackPlay()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackPlay(int alias_index)`

Start or resume playback.

**Parameters**

\[in]`int` alias\_indexThe index of the device alias to start playback on. If aliases aren't used, pass -1.

**Returns**

Returns an error code

### SpPlaybackPause()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackPause(void)`

Pause playback.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Returns**

Returns an error code

### SpPlaybackSkipToNext()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSkipToNext(void)`

Skip playback to the next track in the track list.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Returns**

Returns an error code

### SpPlaybackSkipToPrev()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSkipToPrev(void)`

Skip playback to the previous track in the track list.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Returns**

Returns an error code

**Notes:**

- This function will try to skip to the previous track regardless of the current playback position. If the desired behaviour is to only skip to the previous track UNLESS the current playback position is beyond 3 seconds, the following code example is suggested as a base: if(SpPlaybackGetPosition()/1000=3) SpPlaybackSeek(0); else [SpPlaybackSkipToPrev](#spplaybackskiptoprev)

### SpPlaybackSeek()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSeek(uint32_t position_ms)`

Seek to a position within the current track.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Parameters**

\[in]`uint32_t` position\_msPosition within the track in milliseconds

**Returns**

Returns an error code

### SpPlaybackSeekRelative()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSeekRelative(int32_t time_ms)`

Seek a relative amount of time within the current track.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Parameters**

\[in]`int32_t` time\_msAmount of time to seek within the current track, negative values seek backwards and positive values seek forward.

**Returns**

Returns an error code

### SpPlaybackGetPosition()

[Return to Main functions](#main-functions)

`1`

`uint32_t SpPlaybackGetPosition(void)`

Get the current playback position within the track.

**Returns**

Playback position in milliseconds

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackUpdateVolume()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackUpdateVolume(uint16_t volume)`

Request a change to the playback volume.

It is the application's responsibility to apply the volume change to its audio output. This function merely notifies the library of the volume change, so that the library can inform other Spotify Connect-enabled devices. Calling this function invokes the [SpCallbackPlaybackApplyVolume](#spcallbackplaybackapplyvolume) callback, which the application can use to apply the actual volume change.

**Parameters**

\[in]uint16\_t volumeVolume in the range 0 (silence) to 65535 (full volume)

**Returns**

Returns an error code

**Notes:**

- When the library is initialized, it assumes a volume level of 65535 (maximum volume). The application must invoke [SpPlaybackUpdateVolume](#spplaybackupdatevolume) at some point after calling [SpInit](#spinit) to inform the library of the actual volume level of the device's audio output.

### SpPlaybackGetVolume()

[Return to Main functions](#main-functions)

`1`

`uint16_t SpPlaybackGetVolume(void)`

Get the playback volume level.

This returns the last volume level that the application set using [SpPlaybackUpdateVolume](#spplaybackupdatevolume) or that was reported to the application using [SpCallbackPlaybackApplyVolume](#spcallbackplaybackapplyvolume)

**Returns**

Volume level in the range 0 (silence) to 65535 (full volume).

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsPlaying()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackIsPlaying(void)`

Is the playback status playing or paused.

**Returns**

1: Playback status is playing 0: Playback status is paused (or no playback has been started at all)

**See also**

- [kSpPlaybackNotifyPlay](#spplaybacknotification)
- [kSpPlaybackNotifyPause](#spplaybacknotification)
- [SpPlaybackPlay](#spplaybackplay)
- [SpPlaybackPause](#spplaybackpause)

**Notes:**

- This API can be invoked from a callback.
- The result of this API is analogous to the playback notifications [kSpPlaybackNotifyPlay](#spplaybacknotification) and kSpPlaybackNotifypause

### SpPlaybackIsAdPlaying()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackIsAdPlaying(void)`

Is the the current track an Ad or not.

**Returns**

1: The current playing track is an Ad 0: The current playing track is not an Ad.

**See also**

- [kSpPlaybackNotifyTrackChanged](#spplaybacknotification)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsShuffled()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackIsShuffled(void)`

Is "shuffle" mode enabled.

**Returns**

1: Shuffle is enabled 0: Shuffle is disabled

**See also**

- [kSpPlaybackNotifyShuffleOn](#spplaybacknotification)
- [kSpPlaybackNotifyShuffleOff](#spplaybacknotification)
- [SpPlaybackEnableShuffle](#spplaybackenableshuffle)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsRepeated()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackIsRepeated(void)`

Is "repeat" mode enabled.

**Returns**

1: Repeat is enabled 0: Repeat is disabled

**See also**

- [kSpPlaybackNotifyRepeatOn](#spplaybacknotification)
- [kSpPlaybackNotifyRepeatOff](#spplaybacknotification)
- [SpPlaybackEnableRepeat](#spplaybackenablerepeat)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackGetRepeatMode()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackGetRepeatMode(void)`

What "repeat" mode is on.

**Returns**

0: Repeat is disabled 1: Repeat Context is enabled 2: Repeat Track is enabled

**See also**

- [kSpPlaybackNotifyRepeatOn](#spplaybacknotification)
- [kSpPlaybackNotifyRepeatOff](#spplaybacknotification)
- [SpPlaybackEnableRepeat](#spplaybackenablerepeat)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsActiveDevice()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackIsActiveDevice(void)`

Is the device the active playback device.

**Returns**

1: The device is the active playback device 0: Another device is the active playback device

**See also**

- [kSpPlaybackNotifyBecameActive](#spplaybacknotification)
- [kSpPlaybackNotifyBecameInactive](#spplaybacknotification)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackEnableShuffle()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackEnableShuffle(uint8_t enable)`

Enable or disable "shuffle" mode.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Parameters**

\[in]uint8\_t enable1 to enable, 0 to disable

**Returns**

Returns an error code

**See also**

- [SpPlaybackIsShuffled](#spplaybackisshuffled)

**Notes:**

- The change to the shuffle mode might not take effect if the API is invoked in the time window between requesting playback of a new context (e.g., by calling SpPlayUri), and playback of the new context actually starting.

### SpPlaybackEnableRepeat()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackEnableRepeat(uint8_t enable)`

Enable or disable "repeat" mode.

If the device is not the active speaker (SpPlaybackIsActiveDevice()), the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Parameters**

\[in]uint8\_t enable0 to disable, 1 to Repeat Context, 2 to Repeat Track The Repeat values where previously called Repeat and Repeat-1.

**Returns**

Returns an error code

**See also**

- [SpPlaybackIsRepeated](#spplaybackisrepeated)

### SpPlaybackCycleRepeatMode()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackCycleRepeatMode(void)`

Cycle through the available repeat modes.

Cycles through repeat modes (repeat off, repeat context, repeat track) given their current availability. If for example repeat context is enabled and repeat track is disallowed due to restrictions, this API will go directly to repeat off.

**Returns**

Returns an error code.

### SpPlaybackSetBitrate()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSetBitrate(enum SpPlaybackBitrate bitrate)`

Change the bitrate at which compressed audio data is delivered.

This will take effect for the next chunk of audio data that is streamed from the backend. The format or sample rate of the audio data that is received does not change.

**Parameters**

**Returns**

Returns an error code

### SpPlaybackSetAvailableToPlay()

[Return to Main functions](#main-functions)

**This function is deprecated and should not be used. See alternatives:**

- [SpPlaybackSetDeviceInactive](#spplaybacksetdeviceinactive)
- [SpPlaybackSetDeviceControllable](#spplaybacksetdevicecontrollable)

`1`

`SpError SpPlaybackSetAvailableToPlay(uint8_t can_play)`

Allow or disallow the device to start playback.

On some platforms, there might be certain situations in which playback should be disallowed temporarily. In this case, when the user tries to start playback on the device using the mobile application, the device should be marked as "Unavailable for playback" in the UI.

**Parameters**

\[in]uint8\_t can\_play2 to allow playback (default), 1 to disallow playback without becoming inactive, the playback will be paused, 0 to disallow playback and become inactive.

**See also**

- [SpPlaybackIsAvailableToPlay](#spplaybackisavailabletoplay)

**Notes:**

- This functionality is reserved for specific integration scenarios. In most cases, when integrating the SDK into a device, this API must not be used. If the device is unable to play (for example, if a firmware upgrade is about to be performed), the application shall log out, shut down the library, and stop announcing the device via the ZeroConf.)
- If the device is currently the active device when setting can\_play to 0, the notification [kSpPlaybackNotifyBecameInactive](#spplaybacknotification) will be sent. Playback-related APIs (SpPlaybackPlay(), ...) will return an error code. This setting will persist across logout/login.

### SpPlaybackIsAvailableToPlay()

[Return to Main functions](#main-functions)

**This function is deprecated and should not be used. See alternatives:**

- [SpPlaybackIsDeviceControllable](#spplaybackisdevicecontrollable)

`1`

`uint8_t SpPlaybackIsAvailableToPlay(void)`

Is the device available for playback.

**Returns**

1: The device is available for playback 0: The device can't accept playback request nor start playback either.

**See also**

- [SpPlaybackSetAvailableToPlay](#spplaybacksetavailabletoplay)

### SpPlaybackSetDeviceInactive()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSetDeviceInactive(void)`

Set the device inactive.

If the device is currently the active device, this function stops the playback if playing, sets the device inactive, and sends the notification [kSpPlaybackNotifyBecameInactive](#spplaybacknotification) If the device is already inactive, the error code [kSpErrorNotActiveDevice](#sperror) is returned.

**Returns**

Returns an error code

**See also**

- [SpPlaybackIsActiveDevice](#spplaybackisactivedevice)

**Notes:**

- The device gets active and starts playing when integration calls [SpPlaybackPlay](#spplaybackplay) or [SpPlayUri](#spplayuri)

### SpPlaybackIsDeviceControllable()

[Return to Main functions](#main-functions)

`1`

`uint8_t SpPlaybackIsDeviceControllable(void)`

Is the device controllable.

**Returns**

1: The device is controllable. 0: The device is not controllable so can't accept playback request nor start playback either.

### SpPlaybackSetDeviceControllable()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSetDeviceControllable(uint8_t is_controllable)`

Allow or disallow the device to be controllable.

On some platforms, there might be certain situations in which the control of the playback should be disallowed temporarily. In this case, when the user tries to start playback on the device using the mobile application, the device should be marked as "Unavailable for playback" in the UI.

**Parameters**

\[in]uint8\_t is\_controllableWhen set to 0 eSDK will pause the playback and won't accept local and remote playback commands, the device gets grayed off in the picker. Set to 1 to allow device control, eSDK will accept both local and remote playback commands and the device becomes available in the picker.

**Returns**

Returns an error code

**See also**

- [SpPlaybackIsDeviceControllable](#spplaybackisdevicecontrollable)

**Notes:**

- This functionality is reserved for specific integration scenarios. It can be used to temporarily disallow playback when for example playing cutscenes in video games or taking a phone call while driving a car. This API should not be used if the device is unable to play (for example, if a firmware upgrade is about to be performed), the application shall then instead log out, shut down the library, and stop announcing the device via the ZeroConf.

### SpPlaybackIncreaseUnderrunCount()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackIncreaseUnderrunCount(uint32_t count)`

Increase the underrun counter of the current track.

If playback underruns have been detected in the current track, use this API to report it to eSDK. This should only be called when there was no data to play at all and there was a audible glitch or gap for the user. It should only be called if audio was expected to be played and there was audio before. For example if eSDK is active and playing, but there is an underrun, report it. If eSDK is active and was requested to play something, but it never started, do not report it. If eSDK is active and playing and user skips, there is an expected gap, so report an underrun only if audio data started being delivered from eSDK and then stopped.

**Parameters**

\[in]`uint32_t` countA counter of how many underruns happened. Some audio stacks have only a getUnderrunCount, so more than one could have occurred since the last one.

**Returns**

Returns an error code

### SpPlaybackSetBandwidthLimit()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSetBandwidthLimit(uint32_t max_bytes_per_sec)`

Set a limit on the download speed.

By calling this function eSDK will attempt to limit how fast it downloads a track. In some use cases it is preferred to not use the full bandwidth. At the beginning of a download eSDK will do a burst download and then try to obey the limit.

**Parameters**

\[in]`uint32_t` max\_bytes\_per\_secapproximate bandwidth budget for downloads. To use default bandwidth specify 0.

**Returns**

Returns an error code

**Notes:**

- eSDK is not guaranteed to stay strictly below the limit but will not exceed it by much It is also not guaranteed to use all available bandwidth.

### SpPlaybackSetRedeliveryMode()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlaybackSetRedeliveryMode(SpReDeliveryMode mode)`

Activates redelivery of audio data on play or resume playback.

This function should be called to activate or deactivate audio redelivery for the next calls to [SpPlaybackPlay](#spplaybackplay) When the client application can't keep unplayed audio in its playback buffers (for example when audio from some other source was played while Spotify was paused) the eSDK should be notified that redelivery of audio data is needed. The audio data is redelivered from the last playback position reported by the integration with the same precision as seek. eSDK will need to redownload the data that was already delivered to integration and therefore there will be a penalty of increased data consumption and latencies. Only use this function when unplayed audio is discarded.

**Returns**

Returns an error code

### SpPlaybackIsRedeliveryModeActivated()

[Return to Main functions](#main-functions)

`1`

`SpReDeliveryMode SpPlaybackIsRedeliveryModeActivated(void)`

Gets the status of redelivery mode.

When redelivery mode is activated or deactivated through the API SpPlaybackSetRedeliveryMode, an internal state is updated to keep track of the redelivery behavior. This API exposes this internal state.

**Returns**

Returns redelivery mode status: kSpRedeliveryModeActivated or kSpRedeliveryModeDeactivated

### SpPresetSubscribe()

[Return to Main functions](#main-functions)

`1`

`SpError SpPresetSubscribe(int preset_id, uint8_t *buffer, size_t buff_size)`

Subscribe to receive "preset" tokens for use with [SpPlayPreset](#spplaypreset)

This function subscribes to receive periodic "preset" tokens that represent the currently playing context. They can be used to resume from the current context and position with [SpPlayPreset](#spplaypreset) This allows implementation of presets, which can be mapped to physical or virtual buttons, to allow users to save their favorite contexts for quick access. The tokens must be saved to persistent storage and be maintained across power cycles. [SpPresetSubscribe](#sppresetsubscribe) must be provided a buffer to store the preset tokens in. This buffer must be a pointer to valid, writeable memory until the callback is unregistered with [SpPresetUnsubscribe](#sppresetunsubscribe) [SpConnectionLogout](#spconnectionlogout) or [SpFree](#spfree) or whenever the playing context changes. The tokens are delivered asynchronously via the [SpCallbackSavePreset](#spcallbacksavepreset) callback, which must be registered with [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks) prior to calling [SpPresetSubscribe](#sppresetsubscribe) Each time the [SpCallbackSavePreset](#spcallbacksavepreset) callback is called, any previously saved token for the current preset must be discarded and replaced with the updated value.

**Parameters**

\[in]`int` preset\_idAn integer indicating which preset this subscription is for. For products with numbered presets, this should match the number of the preset button. For use-cases with no integer mapping, this should be specified as -1.\[in]uint8\_t * bufferPointer to a buffer that will be filled with the preset tokens. This must be a valid memory location until the preset is unregistered.\[in]size\_t buff\_sizeInput: buff\_size specifies the size of the buffer pointed to by buffer. The buffer should be big enough to hold [SP\_PRESET\_BUFFER\_SIZE](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_preset_buffer_size) bytes.

**Returns**

Returns an error code

**Notes:**

- The buffer passed to [SpPresetSubscribe](#sppresetsubscribe) must be SP\_PRESET\_BUFFER\_SIZE, but the actual preset tokens received from the [SpCallbackSavePreset](#spcallbacksavepreset) callback will typically be much smaller.
- A subscription is only for the currently playing context, and only one subscription is possible at a time.
- At times, some contexts may not be possible to save as presets. Errors will be indicated via the [SpCallbackSavePreset](#spcallbacksavepreset) callback.

### SpPresetUnsubscribe()

[Return to Main functions](#main-functions)

`1`

`SpError SpPresetUnsubscribe(void)`

Unsubscribe from a previously subscribed preset.

[SpPresetUnsubscribe](#sppresetunsubscribe) unsubscribes from receiving preset callbacks. This is the opposite of [SpPresetSubscribe](#sppresetsubscribe) After calling this function, the memory buffer provided to [SpPresetSubscribe](#sppresetsubscribe) is released by eSDK and can be deallocated.

**Returns**

Returns an error code

### SpPlayPreset()

[Return to Main functions](#main-functions)

`1`

`SpError SpPlayPreset(int preset_id, uint32_t playback_position, uint8_t *buffer, size_t buff_size, int alias_index)`

Recall and play a saved or default preset.

[SpPlayPreset](#spplaypreset) accepts a preset token that was previously received from using [SpPresetSubscribe](#sppresetsubscribe) restores the context and playback state to as it was when the token was saved, and starts playback. For default user-recommended playlists, [SpPlayPreset](#spplaypreset) can be used with buffer set to NULL. Spotify will pick a default playlist to play based on popularity and user recommendations. The correct preset\_id should still be provided to guarantee a good mixture of recommended playlists. Default presets do not require subscribing with [SpPresetSubscribe](#sppresetsubscribe) Integrations should always use [SpPresetSubscribe](#sppresetsubscribe) to subscribe to token updates in conjunction with using [SpPlayPreset](#spplaypreset)

**Parameters**

\[in]`int` preset\_idAn integer indicating which preset this token is for. For products with numbered presets, this should match the number of the preset button, starting from 1. For use-cases with no integer mapping, this should be specified as -1.\[in]`uint32_t` playback\_positionThe playback position specified with the preset token from the [SpCallbackSavePreset](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spcallbacksavepreset) callback.\[in]uint8\_t * bufferPreset blob obtained with [SpPresetSubscribe](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sppresetsubscribe) or NULL to play a default user-recommended playlist.\[in]size\_t buff\_sizeThe size of buffer, or 0 if buffer is NULL.\[in]`int` alias\_indexThe index of the device alias to start playback on. If aliases aren't used, pass -1.

**Returns**

Returns an error code

### SpZeroConfGetVars()

[Return to Main functions](#main-functions)

`1`

`SpError SpZeroConfGetVars(struct SpZeroConfVars *vars)`

Get variables for ZeroConf, mainly the "getInfo" request.

The application should use this function to retrieve the data that it should send in the response to the "getInfo" request. See the ZeroConf manual for more information. There are also other fields here that might be needed for ZeroConf.

**Parameters**

\[out]`struct` [SpZeroConfVars](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spzeroconfvars) * varsStructure to be filled with the variables

**Notes:**

- This API can be invoked from a callback.

### SpZeroConfAnnouncePause()

[Return to Main functions](#main-functions)

`1`

`SpError SpZeroConfAnnouncePause(void)`

Temporarily pause ZeroConf mDNS annoucements.

**Returns**

Returns an error code

**Notes:**

- This call requries ZeroConf to be started (by setting [SpConfig::zeroconf\_serve](#spconfig) when calling [SpInit](#spinit)

### SpZeroConfAnnounceResume()

[Return to Main functions](#main-functions)

`1`

`SpError SpZeroConfAnnounceResume(void)`

Resume ZeroConf mDNS annoucement after calling [SpZeroConfAnnouncePause](#spzeroconfannouncepause)

**Returns**

Returns an error code

**Notes:**

- This call requries ZeroConf to be started (by setting [SpConfig::zeroconf\_serve](#spconfig) when calling [SpInit](#spinit)

### SpConnectionLoginZeroConf()

[Return to Main functions](#main-functions)

`1`

`SpError SpConnectionLoginZeroConf(const char *username, const char *zero_conf_blob, const char *client_key, const char *login_id, const char *token_type)`

Log in a user to Spotify using a ZeroConf credentials blob.

This function logs in with the information that the application receives in the "addUser" ZeroConf request. See the ZeroConf manual.

**Parameters**

\[in]`const` `char` * usernameSpotify username. UTF-8 encoded. Must not be longer than [SP\_MAX\_USERNAME\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_username_length) bytes (not UTF-8-encoded characters), not counting the terminating NULL.\[in]`const` `char` * zero\_conf\_blobCredentials blob from the "blob" field of the request. Must not be longer than [SP\_MAX\_ZEROCONF\_BLOB\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_zeroconf_blob_length) bytes, not counting the terminating NULL.\[in]`const` `char` * client\_keyClient key from the "clientKey" field of the request. This may be NULL if not supplied in the "addUser" request. Must not be longer than [SP\_MAX\_CLIENT\_KEY\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_client_key_length) bytes, not counting the terminating NULL.\[in]`const` `char` * login\_idLogin ID from the "loginId" field of the request. This may be NULL if not supplied in the "addUser" request. Must not be longer than [SP\_MAX\_LOGIN\_ID\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_login_id_length) bytes, not counting the terminating NULL.\[in]`const` `char` * token\_typeToken type from the "tokenType" field of the request. This may be NULL if not supplied in the "addUser" request. Must not be longer than [SP\_MAX\_TOKEN\_TYPE\_LENGTH](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_max_token_type_length) bytes, not counting the terminating NULL.

**Returns**

Returns an error code

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:

### SpGetBrandName()

[Return to Main functions](#main-functions)

`1`

`const char * SpGetBrandName(void)`

This function can be used to get the brand name. If the field [SpConfig::brand\_display\_name](#spconfig) was set at [SpInit](#spinit) it returns that, otherwise it returns what was set in the mandatory field [SpConfig::brand\_name](#spconfig)

**Returns**

The UTF-8-encoded brand name

**Notes:**

- This API can be invoked from a callback.

### SpGetModelName()

[Return to Main functions](#main-functions)

`1`

`const char * SpGetModelName(void)`

This function can be used to get the model name. If the field [SpConfig::model\_display\_name](#spconfig) was set at [SpInit](#spinit) it returns that, otherwise it returns what was set in the mandatory field [SpConfig::model\_name](#spconfig)

**Returns**

The UTF-8-encoded model name

**Notes:**

- This API can be invoked from a callback.

### SpRegisterDeviceAliasCallbacks()

[Return to Main functions](#main-functions)

`1`

`SpError SpRegisterDeviceAliasCallbacks(struct SpDeviceAliasCallbacks *cb, void *context)`

Register callbacks related to device aliases.

**Parameters**

\[in]`struct` [SpDeviceAliasCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdevicealiascallbacks) * cbStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

### SpSetDeviceAliases()

[Return to Main functions](#main-functions)

`1`

`SpError SpSetDeviceAliases(const struct SpDeviceAlias *aliases)`

Update the device alias definitions.

Call this whenever the current alias definitions are updated. The id values for the aliases must be unique within the array. aliases Pointer to an array of [SpDeviceAlias](#spdevicealias) structs filled in with the new alias names and corresponding attributes. The array size must be of size SP\_MAX\_DEVICE\_ALIASES.

**Parameters**

\[in]`const` `struct` [SpDeviceAlias](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdevicealias) * aliasesPointer to an array of [SpDeviceAlias](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdevicealias) structs filled in with the new alias names and corresponding attributes. The array size must be of size SP\_MAX\_DEVICE\_ALIASES.

### SpRestrictDrmMediaFormats()

[Return to Main functions](#main-functions)

`1`

`SpError SpRestrictDrmMediaFormats(const struct SpFormat formats[SP_MAX_SUPPORTED_FORMATS])`

Restricts the list of DRM and media formats to a subset of the formats registered in [SpInit](#spinit) To lift the restrictions use [SpRestoreDrmMediaFormats](#sprestoredrmmediaformats)

**See also**

- [SpInit](#spinit)
- [SpConfig::supported\_drm\_media\_formats](#spconfig)

### SpRestoreDrmMediaFormats()

[Return to Main functions](#main-functions)

`1`

`SpError SpRestoreDrmMediaFormats(void)`

Resets the list of DRM formats and media formats to the ones registered in [SpInit](#spinit)

**See also**

- [SpFormat](#spformat)

## Content

* * *

`1`

`#include "spotify_embedded_content.h"`

- [Data Structures](#content-data-structures)
- [Typedefs](#content-typedefs)
- [Enumerations](#content-enumerations)
- [Functions](#content-functions)

## Data Structures

* * *

[Return to header index](#content)

[SpContentCallbacks](#spcontentcallbacks) Callbacks to be registered with SpRegisterContentCallbacks

## Typedefs

* * *

[Return to header index](#content)

[SpCallbackTrackCacheState](#spcallbacktrackcachestate) This callback if set by client is called by eSDK to inform the client about how much data is actually cached for particular track starting from the beginning in percents. For example is 60 reported it mean 60% of the track is cached started from the beginning.[SpCallbackStorageKeyContentMapping](#spcallbackstoragekeycontentmapping) This callback if set by client is called by eSDK to notify the client how storage\_key used to store the data through Storage API is mapped to particular content being stored. SpContentType is used to specify exact content type. For example: hint being equal to kSpContentTrack means descriptor would be in form of: spotify:track:\[base62].[SpCallbackTrackRelinked](#spcallbacktrackrelinked) This callback if set by client is called by eSDK to notify the client about the fact that requested track is substituted with another (relinked) one during prefetch/offline process.[SpCallbackTrackRemoved](#spcallbacktrackremoved) This callback if set by client is called by eSDK to notify the client that the track is removed.[SpCallbackOnAvailableContainer](#spcallbackonavailablecontainer) Callback for each available container.

## Enumerations

* * *

[Return to header index](#content)

## Functions

* * *

[Return to header index](#content)

## Data Structures

* * *

### SpContentCallbacks

[Return to Content data structures](#content-data-structures)

Callbacks to be registered with [SpRegisterContentCallbacks](#spregistercontentcallbacks)

Any of the pointers may be NULL.

**Notes:**

- See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpContentCallbacks {`

`2`

`SpCallbackTrackCacheState track_state_callback;`

`3`

`SpCallbackStorageKeyContentMapping store_key_map_callback;`

`4`

`SpCallbackTrackRelinked track_relink_callback;`

`5`

`SpCallbackTrackRemoved track_removed_callback;`

`6`

`SpCallbackOnAvailableContainer on_available_container;`

`7`

`};`

[SpCallbackTrackCacheState](#spcallbacktrackcachestate) track\_state\_callbackTrack cached state callback.[SpCallbackStorageKeyContentMapping](#spcallbackstoragekeycontentmapping) store\_key\_map\_callbackContent mapping callback.[SpCallbackTrackRelinked](#spcallbacktrackrelinked) track\_relink\_callbackNotify about track relink during prefetch/offline.[SpCallbackTrackRemoved](#spcallbacktrackremoved) track\_removed\_callbackNotify about track removal.[SpCallbackOnAvailableContainer](#spcallbackonavailablecontainer) on\_available\_containerNotify about an available container item.

## Typedefs

* * *

### SpCallbackTrackCacheState()

[Return to Content Typedefs](#content-typedefs)

`1`

`typedef void(* SpCallbackTrackCacheState)(const char *track_uri, uint32_t percents, void *context)`

This callback if set by client is called by eSDK to inform the client about how much data is actually cached for particular track starting from the beginning in percents. For example is 60 reported it mean 60% of the track is cached started from the beginning.

**Parameters**

\[in]`const` `char` * track\_uriTrack URI which status is reported.\[in]`uint32_t` percentsHow much data is cached in percent. Range: \[0 - 100%]\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback. This callback is called before each track delivery is started.

### SpCallbackStorageKeyContentMapping()

[Return to Content Typedefs](#content-typedefs)

`1`

`typedef void(* SpCallbackStorageKeyContentMapping)(const char *storage_key, const char *descriptor, enum SpContentType hint, void *context)`

This callback if set by client is called by eSDK to notify the client how storage\_key used to store the data through Storage API is mapped to particular content being stored. [SpContentType](#spcontenttype) is used to specify exact content type. For example: hint being equal to [kSpContentTrack](#spcontenttype) means descriptor would be in form of: spotify:track:\[base62].

**Parameters**

\[in]`const` `char` * storage\_keyStorage key that was used in Alloc/Read/Write API.\[in]`const` `char` * descriptorContent descriptor. Value depends on hint.

**See also**

- [SpContentType](#spcontenttype)

**Notes:**

- The application should not block or call other API functions in the callback. This callback is called as soon as possible after Alloc callback of Storage API has been called and succeeds.

### SpCallbackTrackRelinked()

[Return to Content Typedefs](#content-typedefs)

`1`

`typedef void(* SpCallbackTrackRelinked)(const char *original_uri, const char *new_uri, void *context)`

This callback if set by client is called by eSDK to notify the client about the fact that requested track is substituted with another (relinked) one during prefetch/offline process.

**Parameters**

\[in]`const` `char` * original\_uriInitial URI passed into eSDK PrefetchURI/OfflineURI function calls.\[in]`const` `char` * new\_uriURI that is obtained after relink has happened.\[in]`void` * contextContext provided in callback register procedure.

### SpCallbackTrackRemoved()

[Return to Content Typedefs](#content-typedefs)

`1`

`typedef void(* SpCallbackTrackRemoved)(const char *track_uri, void *context)`

This callback if set by client is called by eSDK to notify the client that the track is removed.

track\_uri URI passed into eSDK PlayURI/PrefetchURI/OfflineURI function calls. context Context provided in callback register procedure.

**Parameters**

\[in]`const` `char` * track\_uriURI passed into eSDK PlayURI/PrefetchURI/OfflineURI function calls.\[in]`void` * contextContext provided in callback register procedure.

### SpCallbackOnAvailableContainer()

[Return to Content Typedefs](#content-typedefs)

`1`

`typedef void(* SpCallbackOnAvailableContainer)(const char *uri, int total, void *context)`

Callback for each available container.

**Parameters**

\[in]`const` `char` * uriURI of a container\[in]`int` totalTotal number of containers\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- Experimental, subject of change

## Enumerations

* * *

### SpContentType

[Return to Content enumerations](#content-enumerations)

`1`

`enum SpContentType {`

`2`

`kSpContentTrack,`

`3`

`kSpContentTrackMetadata,`

`4`

`};`

kSpContentTrackContent pointed by descriptor is spotify playable item URI (track or episode)kSpContentTrackMetadataContent pointed by descriptor is spotify playable item URI for which metadata is saved.

## Functions

* * *

### SpRegisterContentCallbacks()

[Return to Content functions](#content-functions)

`1`

`SpError SpRegisterContentCallbacks(struct SpContentCallbacks *callbacks, void *context)`

**Parameters**

\[in]`struct` [SpContentCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spcontentcallbacks) * callbacksStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

## Hal

* * *

`1`

`#include "spotify_embedded_hal.h"`

- [Data Structures](#hal-data-structures)
- [Typedefs](#hal-typedefs)
- [Enumerations](#hal-enumerations)
- [Functions](#hal-functions)

## Data Structures

* * *

[Return to header index](#hal)

[SpSockaddr](#spsockaddr) Struct contains resolved hostname ip address and its family.[SpDnsHALCallbacks](#spdnshalcallbacks) Callbacks to be registered with SpRegisterDnsHALCallbacks[SpSocketHandle](#spsockethandle) Socket handle type.[SpSocketHALCallbacks](#spsockethalcallbacks) Callbacks to be registered with SpRegisterSocketHALCallbacks

## Typedefs

* * *

[Return to header index](#hal)

[SpCallbackPerformDNSLookup](#spcallbackperformdnslookup) This callback if set by client is called by eSDK to perform DNS lookup. If expected that lookup could take significant amount of time client may do it asynchronously in which case value of kSpAPITryAgain could be returned.[SpCallbackSocketCreate](#spcallbacksocketcreate) This callback if set by client is called by eSDK to create socket of certain type and family.[SpCallbackSocketSetOption](#spcallbacksocketsetoption) This callback if set by client is called by eSDK to set specific options on previously created socket.[SpCallbackSocketClose](#spcallbacksocketclose) This callback if set by client is called by eSDK to close previously opened socket.[SpCallbackSocketBind](#spcallbacksocketbind) This callback if set by client is called by eSDK to bind to provided socket.[SpCallbackSocketListen](#spcallbacksocketlisten) This callback if set by client is called by eSDK to start listening provided socket. This callbacks has no effect on UPD sockets.[SpCallbackSocketConnect](#spcallbacksocketconnect) This callback if set by client is called by eSDK to connect to specified host and remote port.[SpCallbackSocketAccept](#spcallbacksocketaccept) This callback if set by client is called by eSDK to accept connection on provided socket.[SpCallbackSocketRead](#spcallbacksocketread) This callback if set by client is called by eSDK to read the data from socket.[SpCallbackSocketWrite](#spcallbacksocketwrite) This callback if set by client is called by eSDK to write data to socket.[SpCallbackSocketReadFrom](#spcallbacksocketreadfrom) This callback if set by client is called by eSDK to read the data from socket addressed by SpSockaddr instance.[SpCallbackSocketWriteTo](#spcallbacksocketwriteto) This callback if set by client is called by eSDK to write data to socket addressed by SpSockaddr instance.[SpCallbackSocketError](#spcallbacksocketerror) This callback if set by client is called by eSDK to get underlying OS error code.[SpCallbackSocketReadable](#spcallbacksocketreadable) This callback if set by client is called by eSDK to figure out if socket is readable.[SpCallbackSocketWriteable](#spcallbacksocketwriteable) This callback if set by client is called by eSDK to figure out if socket is writable.[SpCallbackLocalAddresses](#spcallbacklocaladdresses) This callback if set by client is called by eSDK to get local interface addresses. If the clent can't get local interfaces implementation should fill provided \*num\_addrs with 0.[SpCallbackSocketAddress](#spcallbacksocketaddress) This callback if set by client is called by eSDK to provide platform defined representation of address that can be used in SpCallbackSocketReadFrom and SpCallbackSocketWriteTo Client responsible for providing returned pointer lifetime.[SpCallbackPump](#spcallbackpump) This callback if set by client is called by eSDK to pump network layer.

## Enumerations

* * *

[Return to header index](#hal)

## Functions

* * *

[Return to header index](#hal)

[SpRegisterDnsHALCallbacks](#spregisterdnshalcallbacks) Register HAL-related callbacks. Should be called right after SpInit[SpGetDefaultDnsHALCallbacks](#spgetdefaultdnshalcallbacks) Get eSDK's default DNS callbacks.[SpRegisterSocketHALCallbacks](#spregistersockethalcallbacks) Register socket HAL-related callbacks. To remove callbacks call SpRegisterSocketHALCallbacks with SpSocketHALCallbacks initialized to zeros.[SpGetDefaultSocketHALCallbacks](#spgetdefaultsockethalcallbacks) Get eSDK's default socket callbacks.

## Data Structures

* * *

### SpSockaddr

[Return to Hal data structures](#hal-data-structures)

Struct contains resolved hostname ip address and its family.

`1`

`struct SpSockaddr {`

`2`

`enum SpIPFamily family;`

`3`

`uint8_t addr;`

`4`

`int port;`

`5`

`};`

*enum* [SpIPFamily](#spipfamily) familyIP protocol family for which lookup is requested.uint8\_t addrIp address. Network byte order.*int* portContains port value if applicable. Host byte order.

### SpDnsHALCallbacks

[Return to Hal data structures](#hal-data-structures)

Callbacks to be registered with [SpRegisterDnsHALCallbacks](#spregisterdnshalcallbacks)

Any of the pointers may be NULL. To remove DNS callback at any time call [SpRegisterDnsHALCallbacks](#spregisterdnshalcallbacks) with [SpDnsHALCallbacks](#spdnshalcallbacks) which has dns\_lookup\_callback set to NULL.

**Notes:**

- See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpDnsHALCallbacks {`

`2`

`SpCallbackPerformDNSLookup dns_lookup_callback;`

`3`

`};`

[SpCallbackPerformDNSLookup](#spcallbackperformdnslookup) dns\_lookup\_callbackDNS lookup callback. If NULL eSDK will use its internal DNS resolve mechanism.

### SpSocketHandle

[Return to Hal data structures](#hal-data-structures)

Socket handle type.

`1`

`struct SpSocketHandle {`

`2`

`void *handle;`

`3`

`void *tls;`

`4`

`};`

*void* * handleClient defined socket representation.*void* * tlsCan be used by the TLS implementation to store connection specific state.

### SpSocketHALCallbacks

[Return to Hal data structures](#hal-data-structures)

Callbacks to be registered with [SpRegisterSocketHALCallbacks](#spregistersockethalcallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpSocketHALCallbacks {`

`2`

`SpCallbackSocketCreate socket_create;`

`3`

`SpCallbackSocketSetOption socket_set_option;`

`4`

`SpCallbackSocketClose socket_close;`

`5`

`SpCallbackSocketBind socket_bind;`

`6`

`SpCallbackSocketListen socket_listen;`

`7`

`SpCallbackSocketConnect socket_connect;`

`8`

`SpCallbackSocketAccept socket_accept;`

`9`

`SpCallbackSocketRead socket_read;`

`10`

`SpCallbackSocketWrite socket_write;`

`11`

`SpCallbackSocketReadFrom socket_read_from;`

`12`

`SpCallbackSocketWriteTo socket_write_to;`

`13`

`SpCallbackSocketError socket_error;`

`14`

`SpCallbackSocketReadable socket_readable;`

`15`

`SpCallbackSocketWriteable socket_writable;`

`16`

`SpCallbackLocalAddresses local_addresses;`

`17`

`SpCallbackSocketAddress socket_address;`

`18`

`SpCallbackPump on_pump;`

`19`

`};`

[SpCallbackSocketCreate](#spcallbacksocketcreate) socket\_createCallback to create socket instance.[SpCallbackSocketSetOption](#spcallbacksocketsetoption) socket\_set\_optionCallback to set options on created socket.[SpCallbackSocketClose](#spcallbacksocketclose) socket\_closeCallback to close the socket.[SpCallbackSocketBind](#spcallbacksocketbind) socket\_bindCallback to bind to socket.[SpCallbackSocketListen](#spcallbacksocketlisten) socket\_listenCallback to start listening the socket.[SpCallbackSocketConnect](#spcallbacksocketconnect) socket\_connectCallback to connect to socket.[SpCallbackSocketAccept](#spcallbacksocketaccept) socket\_acceptCallback to accept connection on socket.[SpCallbackSocketRead](#spcallbacksocketread) socket\_readCallback to read data from socket.[SpCallbackSocketWrite](#spcallbacksocketwrite) socket\_writeCallback to write data to socket.[SpCallbackSocketReadFrom](#spcallbacksocketreadfrom) socket\_read\_fromCallback to read data from socket pointed by address.[SpCallbackSocketWriteTo](#spcallbacksocketwriteto) socket\_write\_toCallback to write data to socket pointed by address.[SpCallbackSocketError](#spcallbacksocketerror) socket\_errorCallback to get OS error on socket.[SpCallbackSocketReadable](#spcallbacksocketreadable) socket\_readableCallback to get readable state on socket.[SpCallbackSocketWriteable](#spcallbacksocketwriteable) socket\_writableCallback to get writable state on socket.[SpCallbackLocalAddresses](#spcallbacklocaladdresses) local\_addressesCallback to get local interface addresses.[SpCallbackSocketAddress](#spcallbacksocketaddress) socket\_addressCallback to platform address representation.[SpCallbackPump](#spcallbackpump) on\_pumpCallback to pump network layer.

## Typedefs

* * *

### SpCallbackPerformDNSLookup()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackPerformDNSLookup)(const char *hostname, struct SpSockaddr *sockaddr, void *context)`

This callback if set by client is called by eSDK to perform DNS lookup. If expected that lookup could take significant amount of time client may do it asynchronously in which case value of [kSpAPITryAgain](#spapireturncode) could be returned.

**Parameters**

\[in]`const` `char` * hostnameName to be resolved.\[in]`struct` [SpSockaddr](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockaddr) * sockaddrPointer to [SpSockaddr](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockaddr) structure.

**See also**

- [SpAPIReturnCode](#spapireturncode)
- [SpSockaddr](#spsockaddr)
- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The application should not block or call other API functions in the callback. Port value of [SpSockaddr](#spsockaddr) is ignored.

### SpCallbackSocketCreate()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketCreate)(enum SpIPFamily family, enum SpSocketType type, enum SpSocketPool pool_id, struct SpSocketHandle **socket, void *context)`

This callback if set by client is called by eSDK to create socket of certain type and family.

**Parameters**

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketSetOption()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketSetOption)(struct SpSocketHandle *socket, enum SpSocketOptions option, void *value, void *context)`

This callback if set by client is called by eSDK to set specific options on previously created socket.

**Parameters**

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketClose()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketClose)(struct SpSocketHandle *socket, void *context)`

This callback if set by client is called by eSDK to close previously opened socket.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketBind()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketBind)(struct SpSocketHandle *socket, int *port, void *context)`

This callback if set by client is called by eSDK to bind to provided socket.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`int` * portPort which eSDK would listen to (host byte order). If (\*port) is zero, the bound port should be stored in (\*port).\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketListen()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketListen)(struct SpSocketHandle *socket, int backlog, void *context)`

This callback if set by client is called by eSDK to start listening provided socket. This callbacks has no effect on UPD sockets.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`int` backlogParameter defines the maximum length for the queue of pending connections.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketConnect()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketConnect)(struct SpSocketHandle *socket, const struct SpSockaddr *addr, void *context)`

This callback if set by client is called by eSDK to connect to specified host and remote port.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`const` `struct` [SpSockaddr](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockaddr) * addrAddress to connect to.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketAccept()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketAccept)(struct SpSocketHandle *socket, enum SpSocketPool pool_id, struct SpSocketHandle **out_socket, void *context)`

This callback if set by client is called by eSDK to accept connection on provided socket.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) \*\*out_ socketSocket instance to perform action with.\[in]`enum` [SpSocketPool](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsocketpool) pool\_idSocket pool ID to create the new socket from\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) \** out\_socketSocket created by accepting connection.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketRead()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketRead)(struct SpSocketHandle *socket, void *data, int data_size, int *bytes_read, void *context)`

This callback if set by client is called by eSDK to read the data from socket.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`void` * dataBuffer to read data into.\[in]`int` data\_sizeAmount of requested data to read.\[in]`int` * bytes\_readPointer to store how much bytes actually read. If NULL, read is still performed. Should be unchanged if read failed.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketWrite()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketWrite)(struct SpSocketHandle *socket, const void *data, int data_size, int *bytes_written, void *context)`

This callback if set by client is called by eSDK to write data to socket.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`const` `void` * dataBuffer with data to be written.\[in]`int` data\_sizeAmount of data to write.\[in]`int` * bytes\_writtenPointer to store how much bytes actually written. If NULL, write is still performed. Should unchanged if write failed.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketReadFrom()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketReadFrom)(struct SpSocketHandle *socket, void *data, int data_size, const void **addr, int *bytes_read, void *context)`

This callback if set by client is called by eSDK to read the data from socket addressed by [SpSockaddr](#spsockaddr) instance.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`void` * dataBuffer to read data into.\[in]`int` data\_sizeAmount of requested data to read.\[in]`const` `void` \** addrPlatform defined addr pointer. eSDK does not modify it. Just pass through to write\_to.\[in]`int` * bytes\_readPointer to store how much bytes actually read. If NULL, read is still performed. Should be unchanged if read failed.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback. This callback should mirror the behavior of recvfrom for connected/non-connected sockets.

### SpCallbackSocketWriteTo()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackSocketWriteTo)(struct SpSocketHandle *socket, const void *data, int data_size, const void *addr, int *bytes_written, void *context)`

This callback if set by client is called by eSDK to write data to socket addressed by [SpSockaddr](#spsockaddr) instance.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`const` `void` * dataBuffer with data to be written.\[in]`int` data\_sizeAmount of data to write.\[in]`const` `void` * addrPointer received in the call to [SpCallbackSocketReadFrom](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spcallbacksocketreadfrom)\[in]`int` * bytes\_writtenPointer to store how much bytes actually written. If NULL, write is still performed. Should unchanged if write failed.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback. This callback should mirror the behavior of writeto for connected/non-connected sockets.

### SpCallbackSocketError()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef int(* SpCallbackSocketError)(struct SpSocketHandle *socket, void *context)`

This callback if set by client is called by eSDK to get underlying OS error code.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance for which error code is requested.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketReadable()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef int(* SpCallbackSocketReadable)(struct SpSocketHandle *socket, void *context)`

This callback if set by client is called by eSDK to figure out if socket is readable.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketWriteable()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef int(* SpCallbackSocketWriteable)(struct SpSocketHandle *socket, void *context)`

This callback if set by client is called by eSDK to figure out if socket is writable.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketSocket instance to perform action with.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackLocalAddresses()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef void(* SpCallbackLocalAddresses)(struct SpSockaddr *addrs, int *num_addrs, void *context)`

This callback if set by client is called by eSDK to get local interface addresses. If the clent can't get local interfaces implementation should fill provided \*num\_addrs with 0.

**Parameters**

\[in]`int` \*num_ addrsPointer to array of [SpSockaddr](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockaddr) to store the data. Data in network byte order.\[in]`int` * num\_addrsArray size on input, number of items stored in the array on output.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketAddress()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef const void *(* SpCallbackSocketAddress)(const struct SpSockaddr *addr, void *context)`

This callback if set by client is called by eSDK to provide platform defined representation of address that can be used in [SpCallbackSocketReadFrom](#spcallbacksocketreadfrom) and [SpCallbackSocketWriteTo](#spcallbacksocketwriteto) Client responsible for providing returned pointer lifetime.

**Parameters**

\[in]`const` `struct` [SpSockaddr](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockaddr) * addrAddress to convert. Network byte order.\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackPump()

[Return to Hal Typedefs](#hal-typedefs)

`1`

`typedef enum SpCallbackPump)(unsigned max_wait_ms, void *context)`

This callback if set by client is called by eSDK to pump network layer.

**Parameters**

\[in]unsigned max\_wait\_msMaximum time to wait in one pump call\[in]`void` * contextContext provided in callback register procedure.

**Notes:**

- The application should not block or call other API functions in the callback.

## Enumerations

* * *

### SpIPFamily

[Return to Hal enumerations](#hal-enumerations)

`1`

`enum SpIPFamily {`

`2`

`kSpIPV4,`

`3`

`kSpIPV6,`

`4`

`};`

kSpIPV4IP v4 family.kSpIPV6IP v6 family.

### SpSocketPool

[Return to Hal enumerations](#hal-enumerations)

`1`

`enum SpSocketPool {`

`2`

`kSpSocketPoolGeneral,`

`3`

`kSpSocketPoolZeroConf,`

`4`

`};`

kSpSocketPoolGeneralSockets used for backend, streaming, etc.kSpSocketPoolZeroConfSockets used for ZeroConf.

### SpSocketType

[Return to Hal enumerations](#hal-enumerations)

`1`

`enum SpSocketType {`

`2`

`kSpSocketStream,`

`3`

`kSpSocketDgram,`

`4`

`};`

kSpSocketStreamStream socket type.kSpSocketDgramDatagram socket type.

### SpSocketOptions

[Return to Hal enumerations](#hal-enumerations)

`1`

`enum SpSocketOptions {`

`2`

`kSpSocketNonBlocking,`

`3`

`kSpSocketReuseAddr,`

`4`

`kSpSocketReusePort,`

`5`

`kSpSocketMulticastTTL,`

`6`

`kSpSocketMulticastLoop,`

`7`

`kSpSocketMembership,`

`8`

`kSpSocketMcastSendIf,`

`9`

`};`

kSpSocketNonBlockingNonblocking mode has to be set by the implementation if possible. POSIX analog: TCP\_NODELAY.kSpSocketReuseAddrReuse address mode has to be set if possible. POSIX analog: SO\_REUSEADDR. Value 0 or 1.kSpSocketReusePortReuse port mode has to be set if possible. POSIX analog: SO\_REUSEPORT. Value 0 or 1.kSpSocketMulticastTTLMulticast TTL has to be set if possible. POSIX analog: IP\_MULTICAST\_TTL. Value \[0, 255].kSpSocketMulticastLoopMulticast loop has to be set if possible. POSIX analog: IP\_MULTICAST\_LOOP. Value 0 or 1.kSpSocketMembershipSet group address if possible. POSIX analog: IP\_ADD\_MEMBERSHIP. value is pointer SpSockaddr Address is in network byte order. Port field is not applicable.kSpSocketMcastSendIfSet outgoing multicast interface. POSIX analog: IP\_MULTICAST\_IF. value is pointer to SpSockaddr Address is in network byte order. Port field is not applicable.

## Functions

* * *

### SpRegisterDnsHALCallbacks()

[Return to Hal functions](#hal-functions)

`1`

`SpError SpRegisterDnsHALCallbacks(struct SpDnsHALCallbacks *callbacks, void *context)`

Register HAL-related callbacks. Should be called right after [SpInit](#spinit)

**Parameters**

\[in]`struct` [SpDnsHALCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdnshalcallbacks) * callbacksStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code.

**Notes:**

- To remove DNS callback at any time call [SpRegisterDnsHALCallbacks](#spregisterdnshalcallbacks) with [SpDnsHALCallbacks](#spdnshalcallbacks) which has dns\_lookup\_callback set to NULL. Setting DNS callback make sense only if eSDK uses its own socket implementation. If the client provides whole socket API it is also reponsible for hostname resolving if needed. Setting DNS callbacks with provided socket callbacks makes no effect.

### SpGetDefaultDnsHALCallbacks()

[Return to Hal functions](#hal-functions)

`1`

`SpError SpGetDefaultDnsHALCallbacks(struct SpDnsHALCallbacks *callbacks)`

Get eSDK's default DNS callbacks.

**Parameters**

**Returns**

Returns an error code.

**Notes:**

- These callbacks are made available so they may be wrapped by custom DNS functions provided with [SpRegisterDnsHALCallbacks](#spregisterdnshalcallbacks)

### SpRegisterSocketHALCallbacks()

[Return to Hal functions](#hal-functions)

`1`

`SpError SpRegisterSocketHALCallbacks(struct SpSocketHALCallbacks *callbacks, void *context)`

Register socket HAL-related callbacks. To remove callbacks call [SpRegisterSocketHALCallbacks](#spregistersockethalcallbacks) with [SpSocketHALCallbacks](#spsockethalcallbacks) initialized to zeros.

**Parameters**

\[in]`struct` [SpSocketHALCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethalcallbacks) * callbacksStructure with pointers to individual callback functions. Either all pointers are NULL or all are valid.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

**Notes:**

- A call to this function has to be performed before [SpInit](#spinit) is called. Calling this function when eSDK is initialized will fail with [kSpErrorAlreadyInitialized](#sperror)

### SpGetDefaultSocketHALCallbacks()

[Return to Hal functions](#hal-functions)

`1`

`SpError SpGetDefaultSocketHALCallbacks(struct SpSocketHALCallbacks *callbacks, void **context)`

Get eSDK's default socket callbacks.

**Parameters**

**Returns**

Returns an error code.

**Notes:**

- These callbacks are made available so they may be wrapped by custom socket functions provided with [SpRegisterSocketHALCallbacks](#spregistersockethalcallbacks)

## Log

* * *

`1`

`#include "spotify_embedded_log.h"`

- [Macros and Constants](#log-macros-and-constants)
- [Data Structures](#log-data-structures)
- [Enumerations](#log-enumerations)
- [Functions](#log-functions)

## Macros and Constants

* * *

[Return to header index](#log)

[SP\_LOG\_DEFAULT\_LEVEL](#sp_log_default_level) [SP\_LOG\_LEVEL\_INFO](#sploglevel) [SP\_LOG\_DEFINE\_TRACE\_OBJ](#sp_log_define_trace_obj) *struct* [SP\_LOG\_DECLARE\_TRACE\_OBJ](#sp_log_declare_trace_obj) extern *struct* [SP\_LOG\_REGISTER\_TRACE\_OBJ](#sp_log_register_trace_obj) *See macro below* [SP\_LOG](#sp_log) *See macro below* [SpLogFatal](#splogfatal) *See macro below* [SpLogError](#splogerror) *See macro below* [SpLogWarning](#splogwarning) *See macro below* [SpLogInfo](#sploginfo) *See macro below* [SpLogDebug](#splogdebug) *See macro below* [SpLogTrace](#splogtrace) *See macro below*

## Data Structures

* * *

[Return to header index](#log)

[SpLogTraceObject](#splogtraceobject) Trace object.

## Enumerations

* * *

[Return to header index](#log)

## Functions

* * *

[Return to header index](#log)

[SpLogRegisterTraceObject](#splogregistertraceobject) Register a defined trace object with eSDK.[SpLog](#splog) Output a debug message via eSDK.[SpLogSetLevel](#splogsetlevel) Control the current logging level.[SpLogGetLevels](#sploggetlevels) Get registered trace objects and log levels.

## Macros and Constants

* * *

### SP\_LOG\_DEFAULT\_LEVEL

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SP_LOG_DEFAULT_LEVEL SP_LOG_LEVEL_INFO`

Default trace log level.

### SP\_LOG\_DEFINE\_TRACE\_OBJ

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SP_LOG_DEFINE_TRACE_OBJ struct`

Macro to define a trace object.

obj Name of the trace object

### SP\_LOG\_DECLARE\_TRACE\_OBJ

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SP_LOG_DECLARE_TRACE_OBJ extern struct`

Macro to declare a previously defined trace object.

obj Name of the trace object

### SP\_LOG\_REGISTER\_TRACE\_OBJ

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SP_LOG_REGISTER_TRACE_OBJ SpLogRegisterTraceObject(&trace_obj_##obj)`

Macro to register a previously defined trace object.

obj Name of the trace object

### SP\_LOG

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SP_LOG do { \`

`2`

`if (trace_obj_##obj.level >= lvl) { \`

Macro that outputs a trace message.

obj Trace object name lvl Trace level for the message file Source file name func Calling function name line Line number in the source file

### SpLogFatal

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SpLogFatal SP_LOG(obj, SP_LOG_LEVEL_FATAL, __FILE__, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_FATAL.

### SpLogError

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SpLogError SP_LOG(obj, SP_LOG_LEVEL_ERROR, __FILE__, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_ERROR.

### SpLogWarning

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SpLogWarning SP_LOG(obj, SP_LOG_LEVEL_WARNING, __FILE__, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_WARNING.

### SpLogInfo

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SpLogInfo SP_LOG(obj, SP_LOG_LEVEL_INFO, __FILE__, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_INFO.

### SpLogDebug

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SpLogDebug SP_LOG(obj, SP_LOG_LEVEL_DEBUG, __FILE__, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_DEBUG.

### SpLogTrace

[Return to Log macros and constants](#log-macros-and-constants)

`1`

`#define SpLogTrace SP_LOG(obj, SP_LOG_LEVEL_TRACE, __FILE__, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_TRACE.

## Data Structures

* * *

### SpLogTraceObject

[Return to Log data structures](#log-data-structures)

Trace object.

The trace object is an abstraction of a specific trace message category and an associated log level. The level can be changed freely for individual trace objects.

`1`

`struct SpLogTraceObject {`

`2`

`SpLogLevel level;`

`3`

`const char *name;`

`4`

`};`

[SpLogLevel](#sploglevel) levelThe current debug level for this trace object.*const* *char* * nameThe trace category name describing this trace object.

## Enumerations

* * *

### SpLogLevel

[Return to Log enumerations](#log-enumerations)

`1`

`enum SpLogLevel {`

`2`

`SP_LOG_LEVEL_FATAL,`

`3`

`SP_LOG_LEVEL_ERROR,`

`4`

`SP_LOG_LEVEL_WARNING,`

`5`

`SP_LOG_LEVEL_INFO,`

`6`

`SP_LOG_LEVEL_DEBUG,`

`7`

`SP_LOG_LEVEL_TRACE,`

`8`

`};`

SP\_LOG\_LEVEL\_FATALIndicates a severe abnormal condition and program termination.SP\_LOG\_LEVEL\_ERRORIndicates an abnormal condition that could result in degraded functionality.SP\_LOG\_LEVEL\_WARNINGIndicates a condition that probably has some impact on execution or performance.SP\_LOG\_LEVEL\_INFOInformational message.SP\_LOG\_LEVEL\_DEBUGDebug message.SP\_LOG\_LEVEL\_TRACETrace message.

## Functions

* * *

### SpLogRegisterTraceObject()

[Return to Log functions](#log-functions)

`1`

`SpError SpLogRegisterTraceObject(struct SpLogTraceObject *obj)`

Register a defined trace object with eSDK.

**Parameters**

**Returns**

Return kSpErrorOk on success, or error code on failure.

### SpLog()

[Return to Log functions](#log-functions)

`1`

`void SpLog(const struct SpLogTraceObject *obj, SpLogLevel level, const char *file, const char *func, int line, const char *format,...)`

Output a debug message via eSDK.

obj Pointer to trace object level The log level associated this this message file The source file from where the call is made, typically **FILE**. func The function name from where the call is made, typically **func**. line The line number from where the call is made, typically **LINE**. format A printf style format string followed by arguments.

**Parameters**

\[in]`const` `struct` [SpLogTraceObject](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#splogtraceobject) * objPointer to trace object\[in][SpLogLevel](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sploglevel) levelThe log level associated this this message\[in]`const` `char` * fileThe source file from where the call is made, typically **FILE**.\[in]`const` `char` * funcThe function name from where the call is made, typically **func**.\[in]`int` lineThe line number from where the call is made, typically **LINE**.\[in]`const` `char` * formatA printf style format string followed by arguments.

### SpLogSetLevel()

[Return to Log functions](#log-functions)

`1`

`SpError SpLogSetLevel(const char *category, SpLogLevel level)`

Control the current logging level.

Control the logging level for a particular category. If the current configured log level is greater than or equal to the level associated with the message, the log message will be passed to the debug log callback. Each log message is also associated with a category. The category is a string that is included in the log message output. Each individual category has a separate current log level. The log messages produced by the eSDK are formatted as: LEVEL CATEGORY MESSAGE where LEVEL is a single letter indicating the log level (E=Error, I=Info, etc.), CATEGORY is a short string that identifies the log category, for example 'api' and MESSAGE is the actual debug message. As an example, a debug output string with level set to [SP\_LOG\_LEVEL\_ERROR](#sploglevel) (letter "E") and the category "api" could look something like this (the timestamp is not actually part of the debug message from eSDK, but added by the DebugMessageCallback. Thus, the format may not exactly match the example below). 12:01:02.000 E api Invalid parameter passed to [SpInit](#spinit)

**Parameters**

\[in]`const` `char` * categoryIdentifies the log category for which to set the logging level. If NULL is passed in this parameter, the level will be applied to all categories.\[in][SpLogLevel](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sploglevel) levelThe log level defined by [SpLogLevel](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sploglevel)

**Returns**

Returns an error code if the category is not a valid log category.

### SpLogGetLevels()

[Return to Log functions](#log-functions)

`1`

`SpError SpLogGetLevels(char *buffer, int buffer_len)`

Get registered trace objects and log levels.

The information about trace objects and levels is represented as a string containing comma separated tuples level:trace obj, e.g. "4:app,4:esdk,4:audio".

**Parameters**

\[in]`char` * bufferA buffer to copy the string to.\[in]`int` buffer\_lenLength of the buffer

**Returns**

Returns an error code if buffer is not big enough.

## Media

* * *

`1`

`#include "spotify_embedded_media.h"`

- [Data Structures](#media-data-structures)
- [Typedefs](#media-typedefs)
- [Enumerations](#media-enumerations)
- [Functions](#media-functions)

## Data Structures

* * *

[Return to header index](#media)

[SpStreamCallbacks](#spstreamcallbacks) Callbacks to be registered with SpRegisterStreamCallbacks

## Typedefs

* * *

[Return to header index](#media)

[SpCallbackStreamStart](#spcallbackstreamstart) Callback to tell application of the track details.[SpCallbackStreamData](#spcallbackstreamdata) Callback deliver data to the integration.[SpCallbackStreamEnd](#spcallbackstreamend) Callback to tell integration that all data was delivered.[SpCallbackStreamGetPosition](#spcallbackstreamgetposition) Callback get the playback position in milliseconds.[SpCallbackStreamSeekToPosition](#spcallbackstreamseektoposition) Callback to tell the integration to seek to a position.[SpCallbackStreamFlush](#spcallbackstreamflush) Callback to tell the integration to flush.

## Enumerations

* * *

[Return to header index](#media)

## Functions

* * *

[Return to header index](#media)

[SpRegisterStreamCallbacks](#spregisterstreamcallbacks) Register callbacks related to the delivery api.[SpNotifySeekComplete](#spnotifyseekcomplete) API to notify eSDK of the completion of seek operation.[SpNotifyTrackLength](#spnotifytracklength) API to notify eSDK of the track length in milliseconds.[SpNotifyTrackError](#spnotifytrackerror) API to notify eSDK of any track errors with last played position.[SpNotifyStreamPlaybackStarted](#spnotifystreamplaybackstarted) Notify eSDK that the first audio sample of the delivery has been played.[SpNotifyStreamPlaybackContinued](#spnotifystreamplaybackcontinued) Notify eSDK that the first audio sample after a flush of a delivery has been played.[SpNotifyStreamPlaybackFinishedNaturally](#spnotifystreamplaybackfinishednaturally) Notify eSDK that the delivery playback finished by playing the last sample of the delivery.[SpSetDownloadPosition](#spsetdownloadposition) API to instruct eSDK to start downloading from given byte offset.

## Data Structures

* * *

### SpStreamCallbacks

[Return to Media data structures](#media-data-structures)

Callbacks to be registered with [SpRegisterStreamCallbacks](#spregisterstreamcallbacks)

`1`

`struct SpStreamCallbacks {`

`2`

`SpCallbackStreamStart on_start;`

`3`

`SpCallbackStreamData on_data;`

`4`

`SpCallbackStreamEnd on_end;`

`5`

`SpCallbackStreamGetPosition on_get_position;`

`6`

`SpCallbackStreamSeekToPosition on_seek_position;`

`7`

`SpCallbackStreamFlush on_flush;`

`8`

`};`

[SpCallbackStreamStart](#spcallbackstreamstart) on\_startStart of delivery callback.[SpCallbackStreamData](#spcallbackstreamdata) on\_dataData delivery callback.[SpCallbackStreamEnd](#spcallbackstreamend) on\_endEnd of delivery callback.[SpCallbackStreamGetPosition](#spcallbackstreamgetposition) on\_get\_positionCurrent playback position callback.[SpCallbackStreamSeekToPosition](#spcallbackstreamseektoposition) on\_seek\_positionSeek to position callback.[SpCallbackStreamFlush](#spcallbackstreamflush) on\_flushFlush callback.

## Typedefs

* * *

### SpCallbackStreamStart()

[Return to Media Typedefs](#media-typedefs)

`1`

`typedef void(* SpCallbackStreamStart)(unsigned int stream_id, enum SpMediaFormat media_format, enum SpDrmFormat drm_format, uint32_t stream_size_bytes, void *format_specifics, void *context)`

Callback to tell application of the track details.

To register this callback, use the function [SpRegisterStreamCallbacks](#spregisterstreamcallbacks) stream\_id Unique identifier to identify tracks media\_format Information about the format of the audio data. drm\_format Information about the used DRM method stream\_size\_bytes Size of the stream in bytes. If the size is unknown, 0 is used. format\_specifics Format dependent additional information. context Context pointer that was passed when registering the callback

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`enum` [SpMediaFormat](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spmediaformat) media\_formatInformation about the format of the audio data.\[in]`enum` [SpDrmFormat](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdrmformat) drm\_formatInformation about the used DRM method\[in]`uint32_t` stream\_size\_bytesSize of the stream in bytes. If the size is unknown, 0 is used.\[in]`void` * format\_specificsFormat dependent additional information.\[in]`void` * contextContext pointer that was passed when registering the callback

### SpCallbackStreamData()

[Return to Media Typedefs](#media-typedefs)

`1`

`typedef size_t(* SpCallbackStreamData)(unsigned int stream_id, const void *buf, size_t len, uint32_t offset, void *context)`

Callback deliver data to the integration.

To register this callback, use the function [SpRegisterStreamCallbacks](#spregisterstreamcallbacks)

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`const` `void` * bufBlock of data (it can be audio or video data)\[in]size\_t lenSize of the data\[in]`uint32_t` offsetByte offset in the data stream (relative to the start)\[in]`void` * contextContext pointer that was passed when registering the callback

### SpCallbackStreamEnd()

[Return to Media Typedefs](#media-typedefs)

`1`

`typedef void(* SpCallbackStreamEnd)(unsigned int stream_id, void *context)`

Callback to tell integration that all data was delivered.

To register this callback, use the function [SpRegisterStreamCallbacks](#spregisterstreamcallbacks) stream\_id Unique identifier to identify tracks context Context pointer that was passed when registering the callback

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`void` * contextContext pointer that was passed when registering the callback

### SpCallbackStreamGetPosition()

[Return to Media Typedefs](#media-typedefs)

`1`

`typedef uint32_t(* SpCallbackStreamGetPosition)(unsigned int stream_id, void *context)`

Callback get the playback position in milliseconds.

To register this callback, use the function [SpRegisterStreamCallbacks](#spregisterstreamcallbacks)

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`void` * contextContext pointer that was passed when registering the callback

### SpCallbackStreamSeekToPosition()

[Return to Media Typedefs](#media-typedefs)

`1`

`typedef void(* SpCallbackStreamSeekToPosition)(unsigned int stream_id, uint32_t position_ms, void *context)`

Callback to tell the integration to seek to a position.

To register this callback, use the function [SpRegisterStreamCallbacks](#spregisterstreamcallbacks) When receiving this callback, the integration should start to seek to the given position. The integration is expected to call [SpSetDownloadPosition](#spsetdownloadposition) to instruct eSDK to start downloading from a byte offset corresponding to the position given in this callback. stream\_id Unique identifier to identify tracks position\_ms Position in time within the track where to seek to context Context pointer that was passed when registering the callback

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`uint32_t` position\_msPosition in time within the track where to seek to\[in]`void` * contextContext pointer that was passed when registering the callback

### SpCallbackStreamFlush()

[Return to Media Typedefs](#media-typedefs)

`1`

`typedef uint32_t(* SpCallbackStreamFlush)(unsigned int *playing_stream_id, void *context)`

Callback to tell the integration to flush.

To register this callback, use the function [SpRegisterStreamCallbacks](#spregisterstreamcallbacks) When receiving this callback, the integration should: Forget all queued audio and compressed data Forget any deliveries that have ended except the playing one

**Parameters**

\[out]unsigned `int` * playing\_stream\_idThe delivery of the track which is currently playing. If nothing is playing, zero should be used\[in]`void` * contextContext pointer that was passed when registering the callback

## Enumerations

* * *

### SpMediaFormat

[Return to Media enumerations](#media-enumerations)

`1`

`enum SpMediaFormat {`

`2`

`kSpMediaFormatSpotifyOggVorbis,`

`3`

`kSpMediaFormatMp3,`

`4`

`kSpMediaFormatMp4AAC,`

`5`

`kSpMediaFormatSpacAAC,`

`6`

`kSpMediaFormatSpotifyManifestId,`

`7`

`};`

kSpMediaFormatSpotifyOggVorbisogg/vorbis 44.1 kHz stereo audio format with Spotify metadata pagekSpMediaFormatMp3mp3kSpMediaFormatMp4AACmp4/aac-lckSpMediaFormatSpacAACspac/aac-he-v2kSpMediaFormatSpotifyManifestIdSpotify video manifest id.

## Functions

* * *

### SpRegisterStreamCallbacks()

[Return to Media functions](#media-functions)

`1`

`SpError SpRegisterStreamCallbacks(struct SpStreamCallbacks *cb, void *context)`

Register callbacks related to the delivery api.

**Parameters**

\[in]`struct` [SpStreamCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spstreamcallbacks) * cbStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

### SpNotifySeekComplete()

[Return to Media functions](#media-functions)

`1`

`SpError SpNotifySeekComplete(unsigned int stream_id)`

API to notify eSDK of the completion of seek operation.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks

**Returns**

Returns an error code

### SpNotifyTrackLength()

[Return to Media functions](#media-functions)

`1`

`SpError SpNotifyTrackLength(unsigned int stream_id, uint32_t length_ms)`

API to notify eSDK of the track length in milliseconds.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`uint32_t` length\_msPosition in milliseconds of the track

**Returns**

Returns an error code

### SpNotifyTrackError()

[Return to Media functions](#media-functions)

`1`

`SpError SpNotifyTrackError(unsigned int stream_id, uint32_t position_ms, const char *reason)`

API to notify eSDK of any track errors with last played position.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`uint32_t` position\_msPosition in milliseconds of the track\[in]`const` `char` * reasonThe reason for the error

**Returns**

Returns an error code

### SpNotifyStreamPlaybackStarted()

[Return to Media functions](#media-functions)

`1`

`SpError SpNotifyStreamPlaybackStarted(unsigned int stream_id)`

Notify eSDK that the first audio sample of the delivery has been played.

This is used by the eSDK to measure playback latency.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks

**Returns**

Returns an error code. Returns kSpErrorAlreadyInitialized if SpNotifyStreamPlaybackStarted has already been called for this delivery.

### SpNotifyStreamPlaybackContinued()

[Return to Media functions](#media-functions)

`1`

`SpError SpNotifyStreamPlaybackContinued(unsigned int stream_id)`

Notify eSDK that the first audio sample after a flush of a delivery has been played.

This is used by the eSDK to measure seek latency.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks

**Returns**

Returns an error code

### SpNotifyStreamPlaybackFinishedNaturally()

[Return to Media functions](#media-functions)

`1`

`SpError SpNotifyStreamPlaybackFinishedNaturally(unsigned int stream_id, uint32_t last_pos_ms)`

Notify eSDK that the delivery playback finished by playing the last sample of the delivery.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`uint32_t` last\_pos\_msPosition in milliseconds of the track

**Returns**

Returns an error code

### SpSetDownloadPosition()

[Return to Media functions](#media-functions)

`1`

`SpError SpSetDownloadPosition(unsigned int stream_id, uint32_t byte_offset)`

API to instruct eSDK to start downloading from given byte offset.

**Parameters**

\[in]unsigned `int` stream\_idUnique identifier to identify tracks\[in]`uint32_t` byte\_offsetNew download byte offset (relative to the start of the stream) where downloading could continue.

**Returns**

Returns an error code

## Play

* * *

`1`

`#include "spotify_embedded_play_api.h"`

- [Macros and Constants](#play-macros-and-constants)
- [Data Structures](#play-data-structures)
- [Functions](#play-functions)

## Macros and Constants

* * *

[Return to header index](#play)

## Data Structures

* * *

[Return to header index](#play)

[SpSourceInfo](#spsourceinfo) Metadata for identifying where a playback request originated from.[SpPlayOptions](#spplayoptions) PlayOptions passed to SpPlayUriWithOptions

## Functions

* * *

[Return to header index](#play)

[SpPlayUri](#spplayuri) Start local playback of any Spotify URI.[SpPlayUriWithOptions](#spplayuriwithoptions) Play Uri with SpPlayOptions[SpPlayContextUri](#spplaycontexturi) Start local playback of any Spotify URI with an optional track UID.[SpQueueUri](#spqueueuri) Queue a URI. The track will be in queue only after kSpPlaybackNotifyQueuedTrackAccepted event is raised, but for UI purposes one can choose to monitor for kSpPlaybackNotifyMetadataChanged instead.[SpPlaybackBecomeActiveDevice](#spplaybackbecomeactivedevice) Become active without starting to play.[SpPlayPresetEx](#spplaypresetex) Extension for SpPlayPreset: Play a saved preset from different position, optionally with source info.

## Macros and Constants

* * *

### SP\_NO\_INDEX

[Return to Play macros and constants](#play-macros-and-constants)

Indicates that the index value is not set. Note: Can only be used with eSDK 3.

**See also**

- [SpPlayUri](#spplayuri)

### SP\_MAX\_UUID\_LENGTH

[Return to Play macros and constants](#play-macros-and-constants)

`1`

`#define SP_MAX_UUID_LENGTH 36`

Maximum length of a UUID.

A 128 bit UUID containing 32 hexadecimal digits in five groups separated by hyphens.

### SP\_MAX\_SOURCE\_TYPE\_LENGTH

[Return to Play macros and constants](#play-macros-and-constants)

`1`

`#define SP_MAX_SOURCE_TYPE_LENGTH 63`

Maximum length of the type of playback source.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SpPlayUri](#spplayuri)

### SP\_MAX\_SOURCE\_URI\_LENGTH

[Return to Play macros and constants](#play-macros-and-constants)

`1`

`#define SP_MAX_SOURCE_URI_LENGTH 511`

Maximum length of the source URIs.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SpPlayUri](#spplayuri)

### SP\_MAX\_REFERRER\_LENGTH

[Return to Play macros and constants](#play-macros-and-constants)

`1`

`#define SP_MAX_REFERRER_LENGTH 16`

Maximum length of the referrer.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SpPlayUri](#spplayuri)

## Data Structures

* * *

### SpSourceInfo

[Return to Play data structures](#play-data-structures)

Metadata for identifying where a playback request originated from.

**See also**

- [SpPlayUri](#spplayuri)

`1`

`struct SpSourceInfo {`

`2`

`char type;`

`3`

`char uri;`

`4`

`char expected_track_uri;`

`5`

`char referrer;`

`6`

`};`

*char* typeThe type of playlist/context/UI view that caused this playback to start. Note: If set, this MUST be one of the following strings (unless told otherwise):*char* uriThe URI of the parent container, if there is one.*char* expected\_track\_uriThe URI of the track that is expected to play.*char* referrerThe view you were in prior to initiating playback.

### SpPlayOptions

[Return to Play data structures](#play-data-structures)

PlayOptions passed to [SpPlayUriWithOptions](#spplayuriwithoptions)

`1`

`struct SpPlayOptions {`

`2`

`int from_index;`

`3`

`const char *from_uid;`

`4`

`int offset_ms;`

`5`

`int shuffle_context;`

`6`

`const struct SpSourceInfo *source_info;`

`7`

`};`

*int* from\_indexTrack index in the Context from which playback should start.*const* *char* * from\_uidThe UID to identify a unique track in the context.*int* offset\_msThe time offset to start playing specified track from.*int* shuffle\_contextSet to enable shuffle mode for the requested playback command.*const* *struct* [SpSourceInfo](#spsourceinfo) * source\_infoMetadata about what user action caused this playback event, and the expected result.

## Functions

* * *

### SpPlayUri()

[Return to Play functions](#play-functions)

`1`

`SpError SpPlayUri(const char *uri, int index, int offset_ms, const struct SpSourceInfo *source, int alias_index)`

Start local playback of any Spotify URI.

This call starts playback of a Spotify URI, such as a playlist, album, artist, or track. Valid Spotify URIs can be obtained via the Spotify Web API. Using this call will 'pull' playback from any other Spotify Connect client active on the same account. Note that there may be a lag between the introduction of new URI types and support for playing them with this call.

**Parameters**

\[in]`const` `char` * uriURI of resource (ex: spotify:album:6tSdnCBm5HCAjwNxWfUC7m)\[in]`int` alias_ indexThe zero based index of the item to start playing in the resource (for instance, '4' would play the 5th track in a playlist). Set to zero if resource does not have multiple items. In eSDK 3, this can be set to [SP\_NO\_INDEX](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sp_no_index) if no specific index is required. In case of non-shuffled context this will result in first track of the context being played whereas in shuffled context this will result in a random track being played.\[in]`int` offset\_msThe time offset to start playing specified track from. Set to zero to start from the beginning.\[in]`const` `struct` [SpSourceInfo](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsourceinfo) * sourceMetadata about what user action caused this playback event, and the expected result. This information is used to correct behavior when the exact request isn't possible, and to enable better recommendations and suggestions for users. This field is optional, but MUST be provided whenever possible. Failure to fill in this data accurately will result in a downgraded Spotify experience.\[in]`int` alias\_indexThe index of the device alias to start playback on. If aliases aren't used, pass -1.

**Returns**

Returns an error code

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SP\_NO\_INDEX](#sp_no_index)

### SpPlayUriWithOptions()

[Return to Play functions](#play-functions)

`1`

`SpError SpPlayUriWithOptions(const char *uri, const struct SpPlayOptions *opts, int alias_index)`

Play Uri with [SpPlayOptions](#spplayoptions)

**Parameters**

\[in]`const` `char` * uriThe context URI to play.\[in]`const` `struct` [SpPlayOptions](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spplayoptions) * optsThe options to apply to the play command.\[in]`int` alias\_indexDevice alias index.

**Returns**

Returns an error code

### SpPlayContextUri()

[Return to Play functions](#play-functions)

`1`

`SpError SpPlayContextUri(const char *uri, const char *from_uid, int offset_ms, const struct SpSourceInfo *source, int alias_index)`

Start local playback of any Spotify URI with an optional track UID.

This call will start playback of any Spotify context URI. In addition, it allows the client to provide a UID to start the playback from a given track in the context. The main difference between UIDs and the expected\_track\_uri parameter in [SpPlayUri](#spplayuri) is that while one track URI can occur more than once in the context, UIDs are unique for each track in it. Valid Spotify URIs can be obtained via the Spotify Web API. Track UIDs are currently available when resolving contexts from a small subset of services. Using this call will 'pull' playback from any other Spotify Connect client active on the same account.

**Parameters**

\[in]`const` `char` * uriURI of resource (ex: spotify:album:6tSdnCBm5HCAjwNxWfUC7m)\[in]`const` `char` * from\_uidThe UID to identify a unique track in the context.\[in]`int` offset\_msThe time offset to start playing specified track from. Set to zero to start from the beginning.\[in]`const` `struct` [SpSourceInfo](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsourceinfo) * sourceMetadata about what user action caused this playback event, and the expected result. This information is used to correct behavior when the exact request isn't possible, and to enable better recommendations and suggestions for users. This field is optional, but MUST be provided whenever possible. Failure to fill in this data accurately will result in a downgraded Spotify experience.\[in]`int` alias\_indexThe index of the device alias to start playback on. If aliases aren't used, pass -1.

**Returns**

Returns an error code

### SpQueueUri()

[Return to Play functions](#play-functions)

`1`

`SpError SpQueueUri(const char *uri)`

Queue a URI. The track will be in queue only after [kSpPlaybackNotifyQueuedTrackAccepted](#spplaybacknotification) event is raised, but for UI purposes one can choose to monitor for [kSpPlaybackNotifyMetadataChanged](#spplaybacknotification) instead.

**Parameters**

\[in]`const` `char` * uriURI to queue.

**Returns**

Returns an error code.

### SpPlaybackBecomeActiveDevice()

[Return to Play functions](#play-functions)

`1`

`SpError SpPlaybackBecomeActiveDevice(int alias_index)`

Become active without starting to play.

alias\_index The index of the device alias that should become active. If aliases aren't used, pass -1. This call makes the device active, without starting to play anything, if playback is paused or no device is active. The device is active after the [kSpPlaybackNotifyBecameActive](#spplaybacknotification) event is received. If another Connect-enabled device was active and playing, it will be interrupted. If the currently active device is playing, this call behaves like [SpPlaybackPlay](#spplaybackplay) If device aliases are used, this function will switch the selected alias. If the selected alias was changed during playback, the playback will continue uninterrupted with the new alias.

**Parameters**

\[in]`int` alias\_indexThe index of the device alias that should become active. If aliases aren't used, pass -1.

**Returns**

Returns an error code

### SpPlayPresetEx()

[Return to Play functions](#play-functions)

`1`

`SpError SpPlayPresetEx(int preset_id, uint8_t *buffer, size_t buff_size, int relative_index, uint32_t offset_ms, const struct SpSourceInfo *source, int alias_index)`

Extension for SpPlayPreset: Play a saved preset from different position, optionally with source info.

Note: This is an experimental extension, and is not guaranteed to be stable.

**Parameters**

**Returns**

Returns an error code

**See also**

- [SpPlayPreset](#spplaypreset)
- [SpPlayPresetEx](#spplaypresetex)
- [SpPresetSubscribe](#sppresetsubscribe)
- [SpPlayPreset](#spplaypreset)

## Storage

* * *

`1`

`#include "spotify_embedded_storage.h"`

- [Data Structures](#storage-data-structures)
- [Typedefs](#storage-typedefs)
- [Functions](#storage-functions)

## Data Structures

* * *

[Return to header index](#storage)

[SpDiskStorageCallbacks](#spdiskstoragecallbacks) Callbacks to be registered with SpRegisterDataCacheCallbacks

## Typedefs

* * *

[Return to header index](#storage)

[SpCallbackStorageAlloc](#spcallbackstoragealloc) Callback to allocate space for resource being stored. Each successful alloc call is accompanied with corresponding close call. It is obligatory for the user to use this callback to reserve actual space on device media for the key specified.[SpCallbackStorageWrite](#spcallbackstoragewrite) Callback for writing the data into storage. Before writing to the storage eSDK does one of two things: call alloc to reserve space for future write or call read to get the data. After that eSDK writes the data into storage. Once write is fully complete eSDK calls close callback.[SpCallbackStorageRead](#spcallbackstorageread) Callback for reading the data. Once eSDK read all required data close callback is called to notify the user that data handle referenced by storage\_key can be closed.[SpCallbackStorageClose](#spcallbackstorageclose) Callback to inform the user that data handle referenced by storage\_key can be closed.[SpCallbackStorageDelete](#spcallbackstoragedelete) Callback to inform the user that data referenced by storage\_key should be deleted from storage.[SpCallbackThrottleRequest](#spcallbackthrottlerequest) eSDK calls this callback to figure out if it needs to limit write access to the storage.

## Functions

* * *

[Return to header index](#storage)

[SpRegisterStorageCallbacks](#spregisterstoragecallbacks) Register storage callbacks.

## Data Structures

* * *

### SpDiskStorageCallbacks

[Return to Storage data structures](#storage-data-structures)

Callbacks to be registered with SpRegisterDataCacheCallbacks

Storage callbacks must be either all NULLs or all valid pointers. Throttle callback maybe be NULL regardless of storage callbacks value. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpDiskStorageCallbacks {`

`2`

`SpCallbackStorageAlloc alloc_storage;`

`3`

`SpCallbackStorageWrite write_storage;`

`4`

`SpCallbackStorageRead read_storage;`

`5`

`SpCallbackStorageClose close_storage;`

`6`

`SpCallbackStorageDelete delete_storage;`

`7`

`SpCallbackThrottleRequest throttle_request;`

`8`

`};`

[SpCallbackStorageAlloc](#spcallbackstoragealloc) alloc\_storageAlloc storage record callback.[SpCallbackStorageWrite](#spcallbackstoragewrite) write\_storageWrite storage data callback.[SpCallbackStorageRead](#spcallbackstorageread) read\_storageRead storage data callback.[SpCallbackStorageClose](#spcallbackstorageclose) close\_storageClose storage record callback.[SpCallbackStorageDelete](#spcallbackstoragedelete) delete\_storageDelete storage record callback.[SpCallbackThrottleRequest](#spcallbackthrottlerequest) throttle\_requestAsks client if disk writes needs to be throttled.

## Typedefs

* * *

### SpCallbackStorageAlloc()

[Return to Storage Typedefs](#storage-typedefs)

`1`

`typedef enum SpCallbackStorageAlloc)(const char *storage_key, uint32_t total_size, void *context)`

Callback to allocate space for resource being stored. Each successful alloc call is accompanied with corresponding close call. It is obligatory for the user to use this callback to reserve actual space on device media for the key specified.

To register this callback, use the function SpRegisterDiskStorageCallbacks

**Parameters**

\[in]`const` `char` * storage\_keyStorage key identifying the record\[in]`uint32_t` total\_sizeThe full resource size in bytes or 0 if size is not known.\[in]`void` * contextContext pointer that was passed when registering the callback.

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The allocation of space should be done in the way that following read and write operations will succeed within the specified resource size.

### SpCallbackStorageWrite()

[Return to Storage Typedefs](#storage-typedefs)

`1`

`typedef int(* SpCallbackStorageWrite)(const char *storage_key, uint32_t offset, const void *data, uint32_t data_size, void *context)`

Callback for writing the data into storage. Before writing to the storage eSDK does one of two things: call alloc to reserve space for future write or call read to get the data. After that eSDK writes the data into storage. Once write is fully complete eSDK calls close callback.

To register this callback, use the function SpRegisterDiskStorageCallbacks

**Parameters**

\[in]`const` `char` * storage\_keyStorage key identifying the record\[in]`uint32_t` offsetThe offset in bytes in the resource we are writing to.\[in]`const` `void` * dataA pointer to the buffer containing the data to be written to storage.\[in]`uint32_t` data\_sizeThe number of bytes to be written to the storage.\[in]`void` * contextContext pointer that was passed when registering the callback.

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The application should not block or call other API functions in the callback. Offset field must always be respected on write operation. Application should consume whole data in the call.

### SpCallbackStorageRead()

[Return to Storage Typedefs](#storage-typedefs)

`1`

`typedef int(* SpCallbackStorageRead)(const char *storage_key, uint32_t offset, void *data, uint32_t data_size, void *context)`

Callback for reading the data. Once eSDK read all required data close callback is called to notify the user that data handle referenced by storage\_key can be closed.

To register this callback, use the function SpRegisterDiskStorageCallbacks

**Parameters**

\[in]`const` `char` * storage\_keyStorage key identifying the record\[in]`uint32_t` offsetThe offset eSDK are reading from.\[out]`void` * dataA pointer to the buffer that receives the data read from storage.\[in]`uint32_t` data\_sizeThe number bytes to read.\[in]`void` * contextContext pointer that was passed when registering the callback

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The application should not block or call other API functions in the callback. If no storage read is possible, just return 0.

### SpCallbackStorageClose()

[Return to Storage Typedefs](#storage-typedefs)

`1`

`typedef void(* SpCallbackStorageClose)(const char *storage_key, void *context)`

Callback to inform the user that data handle referenced by storage\_key can be closed.

To register this callback, use the function SpRegisterDiskStorageCallbacks

**Parameters**

\[in]`const` `char` * storage\_keyStorage key identifying the record\[in]`void` * contextContext pointer that was passed when registering the callback.

**Notes:**

- The application should not block or call other API functions in the callback. This callback would be called for any successful Alloc. For any resource open caused by Read/Write API calls.

### SpCallbackStorageDelete()

[Return to Storage Typedefs](#storage-typedefs)

`1`

`typedef enum SpCallbackStorageDelete)(const char *storage_key, void *context)`

Callback to inform the user that data referenced by storage\_key should be deleted from storage.

To register this callback, use the function SpRegisterDiskStorageCallbacks

**Parameters**

\[in]`const` `char` * storage\_keyStorage key identifying the record.\[in]`void` * contextContext pointer that was passed when registering the callback.

**Notes:**

- The application should not block or call other API functions in the callback.
- If the deletion operation is expected to take some time the application shall return [kSpAPITryAgain](#spapireturncode) for the duration of the operation and [kSpAPINoError](#spapireturncode) once it has been completed. It is important to not block execution of eSDK for prolonged periods (ideally less than 10ms). This callback can be called for literally any storage\_key.

### SpCallbackThrottleRequest()

[Return to Storage Typedefs](#storage-typedefs)

`1`

`typedef int(* SpCallbackThrottleRequest)(const char *storage_key, void *context)`

eSDK calls this callback to figure out if it needs to limit write access to the storage.

**Parameters**

\[in]`const` `char` * storage\_keyStorage key identifying the record.\[in]`void` * contextContext pointer that was passed when registering the callback.

**Notes:**

- The application should not block or call other API functions in the callback.

## Functions

* * *

### SpRegisterStorageCallbacks()

[Return to Storage functions](#storage-functions)

`1`

`SpError SpRegisterStorageCallbacks(struct SpDiskStorageCallbacks *cb, void *context)`

Register storage callbacks.

**Parameters**

\[in]`struct` [SpDiskStorageCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spdiskstoragecallbacks) * cbStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

## Tls

* * *

`1`

`#include "spotify_embedded_tls.h"`

- [Data Structures](#tls-data-structures)
- [Typedefs](#tls-typedefs)
- [Functions](#tls-functions)

## Data Structures

* * *

[Return to header index](#tls)

[SpTLSCallbacks](#sptlscallbacks) Callbacks to be registered with SpRegisterTLSCallbacks

## Typedefs

* * *

[Return to header index](#tls)

[SpCallbackTLSInit](#spcallbacktlsinit) This callback is invoked by eSDK to let the TLS library integration perform any one-time initialization.[SpCallbackTLSDeinit](#spcallbacktlsdeinit) This callback is invoked by eSDK to let the TLS library integration perform deallocation of resource during teardown.[SpCallbackTLSCreate](#spcallbacktlscreate) This callback is invoked once in the beginning of every TLS connection.[SpCallbackTLSHandshake](#spcallbacktlshandshake) This callback is invoked by eSDK to perform the TLS handshake.[SpCallbackTLSRead](#spcallbacktlsread) This callback is invoked by eSDK to read data on a TLS connection.[SpCallbackTLSWrite](#spcallbacktlswrite) This callback is invoked by eSDK to write data on a TLS connection.[SpCallbackTLSClose](#spcallbacktlsclose) This callback should clean up any resources allocated in the connect callback.[SpCallbackTLSGetError](#spcallbacktlsgeterror) Callback invoked to get an error message for the last error.

## Functions

* * *

[Return to header index](#tls)

[SpRegisterTLSCallbacks](#spregistertlscallbacks) Register TLS-related callbacks.[SpTLSAddCARootCert](#sptlsaddcarootcert) Add root certificate to the eSDK TLS stack.[SpTLSFreeCARootCerts](#sptlsfreecarootcerts) Remove all certificates loaded on the TLS stack and frees the memory used by them.

## Data Structures

* * *

### SpTLSCallbacks

[Return to Tls data structures](#tls-data-structures)

Callbacks to be registered with [SpRegisterTLSCallbacks](#spregistertlscallbacks)

None of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpTLSCallbacks {`

`2`

`SpCallbackTLSInit init;`

`3`

`SpCallbackTLSDeinit deinit;`

`4`

`SpCallbackTLSCreate create;`

`5`

`SpCallbackTLSHandshake handshake;`

`6`

`SpCallbackTLSRead read;`

`7`

`SpCallbackTLSWrite write;`

`8`

`SpCallbackTLSClose close;`

`9`

`SpCallbackTLSGetError get_error;`

`10`

`};`

[SpCallbackTLSInit](#spcallbacktlsinit) initCallback that performs one-time initialization.[SpCallbackTLSDeinit](#spcallbacktlsdeinit) deinitCallback that performs release of resources allocated during init.[SpCallbackTLSCreate](#spcallbacktlscreate) createCallback invoked once per connection to initialize TLS context.[SpCallbackTLSHandshake](#spcallbacktlshandshake) handshakeCallback invoked repeatedly to perform the TLS handshake.[SpCallbackTLSRead](#spcallbacktlsread) readCallback for reading from the TLS data stream.[SpCallbackTLSWrite](#spcallbacktlswrite) writeCallback for writing to the TLS data stream.[SpCallbackTLSClose](#spcallbacktlsclose) closeCallback invoked to cleanup any TLS context before closing the socket.[SpCallbackTLSGetError](#spcallbacktlsgeterror) get\_errorCallback invoked to get an error message for the last error.

## Typedefs

* * *

### SpCallbackTLSInit()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef enum SpCallbackTLSInit)(void *context)`

This callback is invoked by eSDK to let the TLS library integration perform any one-time initialization.

**Parameters**

\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSDeinit()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef enum SpCallbackTLSDeinit)(void *context)`

This callback is invoked by eSDK to let the TLS library integration perform deallocation of resource during teardown.

**Parameters**

\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSCreate()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef enum SpCallbackTLSCreate)(struct SpSocketHandle *socket, const char *hostname, void *context)`

This callback is invoked once in the beginning of every TLS connection.

The callback receives a socket via the pointer to [SpSocketHandle](#spsockethandle) that is already connected to the remote peer. This callback should typically allocate and setup all TLS related resources. The tls field of the [SpSocketHandle](#spsockethandle) should be used to store any connection specific state that is needed.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketPointer to eSDK socket already connected to the remote peer.\[in]`const` `char` * hostnameHostname of the remote peer.\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSHandshake()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef enum SpCallbackTLSHandshake)(struct SpSocketHandle *socket, void *context)`

This callback is invoked by eSDK to perform the TLS handshake.

The callback is invoked repeatedly to perform the handshake. This callback is invoked repeatedly as long as it returns [kSpAPITryAgain](#spapireturncode) The peer verification is mandatory and the implementation of this callback must validate the peer certificate against a list of trusted CA certificates. Should return [kSpAPIGenericError](#spapireturncode) is the handshake failed. Any specific information about the reason for the failure will be returned in the [SpCallbackTLSGetError](#spcallbacktlsgeterror) call.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketPointer to eSDK socket already connected to the remote peer.\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application must not block or call other API functions in the callback.

### SpCallbackTLSRead()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef enum SpCallbackTLSRead)(struct SpSocketHandle *socket, void *buf, size_t len, size_t *actual, void *context)`

This callback is invoked by eSDK to read data on a TLS connection.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketPointer to eSDK socket already connected to the remote peer.\[in]`void` * bufPointer to buffer for the data to be received.\[in]size\_t lenThe size of the buffer (in bytes).\[out]size\_t * actualActual number of bytes received.\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSWrite()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef enum SpCallbackTLSWrite)(struct SpSocketHandle *socket, const void *buf, size_t len, size_t *actual, void *context)`

This callback is invoked by eSDK to write data on a TLS connection.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketPointer to eSDK socket already connected to the remote peer.\[in]`const` `void` * bufPointer to buffer with data to be written.\[in]size\_t lenNumber of bytes of data in buffer.\[out]size\_t * actualNumber of byte actually written.\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSClose()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef void(* SpCallbackTLSClose)(struct SpSocketHandle *socket, void *context)`

This callback should clean up any resources allocated in the connect callback.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketPointer to eSDK socket already connected to the remote peer.\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSGetError()

[Return to Tls Typedefs](#tls-typedefs)

`1`

`typedef int(* SpCallbackTLSGetError)(struct SpSocketHandle *socket, char *buf, size_t len, void *context)`

Callback invoked to get an error message for the last error.

The implementation of this callback should put a error message in the form of a zero-terminated string in the buffer pointed to by buf. This error message should describe the latest error returned by any of the other callback functions.

**Parameters**

\[in]`struct` [SpSocketHandle](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#spsockethandle) * socketPointer to eSDK socket already connected to the remote peer.\[in]`char` * bufPointer to buffer that will receive the error message.\[in]size\_t lenLength of the buffer.\[in]`void` * contextContext provided in callback register function.

**Notes:**

- The application should not block or call other API functions in the callback.

## Functions

* * *

### SpRegisterTLSCallbacks()

[Return to Tls functions](#tls-functions)

`1`

`SpError SpRegisterTLSCallbacks(struct SpTLSCallbacks *callbacks, void *context)`

Register TLS-related callbacks.

**Parameters**

\[in]`struct` [SpTLSCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sptlscallbacks) * callbacksStructure with pointers to individual callback functions. All pointers must be valid.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

**Notes:**

- A call to this function has to be performed before [SpInit](#spinit) is called. Calling this function when eSDK is initialized will fail with [kSpErrorAlreadyInitialized](#sperror) The function will return [kSpErrorUnsupported](#sperror) in the eSDK configurations with built-in TLS.

### SpTLSAddCARootCert()

[Return to Tls functions](#tls-functions)

`1`

`SpError SpTLSAddCARootCert(const uint8_t *certificate, size_t length, int *underlying_error)`

Add root certificate to the eSDK TLS stack.

eSDK uses TLS secured HTTPS connections to download media files from CDN (Content Delivery Network) servers. The servers that CDN providers use are using certificates from common Certificate Authorities (CA). eSDK cannot read Certificate Authority (CA) root certificates from the operating system, but the integration has to provide the certificates. The purpose of this function is to provide eSDK the CA root certificates which eSDK needs. As an example, integration can use the CA certificate bundle from Mozilla: [https://curl.se/docs/caextract.html](https://curl.se/docs/caextract.html)

**Parameters**

\[in]`const` uint8\_t * certificateEither a binary DER certificate or a string with a PEM-format certificate.

**Returns**

Returns kSpErrorInvalidArgument if the certificate could not be parsed kSpErrorAlreadyInitialized if the function is called between SpInit and SpFree. If the return value is kSpErrorInvalidArgument and underlying\_error is non-NULL, there will be an error code from the underlying TLS stack (currently MbedTLS) returned in \*underlying\_error.

**Notes:**

- If the buffer is a PEM-format certificate, it must be NULL-terminated.
- If the buffer is a PEM-format certificate, this length must include the NULL termination.
- Calls to this function have to be performed before [SpInit](#spinit) is called or after [SpFree](#spfree)

### SpTLSFreeCARootCerts()

[Return to Tls functions](#tls-functions)

`1`

`SpError SpTLSFreeCARootCerts(void)`

Remove all certificates loaded on the TLS stack and frees the memory used by them.

**Returns**

kSpErrorUnavailable if the function is called between SpInit and SpFree.

## Token

* * *

`1`

`#include "spotify_embedded_token.h"`

- [Data Structures](#token-data-structures)
- [Typedefs](#token-typedefs)
- [Functions](#token-functions)

## Data Structures

* * *

[Return to header index](#token)

[SpTokenCallbacks](#sptokencallbacks) Callbacks to be registered with SpRegisterTokenCallbacks

## Typedefs

* * *

[Return to header index](#token)

[SpCallbackConnectionReceiveAccessToken](#spcallbackconnectionreceiveaccesstoken) Callback to deliver the access token requested by SpConnectionRequestAccessToken[SpCallbackConnectionReceiveAuthCode](#spcallbackconnectionreceiveauthcode) Callback to deliver the access token requested by SpConnectionRequestAuthCode

## Functions

* * *

[Return to header index](#token)

[SpRegisterTokenCallbacks](#spregistertokencallbacks) Register token callbacks.[SpConnectionRequestAccessToken](#spconnectionrequestaccesstoken) Request an access token for the logged in user.[SpConnectionRequestAuthCode](#spconnectionrequestauthcode) Request an authorization code for the logged in user.

## Data Structures

* * *

### SpTokenCallbacks

[Return to Token data structures](#token-data-structures)

Callbacks to be registered with [SpRegisterTokenCallbacks](#spregistertokencallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

`1`

`struct SpTokenCallbacks {`

`2`

`SpCallbackConnectionReceiveAccessToken on_access_token;`

`3`

`SpCallbackConnectionReceiveAuthCode on_auth_code;`

`4`

`};`

[SpCallbackConnectionReceiveAccessToken](#spcallbackconnectionreceiveaccesstoken) on\_access\_tokenAccess token event callbacks.[SpCallbackConnectionReceiveAuthCode](#spcallbackconnectionreceiveauthcode) on\_auth\_codeAuthorization code event callbacks.

## Typedefs

* * *

### SpCallbackConnectionReceiveAccessToken()

[Return to Token Typedefs](#token-typedefs)

`1`

`typedef void(* SpCallbackConnectionReceiveAccessToken)(const char *token_json, int error, void *context)`

Callback to deliver the access token requested by [SpConnectionRequestAccessToken](#spconnectionrequestaccesstoken)

**Parameters**

\[in]`const` `char` * token\_jsonA serialized JSON object containing the access token or an empty string if error is != 0. See Notes below.\[in]`int` errorAn internal error code or 0 on success. The token in token\_json is only valid if this is 0.\[in]`void` * contextContext pointer that was passed then the callback was registered.

**Notes:**

- The JSON object looks as follows: "accessToken":"tokendata", "expiresIn":expiryinseconds,//typically3600 "tokenType":"tokentype"//typically"Bearer"

### SpCallbackConnectionReceiveAuthCode()

[Return to Token Typedefs](#token-typedefs)

`1`

`typedef void(* SpCallbackConnectionReceiveAuthCode)(const char *token_json, int error, void *context)`

Callback to deliver the access token requested by [SpConnectionRequestAuthCode](#spconnectionrequestauthcode)

**Parameters**

\[in]`const` `char` * token\_jsonA serialized JSON object containing the access token or an empty string if error is != 0. See Notes below.\[in]`int` errorAn internal error code or 0 on success. The token in token\_json is only valid if this is 0.\[in]`void` * contextContext pointer that was passed then the callback was registered.

**Notes:**

- The JSON object looks as follows: "code":"tokendata", "redirectUri":"someUri"

## Functions

* * *

### SpRegisterTokenCallbacks()

[Return to Token functions](#token-functions)

`1`

`SpError SpRegisterTokenCallbacks(struct SpTokenCallbacks *cb, void *context)`

Register token callbacks.

**Parameters**

\[in]`struct` [SpTokenCallbacks](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194#sptokencallbacks) * cbStructure with pointers to individual callback functions. Any of the pointers in the structure may be NULL.\[in]`void` * contextApplication-defined pointer that will be passed unchanged as the context argument to the callbacks.

**Returns**

Returns an error code

### SpConnectionRequestAccessToken()

[Return to Token functions](#token-functions)

`1`

`SpError SpConnectionRequestAccessToken(const char *scope)`

Request an access token for the logged in user.

scope A comma-separated list of scopes for the resulting access token. See [https://developer.spotify.com/documentation/web-api/concepts/scopes/](https://developer.spotify.com/documentation/web-api/concepts/scopes/)

**Parameters**

### SpConnectionRequestAuthCode()

[Return to Token functions](#token-functions)

`1`

`SpError SpConnectionRequestAuthCode(const char *scope)`

Request an authorization code for the logged in user.

**Parameters**

**Notes:**

- The string scope must not be longer than 425 characters.