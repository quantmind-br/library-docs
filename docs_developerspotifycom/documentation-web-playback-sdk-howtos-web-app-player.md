---
title: Building a Spotify Player inside a Web app
url: https://developer.spotify.com/documentation/web-playback-sdk/howtos/web-app-player
source: crawler
fetched_at: 2026-02-27T23:40:16.210945-03:00
rendered_js: true
word_count: 3211
summary: A step-by-step tutorial for building a full-stack web application that integrates the Spotify Web Playback SDK using React and Node.js to create a custom browser-based music player.
tags:
    - spotify-api
    - web-playback-sdk
    - react
    - node-js
    - authentication
    - express-js
    - javascript
category: tutorial
---

The following how-to will lead you to step by step create a simple full-stack application to host the Spotify player to play music along with the rest of the devices from your home. By the end of the how-to, you will have a fully working Spotify Player running on your browser similar to this one:

![Final Player](https://developer-assets.spotifycdn.com/images/documentation/web-playback-sdk/guide_final_player.png)

Let's start coding!

## Prerequisites

The Web Playback SDK requires Spotify Premium, so you'll need a premium account to use it.

This how-to assumes that you have some knowledge of JavaScript -both frontend using [React](https://reactjs.org/) and backend with [Node](https://nodejs.org/).

Although not fully necessary, it is highly recommended to read the [Quick Start Guide](https://developer.spotify.com/documentation/web-playback-sdk/tutorials/getting-started) before this how-to.

## Source Code

The source code of the application can be found on the [Spotifty GitHub repository](https://github.com/spotify/spotify-web-playback-sdk-example). Feel free to fork it if you feel like it!

## Set up your Account

Go to [Spotify for Developers](https://developer.spotify.com/) portal and log in using your Spotify credentials (You can find the login button under the [Dashboard](https://developer.spotify.com/dashboard)).

The dashboard is where we can create apps, control the API credentials bound to the app or just get some nice app usage statistics. Click on the *Create an APP* button and provide a name and a short description of your new application. Finally, accept the terms and conditions and click on *Create*. Your new application contains your *Client ID* and *Client Secret* needed to authorize the application we are about to code to use the Spotify resources.

## Initializing the Project

The easiest way to start a project based on React is using the [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app) tool. Open a terminal and run the tool using the `npx` command:

`1`

`npx create-react-app spotify-web-player`

`2`

`cd spotify-web-player`

`npx` is pre-bundled with `npm` since 5.2.0 version. The command creates a new folder called `spotify-web-player` that we will use as a template for our project, along with the `package.json` file which contains the project configuration.

Let's install the dependencies and test the project by running:

`1`

`npm install`

`2`

`HOST=127.0.0.1 npm run start`

Go to your browser and open `http://127.0.0.1:3000`. If you see a spinning React logo, then the React project is ready.

Let's create a `server` folder which will contain the implementation of the backend:

Finally, let's add some extra commands to the `package.json` file to properly start the project. Open the `package.json` with your favorite editor and add the following entries inside the `script` section of the file:

`1`

`"scripts": {`

`2`

`"start": "HOST=127.0.0.1 react-scripts start",`

`3`

`"build": "react-scripts build",`

`4`

`"server": "HOST=127.0.0.1 node server",`

`5`

`"dev": "run-p server start"`

`6`

`},`

Each entry corresponds with the following actions:

- `start` starts an HTTP server on port 3000 to serve the React application.
- `build` generates the static code ready to be deployed in production.
- `server` executes the `index.js` file located on the `server` folder.
- `dev` runs both client and server up using `run-p` tool to allow run multiple npm-scripts in parallel.

The `run-p` command belongs to the `npm-run-all` package. Let's install the dependency by running the following command:

`1`

`npm install npm-run-all --save-dev`

Now that the project is ready, let's move forward and start coding the backend's authorization.

Spotify allows developers to authenticate in [several ways](https://developer.spotify.com/documentation/web-api/concepts/authorization). Our project will implement the [Authorization Code flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow), which is very convenient for long-running apps, such as web apps, where the user grants permissions only once.

Rather than hard-coding the user credentials inside the source code of our application, we are going to use the `dotenv` package to store and read them from a hidden configuration file.

Install the dependency with the following command:

`1`

`npm install dotenv --save-dev`

Create a `.env` file in the root folder of the project and add the following variables using the `NAME=VALUE` format:

`1`

`SPOTIFY_CLIENT_ID='my_spotify_client_id'`

`2`

`SPOTIFY_CLIENT_SECRET='my_spotify_client_secret'`

The values are now accessible as environment variables and can be read using `process.env`:

`1`

`var spotify_client_id = process.env.SPOTIFY_CLIENT_ID`

`2`

`var spotify_client_secret = process.env.SPOTIFY_CLIENT_SECRET`

The idea behind the server is to export some basic endpoints to the frontend corresponding to the steps of the authorization flow:

- `/auth/login` to *request user authorization* by getting an *Authorization Code*.
- `/auth/callback` to *request the Access Token* using the *Authorization Code* requested in the previous step.

We will use [Express](https://expressjs.com/) to receive and handle all incoming requests to the server. Let's start by installing the package dependency:

`1`

`npm install express --save-dev`

Create a new `index.js` file inside the `server` folder with the following content:

`1`

`const express = require('express')`

`2`

`const dotenv = require('dotenv');`

`3`

`4`

`const port = 5000`

`5`

`6`

`dotenv.config()`

`7`

`8`

`var spotify_client_id = process.env.SPOTIFY_CLIENT_ID`

`9`

`var spotify_client_secret = process.env.SPOTIFY_CLIENT_SECRET`

`10`

`11`

`var app = express();`

`12`

`13`

`app.get('/auth/login', (req, res) => {`

`14`

`});`

`15`

`16`

`app.get('/auth/callback', (req, res) => {`

`17`

`});`

`18`

`19`

`app.listen(port, () => {`

`20`

``console.log(`Listening at http://127.0.0.1:${port}`)``

`21`

`})`

We can test the server with the following command:

If everything goes fine, the server will start listening incoming requests on port 5000.

We are ready to start coding the authorization flow!

### Request User Authorization

The first step is to redirect the user to a web page where they can choose to grant our application access to their premium account.

To do so, we need to send a `GET` request to the `/authorize` endpoint of the Spotify account service with the following parameters:

- `response_type`, is the credential that will be returned. The value will always be `code`.
- `client_id`, is the Client ID of the application we have just created on the portal dashboard.
- `scope`, a space-separated list of actions that our app can be allowed to do on a user's behalf. We need permission for `streaming`, `user-read-email` and `user-read-private` for the Web Player SDK.
- `redirect_uri` is the URL that Spotify's Authorization server will redirect once the access token is granted. Since we are running the project locally, our redirect URL will point to `127.0.0.1:3000/auth/callback` since all petitions are handled from the frontend.
- `state`, a randomly generated string to protect against attacks such as cross-site request forgery.

Although `state` is not mandatory, is highly recommended including one. Here you have our proposal to generate randomly generated strings. Of course, feel free to implement something different:

`1`

`var generateRandomString = function (length) {`

`2`

`var text = '';`

`3`

`var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';`

`4`

`5`

`for (var i = 0; i < length; i++) {`

`6`

`text += possible.charAt(Math.floor(Math.random() * possible.length));`

`7`

`}`

`8`

`return text;`

`9`

`};`

We have everything we need to implement the user authorization request. The following code implements the `GET` method, which performs the redirection to the Spotify login screen to allow users to grant permissions:

`1`

`router.get('/auth/login', (req, res) => {`

`2`

`3`

`var scope = "streaming \`

`4`

`user-read-email \`

`5`

`user-read-private"`

`6`

`7`

`var state = generateRandomString(16);`

`8`

`9`

`var auth_query_parameters = new URLSearchParams({`

`10`

`response_type: "code",`

`11`

`client_id: spotify_client_id,`

`12`

`scope: scope,`

`13`

`redirect_uri: "http://127.0.0.1:3000/auth/callback",`

`14`

`state: state`

`15`

`})`

`16`

`17`

`res.redirect('https://accounts.spotify.com/authorize/?' + auth_query_parameters.toString());`

`18`

`})`

#### Response

Once the user approves the application request, the user is redirected back to the application using the `redirect_uri` passed on the authorized request `http://127.0.0.1:3000/auth/callback` just described above.

The callback contains two query parameters:

- An authorization `code` that will be exchanged for an access token.
- The same `state` supplied in the request.

Before continuing with the second step, we need to go back to the portal to allow our application to perform callbacks to the `redirect_uri` we have supplied on the previous call:

- Go to the *Dashboard* and select the application we created on the first step.
- Click on *Edit Settings* and add the URL callback `http://127.0.0.1:3000/auth/callback` under the *Redirect URIs* field.

![Register Callback](https://developer-assets.spotifycdn.com/images/documentation/web-playback-sdk/register_callback.png)

**Remember to click save for the changes to take effect.**

### Request Access Token

Now that we have the authorization code, we must exchange it for tokens. Using the `code` from the previous step, we need to make a `POST` request to the `/api/token` endpoint.

The body of the request must be encoded in `application/x-www-form-urlencoded` with the following parameters:

- `grant_type`, must always contain the value `authorization_code`.
- `code`, is the authorization code returned on the previous step.
- `redirect_uri`, must exactly match the same value sent on the user authorization request (previous step). This value is used for validation only since there is no actual redirection.

We must also include the following HTTP headers:

- `Authorization`, is a base64 encoded string that contains the client ID and client secret keys. The field must have the format: `Basic *<base64 encoded client_id:client_secret>*`
- `Content-type`, set with the value `application/x-www-form-urlencoded` to inform the server about the encoding of the body.

As the `POST` HTTP call will be made using the `request` library, we need to install the dependency:

`1`

`npm install request --save-dev`

We are now ready to implement the `/auth/callback` endpoint of our server:

`1`

`app.get('/auth/callback', (req, res) => {`

`2`

`3`

`var code = req.query.code;`

`4`

`5`

`var authOptions = {`

`6`

`url: 'https://accounts.spotify.com/api/token',`

`7`

`form: {`

`8`

`code: code,`

`9`

`redirect_uri: "http://127.0.0.1:3000/auth/callback",`

`10`

`grant_type: 'authorization_code'`

`11`

`},`

`12`

`headers: {`

`13`

`'Authorization': 'Basic ' + (Buffer.from(spotify_client_id + ':' + spotify_client_secret).toString('base64')),`

`14`

`'Content-Type' : 'application/x-www-form-urlencoded'`

`15`

`},`

`16`

`json: true`

`17`

`};`

`18`

`19`

`request.post(authOptions, function(error, response, body) {`

`20`

`if (!error && response.statusCode === 200) {`

`21`

`var access_token = body.access_token;`

`22`

`res.redirect('/')`

`23`

`}`

`24`

`});`

`25`

`})`

Note how the authentication ends with the `access_token` stored locally and redirection to `/`.

#### Response

If everything goes well, we will receive an `HTTP 200` response with the `access_token` in the payload of the response:

`1`

`{`

`2`

`"access_token":"BQBZiiCqVjpZz9Boj1-8WirXFLgBpfZJwSR0Kw",`

`3`

`"token_type":"Bearer",`

`4`

`"expires_in":3600,`

`5`

`"refresh_token":"AQC-JL7jaByIRKwZiFb29Tf_2AlF1qs",`

`6`

`"scope":"streaming user-read-email user-read-private"`

`7`

`}`

### Return Access Token

The backend implements the `/auth/token` endpoint to return the access token in JSON format. The code looks like this:

`1`

`app.get('/auth/token', (req, res) => {`

`2`

`res.json(`

`3`

`{`

`4`

`access_token: access_token`

`5`

`})`

`6`

`})`

This access token will be used to instantiate the *Web Playback SDK* and, eventually, perform API calls using the [Web APIs](https://developer.spotify.com/documentation/web-api).

## Proxying Backend Requests

During the development phase, our React app and backend will run on different hosts and ports:

- The client runs on `127.0.0.1:3000`
- The backend runs on `127.0.0.1:5000`

Thus, we need to tell our React app where to find the server when doing API calls such as `/auth/login` or `/auth/token`.

There are different approaches to do so:

- Use the canonical URI on every API call.
- Adding a `proxy` field to the `package.json` file: `"proxy": "http://127.0.0.1:5000"`.
- Set up our own proxy using the `http-proxy-middleware` package.

Let's include the package in our project by doing:

`1`

`npm install http-proxy-middleware --save-dev`

Now, add a new file called `setupProxy.js` to the `src` folder with the following content:

`1`

`module.exports = function (app) {`

`2`

``app.use(proxy(`/auth/**`, {``

`3`

`target: 'http://127.0.0.1:5000'`

`4`

`}));`

`5`

`};`

This way, all petitions with the `/auth/**` pattern will be redirected to the backend.

## React Components

### Login Component

Let's start by implementing a welcome screen with a nice *Login in* button to start the authorization flow we have just implemented on the backend side.

Open the `src/App.js` and replace the current implementation with this one:

`1`

`import React, { useState, useEffect } from 'react';`

`2`

`import WebPlayback from './WebPlayback'`

`3`

`import Login from './Login'`

`4`

`import './App.css';`

`5`

`6`

`function App() {`

`7`

`8`

`const [token, setToken] = useState('');`

`9`

`10`

`useEffect(() => {`

`11`

`12`

`async function getToken() {`

`13`

`const response = await fetch('/auth/token');`

`14`

`const json = await response.json();`

`15`

`setToken(json.access_token);`

`16`

`}`

`17`

`18`

`getToken();`

`19`

`20`

`}, []);`

`21`

`22`

`return (`

`23`

`<>`

`24`

`{ (token === '') ? <Login/> : <WebPlayback token={token} /> }`

`25`

`</>`

`26`

`);`

`27`

`}`

`28`

`29`

`export default App;`

The component uses the `useEffect` hook to send a `GET` request to the `/auth/token` endpoint to check if we have a valid `access_token` already requested.

Once received, the `access_token` is stored using the `setToken()`, so the component will be rendered according to the following logic:

- The `Login` component will be loaded in case the `access_token` is still empty.
- If the `access_token` has been requested already (there is an active session ongoing), the `WebPlaback` component will load instead, receiving the `access_token` we have just requested.

Let's take a look at the `Login` component:

`1`

`2`

`import React from 'react';`

`3`

`4`

`function Login() {`

`5`

`return (`

`6`

`<div className="App">`

`7`

`<header className="App-header">`

`8`

`<a className="btn-spotify" href="/auth/login" >`

`9`

`Login with Spotify`

`10`

`</a>`

`11`

`</header>`

`12`

`</div>`

`13`

`);`

`14`

`}`

`15`

`16`

`export default Login;`

The login screen consists of one single button inviting users to log in. Once the user clicks on *Login with Spotify*, the component will perform a `GET` operation to `/auth/login` to start the authentication flow described on the previous section.

### WebPlayback Component

Let's create a new component to implement the web player. Create a new file called `Webplayback.jsx` and add a basic new React functional component as follows:

`1`

`import React, { useState, useEffect } from 'react';`

`2`

`3`

`function WebPlayback(props) {`

`4`

`5`

`return (`

`6`

`<>`

`7`

`<div className="container">`

`8`

`<div className="main-wrapper">`

`9`

`10`

`</div>`

`11`

`</div>`

`12`

`</>`

`13`

`);`

`14`

`}`

`15`

`16`

`export default WebPlayback`

Add the `useEffect` hook so the instance of the **Web Playback SDK** object is created right before we render the page for the first time:

`1`

`2`

`useEffect(() => {`

`3`

`4`

`const script = document.createElement("script");`

`5`

`script.src = "https://sdk.scdn.co/spotify-player.js";`

`6`

`script.async = true;`

`7`

`8`

`document.body.appendChild(script);`

`9`

`10`

`window.onSpotifyWebPlaybackSDKReady = () => {`

`11`

`12`

`const player = new window.Spotify.Player({`

`13`

`name: 'Web Playback SDK',`

`14`

`getOAuthToken: cb => { cb(props.token); },`

`15`

`volume: 0.5`

`16`

`});`

`17`

`18`

`setPlayer(player);`

`19`

`20`

`player.addListener('ready', ({ device_id }) => {`

`21`

`console.log('Ready with Device ID', device_id);`

`22`

`});`

`23`

`24`

`player.addListener('not_ready', ({ device_id }) => {`

`25`

`console.log('Device ID has gone offline', device_id);`

`26`

`});`

`27`

`28`

`29`

`player.connect();`

`30`

`31`

`};`

`32`

`}, []);`

The first step to install the SDK is to load the library creating a new `script` tag within the DOM tree. As the `onSpotifyWebPlaybackSDKReady` method will be executed right after the **Web Playback SDK** has been successfully loaded, we create the `Player` instance inside the callback using the `access_token` supplied via React `props`

Once the `Player` object has been successfully created, we store the object using the `userPlayer()` hook, which has been defined as follows:

`1`

`const [player, setPlayer] = useState(undefined);`

The callback also connects the events emitted by the SDK using the [addListener](https://developer.spotify.com/documentation/web-playback-sdk/reference#spotifyplayeraddlistener) method of the player. You can find detailed information about the events supported by the SDK on the [SDK reference page](https://developer.spotify.com/documentation/web-playback-sdk/reference)

The events we want to get notified are:

- [ready](https://developer.spotify.com/documentation/web-playback-sdk/reference#ready), emitted when the SDK is connected and ready to stream content.
- [not\_ready](https://developer.spotify.com/documentation/web-playback-sdk/reference#not_ready), in case the connection is broken.
- [player\_state\_changed](https://developer.spotify.com/documentation/web-playback-sdk/reference#player_state_changed), emitted when the state of the local playback has changed (i.e., change of track).

Finally, the method calls to [connect](https://developer.spotify.com/documentation/web-playback-sdk/reference#spotifyplayerconnect) method to perform the connection of our new Spotify instance.

### Running everything together

At this point we are ready to test the application:

1. Open a console and run the both client and server using the `npm run dev` command.
2. Open a browser and go to `http://127.0.0.1:3000`.
3. Click on the "Log in with Spotify" button.
4. Log in to Spotify using your credentials if you haven't done it yet.
5. Open any Spotify client. You should be able to see a new Spotify instance in the [Spotify connect](https://developer.spotify.com/documentation/web-playback-sdk/concepts/spotify-connect) button.
6. If you switch to the new instance, the music should start playing within the browser.

Congrats! The first step has been successfully accomplished! What about displaying some cool information about the stream currently playing, such as artist, track or album cover?

### Playback Information Display

Let's modify our `WebPlayback` component to store and display information about the track that is currently playing. Add the following hooks to the component:

`1`

`const [is_paused, setPaused] = useState(false);`

`2`

`const [is_active, setActive] = useState(false);`

`3`

`const [current_track, setTrack] = useState(track);`

- `is_paused` is a boolean variable that indicates whether the current track is being played or not.
- `is_active` to indicate whether the current playback has been transferred to this player or not.
- `current_track`, an object to store the currently playing track.

Next step, we need to define the `track` JSON object. Add the following code outside the component implementation:

`1`

`const track = {`

`2`

`name: "",`

`3`

`album: {`

`4`

`images: [`

`5`

`{ url: "" }`

`6`

`]`

`7`

`},`

`8`

`artists: [`

`9`

`{ name: "" }`

`10`

`]`

`11`

`}`

Extend the `useEffect()` hook by adding a new `eventListener` to, once the event is emitted, update the component with the current track

`1`

`player.addListener('player_state_changed', ( state => {`

`2`

`3`

`if (!state) {`

`4`

`return;`

`5`

`}`

`6`

`7`

`setTrack(state.track_window.current_track);`

`8`

`setPaused(state.paused);`

`9`

`10`

`11`

`player.getCurrentState().then( state => {`

`12`

`(!state)? setActive(false) : setActive(true)`

`13`

`});`

`14`

`15`

`}));`

Finally, let's display information about the track the user is currently playing. Replace the `render` method with the following code:

`1`

`return (`

`2`

`<>`

`3`

`<div className="container">`

`4`

`<div className="main-wrapper">`

`5`

`<img src={current_track.album.images[0].url}`

`6`

`className="now-playing__cover" alt="" />`

`7`

`8`

`<div className="now-playing__side">`

`9`

`<div className="now-playing__name">{`

`10`

`current_track.name`

`11`

`}</div>`

`12`

`13`

`<div className="now-playing__artist">{`

`14`

`current_track.artists[0].name`

`15`

`}</div>`

`16`

`</div>`

`17`

`</div>`

`18`

`</div>`

`19`

`</>`

`20`

`)`

### Playback Control

Once the playback is transferred to the browser, there is no way to modify the state of the playback, e.g. move to the next or previous tracks or pause/resume the playback.

Let's add three new buttons to the `WebPlayback` component that will call to [nextTrack()](https://developer.spotify.com/documentation/web-playback-sdk/reference#spotifyplayernexttrack), [previousTrack()](https://developer.spotify.com/documentation/web-playback-sdk/reference#spotifyplayerprevioustrack), and [togglePlay()](https://developer.spotify.com/documentation/web-playback-sdk/reference#spotifyplayertoggleplay) methods from the SDK:

`1`

`<button className="btn-spotify" onClick={() => { player.previousTrack() }} >`

`2`

`&lt;&lt;`

`3`

`</button>`

`4`

`5`

`<button className="btn-spotify" onClick={() => { player.togglePlay() }} >`

`6`

`{ is_paused ? "PLAY" : "PAUSE" }`

`7`

`</button>`

`8`

`9`

`<button className="btn-spotify" onClick={() => { player.nextTrack() }} >`

`10`

`&gt;&gt;`

`11`

`</button>`

## Preparing for Production

There are different approaches to roll out your React application in production along with the backend server. In this how-to, we will cover the manual steps to build and place the code into one single folder.

Let's start by generating the React app and all the static assets:

If everything went fine, a new `build` folder will be generated containing all the generated files. You can check that the application works fine by using the `serve` HTTP server to serve the static files:

`1`

`npm install -g serve`

`2`

`serve -s build`

As we will be using the React server we have implemented through the how-to, we need to extend the backend server to serve static files. Open the `server/index.js` file and add the following line:

`1`

`app.use(express.static(path.join(__dirname, '../build')));`

From now on, we can run the server and load files directly from the server, for example:

`1`

`http://127.0.0.1:5000/index.html`

`2`

`http://127.0.0.1:5000/static/js/main.js`

## Next Steps

If you have reached this point, congratulations! Your first Spotify instance is up and running!

But this is just the beginning! What could we do next? Here you have some ideas to add to the prototype:

- Use the `refresh_token` field from the *Request Access Token* response to request a new token once the current one expires.
- Use the [Search](https://developer.spotify.com/documentation/web-api/reference/search) endpoint to include search capabilities by artist, albums, or tracks.
- Include a *Transfer Playback* button to transfer the current playback to another Spotify instance using the [Get Playback State](https://developer.spotify.com/documentation/web-api/reference/get-information-about-the-users-current-playback) endpoint.
- Get and play any of your favourite playlists using the [Get Playlist](https://developer.spotify.com/documentation/web-api/reference/get-playlist) endpoint.