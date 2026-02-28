---
title: FAQs | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/faqs#general
source: crawler
fetched_at: 2026-02-27T23:41:46.482253-03:00
rendered_js: true
word_count: 2688
summary: This document provides a comprehensive FAQ for hardware partners integrating the Spotify Embedded SDK, covering build access, audio buffering, sample formats, and voice assistant requirements.
tags:
    - embedded-sdk
    - hardware-integration
    - spotify-connect
    - audio-buffering
    - esdk-builds
    - voice-solutions
    - amazon-alexa
category: reference
---

## General

### Where can I download the eSDK builds?

eSDK builds can be found under the *builds* section in [Certomato](https://certomato.spotify.com/builds).

Certomato builds have replaced our previous eSDK builds distribution service Box.

### I don't have access to Certomato. What can I do?

If you don't have access to Certomato, please create a access request ticket in the Spotify helpdesk (you can find the link to the Helpdesk tool in the onboarding email).

### How do I get Spotify Free enabled on my product?

Spotify Free is only available for eSDK builds 3 and above, please make sure you have the correct build. If you don't have the right version, you need to update to the latest eSDK version. If you are updating between major eSDK versions (v2.xx to v3.xx) you must go through certification again.

### Can we use the Web API?

No, hardware partners must only use the embedded SDK.

### Can we create voice solutions?

No, you are not allowed to build a proprietary voice solution. However, If you are interested in a voice integration with Spotify, we support Amazon Alexa or Google Assistant.

### Can we build a search experience in our application?

No, we believe that the best experience lives within the native Spotify app.

### How much audio data does the eSDK buffer?

By default, the Embedded SDK buffers up to 256 KB of compressed audio data internally.

Added in version 1.5: When you call [SpInit()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spinit) with a [SpConfig::memory\_block\_size](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) of more than [SP\_RECOMMENDED\_MEMORY\_BLOCK\_SIZE](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#macros) bytes, the additional memory will be allocated for this buffer, up to 5 MB.

This buffer makes it possible for the speaker to continue playing audio during network outages, as long as enough data has been buffered before the outage occurs.

**Table: Approximate number of seconds in the buffer for various buffer sizes and bit rates.**

### How much audio data should the application buffer?

It is up to the application whether or not to buffer uncompressed audio data sent to the callback SpCallbackPlaybackAudioData. In general, it is more efficient memory-wise to have the Embedded SDK buffer compressed audio data (see the question “How much audio data does the Embedded SDK buffer”) than to buffer uncompressed data inside the application.

If you do buffer, make sure to return the correct number of buffered samples in the `samples_buffered` parameter to the callback SpCallbackPlaybackAudioData.

### Are there tracks that have an SpSampleFormat different from 44kHz Stereo?

Most tracks are 44kHz Stereo (SpSampleFormat::channels = 2 and SpSampleFormat::sample\_rate = 44100 in the callback SpCallbackPlaybackAudioData).

Your code should also be prepared for Mono tracks (SpSampleFormat::channels = 1):

- Example Mono track:
  
  - Track: ‘Bobcat Goldthwait – How They Met – In Utero Interview’ ([spotify:track:1FqY3uJypma5wkYw66QOUi](http://open.spotify.com/track/1FqY3uJypma5wkYw66QOUi))
  - Album: ‘Spotify Landmark: Nirvana’s In Utero’ ([spotify:album:62Eg7rm61rMiZWjjZ98UER](http://open.spotify.com/album/62Eg7rm61rMiZWjjZ98UER))

48kHz tracks (SpSampleFormat::sample\_rate = 48000) are very rare and we do not currently add new 48kHz tracks to our library:

- Example 48kHz track:
  
  - Track: ‘Holberg Suite Op.40 Praeludium’ ([spotify:track:2pD4Qq6v9Vi3AWnbFHnSbs](http://open.spotify.com/track/2pD4Qq6v9Vi3AWnbFHnSbs))
  - Album: ‘Classical Overtures’ ([spotify:album:2DLVSZfj6ZeMJGoLNAhFjn](http://open.spotify.com/album/2DLVSZfj6ZeMJGoLNAhFjn))

Here is a playlist that alternates between tracks of different formats: [HWP-PL-MIXED-FORMATS](http://open.spotify.com/user/spotifyhwp/playlist/2EIxgGw3wGsr2UrVjmGRKV)

### What should the application do if it cannot handle the provided SpSampleFormat?

In case the callback SpCallbackPlaybackAudioData receives an SpSampleFormat that your application cannot handle, simply return 0 from the callback and invoke SpPlaybackPause() the next time [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents) returns.

### Do you have special playlists for testing different aspects of the implementation?

We have added a user account with a number of playlists that you can use for testing. Go to the user [spotifyhwp](http://open.spotify.com/user/spotifyhwp)'s profile page (or paste `spotify:user:spotifyhwp` in the search box in the Spotify application) and take a look at the user’s public playlists. The playlists contain descriptions (currently, only the Spotify desktop application displays these descriptions when you open the individual playlist pages).

### If the speaker has additional input sources (such as “AUX”, “Internet Radio”), what APIs should be called when Spotify is no longer the active input source?

When the user switches the input source away from Spotify while the speaker is the active device ([SpPlaybackIsActiveDevice()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackisactivedevice) returns true) and is playing audio, the application should pause the audio by calling SpPlaybackPause(). This will cause the mobile app to display the audio as paused, but the speaker will remain the active device.

If the speaker is not the active device ([SpPlaybackIsActiveDevice()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackisactivedevice) returns false) when the user switches the input source, the application does not have to do anything.

### What should happen when the user makes Spotify the active input source?

The application does not have to call any Embedded SDK APIs when switching from a different input source (such as “AUX” or “Internet Radio”) to Spotify.

It is up to the application whether switching the input source to Spotify should automatically pull playback to the speaker. If this should happen, the application should call [SpPlaybackPlay()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackplay), which will take playback away from another Connect-enabled device (such as the Spotify mobile client) and start playback on the speaker.

### What should happen when Spotify is not the active input source and the user moves playback to the speaker from the Spotify mobile app?

When the speaker is playing from a different audio source (such as “AUX” or “Internet Radio”) and the user moves playback to the speaker, the input source should be switched to Spotify and playback should start.

The application receives the notification kSpPlaybackPlay and starts receiving audio data via the callback SpCallbackPlaybackAudioData. If the speaker was not the active device previously (according to SpPlaybackIsDeviceActive()), the application also receives the notification kSpPlaybackNotifyBecameActive.

## Amazon Alexa

### Do I need a special eSDK build for SP-AVS?

As long as you already have a playapi build of eSDK3, you should be good to go. If you are implementing MRM you will need a separate eSDK build. You can request that here, by putting \[MRM build] in the summary of the ticket. The MRM build should not be used for the single room use case.

### Do I need two different eSDK builds for Spotify Connect and MRM?

Yes, the Alexa MRM eSDK is a specific build distributed to you with a special config of your current build. This means that you first need a regular Spotify Connect build. Please request an eSDK build if you haven't already. You do so from the same service desk you created this ticket.

The MRM build should not be used for the single room use case.

- You need to work with Amazon to get Spotify enabled for your platform. You need to send them proof that you have passed Spotify Connect certification in order for them to enable Spotify. You can find more information regarding the Amazon Alexa process on their developer site.
- When you have implemented AVS, including Spotify, you need to go through Voice Certification.
  
  - Download the AVS self-certification checklist (please contact us if you don't have the checklist file).
  - Make sure that your integration passes all applicable tests.
  - Submit for Voice certification by filing a Spotify Helpdesk ticket.

## Standby Power Off

### What APIs should be called when the speaker goes in standby mode or is powered off?

If the speaker was active (SpPlaybackIsActiveDevice() returns true) and was playing audio, the application must call SpPlaybackPause(). This will cause the mobile app to display the audio as paused, but the speaker will remain the active device.

If the speaker continues to react to commands coming from the Spotify mobile app (for example, if the user can “wake up” the speaker by resuming playback on the speaker via the app), the application does not have to do anything else. In this case, the application must continue to call [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents), react to all notifications and callbacks, and handle requests coming in through the Spotify Connect ZeroConf API.

If the speaker can no longer be controlled from the Spotify mobile app, the application should log out from the Embedded SDK and stop announcing itself via the Spotify Connect ZeroConf API:

1. Call [SpConnectionLogout()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionlogout)
2. Wait for [kSpConnectionLoggedOut](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionnotification)
3. (Optional: Destroy the Embedded SDK instance via SpFree() )
4. Stop announcing the `spotify-connect._tcp` service via Bonjour/mDNS
5. Stop processing the ZeroConf HTTP requests (getInfo, addUser, etc.)

If the application fails to do this, the speaker would still appear in the Connect device picker in the mobile app, even though the speaker would no longer react to commands.

### What APIs should be called when the speaker wakes up from standby mode or is powered on?

If the Embedded SDK was fully up and running while the speaker was in standby mode, the application does not have to do anything else. (In this case, the application called [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents), reacted to all notifications and callbacks, and handled requests coming in through the Spotify Connect ZeroConf API while the speaker was in standby mode.)

If the Embedded SDK was shut down during standby/power-off mode, the application must re-initialize the Embedded SDK using SpInit(), log the user back in (using [SpConnectionLoginBlob()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginblob) and start announcing itself again via the Spotify Connect ZeroConf API.

The application should not start playback automatically by calling [SpPlaybackPlay()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybackplay).

## Zeroconf

### How does the application log in a user that was previously added through the “addUser” request after the speaker reboots?

This is the sequence of events when a user logs in through the ZeroConf addUser request:

1. ZeroConf `addUser` request receives `userName`, `blob`, and `clientKey` from the mobile app (**Note:** Do **NOT** save the `blob` and the `clientKey` to persistent storage!)
2. Your code invokes `SpConnectionLoginZeroConf(userName, blob, clientKey)`. **Note:** After this, you should throw away `blob` and `clientKey`. You will not need them anymore. But keep `userName`.
3. Your code waits for the notification `kSpConnectionNotifyLoggedIn`.
4. Your code waits for the callback `SpCallbackConnectionNewCredentials(credentials_blob, context)`.

ONLY if you received both 3. and 4. and no SpCallbackError occurred:

1. Save `userName` (from the addUser request) and the `credentials_blob` (from SpCallbackConnectionNewCredentials) to persistent storage.
2. Reply with a success status of 101 to the addUser request.
3. You are now logged in.

To log in the user after the speaker has rebooted:

1. Read the stored userName and credentials\_blob from persistent storage.
2. Perform a login with `SpCallbackConnectionLoginBlob(userName, credentials_blob)`.
3. Wait for the success as you did before. Again you will receive SpCallbackConnectionNewCredentials(credentials\_blob, context). You should replace credentials\_blob in persistent storage if its value changed for the next reboot. **Note:** Make sure that the [SpConfig::unique\_id](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) stays the same across reboots. If the value changes, the previously stored credentials\_blob is invalid. [SpConnectionLoginBlob()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginblob) will return an error and you will get the debug message “Parsing ZeroConf blob failed with code -3”.

### Are the values returned by the SpZeroConfGetVars() API properly escaped to be placed into a JSON reply?

No, the application needs to properly escape all special characters in the strings that are returned by the [SpZeroConfGetVars()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spzeroconfgetvars) API before they are written to the JSON reply. See [http://www.json.org/](http://www.json.org/) for information about strings in JSON.

### How does the mobile app try to connect to a speaker using the Spotify Connect ZeroConf API?

The mobile app first discovers the speaker using Bonjour/mDNS to retrieve the IP address and port number as well as the path to the ZeroConf API on the speaker’s HTTP server. (The path is specified in the CPath field of the TXT record.)

The mobile device then sends an HTTP request to the following URL:

`http://<ip-address>:<port>/<path>?action=getInfo`

For example:

`http://192.168.1.100:8080/spotifyConnect?action=getInfo`

The speaker shows up in the Connect device picker in the mobile app if it receives a valid reply from the getInfo request.

If the speaker announces several IP addresses (e.g., one IPv4 and one IPv6 address), the mobile app will try to connect to both and use the one that works first.

If the same user is already logged in both to the speaker and to the mobile app, the speaker will show up even if an error occurs in the ZeroConf discovery.

### What are common reasons for the speaker not showing up in the mobile app?

- The speaker might not announce itself correctly over Bonjour/mDNS.
  
  - Make sure that the SRV record contains a TXT record with a CPath field. Note that the field name CPath is case-sensitive.
  - Use a third-party mDNS browser or a third-party tool to capture the network traffic to verify that the announcement works as expected.
- The HTTP server might not be able to accept requests using the announced IP address.
  
  - Does the HTTP server bind to the public network interface whose IP address is announced?
  - Can you manually perform an HTTP request to `http://<ip-address>:<port>/<path>?action=getInfo`?
  - Is there any firewall preventing you from making the connection?
- The response to the “getInfo” request might be invalid.
  
  - Does the request return a valid JSON response? Do the strings contain special characters and are they properly escaped?
  - Is the “version” field of the “getInfo” response set to the correct version of the Spotify Connect ZeroConf API (not of the eSDK version that you are using)?
  - Does the response contain all required fields and no fields that are undefined in the API?
- The application might not implement the Spotify Connect ZeroConf API correctly.
  
  - Check the Spotify Connect ZeroConf API documentation (part of the API Reference Manual) and make sure that the application handles all requests according to the specification.
  - Does the application handle all documented actions?
  - Does the application send all required fields in the JSON responses?
  - Does the application handle missing optional fields in the JSON requests?
  - Does the application handle special characters in JSON by escaping them correctly?

### Why does SpConnectionLoginZeroConf() fail and I see the debug message “Parsing ZeroConf blob failed with code -3” (or similar)?

**Note:** In order to see debug messages, you need to register the callback [SpCallbackDebugMessage](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spcallbackdebugmessage).

This can occur if the application provides the wrong values in the response to the “getInfo” request. Make sure to populate all fields of the response with the values you get when calling the function [SpZeroConfGetVars](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spzeroconfgetvars). (Call SpZeroConfGetVars() for every getInfo request. Do not cache the result.) Also make sure to properly JSON-escape special characters in the strings when sending the getInfo response.

This error might also happen if you try to re-login a user after a reboot of the device using [SpConnectionLoginZeroConf](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginzeroconf). You must use [SpConnectionLoginBlob()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginblob) after a reboot. See also the question about re-login after a reboot.

## Media Delivery API

### Having issues with the integration?

You can send us a support ticket with attached logs or reach out to your System integrator directly. An integration can enable more verbose logs by using API call [SpLogSetLevel](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#splogsetlevel) on the latest eSDK version: SpLogSetLevel(NULL, SP\_LOG\_LEVEL\_TRACE);

### What information do I need to send Spotify to enable new formats on my device?

Send us your Spotify premium username with the correct email address. We can also enable premium Family accounts.

### Does Media delivery API require new certification on all products?

Yes, you are required to file a certification request for your media delivery API implementation, completing a Certomato test run (See Audio Format section in Certomato), and making sure that all your devices meet our requirements. Spotify will only test one model per platform.

### Do you require us to re-certify all our existing Spotify Connect products?

Spotify will only certify one device per platform. This means if your brand has two different platforms we would then want to test two devices, one on each platform. If yo uare unsure about what we classify as a platform, please reach through your system integrator. Otherwise please reach out to us with details about your platforms.

### Using a system integrator?

If you are a brand that uses a system integrator, please send support and process questions directly to your system integrator and they will guide you through the process.

### Should we send you new units for testing?

Please reach out through your system integrator, and they will help you answer this question. Otherwise please reach out and we will will let you know if you need to provide new devices or if we already have them handy.

### Call SpPlaybackIncreaseUnderrunCount():

Make sure that the following function is being invoked in your implementation (as it is now a requirement): SpPlaybackIncreaseUnderrunCount()

If playback under runs have been detected in the current track, use this API to report it to eSDK. This should only be called when there was no data to play at all and there was an audible glitch or gap for the user. It should only be called if audio was expected to be played and there was audio before. Please see the eSDK documentation for more details.