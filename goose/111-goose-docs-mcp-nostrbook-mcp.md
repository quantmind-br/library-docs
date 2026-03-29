---
title: Nostrbook Extension | goose
url: https://block.github.io/goose/docs/mcp/nostrbook-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:33.173393259-03:00
rendered_js: true
word_count: 501
summary: This document explains how to integrate the Nostrbook MCP server into the goose environment and provides a detailed guide on implementing NIP-61 Nutzaps for Bitcoin micropayments.
tags:
    - nostr
    - mcp-server
    - goose-ai
    - nip-61
    - nutzaps
    - decentralized-protocol
    - cashu
category: tutorial
---

This tutorial covers how to add the [Nostrbook MCP Server](https://gitlab.com/soapbox-pub/nostrbook) as a goose extension to provide access to a comprehensive registry of Nostr documentation that helps users understand the decentralized social protocol, its implementation possibilities, and technical specifications.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=%40nostrbook%2Fmcp&id=nostrbook&name=Nostrbook&description=A%20comprehensive%20registry%20of%20Nostr%20documentation%20with%20structured%20knowledge)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

### goose Prompt[​](#goose-prompt "Direct link to goose Prompt")

> *goose, what is the NIP-61 and how can I implement it?.*

### goose Output[​](#goose-output "Direct link to goose Output")

Note that IDs have been changed to generic ones

CLI

Tool Calls

## NIP-61: Implementing Nutzaps

NIP-61 defines "Nutzaps," which are P2PK Cashu tokens where the payment itself acts as the receipt. This protocol allows for Bitcoin micropayments through the Nostr ecosystem using Cashu tokens.

## Core Concept[​](#core-concept "Direct link to Core Concept")

Nutzaps enable users to send small Bitcoin payments to each other through Nostr events, with the tokens being locked to the recipient's specified public key.

## Implementation Guide[​](#implementation-guide "Direct link to Implementation Guide")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1. Familiarize yourself with [Cashu](https://cashu.space/) and [P2PK token locking](https://github.com/cashubtc/nuts/blob/main/11.md)
2. Understand [NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) for wallet functionality
3. Ensure your implementation supports NUT-11 (P2PK) and NUT-12 (DLEQ proofs)

### Step 1: Set Up Recipient Information (For Receiving Nutzaps)[​](#step-1-set-up-recipient-information-for-receiving-nutzaps "Direct link to Step 1: Set Up Recipient Information (For Receiving Nutzaps)")

Create and publish a `kind:10019` event to inform others how to send you money:

```
{
"kind":10019,
"tags":[
["relay","wss://your-relay1.com"],
["relay","wss://your-relay2.com"],
["mint","https://your-trusted-mint.com","sat"],
["pubkey","<your-p2pk-pubkey>"]
]
}
```

- The `pubkey` should be a dedicated public key (NOT your Nostr identity key)
- Store the corresponding private key safely in your NIP-60 wallet event
- List only mints you trust and monitor

### Step 2: Building the Sender Functionality[​](#step-2-building-the-sender-functionality "Direct link to Step 2: Building the Sender Functionality")

To implement nutzapping:

1. **Query recipient information**:
   
   ```
   // Fetch recipient's kind:10019 event
   const recipientInfo =await relay.get({
   kinds:[10019],
   authors:[recipientPubkey]
   });
   ```
2. **Extract mint and P2PK information**:
   
   ```
   const recipientMints = recipientInfo.tags
   .filter(tag=> tag[0]==='mint')
   .map(tag=> tag[1]);
   
   const recipientLockKey = recipientInfo.tags
   .find(tag=> tag[0]==='pubkey')?.[1];
   ```
3. **Mint or swap tokens** at one of the recipient's trusted mints, P2PK-locking them to their specified key
4. **Publish the nutzap event**:
   
   ```
   {
   "kind":9321,
   "content":"Thanks for your post!",
   "tags":[
   ["proof","{\"amount\":1,\"C\":\"02...3f\",\"id\":\"000...\",\"secret\":\"[\\\"P2PK\\\",...]\"}"],
   ["u","https://recipient-specified-mint.com"],
   ["e","<event-being-zapped>","<relay-hint>"],
   ["p","<recipient-pubkey>"]
   ]
   }
   ```

### Step 3: Building the Recipient Functionality[​](#step-3-building-the-recipient-functionality "Direct link to Step 3: Building the Recipient Functionality")

To implement nutzap receiving:

1. **Query for incoming nutzaps**:
   
   ```
   // Subscribe to nutzap events
   relay.subscribe([
   {
   kinds:[9321],
   "#p":[myPubkey],
   "#u": myTrustedMints,
   since: lastCheckTimestamp
   }
   ]);
   ```
2. **Validate incoming nutzaps**:
   
   - Verify the token is from a mint you've specified
   - Verify the token is locked to your P2PK key
   - Verify the DLEQ proof
3. **Redeem the token**:
   
   - Swap the P2PK token into your wallet
   - Create a `kind:7376` event to record redemption:
   
   ```
   {
   "kind":7376,
   "content":"<encrypted-content>",
   "tags":[
   ["e","<nutzap-event-id>","","redeemed"],
   ["p","<sender-pubkey>"]
   ]
   }
   ```

### Important Implementation Details[​](#important-implementation-details "Direct link to Important Implementation Details")

1. **P2PK Key Prefixing**: Always prefix the P2PK-lock public key with "02" for compatibility
2. **Token Verification**: Implement local verification of DLEQ proofs
3. **Mint URL Normalization**: Normalize mint URLs to avoid issues with slight URL variations
4. **User Guidance**: Guide users to use only NUT-11 and NUT-12 compatible mints
5. **Publishing Locations**: Publish nutzap events to the recipient's specified relays

## Testing[​](#testing "Direct link to Testing")

When testing your implementation:

1. Create test nutzaps with small amounts
2. Verify token redemption works correctly
3. Check that redemption records are properly created
4. Test with multiple mints for compatibility

## Security Considerations[​](#security-considerations "Direct link to Security Considerations")

- Never use the user's main Nostr key for P2PK operations
- Ensure proper encryption of sensitive wallet data
- Validate all proofs before attempting to redeem tokens
- Only interact with explicitly trusted mints

By following these steps, you can implement a complete nutzap solution that allows users to send and receive Bitcoin micropayments through the Nostr protocol using Cashu tokens.