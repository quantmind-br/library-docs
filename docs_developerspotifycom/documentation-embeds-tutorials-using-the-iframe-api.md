---
title: Using the iFrame API | Spotify for Developers
url: https://developer.spotify.com/documentation/embeds/tutorials/using-the-iframe-api
source: crawler
fetched_at: 2026-02-27T23:40:20.326767-03:00
rendered_js: true
word_count: 889
summary: This document provides a step-by-step tutorial on implementing the Spotify iFrame API to programmatically create, control, and customize Spotify Embeds in web applications. It covers script integration, controller initialization, and dynamic content loading using the API's built-in methods.
tags:
    - spotify-iframe-api
    - web-embeds
    - javascript-sdk
    - media-playback
    - frontend-development
    - iframe-controller
category: tutorial
---

## Overview

Developers can use the iFrame API to programmatically create and interact with a single [Embed](https://developer.spotify.com/documentation/embeds/tutorials/creating-an-embed) or with multiple Embeds in the same web app. The iFrame API includes methods that you can use to start playback, change the content rendering in an Embed, or stop playback. This step-by-step guide explains one way you might implement the iFrame API in an existing web site.

### 1. Add the iFrame API script tag to your HTML page

Begin by including a `<script>` element to your web page that refers to Spotify's iFrame API script, `https://open.spotify.com/embed/iframe-api/v1`. We recommend adding this element somewhere in the `<body>` element of the page:

`1`

`<script src="https://open.spotify.com/embed/iframe-api/v1" async></script>`

### 2. Create an element for the iFrame

Add an HTML element with a unique `id` attribute to your document. This element will be replaced with the Embed iFrame.

For example, you could add a `<div>` element like this one after the `<body>` HTML tag:

`1`

`<div id="embed-iframe"></div>`

### 3. Define the `window.onSpotifyIframeApiReady` function

After the browser has loaded the iFrame API script, the `window.onSpotifyIframeApiReady` function is called. This signals to your app that it is now safe to rely on the methods of the iFrame API.

`1`

`window.onSpotifyIframeApiReady = (IFrameAPI) => {`

`2`

`//`

`3`

`};`

### 4. Create a controller object

Each instance of the Embed should have a controller object associated with it. The controller object has methods that you can use to configure the Embed and to control playback.

The `window.onSpotifyIframeApiReady` function receives an object parameter, `IFrameAPI` in our example. You can use the `createController` method of the IFrameAPI to create a controller for your Embed. `createController` accepts three mandatory parameters: the element that we defined earlier, an `options` object, and a callback function:

`1`

`window.onSpotifyIframeApiReady = (IFrameAPI) => {`

`2`

`const element = document.getElementById('embed-iframe');`

`3`

`const options = {`

`4`

`uri: 'spotify:episode:7makk4oTQel546B0PZlDM5'`

`5`

`};`

`6`

`const callback = (EmbedController) => {};`

`7`

`IFrameAPI.createController(element, options, callback);`

`8`

`};`

### 5. Test your page

At this point, your page displays an Embed!

![Web page with an Embed for the Life at Spotify podcast](https://developer-assets.spotifycdn.com/images/documentation/embeds/basic-iframe-api.png)

### 6. Add episode switching logic

Let's use the capabilities of the iFrame API to change the contents of the Embed. We'll add three podcast episodes to the page. Each episode has a button with a data attribute that contains the Spotify ID of the episode.

`1`

`<div class="episodes">`

`2`

`<button class="episode" data-spotify-id="spotify:episode:7makk4oTQel546B0PZlDM5">`

`3`

`My Path to Spotify: Women in Engineering`

`4`

`</button>`

`5`

`6`

`<button class="episode" data-spotify-id="spotify:episode:43cbJh4ccRD7lzM2730YK3">`

`7`

`What is Backstage?`

`8`

`</button>`

`9`

`10`

`<button class="episode" data-spotify-id="spotify:episode:6I3ZzCxRhRkNqnQNo8AZPV">`

`11`

`Introducing Nerd Out@Spotify`

`12`

`</button>`

`13`

`</div>`

Next, let's modify the `callback` function we defined earlier. We're going to add a click event listener to each of the buttons.

`1`

`const callback = (EmbedController) => {`

`2`

`document.querySelectorAll('.episode').forEach(`

`3`

`episode => {`

`4`

`episode.addEventListener('click', () => {`

`5`

`// click event handler logic goes here`

`6`

`});`

`7`

`})`

`8`

`};`

Each of the buttons has a data attribute that contains the episode's Spotify URI. As a final step, we're going to use the iFrame API's loadUri method to tell the Embed to load the episode that has been clicked on.

`1`

`episode.addEventListener('click', () => {`

`2`

`EmbedController.loadUri(episode.dataset.spotifyId)`

`3`

`});`

Now we have a menu that loads Spotify episodes in the Embed as each button is clicked!

### 7. Customize the appearance of the Embed

Our app works, but the design could look better. Let's resize the Embed by adjusting the `options` object that we set when creating the controller.

`1`

`const options = {`

`2`

`width: '60%',`

`3`

`height: '200',`

`4`

`uri: 'spotify:episode:7makk4oTQel546B0PZlDM5'`

`5`

`};`

Next let's add some CSS to the page to style the menu. You can do this by by linking to an external stylesheet or inline on the page using a `<style>` element. Here's what our UI looks like now:

Now we have a working example that uses the iFrame API and one of its methods. You can expand on this further by implementing the [`togglePlay()`](https://developer.spotify.com/documentation/embeds/references/iframe-api#embedcontrollertoggleplay) method or other available methods of the iFrame API. Full source code for this sample page is below:

`1`

`<html lang="en">`

`2`

`<head>`

`3`

`<title>A Spotify Embed Example</title>`

`4`

`<meta name="viewport" content="width=device-width, initial-scale=1" />`

`5`

`<style>`

`6`

`.episodes {`

`7`

`display: flex;`

`8`

`flex-direction: column;`

`9`

`}`

`10`

`11`

`.episode {`

`12`

`min-width: max-content;`

`13`

`margin-bottom: .8rem;`

`14`

`padding: .8rem 1rem;`

`15`

`border-radius: 10px;`

`16`

`border: 0;`

`17`

`background: #191414;`

`18`

`color: #fff;`

`19`

`cursor: pointer;`

`20`

`}`

`21`

`22`

`.episode:hover {`

`23`

`background: #1Db954;`

`24`

`}`

`25`

`26`

`@media screen and (min-width: 860px) {`

`27`

`body {`

`28`

`display: flex;`

`29`

`flex-direction: row;`

`30`

`gap: 1rem;`

`31`

`}`

`32`

`}`

`33`

`</style>`

`34`

`</head>`

`35`

`36`

`<body>`

`37`

`<div class="episodes">`

`38`

`<button class="episode" data-spotify-id="spotify:episode:7makk4oTQel546B0PZlDM5">`

`39`

`My Path to Spotify: Women in Engineering`

`40`

`</button>`

`41`

`<button class="episode" data-spotify-id="spotify:episode:43cbJh4ccRD7lzM2730YK3">`

`42`

`What is Backstage?`

`43`

`</button>`

`44`

`<button class="episode" data-spotify-id="spotify:episode:6I3ZzCxRhRkNqnQNo8AZPV">`

`45`

`Introducing Nerd Out@Spotify`

`46`

`</button>`

`47`

`</div>`

`48`

`49`

`<div id="embed-iframe"></div>`

`50`

`<script src="https://open.spotify.com/embed/iframe-api/v1" async>`

`51`

`</script>`

`52`

`<script type="text/javascript">`

`53`

`window.onSpotifyIframeApiReady = (IFrameAPI) => {`

`54`

`const element = document.getElementById('embed-iframe');`

`55`

`const options = {`

`56`

`width: '100%',`

`57`

`height: '160',`

`58`

`uri: 'spotify:episode:7makk4oTQel546B0PZlDM5'`

`59`

`};`

`60`

`const callback = (EmbedController) => {`

`61`

`document.querySelectorAll('.episode').forEach(`

`62`

`episode => {`

`63`

`episode.addEventListener('click', () => {`

`64`

`EmbedController.loadUri(episode.dataset.spotifyId)`

`65`

`});`

`66`

`})`

`67`

`};`

`68`

`IFrameAPI.createController(element, options, callback);`

`69`

`};`

`70`

`</script>`

`71`

`</body>`

`72`

`</html>`