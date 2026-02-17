---
title: Bitcoin Core
url: https://coolify.io/docs/services/bitcoin-core.md
source: llms
fetched_at: 2026-02-17T14:42:29.838296-03:00
rendered_js: false
word_count: 219
summary: This document explains how to set up and configure a Bitcoin Core full node, specifically detailing the steps required to transition from a private internal setup to a public peer-to-peer node.
tags:
    - bitcoin-core
    - coolify
    - self-hosting
    - node-configuration
    - p2p-networking
    - firewall-setup
category: configuration
---

# Bitcoin Core

## What is Bitcoin Core

A self-hosted Bitcoin Core full node.

## Public Node vs. Private Use

By default, Coolify’s Bitcoin Core service is configured for private/internal use. This means it is intended for connecting wallets or apps from the same server or private network, and **does not accept inbound P2P connections from the public internet**. This is a security-conscious default to help reduce the attack surface, especially for new users.

### How to Run a Public Node

If you want your Bitcoin node to be a fully public peer (accepting inbound connections from other nodes):

1. **Expose the P2P port in your Compose file:**\
   Add the following under your `bitcoin-core` service:
   ```text
   ports:
   - "8333:8333"
   ```

2. **Open port 8333 in your server’s firewall:**

* On Ubuntu with UFW:
  ```bash
  sudo ufw allow 8333/tcp
  ```
* On CentOS with firewalld:
  ```bash
  sudo firewall-cmd --add-port=8333/tcp --permanent
  sudo firewall-cmd --reload
  ```
* For cloud servers, update your provider’s security group or firewall rules to allow inbound TCP on port 8333.

### Considerations

* **Default Behavior:**\
  Without the `ports` section, your node will not accept inbound P2P connections, but can still make outbound connections and fully sync the blockchain.
* **Security:**\
  Not exposing 8333 by default helps protect users who may not understand the implications of running a public Bitcoin node.
* **Advanced Users:**\
  If you understand the risks and want to contribute more fully to the Bitcoin network, follow the steps above to run a public node.

## Links

* [Official Documentation](https://hub.docker.com/r/ruimarinho/bitcoin-core/?utm_source=coolify.io)