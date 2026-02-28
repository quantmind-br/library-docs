---
title: Display your Spotify profile data in a web app
url: https://developer.spotify.com/documentation/web-api/howtos/web-app-profile
source: crawler
fetched_at: 2026-02-27T23:45:24.655152-03:00
rendered_js: true
word_count: 1902
summary: This guide provides step-by-step instructions for building a client-side application that authenticates users via the Spotify Web API using the PKCE authorization flow. It demonstrates how to retrieve and display a user's profile information using TypeScript or JavaScript.
tags:
    - spotify-web-api
    - pkce-auth
    - oauth2
    - typescript
    - javascript
    - user-profile
    - web-apps
category: tutorial
---

This guide creates a simple client-side application that uses the Spotify Web API to get user profile data. We'll show both TypeScript and JavaScript code snippets, make sure to use the code that is correct for your application.

External applications can use the Spotify Web API to retrieve Spotify content, such as song data, album data and playlists. However, in order to access user-related data with the Spotify Web API, an application must be authorized by the user to access that particular information.

## Prerequisites

To work through this guide you'll need:

- A [Node.js LTS](https://nodejs.org/en/) environment or later.
- [npm](https://docs.npmjs.com/) version 7 or later
- A [Spotify account](https://accounts.spotify.com/)

## Set up your account

Login to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard). If necessary, accept the latest [Developer Terms of Service](https://developer.spotify.com/terms) to complete your account set up.

## Creating a Spotify app

We will need to register a new app to generate valid credentials - we'll use these credentials later to perform API calls. Follow the [apps guide](https://developer.spotify.com/documentation/web-api/concepts/apps) to learn how to create an app and generate the necessary credentials.

Once you've created your app, make a note of your `client_id`.

## Creating a new project

This app uses [Vite](https://vitejs.dev/) as a development server. We'll scaffold a new project with the Vite `create` command and use their default template to give us a basic app:

`1`

`npm create vite@latest spotify-profile-demo -- --template vanilla-ts`

Select `y` when it prompts you to install Vite.

Change directory to the new app directory that Vite just created and start the development server:

`1`

`cd spotify-profile-demo`

`2`

`npm install`

`3`

`npm run dev`

The default Vite template creates some files that we won't need for this demo, so you can delete all of the files in `./src/` and `./public/`

### Creating the user interface

This demo is going to be a single page application that runs entirely in the browser. We're going to replace the provided `index.html` file with a simple HTML page that constitutes the user interface to display the user's profile data.

Start by deleting the content of the `index.html` file and replacing it with a `html` and `head` tag that references a TypeScript/JavaScript file (`src/script.ts`, or `src/script.js`, we'll create this file later).

`1`

`<!DOCTYPE html>`

`2`

`<html lang="en">`

`3`

`<head>`

`4`

`<meta charset="utf-8">`

`5`

`<title>My Spotify Profile</title>`

`6`

`<script src="src/script.ts" type="module"></script>`

`7`

`</head>`

`8`

`<body>`

`9`

`10`

`</body>`

`11`

`</html>`

`12`

`13`

`<!-- Note- We're referring directly to the TypeScript file,`

`14`

``and we're using the `type="module"` attribute.``

`15`

`Vite will transpile our TypeScript to JavaScript`

`16`

`so that it can run in the browser. -->`

Inside the `body`, we'll add some markup to display the profile data:

`1`

`<h1>Display your Spotify profile data</h1>`

`2`

`3`

`<section id="profile">`

`4`

`<h2>Logged in as <span id="displayName"></span></h2>`

`5`

`<span id="avatar"></span>`

`6`

`<ul>`

`7`

`<li>User ID: <span id="id"></span></li>`

`8`

`<li>Email: <span id="email"></span></li>`

`9`

`<li>Spotify URI: <a id="uri" href="#"></a></li>`

`10`

`<li>Link: <a id="url" href="#"></a></li>`

`11`

`<li>Profile Image: <span id="imgUrl"></span></li>`

`12`

`</ul>`

`13`

`</section>`

Some elements in this block have `id` attributes. We'll use these to replace the element's text with the data we fetch from the Web API.

### Calling the Web API

We're going to use the Web API to get the user's profile data. We'll use the [authorization code flow with PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow) to get an access token, and then use that token to call the API.

### How it works

- When the page loads, we'll check if there is a code in the callback query string
- If we don't have a code, we'll redirect the user to the Spotify authorization page.
- Once the user authorizes the application, Spotify will redirect the user back to our application, and we'll read the code from the query string.
- We will use the code to request an access token from the Spotify token API
- We'll use the access token to call the Web API to get the user's profile data.
- We'll populate the user interface with the user's profile data.

Create a `src/script.ts` or `src/script.js` file and add the following code:

`1`

`const clientId = "your-client-id-here"; // Replace with your client id`

`2`

`const code = undefined;`

`3`

`4`

`if (!code) {`

`5`

`redirectToAuthCodeFlow(clientId);`

`6`

`} else {`

`7`

`const accessToken = await getAccessToken(clientId, code);`

`8`

`const profile = await fetchProfile(accessToken);`

`9`

`populateUI(profile);`

`10`

`}`

`11`

`12`

`async function redirectToAuthCodeFlow(clientId: string) {`

`13`

`// TODO: Redirect to Spotify authorization page`

`14`

`}`

`15`

`16`

`async function getAccessToken(clientId: string, code: string) {`

`17`

`// TODO: Get access token for code`

`18`

`}`

`19`

`20`

`async function fetchProfile(token: string): Promise<any> {`

`21`

`// TODO: Call Web API`

`22`

`}`

`23`

`24`

`function populateUI(profile: any) {`

`25`

`// TODO: Update UI with profile data`

`26`

`}`

This is the outline of our application.

On the first line there is a `clientId` variable - you'll need to set this variable to the `client_id` of the Spotify app you created earlier.

The code now needs to be updated to redirect the user to the Spotify authorization page. To do this, let's write the `redirectToAuthCodeFlow` function:

`1`

`export async function redirectToAuthCodeFlow(clientId: string) {`

`2`

`const verifier = generateCodeVerifier(128);`

`3`

`const challenge = await generateCodeChallenge(verifier);`

`4`

`5`

`localStorage.setItem("verifier", verifier);`

`6`

`7`

`const params = new URLSearchParams();`

`8`

`params.append("client_id", clientId);`

`9`

`params.append("response_type", "code");`

`10`

`params.append("redirect_uri", "http://127.0.0.1:5173/callback");`

`11`

`params.append("scope", "user-read-private user-read-email");`

`12`

`params.append("code_challenge_method", "S256");`

`13`

`params.append("code_challenge", challenge);`

`14`

`15`

``document.location = `https://accounts.spotify.com/authorize?${params.toString()}`;``

`16`

`}`

`17`

`18`

`function generateCodeVerifier(length: number) {`

`19`

`let text = '';`

`20`

`let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';`

`21`

`22`

`for (let i = 0; i < length; i++) {`

`23`

`text += possible.charAt(Math.floor(Math.random() * possible.length));`

`24`

`}`

`25`

`return text;`

`26`

`}`

`27`

`28`

`async function generateCodeChallenge(codeVerifier: string) {`

`29`

`const data = new TextEncoder().encode(codeVerifier);`

`30`

`const digest = await window.crypto.subtle.digest('SHA-256', data);`

`31`

`return btoa(String.fromCharCode.apply(null, [...new Uint8Array(digest)]))`

`32`

`.replace(/\+/g, '-')`

`33`

`.replace(/\//g, '_')`

`34`

`.replace(/=+$/, '');`

`35`

`}`

In this function, a new `URLSearchParams` object is created, and we add the `client_id`, `response_type`, `redirect_uri` and `scope` parameters to it. The scope parameter is a [list of permissions](https://developer.spotify.com/documentation/web-api/concepts/scopes) that we're requesting from the user. In this case, we're requesting the `user-read-private` and `user-read-email` scopes - these are the scopes that allow us to fetch the user's profile data.

The `redirect_uri` parameter is the URL that Spotify will redirect the user back to after they've authorized the application. In this case, we're using a URL that points to our local Vite dev server.

*You need to make sure this URL is listed in the Redirect URIs section of your Spotify Application Settings in your Developer Dashboard.*

![Edit settings to add your Redirect URI to your app](https://developer-assets.spotifycdn.com/images/documentation/web-api/add-redirect-uri.png)

You will also notice that we are generating [PKCE verifier and challenge data](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow), we're using this to verify that our request is authentic. We're using local storage to store the verifier data, which works like a password for the token exchange process.

To prevent the user from being stuck in a redirect loop when they authenticate, we need to check if the callback contains a `code` parameter. To do this, the first three lines of code in the file are modified like this:

`1`

`const clientId = "your_client_id";`

`2`

`const params = new URLSearchParams(window.location.search);`

`3`

`const code = params.get("code");`

`4`

`5`

`if (!code) {`

`6`

`redirectToAuthCodeFlow(clientId);`

`7`

`} else {`

`8`

`const accessToken = await getAccessToken(clientId, code);`

`9`

`const profile = await fetchProfile(accessToken);`

`10`

`populateUI(profile);`

`11`

`}`

In order to make sure that the token exchange works, we need to write the `getAccessToken` function.

`1`

`export async function getAccessToken(clientId: string, code: string): Promise<string> {`

`2`

`const verifier = localStorage.getItem("verifier");`

`3`

`4`

`const params = new URLSearchParams();`

`5`

`params.append("client_id", clientId);`

`6`

`params.append("grant_type", "authorization_code");`

`7`

`params.append("code", code);`

`8`

`params.append("redirect_uri", "http://127.0.0.1:5173/callback");`

`9`

`params.append("code_verifier", verifier!);`

`10`

`11`

`const result = await fetch("https://accounts.spotify.com/api/token", {`

`12`

`method: "POST",`

`13`

`headers: { "Content-Type": "application/x-www-form-urlencoded" },`

`14`

`body: params`

`15`

`});`

`16`

`17`

`const { access_token } = await result.json();`

`18`

`return access_token;`

`19`

`}`

In this function, we load the verifier from local storage and using both the code returned from the callback and the verifier to perform a POST to the Spotify token API. The API uses these two values to verify our request and it returns an access token.

Now, if we run `npm run dev`, and navigate to [http://127.0.0.1:5173](http://127.0.0.1:5173) in a browser, we'll be redirected to the Spotify authorization page. If we authorize the application, we'll be redirected back to our application, but no data will be fetched and displayed.

To fix this, we need to update the `fetchProfile` function to call the Web API and get the profile data. Update the `fetchProfile` function:

`1`

`async function fetchProfile(token: string): Promise<any> {`

`2`

`const result = await fetch("https://api.spotify.com/v1/me", {`

`3`

``method: "GET", headers: { Authorization: `Bearer ${token}` }``

`4`

`});`

`5`

`6`

`return await result.json();`

`7`

`}`

In this function, a call is made to `https://api.spotify.com/v1/me` using the browser's [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) to get the profile data. The `Authorization` header is set to `Bearer ${token}`, where `token` is the access token that we got from the `https://accounts.spotify.com/api/token` endpoint.

If we add a `console.log` statement to the calling code we can see the profile data that is returned from the API in the browser's console:

`1`

`} else {`

`2`

`const profile = await fetchProfile(token);`

`3`

`console.log(profile); // Profile data logs to console`

`4`

`...`

`5`

`}`

Finally, we need to update the `populateUI` function to display the profile data in the UI. To do this, we'll use the DOM to find our HTML elements and update them with the profile data:

`1`

`function populateUI(profile: any) {`

`2`

`document.getElementById("displayName")!.innerText = profile.display_name;`

`3`

`if (profile.images[0]) {`

`4`

`const profileImage = new Image(200, 200);`

`5`

`profileImage.src = profile.images[0].url;`

`6`

`document.getElementById("avatar")!.appendChild(profileImage);`

`7`

`}`

`8`

`document.getElementById("id")!.innerText = profile.id;`

`9`

`document.getElementById("email")!.innerText = profile.email;`

`10`

`document.getElementById("uri")!.innerText = profile.uri;`

`11`

`document.getElementById("uri")!.setAttribute("href", profile.external_urls.spotify);`

`12`

`document.getElementById("url")!.innerText = profile.href;`

`13`

`document.getElementById("url")!.setAttribute("href", profile.href);`

`14`

`document.getElementById("imgUrl")!.innerText = profile.images[0]?.url ?? '(no profile image)';`

`15`

`}`

You can now run your code by running `npm run dev` in the terminal and navigating to `http://127.0.0.1:5173` in your browser.

![Your profile data will display as a heading with your name, show your avatar image and then list your profile details](https://developer-assets.spotifycdn.com/images/documentation/web-api/profile.png)

At the moment, even though we're using TypeScript, we don't have any type safety around the data being returned from the Web API. To improve this, we can create a `UserProfile` interface to describes the data that we expect to be returned from the API. Adding an interface will define the shape of the object that we're expecting, this will make using the data type-safe and will allow for type prompts while coding, making a more pleasant developer experience if you extend this project in future.

To do this, create a new file called `types.d.ts` in the `src` folder and add the following code:

`1`

`interface UserProfile {`

`2`

`country: string;`

`3`

`display_name: string;`

`4`

`email: string;`

`5`

`explicit_content: {`

`6`

`filter_enabled: boolean,`

`7`

`filter_locked: boolean`

`8`

`},`

`9`

`external_urls: { spotify: string; };`

`10`

`followers: { href: string; total: number; };`

`11`

`href: string;`

`12`

`id: string;`

`13`

`images: Image[];`

`14`

`product: string;`

`15`

`type: string;`

`16`

`uri: string;`

`17`

`}`

`18`

`19`

`interface Image {`

`20`

`url: string;`

`21`

`height: number;`

`22`

`width: number;`

`23`

`}`

We can now update our calling code to expect these types:

`1`

`async function fetchProfile(token: string): Promise<UserProfile> {`

`2`

`// ...`

`3`

`}`

`4`

`5`

`function populateUI(profile: UserProfile) {`

`6`

`// ...`

`7`

`}`

You can view and fork the final code for this demo on GitHub: [Get User Profile Repository](https://github.com/spotify/web-api-examples/tree/master/get_user_profile).