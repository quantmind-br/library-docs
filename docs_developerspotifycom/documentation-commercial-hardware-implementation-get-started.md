---
title: Getting Started | Spotify for Developers
url: https://developer.spotify.com/documentation/commercial-hardware/implementation/get-started
source: crawler
fetched_at: 2026-02-27T23:41:19.93689-03:00
rendered_js: true
word_count: 880
summary: This tutorial explains how to set up the Spotify eSDK and create a basic Spotify Connect-enabled music player application using the C API. It covers environment configuration, library initialization with specific device parameters, and the implementation of a main event loop.
tags:
    - spotify-esdk
    - spotify-connect
    - embedded-development
    - c-api
    - sdk-initialization
    - event-loop
category: tutorial
---

This section shows you how to use the Spotify eSDK to write a simple Spotify Connect-enabled music player application.

The Spotify eSDK is a lightweight library with a C API that allows you to integrate Spotify into your devices and applications. It has been written from the ground up with the needs of device manufacturers in mind. The SDK provides an API that facilitates the integration and ensures high performance and low memory footprint on a wide range of hardware architectures.

## Set up the environment

The first steps is to download an eSDK build from Certomato under the [*Builds*](https://certomato.spotify.com/builds/) section. Please refer to the [Onboarding](https://developer.spotify.com/documentation/commercial-hardware/onboarding) section if you don't have access to Certomato access yet.

Once you have the eSDK bundle locally stored, unzip it. A new folder will be created with the following contents:

- `docs` folder which contains the API Reference in HTML format.
- `examples` with file samples using the eSDK in different contexts.
- `include` with headers file for compiling.
- `libs` which contains a static and dynamic version of the eSDK library ready to be linked with.

The next step is to generate a valid `client_id`. Please follow the [app guide](https://developer.spotify.com/documentation/web-api/concepts/apps) to do so.

Let's create our workspace that will store our project. Create a new folder called `esdk-hello-world` and add a file called `Makefile`.

A Makefile is a file which defines a set of rules (compile, link, clean, etc.) to be executed by the `make` tool. There are other tools you could use to build your software, such as [cmake](https://www.cmake.org) or [scons](https://www.scons.org/), but we will use `make` for the sake of simplicity.

`1`

`CC = gcc`

`2`

`3`

`ESDK_HOME=path/to/your/esdk/folder`

`4`

`5`

`CFLAGS = -g -Wall -I$(ESDK_HOME)/include`

`6`

`LDFLAGS = -lm $(ESDK_HOME)/lib/libspotify_embedded_static.a`

`7`

`8`

`all: main`

`9`

`10`

`main: main.o`

`11`

`main.o: main.c`

`12`

`13`

`clean:`

`14`

`rm -rvf main.o main`

Don't forget to replace the `ESDK_HOME` variable with the location of the unzipped eSDK folder.

## Initializing the library

Create a new file called `main.c` with the following content, which contains a simplified example of using the [SpInit()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spinit) function:

`1`

`#include <stdio.h>`

`2`

`#include <unistd.h>`

`3`

`#include <sys/time.h>`

`4`

`#include <stdlib.h>`

`5`

`#include <string.h>`

`6`

`#include <ctype.h>`

`7`

`#include <signal.h>`

`8`

`#include "latest"`

`9`

`#include "spotify_embedded_log.h"`

`10`

`11`

`static void CallbackError(SpError error, void *context) {`

`12`

`printf("Error: %d\n", error);`

`13`

`}`

`14`

`15`

`int main(int argc, char *argv[]) {`

`16`

`SpError err;`

`17`

`struct SpConfig conf;`

`18`

`int buffer_size = SP_RECOMMENDED_MEMORY_BLOCK_SIZE;`

`19`

`enum SpDeviceType device_type = kSpDeviceTypeSpeaker;`

`20`

`const char *client_id = "my-client-id";`

`21`

`22`

`memset(&conf, 0, sizeof(conf));`

`23`

`24`

`conf.api_version = SP_API_VERSION;`

`25`

`conf.memory_block = malloc(buffer_size);`

`26`

`conf.memory_block_size = buffer_size;`

`27`

`conf.error_callback = CallbackError;`

`28`

`conf.error_callback_context = NULL;`

`29`

`conf.display_name = "Example";`

`30`

`conf.unique_id = "my-sample-unique-id";`

`31`

`conf.brand_name = "Example_Brand";`

`32`

`conf.model_name = "example_embedded";`

`33`

`conf.brand_display_name = "Example Brand";`

`34`

`conf.model_display_name = "example_embedded \u266C";`

`35`

`conf.device_type = device_type;`

`36`

`conf.zeroconf_serve = 1;`

`37`

`conf.zeroconf_port = 0;`

`38`

`conf.host_name = conf.unique_id;`

`39`

`conf.client_id = client_id;`

`40`

`conf.scope = SP_SCOPE_STREAMING;`

`41`

`42`

`if (kSpErrorOk != (err = SpInit(&conf))) {`

`43`

`printf("Error %d\n", err);`

`44`

`return 0;`

`45`

`}`

`46`

`47`

`SpFree();`

`48`

`49`

`return 0;`

`50`

`}`

The example calls the function [SpInit()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spinit) to perform the eSDK initialization. The function takes a struct of type [SpConfig](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconfig) as a parameter.

Finally, compile and generate the binary with the following command:

## Adding a main event loop

In order to implement the main event loop, the function [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents) must be called periodically. To show how this works, let's force a login error by calling the function [SpConnectionLoginOauthToken()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#spconnectionloginpassword:~:text=SpConnectionLoginOauthToken%28%29) with an invalid token. After calling [SpPumpEvents()](https://developer.spotify.com/documentation/commercial-hardware/implementation/reference/latest#sppumpevents) a couple of times, the error callback will be invoked and the application quits.

Here is the new code that checks for login errors:

`1`

`SpError error_occurred = kSpErrorOk;`

`2`

`3`

`static void CallbackError(SpError err, void *context) {`

`4`

`LOG("Error: %d\n", err);`

`5`

`error_occurred = err;`

`6`

`}`

`7`

`8`

`int main(int argc, char *argv[]) {`

`9`

`SpError err;`

`10`

`struct SpConfig conf;`

`11`

`int buffer_size = SP_RECOMMENDED_MEMORY_BLOCK_SIZE;`

`12`

`enum SpDeviceType device_type = kSpDeviceTypeSpeaker;`

`13`

`const char *client_id = "my-client-id";`

`14`

`15`

`memset(&conf, 0, sizeof(conf));`

`16`

`17`

`conf.api_version = SP_API_VERSION;`

`18`

`conf.memory_block = malloc(buffer_size);`

`19`

`conf.memory_block_size = buffer_size;`

`20`

`conf.error_callback = CallbackError;`

`21`

`conf.error_callback_context = NULL;`

`22`

`conf.display_name = "Example";`

`23`

`conf.unique_id = "my-sample-unique-id";`

`24`

`conf.brand_name = "Example_Brand";`

`25`

`conf.model_name = "example_embedded";`

`26`

`conf.brand_display_name = "Example Brand";`

`27`

`conf.model_display_name = "example_embedded \u266C";`

`28`

`conf.device_type = device_type;`

`29`

`conf.zeroconf_serve = 1;`

`30`

`conf.zeroconf_port = 0;`

`31`

`conf.host_name = conf.unique_id;`

`32`

`conf.client_id = client_id;`

`33`

`conf.scope = SP_SCOPE_STREAMING;`

`34`

`35`

`if (kSpErrorOk != (err = SpInit(&conf)))`

`36`

`LOG("Error %d\n", err);`

`37`

`goto end;`

`38`

`}`

`39`

`40`

`err = SpConnectionLoginOauthToken("this is not a real OAuth access token");`

`41`

`if (err != kSpErrorOk) {`

`42`

`/* The function would only return an error if we hadn't invoked SpInit()`

`43`

`or if we had passed an empty username or password.`

`44`

`Actual login errors will be reported to ErrorCallback().`

`45`

`*/`

`46`

`LOG("Error %d\n", err);`

`47`

`goto end;`

`48`

`}`

`49`

`50`

`while (1) {`

`51`

`err = SpPumpEvents();`

`52`

`if (kSpErrorOk != err || error_occurred) {`

`53`

`goto end;`

`54`

`}`

`55`

`}`

`56`

`57`

`end:`

`58`

`SpFree();`

`59`

`60`

`return 0;`

`61`

`}`

## What's next?

You can follow the eSDK Developer Guides to read further about how to integrate the eSDK.