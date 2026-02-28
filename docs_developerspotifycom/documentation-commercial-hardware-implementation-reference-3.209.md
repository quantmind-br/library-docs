---
title: API Reference eSDK 3.209.360 | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.209
source: crawler
fetched_at: 2026-02-27T23:41:30.48346-03:00
rendered_js: true
word_count: 3544
summary: This document provides a technical reference for the spotify_embedded.h header file, detailing data structures, macros, and constants for managing media playback, metadata, and device configurations in the Spotify Embedded SDK.
tags:
    - spotify-sdk
    - embedded-systems
    - c-api
    - audio-playback
    - metadata-management
    - api-reference
category: reference
---

- [Main](#main)
- [Content](#content)
- [Hal](#hal)
- [Log](#log)
- [Media](#media)
- [Play](#play)
- [Storage](#storage)
- [Tls](#tls)
- [Token](#token)

## Main

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded.h"`

- [macros and constants](#main-macros-and-constants)
- [data structures](#main-data-structures)
- [enumerations](#main-enumerations)

## macros and constants

* * *

*[main](#main) -&gt; macros and constants*

## data structures

* * *

*[main](#main) -&gt; data structures*

[SpPlayerModeDisallowReasons](#spplayermodedisallowreasons)This *struct* stores a Mode value and the restriction disallow reasons associated with it. [SpPlayerModeRestrictions](#spplayermoderestrictions)this *struct* stores a Mode key and the list of restricted values. [SpPlaybackRestrictions](#spplaybackrestrictions)Playback restrictions. [SpFormat](#spformat)Mapping of which media formats are supported in which DRM. [SpMetadata](#spmetadata)Track metadata. [SpAdMetadata](#spadmetadata)Key value pair for Ad-related metadata. [SpZeroConfDeviceAlias](#spzeroconfdevicealias)ZeroConf DeviceAlias. [SpZeroConfVars](#spzeroconfvars)ZeroConf variables. [SpSampleFormat](#spsampleformat)Sample format of the audio data. [SpPlaybackCallbacks](#spplaybackcallbacks)Callbacks to be registered with [SpRegisterPlaybackCallbacks()](#spregisterplaybackcallbacks) [SpDebugCallbacks](#spdebugcallbacks)Callbacks to be registered with [SpRegisterDebugCallbacks()](#spregisterdebugcallbacks) [SpConnectionCallbacks](#spconnectioncallbacks)Callbacks to be registered with [SpRegisterConnectionCallbacks()](#spregisterconnectioncallbacks) [SpDeviceAlias](#spdevicealias)Device alias definition. [SpConfig](#spconfig)Configuration. [SpDeviceAliasCallbacks](#spdevicealiascallbacks)Callbacks to be registered with [SpRegisterDeviceAliasCallbacks()](#spregisterdevicealiascallbacks)

## enumerations

* * *

*[main](#main) -&gt; enumerations*

### SP\_MAX\_METADATA\_KEY\_LENGTH

* * *

*[main](#main) -&gt; [macros and constants](#main-macros-and-constants) -&gt; SP\_MAX\_METADATA\_KEY\_LENGTH*

`1`

`#define SP_MAX_METADATA_KEY_LENGTH 32`

Maximum number of characters in the key of a [SpAdMetadata](#spadmetadata) *struct*, not counting the terminating NULL.

**See also**

- [SpAdMetadata](#spadmetadata)

### SP\_MAX\_METADATA\_VALUE\_LENGTH

* * *

*[main](#main) -&gt; [macros and constants](#main-macros-and-constants) -&gt; SP\_MAX\_METADATA\_VALUE\_LENGTH*

`1`

`#define SP_MAX_METADATA_VALUE_LENGTH 64`

Maximum number of characters in the value of a [SpAdMetadata](#spadmetadata) *struct*, not counting the terminating NULL.

**See also**

- [SpAdMetadata](#spadmetadata)

### SpPlayerModeDisallowReasons

* * *

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpPlayerModeDisallowReasons*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpPlayerModeRestrictions*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpPlaybackRestrictions*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpFormat*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpMetadata*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpAdMetadata*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpZeroConfDeviceAlias*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpZeroConfVars*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpSampleFormat*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpPlaybackCallbacks*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpDebugCallbacks*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpConnectionCallbacks*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpDeviceAlias*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpConfig*

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

*[main](#main) -&gt; [data structures](#main-data-structures) -&gt; SpDeviceAliasCallbacks*

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

### SpDrmFormat

* * *

*[main](#main) -&gt; [enumerations](#main-enumerations) -&gt; SpDrmFormat*

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

## Content

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_content.h"`

- [data structures](#content-data-structures)

## data structures

* * *

*[content](#content) -&gt; data structures*

[SpContentCallbacks](#spcontentcallbacks)Callbacks to be registered with [SpRegisterContentCallbacks()](#spregistercontentcallbacks)

### SpContentCallbacks

* * *

*[content](#content) -&gt; [data structures](#content-data-structures) -&gt; SpContentCallbacks*

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

## Hal

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_hal.h"`

- [data structures](#hal-data-structures)

## data structures

* * *

*[hal](#hal) -&gt; data structures*

[SpSockaddr](#spsockaddr)Struct contains resolved hostname IP address and its family. [SpDnsHALCallbacks](#spdnshalcallbacks)Callbacks to be registered with [SpRegisterDnsHALCallbacks()](#spregisterdnshalcallbacks) [SpSocketHandle](#spsockethandle)Socket handle type. [SpSocketHALCallbacks](#spsockethalcallbacks)Callbacks to be registered with [SpRegisterSocketHALCallbacks()](#spregistersockethalcallbacks)

### SpSockaddr

* * *

*[hal](#hal) -&gt; [data structures](#hal-data-structures) -&gt; SpSockaddr*

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

*[hal](#hal) -&gt; [data structures](#hal-data-structures) -&gt; SpDnsHALCallbacks*

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

*[hal](#hal) -&gt; [data structures](#hal-data-structures) -&gt; SpSocketHandle*

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

*[hal](#hal) -&gt; [data structures](#hal-data-structures) -&gt; SpSocketHALCallbacks*

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

## Log

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_log.h"`

- [macros and constants](#log-macros-and-constants)
- [data structures](#log-data-structures)

## macros and constants

* * *

*[log](#log) -&gt; macros and constants*

## data structures

* * *

*[log](#log) -&gt; data structures*

[SpLogTraceObject](#splogtraceobject)Trace object.

### SP\_FILE\_NAME

* * *

*[log](#log) -&gt; [macros and constants](#log-macros-and-constants) -&gt; SP\_FILE\_NAME*

`1`

`#define SP_FILE_NAME __FILE__`

Preferred macro to log the file name, you might redefine [SP\_FILE\_NAME](#sp_file_name) using basename() or use -ffile-prefix-map.

### SpLogTraceObject

* * *

*[log](#log) -&gt; [data structures](#log-data-structures) -&gt; SpLogTraceObject*

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

## Media

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_media.h"`

- [data structures](#media-data-structures)

## data structures

* * *

*[media](#media) -&gt; data structures*

[SpStreamInfo](#spstreaminfo)Stream Parameters. [SpStreamCallbacks](#spstreamcallbacks)Callbacks to be registered with [SpRegisterStreamCallbacks()](#spregisterstreamcallbacks)

### SpStreamInfo

* * *

*[media](#media) -&gt; [data structures](#media-data-structures) -&gt; SpStreamInfo*

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

*[media](#media) -&gt; [data structures](#media-data-structures) -&gt; SpStreamCallbacks*

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

## Play

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_play_api.h"`

- [data structures](#play-data-structures)

## data structures

* * *

*[play](#play) -&gt; data structures*

[SpSourceInfo](#spsourceinfo)Metadata for identifying where a playback request originated from. [SpPlayOptions](#spplayoptions)PlayOptions passed to [SpPlayUriWithOptions()](#spplayuriwithoptions). Use [SP\_PLAYOPTIONS\_INITIALIZER](#sp_playoptions_initializer) for initializing with default values.

### SpSourceInfo

* * *

*[play](#play) -&gt; [data structures](#play-data-structures) -&gt; SpSourceInfo*

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

*[play](#play) -&gt; [data structures](#play-data-structures) -&gt; SpPlayOptions*

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

## Storage

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_storage.h"`

- [data structures](#storage-data-structures)

## data structures

* * *

*[storage](#storage) -&gt; data structures*

[SpDiskStorageCallbacks](#spdiskstoragecallbacks)Callbacks to be registered with [SpRegisterStorageCallbacks()](#spregisterstoragecallbacks)

### SpDiskStorageCallbacks

* * *

*[storage](#storage) -&gt; [data structures](#storage-data-structures) -&gt; SpDiskStorageCallbacks*

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

## Tls

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_tls.h"`

- [data structures](#tls-data-structures)

## data structures

* * *

*[tls](#tls) -&gt; data structures*

[SpTLSCallbacks](#sptlscallbacks)Callbacks to be registered with [SpRegisterTLSCallbacks()](#spregistertlscallbacks)

### SpTLSCallbacks

* * *

*[tls](#tls) -&gt; [data structures](#tls-data-structures) -&gt; SpTLSCallbacks*

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

## Token

* * *

[Back to top of page](#top)

`1`

`#include "spotify_embedded_token.h"`

- [data structures](#token-data-structures)

## data structures

* * *

*[token](#token) -&gt; data structures*

[SpTokenCallbacks](#sptokencallbacks)Callbacks to be registered with [SpRegisterTokenCallbacks()](#spregistertokencallbacks)

### SpTokenCallbacks

* * *

*[token](#token) -&gt; [data structures](#token-data-structures) -&gt; SpTokenCallbacks*

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