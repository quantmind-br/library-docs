---
title: eSDK Changelog | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/changelog
source: crawler
fetched_at: 2026-02-27T23:41:53.500998-03:00
rendered_js: true
word_count: 5819
summary: This document provides a chronological log of version updates, bug fixes, and API changes for the Spotify Commercial Hardware eSDK.
tags:
    - spotify-sdk
    - release-notes
    - changelog
    - hardware-integration
    - api-changes
    - firmware-development
category: reference
---

[Skip to content](#main)

### [Version 3.211.126](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.211)

- Fix Fixed an issue where long track titles were truncated in SpMetadata.
- Fix Fixed an issue where long album titles were truncated in SpMetadata.
- Fix Fixed an issue where long artist names were truncated in SpMetadata.
- Fix Made non-functional performance optimizations to a few frequently called code paths.

### [Version 3.210.385](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.210)

- Fix Fixed a regression introduced in 3.210.377 where we were asking for position unnecessarily while observing.

### [Version 3.210.377](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.210)

- API-Change Feature Added SpPlayRecommendation() API.
- Fix Improved PortAudio example code that could glitch.
- Fix Removed obsolete include from mbedTLS.c example code.
- Fix Increased the frequency of calls to SpCallbackStreamGetPosition() at certain intervals.

### [Version 3.209.360](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.209)

- API-Change Feature Removed support for builtin TLS.
- Fix Fixed an issue where we would resume at a too early position when pulling playback after being inactive.
- Fix Reworded the description of SpPlaybackSetBandwidthLimit() somewhat.

### [Version 3.208.26](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.208)

- Fix Started notifying integrations that Zeroconf variables have changed after calling SpSetDeviceAliases().

### [Version 3.208.18](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.208)

- Fix Made IPv4 preferred over IPv6 in mixed setups, with IPv6 used only when IPv4 is unavailable.

### [Version 3.206.295](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.206)

- API-Change Feature Removed deprecated APIs SetAvailableToPlay and IsAvailableToPlay. Use SpPlaybackIsDeviceControllable(), SpPlaybackSetDeviceControllable() and SpPlaybackSetDeviceInactive() instead.

### [Version 3.205.205](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.205)

- Fix Fixed a regression introduced in 3.200 where there would be an underrun if queuing a track after starting playback of a single, unrepeated track.

### [Version 3.205.189](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.205)

- Fix Fixed an issue in the example code (decoder\_mp3.c) where the logging headers were included in a way that prevented the logging hooks from being overridden.

### [Version 3.205.187](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.205)

- API-Change Feature Added support for switching between 24-bit and 16-bit formats to the osx.c example code audio driver.
- Fix Fixed an issue where we could divide by 0 in the FLAC decoder (this surfaced in ALSA and PortAudio drivers under Linux).
- Fix Avoided clipping 24-bit sample values in decoder\_flac example code.
- Fix Added support for unpacked 24-bit PCM format in osx.c example code.
- Fix Added support for 24-bit audio in example code using fixed point sample formats.
- Fix Updated the docstring for the SpPlaybackSetBitrate API to better reflect current behavior.
- Fix Made non-functional size saving changes to media\_delivery\_state.h.
- Fix Fixed an issue with distortion in decoder\_vorbis example code.
- Fix Added a migration guide for the now bit-depth agnostic example code.

### [Version 3.204.112](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.204)

- Fix Added a short doc to aid migrating the example code to 24-bit audio.
- Fix Fixed an issue with distortion in the example Ogg Vorbis decoder.

### [Version 3.204.105](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.204)

- API-Change Added support for requesting and receiving 24-bit FLAC files.
- Fix Updated the PuTTY license.
- Fix Updated example decoders, audio drivers and related glue code to handle 24-bit PCM. The tested audio drivers are ALSA and PortAudio, the remaining example audio drivers are currently untested.
- Fix Added audio\_deinit callback to osx audio example. Fixes a crash when cleaning up the osx audio driver.

### [Version 3.203.239](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.203)

- Fix Internal bug fixes.

### [Version 3.203.235](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.203)

- API-Change Removed `SpConnectionLoginPassword` API.

### [Version 3.203.233](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.203)

- Fix Fixed an issue where eSDK will not call the `SpCallbackStreamEnd` callback when the integration reports an invalid position.

### [Version 3.203.227](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.203)

- API-Change eSDK will only send the `kSpConnectionNotifyProductTypeChanged` notification if the product type is changed during a logged in session. Previously it was also sent unconditionally after each new login.
- Fix Extended list of valid values for `SpSourceInfo::type` field.
- Fix Fixed built-in mDNS implementation in order to provide all local IPv4 network addresses when queries target the specific mDNS/DNS-SD service. Align this behaviour with how queries for spotify-connect related service-type & domain "\_spotify-connect.\_tcp.local" were handled.
- Fix Extended HTTP response headers of the built-in ZeroConf HTTP server with Content-Security-Policy. When set to frame-ancestors: 'none' it prevents embedding of ZeroConf URLs into malicious webpages and therefore minimizes the risk of ZeroConf attacks. Partners who don't use the ZeroConf HTTP server provided with eSDK have to make sure they apply the same measures on their external webservers.
- Fix Fixed an issue where the last track of a context can cause media delivery to be stuck in a draining audio loop.

### [Version 3.202.369](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.202)

- Fix Fixed an issue where the last track of a context can cause media delivery to be stuck in a draining audio loop.

### [Version 3.202.356](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.202)

- Fix Internal bug fixes.

### [Version 3.202.330](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.202)

- Fix Fixed an issue with download fallback during network outage which causes a skip to the next track once reconnected.
- Fix Fixed missing error handling for setting socket into non-blocking mode on windows.
- Fix Modified Windows examples in order to use CRITICAL\_SECTION instead of mutex-based synchronisation.
- Fix Made the pytest environment compatible with Python 3.11.
- Fix Fixed an issue that caused playback to fail once storage manager had filled up the cache.
- Fix Added certificate verification in the OpenSSL example.
- Fix Split header file `media_delivery.h` in order to ease reuse of single structures. Fix include dependencies.
- Fix Renamed `decode_error` to `track_error` and made error reason configurable in MediaDelivery examples.

### [Version 3.201.448](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.201)

- Fix Fixed an error when inability of setting kSpSocketMcastSendIf option led to the missing mDNS advertisings.
- Fix Changed hal\_get\_unix\_time\_in\_milliseconds() in order to avoid overflows.
- Fix Fixed a bug where toggling shuffle/repeat while being paused causes data corruption in the audio- and download buffers.
- Fix Fixed an issue with audio clipping in the vorbis decoder example code.

### [Version 3.201.430](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.201)

- Fix Made example implementation of MediaDelivery API more modular. The header `media_delivery.h` was split into 4 single files and include dependencies were revisited. This change made it possible for partner integrations to add our example code to their projects unmodified.

### [Version 3.201.417](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.201)

- Fix Improved error handling for sending of mDNS messages. Introduced a check whether the outgoing interface was suitable for sending a multicast message (see `SpCallbackSocketSetOption()` & `kSpSocketMcastSendIf`). Send multiple A records as part of a single mDNS answer.
- Fix Improved out-of-sync playback position between the active device and its observers. In case of long buffering or seek there will be an additional update of the connect cluster.
- Fix Fixed an issue where a new seek while a seek was ongoing caused track failure.
- Fix Changed the implementation of seek beyond the track length to no longer result in a skip next. Rather, the integration should seek to the very end of the track.
- Fix Fixed minor inaccuracy of playback position which might occur during seek.
- Fix Removed support for legacy streaming from Spotify's proprietary access point.
- Fix Removed `TrackStream::position_ms` in MediaDelivery examples and replaced it with `TrackStream::position_samples`. This was done in order to avoid intermediate conversion of samples to milliseconds and to minimize rounding errors.
- Fix Cleaned up example code from internal preprocessor directives.
- Fix Added support for mono tracks to the vorbis decoder in example code. Mono tracks are very rare as most mono tracks are converted to stereo.
- Fix Stopped sending unconditional MetadataChanged notifications on calls to `SpNotifyTrackLength()`. The notification is only sent if the track length actually differs from the information in eSDK's metadata.
- Fix Fixed truncation of oversized values in class `SpDeviceAlias::display_name` which was ignoring UTF-8 before.
- Fix Fixed length check for the passed URI in `SpQueueUri()`.
- Fix Fixed validation of passed formats in `SpRestrictDrmMediaFormats()`. Previously only the first item of the array was checked.
- Fix Changed the Posix HAL to use `clock_gettime()` instead of `gettimeofday()`.
- Fix Updated the documentation on HTTPS support and removed deprecated TLS APIs from example code.
- Fix Marked `SpTLSAddCARootCert()` and `SpTLSFreeCARootCerts()` as deprecated and to be removed in a future release.
- Fix Marked `SpConnectionLoginPassword()` as deprecated and to be removed in a future release.
- Fix Removed obsolete notifications `kSpPlaybackNotifyLostPermission` and `kSpPlaybackNotifyTrackDelivered` from the public header.
- Fix Corrected documentation for `kSpErrorInvalidRequest`. It is used for asynchronous notifications about failed attempts to call `SpQueueUri()`.

### [Version 3.200.454](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.200)

- Fix Fixed an issue where a new seek while a seek was ongoing caused track failure.
- Fix Fixed an issue where calling `SpNotifyStreamPlaybackStarted()` multiple times for the same track would incorrectly result in `kSpErrorAlreadyInitialized` error.

### [Version 3.200.445](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.200)

- Fix Fixed an issue in the example OGG/Vorbis decoder where a seek to a position near the end of the file would cause an error.
- Fix Made the example vorbis decoder play mono tracks. These are very rare as most mono tracks are converted to stereo.
- Fix Flush of delivery stream is moved prior to track pipeline re-enumeration to avoid integration returning stale stream id at media seek.
- Fix Removed very chatty async DNS printouts about a request being in progress.
- Fix Fixed an issue where a combination of queuing and seeking could corrupt the internal download buffer and eSDK would deliver corrupt data to the integration.
- Fix Changed the internal scheduling to prevent calls to the integration from `SpSetDownloadPosition()` function.
- Fix Added more robust handling of `FINAL_JUMP_OFFSET` to the example implementation of Media Delivery API.
- Fix Fixed handling of retryable error codes in the example of TLS handshake function for OpenSSL.

### [Version 3.200.405](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.200)

- Fix Relaxed the checks on position reporting allowing one second of deviation.
- Fix Fixed too chatty mDNS advertisements which contradict RFC6762 and Bonjour Conformance Test.

### [Version 3.200.397](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.200)

- Fix Fixed mangling of symbols for certain builds.

### [Version 3.200.389](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.200) (Standard builds only)

- API-Change Feature Introduced ability to set repeat mode in `SpPlayUriWithOptions()`.
- API-Change Feature Added support for asynchronous name lookup library (libanl, glibc &gt;= 2.2.3). It avoids blocking of eSDK and reduces the amount of stutters. Libanl will be used automatically in case toolchain provides it. User code has to be linked with `-lanl`.
- API-Change Fix Removed Preset APIs from eSDK API, see [requirements presets](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#presets).
- API-Change Fix Fixed `SpPlayUriWithOptions()` which didn't allow to turn off shuffling mode. This fix changes the semantics of `struct SpPlayOptions::shuffle_change` and requires modification on the caller side.
- API-Change Fix Introduced macro `SP_PLAYOPTIONS_INITIALIZER` which has be used for initialization of `SpPlayOptions` structure.
- Fix Corrected and extended documentation about built-in implementation of DNS lookups as well as corresponding callbacks.
- Fix Updated seeking in the example vorbis decoder to be millisecond accurate. The `seek_result` enum is expanded with a `SEEK_DONE` value that signifies that seeking has now reached the desired PCM offset.
- Fix Remove usage of floating point arithmetics with double precision from the example code.
- Fix Make examples more platform independent.
- Fix Updated link to the eSDK [changelog](https://developer.spotify.com/documentation/commercial-hardware/implementation/changelog).
- API-Change Fix Added documentation about the field `struct SpPlayOptions::from_index` being optional.
- Fix Fixed an issue where the downloading stream could be stalled due to erroneous flagging of two tracks downloading at the same time.
- Fix Fixed a bug where track byte\_offset was not cleared at reset of the stream delivery.
- Fix Fixed `SpQueueUri()` which might stop working after temporary network issues.
- Fix Fixed missing check in `SpGetMetadataImageURL()` which supposed to return `kSpErrorFailed` if the output buffer is not big enough.
- Fix Fixed an issue where eSDK made a flush call to the integration even though no playback was active.
- Fix Added error code `kSpErrorGeneralDownloadError` which can be used for notification over `SpCallbackError()` callback. Corrected documentation for `kSpErrorGeneralPlaybackError` with respect to the fact that it doesn't require any additional error handling.

### [Version 3.199.414](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- Fix Fixed an issue where calling `SpNotifyStreamPlaybackStarted()` multiple times for the same track would incorrectly result in `kSpErrorAlreadyInitialized` error.
- Fix Fixed an issue where a new seek while a seek was ongoing caused track failure.
- Fix Fixed an issue where a combination of queuing and seeking would bring eSDK to a state where upcoming track will never be delivered and as a result the playback will stop.
- Fix Fixed a bug where `on_seek_callback` would be called twice when seeking in the delivering track.

### [Version 3.199.383](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- Fix Fixed too chatty mDNS advertisements which contradict RFC6762 and Bonjour Conformance Test.

### [Version 3.199.379](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- Fix Fixed an issue where eSDK could end up in a broken state if the user skips immediately after transferring the playback.

### [Version 3.199.375](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- Fix Changed ad progress reporting to be more granular, the new minimum value is 1 sec instead of 15 sec.

### [Version 3.199.368](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- Fix Changed the internal scheduling to prevent calls to the integration from `SpNotify` functions. Updated the example code to call those functions in the correct order.
- Fix Updated to mbedtls v2.28.0.
- Fix Corrected documentation for `SpCallbackStreamSeekToPosition`.

### [Version 3.199.315](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- Fix Fixed an issue where decryption of downloaded audio data is causing high CPU usage.
- Fix Made the `SpConfig::platform_name` parameter optional.

### [Version 3.199.303](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.199)

- API-Change Feature Added support for loudness normalization, see documentation.
- Fix Fixed calculation of buffered samples in OSX/AudioToolbox example. In paused state it has to return the amount of samples stored in the ring buffer.
- Fix Fixed a bug to not end seek in playing track if download of upcoming track fails.
- Fix Introduced new internal calculation of playback position. This will reduce overhead caused by polling for position.
- Fix Fixed a bug to not report corrupt track for playing track if download of upcoming track fails.
- Fix Fixed an issue where the example OGG decoder could fail to parse the metadata page.
- Fix Fixed reuse stored TLS session tickets only if handshake is performed with matching host. This is relevant if built-in MbedTLS implementation is used.
- Fix Removed unnecessary re-delivery when doing a regular seek in currently downloading track.
- Fix Fixed a bug where eSDK ends up in a loop falling back to ingested track at download failure of upcoming track.
- Feature Improved documentation of media\_delivery\_* example code functions.

### [Version 3.198.103](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.198)

- Fix Fixed an issue where downloads would fail after too many network timeouts.

### [Version 3.198.85](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.198)

- Fix Fixed an issue with inaccurate seeking in the beginning of long files.

### [Version 3.198.41](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.198)

- API-Change Feature `SpPlayPreset()` and related preset APIs have been deprecated and will be removed at the start of 2022. Integrations should use `SpPlayUriWithOptions()` instead. See the product requirements for presets.
- API-Change Fix Added missing API call validation for multithreading and reentry for `SpNotifyTrackLength()` and `SpNotifyTrackError()`.
- API-Change Feature Added generic builds for linux-arm7hf and linux-aarch64.
- Feature Enabled use of TLS SessionTicket for a faster connection re-establishment (RFC5077).
- Fix Fixed memory leaks in example code for vorbis decoder.
- Fix Removed deprecated notifications `kSpPlaybackNotifyNext` and `kSpPlaybackNotifyPrev` from example code and documentation.
- Fix Extended comments to the media delivery example implementation.
- Fix Removed obsolete example code for WAV and sndio from examples/common/audio.
- Fix Removed unused parameters from `media_delivery_init` in the example code.
- Fix Updated public documentation regarding switching of audio sources. Suggested to use `SpPlaybackSetDeviceInactive()` instead of SpPlaybackPause().
- Fix Fixed an issue where the updated track length (as reported by the application via `SpNotifyTrackLength()`) was not propagated to the observing clients.
- Fix Fixed an issue with inaccurate seeking in the beginning of long files.
- Fix Fixed an assertion failure in `CallbackStreamGetPosition()` in case the integration called `SpPlaybackGetPosition()` immediately after track change when `kSpPlaybackNotifyMetadataChanged` was received.
- Fix Restored correct invocation of `SpCallbackStreamEnd` callback which could be suppressed for multiple consecutive short tracks.

### [Version 3.194.71](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194)

- Fix Removed superfluous flush for a skip made over connect.
- Fix Updated mbedTLS to include upstream bug-fixes

### [Version 3.194.67](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194)

- Fix Fixed an issue where the hostname is not properly parsed for some external URLs.

### [Version 3.194.61](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.194)

- Fix Simplified ZeroConf URL: use /zc instead of /zc/0.
- Fix Removed platform specific implementation of `mbedtls_platform_zeroize()` in order to avoid additional glibc dependencies.
- Fix Added handling of the error returned by `SpNotifyStreamPlaybackFinishedNaturally()` in the example code.
- Fix Fixed an issue where the MP3 decoder PCM buffer is not cleared when flushing.
- Fix Fixed an issue where the fallback track doesn't start at a given seek position after the external URL failed to download.

### [Version 3.192.28](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.192)

- Fix Added context pointer to the example audio driver api.
- Fix Removed frequent logging of samples played from the example code.

### [Version 3.191.6](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.191)

- Fix Fixed a memory leak in the example code.
- Fix Fixed an issue where a track download is started but a track is already downloading.
- Feature Included Storage Manager in all (non-offline) build configurations using Storage API. Whether the Storage Manager is used depends on whether the callbacks for it are registered by the integration.
- Fix Fixed an issue where the internal ZeroConf webserver could get blocked by clients sending non-HTTP traffic on the server connection.
- Fix Fixed the example code to remove decoders on shutdown.
- Fix Removed obsolete licenses for mongoose and c-ares.

### [Version 3.189.33](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.189)

- Fix Fixed repeated entries in supported\_drm\_media\_formats from the ZeroConf device description.
- Fix Fixed example code in decoder\_mp3.c for decoding error detection to work with the latest minimp3 version.
- Fix Fixed an issue where 64-bit addresses are truncated on Windows 64-bit build.

### [Version 3.188.74](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.188)

- Fix Fixed error logging for WSAEWOULDBLOCK socket error on Windows builds.
- Fix Fixed progress calculation in case draining audio is required. Media delivery example missed information about the sample format in such cases.
- Fix Fixed media delivery example with regards to the playback of corrupted tracks.

### [Version 3.184.49](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.184)

- API-Change Improved performance of Media Delivery API. The StreamData callback is called up to 4 times per pump to deliver more data.
- Fix Fixed edge case where seeking would fail if seek action was triggered immediately after a track finished before the next track delivery started.
- Fix Fixed error logging for `WSAEWOULDBLOCKi` socket error on Windows builds.

### [Version 3.183.28](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/3.183)

- Fix Fixed an issue where eSDK would fail playback in case of quick subsequent pause/resume actions. The issue was caused by eSDK forgetting the current playing position if a pause is issued before the (re-)delivery of current track data started.
- Fix Fixed an error where eSDK incorrectly detected an invalid position when seek is requested on the playing track.
- Fix Avoid using IPv6 from DNS resolver if no valid IPv6 interface exists.

### Version 3.180.57

- Fix Fixed reporting of correct seek-to position in `SpCallbackPlaybackSeek`.
- Fix Changed volume update rate-limiting algorithm to have limited number of volume update requests in flight. Previously eSDK could drop volume updates which would cause different volume levels in the integration and Spotify backend.

### Version 3.179.27

- Fix Fixed progress calculation of media delivery example.
- Fix Updated MbedTls version (2.16.5 to 2.26.0) in build configurations with TLS support.

### Version 3.178.38

- Fix Fixed an issue where the playing track got interrupted as a result of calling `SpQueueUri()`.

### Version 3.176.20

- Fix Fixed an issue where playback would not work with re-delivery mode enabled.

### Version 3.171.19

- Fix Fixed inconsistent ZeroConf documentation about remoteName when integration uses device aliases.

### Version 3.170.37

- API-Change Added new API function (`SpNotifySeekComplete()`) for ending a seek operation. In addition, the parameter is\_final\_value is removed from the function `SpSetDownloadPosition()`. To adapt your code to this API change: after every call where `SpSetDownloadPosition()` was called with is\_final\_value==1, remove this argument and add a call to `SpNotifySeekComplete()` immediately after.
- Feature Added code to example\_delivery.c on how to provide CA certificates to eSDK via the API function `SpTLSAddCARootCerts()`.
- Fix Fixed crash in Linux pulseaudio example code.
- Fix Fixed the example code calculation of the duration of an MP3 file with constant bitrate given the file size and bitrate.

### Version 3.169.26

- Fix Fixed an issue where mp3 playback would get stuck at the end of the stream and not continuing on with the next track. The issue is fixed in the eSDK example code.

### Version 3.168.57

- Fix Fixed a problem where calling `SpNotifyStreamPlaybackStarted()` immediately after `SpNotifyStreamPlaybackFinishedNaturally()` would fail.

### Version 3.167.55

- Fix Fixed an issue where eSDK gets stuck when calling `SpPlayUri()` while an advertisement is playing. This issue was introduced in v3.162.
- Fix Removed mentions of compressed mode in the documentation.
- Fix Added error reporting to MP3 decoder in the example code.
- Feature Removed PCM delivery mode. All build configurations which were previously using PCM delivery mode are now changed to use Media Delivery.

### Version 3.166.69

Note: This is the last version of eSDK to support PCM mode. All future releases will be media-delivery only.

- Fix Fixed seeking video track over connect. The position was corrupted.
- Fix don't include port number in HTTP "Host" request header field when using standard port number for the protocol. Some HTTP servers were found to return status 404 (Not Found) when the Host header field contains a port number.
- Fix Fixed some bytes from old offset being delivered after call to `SpSetDownloadPosition()` if `SpSetDownloadPosition()` was not called within `SpCallbackStreamSeekToPosition` callback.
- Feature Changed audio decoder example code to use stream\_size\_bytes.
- API-Change Added audio quality field to `SpMetadata`. This field tells the currently playing track quality.
- API-Change Added stream byte size to `SpCallbackStreamStart on_start` function in Media Delivery API.

### Version 3.163.106

- Fix Fixed documentation for ZeroConf regarding device aliases and display name in getInfo reply.
- Feature Removed the following unused callbacks from example code `SpExampleAudioCallbacks`: `audio_get_buffered_ms,audio_get_written_frames, audio_reset_written_frames, audio_subtract_written_frames, audio_changed`.
- Feature Removed Compressed Mode audio delivery (WITH\_COMPRESS\_DATA\_API build option). All integrations using compressed mode should migrate to Media Delivery ("playapi\_media\_tls" build profile).
- Feature Added `OsConnectivityStatus()` to arch example code.
- API-Change Introduced a new API to allow starting playback with `SpPlayOptions`. This change simplifies "play uri" functionality by receiving the optional parameters in a single struct (rather than as individual params).
- API-Change Added support for shuffle\_context parameter in `SpPlayOptions`.
- API-Change Added support for referrer in `SpSourceInfo`.

### Version 3.162.101

- Fix Changed the behaviour of `SpPlayUri` to stop the music immediately when called. Where it previously continued playback of current track till Backend response was received.
- Fix Fixed a bug where switching bitrate mid-track would not start the playback from the position where the bitrate change happened. This affected Media Delivery builds.
- Feature Disabled automatic bitrate switching.

### Version 3.161.46

- Fix Fixed audio glitches with vorbis decoder example code. This was a regression in the example code shipped with eSDK versions &gt;=3.157.
- Fix Fixed reporting of position in Media Delivery example code. The last\_samples\_buffered was not reset correctly during flush which caused the track position to have too big value after skip or seek.
- Fix Fixed a typo in `SpLogSetLevel()` documentation.
- API-Change Added `kSpErrorPlaybackInitiationTimeout` to `SpError` enum. This is used to notify integration that `SpPlayUri()` timed out.

### Version 3.160.72

- Fix Fixed a small typo in the documentation for is\_group field in `SpZeroConfDeviceAlias` structure.

### Version 3.159.86

- API-Change Removed event `kSpPlaybackNotifyTrackDelivered` from the public API in Media Delivery builds. In the Media Delivery API, callback `SpCallbackStreamEnd on_end` is used instead to let the integration know that delivery of track data has finished.

### Version 3.158.86

- Fix Added an interface to check for audio decoder errors in the Media Delivery API example.
- Feature Set default log level to INFO in builds with verbose logging. Integration should use `SpLogSetLevel()` to set TRACE and DEBUG log levels.
- Feature Changed the example code `audio_decoder.h` `seek()` function definition to simplify the seeking logic in `media_delivery.c`.

### Version 3.157.78

- Fix Fixed minor errors in the device alias documentation (incorrect description of fields 'isGroup' and 'alias\_count').
- Fix Updated examples for the proprietary metadata page. Relevant for Media Delivery API builds.
- Feature simplified ogg vorbis decoder in the example code. Relevant for Media Delivery API builds.
- Feature Added more precise seeking to ogg decoder example code. When seeking, samples from ogg pages before the actual location will be skipped and not played. Relevant for Media Delivery API builds.
- Feature Changed example code `audio_decoder.h` `decode_and_output_to_audio_driver()` to not return anything. Use `finished()` to check if the decoder has finished decoding. Relevant for Media Delivery API builds.
- Feature Removed `written_frames()` from audio\_decoder.h API in the example code. Relevant for Media Delivery API builds.

### Version 3.156.25

- Fix Fixed an issue where eSDK starts playback on skip and seek actions when the device is not in controllable state. With this fix the integration receives an error code `kSpErrorDeviceUncontrollable`.
- Fix Added `SpContentType` field to `SpMetadata` to indicate the type of the content (e.g. music track, podcast show episode, advertisement) in TPAPI configurations.
- Fix Added a new error code `kSpErrorDeviceUncontrollable`. eSDK returns this error code when integration calls playback APIs when the device is not controllable.

### Version 3.155.22

- Fix Fixed track statistics reporting when seek was done while a track was playing but had been fully delivered using the Media Delivery API.

### Version 3.152.41

- Fix Observed position is now reset when receiving observe commands without seek to value. Without this fix the incorrect position will be set after track change.

### Version 3.151.52

- API-Change Introduced a new API to operate on device's controllable and active states. `SpPlaybackSetAvailableToPlay()` is marked as deprecated and the integration should use `SpPlaybackSetDeviceControllable()`, `SpPlaybackIsDeviceControllable()` and `SpPlaybackSetDeviceInactive()` instead.
- Fix Fixed an issue where the current playback continues to play when eSDK fails to send a play command to the backend when an integration calls `SpPlayUri()` API. With this fix, eSDK pauses the current playback if eSDK fails to send a play command to the backend.

### Version 3.150.82

- Fix Fixed use case diagram pictures for edge cases in Media Delivery API doxygen doc.
- Fix Fixed issue where media format restrictions wouldn't survive re-login.
- Fix verified that the format of a fallback file is supported before playing it.

### Version 3.149.74

- Fix restored missing mbedTLS object files in the static library.
- Fix Fixed case where integration restricted capabilities immediately after `SpInit()`. The original capabilities set in `SpInit()` were ignored when restoring all capabilities.
- Fix Fixed an issue where restricted capabilities would be registered with Track Playback if restriction happened between initializing the eSDK and registering.
- Fix Fixed an issue where the currently playing file was unnecessarily reloaded and resumed. This happened when it was the preferred file (for the currently playing track) both before and after format capabilities changed.
- API-Change renamed the field `supported_media_formats_bitmask` on struct `SpFormat` to `media`.
- API-Change renamed `SP_MAX_SUPPORTED_DRM_FORMATS to SP_MAX_SUPPORTED_FORMATS`.

### Version 3.148.40

- Fix Fixed an issue in Zeroconf urldecode where the '+' character is not decoded as a space.
- Feature Added `SpRestrictMediaFormat()` and `SpRestoreMediaFormat()` API functions to update the list of supported DRM and media formats during runtime.

### Version 3.147.79

- Fix Fixed c89 compatibility in mp3 decoder example code.
- Fix Changed the behaviour how eSDK becomes Active when `SpPlayUri()` is called. Previously eSDK would become Active immediately which could cause the old metadata being displayed for a short period of time. Now the Active status is not updated until the reply from the backend arrives and the metadata is updated.
- Fix Fixed an issue with multicast DNS server could fail after a network connectivity interruption.
- Fix Fixed an rarely occurring issue where the OGG decoder could fail during seek if a false sync sequence was hit in the input stream. A false sync sequence is some part of the compressed audio stream that happens to contain the start-of-page marker "OggS". The symptoms would include an eSDK log message with the message "OUT OF RAM!".
- Fix Fixed ogg decoder code example which would hang if seeking to or beyond the end of a track.
- Fix Fixed an issue where calls to `SpPlayUri()` might get lost between the pumps.

#### Migration to eSDK 3.147.79

- Fix Deprecation of separate voice APIs: From now on for Alexa actions the integrations should call `SpPlayUri` instead of `SpPerformVoiceAction`
- Fix Remove mentions of `spotify_embedded_voice_api.h`.
- Fix Remove `SpCallbackVoiceActionStatus` callback and calls to `SpRegisterVoiceCallbacks`.
- Fix Replace calls to `SpPerformVoiceAction` by `SpPlayUri`: `err = SpPlayUri(action, SP_NO_INDEX, 0, NULL, -1);`

### Version 3.146.79

- Fix corrected a bug which could have caused DDoS-like simultaneous calls to the backend from many different eSDK clients if integrations made certain API-calls (such as SetAvailableToPlay) at startup, and those integrations were restarted at the same time (as in a major upgrade).
- Fix Fixed an audio corruption in Media Delivery vorbis decoder example code.
- Fix Fixed potential memory out-of-bounds read in Media Delivery example code.
- Fix Fixed error where TrackChanged notification was played twice in succession in the same context.
- API-Change Added `kSpDrmFormatUnknown` to `SpDrmFormat`. This is used for `kSpMediaFormatSpotifyManifestId` media format.
- Fix Fixed playback for mono MP3 by interleaving mono samples to stereo in the Media Delivery API example.
- Fix Fixed an issue causing a crash when a platform implements asynchronous DNS lookup.
- Fix Added retry logic on socket read error while streaming from CDN for the streamer builds.

### Version 3.145.39

- Fix Fixed a bug causing eSDK to send constant traffic to the backend after approximately 49 days and 17 hours have elapsed since initialization or re-login.
- API-Change Extended metadata track window by adding `kSpMetadataTrackBeforePrevious` and `kSpMetadataTrackAfterNext` to `SpMetadataTrack` enum.
- API-Change Changed stream\_id type from "int" to "unsigned int" in Media Delivery API.

### Version 3.143.24

- API-Change Fixed an issue with HTTP redirects, increased the max number of HTTP redirects allowed to 10.
- Fix Added possibility to uniquely identify a track in the context by introducing track UIDs. The playback could be started using new API `SpPlayContextUri()` defined in `spotify_embedded.h` for PCM builds.

### Version 3.142.85

- API-Change Removed `on_audio_data` callback from `spotify_embedded.h` from non PCM build configurations.
- Fix Fixed an issue where playback stopped after network reconnection.
- Fix Removed mentions of `SpCallbackPlaybackAudioData()` from documentation of compress builds.

### Version 3.140.92

- Fix Fixed an issue where timing out when resolving apresolve.spotify.com could lead to infinite retry loops by correctly falling back to ap.spotify.com.
- Fix Fixed a bug that could cause the wrong next track to be played if playback order changed (i.e. toggling shuffle) under certain conditions.
- Fix Fixed an issue where `SpConnectionRequestAccessTokenForClientId()` would fail because of a long scope string provided.

### Version 3.139.109

- Fix Introduced a possibility to run an external webserver for ZeroConf with the built-in mDNS.

### Version 3.138.47

- Fix Added caching of HTTP redirect locations to reduce the overhead setting up HTTPS connections for each CDN download request.

### Version 3.137.39

- Fix Fixed an issue where eSDK could crash due to receiving a too long or malformed redirect URL.

### Version 3.136.71

- Fix Removed the context parameter from example audio drivers' audio\_data functions (as the parameter was never used).
- Fix Added comments to the audio functions in examples/common/include/audio.h
- Fix Fixed an issue where the current play time position in an observing client can be out of bounds.

### Version 3.134.19

- Fix Fixed an issue with `kSpPlaybackNotifyTrackDelivered` event raised for the prefetched track before the playing track had finished and `kSpPlaybackNotifyTrackChanged` was raised, which could happen when playing short tracks.
- Fix Fixed an issue where eSDK was not reporting the initial start position when the current track progressed to the next track with resume position.

### Version 3.133.35

- Feature Implemented an example application of the Media Delivery API with audio decoder abstraction.
- API-Change Added audio decoder abstraction seek support for the Media Delivery API example implementation.

### Version 3.132.71

- Feature When changing connectivity type, the active sockets are recreated. When an attempt is made to read from them, EOF (-1) will be returned.
- Fix Removed reentrancy check from `SpZeroConfGetVars()`.
- Fix Changed colors of sequence diagrams in the documentation.

### Version 3.131.65

- Fix Fixed the color of the tabs in the documentation page.

### Version 3.129.43

- Fix Updated outdated link to the Tremor repo in docs/LICENSE file.
- Fix Added missing documentation to `spotify_embedded_debug.h` and `spotify_embedded_internal.h`.

### Version 3.127.32

- API-Change Removed deprecated `SpGetLoginUsername()` API.
- Fix Updated the documentation about TLS certificate buffer in `SpTLSAddCARootCert()`.

### Version 3.126.17

- Fix Fixed calculation of `buffered_ms` for example pulseaudio driver.

### Version 3.125.62

- Fix Fixed documentation for `SpSetDeviceIsGroup()` regarding device aliases: when using device aliases, SpSetDeviceAliases should be used instead.
- Fix Fixed an issue where Zeroconf login would fail due to the way the request was split into TCP segments on the network connection.
- Fix Fixed documentation in `SpConfig::display_name` and `SpConfig::device_aliases` to reflect the fact that `SpConfig::device_aliases` and `SpConfig::display_name` are mutually exclusive.
- Fix Documented the expected array size in `SpSetDeviceAliases()` argument.
- Fix Fixed an issue where sometimes seek immediately after starting track does not produce any audio.
- Fix Fixed an issue where mbedTLS would not link on Windows plarforms because of usage of forbidden API `lstrlenW`.
- Fix Fixed an issue in the default MbedTLS entropy functions on Windows platforms. The API used by MbedTLS (CryptGenRandom) is forbidden in Windows Store Apps.

### Version 3.124.52

- Fix Added missing multithreading check to `SpZeroConfGetVars()` to prevent the API function being called from a different thread than where eSDK was initialized.
- Fix Fixed `CallbackNewCredentials()` function signature in example code in eSDK documentation.

### Version 3.123.57

- Fix Removed undefined `SP_MAX_DEVICE_ALIASES_OVERRIDE` from builds with 32 device aliases.
- Fix Fixed an issue where sometimes `ms_played` in the end-song is less than the actual playing time when network connection toggles while playing track.
- Fix Fixed an issue where the metadata is changed but not the playing track when changing presets.

### Version 3.122.67

- API-Change Introduced macro `SP_LOG_REGISTER_TRACE_OBJ` to decorate the registration of a trace object.
- Feature Added API function `SpLogGetLevels` to get current logging levels from eSDK.
- Fix Fixed an issue where socket communications fail in builds with custom socket HAL. The issue was caused by the "tls" field in struct `SpSocketHandle` not being initialized properly (introduced in eSDK release 3.117).
- Fix Fixed an issue where the process stack was mapped as executable (PROT\_EXEC) on Linux platforms.
- Fix Fixed a bug where eSDK in bad network conditions would run out of network resources and become unresponsive until restart.

### Version 3.121.19

- Fix Fixed an issue where socket communications fail in builds with custom socket HAL. The issue was caused by the "tls" field in struct `SpSocketHandle` was not initialized properly (introduced in eSDK release 3.117).

### Version 3.120.58

- Fix Fixed an issue where there was sometimes no sound for the externally hosted tracks.
- Fix Fixed a regression in eSDK &gt;=3.114 where mDNS announcements and replies were not sent on all network interfaces.

### Version 3.119.105

- Feature Introduced new APIs for controlling logging via eSDK in `spoitfy_embedded_logh.h`.
- Fix Unified logging function for all examples.
- Fix Fixed a bug with high latency on externally hosted podcasts in low bandwidth conditions.

### Version 3.118.55

- Fix Fixed an issue where user login failed because of long brand and model names.
- Feature Shut down TLS connections gracefully.
- Fix Fixed a crash caused by a stack corruption during TLS connection establishment on platforms with HTTPS support.
- Fix Fixed an issue where an externally hosted podcast fails without falling back to ingested when playback error happens before transitioning from upcoming to playing.
- Fix Fixed an issue where CDN times out with HTTP redirects.

### Version 3.117.71

- Feature Deprecated ZeroConf fields `accountReq`, `activeUser` & `voiceSupport`; added uniqueness requirement for `deviceId`.
- Fix Allocated enough korn memory for aliases in zeroconf.
- Fix Changed the error code returned when calling `SpRegisterSocketHALCallbacks()` or `SpRegisterTLSCallbacks()` after `SpInit()`. The returned error code (`kSpErrorAlreadyInitialized`) will now signal this particular reason much more clearly than the previous value (`kSpErrorFailed`).

### Version 3.116.55

- Fix Fixed an issue where device gets stuck at an ad when device goes to unavailable and inactive state and then goes to available to play state.
- Feature Introduced a support of redirects in the http client.
- Fix Updated the documentation to clarify that `SpPresetSubscribe` should always be used with `SpPlayPreset`.

### Version 3.114.42

- Feature Introduced new device aliases. Backwards incompatible changes in API.
- Fix Fixed an issue where seeking back at the end of the track would play the next track instead

#### Migration of 3.114.42

- In the new device alias implementation the selection of the alias is moved from the device login to the playback initiation. Because of this change parameters related to device alias selection are moved from login related functions to the functions responsible for starting playback of a context.
- Functions that lost alias index (alias id or index should be removed from the call):
  
  - `SpCallbackConnectionNewCredentials`
  - `SpConnectionLoginBlob`
  - `SpConnectionLoginUnscrambledBlob`
  - `SpZeroConfGetVars`
  - `SpConnectionLoginZeroConf`
- Functions that got alias index:
  
  - `SpPlaybackPlay`
  - `SpPlayUriAtByteOffset`
  - `SpPlayUri`
  - `SpPlaybackBecomeActiveDevice`
  - `SpPlayPreset`
  - `SpPlayPresetEx`
- From now on the integration has to either use old style display name or device aliases. These two approaches can not be combined. If the integration does not use aliases then use:
  
  - `display_name` in in `SpConfig` structure
  - `SpSetDisplayName()`
  - `SpSetDeviceIsGroup()`
  - `SP_NO_ALIAS_SELECTED` as an alias index

With the device aliases use: _ `device_aliases` in `SpConfig` structure _ `SpGetSelectedDeviceAlias()` * `SpSetDeviceAliases()`