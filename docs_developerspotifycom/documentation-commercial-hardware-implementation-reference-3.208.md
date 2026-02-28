---
title: API Reference eSDK 3.208.26 | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.208
source: crawler
fetched_at: 2026-02-27T23:41:29.824039-03:00
rendered_js: true
word_count: 15838
summary: This document provides a comprehensive index of the API components for the Spotify Embedded SDK, detailing macros, data structures, and functions required for media playback integration.
tags:
    - spotify-sdk
    - embedded-systems
    - api-reference
    - c-programming
    - audio-playback
    - spotify-connect
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

[SP\_API\_VERSION](#sp_api_version)82 [SP\_RECOMMENDED\_MEMORY\_BLOCK\_SIZE](#sp_recommended_memory_block_size)1024 * 1024 [SP\_MAX\_BRAND\_NAME\_LENGTH](#sp_max_brand_name_length)32 [SP\_MAX\_MODEL\_NAME\_LENGTH](#sp_max_model_name_length)30 [SP\_MAX\_PLATFORM\_NAME\_LENGTH](#sp_max_platform_name_length)64 [SP\_MAX\_CLIENT\_ID\_LENGTH](#sp_max_client_id_length)32 [SP\_MAX\_OS\_VERSION\_LENGTH](#sp_max_os_version_length)64 [SP\_MAX\_DISPLAY\_NAME\_LENGTH](#sp_max_display_name_length)64 [SP\_MAX\_AD\_USER\_AGENT\_LENGTH](#sp_max_ad_user_agent_length)256 [SP\_MAX\_UNIQUE\_ID\_LENGTH](#sp_max_unique_id_length)64 [SP\_MAX\_USERNAME\_LENGTH](#sp_max_username_length)64 [SP\_MAX\_DEVICE\_ALIASES](#sp_max_device_aliases)8 [SP\_MAX\_AD\_METADATA\_PAIRS](#sp_max_ad_metadata_pairs)4 [SP\_NO\_ALIAS\_SELECTED](#sp_no_alias_selected)-1 [SP\_MAX\_PLAYER\_MODES](#sp_max_player_modes)8 [SP\_MAX\_MODE\_KEY\_LENGTH](#sp_max_mode_key_length)32 [SP\_MAX\_MODE\_VALUE\_LENGTH](#sp_max_mode_value_length)32 [SP\_MAX\_METADATA\_NAME\_LENGTH](#sp_max_metadata_name_length)255 [SP\_MAX\_METADATA\_URI\_LENGTH](#sp_max_metadata_uri_length)127 [SP\_MAX\_TRACK\_UID\_LENGTH](#sp_max_track_uid_length)64 [SP\_MAX\_METADATA\_IMAGE\_URL\_LENGTH](#sp_max_metadata_image_url_length)255 [SP\_PLAYER\_COOKIE\_LENGTH](#sp_player_cookie_length)32 [SP\_MAX\_PLAYBACK\_ID\_LENGTH](#sp_max_playback_id_length)32 [SP\_MAX\_PUBLIC\_KEY\_LENGTH](#sp_max_public_key_length)149 [SP\_MAX\_DEVICE\_ID\_LENGTH](#sp_max_device_id_length)64 [SP\_MAX\_DEVICE\_TYPE\_LENGTH](#sp_max_device_type_length)15 [SP\_MAX\_VERSION\_LENGTH](#sp_max_version_length)30 [SP\_MAX\_GROUP\_STATUS\_LENGTH](#sp_max_group_status_length)15 [SP\_MAX\_TOKEN\_TYPE\_LENGTH](#sp_max_token_type_length)30 [SP\_MAX\_SCOPE\_LENGTH](#sp_max_scope_length)64 [SP\_MAX\_CLIENT\_KEY\_LENGTH](#sp_max_client_key_length)511 [SP\_MAX\_ZEROCONF\_BLOB\_LENGTH](#sp_max_zeroconf_blob_length)2047 [SP\_MAX\_LOGIN\_ID\_LENGTH](#sp_max_login_id_length)64 [SP\_MAX\_AVAILABILITY\_LENGTH](#sp_max_availability_length)15 [SP\_MAX\_PARTNER\_NAME\_LENGTH](#sp_max_partner_name_length)48 [SP\_MAX\_FILENAME\_LENGTH](#sp_max_filename_length)63 [SP\_MAX\_RESPONSE\_SOURCE\_LENGTH](#sp_max_response_source_length)20 [SP\_ZEROCONF\_DISABLED](#sp_zeroconf_disabled)0 [SP\_ZEROCONF\_SERVE](#sp_zeroconf_serve)1 [SP\_ZEROCONF\_SERVE\_HTTP\_ONLY](#sp_zeroconf_serve_http_only)2 [SP\_ZEROCONF\_SERVE\_MDNS\_ONLY](#sp_zeroconf_serve_mdns_only)3 [SP\_SCOPE\_STREAMING](#sp_scope_streaming)"streaming" [SP\_DEVICE\_ALIAS\_ATTRIBUTE\_GROUP](#sp_device_alias_attribute_group)1 [SP\_GLOBAL\_ATTRIBUTE\_VOICE](#sp_global_attribute_voice)2 [SP\_MAX\_SUPPORTED\_FORMATS](#sp_max_supported_formats)8 [SP\_PLAYBACK\_RESTRICTION\_ALREADY\_PAUSED](#sp_playback_restriction_already_paused)1 [SP\_PLAYBACK\_RESTRICTION\_NOT\_PAUSED](#sp_playback_restriction_not_paused)2 [SP\_PLAYBACK\_RESTRICTION\_LICENSE\_DISALLOW](#sp_playback_restriction_license_disallow)4 [SP\_PLAYBACK\_RESTRICTION\_AD\_DISALLOW](#sp_playback_restriction_ad_disallow)8 [SP\_PLAYBACK\_RESTRICTION\_NO\_PREV\_TRACK](#sp_playback_restriction_no_prev_track)16 [SP\_PLAYBACK\_RESTRICTION\_NO\_NEXT\_TRACK](#sp_playback_restriction_no_next_track)32 [SP\_PLAYBACK\_RESTRICTION\_UNKNOWN](#sp_playback_restriction_unknown)64 [SP\_PLAYBACK\_RESTRICTION\_ENDLESS\_CONTEXT](#sp_playback_restriction_endless_context)128 [SP\_MAX\_PLAYER\_MODES\_RESTRICTIONS](#sp_max_player_modes_restrictions)Maximum number of Player Mode Restrictions eSDK can provide through [SpPlaybackRestrictions](#spplaybackrestrictions) in Metadata. [SP\_MAX\_PLAYER\_MODE\_VALUE\_DISALLOW\_REASONS](#sp_max_player_mode_value_disallow_reasons)16 [SP\_MAX\_METADATA\_KEY\_LENGTH](#sp_max_metadata_key_length)32 [SP\_MAX\_METADATA\_VALUE\_LENGTH](#sp_max_metadata_value_length)64

## Data Structures

* * *

[Return to header index](#main)

[SpPlayerModeDisallowReasons](#spplayermodedisallowreasons)This *struct* stores a Mode value and the restriction disallow reasons associated with it. [SpPlayerModeRestrictions](#spplayermoderestrictions)this *struct* stores a Mode key and the list of restricted values. [SpPlaybackRestrictions](#spplaybackrestrictions)Playback restrictions. [SpFormat](#spformat)Mapping of which media formats are supported in which DRM. [SpMetadata](#spmetadata)Track metadata. [SpAdMetadata](#spadmetadata)Key value pair for Ad-related metadata. [SpZeroConfDeviceAlias](#spzeroconfdevicealias)ZeroConf DeviceAlias. [SpZeroConfVars](#spzeroconfvars)ZeroConf variables. [SpSampleFormat](#spsampleformat)Sample format of the audio data. [SpPlaybackCallbacks](#spplaybackcallbacks)Callbacks to be registered with [SpRegisterPlaybackCallbacks()](#spregisterplaybackcallbacks) [SpDebugCallbacks](#spdebugcallbacks)Callbacks to be registered with [SpRegisterDebugCallbacks()](#spregisterdebugcallbacks) [SpConnectionCallbacks](#spconnectioncallbacks)Callbacks to be registered with [SpRegisterConnectionCallbacks()](#spregisterconnectioncallbacks) [SpDeviceAlias](#spdevicealias)Device alias definition. [SpConfig](#spconfig)Configuration. [SpDeviceAliasCallbacks](#spdevicealiascallbacks)Callbacks to be registered with [SpRegisterDeviceAliasCallbacks()](#spregisterdevicealiascallbacks)

## Typedefs

* * *

[Return to header index](#main)

[SpCallbackError](#spcallbackerror)Callback for reporting errors to the application. [SpCallbackPlaybackNotify](#spcallbackplaybacknotify)Callback for notifying the application about playback-related events. [SpCallbackPlaybackSeek](#spcallbackplaybackseek)Callback to notify the application of a change in the playback position. [SpCallbackPlaybackApplyVolume](#spcallbackplaybackapplyvolume)Callback to notify the application of a volume change using Spotify Connect. [SpCallbackConnectionNotify](#spcallbackconnectionnotify)Callback for notifying the application about events related to the connection to [Spotify.](#spotify) [SpCallbackConnectionNewCredentials](#spcallbackconnectionnewcredentials)Callback for passing a login blob to the application. [SpCallbackConnectionMessage](#spcallbackconnectionmessage)Callback for sending a message to the user. [SpCallbackDebugMessage](#spcallbackdebugmessage)Callback for sending debug messages/trace logs. [SpCallbackSelectedDeviceAliasChanged](#spcallbackselecteddevicealiaschanged)Callback for receiving the selected device alias from the backend. [SpCallbackDeviceAliasesUpdateDone](#spcallbackdevicealiasesupdatedone)Callback for knowing when the device alias list has been updated after call to [SpSetDeviceAliases()](#spsetdevicealiases)

## Enumerations

* * *

[Return to header index](#main)

[SpError](#sperror)Error codes. [SpAPIReturnCode](#spapireturncode)Enum describes return codes that public API functions can report to eSDK. [SpPlaybackBitrate](#spplaybackbitrate)Valid bitrate values. This *enum* is used for selecting the audio quality of the files to play. [SpPlaybackNotification](#spplaybacknotification)Playback-related notification events. [SpConnectionNotification](#spconnectionnotification)Notifications related to the connection to [Spotify.](#spotify) [SpDeviceType](#spdevicetype)Device type reported to client applications. [SpMetadataTrack](#spmetadatatrack)Metadata track selector. [SpConnectivity](#spconnectivity)Type of network connection. [SpContent](#spcontent)Content type. [SpMediaType](#spmediatype)Media Type. [SpAudioQuality](#spaudioquality)Audio quality. [SpDrmFormat](#spdrmformat)DRM formats. [SpReDeliveryMode](#spredeliverymode)Redelivery mode types.

## Functions

* * *

[Return to header index](#main)

[SpInit](#spinit)Initialize the library. [SpFree](#spfree)Shut down the library. [SpGetLibraryVersion](#spgetlibraryversion)Retrieve a version string for the library. [SpConnectionSetConnectivity](#spconnectionsetconnectivity)Set the type of network connection of the device. [SpConnectionGetConnectivity](#spconnectiongetconnectivity)Get the connectivity that was set with [SpConnectionSetConnectivity()](#spconnectionsetconnectivity) [SpConnectionLoginBlob](#spconnectionloginblob)Log in a user to Spotify using a credentials blob. [SpConnectionLoginOauthToken](#spconnectionloginoauthtoken)Log in a user to Spotify using a Spotify OAuth token. [SpConnectionLogout](#spconnectionlogout)Log the user out of [Spotify.](#spotify) [SpConnectionIsLoggedIn](#spconnectionisloggedin)Is the user logged in to [Spotify.](#spotify) [SpConnectionGetAckId](#spconnectiongetackid)Get the last Ack ID. [SpGetCanonicalUsername](#spgetcanonicalusername)Get the canonical username of the logged in user. [SpSetDisplayName](#spsetdisplayname)Set the display name for the device or application. [SpSetVolumeSteps](#spsetvolumesteps)Set the volume steps the device is capable of. [SpSetDeviceIsGroup](#spsetdeviceisgroup)Control if the device represents a group. [SpEnableConnect](#spenableconnect)Enable Connect functionality for this device. [SpDisableConnect](#spdisableconnect)Disable Connect functionality for this device. [SpGetSelectedDeviceAlias](#spgetselecteddevicealias)Return the currently selected device alias. [SpPumpEvents](#sppumpevents)Allow the library to perform asynchronous tasks and process events. [SpRegisterConnectionCallbacks](#spregisterconnectioncallbacks)Register callbacks related to the connection to [Spotify.](#spotify) [SpRegisterDebugCallbacks](#spregisterdebugcallbacks)Register a callback that receives debug messages/trace logs. [SpRegisterPlaybackCallbacks](#spregisterplaybackcallbacks)Register playback-related callbacks. [SpGetMetadata](#spgetmetadata)Retrieve metadata for a track in the current track list. [SpGetMetadataImageURL](#spgetmetadataimageurl)Return the HTTP URL to an image file from a spotify:image: URI. [SpGetPlayerCookie](#spgetplayercookie)Obtain player cookie for current playback. [SpPlaybackPlay](#spplaybackplay)Start or resume playback. [SpPlaybackPause](#spplaybackpause)Pause playback. [SpPlaybackSkipToNext](#spplaybackskiptonext)Skip playback to the next track in the track list. [SpPlaybackSkipToPrev](#spplaybackskiptoprev)Skip playback to the previous track in the track list. [SpPlaybackSeek](#spplaybackseek)Seek to a position within the current track. [SpPlaybackSeekRelative](#spplaybackseekrelative)Seek a relative amount of time within the current track. [SpPlaybackGetPosition](#spplaybackgetposition)Get the current playback position within the track. [SpPlaybackUpdateVolume](#spplaybackupdatevolume)Request a change to the playback volume. [SpPlaybackGetVolume](#spplaybackgetvolume)Get the playback volume level. [SpPlaybackIsPlaying](#spplaybackisplaying)Is the playback status playing or paused. [SpPlaybackIsAdPlaying](#spplaybackisadplaying)Is the current track an Ad or not. [SpPlaybackIsShuffled](#spplaybackisshuffled)Is "shuffle" mode enabled. [SpPlaybackIsRepeated](#spplaybackisrepeated)Is "repeat" mode enabled. [SpPlaybackGetRepeatMode](#spplaybackgetrepeatmode)Which "repeat" mode is on. [SpPlaybackIsActiveDevice](#spplaybackisactivedevice)Is the device the active playback device. [SpPlaybackEnableShuffle](#spplaybackenableshuffle)Enable or disable "shuffle" mode. [SpPlaybackEnableRepeat](#spplaybackenablerepeat)Enable or disable "repeat" mode. [SpPlaybackCycleRepeatMode](#spplaybackcyclerepeatmode)Cycle through the available repeat modes. [SpPlaybackSetBitrate](#spplaybacksetbitrate)Change the bitrate at which compressed audio data is delivered. [SpPlaybackSetDeviceInactive](#spplaybacksetdeviceinactive)Set the device inactive. [SpPlaybackIsDeviceControllable](#spplaybackisdevicecontrollable)Is the device controllable. [SpPlaybackSetDeviceControllable](#spplaybacksetdevicecontrollable)Allow or disallow the device to be controllable. [SpPlaybackIncreaseUnderrunCount](#spplaybackincreaseunderruncount)Increase the underrun counter of the current track. [SpPlaybackSetBandwidthLimit](#spplaybacksetbandwidthlimit)Set a limit on the download speed. [SpPlaybackSetRedeliveryMode](#spplaybacksetredeliverymode)Activates redelivery of audio data on play or resume playback. [SpPlaybackIsRedeliveryModeActivated](#spplaybackisredeliverymodeactivated)Gets the status of redelivery mode. [SpZeroConfGetVars](#spzeroconfgetvars)Get variables for ZeroConf, mainly the "getInfo" request. [SpZeroConfAnnouncePause](#spzeroconfannouncepause)Temporarily pause ZeroConf mDNS announcements. [SpZeroConfAnnounceResume](#spzeroconfannounceresume)Resume ZeroConf mDNS announcement after calling [SpZeroConfAnnouncePause()](#spzeroconfannouncepause) [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)Log in a user to Spotify using a ZeroConf credentials blob. [SpGetBrandName](#spgetbrandname)[SpGetModelName](#spgetmodelname)[SpRegisterDeviceAliasCallbacks](#spregisterdevicealiascallbacks)Register callbacks related to device aliases. [SpSetDeviceAliases](#spsetdevicealiases)Update the device alias definitions. [SpSetAdUserAgent](#spsetaduseragent)Set the ad user agent. [SpRestrictDrmMediaFormats](#sprestrictdrmmediaformats)Restrict DRM/Media formats.

### SP\_API\_VERSION

* * *

[*Return to header index*](#main)

`1`

`#define SP_API_VERSION 82`

The version of the API defined in this header file.

**See also**

- [SpInit](#spinit)

### SP\_RECOMMENDED\_MEMORY\_BLOCK\_SIZE

* * *

[*Return to header index*](#main)

`1`

`#define SP_RECOMMENDED_MEMORY_BLOCK_SIZE 1024 * 1024`

Minimum recommended size of the buffer [SpConfig::memory\_block.](#spconfig::memory_block)

### SP\_MAX\_BRAND\_NAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_BRAND_NAME_LENGTH 32`

Maximum length of the brand name string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_MODEL\_NAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_MODEL_NAME_LENGTH 30`

Maximum length of the model name string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_PLATFORM\_NAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PLATFORM_NAME_LENGTH 64`

Maximum length of the platform\_name string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_CLIENT\_ID\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_CLIENT_ID_LENGTH 32`

Maximum length of the client id string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_OS\_VERSION\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_OS_VERSION_LENGTH 64`

Maximum length of the os version string (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_DISPLAY\_NAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_DISPLAY_NAME_LENGTH 64`

Maximum length of the device display name (not counting terminating NULL)

**See also**

- [SpSetDisplayName](#spsetdisplayname)
- [SpConfig](#spconfig)
- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_AD\_USER\_AGENT\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_AD_USER_AGENT_LENGTH 256`

Maximum length of the ad UserAgent (not counting terminating NULL)

**See also**

- [SpSetAdUserAgent](#spsetaduseragent)

### SP\_MAX\_UNIQUE\_ID\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_UNIQUE_ID_LENGTH 64`

Maximum length of the device's unique ID (not counting terminating NULL)

**See also**

- [SpConfig](#spconfig)

### SP\_MAX\_USERNAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_USERNAME_LENGTH 64`

Maximum length of usernames (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)
- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_DEVICE\_ALIASES

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_DEVICE_ALIASES 8`

Maximum number of device aliases that can be configured.

**See also**

- [SpConfig::device\_aliases](#spconfig)

### SP\_MAX\_AD\_METADATA\_PAIRS

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_AD_METADATA_PAIRS 4`

Maximum number of key/value pairs containing ad metadata.

### SP\_NO\_ALIAS\_SELECTED

* * *

[*Return to header index*](#main)

`1`

`#define SP_NO_ALIAS_SELECTED -1`

A value to use for alias\_index when aliases are not used.

**See also**

- [SpConfig::device\_aliases](#spconfig)

### SP\_MAX\_PLAYER\_MODES

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PLAYER_MODES 8`

Maximum number of Player Option Modes eSDK can provide when calling [SpPlaybackGetPlayerModes()](#spplaybackgetplayermodes)

Note: reserved for future use.

### SP\_MAX\_MODE\_KEY\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_MODE_KEY_LENGTH 32`

Maximum length of the key field in *struct* [SpPlayerModePair.](#spplayermodepair)

Note: reserved for future use.

### SP\_MAX\_MODE\_VALUE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_MODE_VALUE_LENGTH 32`

Maximum length of the value field in *struct* [SpPlayerModePair.](#spplayermodepair)

Note: reserved for future use.

### SP\_MAX\_METADATA\_NAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_METADATA_NAME_LENGTH 255`

Maximum length of display names in track metadata (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

**Notes:**

- It is possible that metadata will be truncated to less than this length. Applications requiring full length metadata should request it from the Spotify web APIs ([https://developer.spotify.com/documentation/web-api/](https://developer.spotify.com/documentation/web-api/))

### SP\_MAX\_METADATA\_URI\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_METADATA_URI_LENGTH 127`

Maximum length of URIs in track metadata (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

### SP\_MAX\_TRACK\_UID\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_TRACK_UID_LENGTH 64`

Maximum length of Track UID in track metadata (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

### SP\_MAX\_METADATA\_IMAGE\_URL\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_METADATA_IMAGE_URL_LENGTH 255`

Maximum length of URLs (not counting terminating NULL)

**See also**

- [SpGetMetadataImageURL](#spgetmetadataimageurl)

### SP\_PLAYER\_COOKIE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYER_COOKIE_LENGTH 32`

Length of player cookie (not counting terminating NULL)

**See also**

- [SpGetPlayerCookie](#spgetplayercookie)

### SP\_MAX\_PLAYBACK\_ID\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PLAYBACK_ID_LENGTH 32`

Maximum length of Playback-Id (not counting terminating NULL)

**See also**

- [SpGetMetadata](#spgetmetadata)
- [SpMetadata](#spmetadata)

### SP\_MAX\_PUBLIC\_KEY\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PUBLIC_KEY_LENGTH 149`

Maximum length of the public key used in ZeroConf logins (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_DEVICE\_ID\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_DEVICE_ID_LENGTH 64`

Maximum length of the device ID used for ZeroConf logins (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_DEVICE\_TYPE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_DEVICE_TYPE_LENGTH 15`

Maximum length of the device type string (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_VERSION\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_VERSION_LENGTH 30`

Maximum length of the library version string (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_GROUP\_STATUS\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_GROUP_STATUS_LENGTH 15`

Maximum length of the group status string (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_TOKEN\_TYPE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_TOKEN_TYPE_LENGTH 30`

Maximum length of the token type used for OAuth logins (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_SCOPE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_SCOPE_LENGTH 64`

Maximum length of the scope used for OAuth login (not counting terminating NULL)

**See also**

- [SpZeroConfVars](#spzeroconfvars)

### SP\_MAX\_CLIENT\_KEY\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_CLIENT_KEY_LENGTH 511`

Maximum length of the client key (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_ZEROCONF\_BLOB\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_ZEROCONF_BLOB_LENGTH 2047`

Maximum length of the ZeroConf blob (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_LOGIN\_ID\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_LOGIN_ID_LENGTH 64`

Maximum length of the login ID used for ZeroConf logins (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_AVAILABILITY\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_AVAILABILITY_LENGTH 15`

Maximum length of the availability string (not counting terminating NULL)

**See also**

- [SpConnectionLoginZeroConf](#spconnectionloginzeroconf)

### SP\_MAX\_PARTNER\_NAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PARTNER_NAME_LENGTH 48`

Maximum length of the Partner Name (TSP\_PARTNER\_NAME) (not counting terminating NULL) The longest partner name when this was written was "imagination\_technologies\_mips" at 29 characters.

### SP\_MAX\_FILENAME\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_FILENAME_LENGTH 63`

Maximum length of filename fields (not counting terminating NULL)

### SP\_MAX\_RESPONSE\_SOURCE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_RESPONSE_SOURCE_LENGTH 20`

Maximum length of the response source string (not counting terminating NULL)

### SP\_ZEROCONF\_DISABLED

* * *

[*Return to header index*](#main)

`1`

`#define SP_ZEROCONF_DISABLED 0`

Value for [SpConfig::zeroconf\_serve](#spconfig) when disabling built-in ZeroConf stack. Complete ZeroConf stack has to run externally.

**See also**

- [SpInit](#spinit)

### SP\_ZEROCONF\_SERVE

* * *

[*Return to header index*](#main)

`1`

`#define SP_ZEROCONF_SERVE 1`

Value for [SpConfig::zeroconf\_serve](#spconfig) when activating complete built-in ZeroConf stack (both mDNS and http server).

**See also**

- [SpInit](#spinit)

### SP\_ZEROCONF\_SERVE\_HTTP\_ONLY

* * *

[*Return to header index*](#main)

`1`

`#define SP_ZEROCONF_SERVE_HTTP_ONLY 2`

Value for [SpConfig::zeroconf\_serve](#spconfig) when activating built-in ZeroConf http server only while running the ZeroConf mDNS server externally.

**See also**

- [SpInit](#spinit)

### SP\_ZEROCONF\_SERVE\_MDNS\_ONLY

* * *

[*Return to header index*](#main)

`1`

`#define SP_ZEROCONF_SERVE_MDNS_ONLY 3`

Value for [SpConfig::zeroconf\_serve](#spconfig) when activating built-in ZeroConf mDNS server only while running the ZeroConf http server externally.

**See also**

- [SpInit](#spinit)

### SP\_SCOPE\_STREAMING

* * *

[*Return to header index*](#main)

`1`

`#define SP_SCOPE_STREAMING "streaming"`

Value for [SpConfig::scope](#spconfig) when implementing a basic streaming device.

### SP\_DEVICE\_ALIAS\_ATTRIBUTE\_GROUP

* * *

[*Return to header index*](#main)

`1`

`#define SP_DEVICE_ALIAS_ATTRIBUTE_GROUP 1`

Set this bit in the device alias attributes integer ([SpDeviceAlias::attributes](#spdevicealias)) to mark a device alias as representing a group.

**Notes:**

- [SpSetDeviceIsGroup](#spsetdeviceisgroup) also sets group status, but only for the currently selected alias.

### SP\_GLOBAL\_ATTRIBUTE\_VOICE

* * *

[*Return to header index*](#main)

`1`

`#define SP_GLOBAL_ATTRIBUTE_VOICE 2`

Set this bit in the global attributes integer ([SpConfig::global\_attributes](#spconfig)) to mark that this device supports voice.

### SP\_MAX\_SUPPORTED\_FORMATS

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_SUPPORTED_FORMATS 8`

**See also**

- [SpFormat](#spformat)
- [SpConfig::supported\_drm\_media\_formats](#spconfig)

### SP\_PLAYBACK\_RESTRICTION\_ALREADY\_PAUSED

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_ALREADY_PAUSED 1`

The track is already paused.

### SP\_PLAYBACK\_RESTRICTION\_NOT\_PAUSED

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_NOT_PAUSED 2`

The track is already playing.

### SP\_PLAYBACK\_RESTRICTION\_LICENSE\_DISALLOW

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_LICENSE_DISALLOW 4`

Licensing rules disallow this action.

### SP\_PLAYBACK\_RESTRICTION\_AD\_DISALLOW

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_AD_DISALLOW 8`

Action can't be performed while an ad is playing.

### SP\_PLAYBACK\_RESTRICTION\_NO\_PREV\_TRACK

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_NO_PREV_TRACK 16`

There is no track before the current one in the currently playing context.

### SP\_PLAYBACK\_RESTRICTION\_NO\_NEXT\_TRACK

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_NO_NEXT_TRACK 32`

There is no track after the current one in the currently playing context.

### SP\_PLAYBACK\_RESTRICTION\_UNKNOWN

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_UNKNOWN 64`

The action is restricted, but no reason is provided.

This means that eSDK has not retrieved the restrictions from the backend yet and therefore the action is not allowed right now. As soon as eSDK retrieves the information, the notification kSpPlaybackNotifyMetadataChanged will be sent, and the application can check the field again.

### SP\_PLAYBACK\_RESTRICTION\_ENDLESS\_CONTEXT

* * *

[*Return to header index*](#main)

`1`

`#define SP_PLAYBACK_RESTRICTION_ENDLESS_CONTEXT 128`

The action is restricted for context level reasons.

### SP\_MAX\_PLAYER\_MODES\_RESTRICTIONS

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PLAYER_MODES_RESTRICTIONS`

Maximum number of Player Mode Restrictions eSDK can provide through [SpPlaybackRestrictions](#spplaybackrestrictions) in Metadata.

Note: reserved for future use.

### SP\_MAX\_PLAYER\_MODE\_VALUE\_DISALLOW\_REASONS

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_PLAYER_MODE_VALUE_DISALLOW_REASONS 16`

Maximum number of restriction disallow reasons per value of a Player Mode.

### SP\_MAX\_METADATA\_KEY\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_METADATA_KEY_LENGTH 32`

Maximum number of characters in the key of a [SpAdMetadata](#spadmetadata) *struct*, not counting the terminating NULL.

**See also**

- [SpAdMetadata](#spadmetadata)

### SP\_MAX\_METADATA\_VALUE\_LENGTH

* * *

[*Return to header index*](#main)

`1`

`#define SP_MAX_METADATA_VALUE_LENGTH 64`

Maximum number of characters in the value of a [SpAdMetadata](#spadmetadata) *struct*, not counting the terminating NULL.

**See also**

- [SpAdMetadata](#spadmetadata)

### SpPlayerModeDisallowReasons

* * *

[*Return to header index*](#main)

`1`

`struct SpPlayerModeDisallowReasons {`

`2`

`char value;`

`3`

`uint32_t disallow_reasons;`

`4`

`};`

This *struct* stores a Mode value and the restriction disallow reasons associated with it.

*char* valueA null-terminated string to represent the value of the restricted Player Mode. *uint32\_t* disallow\_reasonsBitfield of reasons for disallowing setting the mode value.

### SpPlayerModeRestrictions

* * *

[*Return to header index*](#main)

`1`

`struct SpPlayerModeRestrictions {`

`2`

`char key;`

`3`

`struct SpPlayerModeDisallowReasons reasons;`

`4`

`};`

this *struct* stores a Mode key and the list of restricted values.

*char* keyA null-terminated string to represent the key of the Player Mode that is restricted. *struct* [SpPlayerModeDisallowReasons](#spplayermodedisallowreasons) reasonsthe list of restricted values and the disallow reasons.

### SpPlaybackRestrictions

* * *

[*Return to header index*](#main)

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

Playback restrictions.

*uint32\_t* disallow\_pausing\_reasonsBitfield of reasons the pause action is not allowed. *uint32\_t* disallow\_resuming\_reasonsBitfield of reasons the resume action is not allowed. *uint32\_t* disallow\_seeking\_reasonsBitfield of reasons seeking is not allowed. *uint32\_t* disallow\_peeking\_prev\_reasonsBitfield of reasons peeking on the previous track is not allowed. *uint32\_t* disallow\_peeking\_next\_reasonsBitfield of reasons peeking on the next track is not allowed. *uint32\_t* disallow\_skipping\_prev\_reasonsBitfield of reasons skipping to the previous track is not allowed. *uint32\_t* disallow\_skipping\_next\_reasonsBitfield of reasons skipping to the next track is not allowed. *uint32\_t* disallow\_toggling\_repeat\_context\_reasonsBitfield of reasons setting repeat context is not allowed. *uint32\_t* disallow\_toggling\_repeat\_track\_reasonsBitfield of reasons setting repeat track is not allowed. *uint32\_t* disallow\_toggling\_shuffle\_reasonsBitfield of reasons toggling shuffle is not allowed.

### SpFormat

* * *

[*Return to header index*](#main)

`1`

`struct SpFormat {`

`2`

`enum SpDrmFormat drm;`

`3`

`uint64_t media;`

`4`

`};`

Mapping of which media formats are supported in which DRM.

**See also**

- [SpConfig::supported\_drm\_media\_formats](#spconfig)

*enum* [SpDrmFormat](#spdrmformat) drmDRM format which the integration supports. uint64\_t mediaSupported media formats for a DRM.

### SpMetadata

* * *

[*Return to header index*](#main)

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

Track metadata.

**See also**

- [SpGetMetadata](#spgetmetadata)

*char* playback\_sourceDisplay name of the playback source. E.g., the name of the playlist from which playback was initiated (UTF-8-encoded) *char* playback\_source\_uriSpotify URI of the playback source (in the form "spotify:xxxxxx:xxxxxxx...") *char* trackDisplay name of the track (UTF-8-encoded) *char* track\_uriSpotify URI of the track (in the form "spotify:track:xxxxxxx...") *char* artistDisplay name of the artist of the track (UTF-8-encoded) *char* artist\_uriSpotify URI of the artist of the track (in the form "spotify:artist:xxxxxxx...") *char* albumDisplay name of the track's album (UTF-8-encoded) *char* album\_uriSpotify URI of the track's album (in the form "spotify:album:xxxxxxx...") *char* album\_cover\_uriSpotify URI of the album's cover art image (in the form "spotify:image:xxxxxxx...") *char* original\_track\_uriSpotify URI of the original track before relinking (in the form "spotify:track:xxxxxxx...") *uint32\_t* duration\_msPlayback duration of the track in milliseconds. *int32\_t* indexIndex of the track in the currently playing context. *char* track\_uidTrack UID of the track in the currently playing context. *uint32\_t* original\_indexIndex of the track in the original (unchanged) playing context. *uint32\_t* bitrateThe bitrate of the track in kbps. 0 means "unplayable". *struct* [SpPlaybackRestrictions](#spplaybackrestrictions) playback\_restrictionsRestrictions that apply to playback and transitions related to this track. *char* playback\_idPlayback-id of this playback of this specific track. *enum* [SpContent](#spcontent) content\_typeContent type of this track. *enum* [SpMediaType](#spmediatype) media\_typeMedia type of this track. *enum* [SpAudioQuality](#spaudioquality) audio\_qualityAudio quality of this track.

### SpAdMetadata

* * *

[*Return to header index*](#main)

`1`

`struct SpAdMetadata {`

`2`

`char key;`

`3`

`char value;`

`4`

`};`

Key value pair for Ad-related metadata.

*char* keyKey. *char* valueValue.

### SpZeroConfDeviceAlias

* * *

[*Return to header index*](#main)

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

ZeroConf DeviceAlias.

This structure contains information about a single device alias, as returned by [SpZeroConfGetVars()](#spzeroconfgetvars).

**See also**

- [SpZeroConfGetVars](#spzeroconfgetvars)

*uint32\_t* idString to be sent in the "id" field of the alias in the "getInfo" response. *int* is\_groupBoolean (0 = "false", 1 = "true") to be sent in the "isGroup" field of the alias in the "getInfo" response. *char* display\_nameString to be sent in the "name" field of the alias in the "getInfo" response.

### SpZeroConfVars

* * *

[*Return to header index*](#main)

`1`

`struct SpZeroConfVars {`

`2`

`char public_key;`

`3`

`char response_source;`

`4`

`char device_id;`

`5`

`char remote_name;`

`6`

`char device_type;`

`7`

`char library_version;`

`8`

`int resolver_version;`

`9`

`char group_status;`

`10`

`int webserver_current_port;`

`11`

`char token_type;`

`12`

`char client_id;`

`13`

`char scope;`

`14`

`char availability;`

`15`

`uint32_t product_id;`

`16`

`struct SpZeroConfDeviceAlias aliases;`

`17`

`uint32_t alias_count;`

`18`

`struct SpFormat supported_drm_media_formats;`

`19`

`uint64_t supported_capabilities;`

`20`

`};`

ZeroConf variables.

This structure contains the fields that the application needs for ZeroConf, mainly what to send in the response to the "getInfo" request. See the ZeroConf manual for more information.

**See also**

- [SpZeroConfGetVars](#spzeroconfgetvars)

*char* public\_keyString to be sent in the "publicKey" field of the "getInfo" response\[\*]. *char* response\_sourceString to be sent in the "responseSource" field of the "getInfo" response\[\*]. *char* device\_idString to be sent in the "deviceID" field of the "getInfo" response\[\*]. *char* remote\_nameString to be sent in the "remoteName" field of the "getInfo" response\[\*]. *char* device\_typeString to be sent in the "deviceType" field of the "getInfo" response\[\*]. *char* library\_versionString to be sent in the "libraryVersion" field of the "getInfo" response\[\*]. *int* resolver\_versionInteger to be sent as string in the "resolverVersion" field of the "getInfo" response\[\*]. *char* group\_statusString to be sent in the "groupStatus" field of the "getInfo" response\[\*]. *int* webserver\_current\_portCurrent internal ZeroConf webserver port number. To be used when running an external mDNS server together with an internal webserver. *char* token\_typeString to be sent in the "tokenType" field of the "getInfo" response\[\*]. *char* client\_idString to be sent in the "clientID" field of the "getInfo" response\[\*]. *char* scopeString to be sent in the "scope" field of the "getInfo" response\[\*]. *char* availabilityString to be sent in the "availability" field of the "getInfo" response\[\*]. *uint32\_t* product\_idInteger to be sent in the "productID" field of the "getInfo" response\[\*]. *struct* [SpZeroConfDeviceAlias](#spzeroconfdevicealias) aliasesArray of [SpZeroConfDeviceAlias](#spzeroconfdevicealias) to be sent in the "aliases" field of the "getInfo" response\[\*]. *uint32\_t* alias\_countNumber of valid items in aliases array. *struct* [SpFormat](#spformat) supported\_drm\_media\_formatsArray of [SpFormat](#spformat) to be sent in the "supported\_drm\_media\_formats" field of the "getInfo" response\[\*]. uint64\_t supported\_capabilitiesInteger representing a bitmask to be sent in the "supported\_capabilities" field of the "getInfo" response\[\*].

### SpSampleFormat

* * *

[*Return to header index*](#main)

`1`

`struct SpSampleFormat {`

`2`

`int channels;`

`3`

`int sample_rate;`

`4`

`int bits_per_sample;`

`5`

`};`

Sample format of the audio data.

*int* channelsNumber of channels (1 = mono, 2 = stereo) *int* sample\_rateSample rate in Hz (such as 22050, 44100 or 48000) *int* bits\_per\_sampleBits per sample (16 or 24)

### SpPlaybackCallbacks

* * *

[*Return to header index*](#main)

`1`

`struct SpPlaybackCallbacks {`

`2`

`SpCallbackPlaybackNotify on_notify;`

`3`

`SpCallbackPlaybackSeek on_seek;`

`4`

`SpCallbackPlaybackApplyVolume on_apply_volume;`

`5`

`};`

Callbacks to be registered with [SpRegisterPlaybackCallbacks()](#spregisterplaybackcallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackPlaybackNotify](#spcallbackplaybacknotify) on\_notifyNotification callback. [SpCallbackPlaybackSeek](#spcallbackplaybackseek) on\_seekSeek position callback. [SpCallbackPlaybackApplyVolume](#spcallbackplaybackapplyvolume) on\_apply\_volumeApply volume callback.

### SpDebugCallbacks

* * *

[*Return to header index*](#main)

`1`

`struct SpDebugCallbacks {`

`2`

`SpCallbackDebugMessage on_message;`

`3`

`};`

Callbacks to be registered with [SpRegisterDebugCallbacks()](#spregisterdebugcallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackDebugMessage](#spcallbackdebugmessage) on\_messageDebug message callback.

### SpConnectionCallbacks

* * *

[*Return to header index*](#main)

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

Callbacks to be registered with [SpRegisterConnectionCallbacks()](#spregisterconnectioncallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackConnectionNotify](#spcallbackconnectionnotify) on\_notifyNotification callback. [SpCallbackConnectionNewCredentials](#spcallbackconnectionnewcredentials) on\_new\_credentialsCredentials blob callback. [SpCallbackConnectionMessage](#spcallbackconnectionmessage) on\_messageConnection message callback.

### SpDeviceAlias

* * *

[*Return to header index*](#main)

`1`

`struct SpDeviceAlias {`

`2`

`const char *display_name;`

`3`

`uint32_t attributes;`

`4`

`};`

Device alias definition.

This *struct* is used to define (optional) device aliases. It's a part of the [SpConfig](#spconfig) *struct* which will be passed to [SpInit()](#spinit) to initialize the eSDK.

*const* *char* * display\_nameA UTF-8 encoded display name for an alias of the application/device. *uint32\_t* attributesAttributes for this device alias.

### SpConfig

* * *

[*Return to header index*](#main)

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

`const char *platform_name;`

`14`

`const char *client_id;`

`15`

`uint32_t product_id;`

`16`

`const char *scope;`

`17`

`const char *os_version;`

`18`

`enum SpDeviceType device_type;`

`19`

`enum SpPlaybackBitrate max_bitrate;`

`20`

`SpCallbackError error_callback;`

`21`

`void *error_callback_context;`

`22`

`int zeroconf_serve;`

`23`

`const char *host_name;`

`24`

`int zeroconf_port;`

`25`

`int zeroconf_port_range;`

`26`

`struct SpFormat supported_drm_media_formats;`

`27`

`struct SpAdMetadata ad_metadata;`

`28`

`};`

Configuration.

**See also**

- [SpInit](#spinit)

*int* api\_versionThe version of the API contained in this header file. Must be set to SP\_API\_VERSION. *void* * memory\_blockPointer to a memory block to be used by the library. *uint32\_t* memory\_block\_sizeSize of the memory\_block buffer in bytes. *const* *char* * unique\_idA NULL-terminated character string that uniquely identifies the device (such as a MAC address) *const* *char* * display\_nameA UTF-8-encoded display name for the application/device. *uint32\_t* global\_attributesThe global attributes is a bitfield where each attribute is OR:ed together and stored in this integer. *struct* [SpDeviceAlias](#spdevicealias) device\_aliasesDevice alias definitions. These are optional, if you don't want to define aliases this array must be zeroed. *const* *char* * brand\_nameA NULL-terminated string containing the brand name of the hardware device (for hardware integrations) *const* *char* * brand\_display\_nameA UTF-8-encoded brand name of the hardware device (for hardware integrations). Should be very similar to brand\_name. *const* *char* * model\_nameA NULL-terminated string containing the model name of the hardware device (for hardware integrations) *const* *char* * model\_display\_nameA UTF-8-encoded model name of the hardware device (for hardware integrations) *const* *char* * platform\_nameA NULL-terminated string containing the platform identifier. *const* *char* * client\_idA NULL-terminated string containing the client id of the application. *uint32\_t* product\_idAn integer enumerating the product for this partner. *const* *char* * scopeA NULL-terminated string containing the OAuth scope requested when authenticating with the Spotify backend. *const* *char* * os\_versionA NULL-terminated string containing the os version running on the hardware. *enum* [SpDeviceType](#spdevicetype) device\_typeThe device type that best describes this product. *enum* [SpPlaybackBitrate](#spplaybackbitrate) max\_bitrateThe maximum bitrate to use for playback. [SpCallbackError](#spcallbackerror) error\_callbackPointer to a callback function that will receive error notifications. *void* * error\_callback\_contextApplication-defined pointer that will be passed unchanged as the context argument to the error\_callback callback. *int* zeroconf\_serveNot applicable in this eSDK configuration. *const* *char* * host\_nameNot applicable in this eSDK configuration. *int* zeroconf\_portNot applicable in this eSDK configuration. *int* zeroconf\_port\_rangeNot applicable in this eSDK configuration. *struct* [SpFormat](#spformat) supported\_drm\_media\_formats*struct* [SpAdMetadata](#spadmetadata) ad\_metadataFor clients that need to register ad-relasted metadata.

### SpDeviceAliasCallbacks

* * *

[*Return to header index*](#main)

`1`

`struct SpDeviceAliasCallbacks {`

`2`

`SpCallbackSelectedDeviceAliasChanged on_selected_device_alias_changed;`

`3`

`SpCallbackDeviceAliasesUpdateDone on_device_aliases_update_done;`

`4`

`};`

Callbacks to be registered with [SpRegisterDeviceAliasCallbacks()](#spregisterdevicealiascallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackSelectedDeviceAliasChanged](#spcallbackselecteddevicealiaschanged) on\_selected\_device\_alias\_changedSelected device alias updated callback. [SpCallbackDeviceAliasesUpdateDone](#spcallbackdevicealiasesupdatedone) on\_device\_aliases\_update\_doneDevice alias list updated.

### SpCallbackError

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackError) (SpError error, void *context)`

Callback for reporting errors to the application.

To register this callback, set the field [SpConfig::error\_callback](#spconfig) when invoking the function [SpInit()](#spinit).

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackPlaybackNotify

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackPlaybackNotify) (enum SpPlaybackNotification event, void *context)`

Callback for notifying the application about playback-related events.

To register this callback, use the function [SpRegisterPlaybackCallbacks()](#spregisterplaybackcallbacks).

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackPlaybackSeek

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackPlaybackSeek) (uint32_t position_ms, void *context)`

Callback to notify the application of a change in the playback position.

To register this callback, use the function [SpRegisterPlaybackCallbacks()](#spregisterplaybackcallbacks). This callback is invoked when [SpPlaybackSeek()](#spplaybackseek) is invoked or when the user seeks to a position within the track using Spotify Connect.

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackPlaybackApplyVolume

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackPlaybackApplyVolume) (uint16_t volume, uint8_t remote, void *context)`

Callback to notify the application of a volume change using Spotify Connect.

To register this callback, use the function [SpRegisterPlaybackCallbacks()](#spregisterplaybackcallbacks). This callback is invoked in two cases: When the user changes the playback volume using Spotify Connect. When the application invoked [SpPlaybackUpdateVolume()](#spplaybackupdatevolume). In both cases, the application is responsible for applying the new volume to its audio output. The application should never invoke [SpPlaybackUpdateVolume()](#spplaybackupdatevolume) from this callback, as this might result in an endless loop.

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackConnectionNotify

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackConnectionNotify) (enum SpConnectionNotification event, void *context)`

Callback for notifying the application about events related to the connection to [Spotify.](#spotify)

To register this callback, use the function [SpRegisterConnectionCallbacks()](#spregisterconnectioncallbacks).

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackConnectionNewCredentials

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackConnectionNewCredentials) (const char *credentials_blob, const char *username, void *context)`

Callback for passing a login blob to the application.

To register this callback, use the function [SpRegisterConnectionCallbacks()](#spregisterconnectioncallbacks). The application may save the credentials\_blob for subsequent logins using the function [SpConnectionLoginBlob()](#spconnectionloginblob). The application should also discard any credentials blobs for this user that it received previously, either through this callback or through ZeroConf (see the ZeroConf manual). Note: If credentials\_blob is an empty string, the application MUST delete any existing saved credentials for the account, and must not attempt to login again with the empty credentials. This happens when a permanent logout is requested.

**See also**

- [SpConnectionLoginBlob](#spconnectionloginblob)

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackConnectionMessage

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackConnectionMessage) (const char *message, void *context)`

Callback for sending a message to the user.

To register this callback, use the function [SpRegisterConnectionCallbacks()](#spregisterconnectioncallbacks). This callback is invoked when Spotify wants to display a message to the user. The message is meant to be displayed to the user as-is and should not be interpreted by the application (the format of the messages may change without notice). If the application does not have a graphical user interface, it can safely ignore this callback.

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackDebugMessage

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackDebugMessage) (const char *debug_message, void *context)`

Callback for sending debug messages/trace logs.

To register this callback, use the function [SpRegisterDebugCallbacks()](#spregisterdebugcallbacks). In special builds of the library, this callback receives debug messages that the application may write to its logs. The application should not interpret the messages (the format of the messages may change without notice).

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackSelectedDeviceAliasChanged

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackSelectedDeviceAliasChanged) (uint32_t alias_index, void *context)`

Callback for receiving the selected device alias from the backend.

To register this callback, use the function [SpRegisterDeviceAliasCallbacks()](#spregisterdevicealiascallbacks). This callback is invoked whenever the selected device alias is updated. This can happen when, for example, the user selects an alias from Spotify Connect device picker.

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpCallbackDeviceAliasesUpdateDone

* * *

[*Return to header index*](#main)

`1`

`typedef void(* SpCallbackDeviceAliasesUpdateDone) (SpError error_code, void *context)`

Callback for knowing when the device alias list has been updated after call to [SpSetDeviceAliases()](#spsetdevicealiases)

To register this callback, use the function [SpRegisterDeviceAliasCallbacks()](#spregisterdevicealiascallbacks). This callback is invoked when the operation started by [SpSetDeviceAliases()](#spsetdevicealiases) has finished.

**Notes:**

- The application should not block or call API functions that are not allowed in the callback.

### SpError

* * *

[*Return to header index*](#main)

Error codes.

These are the possible status codes returned by functions in the SDK. They should be used to determine if an action was successful, and if not, why the action failed.

**See also**

- [SpCallbackError](#spcallbackerror)

### SpAPIReturnCode

* * *

[*Return to header index*](#main)

`1`

`enum SpAPIReturnCode {`

`2`

`3`

`};`

Enum describes return codes that public API functions can report to eSDK.

### SpPlaybackBitrate

* * *

[*Return to header index*](#main)

`1`

`enum SpPlaybackBitrate {`

`2`

`3`

`};`

Valid bitrate values. This *enum* is used for selecting the audio quality of the files to play.

**See also**

- [SpPlaybackSetBitrate](#spplaybacksetbitrate)

### SpPlaybackNotification

* * *

[*Return to header index*](#main)

`1`

`enum SpPlaybackNotification {`

`2`

`3`

`};`

Playback-related notification events.

**See also**

- [SpCallbackPlaybackNotify](#spcallbackplaybacknotify)

### SpConnectionNotification

* * *

[*Return to header index*](#main)

`1`

`enum SpConnectionNotification {`

`2`

`3`

`};`

Notifications related to the connection to [Spotify.](#spotify)

**See also**

- [SpCallbackConnectionNotify](#spcallbackconnectionnotify)

### SpDeviceType

* * *

[*Return to header index*](#main)

Device type reported to client applications.

### SpMetadataTrack

* * *

[*Return to header index*](#main)

`1`

`enum SpMetadataTrack {`

`2`

`3`

`};`

Metadata track selector.

**See also**

- [SpGetMetadata](#spgetmetadata)

### SpConnectivity

* * *

[*Return to header index*](#main)

`1`

`enum SpConnectivity {`

`2`

`3`

`};`

Type of network connection.

**See also**

- [SpConnectionSetConnectivity](#spconnectionsetconnectivity)

### SpContent

* * *

[*Return to header index*](#main)

Content type.

### SpMediaType

* * *

[*Return to header index*](#main)

Media Type.

### SpAudioQuality

* * *

[*Return to header index*](#main)

`1`

`enum SpAudioQuality {`

`2`

`3`

`};`

Audio quality.

### SpDrmFormat

* * *

[*Return to header index*](#main)

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

`8`

`};`

DRM formats.

kSpDrmFormatUnknownUnknown DRM. kSpDrmFormatUnencryptedNo DRM, unencrypted. kSpDrmFormatFairPlayFairPlay. kSpDrmFormatWidevineWidevine. kSpDrmFormatPlayReadyPlayReady.

### SpReDeliveryMode

* * *

[*Return to header index*](#main)

`1`

`enum SpReDeliveryMode {`

`2`

`3`

`};`

Redelivery mode types.

### SpInit

* * *

[*Return to header index*](#main)

`1`

`SpError SpInit(struct SpConfig *conf)`

Initialize the library.

### SpFree

* * *

[*Return to header index*](#main)

Shut down the library.

If a user is currently logged in, the application should first call [SpConnectionLogout()](#spconnectionlogout) and wait for the kSpConnectionNotifyLoggedOut event, otherwise [SpFree()](#spfree) may take several seconds.

### SpGetLibraryVersion

* * *

[*Return to header index*](#main)

`1`

`const char * SpGetLibraryVersion(void)`

Retrieve a version string for the library.

**Notes:**

- This API can be invoked from a callback.

### SpConnectionSetConnectivity

* * *

[*Return to header index*](#main)

`1`

`SpError SpConnectionSetConnectivity(enum SpConnectivity connectivity)`

Set the type of network connection of the device.

When the application detects that the device has lost network connection, it should call this function with [kSpConnectivityNone.](#kspconnectivitynone) When network connection is restored, the application should call this function with one of the other values of [SpConnectivity.](#spconnectivity) The library will then immediately retry to reconnect to Spotify (rather than waiting for the next retry timeout). The library may use the type of network connection to adapt its streaming and buffering strategies. Currently, however, all types of network connection are treated the same.

### SpConnectionGetConnectivity

* * *

[*Return to header index*](#main)

`1`

`enum SpConnectivity SpConnectionGetConnectivity(void)`

Get the connectivity that was set with [SpConnectionSetConnectivity()](#spconnectionsetconnectivity)

The library does not detect the type of network connection by itself. It only updates it if the application calls [SpConnectionSetConnectivity()](#spconnectionsetconnectivity). If [SpConnectionSetConnectivity()](#spconnectionsetconnectivity) was never called, the connection defaults to [kSpConnectivityWired.](#kspconnectivitywired)

**Notes:**

- This API can be invoked from a callback.

### SpConnectionLoginBlob

* * *

[*Return to header index*](#main)

`1`

`SpError SpConnectionLoginBlob(const char *username, const char *credentials_blob)`

Log in a user to Spotify using a credentials blob.

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:
- The blob can only be used for subsequent logins as long as the value of [SpConfig::unique\_id](#spconfig) does not change. If [SpConfig::unique\_id](#spconfig) has changed since the blob was received, this function returns an error and you will receive a debug message similar to "Parsing ZeroConf blob failed with code -3".

### SpConnectionLoginOauthToken

* * *

[*Return to header index*](#main)

`1`

`SpError SpConnectionLoginOauthToken(const char *oauth_token)`

Log in a user to Spotify using a Spotify OAuth token.

For subsequent logins the [SpCallbackConnectionNewCredentials()](#spcallbackconnectionnewcredentials) callback should be implemented and the received credentials blob should be stored and used. (Note that the OAuth access token itself expires after a short time. The credentials blob returned by the callback allows you to re-login even after the token has expired.)

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:
- Spotify Connect-enabled hardware devices that implement the ZeroConf stack must use the function [SpConnectionLoginBlob()](#spconnectionloginblob) instead.

### SpConnectionLogout

* * *

[*Return to header index*](#main)

`1`

`SpError SpConnectionLogout(void)`

Log the user out of [Spotify.](#spotify)

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The logout is performed asynchronously. The logout is complete when the callback [SpCallbackConnectionNotify()](#spcallbackconnectionnotify) is called with the event [kSpConnectionNotifyLoggedOut.](#kspconnectionnotifyloggedout)

### SpConnectionIsLoggedIn

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpConnectionIsLoggedIn(void)`

Is the user logged in to [Spotify.](#spotify)

**See also**

- kSpConnectionNotifyLoggedIn
- kSpConnectionNotifyLoggedOut
- [SpConnectionLoginBlob](#spconnectionloginblob)
- [SpConnectionLogout](#spconnectionlogout)

**Notes:**

- This API can be invoked from a callback.

### SpConnectionGetAckId

* * *

[*Return to header index*](#main)

`1`

`const char * SpConnectionGetAckId(void)`

Get the last Ack ID.

**Notes:**

- This function is deprecated and should not be used.

### SpGetCanonicalUsername

* * *

[*Return to header index*](#main)

`1`

`const char * SpGetCanonicalUsername(void)`

Get the canonical username of the logged in user.

This function returns the canonical username of the logged in user, which is the unique username used for identifying a specific user for things like playlists and the Spotify Web API. This username might differ from the username used to login. A user can login with an e-mail address or non-canonical unicode. This function will return the canonicalized version of the username after a successful login.

**Notes:**

- The canonical username should not be stored persistently. Always store the username as provided by the user, not the canonicalized version.
- This API can be invoked from a callback.

### SpSetDisplayName

* * *

[*Return to header index*](#main)

`1`

`SpError SpSetDisplayName(const char *display_name)`

Set the display name for the device or application.

This function can be used to change the display name that was passed to [SpInit()](#spinit) in the field [SpConfig::display\_name.](#spconfig::display_name)

**Notes:**

- The display name is not allowed to be an empty string.

### SpSetVolumeSteps

* * *

[*Return to header index*](#main)

`1`

`SpError SpSetVolumeSteps(uint32_t steps)`

Set the volume steps the device is capable of.

This function will indicate the number of intermediate steps from min\_volume to max\_volume that the device supports. If there's no volume control ability it must be set to zero to inform that no volume control is possible at all. The default number of steps if this function is not called is 16.

**Notes:**

- There's no commitment from the other Connect clients to respect the volume steps. It's important to call this function passing zero if no volume control is possible though.

### SpSetDeviceIsGroup

* * *

[*Return to header index*](#main)

`1`

`SpError SpSetDeviceIsGroup(int is_group)`

Control if the device represents a group.

A group is a number of devices all playing back the same sound synchronized. Setting this status correctly will allow Spotify clients to display the correct metadata for this device.

**Notes:**

- If device aliases are used, this function should not be used to set the group status. Instead, [SpSetDeviceAliases()](#spsetdevicealiases) should be used to update group status individually for each alias.

### SpEnableConnect

* * *

[*Return to header index*](#main)

`1`

`SpError SpEnableConnect(void)`

Enable Connect functionality for this device.

A device with enabled Connect functionality will show up in other devices' Connect pickers, and will be able to both control them and be controlled. The Spotify embedded library will enable Connect functionality by default

### SpDisableConnect

* * *

[*Return to header index*](#main)

`1`

`SpError SpDisableConnect(void)`

Disable Connect functionality for this device.

A device that disables Connect will not be able to control playback on other devices, or be controlled by them.

### SpGetSelectedDeviceAlias

* * *

[*Return to header index*](#main)

`1`

`int SpGetSelectedDeviceAlias(void)`

Return the currently selected device alias.

### SpPumpEvents

* * *

[*Return to header index*](#main)

`1`

`SpError SpPumpEvents(void)`

Allow the library to perform asynchronous tasks and process events.

Note: The suggested time interval to call this function is 10ms. This function should not be called from a callback. A typical usage pattern looks like this:

**Example:**

`1`

`int quit=0;`

`2`

`SpInit(&conf);`

`3`

`SpConnectionLoginBlob(username,blob);`

`4`

`while (!quit){`

`5`

`//Processtasksandinvokecallbacks`

`6`

`SpPumpEvents();`

`7`

`//HeretheapplicationshouldupdateitsUIand`

`8`

`//callotherSpotifyEmbeddedAPIsinreaction`

`9`

`//tothecallbackeventsthatitreceived.`

`10`

`};`

`11`

`SpFree();`

### SpRegisterConnectionCallbacks

* * *

[*Return to header index*](#main)

`1`

`SpError SpRegisterConnectionCallbacks(struct SpConnectionCallbacks *cb, void *context)`

Register callbacks related to the connection to [Spotify.](#spotify)

### SpRegisterDebugCallbacks

* * *

[*Return to header index*](#main)

`1`

`SpError SpRegisterDebugCallbacks(struct SpDebugCallbacks *cb, void *context)`

Register a callback that receives debug messages/trace logs.

These callbacks can be registered before [SpInit()](#spinit) has been called, in order to receive debug logs that occur during initialization.

### SpRegisterPlaybackCallbacks

* * *

[*Return to header index*](#main)

`1`

`SpError SpRegisterPlaybackCallbacks(struct SpPlaybackCallbacks *cb, void *context)`

Register playback-related callbacks.

### SpGetMetadata

* * *

[*Return to header index*](#main)

`1`

`SpError SpGetMetadata(struct SpMetadata *metadata, int relative_index)`

Retrieve metadata for a track in the current track list.

**Notes:**

- This API can be invoked from a callback.
- Be aware that many APIs that change the currently playing context are asynchronous, and the changes will not be immediately reflected in the metadata returned by [SpGetMetadata()](#spgetmetadata). For example, when calling [SpPlaybackSkipToNext()](#spplaybackskiptonext), [SpPlaybackEnableShuffle()](#spplaybackenableshuffle), etc., the metadata returned by [SpGetMetadata()](#spgetmetadata) might be unchanged while the command is being processed (which involves network communication). The notification kSpPlaybackNotifyMetadataChanged will be sent as soon as [SpGetMetadata()](#spgetmetadata) would return a different result for any relative\_index defined in the *enum* [SpMetadataTrack.](#spmetadatatrack)

### SpGetMetadataImageURL

* * *

[*Return to header index*](#main)

`1`

`SpError SpGetMetadataImageURL(const char *image_uri, char *image_url, size_t image_url_size)`

Return the HTTP URL to an image file from a spotify:image: URI.

**Notes:**

- This API can be invoked from a callback.

### SpGetPlayerCookie

* * *

[*Return to header index*](#main)

`1`

`SpError SpGetPlayerCookie(char *player_cookie, size_t player_cookie_size)`

Obtain player cookie for current playback.

The obtained player cookie can then be used to get more detailed metadata for current playback from Spotify's backend using Spotify Web API.

**Notes:**

- Experimental, subject to change

### SpPlaybackPlay

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackPlay(int alias_index)`

Start or resume playback.

### SpPlaybackPause

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackPause(void)`

Pause playback.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

### SpPlaybackSkipToNext

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSkipToNext(void)`

Skip playback to the next track in the track list.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

### SpPlaybackSkipToPrev

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSkipToPrev(void)`

Skip playback to the previous track in the track list.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

**Notes:**

- This function will try to skip to the previous track regardless of the current playback position. If the desired behaviour is to only skip to the previous track UNLESS the current playback position is beyond 3 seconds, the following code example is suggested as a base: if(SpPlaybackGetPosition()/1000=3) SpPlaybackSeek(0); else [SpPlaybackSkipToPrev()](#spplaybackskiptoprev);

### SpPlaybackSeek

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSeek(uint32_t position_ms)`

Seek to a position within the current track.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

### SpPlaybackSeekRelative

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSeekRelative(int32_t time_ms)`

Seek a relative amount of time within the current track.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

### SpPlaybackGetPosition

* * *

[*Return to header index*](#main)

`1`

`uint32_t SpPlaybackGetPosition(void)`

Get the current playback position within the track.

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackUpdateVolume

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackUpdateVolume(uint16_t volume)`

Request a change to the playback volume.

It is the application's responsibility to apply the volume change to its audio output. This function merely notifies the library of the volume change, so that the library can inform other Spotify Connect-enabled devices. Calling this function invokes the [SpCallbackPlaybackApplyVolume()](#spcallbackplaybackapplyvolume) callback, which the application can use to apply the actual volume change.

**Notes:**

- When the library is initialized, it assumes a volume level of 32768 (50% volume). The application must invoke [SpPlaybackUpdateVolume()](#spplaybackupdatevolume) at some point after calling [SpInit()](#spinit) to inform the library of the actual volume level of the device's audio output.

### SpPlaybackGetVolume

* * *

[*Return to header index*](#main)

`1`

`uint16_t SpPlaybackGetVolume(void)`

Get the playback volume level.

This returns the last volume level that the application set using [SpPlaybackUpdateVolume()](#spplaybackupdatevolume) or that was reported to the application using [SpCallbackPlaybackApplyVolume()](#spcallbackplaybackapplyvolume).

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsPlaying

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackIsPlaying(void)`

Is the playback status playing or paused.

**See also**

- kSpPlaybackNotifyPlay
- kSpPlaybackNotifyPause
- [SpPlaybackPlay](#spplaybackplay)
- [SpPlaybackPause](#spplaybackpause)

**Notes:**

- This API can be invoked from a callback.
- The result of this API is analogous to the playback notifications kSpPlaybackNotifyPlay and [kSpPlaybackNotifyPause.](#kspplaybacknotifypause)

### SpPlaybackIsAdPlaying

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackIsAdPlaying(void)`

Is the current track an Ad or not.

**See also**

- kSpPlaybackNotifyTrackChanged

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsShuffled

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackIsShuffled(void)`

Is "shuffle" mode enabled.

**See also**

- kSpPlaybackNotifyShuffleOn
- kSpPlaybackNotifyShuffleOff
- [SpPlaybackEnableShuffle](#spplaybackenableshuffle)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsRepeated

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackIsRepeated(void)`

Is "repeat" mode enabled.

**See also**

- kSpPlaybackNotifyRepeatOn
- kSpPlaybackNotifyRepeatOff
- [SpPlaybackEnableRepeat](#spplaybackenablerepeat)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackGetRepeatMode

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackGetRepeatMode(void)`

Which "repeat" mode is on.

**See also**

- kSpPlaybackNotifyRepeatOn
- kSpPlaybackNotifyRepeatOff
- [SpPlaybackEnableRepeat](#spplaybackenablerepeat)

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackIsActiveDevice

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackIsActiveDevice(void)`

Is the device the active playback device.

**See also**

- kSpPlaybackNotifyBecameActive
- kSpPlaybackNotifyBecameInactive

**Notes:**

- This API can be invoked from a callback.

### SpPlaybackEnableShuffle

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackEnableShuffle(uint8_t enable)`

Enable or disable "shuffle" mode.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

**See also**

- [SpPlaybackIsShuffled](#spplaybackisshuffled)

**Notes:**

- The change to the shuffle mode might not take effect if the API is invoked in the time window between requesting playback of a new context (e.g., by calling [SpPlayUri()](#spplayuri)), and playback of the new context actually starting.

### SpPlaybackEnableRepeat

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackEnableRepeat(uint8_t enable)`

Enable or disable "repeat" mode.

If the device is not the active speaker ([SpPlaybackIsActiveDevice()](#spplaybackisactivedevice)), the error code kSpErrorNotActiveDevice is returned.

**See also**

- [SpPlaybackIsRepeated](#spplaybackisrepeated)

### SpPlaybackCycleRepeatMode

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackCycleRepeatMode(void)`

Cycle through the available repeat modes.

Cycles through repeat modes (repeat off, repeat context, repeat track) given their current availability. If for example repeat context is enabled and repeat track is disallowed due to restrictions, this API will go directly to repeat off.

### SpPlaybackSetBitrate

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSetBitrate(enum SpPlaybackBitrate bitrate)`

Change the bitrate at which compressed audio data is delivered.

The integration will be required to flush the data it has already received at the current audio quality. The data in the new audio quality will then be streamed from the playback position we were at when this API was called.

### SpPlaybackSetDeviceInactive

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSetDeviceInactive(void)`

Set the device inactive.

If the device is currently the active device, this function stops the playback if playing, sets the device inactive, and sends the notification [kSpPlaybackNotifyBecameInactive.](#kspplaybacknotifybecameinactive) If the device is already inactive, the error code kSpErrorNotActiveDevice is returned.

**See also**

- [SpPlaybackIsActiveDevice](#spplaybackisactivedevice)

**Notes:**

- The device gets active and starts playing when integration calls [SpPlaybackPlay()](#spplaybackplay) or [SpPlayUri()](#spplayuri).

### SpPlaybackIsDeviceControllable

* * *

[*Return to header index*](#main)

`1`

`uint8_t SpPlaybackIsDeviceControllable(void)`

Is the device controllable.

**See also**

- [SpPlaybackSetDeviceControllable](#spplaybacksetdevicecontrollable)

### SpPlaybackSetDeviceControllable

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSetDeviceControllable(uint8_t is_controllable)`

Allow or disallow the device to be controllable.

On some platforms, there might be certain situations in which the control of the playback should be disallowed temporarily. In this case, when the user tries to start playback on the device using the mobile application, the device should be marked as "Unavailable for playback" in the UI.

**See also**

- [SpPlaybackIsDeviceControllable](#spplaybackisdevicecontrollable)

**Notes:**

- This functionality is reserved for specific integration scenarios. It can be used to temporarily forbid playback when for example playing cutscenes in video games or taking a phone call while driving a car. This API should not be used if the device is unable to play (for example, if a firmware upgrade is about to be performed), the application shall then instead log out, shut down the library, and stop announcing the device via the ZeroConf.

### SpPlaybackIncreaseUnderrunCount

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackIncreaseUnderrunCount(uint32_t count)`

Increase the underrun counter of the current track.

If playback underruns have been detected in the current track, use this API to report it to eSDK. This should only be called when there was no data to play at all and there was an audible glitch or gap for the user. It should only be called if audio was expected to be played and there was audio before. For example if eSDK is active and playing, but there is an underrun, report it. If eSDK is active and was requested to play something, but it never started, do not report it. If eSDK is active and playing and user skips, there is an expected gap, so report an underrun only if audio data started being delivered from eSDK and then stopped.

### SpPlaybackSetBandwidthLimit

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSetBandwidthLimit(uint32_t max_bytes_per_sec)`

Set a limit on the download speed.

By calling this function eSDK will attempt to limit how fast it downloads a track. In some use cases it is preferred to not use the full bandwidth. At the beginning of a download eSDK will do a burst download and then try to obey the limit.

**Notes:**

- eSDK is not guaranteed to stay strictly below the limit but will not exceed it by much. It is also not guaranteed to use all available bandwidth.

### SpPlaybackSetRedeliveryMode

* * *

[*Return to header index*](#main)

`1`

`SpError SpPlaybackSetRedeliveryMode(SpReDeliveryMode mode)`

Activates redelivery of audio data on play or resume playback.

This function should be called to activate or deactivate audio redelivery for the next calls to [SpPlaybackPlay()](#spplaybackplay). When the client application can't keep unplayed audio in its playback buffers (for example when audio from some other source was played while Spotify was paused) the eSDK should be notified that redelivery of audio data is needed. The audio data is redelivered from the last playback position reported by the integration with the same precision as seek. eSDK will need to redownload the data that was already delivered to the integration and therefore there will be a penalty of increased data consumption and latencies. Only use this function when unplayed audio is discarded.

### SpPlaybackIsRedeliveryModeActivated

* * *

[*Return to header index*](#main)

`1`

`SpReDeliveryMode SpPlaybackIsRedeliveryModeActivated(void)`

Gets the status of redelivery mode.

When redelivery mode is activated or deactivated through the API [SpPlaybackSetRedeliveryMode()](#spplaybacksetredeliverymode), an internal state is updated to keep track of the redelivery behavior. This API exposes this internal state.

### SpZeroConfGetVars

* * *

[*Return to header index*](#main)

`1`

`SpError SpZeroConfGetVars(struct SpZeroConfVars *vars)`

Get variables for ZeroConf, mainly the "getInfo" request.

The application should use this function to retrieve the data that it should send in the response to the "getInfo" request. See the ZeroConf manual for more information. There are also other fields here that might be needed for ZeroConf.

**Notes:**

- This API can be invoked from a callback.

### SpZeroConfAnnouncePause

* * *

[*Return to header index*](#main)

`1`

`SpError SpZeroConfAnnouncePause(void)`

Temporarily pause ZeroConf mDNS announcements.

**Notes:**

- This call requires ZeroConf to be started by setting [SpConfig::zeroconf\_serve](#spconfig) when calling [SpInit()](#spinit)

### SpZeroConfAnnounceResume

* * *

[*Return to header index*](#main)

`1`

`SpError SpZeroConfAnnounceResume(void)`

Resume ZeroConf mDNS announcement after calling [SpZeroConfAnnouncePause()](#spzeroconfannouncepause)

**Notes:**

- This call requires ZeroConf to be started by setting [SpConfig::zeroconf\_serve](#spconfig) when calling [SpInit()](#spinit)

### SpConnectionLoginZeroConf

* * *

[*Return to header index*](#main)

`1`

`SpError SpConnectionLoginZeroConf(const char *username, const char *zero_conf_blob, const char *client_key, const char *login_id, const char *token_type)`

Log in a user to Spotify using a ZeroConf credentials blob.

This function logs in with the information that the application receives in the "addUser" ZeroConf request. See the ZeroConf manual.

**See also**

- [SpConnectionIsLoggedIn](#spconnectionisloggedin)

**Notes:**

- The login is performed asynchronously. The return value only indicates whether the library is able to perform the login attempt. The status of the login will be reported via callbacks:

### SpGetBrandName

* * *

[*Return to header index*](#main)

`1`

`const char * SpGetBrandName(void)`

This function can be used to get the brand name. If the field [SpConfig::brand\_display\_name](#spconfig) was set at [SpInit()](#spinit), function returns its value, otherwise it returns what was set in the mandatory field [SpConfig::brand\_name.](#spconfig::brand_name)

**Notes:**

- This API can be invoked from a callback.

### SpGetModelName

* * *

[*Return to header index*](#main)

`1`

`const char * SpGetModelName(void)`

This function can be used to get the model name. If the field [SpConfig::model\_display\_name](#spconfig) was set at [SpInit()](#spinit), function returns its value, otherwise it returns what was set in the mandatory field [SpConfig::model\_name.](#spconfig::model_name)

**Notes:**

- This API can be invoked from a callback.

### SpRegisterDeviceAliasCallbacks

* * *

[*Return to header index*](#main)

`1`

`SpError SpRegisterDeviceAliasCallbacks(struct SpDeviceAliasCallbacks *cb, void *context)`

Register callbacks related to device aliases.

### SpSetDeviceAliases

* * *

[*Return to header index*](#main)

`1`

`SpError SpSetDeviceAliases(const struct SpDeviceAlias *aliases)`

Update the device alias definitions.

Call this whenever the current alias definitions are updated. The id values for the aliases must be unique within the array. aliases Pointer to an array of [SpDeviceAlias](#spdevicealias) structs filled in with the new alias names and corresponding attributes. The array size must be of size SP\_MAX\_DEVICE\_ALIASES.

### SpSetAdUserAgent

* * *

[*Return to header index*](#main)

`1`

`SpError SpSetAdUserAgent(const char *user_agent)`

Set the ad user agent.

For clients that need to register a specific UserAgent for ads.

**See also**

- [SpConfig](#spconfig)

### SpRestrictDrmMediaFormats

* * *

[*Return to header index*](#main)

`1`

`SpError SpRestrictDrmMediaFormats(const struct SpFormat restricted_formats[SP_MAX_SUPPORTED_FORMATS])`

Restrict DRM/Media formats.

restricted\_formats An array of DRM/media format pairs to restrict. Restricts the list of DRM and media formats to a subset of the formats registered in [SpInit()](#spinit). COMPATIBILITY NOTE: To restore the restricted capabilitites to the ones registered in [SpInit()](#spinit) call this API again with a NULL parameter. That is, [SpRestoreDrmMediaFormats()](#sprestoredrmmediaformats) is now removed.

**See also**

- [SpInit](#spinit)
- [SpConfig::supported\_drm\_media\_formats](#spconfig)

**Notes:**

- This API can be invoked from a callback.

**Example:**

`1`

`const struct SpFormat formats[SP_MAX_SUPPORTED_FORMATS];`

`2`

`memset(formats,0, sizeof (formats));`

`3`

`formats[0].drm= kSpDrmFormatUnencrypted;`

`4`

`formats[0].media=`

`5`

`(1 kSpMediaFormatSpotifyOggVorbis)|(1 kSpMediaFormatMp3);`

`6`

`formats[1].drm= kSpDrmFormatFairPlay;`

`7`

`formats[1].media=(1 kSpMediaFormatMp4AAC);`

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

[SpContentCallbacks](#spcontentcallbacks)Callbacks to be registered with [SpRegisterContentCallbacks()](#spregistercontentcallbacks)

## Typedefs

* * *

[Return to header index](#content)

[SpCallbackTrackCacheState](#spcallbacktrackcachestate)This callback, if set by the client, is called by eSDK to inform how many percent of the particular track are cached. It is measured from the beginning of the track. E.g. if 60 is reported it means that 60% of the track is cached starting from the beginning. [SpCallbackStorageKeyContentMapping](#spcallbackstoragekeycontentmapping)This callback, if set by the client, is called by eSDK to notify how the storage\_key is mapped to particular content being stored. [SpContentType](#spcontenttype) is used to specify exact content type. For example: hint being equal to kSpContentTrack means that the descriptor's representation is spotify:track:\[base62]. [SpCallbackTrackRelinked](#spcallbacktrackrelinked)This callback, if set by the client, is called by eSDK to notify about the fact that requested track is substituted with another (relinked) one during prefetch/offline process. [SpCallbackTrackRemoved](#spcallbacktrackremoved)This callback, if set by the client, is called by eSDK to notify that the track is removed. [SpCallbackOnAvailableContainer](#spcallbackonavailablecontainer)Callback for each available container.

## Enumerations

* * *

[Return to header index](#content)

[SpContentType](#spcontenttype)Enum describes content type being stored by eSDK.

## Functions

* * *

[Return to header index](#content)

### SpContentCallbacks

* * *

[*Return to header index*](#content)

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

Callbacks to be registered with [SpRegisterContentCallbacks()](#spregistercontentcallbacks)

Any of the pointers may be NULL.

**Notes:**

- See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackTrackCacheState](#spcallbacktrackcachestate) track\_state\_callbackTrack cached state callback. [SpCallbackStorageKeyContentMapping](#spcallbackstoragekeycontentmapping) store\_key\_map\_callbackContent mapping callback. [SpCallbackTrackRelinked](#spcallbacktrackrelinked) track\_relink\_callbackNotify about track relink during prefetch/offline. [SpCallbackTrackRemoved](#spcallbacktrackremoved) track\_removed\_callbackNotify about track removal. [SpCallbackOnAvailableContainer](#spcallbackonavailablecontainer) on\_available\_containerNotify about an available container item.

### SpCallbackTrackCacheState

* * *

[*Return to header index*](#content)

`1`

`typedef void(* SpCallbackTrackCacheState) (const char *track_uri, uint32_t percents, void *context)`

This callback, if set by the client, is called by eSDK to inform how many percent of the particular track are cached. It is measured from the beginning of the track. E.g. if 60 is reported it means that 60% of the track is cached starting from the beginning.

**Notes:**

- The application should not block or call other API functions in the callback. This callback is called before each track delivery is started.

### SpCallbackStorageKeyContentMapping

* * *

[*Return to header index*](#content)

`1`

`typedef void(* SpCallbackStorageKeyContentMapping) (const char *storage_key, const char *descriptor, enum SpContentType hint, void *context)`

This callback, if set by the client, is called by eSDK to notify how the storage\_key is mapped to particular content being stored. [SpContentType](#spcontenttype) is used to specify exact content type. For example: hint being equal to kSpContentTrack means that the descriptor's representation is spotify:track:\[base62].

**See also**

- [SpContentType](#spcontenttype)

**Notes:**

- The application should not block or call other API functions in the callback. This callback is called as soon as possible after Alloc callback of Storage API has been called and succeeds.

### SpCallbackTrackRelinked

* * *

[*Return to header index*](#content)

`1`

`typedef void(* SpCallbackTrackRelinked) (const char *original_uri, const char *new_uri, void *context)`

This callback, if set by the client, is called by eSDK to notify about the fact that requested track is substituted with another (relinked) one during prefetch/offline process.

### SpCallbackTrackRemoved

* * *

[*Return to header index*](#content)

`1`

`typedef void(* SpCallbackTrackRemoved) (const char *track_uri, void *context)`

This callback, if set by the client, is called by eSDK to notify that the track is removed.

track\_uri URI passed into eSDK PlayURI/PrefetchURI/OfflineURI function calls. context Context provided in callback register procedure.

### SpCallbackOnAvailableContainer

* * *

[*Return to header index*](#content)

`1`

`typedef void(* SpCallbackOnAvailableContainer) (const char *uri, int total, void *context)`

Callback for each available container.

**Notes:**

- Experimental, subject of change

### SpContentType

* * *

[*Return to header index*](#content)

`1`

`enum SpContentType {`

`2`

`3`

`};`

Enum describes content type being stored by eSDK.

### SpRegisterContentCallbacks

* * *

[*Return to header index*](#content)

`1`

`SpError SpRegisterContentCallbacks(struct SpContentCallbacks *callbacks, void *context)`

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

[SpSockaddr](#spsockaddr)Struct contains resolved hostname IP address and its family. [SpDnsHALCallbacks](#spdnshalcallbacks)Callbacks to be registered with [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks) [SpSocketHandle](#spsockethandle)Socket handle type. [SpSocketHALCallbacks](#spsockethalcallbacks)Callbacks to be registered with [SpRegisterSocketHALCallbacks()](#spregistersockethalcallbacks)

## Typedefs

* * *

[Return to header index](#hal)

[SpCallbackPerformDNSLookup](#spcallbackperformdnslookup)This callback, if set by the client, is called by eSDK to perform DNS lookups. It should be robust against slow name resolutions (e.g. poor network conditions) by performing lookups asynchronously. Otherwise [SpPumpEvents()](#sppumpevents) might block for too long and cause audio stutters. See documentation for return value for more recommendations w.r.t. asynchronous implementation. [SpCallbackSocketCreate](#spcallbacksocketcreate)This callback, if set by the client, is called by eSDK to create a socket of a certain type and family. [SpCallbackSocketSetOption](#spcallbacksocketsetoption)This callback, if set by the client, is called by eSDK to set specific options on the previously created socket. [SpCallbackSocketClose](#spcallbacksocketclose)This callback, if set by the client, is called by eSDK to close the previously opened socket. [SpCallbackSocketBind](#spcallbacksocketbind)This callback, if set by the client, is called by eSDK to bind to the provided socket. [SpCallbackSocketListen](#spcallbacksocketlisten)This callback, if set by the client, is called by eSDK to start listening on the provided socket. This callback has no effect on UDP sockets. [SpCallbackSocketConnect](#spcallbacksocketconnect)This callback, if set by the client, is called by eSDK to connect to the specified address and remote port. [SpCallbackSocketAccept](#spcallbacksocketaccept)This callback, if set by the client, is called by eSDK to accept connection on the provided socket. [SpCallbackSocketRead](#spcallbacksocketread)This callback, if set by the client, is called by eSDK to read data from the socket. [SpCallbackSocketWrite](#spcallbacksocketwrite)This callback, if set by the client, is called by eSDK to write data to the socket. [SpCallbackSocketReadFrom](#spcallbacksocketreadfrom)This callback, if set by the client, is called by eSDK to read data from the socket addressed by the [SpSockaddr](#spsockaddr) instance. [SpCallbackSocketWriteTo](#spcallbacksocketwriteto)This callback, if set by the client, is called by eSDK to write data to the socket addressed by the [SpSockaddr](#spsockaddr) instance. [SpCallbackSocketError](#spcallbacksocketerror)This callback, if set by the client, is called by eSDK to get the underlying OS error code. [SpCallbackSocketReadable](#spcallbacksocketreadable)This callback, if set by the client, is called by eSDK to figure out if the socket is readable. [SpCallbackSocketWriteable](#spcallbacksocketwriteable)This callback, if set by the client, is called by eSDK to figure out if the socket is writable. [SpCallbackLocalAddresses](#spcallbacklocaladdresses)This callback, if set by the client, is called by eSDK to get local interface addresses. [SpCallbackSocketAddress](#spcallbacksocketaddress)This callback, if set by the client, is called by eSDK to provide platform defined representation of address that can be used in [SpCallbackSocketReadFrom()](#spcallbacksocketreadfrom) and [SpCallbackSocketWriteTo()](#spcallbacksocketwriteto). The client is responsible for providing a sufficient lifetime of the returned pointer. [SpCallbackPump](#spcallbackpump)This callback, if set by the client, is called by eSDK to pump the network layer.

## Enumerations

* * *

[Return to header index](#hal)

[SpIPFamily](#spipfamily)Enum describes the IP family. [SpSocketPool](#spsocketpool)Socket pool IDs. [SpSocketType](#spsockettype)Enum defines the type of socket supported by eSDK. [SpSocketOptions](#spsocketoptions)Enum defines options that can be applied to sockets.

## Functions

* * *

[Return to header index](#hal)

[SpRegisterDnsHALCallbacks](#spregisterdnshalcallbacks)Register HAL-related callbacks. Should be called right after [SpInit()](#spinit). [SpGetDefaultDnsHALCallbacks](#spgetdefaultdnshalcallbacks)Get eSDK's default DNS callbacks. [SpRegisterSocketHALCallbacks](#spregistersockethalcallbacks)Register socket HAL-related callbacks. To remove callbacks, call [SpRegisterSocketHALCallbacks()](#spregistersockethalcallbacks) with [SpSocketHALCallbacks](#spsockethalcallbacks) initialized to zeros. [SpGetDefaultSocketHALCallbacks](#spgetdefaultsockethalcallbacks)Get eSDK's default socket callbacks.

### SpSockaddr

* * *

[*Return to header index*](#hal)

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

Struct contains resolved hostname IP address and its family.

*enum* [SpIPFamily](#spipfamily) familyIP protocol family for which lookup is requested. uint8\_t addrIp address. Network byte order. *int* portContains port value if applicable. Host byte order.

### SpDnsHALCallbacks

* * *

[*Return to header index*](#hal)

`1`

`struct SpDnsHALCallbacks {`

`2`

`SpCallbackPerformDNSLookup dns_lookup_callback;`

`3`

`};`

Callbacks to be registered with [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks)

Any of the pointers may be NULL. To remove DNS callback at any time call [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks) with [SpDnsHALCallbacks::dns\_lookup\_callback](#spdnshalcallbacks) set to NULL.

**Notes:**

- See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackPerformDNSLookup](#spcallbackperformdnslookup) dns\_lookup\_callbackDNS lookup callback. If NULL eSDK will use its internal DNS resolve mechanism.

### SpSocketHandle

* * *

[*Return to header index*](#hal)

`1`

`struct SpSocketHandle {`

`2`

`void *handle;`

`3`

`void *tls;`

`4`

`};`

Socket handle type.

*void* * handlePlatform defined socket representation. *void* * tlsCan be used by the TLS implementation to store connection specific state.

### SpSocketHALCallbacks

* * *

[*Return to header index*](#hal)

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

Callbacks to be registered with [SpRegisterSocketHALCallbacks()](#spregistersockethalcallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackSocketCreate](#spcallbacksocketcreate) socket\_createCallback to create socket instance. [SpCallbackSocketSetOption](#spcallbacksocketsetoption) socket\_set\_optionCallback to set options on created socket. [SpCallbackSocketClose](#spcallbacksocketclose) socket\_closeCallback to close the socket. [SpCallbackSocketBind](#spcallbacksocketbind) socket\_bindCallback to bind to socket. [SpCallbackSocketListen](#spcallbacksocketlisten) socket\_listenCallback to start listening the socket. [SpCallbackSocketConnect](#spcallbacksocketconnect) socket\_connectCallback to connect to socket. [SpCallbackSocketAccept](#spcallbacksocketaccept) socket\_acceptCallback to accept connection on socket. [SpCallbackSocketRead](#spcallbacksocketread) socket\_readCallback to read data from socket. [SpCallbackSocketWrite](#spcallbacksocketwrite) socket\_writeCallback to write data to socket. [SpCallbackSocketReadFrom](#spcallbacksocketreadfrom) socket\_read\_fromCallback to read data from socket pointed by address. [SpCallbackSocketWriteTo](#spcallbacksocketwriteto) socket\_write\_toCallback to write data to socket pointed by address. [SpCallbackSocketError](#spcallbacksocketerror) socket\_errorCallback to get OS error on socket. [SpCallbackSocketReadable](#spcallbacksocketreadable) socket\_readableCallback to get readable state on socket. [SpCallbackSocketWriteable](#spcallbacksocketwriteable) socket\_writableCallback to get writable state on socket. [SpCallbackLocalAddresses](#spcallbacklocaladdresses) local\_addressesCallback to get local interface addresses. [SpCallbackSocketAddress](#spcallbacksocketaddress) socket\_addressCallback to platform address representation. [SpCallbackPump](#spcallbackpump) on\_pumpCallback to pump network layer.

### SpCallbackPerformDNSLookup

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackPerformDNSLookup) (const char *hostname, struct SpSockaddr *sockaddr, void *context)`

This callback, if set by the client, is called by eSDK to perform DNS lookups. It should be robust against slow name resolutions (e.g. poor network conditions) by performing lookups asynchronously. Otherwise [SpPumpEvents()](#sppumpevents) might block for too long and cause audio stutters. See documentation for return value for more recommendations w.r.t. asynchronous implementation.

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- See [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks) for recommendation when it makes sense to provide a custom DNS callback.
- The application should not block or call other API functions in the callback.

### SpCallbackSocketCreate

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketCreate) (enum SpIPFamily family, enum SpSocketType type, enum SpSocketPool pool_id, struct SpSocketHandle **socket, void *context)`

This callback, if set by the client, is called by eSDK to create a socket of a certain type and family.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketSetOption

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketSetOption) (struct SpSocketHandle *socket, enum SpSocketOptions option, void *value, void *context)`

This callback, if set by the client, is called by eSDK to set specific options on the previously created socket.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketClose

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketClose) (struct SpSocketHandle *socket, void *context)`

This callback, if set by the client, is called by eSDK to close the previously opened socket.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketBind

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketBind) (struct SpSocketHandle *socket, int *port, void *context)`

This callback, if set by the client, is called by eSDK to bind to the provided socket.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketListen

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketListen) (struct SpSocketHandle *socket, int backlog, void *context)`

This callback, if set by the client, is called by eSDK to start listening on the provided socket. This callback has no effect on UDP sockets.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketConnect

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketConnect) (struct SpSocketHandle *socket, const struct SpSockaddr *addr, void *context)`

This callback, if set by the client, is called by eSDK to connect to the specified address and remote port.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketAccept

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketAccept) (struct SpSocketHandle *socket, enum SpSocketPool pool_id, struct SpSocketHandle **out_socket, void *context)`

This callback, if set by the client, is called by eSDK to accept connection on the provided socket.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketRead

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketRead) (struct SpSocketHandle *socket, void *data, int data_size, int *bytes_read, void *context)`

This callback, if set by the client, is called by eSDK to read data from the socket.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketWrite

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketWrite) (struct SpSocketHandle *socket, const void *data, int data_size, int *bytes_written, void *context)`

This callback, if set by the client, is called by eSDK to write data to the socket.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketReadFrom

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketReadFrom) (struct SpSocketHandle *socket, void *data, int data_size, const void **addr, int *bytes_read, void *context)`

This callback, if set by the client, is called by eSDK to read data from the socket addressed by the [SpSockaddr](#spsockaddr) instance.

**Notes:**

- The application should not block or call other API functions in the callback. This callback should mirror the behavior of recvfrom() for connected/non-connected sockets.

### SpCallbackSocketWriteTo

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackSocketWriteTo) (struct SpSocketHandle *socket, const void *data, int data_size, const void *addr, int *bytes_written, void *context)`

This callback, if set by the client, is called by eSDK to write data to the socket addressed by the [SpSockaddr](#spsockaddr) instance.

**Notes:**

- The application should not block or call other API functions in the callback. This callback should mirror the behavior of sendto() for connected/non-connected sockets.

### SpCallbackSocketError

* * *

[*Return to header index*](#hal)

`1`

`typedef int(* SpCallbackSocketError) (struct SpSocketHandle *socket, void *context)`

This callback, if set by the client, is called by eSDK to get the underlying OS error code.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketReadable

* * *

[*Return to header index*](#hal)

`1`

`typedef int(* SpCallbackSocketReadable) (struct SpSocketHandle *socket, void *context)`

This callback, if set by the client, is called by eSDK to figure out if the socket is readable.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketWriteable

* * *

[*Return to header index*](#hal)

`1`

`typedef int(* SpCallbackSocketWriteable) (struct SpSocketHandle *socket, void *context)`

This callback, if set by the client, is called by eSDK to figure out if the socket is writable.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackLocalAddresses

* * *

[*Return to header index*](#hal)

`1`

`typedef void(* SpCallbackLocalAddresses) (struct SpSockaddr *addrs, int *num_addrs, void *context)`

This callback, if set by the client, is called by eSDK to get local interface addresses.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackSocketAddress

* * *

[*Return to header index*](#hal)

`1`

`typedef const void *(* SpCallbackSocketAddress) (const struct SpSockaddr *addr, void *context)`

This callback, if set by the client, is called by eSDK to provide platform defined representation of address that can be used in [SpCallbackSocketReadFrom()](#spcallbacksocketreadfrom) and [SpCallbackSocketWriteTo()](#spcallbacksocketwriteto). The client is responsible for providing a sufficient lifetime of the returned pointer.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackPump

* * *

[*Return to header index*](#hal)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackPump) (unsigned max_wait_ms, void *context)`

This callback, if set by the client, is called by eSDK to pump the network layer.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpIPFamily

* * *

[*Return to header index*](#hal)

Enum describes the IP family.

### SpSocketPool

* * *

[*Return to header index*](#hal)

Socket pool IDs.

### SpSocketType

* * *

[*Return to header index*](#hal)

Enum defines the type of socket supported by eSDK.

### SpSocketOptions

* * *

[*Return to header index*](#hal)

`1`

`enum SpSocketOptions {`

`2`

`3`

`};`

Enum defines options that can be applied to sockets.

### SpRegisterDnsHALCallbacks

* * *

[*Return to header index*](#hal)

`1`

`SpError SpRegisterDnsHALCallbacks(struct SpDnsHALCallbacks *callbacks, void *context)`

Register HAL-related callbacks. Should be called right after [SpInit()](#spinit).

**Notes:**

- To remove DNS callback at any time call [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks) with [SpDnsHALCallbacks::dns\_lookup\_callback](#spdnshalcallbacks) set to NULL.
- eSDK provides built-in implementation for DNS lookups. For integrations built with glibc = 2.2.3 DNS lookups will be implemented via getaddrinfo\_a() and therefore will be done asynchronously. Such integrations have to link libanl (-lanl). Remaining builds will use blocking DNS lookups (e.g. getaddrinfo() for POSIX). Depending on the platform's timeout settings they might cause [SpPumpEvents()](#sppumpevents) to block for a long time and result in audio stutters. For affected platforms it's recommended to provide an asynchronous implementation instead.

### SpGetDefaultDnsHALCallbacks

* * *

[*Return to header index*](#hal)

`1`

`SpError SpGetDefaultDnsHALCallbacks(struct SpDnsHALCallbacks *callbacks)`

Get eSDK's default DNS callbacks.

**Notes:**

- These callbacks are made available so they may be wrapped by custom DNS functions provided with [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks).

### SpRegisterSocketHALCallbacks

* * *

[*Return to header index*](#hal)

`1`

`SpError SpRegisterSocketHALCallbacks(struct SpSocketHALCallbacks *callbacks, void *context)`

Register socket HAL-related callbacks. To remove callbacks, call [SpRegisterSocketHALCallbacks()](#spregistersockethalcallbacks) with [SpSocketHALCallbacks](#spsockethalcallbacks) initialized to zeros.

**Notes:**

- A call to this function has to be performed before [SpInit()](#spinit) is called. Calling this function when eSDK is initialized will fail with [kSpErrorAlreadyInitialized.](#ksperroralreadyinitialized)

### SpGetDefaultSocketHALCallbacks

* * *

[*Return to header index*](#hal)

`1`

`SpError SpGetDefaultSocketHALCallbacks(struct SpSocketHALCallbacks *callbacks, void **context)`

Get eSDK's default socket callbacks.

**Notes:**

- These callbacks are made available so they may be wrapped by custom socket functions provided with [SpRegisterSocketHALCallbacks()](#spregistersockethalcallbacks).

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

[SP\_FILE\_NAME](#sp_file_name)**FILE** [SP\_LOG\_DEFAULT\_LEVEL](#sp_log_default_level)SP\_LOG\_LEVEL\_INFO [SP\_LOG\_DEFINE\_TRACE\_OBJ](#sp_log_define_trace_obj)*struct* [SP\_LOG\_DECLARE\_TRACE\_OBJ](#sp_log_declare_trace_obj)extern *struct* [SP\_LOG\_REGISTER\_TRACE\_OBJ](#sp_log_register_trace_obj)*See macro below* [SP\_LOG](#sp_log)*See macro below* [SpLogFatal](#splogfatal)*See macro below* [SpLogError](#splogerror)*See macro below* [SpLogWarning](#splogwarning)[SpLogInfo](#sploginfo)*See macro below* [SpLogDebug](#splogdebug)*See macro below* [SpLogTrace](#splogtrace)*See macro below*

## Data Structures

* * *

[Return to header index](#log)

[SpLogTraceObject](#splogtraceobject)Trace object.

## Enumerations

* * *

[Return to header index](#log)

## Functions

* * *

[Return to header index](#log)

[SpLogRegisterTraceObject](#splogregistertraceobject)Register a defined trace object with eSDK. [SpLog](#splog)Output a debug message via eSDK. [SpLogSetLevel](#splogsetlevel)Control the current logging level. [SpLogGetLevels](#sploggetlevels)Get registered trace objects and log levels.

### SP\_FILE\_NAME

* * *

[*Return to header index*](#log)

`1`

`#define SP_FILE_NAME __FILE__`

Preferred macro to log the file name, you might redefine [SP\_FILE\_NAME](#sp_file_name) using basename() or use -ffile-prefix-map.

### SP\_LOG\_DEFAULT\_LEVEL

* * *

[*Return to header index*](#log)

`1`

`#define SP_LOG_DEFAULT_LEVEL SP_LOG_LEVEL_INFO`

Default trace log level.

### SP\_LOG\_DEFINE\_TRACE\_OBJ

* * *

[*Return to header index*](#log)

`1`

`#define SP_LOG_DEFINE_TRACE_OBJ struct`

Macro to define a trace object.

obj Name of the trace object

### SP\_LOG\_DECLARE\_TRACE\_OBJ

* * *

[*Return to header index*](#log)

`1`

`#define SP_LOG_DECLARE_TRACE_OBJ extern struct`

Macro to declare a previously defined trace object.

obj Name of the trace object

### SP\_LOG\_REGISTER\_TRACE\_OBJ

* * *

[*Return to header index*](#log)

`1`

`#define SP_LOG_REGISTER_TRACE_OBJ SpLogRegisterTraceObject(&trace_obj_##obj)`

Macro to register a previously defined trace object.

obj Name of the trace object

### SP\_LOG

* * *

[*Return to header index*](#log)

`1`

`#define SP_LOG do { \`

`2`

`if (trace_obj_##obj.level >= lvl) { \`

Macro that outputs a trace message.

obj Trace object name lvl Trace level for the message file Source file name func Calling function name line Line number in the source file

### SpLogFatal

* * *

[*Return to header index*](#log)

`1`

`#define SpLogFatal SP_LOG(obj, SP_LOG_LEVEL_FATAL, SP_FILE_NAME, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_FATAL.

### SpLogError

* * *

[*Return to header index*](#log)

`1`

`#define SpLogError SP_LOG(obj, SP_LOG_LEVEL_ERROR, SP_FILE_NAME, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_ERROR.

### SpLogWarning

* * *

[*Return to header index*](#log)

Emit trace message with SP\_LOG\_LEVEL\_WARNING.

### SpLogInfo

* * *

[*Return to header index*](#log)

`1`

`#define SpLogInfo SP_LOG(obj, SP_LOG_LEVEL_INFO, SP_FILE_NAME, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_INFO.

### SpLogDebug

* * *

[*Return to header index*](#log)

`1`

`#define SpLogDebug SP_LOG(obj, SP_LOG_LEVEL_DEBUG, SP_FILE_NAME, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_DEBUG.

### SpLogTrace

* * *

[*Return to header index*](#log)

`1`

`#define SpLogTrace SP_LOG(obj, SP_LOG_LEVEL_TRACE, SP_FILE_NAME, __func__, __LINE__, __VA_ARGS__)`

Emit trace message with SP\_LOG\_LEVEL\_TRACE.

### SpLogTraceObject

* * *

[*Return to header index*](#log)

`1`

`struct SpLogTraceObject {`

`2`

`SpLogLevel level;`

`3`

`const char *name;`

`4`

`};`

Trace object.

The trace object is an abstraction of a specific trace message category and an associated log level. The level can be changed freely for individual trace objects.

[SpLogLevel](#sploglevel) levelThe current debug level for this trace object. *const* *char* * nameThe trace category name describing this trace object.

### SpLogLevel

* * *

[*Return to header index*](#log)

Log levels.

These are the log levels assigned to log messages emitted by the eSDK.

**See also**

- [SpLogSetLevel](#splogsetlevel)

### SpLogRegisterTraceObject

* * *

[*Return to header index*](#log)

`1`

`SpError SpLogRegisterTraceObject(struct SpLogTraceObject *obj)`

Register a defined trace object with eSDK.

### SpLog

* * *

[*Return to header index*](#log)

`1`

`void SpLog(const struct SpLogTraceObject *obj, SpLogLevel level, const char *file, const char *func, int line, const char *format,...)`

Output a debug message via eSDK.

obj Pointer to trace object level The log level associated this this message file The source file from where the call is made, see SP\_FILE\_NAME. func The function name from where the call is made, typically **func**. line The line number from where the call is made, typically **LINE**. format A printf style format string followed by arguments.

### SpLogSetLevel

* * *

[*Return to header index*](#log)

`1`

`SpError SpLogSetLevel(const char *category, SpLogLevel level)`

Control the current logging level.

Control the logging level for a particular category. If the current configured log level is greater than or equal to the level associated with the message, the log message will be passed to the debug log callback. Each log message is also associated with a category. The category is a string that is included in the log message output. Each individual category has a separate current log level. The log messages produced by the eSDK are formatted as: LEVEL CATEGORY MESSAGE where LEVEL is a single letter indicating the log level (E=Error, I=Info, etc.), CATEGORY is a short string that identifies the log category, for example 'api' and MESSAGE is the actual debug message. As an example, a debug output string with level set to SP\_LOG\_LEVEL\_ERROR (letter "E") and the category "api" could look something like this (the timestamp is not actually part of the debug message from eSDK, but added by the [SpCallbackDebugMessage()](#spcallbackdebugmessage). Therefore, the format may not exactly match the example below).

**Example:**

`1`

`12:01:02.000EapiInvalidparameterpassedtoSpInit()`

### SpLogGetLevels

* * *

[*Return to header index*](#log)

`1`

`SpError SpLogGetLevels(char *buffer, int buffer_len)`

Get registered trace objects and log levels.

The information about trace objects and levels is represented as a string containing comma separated tuples level:trace obj, e.g. "4:app,4:esdk,4:audio".

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

[SpStreamInfo](#spstreaminfo)Stream Parameters. [SpStreamCallbacks](#spstreamcallbacks)Callbacks to be registered with [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks)

## Typedefs

* * *

[Return to header index](#media)

[SpCallbackStreamStart](#spcallbackstreamstart)Callback to provide track details to the application. [SpCallbackStreamData](#spcallbackstreamdata)Callback for delivering data to the integration. [SpCallbackStreamEnd](#spcallbackstreamend)Callback to tell integration that all data was delivered. [SpCallbackStreamGetPosition](#spcallbackstreamgetposition)Callback to get the playback position in milliseconds. [SpCallbackStreamSeekToPosition](#spcallbackstreamseektoposition)Callback to tell the integration to seek to a position. [SpCallbackStreamFlush](#spcallbackstreamflush)Callback to tell the integration to flush.

## Enumerations

* * *

[Return to header index](#media)

[SpMediaFormat](#spmediaformat)Media formats.

## Functions

* * *

[Return to header index](#media)

[SpRegisterStreamCallbacks](#spregisterstreamcallbacks)Register callbacks related to the delivery API. [SpNotifySeekComplete](#spnotifyseekcomplete)API to notify eSDK of the completion of seek operation. [SpNotifyTrackLength](#spnotifytracklength)API to notify eSDK of the track length in milliseconds. [SpNotifyTrackError](#spnotifytrackerror)API to notify eSDK of any track errors with last played position. [SpNotifyStreamPlaybackStarted](#spnotifystreamplaybackstarted)Notify eSDK that the first audio sample of the delivery has been played. [SpNotifyStreamPlaybackContinued](#spnotifystreamplaybackcontinued)Notify eSDK that the first audio sample after a flush of a delivery has been played. [SpNotifyStreamPlaybackFinishedNaturally](#spnotifystreamplaybackfinishednaturally)Notify eSDK that the delivery playback finished by playing the last sample of the delivery. [SpSetDownloadPosition](#spsetdownloadposition)API to instruct eSDK to start downloading from a given byte offset.

### SpStreamInfo

* * *

[*Return to header index*](#media)

`1`

`struct SpStreamInfo {`

`2`

`uint32_t size;`

`3`

`int32_t gain_mdb;`

`4`

`uint32_t start_position_ms;`

`5`

`const char *track_uri;`

`6`

`const char *resource;`

`7`

`};`

Stream Parameters.

*uint32\_t* sizeSize of the stream in bytes. If the size is unknown, 0 is used. *int32\_t* gain\_mdbAudio normalization gain (in mdB) to apply to the stream. *uint32\_t* start\_position\_msReserved for internal use. *const* *char* * track\_uriSpotify track URI. *const* *char* * resourceReserved for internal use.

### SpStreamCallbacks

* * *

[*Return to header index*](#media)

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

Callbacks to be registered with [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks)

[SpCallbackStreamStart](#spcallbackstreamstart) on\_startStart of delivery callback. [SpCallbackStreamData](#spcallbackstreamdata) on\_dataData delivery callback. [SpCallbackStreamEnd](#spcallbackstreamend) on\_endEnd of delivery callback. [SpCallbackStreamGetPosition](#spcallbackstreamgetposition) on\_get\_positionCurrent playback position callback. [SpCallbackStreamSeekToPosition](#spcallbackstreamseektoposition) on\_seek\_positionSeek to position callback. [SpCallbackStreamFlush](#spcallbackstreamflush) on\_flushFlush callback.

### SpCallbackStreamStart

* * *

[*Return to header index*](#media)

`1`

`typedef void(* SpCallbackStreamStart) (unsigned int stream_id, enum SpMediaFormat media_format, enum SpDrmFormat drm_format, const struct SpStreamInfo *stream_info, void *context)`

Callback to provide track details to the application.

To register this callback, use the function [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks).

**See also**

- [SpStreamInfo](#spstreaminfo)

### SpCallbackStreamData

* * *

[*Return to header index*](#media)

`1`

`typedef size_t(* SpCallbackStreamData) (unsigned int stream_id, const void *buf, size_t len, uint32_t offset, void *context)`

Callback for delivering data to the integration.

To register this callback, use the function [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks). This callback is called up to 4 times in a single pump until the integration accepts data less than buffer length or when all data from the download buffer is exhausted.

### SpCallbackStreamEnd

* * *

[*Return to header index*](#media)

`1`

`typedef void(* SpCallbackStreamEnd) (unsigned int stream_id, void *context)`

Callback to tell integration that all data was delivered.

To register this callback, use the function [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks). stream\_id Unique identifier to identify tracks context Context pointer that was passed when registering the callback

### SpCallbackStreamGetPosition

* * *

[*Return to header index*](#media)

`1`

`typedef uint32_t(* SpCallbackStreamGetPosition) (unsigned int stream_id, void *context)`

Callback to get the playback position in milliseconds.

To register this callback, use the function [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks).

### SpCallbackStreamSeekToPosition

* * *

[*Return to header index*](#media)

`1`

`typedef void(* SpCallbackStreamSeekToPosition) (unsigned int stream_id, uint32_t position_ms, void *context)`

Callback to tell the integration to seek to a position.

To register this callback, use the function [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks). When receiving this callback, the integration should start to seek to the given position. The integration is expected to call [SpSetDownloadPosition()](#spsetdownloadposition) to instruct eSDK to start downloading from a byte offset corresponding to the position given in this callback. If the position exceeds the length of the track the integration is expected to seek as close as possible to the end. stream\_id Unique identifier to identify tracks position\_ms Position in time within the track where to seek to context Context pointer that was passed when registering the callback

### SpCallbackStreamFlush

* * *

[*Return to header index*](#media)

`1`

`typedef uint32_t(* SpCallbackStreamFlush) (unsigned int *playing_stream_id, void *context)`

Callback to tell the integration to flush.

To register this callback, use the function [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks). When receiving this callback, the integration should forget all queued audio and compressed data.

### SpMediaFormat

* * *

[*Return to header index*](#media)

`1`

`enum SpMediaFormat {`

`2`

`3`

`};`

Media formats.

### SpRegisterStreamCallbacks

* * *

[*Return to header index*](#media)

`1`

`SpError SpRegisterStreamCallbacks(struct SpStreamCallbacks *cb, void *context)`

Register callbacks related to the delivery API.

### SpNotifySeekComplete

* * *

[*Return to header index*](#media)

`1`

`SpError SpNotifySeekComplete(unsigned int stream_id)`

API to notify eSDK of the completion of seek operation.

### SpNotifyTrackLength

* * *

[*Return to header index*](#media)

`1`

`SpError SpNotifyTrackLength(unsigned int stream_id, uint32_t length_ms)`

API to notify eSDK of the track length in milliseconds.

### SpNotifyTrackError

* * *

[*Return to header index*](#media)

`1`

`SpError SpNotifyTrackError(unsigned int stream_id, uint32_t position_ms, const char *reason)`

API to notify eSDK of any track errors with last played position.

### SpNotifyStreamPlaybackStarted

* * *

[*Return to header index*](#media)

`1`

`SpError SpNotifyStreamPlaybackStarted(unsigned int stream_id)`

Notify eSDK that the first audio sample of the delivery has been played.

This is used by the eSDK to measure playback latency.

### SpNotifyStreamPlaybackContinued

* * *

[*Return to header index*](#media)

`1`

`SpError SpNotifyStreamPlaybackContinued(unsigned int stream_id)`

Notify eSDK that the first audio sample after a flush of a delivery has been played.

This is used by the eSDK to measure seek latency.

### SpNotifyStreamPlaybackFinishedNaturally

* * *

[*Return to header index*](#media)

`1`

`SpError SpNotifyStreamPlaybackFinishedNaturally(unsigned int stream_id, uint32_t last_pos_ms)`

Notify eSDK that the delivery playback finished by playing the last sample of the delivery.

### SpSetDownloadPosition

* * *

[*Return to header index*](#media)

`1`

`SpError SpSetDownloadPosition(unsigned int stream_id, uint32_t byte_offset)`

API to instruct eSDK to start downloading from a given byte offset.

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

[SP\_NO\_INDEX](#sp_no_index)-1 [SP\_MAX\_UUID\_LENGTH](#sp_max_uuid_length)36 [SP\_MAX\_SOURCE\_TYPE\_LENGTH](#sp_max_source_type_length)63 [SP\_MAX\_SOURCE\_URI\_LENGTH](#sp_max_source_uri_length)511 [SP\_MAX\_REFERRER\_LENGTH](#sp_max_referrer_length)16 [SP\_PLAYOPTIONS\_INITIALIZER\_LOGGING\_PARAMS](#sp_playoptions_initializer_logging_params)Internal macro. [SP\_PLAYOPTIONS\_INITIALIZER](#sp_playoptions_initializer)*See macro below*

## Data Structures

* * *

[Return to header index](#play)

[SpSourceInfo](#spsourceinfo)Metadata for identifying where a playback request originated from. [SpPlayOptions](#spplayoptions)PlayOptions passed to [SpPlayUriWithOptions()](#spplayuriwithoptions). Use [SP\_PLAYOPTIONS\_INITIALIZER](#sp_playoptions_initializer) for initializing with default values.

## Functions

* * *

[Return to header index](#play)

[SpPlayUri](#spplayuri)Start local playback of the given Spotify URI. [SpPlayUriWithOptions](#spplayuriwithoptions)Start local playback of the given Spotify URI with additional options. [SpPlayContextUri](#spplaycontexturi)Start local playback of the given Spotify URI with an optional track UID. [SpQueueUri](#spqueueuri)Queue a URI. The track will be in queue only after kSpPlaybackNotifyQueuedTrackAccepted event is raised, but for UI purposes one can choose to monitor for kSpPlaybackNotifyMetadataChanged instead. [SpPlaybackBecomeActiveDevice](#spplaybackbecomeactivedevice)Become active without starting to play.

### SP\_NO\_INDEX

* * *

[*Return to header index*](#play)

Indicates that the index value is not set. Note: Can only be used with eSDK 3.

**See also**

- [SpPlayUri](#spplayuri)

### SP\_MAX\_UUID\_LENGTH

* * *

[*Return to header index*](#play)

`1`

`#define SP_MAX_UUID_LENGTH 36`

Maximum length of a UUID.

A 128 bit UUID containing 32 hexadecimal digits in five groups separated by hyphens.

### SP\_MAX\_SOURCE\_TYPE\_LENGTH

* * *

[*Return to header index*](#play)

`1`

`#define SP_MAX_SOURCE_TYPE_LENGTH 63`

Maximum length of the type of playback source.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SpPlayUri](#spplayuri)

### SP\_MAX\_SOURCE\_URI\_LENGTH

* * *

[*Return to header index*](#play)

`1`

`#define SP_MAX_SOURCE_URI_LENGTH 511`

Maximum length of the source URIs.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SpPlayUri](#spplayuri)

### SP\_MAX\_REFERRER\_LENGTH

* * *

[*Return to header index*](#play)

`1`

`#define SP_MAX_REFERRER_LENGTH 16`

Maximum length of the referrer.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SpPlayUri](#spplayuri)

### SP\_PLAYOPTIONS\_INITIALIZER\_LOGGING\_PARAMS

* * *

[*Return to header index*](#play)

`1`

`#define SP_PLAYOPTIONS_INITIALIZER_LOGGING_PARAMS`

Internal macro.

**See also**

- [SP\_PLAYOPTIONS\_INITIALIZER](#sp_playoptions_initializer)

### SP\_PLAYOPTIONS\_INITIALIZER

* * *

[*Return to header index*](#play)

`1`

`#define SP_PLAYOPTIONS_INITIALIZER { \`

`2`

`/*.from_index =*/`

Macro for initialization of *struct* [SpPlayOptions.](#spplayoptions) Use it instead of memset() due to the fact that some fields are optional and encoded as non-zero values.

### SpSourceInfo

* * *

[*Return to header index*](#play)

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

Metadata for identifying where a playback request originated from.

**See also**

- [SpPlayUri](#spplayuri)

*char* typeThe type of playlist/context/UI view that caused this playback to start. Note: If set, this MUST be one of the following strings (unless told otherwise): *char* uriThe URI of the parent container, if there is one. *char* expected\_track\_uriThe URI of the track that is expected to play. *char* referrerThe view you were in prior to initiating playback.

### SpPlayOptions

* * *

[*Return to header index*](#play)

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

`int repeat_mode;`

`7`

`const struct SpSourceInfo *source_info;`

`8`

`};`

PlayOptions passed to [SpPlayUriWithOptions()](#spplayuriwithoptions). Use [SP\_PLAYOPTIONS\_INITIALIZER](#sp_playoptions_initializer) for initializing with default values.

**Example:**

`1`

`struct SpPlayOptionsoptions= SP_PLAYOPTIONS_INITIALIZER;`

*int* from\_indexTrack index in the Context from which playback should start. Use [SP\_NO\_INDEX](#sp_no_index) if no specific index is required. In case of non-shuffled context this will result in the first track of the context being played whereas in shuffled context this will result in a random track being played. *const* *char* * from\_uidThe UID to identify a unique track in the context. *int* offset\_msThe time offset to start playing specified track from. *int* shuffle\_contextSet to enable or disable shuffle mode for the requested playback command. *int* repeat\_modeSet to enable or disable repeat mode for the requested playback command. *const* *struct* [SpSourceInfo](#spsourceinfo) * source\_infoMetadata about what user action caused this playback event, and the expected result.

### SpPlayUri

* * *

[*Return to header index*](#play)

`1`

`SpError SpPlayUri(const char *uri, int index, int offset_ms, const struct SpSourceInfo *source, int alias_index)`

Start local playback of the given Spotify URI.

This call starts playback of a Spotify URI, such as a playlist, album, artist, or track. Valid Spotify URIs can be obtained via the Spotify Web API. Using this call will 'pull' playback from any other Spotify Connect client active on the same account. Note that there may be a lag between the introduction of new URI types and support for playing them with this call.

**See also**

- [SpSourceInfo](#spsourceinfo)
- [SP\_NO\_INDEX](#sp_no_index)

### SpPlayUriWithOptions

* * *

[*Return to header index*](#play)

`1`

`SpError SpPlayUriWithOptions(const char *uri, const struct SpPlayOptions *opts, int alias_index)`

Start local playback of the given Spotify URI with additional options.

### SpPlayContextUri

* * *

[*Return to header index*](#play)

`1`

`SpError SpPlayContextUri(const char *uri, const char *from_uid, int offset_ms, const struct SpSourceInfo *source, int alias_index)`

Start local playback of the given Spotify URI with an optional track UID.

This call will start playback of any Spotify context URI. In addition, it allows the client to provide a UID to start the playback from a given track in the context. The main difference between UIDs and the field [SpSourceInfo::expected\_track\_uri](#spsourceinfo) is that while one track URI can occur more than once in the context, UIDs are unique for each track in it. Valid Spotify URIs can be obtained via the Spotify Web API. Track UIDs are currently available when resolving contexts from a small subset of services. Using this call will 'pull' playback from any other Spotify Connect client active on the same account.

**See also**

- [SpPlayUriWithOptions](#spplayuriwithoptions)
- [SpPlayOptions::from\_uid](#spplayoptions)

### SpQueueUri

* * *

[*Return to header index*](#play)

`1`

`SpError SpQueueUri(const char *uri)`

Queue a URI. The track will be in queue only after kSpPlaybackNotifyQueuedTrackAccepted event is raised, but for UI purposes one can choose to monitor for kSpPlaybackNotifyMetadataChanged instead.

**See also**

- kSpPlaybackNotifyQueuedTrackAccepted
- kSpErrorInvalidRequest

### SpPlaybackBecomeActiveDevice

* * *

[*Return to header index*](#play)

`1`

`SpError SpPlaybackBecomeActiveDevice(int alias_index)`

Become active without starting to play.

alias\_index The index of the device alias that should become active. If aliases aren't used, pass SP\_NO\_ALIAS\_SELECTED. This call makes the device active, without starting to play anything, if playback is paused or no device is active. The device is active after the kSpPlaybackNotifyBecameActive event is received. If another Connect-enabled device was active and playing, it will be interrupted. If the currently active device is playing, this call behaves like [SpPlaybackPlay()](#spplaybackplay). If device aliases are used, this function will switch the selected alias. If the selected alias was changed during playback, the playback will continue uninterrupted with the new alias.

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

[SpDiskStorageCallbacks](#spdiskstoragecallbacks)Callbacks to be registered with [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks)

## Typedefs

* * *

[Return to header index](#storage)

[SpCallbackStorageAlloc](#spcallbackstoragealloc)Callback to allocate space for the resource being stored. Each successful alloc call is accompanied with a corresponding close call. It is obligatory for the user to use this callback to reserve actual space on device media for the key specified. [SpCallbackStorageWrite](#spcallbackstoragewrite)Callback for writing the data into storage. Before writing to the storage eSDK does one of two things: call alloc to reserve space for future write or call read to get the data. After that eSDK writes the data into storage. Once write is fully complete eSDK calls close callback. [SpCallbackStorageRead](#spcallbackstorageread)Callback for reading the data. Once eSDK reads all required data, the close callback is called to notify the user that the data handle referenced by storage\_key can be closed. [SpCallbackStorageClose](#spcallbackstorageclose)Callback to inform the user that the data handle referenced by storage\_key can be closed. [SpCallbackStorageDelete](#spcallbackstoragedelete)Callback to inform the user that data referenced by storage\_key should be deleted from storage. [SpCallbackThrottleRequest](#spcallbackthrottlerequest)eSDK calls this callback to figure out if it needs to limit write access to the storage.

## Functions

* * *

[Return to header index](#storage)

[SpRegisterStorageCallbacks](#spregisterstoragecallbacks)Register storage callbacks.

### SpDiskStorageCallbacks

* * *

[*Return to header index*](#storage)

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

Callbacks to be registered with [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks)

Storage callbacks must be either all NULLs or all valid pointers. Throttle callback may be NULL regardless of storage callbacks. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackStorageAlloc](#spcallbackstoragealloc) alloc\_storageAlloc storage record callback. [SpCallbackStorageWrite](#spcallbackstoragewrite) write\_storageWrite storage data callback. [SpCallbackStorageRead](#spcallbackstorageread) read\_storageRead storage data callback. [SpCallbackStorageClose](#spcallbackstorageclose) close\_storageClose storage record callback. [SpCallbackStorageDelete](#spcallbackstoragedelete) delete\_storageDelete storage record callback. [SpCallbackThrottleRequest](#spcallbackthrottlerequest) throttle\_requestAsks the client if disk writes need to be throttled.

### SpCallbackStorageAlloc

* * *

[*Return to header index*](#storage)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackStorageAlloc) (const char *storage_key, uint32_t total_size, void *context)`

Callback to allocate space for the resource being stored. Each successful alloc call is accompanied with a corresponding close call. It is obligatory for the user to use this callback to reserve actual space on device media for the key specified.

To register this callback, use the function [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks).

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The allocation of space should be done in the way that following read and write operations will succeed within the specified resource size.

### SpCallbackStorageWrite

* * *

[*Return to header index*](#storage)

`1`

`typedef int(* SpCallbackStorageWrite) (const char *storage_key, uint32_t offset, const void *data, uint32_t data_size, void *context)`

Callback for writing the data into storage. Before writing to the storage eSDK does one of two things: call alloc to reserve space for future write or call read to get the data. After that eSDK writes the data into storage. Once write is fully complete eSDK calls close callback.

To register this callback, use the function [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks).

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The application should not block or call other API functions in the callback. Offset field must always be respected on write operation. Application should consume whole data in the call.

### SpCallbackStorageRead

* * *

[*Return to header index*](#storage)

`1`

`typedef int(* SpCallbackStorageRead) (const char *storage_key, uint32_t offset, void *data, uint32_t data_size, void *context)`

Callback for reading the data. Once eSDK reads all required data, the close callback is called to notify the user that the data handle referenced by storage\_key can be closed.

To register this callback, use the function [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks).

**See also**

- [SpAPIReturnCode](#spapireturncode)

**Notes:**

- The application should not block or call other API functions in the callback. If no storage read is possible, just return 0.

### SpCallbackStorageClose

* * *

[*Return to header index*](#storage)

`1`

`typedef void(* SpCallbackStorageClose) (const char *storage_key, void *context)`

Callback to inform the user that the data handle referenced by storage\_key can be closed.

To register this callback, use the function [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks).

**Notes:**

- The application should not block or call other API functions in the callback. This callback would be called for any successful alloc. For any resource open caused by Read/Write API calls.

### SpCallbackStorageDelete

* * *

[*Return to header index*](#storage)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackStorageDelete) (const char *storage_key, void *context)`

Callback to inform the user that data referenced by storage\_key should be deleted from storage.

To register this callback, use the function [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks).

**Notes:**

- The application should not block or call other API functions in the callback.
- If the deletion operation is expected to take some time the application shall return kSpAPITryAgain for the duration of the operation and kSpAPINoError once it has been completed. It is important to not block execution of eSDK for prolonged periods (ideally less than 10ms). This callback can be called for literally any storage\_key.

### SpCallbackThrottleRequest

* * *

[*Return to header index*](#storage)

`1`

`typedef int(* SpCallbackThrottleRequest) (const char *storage_key, void *context)`

eSDK calls this callback to figure out if it needs to limit write access to the storage.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpRegisterStorageCallbacks

* * *

[*Return to header index*](#storage)

`1`

`SpError SpRegisterStorageCallbacks(struct SpDiskStorageCallbacks *cb, void *context)`

Register storage callbacks.

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

[SpTLSCallbacks](#sptlscallbacks)Callbacks to be registered with [SpRegisterTLSCallbacks()](#spregistertlscallbacks)

## Typedefs

* * *

[Return to header index](#tls)

[SpCallbackTLSInit](#spcallbacktlsinit)This callback is invoked by eSDK to let the TLS library integration perform any one-time initialization. [SpCallbackTLSDeinit](#spcallbacktlsdeinit)This callback is invoked by eSDK to let the TLS library integration perform deallocation of resources during teardown. [SpCallbackTLSCreate](#spcallbacktlscreate)This callback is invoked once in the beginning of every TLS connection. [SpCallbackTLSHandshake](#spcallbacktlshandshake)This callback is invoked by eSDK to perform the TLS handshake. [SpCallbackTLSRead](#spcallbacktlsread)This callback is invoked by eSDK to read data on a TLS connection. [SpCallbackTLSWrite](#spcallbacktlswrite)This callback is invoked by eSDK to write data on a TLS connection. [SpCallbackTLSClose](#spcallbacktlsclose)This callback should clean up any resources allocated in the connect callback. [SpCallbackTLSGetError](#spcallbacktlsgeterror)Callback invoked to get an error message for the last error.

## Functions

* * *

[Return to header index](#tls)

[SpRegisterTLSCallbacks](#spregistertlscallbacks)Register TLS-related callbacks. [SpTLSAddCARootCert](#sptlsaddcarootcert)Add root certificate to the eSDK TLS stack. [SpTLSFreeCARootCerts](#sptlsfreecarootcerts)Remove all certificates loaded on the TLS stack and free the memory used by them.

### SpTLSCallbacks

* * *

[*Return to header index*](#tls)

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

Callbacks to be registered with [SpRegisterTLSCallbacks()](#spregistertlscallbacks)

None of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackTLSInit](#spcallbacktlsinit) initCallback that performs one-time initialization. [SpCallbackTLSDeinit](#spcallbacktlsdeinit) deinitCallback that performs release of resources allocated during init. [SpCallbackTLSCreate](#spcallbacktlscreate) createCallback invoked once per connection to initialize TLS context. [SpCallbackTLSHandshake](#spcallbacktlshandshake) handshakeCallback invoked repeatedly to perform the TLS handshake. [SpCallbackTLSRead](#spcallbacktlsread) readCallback for reading from the TLS data stream. [SpCallbackTLSWrite](#spcallbacktlswrite) writeCallback for writing to the TLS data stream. [SpCallbackTLSClose](#spcallbacktlsclose) closeCallback invoked to cleanup any TLS context before closing the socket. [SpCallbackTLSGetError](#spcallbacktlsgeterror) get\_errorCallback invoked to get an error message for the last error.

### SpCallbackTLSInit

* * *

[*Return to header index*](#tls)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackTLSInit) (void *context)`

This callback is invoked by eSDK to let the TLS library integration perform any one-time initialization.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSDeinit

* * *

[*Return to header index*](#tls)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackTLSDeinit) (void *context)`

This callback is invoked by eSDK to let the TLS library integration perform deallocation of resources during teardown.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSCreate

* * *

[*Return to header index*](#tls)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackTLSCreate) (struct SpSocketHandle *socket, const char *hostname, void *context)`

This callback is invoked once in the beginning of every TLS connection.

The callback receives a socket via the pointer to [SpSocketHandle](#spsockethandle) that is already connected to the remote peer. This callback should typically allocate and set up all TLS related resources. The tls field of the [SpSocketHandle](#spsockethandle) should be used to store any connection specific state that is needed.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSHandshake

* * *

[*Return to header index*](#tls)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackTLSHandshake) (struct SpSocketHandle *socket, void *context)`

This callback is invoked by eSDK to perform the TLS handshake.

The callback is invoked repeatedly to perform the handshake. This callback is invoked repeatedly as long as it returns [kSpAPITryAgain.](#kspapitryagain) The peer verification is mandatory and the implementation of this callback must validate the peer certificate against a list of trusted CA certificates. Should return kSpAPIGenericError if the handshake failed. Any specific information about the reason for the failure will be returned in the [SpCallbackTLSGetError()](#spcallbacktlsgeterror) call.

**Notes:**

- The application must not block or call other API functions in the callback.

### SpCallbackTLSRead

* * *

[*Return to header index*](#tls)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackTLSRead) (struct SpSocketHandle *socket, void *buf, size_t len, size_t *actual, void *context)`

This callback is invoked by eSDK to read data on a TLS connection.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSWrite

* * *

[*Return to header index*](#tls)

`1`

`typedef enum SpAPIReturnCode(* SpCallbackTLSWrite) (struct SpSocketHandle *socket, const void *buf, size_t len, size_t *actual, void *context)`

This callback is invoked by eSDK to write data on a TLS connection.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSClose

* * *

[*Return to header index*](#tls)

`1`

`typedef void(* SpCallbackTLSClose) (struct SpSocketHandle *socket, void *context)`

This callback should clean up any resources allocated in the connect callback.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpCallbackTLSGetError

* * *

[*Return to header index*](#tls)

`1`

`typedef int(* SpCallbackTLSGetError) (struct SpSocketHandle *socket, char *buf, size_t len, void *context)`

Callback invoked to get an error message for the last error.

The implementation of this callback should put an error message in the form of a zero-terminated string in the buffer pointed to by buf. This error message should describe the latest error returned by any of the other callback functions.

**Notes:**

- The application should not block or call other API functions in the callback.

### SpRegisterTLSCallbacks

* * *

[*Return to header index*](#tls)

`1`

`SpError SpRegisterTLSCallbacks(struct SpTLSCallbacks *callbacks, void *context)`

Register TLS-related callbacks.

**Notes:**

- A call to this function has to be performed before [SpInit()](#spinit) is called. Calling this function when eSDK is initialized will fail with [kSpErrorAlreadyInitialized.](#ksperroralreadyinitialized) The function will return kSpErrorUnsupported in the eSDK configurations with built-in TLS.

### SpTLSAddCARootCert

* * *

[*Return to header index*](#tls)

`1`

`SpError SpTLSAddCARootCert(const uint8_t *certificate, size_t length, int *underlying_error)`

**This function is deprecated and should not be used. See alternatives:**

- [SpTLSCallbacks](#sptlscallbacks)

Add root certificate to the eSDK TLS stack.

eSDK uses TLS secured HTTPS connections to download media files from CDN (Content Delivery Network) servers. All CDN servers are using certificates from common Certificate Authorities (CA). eSDK cannot read Certificate Authority (CA) root certificates from the operating system. The purpose of this function is to provide eSDK the CA root certificates which eSDK needs. As an example, integration can use the CA certificate bundle from Mozilla: [https://curl.se/docs/caextract.html](https://curl.se/docs/caextract.html) This API is cumulative and can be called several times until the integration has loaded all the certificates. This API allocates and owns the memory to store the certificates. The integration can reuse the memory used to pass the certificates (first parameter)

**Notes:**

- If the buffer is a PEM-format certificate, it must be NULL-terminated.
- If the buffer is a PEM-format certificate, this length must include the NULL termination.
- Calls to this function have to be performed before [SpInit()](#spinit) is called or after [SpFree()](#spfree).

### SpTLSFreeCARootCerts

* * *

[*Return to header index*](#tls)

`1`

`SpError SpTLSFreeCARootCerts(void)`

**This function is deprecated and should not be used. See alternatives:**

- [SpTLSCallbacks](#sptlscallbacks)

Remove all certificates loaded on the TLS stack and free the memory used by them.

This API must be called before calling [SpInit()](#spinit) or after [SpFree()](#spfree).

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

[SpTokenCallbacks](#sptokencallbacks)Callbacks to be registered with [SpRegisterTokenCallbacks()](#spregistertokencallbacks)

## Typedefs

* * *

[Return to header index](#token)

[SpCallbackConnectionReceiveAccessToken](#spcallbackconnectionreceiveaccesstoken)Callback to deliver the access token requested by [SpConnectionRequestAccessToken()](#spconnectionrequestaccesstoken). [SpCallbackConnectionReceiveAuthCode](#spcallbackconnectionreceiveauthcode)Callback to deliver the access token requested by [SpConnectionRequestAuthCode()](#spconnectionrequestauthcode).

## Functions

* * *

[Return to header index](#token)

[SpRegisterTokenCallbacks](#spregistertokencallbacks)Register token callbacks. [SpConnectionRequestAccessToken](#spconnectionrequestaccesstoken)Request an access token for the logged in user. [SpConnectionRequestAuthCode](#spconnectionrequestauthcode)Request an authorization code for the logged in user.

### SpTokenCallbacks

* * *

[*Return to header index*](#token)

`1`

`struct SpTokenCallbacks {`

`2`

`SpCallbackConnectionReceiveAccessToken on_access_token;`

`3`

`SpCallbackConnectionReceiveAuthCode on_auth_code;`

`4`

`};`

Callbacks to be registered with [SpRegisterTokenCallbacks()](#spregistertokencallbacks)

Any of the pointers may be NULL. See the documentation of the callback typedefs for information about the individual callbacks.

[SpCallbackConnectionReceiveAccessToken](#spcallbackconnectionreceiveaccesstoken) on\_access\_tokenAccess token event callbacks. [SpCallbackConnectionReceiveAuthCode](#spcallbackconnectionreceiveauthcode) on\_auth\_codeAuthorization code event callbacks.

### SpCallbackConnectionReceiveAccessToken

* * *

[*Return to header index*](#token)

`1`

`typedef void(* SpCallbackConnectionReceiveAccessToken) (const char *token_json, int error, void *context)`

Callback to deliver the access token requested by [SpConnectionRequestAccessToken()](#spconnectionrequestaccesstoken).

**Notes:**

- The JSON object looks as following: "accessToken":"tokendata", "expiresIn":expiryinseconds,//typically3600 "tokenType":"tokentype"//typically"Bearer"

### SpCallbackConnectionReceiveAuthCode

* * *

[*Return to header index*](#token)

`1`

`typedef void(* SpCallbackConnectionReceiveAuthCode) (const char *token_json, int error, void *context)`

Callback to deliver the access token requested by [SpConnectionRequestAuthCode()](#spconnectionrequestauthcode).

**Notes:**

- The JSON object looks as following: "code":"tokendata", "redirectUri":"someUri"

### SpRegisterTokenCallbacks

* * *

[*Return to header index*](#token)

`1`

`SpError SpRegisterTokenCallbacks(struct SpTokenCallbacks *cb, void *context)`

Register token callbacks.

### SpConnectionRequestAccessToken

* * *

[*Return to header index*](#token)

`1`

`SpError SpConnectionRequestAccessToken(const char *scope)`

Request an access token for the logged in user.

scope A comma-separated list of scopes for the resulting access token. See [https://developer.spotify.com/documentation/web-api/concepts/scopes/](https://developer.spotify.com/documentation/web-api/concepts/scopes/)

### SpConnectionRequestAuthCode

* * *

[*Return to header index*](#token)

`1`

`SpError SpConnectionRequestAuthCode(const char *scope)`

Request an authorization code for the logged in user.

**Notes:**

- The string scope must not be longer than 425 characters.