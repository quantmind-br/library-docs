---
title: Remove Profile Picture - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/profile-settings/remove-profile-picture
source: sitemap
fetched_at: 2026-04-12T18:47:05.642765318-03:00
rendered_js: false
word_count: 48
summary: This documentation serves as a comprehensive guide to the Evolution API, providing reference materials and examples for various functionalities like removing a user's profile picture.
tags:
    - api
    - documentation
    - profile-picture
    - api-reference
    - curl
    - authentication
category: reference
---

[Evolution API Documentation home page![light logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=f1b6e7e9e3c26afb6c9dea2e589e589a)![dark logo](https://mintcdn.com/evolution-74046672/bBwt1xoriRb-DHv0/images/brand/cover-white.png?fit=max&auto=format&n=bBwt1xoriRb-DHv0&q=85&s=337207c57ad618db275c889b70137c0b)](https://doc.evolution-api.com/)

[Português](https://doc.evolution-api.com/v2/pt/get-started/introduction)[English](https://doc.evolution-api.com/v2/en/get-started/introduction)[API](https://doc.evolution-api.com/v2/api-reference/get-information)

Remove Profile Picture

```
curl --request DELETE \
  --url https://evolution-example/chat/removeProfilePicture/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

DELETE

/

chat

/

removeProfilePicture

/

{instance}

Remove Profile Picture

```
curl --request DELETE \
  --url https://evolution-example/chat/removeProfilePicture/{instance} \
  --header 'apikey: <api-key>'

This response has no body data.
```

#### Authorizations

[​](#authorization-apikey)

apikey

string

header

required

Your authorization key header

#### Path Parameters

[​](#parameter-instance)

instance

string

required

Name instance

#### Response

200 - undefined

[Update Profile Picture](https://doc.evolution-api.com/v2/api-reference/profile-settings/update-profile-picture)[Fetch Privacy Settings](https://doc.evolution-api.com/v2/api-reference/profile-settings/fetch-privacy-settings)