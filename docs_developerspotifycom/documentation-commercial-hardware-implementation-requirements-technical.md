---
title: Technical Requirements | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical
source: crawler
fetched_at: 2026-02-27T23:41:19.54835-03:00
rendered_js: true
word_count: 5409
summary: This document outlines the hardware, licensing, and certification requirements for partners integrating the Spotify Embedded SDK into commercial hardware products. It details memory specifications, device identification protocols, and the mandatory certification process for different partner types.
tags:
    - spotify-embedded-sdk
    - hardware-requirements
    - device-certification
    - partner-integration
    - licensing-agreements
    - iot-development
category: guide
---

Here we describe the technical requirements we have on partner products that use the Spotify Embedded SDK.

If you have questions about these requirements, please contact us in our Audio Device Integrations Helpdesk. You can find the link to the Helpdesk portal in the onboarding email.

## Key to Partner Types Used in These Requirements

In this document we distinguish between the following partner types. Requirements may vary according to your partner type.

- **Device Maker (DM)**: a partner who accesses Spotify services directly through the Spotify Embedded SDK binary.
- **Systems Integrator (SI)**: a partner who integrates the Spotify Embedded SDK binary into their own SDK. The binary is hidden from users of the SDK of the Systems Integrator; Spotify services can be accessed only through the SDK of the Systems Integrator.
- **Device Maker using a Systems Integrator SDK (SI DM)**: a partner who accesses Spotify services through an SDK of the Systems Integrator.

## Device Requirements and Dependencies

### RAM

The runtime memory consumption of the eSDK binary is fully configurable – just allocate a memory block and pass it to the SDK during initialization. For performance reasons, we recommend a minimum RAM size of 1.4MB. TLS functionality must be integrated in the eSDK, approximately 412 kB will be allocated on the heap.

### ROM

The read-only memory footprint of the Spotify Embedded SDK binary is approximately 378 kB if the integration provides audio decoders and TLS functionality, and 901 kB if the eSDK implements TLS and Vorbis decoding. This footprint does not include any TLS certificates (see TLS/HTTPS support below).

The binary requires access to a persistent storage area of 4kB.

**eSDK code & data size for Linux ARM v7 Hard Float platform, as of version 3.130**

Integrated TLS?Integrated Vorbis decoder?Size \[kB]NoNo378NoYes448YesNo832YesYes901

### UDP/TCP sockets and Hostname Look-Up

Each target device needs to provide the Spotify Embedded SDK binary with access to UDP/TCP sockets and hostname look-up.

### Chipset and OS

The Embedded SDK is buildable for several common chipset and OS combinations. You will need to provide us the toolchain to compile the binary to a particular chipset and operating system (a “build request”).

### ZeroConf stack: mDNS and HTTP server

The target device must run a Spotify Connect ZeroConf stack. This can be done either by enabling the built-in ZeroConf stack in the Embedded SDK, or by implementing the ZeroConf API. The ZeroConf API specification is provided as part of the Embedded SDK package. The API requires an HTTP server and an mDNS/DNS-SD server to be implemented on the target device (compliant with RFCs 6762 and 6763).

## Licensing and Certification Requirements

To be able to use the Spotify Embedded SDK and any of its components in a commercial product you must sign a license and distribution agreement with Spotify. This is a part of the regular process and you will get this agreement sent to you.

Spotify must certify all commercial products before we allow a release to market. During our certification process, as well as testing Spotify-specific functionality and performance, we also ensure that commercial products meet usability and general performance requirements.

### Product Range and Model Certification

Certification covers a **single product range** – defined as *a set of products using the same hardware/software configuration and presenting the same or substantially similar user interfaces and controls*.

A single product range can consist of several **product models**. Each product model must have a unique brand and model identifier, as well as a unique Product ID.

All product models within a product range are covered by that product range’s certification. If you wish to use Embedded SDK components in *another* product range, that product range will require separate certification.

### Third-Party Licenses

Several free and open-source software products have helped Spotify get to where it is today. We need you to link to those license agreements if you use any part of the Spotify Embedded SDK in your products. Therefore, please make sure that your device manuals (both in physical and digital form) include the following text:

