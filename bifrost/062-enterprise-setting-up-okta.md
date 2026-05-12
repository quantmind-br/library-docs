---
title: Setting up Okta
url: https://docs.getbifrost.ai/enterprise/setting-up-okta.md
source: llms
fetched_at: 2026-01-21T19:43:32.586496326-03:00
rendered_js: false
word_count: 2073
summary: Step-by-step instructions for configuring Okta as an identity provider for Bifrost Enterprise to enable SSO and automated role synchronization.
tags:
    - okta
    - sso
    - authentication
    - identity-provider
    - oidc
    - user-provisioning
category: guide
---

# Setting up Okta

> Step-by-step guide to configure Okta as your identity provider for Bifrost Enterprise SSO authentication.

## Overview

This guide walks you through configuring Okta as your identity provider for Bifrost Enterprise. After completing this setup, your users will be able to sign in to Bifrost using their Okta credentials, with roles and team memberships automatically synchronized.

## Prerequisites

* An Okta organization with admin access
* Bifrost Enterprise deployed and accessible
* The redirect URI for your Bifrost instance (e.g., `https://your-bifrost-domain.com/login`)

***

## Step 1: Create an OIDC Application

1. Log in to the **Okta Admin Console**
2. Navigate to **Applications** → **Applications**
3. Click **Create App Integration**

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=d51122d65f7b21e70c73d6ce779cb8bc" alt="Okta Applications page" data-og-width="1924" width="1924" data-og-height="1320" height="1320" data-path="media/user-provisioning/okta-create-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=1c720653d0b5362e418c1942b08fa1db 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=89751650c0542e19c08ecb8b4a748995 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=e14b0c5bbb24613295688844411b9119 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=b7338f318624fcea1a8b923a983842f3 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=43045e04ec39074a288b77d6054340a5 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-create-app.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=edab037de67f993d83f53a7c6c2ac8af 2500w" />
</Frame>

4. In the dialog, select:
   * **Sign-in method**: OIDC - OpenID Connect
   * **Application type**: Web Application

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=e9d460369db3e297e7c688b757c462a4" alt="Create new app integration dialog" data-og-width="2774" width="2774" data-og-height="2346" height="2346" data-path="media/user-provisioning/okta-app-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=2cc15005668c93ad5d409ae13365e8c1 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=8343cdab5ab2951476efdb6e5433b21a 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=efc4775f4d49092871f50b9cfde9ef21 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=e29fe2c13b632beb197dbf6f7203d8c7 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=584aea36454e805f7aaf2e583a912426 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-configuration.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=51ab390074f1725fdc831e068e98a91a 2500w" />
</Frame>

5. Click **Next** to continue

***

## Step 2: Configure Application Settings

Configure the following settings for your application:

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=6458424a3490f0ac6e8bffcea2dc763a" alt="New Web App Integration settings" data-og-width="2592" width="2592" data-og-height="4050" height="4050" data-path="media/user-provisioning/okta-app-integration-main-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=1bc793967e117a584fb344e416b32df0 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=8397c1816bae0cdc612113fe9a45ed2d 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=8711ff77c71a57a72308a4a1a45d2222 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=cedf06fa66fa06c45fc72ac06df9af66 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=d175f164e932bc32b140ed3078cf8aa3 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-app-integration-main-page.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=e689c57a6b17e254c9f415ac3822627e 2500w" />
</Frame>

**General Settings:**

