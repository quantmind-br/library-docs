---
title: Media Delivery API | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/media-delivery
source: crawler
fetched_at: 2026-02-27T23:41:24.260392-03:00
rendered_js: true
word_count: 2299
summary: This document outlines the Media Delivery API for the Spotify eSDK, explaining how to manage media streams, audio decoding, and playback through specialized callbacks and notifications.
tags:
    - media-delivery-api
    - esdk
    - audio-streaming
    - playback-control
    - media-callbacks
    - stream-fetching
category: api
---

The Media Delivery API is a new way to get media streams from eSDK. The API decouples audio decoding and playback from fetching files. This makes it possible to add support for new file formats to already released versions of the eSDK by using decoders provided by the application.

The API functions are documented in the file [spotify\_embedded\_media.h](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#media). This document gives an overview of different use cases with the API.

## Terms

TermDescriptionApplicationThe partner code that uses the eSDK.PlaybackThe process of a media device taking raw or uncompressed samples and playing them through a speaker, headphones or equivalent.TrackA single media entity. Note that one track could consist of more than one stream.Playing TrackThe currently playing trackUpcoming TrackThe track that will be streamed and played next, regardless of if it's the next, previous, or otherwise indexed track in the current contextNext TrackThe next track in the current contextPrevious TrackThe previous track in the current contextStreamByte stream for the media. Similar to the downloading of a file.Stream idA unique identifier which is used to differentiate media streams.Stream startBeginning of media stream. The point where the decoder should be initialized. Compare with opening a media file.Stream endEnd of media stream. When the track is playing, stream end will inform the application that there are no more data to be expected. The decoder can then be freed after all the stream are decoded and pcm samples output to the audio driver. Compare with closing a media file.StreamingDelivering data to the application.FlushAction where all queued encoded or decoded media data is cleared.

## Audio Streaming Overview

This is an overview of the flow of data and the role of each party, eSDK and the application.

![Audio Streaming Diagram](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/audio-streaming-overview.png)

Note: Implementing DRM in the application will be supported for only a subset of formats.

## Invariants

- `StreamStart` is always paired with the corresponding `StreamEnd` (i.e. same `stream_id`)
- There can be at most one stream in progress at any time, being delivered to the Application (i.e. only one StreamStart without the corresponding `StreamEnd`)
- When a Stream is delivered, eSDK will proceed with the next stream to prefetch the next track: Two streams then exist, the first one that is currently playing and the second one that is prefetching.

## API

Media Delivery API uses notifications, callbacks, events and a set of auxiliary functions.

### Notifications

The application must call the notification functions for the eSDK to be able to track the current state of the application:

- [SpNotifyStreamPlaybackStarted](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifystreamplaybackstarted)
- [SpNotifyStreamPlaybackContinued](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifystreamplaybackcontinued)
- [SpNotifyStreamPlaybackFinishedNaturally](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifystreamplaybackfinishednaturally)
- [SpNotifyTrackLength](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifytracklength)
- [SpNotifyTrackError](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifytrackerror)

For more information please refer to the API reference documentation for [spotify\_embedded\_media.h](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#media) and the sequence diagrams under Media Delivery API use cases.

### Callbacks

The application must register a set of callbacks using SpRegisterStreamCallbacks. The callbacks are described in the following C structure:

`1`

`struct SpStreamCallbacks {`

`2`

`/* Start of stream callback */`

`3`

`SpCallbackStreamStart on_start;`

`4`

`/* Data stream callback */`

`5`

`SpCallbackStreamData on_data;`

`6`

`/* End of stream callback */`

`7`

`SpCallbackStreamEnd on_end;`

`8`

`/* Current playback position callback */`

`9`

`SpCallbackStreamGetPosition on_get_position;`

`10`

`/* Seek to position callback */`

`11`

`SpCallbackStreamSeekToPosition on_seek_position;`

`12`

`/* Flush callback */`

`13`

`SpCallbackStreamFlush on_flush;`

`14`

`};`

For more information please refer to the API reference documentation in [spotify\_embedded\_media.h](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#media).

### Events

In addition to other eSDK notifications this Media Delivery API uses two notifications that the application should handle through the eSDK notification callback: [kSpPlaybackNotifyPlay](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification) and [kSpPlaybackNotifyPause](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacknotification). It's important that the application buffers delivered data, and plays/pauses it based on those notifications. When the application buffer is full, the new samples delivered by eSDK should be rejected until space in the buffer is available again.

## Media Delivery API use cases

Here is a description of the API usage in different use cases such as skipping and seeking. The following sequence diagrams document how eSDK and the application are supposed to function.

### Playing a track

![Playing a track](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-playing-track.png)

Track 1 is the track that is being played. Track 2 is the upcoming track that is being prefetched. The application buffer will have to keep track of two positions: the playback position (the samples being played) and the delivery position (the samples being buffered).

At a given moment, the buffer might contain data from different streams. The application is not required to keep track of the position where a stream ends or begins. The following diagram illustrate the state of the buffer at a given moment:

Case: playing stream which is being delivered ![Play And Prefetch Current](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/play_and_prefetch_current.png)

Case: prefetching upcoming stream while playing first stream ![Play Current Prefetch Next](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/play_current_prefetch_next.png)

### Skipping

#### Skip while the playing track is being delivered

![Skipping track](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-skipping.png)

Skipping while a track is being streamed will trigger `StreamEnd` followed by `StreamFlush`. After this the `StreamStart` is triggered for the upcoming track.

#### Skip when upcoming track was, or is being delivered

![Skipping track delivered](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-skipping-delivered.png)

- Skipping to the next or the previous track will get rid of all buffered data, both played and not yet played samples.
- The next stream delivery will always have a new ID.
- Stream id 1 is the playing track
- Stream id 2 is the next/previous track
- Stream id 3 is the same track as Track 2 (the next/previous track)

### Seeking

Streams which are seekable have a known size in the beginning of the stream. That is, `StreamStart` callback will have non-zero `stream_size_bytes` value.

#### Start playing a track with non-zero starting position

![Seeking stream](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-seek.png)

- Usually tracks start from the beginning (position zero), but in some cases, a track can start from a non-zero starting position. For example:
  
  - When starting a podcast from a previously stored resume point.
  - When pushing a playing state to the application using Spotify Connect.
- If a track should start playing at a position greater than 0, `StreamStart` will be followed by `StreamSeekToPosition` before `StreamData` is called for the stream.
- The application needs to call [SpSetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) to set the byte offset from where eSDK will start streaming data.
- Once the Application has the bytes that it needs to play from the intended offset, it must call SpNotifySeekComplete to let the eSDK know it's ready to start playback. Please refer to the Seeking and Download Position section.

#### Seek in streaming track

![Seeking stream track](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-seek.png)

- Seeking in a track which is still streaming triggers the `StreamFlush` callback, after which the application should call the [SetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) function with the new offset. This function may be called multiple times to get the corrent seek position. When the correct stream position has been obtained, a call to SpNotifySeekComplete will inform eSDK that the seek is done.
- The stream delivery will resume from the seek position using the same ID as before.

#### Seek when upcoming track has been, or is being delivered

![Seeking in streaming track](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-seek-delivered.png)

- If the playing track has been fully streamed and the upcoming track streaming has started, all data from the upcoming track will be discarded and re-streamed to the application eventually.
- In this case `id=3` is the same track as `id=1`, but since the stream has already ended, there will be a new stream.

### Bitrate changes

**Note**: This section is only applicable for eSDK build profiles that enable automatic bitrate changes between tracks or in the middle of tracks, or if the application intentionally calls [SpPlaybackSetBitrate](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spplaybacksetbitrate) while streaming.

#### Change bitrate middle of playing track which is being delivered

![Chage bitrate middle of playing track](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-setbitrate.png)

- Playing a track when the bitrate changes will result in audio data being dropped.
- The stream delivery will restart from the last played position and will use a new ID.

#### Change bitrate in the middle of a playing track when upcoming track is delivering

![Chage bitrate upcoming track is delivering](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-setbitrate-delivered.png)

Playing a fully buffered track during a bitrate change will result in all audio data being dropped. The stream delivery will restart from the last played position and will use a new ID.

#### Change bitrate for the upcoming track which is already delivering

![Chage bitrate meddile playing upcoming track is delivering](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-setbitrate-track2.png)

- Changing bitrate in a track where data is already available will result in audio data being dropped.
- The stream delivery will provide a new ID.

### Errors

For eSDK to be able to handle errors properly, any playback and/or decoding errors need to be reported back from the application to the eSDK. Error reporting is done through the function [SpNotifyTrackError](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifytrackerror).

#### Application cannot the initialize decoder

![Error initialize decoder](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-errors.png)

- If the application cannot decode a track (because of unsupported format etc.), it needs to call [SpNotifyTrackError](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifytrackerror) to inform eSDK.
- Track 1 is interrupted and marked as failed
- Playback advances to track 2

#### Playing track which is streaming has a decoding or playback error

![Error upcoming streaming decoding](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-errors-track1.png)

- Track 1 is interrupted and marked as failed
- Playback advances to track 2

#### Playing and already streamed track has a decoding or playback error

![Error decoding already streamed](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-errors-delivered.png)

- Track 1 is interrupted and marked as failed
- Playback advances to the next track and streaming starts again for track 2 with new Stream ID 3

#### Upcoming streaming track has decoding error

![Error decoding](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-errors-decoding.png)

- Track 1 is played fully without interruptions
- When it's time to start track 2, it is not played but playback advances to track 3

#### Upcoming already streamed track has decoding error

![Error decoding](https://developer-assets.spotifycdn.com/images/documentation/commercial-hardware/media-errors-already-error.png)

- Track 1 is played fully without interruptions
- When it's time to start track 2, it is not played but playback advances to track 3

### Example code

Included with the eSDK release is the following example code to show how an application with Media Delivery API could work:

- `audio_decoder.h` - generic audio decoder interface
- `decoder_mp3.c` - implementation of mp3 decoder using [minimp3 library](https://github.com/lieff/minimp3)
- `decoder_vorbis.c` - implementation of ogg/vorbis decoder using [libvorbis library](https://gitlab.xiph.org/xiph/vorbis)
- `decoder_flac.c` - implementation of flac decoder using [libflac library](https://gitlab.xiph.org/xiph/flac)
- `media_delivery.c`, `media_delivery.h` - example implementation of the Media Delivery API.
- `bitstream_buffer.c`, `bitstream_buffer.h` - bitstream buffer needed by example mp3 decoder.
- `metadata_page.c`, `metadata_page.h` - code to parse Spotify ogg metadata page. Used by media delivery example code.

### Appendices

#### Media Format

##### How to indicate support for media formats

Since the Media Delivery API is format agnostic, eSDK needs to know which media formats the application supports. This information is provided by the application during eSDK initialization time and eSDK uses it to determine which formats will be delivered to the application. The application is expected to fill in the field supported\_drm\_media\_formats in the SpConfig structure:

`1`

`struct SpConfig {`

`2`

`// ... clip ...`

`3`

`struct SpDrmSupportedMediaFormat supported_drm_media_formats[SP_MAX_SUPPORTED_DRM_FORMATS];`

`4`

`};`

In addition, if the application uses its own ZeroConf webserver, the ZeroConf getInfo response must be amended with the media format information as mentioned in the ZeroConf documentation.

##### Spotify ogg/vorbis media format

Most music tracks within Spotify use the ogg/vorbis media format which was also the only format that the old compressed API (`SpCallbackPlaybackCompressData`) supported.

The ogg/vorbis files delivered by Media Delivery API are different from normal ogg/vorbis files in that they contain a Spotify proprietary metadata page as the first page of the stream. This metadata page is required to have efficient seeking within the files and the application is required to be able to handle the metadata page. Example code to parse the metadata page is included in the release package.

##### Seeking and Download Position

When a seek occurs the application will be informed by a `SpNotifyStreamSeekToPosition` notification, which has a time position in milliseconds as a parameter. The application should convert the time position to a byte offset and use `SpStreamSetDownloadPosition` to communicate this value back to eSDK.

The application can call `SpStreamSetDownloadPosition` multiple times while looking for the correct byte offset. Once the correct byte offset is found the application should call `SpNotifySeekComplete`.

Byte offset calculation methods:

- Calculate using a seek table. The ogg/vorbis files in the Spotify catalog use a proprietary seek table. Refer to metadata\_page.c in the examples/common.
- Calculate using a formula. Usually possible for constant bitrate streams.
- Perform a search by probing different positions in the stream, and comparing the resulting time position with desired one.

If headers are needed for the byte offset calculation they could be cached in memory or fetched from the data stream, for example by requesting data from a certain position.

The ogg decoder in the sample code uses Spotify proprietary ogg/vorbis seek tables embedded in the ogg streams.

The mp3 decoder in the sample code assumes the MP3 file uses a constant bitrate, so that it can calculate the download byte position using the bitrate.

##### Binary search for the seek byte postion

Since eSDK doesn't have a decoder it can't know how to map time position to byte position. As a result, it needs help to find the byte position from where to start download.

The idea is that the integration will prob different byte positions in the file and detect their time positions.

This is achieved using [SpSetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) and `StreamData` working in a command-response fashion to accomplish a binary search (dichotomy).

- [SpSetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) triggers a download from a given byte position.
- `StreamData` delivers the samples to be decoded to compute the time position.

This command-response can be done several times till finding the time position that matches the best the seek position. To help understand better, here is an example of the search algorithm:

Imagine we have a file with `file_size = 2000` bytes .

- The user wants to seeks to the position 5 seconds.
- The integration calls [SpSetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) with an informed guess, the middle of the file: `file_size/2` (1000).
- eSDK will download and callback `StreamData` with encoded audio at file position 1000
- The integration decodes the samples and find time position, 3 cases are possible:
  
  1. `time position == seek position` -&gt; Search is done, The integration calls [SpNotifySeekComplete](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spnotifyseekcomplete) and then decodes and plays the file.
  2. `time position > seek position` -&gt; The integration calls [SpSetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) with `(file_size/2) + (file_size/4)`
  3. `time position < seek position` -&gt; The integration calls [SpSetDownloadPosition](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spsetdownloadposition) with `(file_size/2) - (file_size/4)`
- Repeat this process till the seek position is good enough (matching 5 seconds).

### Code

Refer to header file [spotify\_embedded\_media.h](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#media).