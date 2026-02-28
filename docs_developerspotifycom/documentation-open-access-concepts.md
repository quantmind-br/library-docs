---
title: Open Access Concepts | Spotify for Developers
url: https://developer.spotify.com/documentation/open-access/concepts#entitlements
source: crawler
fetched_at: 2026-02-27T23:40:51.351411-03:00
rendered_js: true
word_count: 1160
summary: This document outlines the technical requirements and core concepts for integrating with the Spotify Open Access API, specifically focusing on account linking, identifier management, and secure authentication flows.
tags:
    - spotify-open-access
    - account-linking
    - oauth-2-0
    - api-security
    - jws-authentication
    - partner-integration
    - access-control
category: guide
---

## Client ID

The OAuth 2.0 Client ID is provided by Spotify’s OAuth server, which is used for accessing the Spotify Open Access API. A single Client ID can own and control multiple Partner IDs.

Client IDs should be created and managed by the partners themselves through the [dashboard](https://developer.spotify.com/dashboard). Creating a Client ID also generates a Client Secret. The client secret is needed to access the API and should not be shared with users, browsers or client software. The new Client ID must be allow-listed by the Spotify Partner Management team before it can be used with the Spotify Open Access API.

Contact the Spotify Partner Management team and provide the Client ID. They will register your Client ID as an Open Access partner and return a Partner ID to you.

## Partner ID

The Partner ID identifies a Spotify Open Access Partner. Spotify will issue a Partner ID during the onboarding process when registering your Client ID (see below).

Accounts are linked per Partner ID.

## Partner user ID

The Partner User ID is a partner-defined, unique, and never reassigned user identifier, intended to be consumed by Spotify. The format of a Partner User ID is a lower case string between 16 and 128 hexadecimal characters in length (inclusive). This could be, for example, a UUID (without dashes or curly braces) or a hash digest. The Partner User ID should not contain any personally identifiable information.

Partner User IDs are namespaced by Partner ID.

## Entitlements

Entitlements are identifiers that the partner defines and assigns to users and episodes. An episode is playable if the user and the episode have at least one entitlement identifier in common.

Entitlements are namespaced by Partner ID.

## Completion URL

The response from the `/v1/register-user` endpoint contains a Completion URL. After successfully registering the user, the partner must forward the user to this URL using an HTTP 302 redirect. The linking flow completes after Spotify loads the user’s personalized landing page. This page lists the shows that are unlocked for the user and, if the linking flow starts by passing a Spotify show URI, it displays the relevant show at the top.

## Entrypoint URL

Each partner should provide an Entrypoint URL, used to bring the user into the account linking flow. The Entrypoint URL will be used to initiate the account linking flow from Spotify surfaces.

An example of this could be `https://partner.com/link-with-spotify`. When a user is sent to this URL the following should happen (see Figure 1 above):

1. Check if the user is authenticated/logged in to your website. If not, the user should get redirected to an authentication/login flow of your website. When successfully authenticated the user should be redirected to the next step:
2. A Spotify OAuth authorization URL (`https://accounts.spotify.com/authorize&...`) should be generated using the client ID obtained from Spotify and a user-specific state.
3. A redirect (preferably a 302) should be returned with a “Location” header set to the generated URL in point 2. This initiates the authorization code Flow.
4. The partner backend makes a synchronous call to the register-user endpoint using the token acquired in step 2 above.
5. The register-user endpoint returns a "completion\_url" upon successful account linking.
6. The user should be redirected to the completion\_url from step 5, which will have a link back into Spotify with the content they have unlocked (assuming entitlements were granted).

## JWT & JWS usage

Unless otherwise stated, the payload of API requests should be a JSON Web Signature (JWS) signed by the sender. Signing the payloads allows Spotify to verify that it is the partner backend making the requests.

The JWT should be signed using the HS256 (HMAC SHA256) algorithm with the client\_secret as the signing key. All request parameters are added to the JWS payload. The entire signed JWS is included as the request payload.

Spotify recommends using a [library](https://jwt.io/libraries) for generating the JWS.

The JWS header should contain the algorithm and type:

`1`

`{`

`2`

`"alg": "HS256",`

`3`

`"typ": "JWT"`

`4`

`}`

The payload should include the fields described for each API call. As an example:

`1`

`{`

`2`

`"partner_id": "0000000000000000000000",`

`3`

`"partner_user_id": "63e6d54b993a447fa1e81d25dd5f09ac",`

`4`

`"entitlements": ["entitlement-1", "entitlement-2"]`

`5`

`}`

The resulting JWS should be encoded with '.' delimiters as is standard.

An example call to the register-user endpoint. The encoded JWS is passed as the request payload:

`1`

`curl -X POST -d 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXJ0bmVyX2lkIjoiMDAwMDAwMDAwMDAwMDAwMDAwMDAwMCIsInBhcnRuZXJfdXNlcl9pZCI6IjYzZTZkNTRiLTk5M2EtNDQ3Zi1hMWU4LTFkMjVkZDVmMDlhYyIsImVudGl0bGVtZW50cyI6WyJlbnRpdGxlbWVudC0xIiwiZW50aXRsZW1lbnQtMiJdfQ.22W1Mp9bDHUzg_KwBAWbT2B8aUvRU_5Kefau6LlLzyw' https://open-access.spotify.com/api/v1/register-user`

## Scopes

Spotify Open Access API uses four OAuth 2.0 scopes. One user-related scope to be used in the authorization code flow, and three service-related scopes to be used with the client credentials flow. A single request must not contain both user-related scopes and service-related scopes.

User-related scope (to be used with the authorization code flow):

- `user-soa-link`

User-related scopes are included in the `https://accounts.spotify.com/authorize` URL using the scope query parameter.

Service-related scopes (to be used with the client credentials flow):

- `soa-manage-entitlements`
- `soa-manage-partner`
- `soa-create-partner`
- `user-soa-unlink`

Service-related scopes are included in the `https://accounts.spotify.com/token` request using the scope query parameter. Multiple scopes can be passed as a space-separated list.

## Spotify show URI

In order to highlight the show that a user-initiated a linking journey from, we will need the corresponding show URI. When a user initiates the linking flow from a Spotify client, Spotify will include a `spotifyShowUri` query parameter that will be stored as a cookie on the spotify.com domain. This cookie has a value of the show URI that the user clicked from one of Spotify’s surfaces. Spotify will later highlight the corresponding show on the success page after a user has linked their accounts. This means that when a user initiates a flow from a Spotify client the partners will not need to take action for the chosen show to be highlighted.

When a user initiates the flow on the partner's site the partner still has the opportunity to highlight the show that the user started the flow with. This show URI needs to be manually added as a query parameter by the partner to the /link URL, for example:

`https://content-access.spotify.com/link/<PartnerID>?spotifyShowUri=spotify:show:<ShowID>`

Partners do not need to take any additional action. Spotify will set the cookie and highlight the show.

In short, an authorized app is used to establish a link, and the link gives access to content. Unlinking does *not* revoke the app authorization, and revoking the app authorization does *not* break the link.

In more detail, when a user successfully goes through a full account linking flow, two new resources will be created:

1. When a user goes through the Authorization Code Flow and consents to sharing their data, the developer app will appear under [https://www.spotify.com/us/account/apps/](https://www.spotify.com/us/account/apps/). This authorization allows the developer app to request an access token, which is required when calling the Register User endpoint to establish a link between accounts. [Read more about the Authorization Code Flow here](https://developer.spotify.com/documentation/web-api/tutorials/code-flow)
2. An account link is the association between a Spotify user and a partner user. As long as this link is active ([read more about Account Unlinking here](https://developer.spotify.com/documentation/open-access/tutorials/account#account-unlinking)), the entitlements associated with that link grant access to content with at least one overlapping entitlement.