* **App integration name**: `Bifrost Enterprise`
* **Logo** (optional): You can upload the Bifrost logo from [https://www.getmaxim.ai/bifrost/bifrost-logo-only.png](https://www.getmaxim.ai/bifrost/bifrost-logo-only.png)

**Grant type:**

* Enable **Authorization Code**
* Enable **Refresh Token**

**Sign-in redirect URIs:**

* Add your Bifrost login callback URL: `https://your-bifrost-domain.com/login`

**Sign-out redirect URIs (Optional):**

* Add your Bifrost base URL: `https://your-bifrost-domain.com`

**Assignments:**

* Choose **Skip group assignment for now** (we'll configure this later)

6. Click **Save** to create the application

7. After saving, note down the following from the **General** tab:
   * **Client ID**
   * **Client Secret** (click to reveal)

***

## Step 3: Configure Authorization Server (optional)

<Note>
  The default authorization server (`/oauth2/default`) is available to all Okta plans and **supports custom claims**, including role claims. The API Access Management paid add-on is only required to create additional custom authorization servers beyond the default.
</Note>

Bifrost uses Okta's Authorization Server to issue tokens. You have three options:

1. **Use `/oauth2/default` with role claims (recommended)** — Complete Steps 4-7 to configure custom role claims on the default authorization server. This enables automatic RBAC synchronization.

2. **Use `/oauth2/default` without role claims** — Skip Steps 4-7. The first user to sign in automatically receives the Admin role and can manage RBAC for all subsequent users through the Bifrost dashboard.

3. **Skip Step 3 entirely** — Authorization is not configured through Okta. You'll need an alternative authentication mechanism.

### Configuring the Authorization Server

1. Navigate to **Security** → **API**
2. Click on **Authorization Servers**

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=020b5fbc39e6382d4c14afee84861aa3" alt="Okta Authorization Servers" data-og-width="4006" width="4006" data-og-height="2516" height="2516" data-path="media/user-provisioning/okta-authorization-server.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=f895a00e515d1e62c23875900fc9e5eb 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=51b632cbf4ad6a9ff09f8776f6094226 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=43b0cf09cfda2b54b6b735cb7295f7c1 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=bf0166c95ecb745775733d89ba6c573c 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=cc80ad053807b47142b7ae962d54055f 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-authorization-server.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=f6e9eb2be686539ed089812174fac437 2500w" />
</Frame>

3. Note the **Issuer URI** for your authorization server (e.g., `https://your-domain.okta.com/oauth2/default`)

<Note>
  The Issuer URI is used as the `issuerUrl` in your Bifrost configuration. Make sure to use the full URL including `/oauth2/default` (or your custom authorization server path).
</Note>

***

## Step 4: Create Custom Role Attribute

To map Okta users to Bifrost roles (Admin, Developer, Viewer), you need to create a custom attribute.

1. Navigate to **Directory** → **Profile Editor**

<Frame>
  <img src="https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=4ce8cb4fb6bf5faf9856c0acd8c867f3" alt="Okta Profile Editor" data-og-width="4102" width="4102" data-og-height="2248" height="2248" data-path="media/user-provisioning/okta-profile-editor-screen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?w=280&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=e1e43588615c8288e954eed0c7c27e89 280w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?w=560&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=2ae5bac25b0e1352077de2c50a459ed1 560w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?w=840&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=b89f64f4ed9bff184eb2935fffbc32d6 840w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?w=1100&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=d2f8e62b10ee8e6a5be5d3b640da6b81 1100w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?w=1650&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=183541ed8c872c0096b5285db7d5f928 1650w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-profile-editor-screen.png?w=2500&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=f012da10886a1d17d161c87034d7263a 2500w" />
</Frame>

2. Click on your application's user profile (e.g., **Bifrost Enterprise User**)
3. Click **Add Attribute**
4. Configure the attribute:

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=f6efc479323b6c20ceb0ff44bce7a3cc" alt="Add custom attribute for bifrostRole" data-og-width="2040" width="2040" data-og-height="2960" height="2960" data-path="media/user-provisioning/okta-custom-attribute-creation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=75dc5c2bf9aa040a277b4f397a6b57f7 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=0749563c303462bf0b854c7ea0ca4a3e 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=75aa4861714c91d59e3327feb2bc1167 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=c1041fe24600c4bb838d92363f5a03df 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=4425380cdf83cfc3c7c35f2df8c38210 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-custom-attribute-creation.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=ddac3e023502ba93c41b0fc1704a4ad6 2500w" />
</Frame>

| Field                 | Value                                                       |
| --------------------- | ----------------------------------------------------------- |
| **Data type**         | string                                                      |
| **Display name**      | bifrostRole                                                 |
| **Variable name**     | bifrostRole                                                 |
| **Enum**              | Check "Define enumerated list of values"                    |
| **Attribute members** | Admin → `admin`, Developer → `developer`, Viewer → `viewer` |
| **Attribute type**    | Personal                                                    |

5. Click **Save**

***

## Step 5: Add Role Claim to Tokens

Configure the authorization server to include the role in the access token.

1. Navigate to **Security** → **API** → **Authorization Servers**
2. Click on your authorization server (e.g., **default**)
3. Go to the **Claims** tab
4. Click **Add Claim**

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=4dc5d79d097823a3ed30634d163e66bc" alt="Add role claim" data-og-width="2102" width="2102" data-og-height="1900" height="1900" data-path="media/user-provisioning/okta-claim-addition.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=15ab686e5385784d97f0345a04b262ad 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=ec340a4a6f6ad200d7502d776f5b620a 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=3509f5e78427631db1fadfa190dec173 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=f54ae391d2114e458122dd3ac72d0532 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=da860890dedf57bc9401996a25bf126e 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-claim-addition.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=9e6bf5fa5e30714ee46b034d346ffccc 2500w" />
</Frame>

Configure the claim:

| Field                     | Value                |
| ------------------------- | -------------------- |
| **Name**                  | `role`               |
| **Include in token type** | Access Token, Always |
| **Value type**            | Expression           |
| **Value**                 | `user.bifrostRole`   |
| **Include in**            | Any scope            |

5. Click **Create**

<Note>
  If you named your custom attribute differently, update the Value expression accordingly (e.g., `user.yourAttributeName`).
</Note>

***

## Step 6: Configure Groups for Team and Role Synchronization

Bifrost can automatically sync Okta groups for two purposes:

* **Team synchronization** — Groups are synced as Bifrost teams
* **Role mapping** — Groups can be mapped to Bifrost roles (Admin, Developer, Viewer) using Group-to-Role Mappings in the Bifrost UI

### Create Groups in Okta

1. Navigate to **Directory** → **Groups**

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=acec042ac2c16ef15c40222d8397dcb7" alt="Okta Groups page" data-og-width="4250" width="4250" data-og-height="2748" height="2748" data-path="media/user-provisioning/okta-groups-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=a0f138b4aa23ea524208a8fdc77b5b9e 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=2fdde538183a402eb4bf19776d04c85d 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=730559e7179d08ad76c907cb846de2fd 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=4b2afd23da0305f47bed171cce2c27d7 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=fa39c8f56987f59e200b8b7b6694306a 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-groups-page.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=5e10ed33abe38041c6b2e76186fa0e32 2500w" />
</Frame>

2. Click **Add group**
3. Create groups that correspond to your teams or roles (e.g., `bifrost-staging-admins`, `bifrost-staging-viewers`)

<Frame>
  <img src="https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=9ef0e1a3cc26d18e1c57ff1091a80396" alt="Groups created in Okta" data-og-width="2796" width="2796" data-og-height="1408" height="1408" data-path="media/user-provisioning/okta-create-groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?w=280&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=f953e86437984a3fa0f217dfff41e60c 280w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?w=560&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=bfd8b907d1c2fc76f260373cb580cf39 560w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?w=840&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=6367aa4662c0231c2def8f4f950df510 840w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?w=1100&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=85cc206e19d3a7437a532ae200298864 1100w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?w=1650&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=8b808f57d9b97eb19250b6343af13843 1650w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-create-groups.png?w=2500&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=48afa9f8013c85863719ea9ba838cdb4 2500w" />
</Frame>

<Note>
  Use a consistent naming convention for your groups. This makes it easier to configure group filters and role mappings later.
</Note>

### Add Groups Claim to Tokens

You have two options for configuring the groups claim. Choose the one that best fits your Okta plan and requirements.

#### Option A: Using App-Level Groups Claim (All Okta Plans)

This approach configures the groups claim directly in your application's settings and works with all Okta plans, including free tiers.

1. Navigate to your application's **Sign On** tab
2. Scroll down to the **OpenID Connect ID Token** section
3. Click **Edit** to modify the settings
4. Configure the **Groups claim filter**:
   * **Groups claim type**: Filter
   * **Groups claim filter**: Set a claim name (e.g., `groups`) and filter condition (e.g., "Starts with" `bifrost-staging`)

<Frame>
  <img src="https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=ed5a2e13bcb38896be03fd9237d20cd7" alt="Application Groups claim configuration" data-og-width="1988" width="1988" data-og-height="1502" height="1502" data-path="media/user-provisioning/okta-app-group-claim-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?w=280&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=0b8fa9690db062cbb4a815d89309fcf6 280w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?w=560&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=7274c79db8d9f0d52424ec703276bbff 560w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?w=840&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=c679c0c624ed6314e994805e21de3f7d 840w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?w=1100&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=8db4bd9d7e90a4b5e34c2f81a449ce24 1100w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?w=1650&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=e99b6b14fabdba355ad156465f95e3ad 1650w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-app-group-claim-setup.png?w=2500&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=7d22684ebae7df612ea30f102474d709 2500w" />
</Frame>

5. Click **Save**

<Note>
  The filter ensures only relevant groups are included in the token. Adjust the filter condition based on your group naming convention.
</Note>

#### Option B: Using Authorization Server Groups Claim

This approach adds the groups claim through your authorization server, providing more flexibility for complex configurations.

1. Navigate to **Security** → **API** → **Authorization Servers**
2. Select your authorization server (e.g., **default**)
3. Go to the **Claims** tab
4. Click **Add Claim**

Configure the groups claim:

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| **Name**                  | `groups`                                                    |
| **Include in token type** | ID Token, Always                                            |
| **Value type**            | Groups                                                      |
| **Filter**                | Matches regex: `.*` (or specify a prefix like `bifrost-.*`) |
| **Include in**            | Any scope                                                   |

5. Click **Create**

You can also configure an additional groups claim in the application's Sign On settings:

1. Navigate to your application's **Sign On** tab

<Frame>
  <img src="https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=cfc141bfc43e065bf9e9bbd298319928" alt="Application Sign On configuration" data-og-width="2710" width="2710" data-og-height="3531" height="3531" data-path="media/user-provisioning/okta-group-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?w=280&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=c497f8b39167571fa71c22e10fd7b675 280w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?w=560&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=fc5d0c9977297076a0906e9b2c037a8d 560w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?w=840&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=c2c01b253c7690959098eff950206d8e 840w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?w=1100&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=d75add65d86f28b602548b48f64be192 1100w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?w=1650&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=69f50b6c2ba4115cf3e49861a290a2d1 1650w, https://mintcdn.com/bifrost/M-O2e07ptwQW1_pO/media/user-provisioning/okta-group-configuration.png?w=2500&fit=max&auto=format&n=M-O2e07ptwQW1_pO&q=85&s=00b6ded74dfac382e17d049cdd7ddc8e 2500w" />
</Frame>

2. Under **OpenID Connect ID Token**, configure:
   * **Groups claim type**: Expression
   * **Groups claim expression**: `Arrays.flatten(Groups.startsWith("OKTA", "bifrost", 100))`

<Note>
  Adjust the group filter expression based on your naming convention. The example above includes groups starting with "bifrost".
</Note>

***

## Step 7: Assign Users to the Application

1. Navigate to your application's **Assignments** tab

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=e365c77d4e475619e5de36d2289c8255" alt="Application Assignments tab" data-og-width="2758" width="2758" data-og-height="2218" height="2218" data-path="media/user-provisioning/okta-assign-users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=1f8c0a7e5a4170404f2a385dea9018c7 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=5194e31c3ef6a2e000e7e90495699183 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=029bd7e986cacad12351fefb6b3a231d 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=d7482c93ea1aa7bf3c739d78e10909ed 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=d882293f335cffb2ce037d658650cdea 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-users.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=b0a6c05c6efb60de3bac4752ed57c7fa 2500w" />
</Frame>

2. Click **Assign** → **Assign to People** or **Assign to Groups**

3. For each user, set their **bifrostRole**:

<Frame>
  <img src="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=e6732e83258fe4bfc70992ae94720771" alt="Assign custom role to user" data-og-width="2386" width="2386" data-og-height="1310" height="1310" data-path="media/user-provisioning/okta-assign-custom-role.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?w=280&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=f0f5eaec1495b509e3c061cb09c0fe64 280w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?w=560&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=3a6102814710cc88dfc707e0b5eb73b9 560w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?w=840&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=8c981dc47aa4329f9a099b1e12919a8a 840w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?w=1100&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=ae5739471cd2e312230179afd361e410 1100w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?w=1650&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=b6ca2e8e611bde572f73d2b48f7c4933 1650w, https://mintcdn.com/bifrost/81g5ib9Jdgu71153/media/user-provisioning/okta-assign-custom-role.png?w=2500&fit=max&auto=format&n=81g5ib9Jdgu71153&q=85&s=bd7569dbea19b5b567830a9a7d03d65d 2500w" />
</Frame>

4. Click **Save and Go Back**

<Note>
  Role claims are available only when you configure custom claims on your authorization server. Ensure you add role claims to your chosen authorization server (for example, `/oauth2/default`) to enable RBAC. If you skipped Steps 4-7, the first user to sign in automatically receives the **Admin** role and can manage RBAC for all subsequent users through the Bifrost dashboard.
</Note>

***

## Step 8: Configure Bifrost

Now configure Bifrost to use Okta as the identity provider.

### Using the Bifrost UI

1. Navigate to **Governance** → **User Provisioning** in your Bifrost dashboard
2. Select **Okta** as the SCIM Provider
3. Enter the following configuration:

| Field             | Value                                                                |
| ----------------- | -------------------------------------------------------------------- |
| **Client ID**     | Your Okta application Client ID                                      |
| **Issuer URL**    | Issuer URL                                                           |
| **Audience**      | Your API audience (e.g., `api://default` or custom)                  |
| **Client Secret** | Your Okta application Client Secret (optional, for token revocation) |

4. Toggle **Enabled** to activate the provider
5. Click **Save Configuration**

### Group-to-Role Mappings (Optional)

If you configured groups in Okta (Step 6), you can map Okta group names directly to Bifrost roles. This is an alternative to using custom role claims (Steps 4-5) and works with all Okta plans.

1. In the User Provisioning configuration, scroll down to **Group-to-Role Mappings**
2. Click **Add Mapping**
3. Enter the **Group Claim Name** exactly as it appears in your Okta groups (e.g., `bifrost-staging-admins`)
4. Select the corresponding **Role** (Admin, Developer, or Viewer)
5. Repeat for each group you want to map

<Frame>
  <img src="https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=23b9f4000294a365e4c346c6bbea118f" alt="Group-to-Role Mappings configuration in Bifrost" data-og-width="1772" width="1772" data-og-height="886" height="886" data-path="media/user-provisioning/okta-group-claim-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?w=280&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=4aaaa88df93308128bf9b0cd74571537 280w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?w=560&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=e8535c9548eeec034245a868e39af24b 560w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?w=840&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=84a6a1589f4df75c1d91d1a5a2c00325 840w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?w=1100&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=ba56e2ae11f4a86b5dbd3507b86bd073 1100w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?w=1650&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=f3dd4b7e7c2c2bf4cdb460ac3941852c 1650w, https://mintcdn.com/bifrost/blvHhT178W7Ot2qr/media/user-provisioning/okta-group-claim-mapping.png?w=2500&fit=max&auto=format&n=blvHhT178W7Ot2qr&q=85&s=bd33f334773a2eed31aa6fe16daaa243 2500w" />
</Frame>

| Group Claim Name          | Role   |
| ------------------------- | ------ |
| `bifrost-staging-admins`  | Admin  |
| `bifrost-staging-viewers` | Viewer |

<Note>
  If a user belongs to multiple groups with different role mappings, the highest privilege role is assigned. If no mapping matches, the first user to sign in receives the **Admin** role, and subsequent users receive the **Viewer** role.
</Note>

6. Click **Save Configuration**

<Warning>
  After saving, you'll need to restart your Bifrost server for the changes to take effect.
</Warning>

### Configuration Reference

| Field          | Required | Description                                                                         |
| -------------- | -------- | ----------------------------------------------------------------------------------- |
| `issuerUrl`    | Yes      | Okta authorization server URL (e.g., `https://your-domain.okta.com/oauth2/default`) |
| `clientId`     | Yes      | Application Client ID from Okta                                                     |
| `clientSecret` | No       | Application Client Secret (enables token revocation)                                |
| `audience`     | Yes      | API audience identifier from your authorization server                              |
| `userIdField`  | No       | JWT claim for user ID (default: `uid`)                                              |
| `rolesField`   | No       | JWT claim for roles (default: `roles`)                                              |
| `teamIdsField` | No       | JWT claim for group/team IDs (default: `groups`)                                    |

***

## Testing the Integration

1. Open your Bifrost dashboard in a new browser or incognito window
2. You should be redirected to Okta for authentication
3. Log in with an assigned user
4. After successful authentication, you'll be redirected back to Bifrost
5. Verify the user appears in the Bifrost users list with the correct role

***

## Troubleshooting

### User not redirected to Okta

* Verify the SCIM provider is enabled in Bifrost
* Check that the Bifrost server was restarted after configuration
* Ensure the Issuer URL is correct and accessible

### "Invalid audience" error

* Verify the `audience` field matches your Okta authorization server's audience
* Check if you're using a custom authorization server and update the issuer URL accordingly

### Roles not syncing

* Ensure the `role` claim is configured in your authorization server
* Verify users have the `bifrostRole` attribute set
* Check that the claim is included in the access token (use Okta's Token Preview feature)

### Groups not appearing as teams

* Verify the `groups` claim is configured in your authorization server
* Ensure users are assigned to the relevant groups
* Check that groups are assigned to the application

### Token refresh failing

* Ensure the **Refresh Token** grant type is enabled for your application
* Verify the `offline_access` scope is included in your authorization requests

***

## Next Steps

* **[Advanced Governance](./advanced-governance)** - Learn about user budgets and compliance features
* **[Role-Based Access Control](./advanced-governance#role-hierarchy)** - Understand the Admin, Developer, Viewer hierarchy
* **[Audit Logs](./audit-logs)** - Monitor user authentication and activity


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt