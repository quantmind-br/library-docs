# mitmproxy Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence from introduction through advanced API reference.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://docs.mitmproxy.org/stable/ |
| **Generated** | 2026-02-11T04:18:00Z |
| **Total Documents** | 53 |
| **Categories** | 9 |
| **Strategy** | crawler |

---

## Document Index

### 1. Introduction & Overview (001-004)
*Core introduction to mitmproxy, installation, first steps, and feature overview.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-stable.md` | Introduction | Introduces the mitmproxy project, its core features, and the three main tools: mitmproxy, mitmweb, and mitmdump | mitmproxy, http-proxy, intercepting-proxy, ssl-tls, mitmdump, mitmweb |
| 002 | `002-stable-overview-installation.md` | Installation | Comprehensive installation instructions for macOS, Linux, Windows, PyPI, and Docker | installation, macos, linux, windows, pypi, docker |
| 003 | `003-stable-overview-getting-started.md` | Getting Started | How to launch tools, configure proxy, verify setup, and install certificates | getting-started, proxy-configuration, tls-inspection, certificate-authority |
| 004 | `004-stable-overview-features.md` | Features | Overview of features: caching, traffic blocking, replay, URL mapping, body/header modification | proxy-features, traffic-modification, request-replay, url-mapping, content-blocking |

### 2. CLI Tutorials - mitmproxy Console (005-009)
*Step-by-step video tutorials for the mitmproxy command-line interactive interface.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 005 | `005-stable-mitmproxytutorial-userinterface.md` | User Interface | Navigating the flow list, viewing flow details, keyboard shortcuts, and commands | user-interface, cli-navigation, keyboard-shortcuts, flow-management |
| 006 | `006-stable-mitmproxytutorial-interceptrequests.md` | Intercept Requests | Using `set intercept` command with flow filter expressions to pause requests | request-interception, cli-command, flow-filters |
| 007 | `007-stable-mitmproxytutorial-modifyrequests.md` | Modify Requests | Editing the path of intercepted flows before forwarding to destination | request-modification, intercepted-requests, flow-editing, path-modification |
| 008 | `008-stable-mitmproxytutorial-replayrequests.md` | Replay Requests | Client-side replay to resend previous client requests to a server | replay-requests, client-side-replay, cli-tutorial |
| 009 | `009-stable-mitmproxytutorial-whatsnext.md` | What's Next | Tutorial completion, next steps for proxy configuration and core features | tutorial-completion, next-steps, proxy-configuration |

### 3. Web UI Tutorials - mitmweb (010-014)
*Step-by-step video tutorials for the mitmweb browser-based interface.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 010 | `010-stable-web-tutorials-web-01-user-interface.md` | User Interface | Documentation index with links to overview, tutorials, concepts, API reference, and addons | documentation-index, network-proxy, traffic-interception |
| 011 | `011-stable-web-tutorials-web-02-intercepting-traffic.md` | Intercept Traffic | Documentation index covering installation, usage, concepts, addon development, and API reference | documentation-overview, proxy-tool, network-security |
| 012 | `012-stable-web-tutorials-web-03-analysing-flows.md` | Analyze Flows | Navigating documentation resources for traffic analysis and addon development | documentation-index, traffic-analysis, how-to-guides |
| 013 | `013-stable-web-tutorials-web-04-modifying-requests.md` | Modify Requests | Documentation table of contents for overview, tutorials, concepts, and how-to guides | documentation-index, traffic-interception, addon-development |
| 014 | `014-stable-web-tutorials-web-05-replaying-flows.md` | Replay Flows | Documentation index covering installation, tutorials, concepts, API references, and addons | documentation-index, traffic-analysis, addon-development |

### 4. Standalone Tutorials (015-016)
*Practical, real-world tutorials demonstrating mitmproxy use cases.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 015 | `015-stable-tutorials-client-replay.md` | Client Playback: 30 Second Example | Automating login process using client replay - recording and replaying HTTP conversations | client-replay, automation, http-conversation, mitmdump, login-process |
| 016 | `016-stable-tutorials-highscores.md` | Setting Highscores on Apple GameCenter | Intercepting and modifying Apple Game Center traffic to alter game high scores | game-center, traffic-manipulation, score-hacking, ios-app, network-intercept |

### 5. Core Concepts (017-023)
*Fundamental concepts explaining how mitmproxy works, its modes, protocols, and configuration.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 017 | `017-stable-concepts-how-mitmproxy-works.md` | How mitmproxy Works | Technical details of traffic interception: explicit/transparent proxying, TLS, SNI | proxying-mechanisms, https-interception, tls-mitm, security-certificates |
| 018 | `018-stable-concepts-modes.md` | Proxy Modes | Available proxy modes: regular, transparent, local capture, WireGuard, reverse proxy | proxy-modes, traffic-capture, regular-proxy, local-capture, wireguard-mode, reverse-proxy |
| 019 | `019-stable-concepts-certificates.md` | Certificates | CA certificates for TLS decryption, client installation, certificate pinning bypass | certificates, certificate-authority, tls-decryption, ca-installation, certificate-pinning |
| 020 | `020-stable-concepts-protocols.md` | Protocols | Supported protocols: HTTP/1, HTTP/2, HTTP/3, WebSocket, DNS, TCP/UDP and limitations | protocols, http, websocket, dns, tcp-udp, limitations |
| 021 | `021-stable-concepts-options.md` | Options | Configuration system: YAML file, CLI flags, interactive editors, option reference | configuration, options, yaml-config, cli-flags, settings, runtime-behavior |
| 022 | `022-stable-concepts-filters.md` | Filter Expressions | Filter expression reference: operators and flow selectors for network flow manipulation | filter-expressions, operators, flow-selectors, network-analysis |
| 023 | `023-stable-concepts-commands.md` | Commands | Command system for interacting with addons and flows, key binding customization | commands, command-interface, key-binding-customization, flow-interaction |

### 6. Addon Development (024-029)
*Guides for developing custom mitmproxy addons with scripting, options, commands, and content views.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 024 | `024-stable-addons-overview.md` | Addons Overview | Addon mechanism: events, options, commands; class-based and scripting addon examples | addons, scripting, events, proxy-tool, development, customization |
| 025 | `025-stable-addons-options.md` | Custom Options | Defining typed options, handling config changes, validating user input in addons | custom-options, addon-configuration, type-specification, option-validation |
| 026 | `026-stable-addons-commands.md` | Custom Commands | Implementing typed commands, argument types (flows, paths), filter integration | custom-commands, command-declaration, command-arguments, flow-filters |
| 027 | `027-stable-addons-contentviews.md` | Custom Contentviews | Creating custom content views for pretty-printing binary data and interactive editing | content-views, pretty-printing, interactive-views, customization |
| 028 | `028-stable-addons-examples.md` | Addon Examples | Example addons: HTTP modification, command integration, options management, DNS spoofing | addons, examples, scripting, websocket, tcp, dns-spoofing |
| 029 | `029-stable-addons-api-changelog.md` | API Changelog | Breaking changes across versions: Contentviews, DNS, connections, logging, event hooks | addon-api, breaking-changes, api-changelog, version-updates |

### 7. How-To Guides (030-035)
*Practical guides for specific deployment scenarios and integrations.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-stable-howto-transparent.md` | Transparent Proxying | Configuring transparent proxy on Linux, OpenBSD, macOS with IP forwarding and firewall rules | transparent-proxying, network-configuration, iptables, pf-firewall |
| 031 | `031-stable-howto-transparent-vms.md` | Transparently Proxying VMs | Setting up transparent proxy for VMs with dnsmasq, iptables, and network interfaces | transparent-proxy, virtual-machines, dnsmasq, iptables, virtualbox |
| 032 | `032-stable-howto-install-system-trusted-ca-android.md` | System CA on Android Emulator | Installing mitmproxy CA into Android emulator system store, Magisk method | android-emulator, ca-certificate, system-ca-store, magisk |
| 033 | `033-stable-howto-ignore-domains.md` | Ignoring Domains | Configuring `ignore_hosts` option with regex patterns for traffic exclusion | ignore-hosts, traffic-exclusion, certificate-pinning, regex-patterns |
| 034 | `034-stable-howto-wireshark-tls.md` | Wireshark and SSL/TLS | Logging SSL/TLS master secrets for Wireshark traffic decryption | wireshark, ssl-tls, key-logging, decryption, environment-variables |
| 035 | `035-stable-howto-kubernetes.md` | Kubernetes Services | Using kubetap kubectl plugin for proxying Kubernetes Services | kubernetes, kubetap, kubectl-plugin, service-proxying |

### 8. API Reference (036-052)
*Complete Python API reference for mitmproxy's core modules, data structures, and event hooks.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-stable-api-events.md` | Event Hooks | All addon event hooks: Lifecycle, Connection, HTTP, DNS, TCP, UDP, QUIC, TLS, WebSocket, SOCKS5 | event-hooks, lifecycle-events, network-events, flow-modification |
| 037 | `037-stable-api-mitmproxy-flow.md` | mitmproxy.flow | Core `Flow` class and `Error` class for representing network interactions | flow-class, error-handling, network-flow, api-definition |
| 038 | `038-stable-api-mitmproxy-http.md` | mitmproxy.http | `Headers` class and `MessageData` dataclass for HTTP message management | http-headers, header-parsing, data-structures, serialization |
| 039 | `039-stable-api-mitmproxy-connection.md` | mitmproxy.connection | `Connection` base class and `Client` subclass with TLS, ALPN, cipher attributes | connection-class, network-connection, tls-details, alpn |
| 040 | `040-stable-api-mitmproxy-tls.md` | mitmproxy.tls | TLS/DTLS ClientHello parsing: SNI, ALPN, cipher suites; TLS event hook data | tls-clienthello, dtls, protocol-parsing, server-name-indication |
| 041 | `041-stable-api-mitmproxy-certs.md` | mitmproxy.certs | `Cert` class for TLS/SSL certificate management using cryptography library | tls-certificate, x509, certificate-management, cryptography |
| 042 | `042-stable-api-mitmproxy-dns.md` | mitmproxy.dns | DNS question and resource record classes with JSON serialization | dns-question, dns-resource-record, data-serialization, dns-record-types |
| 043 | `043-stable-api-mitmproxy-tcp.md` | mitmproxy.tcp | `TCPFlow` and `TCPMessage` classes for TCP session representation | tcp-flow, tcp-message, data-model, network-traffic |
| 044 | `044-stable-api-mitmproxy-udp.md` | mitmproxy.udp | `UDPFlow` and `UDPMessage` classes for UDP session and datagram representation | udp-flow, udp-message, data-model, network-protocol |
| 045 | `045-stable-api-mitmproxy-websocket.md` | mitmproxy.websocket | `WebSocketMessage` and `WebSocketData` classes within HTTP flows | websocket, websocket-message, websocket-data, http-flows |
| 046 | `046-stable-api-mitmproxy-contentviews.md` | mitmproxy.contentviews | Content views for formatting, decoding, highlighting HTTP/WebSocket data | content-views, data-formatting, decoding, http-messages |
| 047 | `047-stable-api-mitmproxy-addonmanager.md` | mitmproxy.addonmanager | `AddonManager` class for addon lifecycle, registration, and event handling | addon-manager, addon-lifecycle, event-hooks, dynamic-registration |
| 048 | `048-stable-api-mitmproxy-coretypes-multidict.md` | mitmproxy.coretypes.multidict | `MultiDict` and `MultiDictView` - dictionary supporting multiple values per key | multidict, data-structure, mutable-mapping, key-value-pair |
| 049 | `049-stable-api-mitmproxy-net-server-spec.md` | mitmproxy.net.server_spec | `ServerSpec` structure and `parse` function for server specification strings | server-specifications, parsing, scheme-host-port |
| 050 | `050-stable-api-mitmproxy-proxy-mode-specs.md` | mitmproxy.proxy.mode_specs | Proxy mode specification parsing: syntax for regular, reverse, socks5 modes | proxy-modes, specification-parsing, configuration-syntax |
| 051 | `051-stable-api-mitmproxy-proxy-context.md` | mitmproxy.proxy.context | `Context` class managing client/server connections, options, and layer stack | context-class, proxy-core, protocol-layers, connection-management |
| 052 | `052-stable-api-mitmproxy-proxy-server-hooks.md` | mitmproxy.proxy.server_hooks | Dataclasses for server/client connection event hooks and lifecycle stages | hooks, connection-events, client-connection, server-connection |

### 9. Other / Dev (053)
*Development-version or empty documents.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 053 | `053-dev-howto-transparent.md` | /howto/transparent/ | Empty document (dev version redirect) | empty-document, no-content |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-004 |
| **CLI Tutorial (mitmproxy)** | 005-009 |
| **Web UI Tutorial (mitmweb)** | 010-014 |
| **Real-World Tutorials** | 015-016 |
| **How It Works & Concepts** | 017-023 |
| **Addon/Script Development** | 024-029 |
| **Deployment & Setup Guides** | 030-035 |
| **Python API Reference** | 036-052 |

### By Concept

| Concept | Files |
|---------|-------|
| **Installation & Setup** | 001, 002, 003 |
| **Traffic Interception** | 006, 011, 017 |
| **Request Modification** | 007, 013 |
| **Request Replay** | 008, 014, 015 |
| **TLS/SSL Certificates** | 019, 032, 034, 040, 041 |
| **Transparent Proxying** | 030, 031, 053 |
| **Filter Expressions** | 022, 033 |
| **Proxy Modes** | 018, 050 |
| **Event Hooks** | 036, 047, 052 |
| **HTTP API Classes** | 037, 038, 039 |
| **Protocol Support (TCP/UDP/DNS/WebSocket)** | 020, 042, 043, 044, 045 |
| **Addon System** | 024, 025, 026, 027, 028, 029 |
| **Content Views** | 027, 046 |
| **Kubernetes** | 035 |
| **Android Emulator** | 032 |
| **Wireshark Integration** | 034 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-004** for introduction, installation, getting started, and feature overview
- Complete CLI tutorial **005-009** OR web UI tutorial **010-014** based on preferred interface

### Level 2: Core Understanding
- Learn how mitmproxy works from files **017-020** (internals, proxy modes, certificates, protocols)
- Configure mitmproxy using files **021-023** (options, filters, commands)

### Level 3: Practical Application
- Follow real-world tutorials in files **015-016** (client replay, GameCenter hacking)
- Set up deployment scenarios with files **030-035** (transparent proxy, VMs, Android, Kubernetes)

### Level 4: Addon Development
- Master addon development with files **024-028** (overview, options, commands, contentviews, examples)
- Review API changes in file **029** for version compatibility

### Level 5: API Reference & Advanced
- Consult event hooks in file **036** for complete addon event reference
- Explore Python API modules in files **037-052** for data structures and internals
- Review protocol-specific APIs: HTTP (038), TCP (043), UDP (044), DNS (042), WebSocket (045), TLS (040)

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression from introduction through advanced API reference.*
