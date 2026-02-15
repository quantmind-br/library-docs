---
title: Developer Keys | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/developer_keys
source: sitemap
fetched_at: 2026-02-15T08:58:27.467326-03:00
rendered_js: false
word_count: 1000
summary: Provides an overview of the DeveloperKey object and defines endpoints for listing, creating, updating, and deleting Canvas API keys used for OAuth2 access.
tags:
    - canvas-lms
    - developer-keys
    - oauth2
    - lti-1-3
    - authentication
    - api-management
category: api
---

Manage Canvas API Keys, used for OAuth access to this API. See [the OAuth access docs](https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth) for usage of these keys. Note that DeveloperKeys are also (currently) used for LTI 1.3 registration and OIDC access, but this endpoint deals with Canvas API keys. See [LTI Registration](https://developerdocs.instructure.com/services/canvas/external-tools/lti/file.registration) for details.

**A DeveloperKey object looks like:**

```
// a Canvas API key (or LTI 1.3 registration)
{
  // The Canvas ID of the DeveloperKey object
"id": 1,
  // The display name
"name": "Test Key",
  // Timestamp of the key's creation
"created_at": "2025-05-30T17:09:18Z",
  // Timestamp of the key's last update
"updated_at": "2025-05-30T17:09:18Z",
  // The state of the key
"workflow_state": "active",
  // True if key represents an LTI 1.3 Registration. False for Canvas API keys
"is_lti_key": false,
  // Contact email configured for key
"email": "test@example.com",
  // URL for a small icon to display in key list
"icon_url": "https://example.com/icon.png",
  // User-provided notes about key
"notes": "this key is for testing",
  // User-specified code representing the vendor that uses the key
"vendor_code": "Google",
  // The name of the account that owns the key
"account_name": "Test Account",
  // True for all keys except Site Admin-level keys, which default to false.
  // Controls visibility in the Inherited tab.
"visible": true,
  // List of API endpoints key is allowed to access (API keys), or LTI 1.3 scopes
  // (LTI keys)
"scopes": ["url:GET|/api/v1/accounts"],
  // Deprecated in favor of redirect_uris. Do not use.
"redirect_uri": "no",
  // List of URLs used during OAuth2 flow to validate given redirect URI (API
  // keys), or to redirect to after login (LTI keys)
"redirect_uris": ["https://mytool.com/oauth2/redirect","https://mytool.com/1_3/launch"],
  // (API keys only) The number of active access tokens associated with the key
"access_token_count": 42,
  // (API keys only) The last time an access token for this key was used in an API
  // request
"last_used_at": "2025-05-30T17:09:18Z",
  // (API keys only) If true, key is only usable in non-production environments
  // (test, beta). Avoids problems with beta refresh.
"test_cluster_only": false,
  // (API keys only) If true, allows `includes` parameters in API requests that
  // match the scopes of this key
"allow_includes": true,
  // (API keys only) If true, then token requests with this key must include
  // scopes
"require_scopes": false,
  // (API keys only) Used in OAuth2 client credentials flow to specify the
  // audience for the access token
"client_credentials_audience": "external",
  // (API keys only) The client secret used in the OAuth authorization_code flow.
"api_key": "sd45fg64....",
  // (LTI keys only) The Canvas-style tool configuration for this key.
"tool_configuration": {"type":"Lti::ToolConfiguration"},
  // (LTI keys only) The tool's public JWK in JSON format. Discouraged in favor of
  // a url hosting a JWK set.
"public_jwk": {"e":"AQAB","etc":"etc"},
  // (LTI keys only) The tool-hosted URL containing its public JWK keyset. Canvas
  // may cache JWKs up to 5 minutes.
"public_jwk_url": "https://mytool.com/1_3/jwks",
  // (LTI keys only) The LTI IMS Registration object for this key, if key was
  // created via Dynamic Registration.
"lti_registration": {"type":"TODO Lti::IMS::Registration"},
  // (LTI keys only) Returns true if key was created via Dynamic Registration.
"is_lti_registration": false,
  // Unused.
"user_name": "",
  // Unused.
"user_id": "",
  // Correlates an API key to a product configuration.
"unified_tool_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
}
```

[DeveloperKeysController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/developer_keys_controller.rb)

`GET /api/v1/accounts/:account_id/developer_keys`

**Scope:** `url:GET|/api/v1/accounts/:account_id/developer_keys`

List all developer keys created in the current account.

**Request Parameters:**

Defaults to false. If true, lists keys inherited from Site Admin (and consortium parent account, if applicable).

Returns a list of [DeveloperKey](https://developerdocs.instructure.com/services/canvas/resources/developer_keys#developerkey) objects.

[DeveloperKeysController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/developer_keys_controller.rb)

`POST /api/v1/accounts/:account_id/developer_keys`

**Scope:** `url:POST|/api/v1/accounts/:account_id/developer_keys`

Create a new Canvas API key. Creating an LTI 1.3 registration is not supported here and should be done via the LTI Registration API.

**Request Parameters:**

`developer_key[auto_expire_tokens]`

Defaults to false. If true, access tokens generated by this key will expire after 1 hour.

Contact email for the key.

URL for a small icon to display in key list.

User-provided notes about the key.

`developer_key[redirect_uri]`

Deprecated in favor of redirect\_uris. Do not use.

`developer_key[redirect_uris]`

List of URLs used during OAuth2 flow to validate given redirect URI.

`developer_key[vendor_code]`

User-specified code representing the vendor that uses the key.

Defaults to true. If false, key will not be visible in the UI.

`developer_key[test_cluster_only]`

Defaults to false. If true, key is only usable in non-production environments (test, beta). Avoids problems with beta refresh.

`developer_key[client_credentials_audience]`

Used in OAuth2 client credentials flow to specify the audience for the access token.

List of API endpoints key is allowed to access.

`developer_key[require_scopes]`

If true, then token requests with this key must include scopes.

`developer_key[allow_includes]`

If true, allows ‘includes\` parameters in API requests that match the scopes of this key.

Returns a [DeveloperKey](https://developerdocs.instructure.com/services/canvas/resources/developer_keys#developerkey) object.

[DeveloperKeysController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/developer_keys_controller.rb)

`PUT /api/v1/developer_keys/:id`

**Scope:** `url:PUT|/api/v1/developer_keys/:id`

Update an existing Canvas API key. Updating an LTI 1.3 registration is not supported here and should be done via the LTI Registration API.

**Request Parameters:**

`developer_key[auto_expire_tokens]`

Defaults to false. If true, access tokens generated by this key will expire after 1 hour.

Contact email for the key.

URL for a small icon to display in key list.

User-provided notes about the key.

`developer_key[redirect_uri]`

Deprecated in favor of redirect\_uris. Do not use.

`developer_key[redirect_uris]`

List of URLs used during OAuth2 flow to validate given redirect URI.

`developer_key[vendor_code]`

User-specified code representing the vendor that uses the key.

Defaults to true. If false, key will not be visible in the UI.

`developer_key[test_cluster_only]`

Defaults to false. If true, key is only usable in non-production environments (test, beta). Avoids problems with beta refresh.

`developer_key[client_credentials_audience]`

Used in OAuth2 client credentials flow to specify the audience for the access token.

List of API endpoints key is allowed to access.

`developer_key[require_scopes]`

If true, then token requests with this key must include scopes.

`developer_key[allow_includes]`

If true, allows ‘includes\` parameters in API requests that match the scopes of this key.

Returns a [DeveloperKey](https://developerdocs.instructure.com/services/canvas/resources/developer_keys#developerkey) object.

[DeveloperKeysController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/developer_keys_controller.rb)

`DELETE /api/v1/developer_keys/:id`

**Scope:** `url:DELETE|/api/v1/developer_keys/:id`

Delete an existing Canvas API key. Deleting an LTI 1.3 registration should be done via the LTI Registration API.

Returns a [DeveloperKey](https://developerdocs.instructure.com/services/canvas/resources/developer_keys#developerkey) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).