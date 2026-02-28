---
title: eSDK Initialization | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/guides/initialization
source: crawler
fetched_at: 2026-02-27T23:41:21.877134-03:00
rendered_js: true
word_count: 442
summary: This document explains how to initialize the Spotify library for commercial hardware by configuring the required fields within the SpConfig structure.
tags:
    - spotify-connect
    - initialization
    - hardware-integration
    - spconfig
    - device-configuration
    - embedded-systems
category: guide
---

To initialize the library, use the function [SpInit()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spinit). The function takes a struct of type [SpConfig](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) as a parameter. Within [SpConfig](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) there are a number of required fields that need to be set to start with:

- [SpConfig::memory\_block](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). A pointer to an application-provided memory buffer that the library uses for all its memory allocations. The library does not allocate any memory beyond the size of the buffer (other than stack variables).
- [SpConfig::unique\_id](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). A unique id for the device on which it is running, typically the MAC address. This is used by the library to distinguish the device from other Spotify Connect-enabled devices that the user has. It is important that this ID is sufficiently unique and that it does not change between sessions. (See [SpConfig::unique\_id](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) for more information.)
- [SpConfig::display\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). The name of the device that will appear when selecting the device in the Connect menu of the Spotify mobile app, for example. Typically, this is the model name of the device or the name that the device uses to announce itself via UPnP or similar protocols.
- The fields [SpConfig::brand\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) and [SpConfig::model\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) should be set to match the brand and model name that you provided in the certification application for the hardware product.
- [SpConfig::brand\_display\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) and [SpConfig::model\_display\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). Use these fields if the brand/model strings (see previous bullet) contain characters not allowed. If used, they will override [SpConfig::brand\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) and [SpConfig::model\_name](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) for display purposes.
- [SpConfig::device\_type](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). The field should be set to the device type that matches the hardware product most closely.
- [SpConfig::client\_id](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). Provide a Client ID in the field.
- [SpConfig::product\_id](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). For each product enter a designated Product ID, a non-zero unsigned integer which enumerates this model. The simplest way to assign Product IDs for your products is to just use 1, 2, 3, and so on. The Product ID must match the value given in the New Product Application form for this particular model.
- [SpConfig::error\_callback](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig). A callback function that the library will use to report errors that happen asynchronously.

Apart from these fields, there are a number of fields you may use. For a complete list, see the [SpConfig](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) page.

`1`

`struct SpConfig conf;`

`2`

`int buffer_size = SP_RECOMMENDED_MEMORY_BLOCK_SIZE;`

`3`

`enum SpDeviceType device_type = kSpDeviceTypeSpeaker;`

`4`

`const char *client_id = "my-client-id";`

`5`

`6`

`memset(&conf, 0, sizeof(conf));`

`7`

`8`

`conf.api_version = SP_API_VERSION;`

`9`

`conf.memory_block = malloc(buffer_size);`

`10`

`conf.memory_block_size = buffer_size;`

`11`

`conf.error_callback = CallbackError;`

`12`

`conf.error_callback_context = NULL;`

`13`

`conf.display_name = "Example";`

`14`

`conf.unique_id = "my-sample-unique-id";`

`15`

`conf.brand_name = "Example_Brand";`

`16`

`conf.model_name = "example_embedded";`

`17`

`conf.brand_display_name = "Example Brand";`

`18`

`conf.model_display_name = "example_embedded \u266C";`

`19`

`conf.device_type = device_type;`

`20`

`conf.zeroconf_serve = 1;`

`21`

`conf.zeroconf_port = 0;`

`22`

`conf.host_name = conf.unique_id;`

`23`

`conf.client_id = client_id;`

`24`

`conf.scope = SP_SCOPE_STREAMING;`