## Device Authentication Requirements

### Spotify Client ID

To make use of Spotify Embedded SDK binary in your devices, you must have a Client ID.

The Client ID needs to be stored securely in each device. It is used to authenticate calls to the SDK binary. Both Systems Integrators, Device Makers using a Systems Integrator and Device Makers must use their own Client IDs.

## Device Identification Requirements

### Product ID

The **Product ID** is a 32-bit unsigned number that you must assign uniquely to each model in the range that implements the Spotify Embedded SDK binary. It needs to be stored in the device and passed to the binary as it is initialized (see the *Embedded SDK API reference*, [SpConfig::product\_id](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig).

### Partner Brand and Model Identification

A **brand and model identifier** needs to be registered with us as a part of the submission for certification for every unique device model in the range that implements the Spotify Embedded SDK binary.

Brand and model identifiers will need to be stored in the device and passed to the binary as it is initialized (see the *Embedded SDK API reference*, [SpConfig::brand\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) and [SpConfig::model\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig)). During the certification process, the identifier must be communicated to Spotify in the form:

*brand;model*

For example:

`ICE;X56`

If exactly the same software is running on different models within the range, a common model number can be used. For example; if the same software is running on device models X51, X52 and X54 the model name for all three devices can be `X5x`.

### Device Type Identification

The **device type** needs to be passed to the binary as it is initialized. There are three different device types to choose from:

- Speaker: `kSpDeviceTypeSpeaker`
- AVR: `kSpDeviceTypeAVR`
- Audio Dongle: `kSpDeviceTypeAudioDongle`

Spotify will use the information on device type to decorate the in-app user experience with icons and information on a particular device.

- **Systems Integrator (SI)** : The SI needs to provide a means to enable the DM Partners to set the partner brand and model identifier and device type.
- **Device Maker using a SI platform (SI DM)** : The SI DM Partner needs to add the partner brand and model identifier as well as the device type to each product.
- **Device Maker (DM)** : The DM needs to implement the partner brand and model identifier as well as the device type in each product.

### Device Attributes

When initializing the eSDK, device attributes can be passed to the binary. These attributes are currently available:

- Speaker has voice support: `SP_GLOBAL_ATTRIBUTE_VOICE`

Spotify will use the information to decorate the in-app user experience.

- **Systems Integrator (SI)** : The SI needs to provide a means to enable the DM Partners to set the correct device attributes.
- **Device Maker using a SI platform (SI DM)** : The SI DM Partner needs to set the device attributes correctly for each product.
- **Device Maker (DM)** : The DM needs to set the device attributes correctly for each product.

## Playback Restrictions Requirements

The eSDK plays tracks according to a state machine defined in the Spotify backend. This machine follows the current license applicable for the combination of user account, device, and possibly other factors. At any time, restrictions regarding the ability to move between and inside tracks may be applied.

The restrictions can be retrieved through [SpGetMetadata()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spgetmetadata). The metadata retrieved (`struct SpMetadata`) contains the restrictions in the `playback_restrictions` field (`struct SpPlaybackRestrictions`).

This struct has a number of bit fields that define which operations are restricted (for instance `disallow_seeking_reasons`), with bits set to explain why (for instance `SP_PLAYBACK_RESTRICTION_LICENSE_DISALLOW`).

Restrictions can be applied to the following operations:

- Pausing
- Resuming
- Shuffle
- Repeat
- Seeking inside track
- Peeking on previous track
- Peeking on next track
- Skipping to previous track
- Skipping to next track

Restrictions will not be applied to other playback attributes like volume.

Any user interfaces that include visible feedback to the user on the device must either

- only support play/pause
- implement support for Restrictions using the APIs described (only applicable if you have gotten a written confirmation from Spotify that you are allowed to do this)

<!--THE END-->

- **Systems Integrator (SI)**: The SI needs to implement Restrictions handling correctly.
- **Device Maker using a SI platform (SI DM)**: Not Applicable.
- **Device Maker (DM)**: The DM needs to implement Restrictions handling correctly.

## Spotify Discovery Protocol Requirements

### Spotify Connect ZeroConf API

The Spotify Connect ZeroConf API handles Spotify device discovery and credential management. Documentation for this API can be found within the Embedded SDK download package.

The ZeroConf discovery mechanism must always be active whenever the target device is running. This can be achieved by either enabling the built-in Embedded SDK ZeroConf or by implementing ZeroConf according to the ZeroConf API. In the case of implementing the ZeroConf API:

- **Systems Integrator (SI)** : The SI needs to implement the Spotify Connect ZeroConf API and mDNS/DNS-SD. The implementation of the Spotify Connect ZeroConf API must be hidden from the SI DM partner.
- **Device Maker using a SI platform (SI DM)** : No implementation or configuration shall be required by the SI DM partner.
- **Device Maker (DM)** : The DM needs to implement the Spotify Connect ZeroConf API and mDNS/DNS-SD.

### Credential Management

End user interaction with the Spotify credential management will be handled exclusively by the Spotify iOS, Android or desktop apps. The official Spotify apps communicate with the integrated Spotify Embedded SDK binary through the Spotify Connect ZeroConf API. There must be no other way for the user to pass Spotify credentials to the device.

The last logged in user must be logged in automatically when the device starts up. Therefore the partner integration needs to ensure the credential blob and the user name of the currently logged in user is stored, and is possible to re-submit, at start up.

- **Systems Integrator (SI)**: The SI needs to implement the credentials blob management.
- **Device Maker using a SI platform (SI DM)**: Not applicable.
- **Device Maker (DM)**: The DM needs to implement the credentials blob management.

## Device Source Selection and Sleep Requirements

### Device source selection

The Spotify Embedded SDK binary must run as soon as a device is powered on. Spotify requires a “last user action” source policy. This means that, if a user is logged into a device and the user selects the device for playback, the Spotify source must be chosen automatically and the device must be ready to play as soon as audio is delivered from Spotify.

If a device has means to switch source, it must be possible to reach the Spotify service through a device source switching mechanism at all times. For example, if a user is listening to the source “Internet radio” on a device, it must be possible for the user to navigate to and select the source “Spotify” through the device navigation system.

If Spotify is the selected source, any device source state information must clearly indicate at all times that Spotify is the source. If an LED on the device indicates the selected source, this LED light must be green whenever Spotify is selected. If the device has multiple sources available and they are grouped under the same LED light as Spotify it is OK to use the same color LED for all the sources in that category.

The Spotify Embedded SDK allows the retrieval of information about the track a logged in user is currently playing even though the user is playing it on another device. Optionally, you can show the currently playing track on another device that has Spotify as the selected source.

- **Systems Integrator (SI)**: The SI needs to ensure “last user action” source selection policy. The SI DM partner shall not be able to change the source selection scheme. If Spotify is selected, all device source information needs to clearly indicate that Spotify is the active source.
- **Device Maker using a SI platform (SI DM)**: If Spotify is selected, all device source information needs to clearly indicate that Spotify is the active source.
- **Device Maker (DM)**: The DM needs to ensure a “last user action” source selection policy. If Spotify is selected, all device source information needs to clearly indicate that Spotify is the active source.

### Device power save mode

The Spotify Embedded SDK binary must run in the default power save mode. This means the Spotify client and the Spotify discovery mechanism (Spotify Connect ZeroConf API) must be running even when the device goes into the “out of the box” default sleep mode.

- **Systems Integrator (SI)**: The SI needs to ensure the Spotify client and the Spotify Connect ZeroConf API implementation is running in the default power save mode. The SI DM partner must not be able to change this behavior.
- **Device Maker using a SI platform (SI DM)**: Not applicable.
- **Device Maker (DM)**: The DM needs to ensure the Spotify client and the Spotify Connect ZeroConf API implementation is running in the default power save mode.

## Physical Device Controls and Screen Output

### On device controls and device remote control

All physical buttons on a device, or its remote control, corresponding to the [Spotify Playback Control commands](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#embedded-sdk-control-and-status-functionality) must be implemented and functional whenever Spotify is the actively playing device. If Spotify is the selected source but not the actively playing device no Spotify control commands must be propagated to Spotify (with the exception of the play button or a standby button, see below).

The [Pull Context](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#embedded-sdk-control-and-status-functionality) functionality must be implemented on all play buttons. The Pull Context via a play button must work at all times when Spotify is the selected source. If your product have a requirement to start playing the last played source as a user switches the device on via a standby button this may also be used to Pull Context. A dedicated Spotify button may also be assigned the Pull Context functionality provided that it also switches the source to Spotify when Spotify is not the selected source.

- **Systems Integrator (SI)**: The SI needs to ensure that all Spotify Playback Control commands and the Pull Context functionality are available to the DM partner.
- **Device Maker using a SI platform (SI DM)**: The SI DM must implement the Spotify Playback Control commands and the Pull Context on all corresponding physical buttons according to the Spotify requirements.
- **Device Maker (DM)**: Must implement the Spotify Playback Control commands and the Pull Context on all corresponding physical buttons according to the Spotify requirements.

### On device screens

When Spotify is the selected source, “Spotify” must be spelled out on all device screens. No abbreviations for “Spotify” may be used, but scrolling of the text is allowed.

The metadata and status information available through the Spotify Embedded SDK binary shall be displayed whenever the display size allows. All platforms that display track name, artist and album name are required to handle strings containing any valid UTF-8 character and to accurately render all characters in the ISO/IEC 8859-1:1998 “Latin 1” character set. All devices are additionally required to render local language scripts for any market where the product will be sold. Characters that the partner cannot render accurately shall be rendered as a question mark or an empty box.

All graphical resources in your product associated with Spotify must comply with the requirements stated in the [Device Display Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/speaker-display)

- **Systems Integrator (SI)**: The SI needs to ensure all metadata and status information are available to the DM partner. The UTF 8 character set must be supported as specified above.
- **Device Maker using a SI platform (SI DM)**: The [Device Display Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/speaker-display) must be implemented.
- **Device Maker (DM)**: The [Device Display Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/speaker-display) must be implemented. The UTF 8 character set must be supported as specified above.

### Partner Device Companion Application and TV Out

A partner companion application for mobile phones or tablets, as well as a TV out interface, must map all play commands to the [Spotify Playback Control commands](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#embedded-sdk-control-and-status-functionality) whenever Spotify is the actively playing device. If Spotify is the selected source but not the actively playing device no Spotify control commands must be propagated to Spotify (with the exception of the play button, see below).

The [Pull Context functionality](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#embedded-sdk-control-and-status-functionality) must be implemented on all play buttons implemented in a companion application or on a TV out screen as Spotify is the selected source. Any other button may also be assigned to use the Pull Context functionality provided it also switches the source to Spotify when used. When Spotify is the selected source, “Spotify” must be spelled out on all playback status screens. No abbreviations for “Spotify” can be used, but scrolling is allowed.

The available metadata and status information should be displayed whenever the display size allow.

All platforms that display track name, artist and album name are required to handle strings containing any valid UTF-8 character and to accurately render all characters in the ISO/IEC 8859-1:1998 “Latin 1” character set.

All platforms are additionally required to render local language scripts for any market where the product will be sold. Characters that partner cannot render accurately shall be rendered as a question mark or an empty box.

All graphical resources associated with Spotify needs to comply with the [Companion App Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app).

If displaying the currently playing track metadata and having play control commands in the same screen Spotify refer to a “Now Playing” screen. All “Now Playing” screens must comply with the [Companion App Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app).

- **Systems Integrator (SI)**: The SI needs to ensure that all [Spotify Playback Control commands](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#embedded-sdk-control-and-status-functionality) and the [Pull Context functionality](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#embedded-sdk-control-and-status-functionality) are available to the DM partner. The SI needs to ensure all metadata and status information are available to the DM partner. The *User Experience Requirements* must be included in all SI user manuals. The UTF 8 character set must be supported as specified above in any template applications or any template screens showing track name, album or artist name.
- **Device Maker using a SI platform (SI DM)**: The [Companion App Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app) must be implemented.
- **Device Maker (DM)**: The DM must map the Spotify Playback Control commands and the Pull Context to all corresponding functionalities in a [companion app](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app). The UTF 8 character set must be supported as specified above on all screens showing track name, album or artist name. The [Companion App Requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/companion-app) must be implemented.

## Audio Quality and Volume

### Audio Quality

The audio quality setting required by the Spotify is 320 kbps. The audio system must under no circumstances generate any unwanted noise. This includes audio glitches of any kind and clicking noises that occur with the lack of cross fading.

- **Systems Integrator (SI)**: The SI needs to ensure the Spotify performance requirements are fulfilled using 320 kbps.
- **Device Maker using a SI platform (SI DM)**: N/A
- **Device Maker (DM)**: The DM needs to ensure the Spotify performance requirements are fulfilled using 320 kbps.

### Volume

All manipulations of the volume on a device must be propagated to the Spotify Embedded SDK binary as a device is selected for Spotify playback. If there is a “Mute” button on the device or on a remote control this must implement setting the volume to zero in the Spotify Embedded binary.

If a device has no means for a user to manipulate the device volume before a Spotify user has logged in, the default volume must be “agreeable”, this means there must be no risk of an uncomfortably high volume level, nor a silence as a Spotify user starts a playback session.

For the volume control requirements on devices that are part of a multi-device system, see [Local propagation of audio in multi-device systems](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#local-propagation-of-audio-in-multi-device-systems).

- **Systems Integrator (SI)** : The SI needs to provide an implementation that propagates volume and mute commands to Spotify as a device is selected for playback.
- **Device Maker using a SI platform (SI DM)** : The SI DM partner must ensure that volume and mute propagates to Spotify as a device is selected for playback.
- **Device Maker (DM)** : The DM must ensure that volume and mute propagates to Spotify as a device is selected for playback.

## Presets

The Spotify Embedded SDK binary supports device presets. Any currently playing context on a device can be set as a preset. It is up to the device to remember the preset.

The binary provides a way to retrieve the currently playing context through [SpGetMetadata()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spgetmetadata). This includes the default name of the context which must be used for naming the preset. Using [SpPlayUriWithOptions()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplayuriwithoptions) the integration can set the specific options (shuffle, repeat) that the context had at the time of preset creation.

If a preset fails to be set or fails to play, an error message will be provided by the binary. A message must then be passed to the user stating that the currently playing context is not supported as a preset, or that it failed to play.

The maximum number of presets that can be associated with a single device is 20. The presets may be stored outside of the device.

If presets are available on a device, Spotify playlists must be possible to set as a preset.

Any textual or graphical representation of a preset associated with a Spotify playlist must state that its content originates from Spotify.

- **Systems Integrator (SI)** : The SI needs to provide an implementation that persistently stores the presets and a way to set a preset. The SI also needs to ensure their SI DM partners have access to the default name and have an API to play a preset. The SI needs to provide a way to propagate any error message.
- **Device Maker using a SI platform (SI DM)** : Any textual or graphical representation of a preset associated with a Spotify playlist must state that its content originates from Spotify. The SI DM needs to ensure that any error message is propagated to the end user.
- **Device Maker (DM)** : The DM needs to implement persistent storage of the presets. Any textual or graphical representation of a preset associated with a Spotify playlist must state that its content originates from Spotify. The DM need to ensure that any error message is propagated to the end user.

## Local propagation of audio in multi-device systems

“Local propagation” is defined as a local transmission of a Spotify audio stream between devices. A “leader” device gets the audio stream from the Spotify servers and redistributes it to local “follower” devices. Only one track at the time can be propagated per Spotify account.

Spotify allows local propagation within a home, typically over a user’s local area network, provided that the [multi-device system performance requirements](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#performance) are met. Spotify requires that the Spotify Embedded SDK binary is integrated in all internet connected devices that are a part of a local propagation set up.

To ensure a consistent device selection experience for single devices and for multi-device systems from within the Spotify applications, we have a number of requirements on the implementation of the [Spotify ZeroConf API](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#spotify-discovery-protocol-requirements) in a multi-device system. Spotify also have requirements on the volume control commands sent back to Spotify.

### Local propagation to non-internet connected speakers

In this document, “non-connected wireless speakers” are defined as speakers that are not connected to the Internet but equipped with a RF unit allowing wireless transmission of an audio stream. Non-connected wireless speakers rely entirely on a leader unit for their playback content and the traditional cable has been replaced by a wireless link for convenience.

#### Requirements on non-internet connected speakers

Spotify have no specific requirements on local propagation to a non-internet connected speaker. The system will be considered a standalone device and the all requirements on a standalone device, including the standalone device performance, will apply. However, it may announce more than one audio configuration using the [Device Alias](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#grouping-through-device-aliases) mechanism.

### Local propagation to internet connected devices

In the case of local propagation to internet-connected devices, we require that each device has the Spotify client integrated. The two main scenarios are multi-channel and multi-room (explained below), but all variations of local propagation to internet-connected devices needs to fulfill the same Spotify requirements.

#### Multi-channel

Multi-channel speakers setup is in this document defined as speakers playing the same track from a Spotify account but with different properties in sync. A multi-channel speaker setup is typically intended to be located in the same room. For instance you’ll have a group constituted by left channel + right channel or by left channel + right channel + subwoofer.

#### Multi-room / single stream

The definition of multi-room / single stream is multiple speakers playing the same track in sync using a single Spotify account.

#### Multi-room / multi-stream

The definition of multi-room / multi-stream is multiple speakers playing different tracks at the same time using a single Spotify account. Spotify does not support nor allow multiple streams from the same account.

#### Requirements on internet connected devices

Grouping a set of speakers with the intention to provide synchronized playback can be done either by

- Letting the group broadcast itself as a [single device](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#grouping-to-a-single-device)
- Announcing a number of “zones” as [Device Aliases](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#grouping-through-device-aliases)

Regardless of which model you choose, every time an Embedded SDK device starts or stops representing a group, it should indicate so by calling the `SpSetDeviceIsGroup()` API.

#### Grouping to a single device

When grouping to a single device, the group must broadcast itself as a single device using the Spotify Connect ZeroConf API.

The individual speakers included in the group must not broadcast themselves over the Spotify ZeroConf protocol. In other words, if a group of speakers will play the same stream in sync and is grouped in a group called “Living room + Bedroom” the device shown in the Spotify device picker should be the group name, for example “Living room + Bedroom”. This is typically done using a leader device, the device from which the Spotify stream will be propagated to follower devices, and rename this device to the group name. All follower devices must stop announcing themselves over the Spotify Connect ZeroConf protocol.

Any user logged into a device that is included in a group must be logged out, with the exception of the leader device which still shall have the user logged in. The renaming of the leader device needs to happen for the Spotify Connect ZeroConf broadcast as well as for the device “display name” (see the *Embedded SDK API reference*, `SpSetDisplayName`).

As soon as a group is “broken”, the individual devices must again broadcast themselves over Spotify Connect ZeroConf and set the device “display name” (see the *Embedded SDK API reference*, `SpSetDisplayName`) with their device names as it was before the grouping took place.

The same principle applies to a single device leaving the group where the group continues to exist. The original device name must be restored via the Spotify Embedded API and the device must start broadcast itself with the original device name on Spotify Connect ZeroConf.

A system that allows for the same speaker to be a part of more than one group at the same time needs to ensure that as long as a speaker is part of a group it is the group(s) that is to be broadcasted via Spotify Connect ZeroConf and that no user is logged into the device. Only non-grouped speakers are to be visible over Spotify Connect ZeroConf or have a user logged into it, with the exception of the leader device.

The Spotify integrated client may be shut down in the follower devices. The leader device needs to have the Spotify client running according to our [Device power save mode](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#device-source-selection-and-sleep-requirements) requirement. An ungrouped speaker must at all times have the Spotify client running according to our [Device power save mode](https://developer.spotify.com/documentation/commercial-hardware/implementation/requirements/technical#device-source-selection-and-sleep-requirements) requirement.

While in grouped mode the device of the group shall communicate the master volume of the group instead of its individual volume to the Spotify client using the Embedded SDK API. Individual speaker volume changes of a grouped device must not be propagated to the Spotify client unless it changes the master volume of the group, in which case the master volume shall be propagated.

If a device is part of a system that supports multi-room or equivalent, Spotify needs to be available to play in both standalone device mode as well as in multi-device mode.

#### Grouping through Device Aliases

From version 2.33, the Embedded SDK device alias concept gives a single Embedded SDK instance the possibility of appearing as several “virtual” speakers. These pseudo-devices are called device aliases.

Selecting which device alias is active can be done both on the device itself (using Embedded SDK APIs) or from the Spotify app (using ZeroConf). Implementation details are in the Embedded SDK package documentation, and in the [FAQ](https://developer.spotify.com/documentation/commercial-hardware/implementation/faqs).

The fundamental way the Embedded SDK and Spotify Connect works is not changed. The Embedded SDK only supports one user logged in at a time – so out of all the aliases available, only one will be active at a time. This will let the Spotify app have the exact same experience with device aliases as if they actually were physical speakers.

- **Systems Integrator (SI)** : The SI needs to provide an implementation that fulfill the above described grouping and volume control principles.
- **Device Maker using a SI platform (SI DM)** : The SI DM needs to provide an implementation that fulfill the above described grouping and volume control principles.
- **Device Maker (DM)** : The DM needs to provide an implementation that fulfill the above described grouping principles

## Performance

All Spotify Embedded SDK integrations need to meet Spotify playback performance standards. The following performance requirements are applicable to integrations, measuring from the press of a key or from the touch of a screen until the action is in effect, on a standard wireless LAN system using an internet connection with a download speed of at least 3 Mbps.

There are different requirements between a standalone device and a multi-device system, with a higher tolerance to latency in a multi-device environment. The standalone device performance requirements apply to all devices, i.e a device that might be part of a multi-device system will have to fulfill the standalone device performance requirements when run alone.

### Spotify performance requirements

Action in Spotify appStandalone device  
Time until action takes effectMulti-device system  
Time until action takes effectSkip/Next500 ms1000 msPrevious500 ms1000 msPause500 ms1000 msPlay/resume500 ms1000 msChange volume500 ms1000 msSeek500 ms1000 msLoad500 ms1000 ms

Action via device button, via  
remote or via companion appStandalone device  
Time until action takes effectMulti-device system  
Time until action takes effectPause250 ms500 msResume250 ms500 ms

## Firmware Upgrades

Spotify requires the possibility to send the partner updates. The firmware upgrade cycle must allow for a Spotify upgrade at least once every 6 months.

In the case of Spotify ceasing support of an outdated version of the Spotify Embedded SDK we may require a firmware upgrade with a maximum of 90 days up until the submission for a new certification.

## Play History

Devices must not store or display the play history of a Spotify user.

## Embedded SDK Control and Status Functionality

The Spotify Embedded SDK binary provides the means to control playback as well as getting status and metadata. This section outlines the functionality available.

### Playback Control Commands and Play Status

The Spotify Embedded SDK binary provides an API that enables the retrieval of the play state of the device, and controls various playback features. Not all commands are allowed for all integrations, so ensure that you check the instructions for your particular integration (e.g. speaker, display or companion app).

FunctionalityControl cmdStatusPlay/Pause/StopYesYesSkip fwdYesN/ASkip backYesN/ASeekYesN/AVolumeYesYesMuteYesN/ARepeatNoYesShuffleNoYes

“Stop” and “Pause” are treated in the same way by the binary: “Stop” command will pause the playback.

### Pull Context

The Pull Context functionality allows the latest played Spotify context to be “taken over”. If a playback is ongoing on another device, the Pull Context functionality will pause the playback on the other device and resume it on the device invoking the Pull Context. If the playback is paused on another device the pull context will resume the playback on the device that invoked the Pull Context.

If no other device is active the latest context known to the device invoking the pull context will be played.

If a device is trying to pull a context and no other devices have been active with the same user logged in since the last reboot, there will be no context to pull and therefore the Pull Context functionality will not work.

### Spotify metadata

The Spotify Embedded SDK provides an API that enables the retrieval of metadata and status regarding the currently playing track. The metadata is restricted to some context and might not be allowed to use in all integrations, so ensure that you check the instructions for your particular integration (e.g. speaker, display or companion app).

SongsPodcastsTrack nameEpisode nameArtist nameShow nameAlbum nameDurationDuration