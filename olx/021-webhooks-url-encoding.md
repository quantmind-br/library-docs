---
title: Codificação de URL
url: https://developers.olx.com.br/webhooks/url_encoding.html
source: crawler
fetched_at: 2026-02-07T15:17:23.195041234-03:00
rendered_js: false
word_count: 56
summary: This document outlines the required URL structures and formatting for configuring notification endpoints, specifically detailing how to include advertiser identifiers in paths or subdomains.
tags:
    - url-encoding
    - endpoint-configuration
    - notification-api
    - advertiser-id
    - integration-setup
category: configuration
---

## Codificação de URL

#### Exemplos de endpoints que poderão ser utilizados:

```
https://yourdomain.com.br/grupoolx/notification/ID-DO-ANUNCIANTE
```

```
https://seudominio.com.br/grupoolx/notification/123456
```

OU

```
https://ID-DO-ANUNCIANTE.yourdomain.com.br/grupoolx/notification
```

```
https://autosxpto.seudominio.com.br/grupoolx/notification
```

ID-DO-ANUNCIANTE é parte da URL que representa o identificador do anunciante no sistema que irá receber a requisição. É uma forma de identificação do cliente no Integrador.

Caso não tenha ou não queira especificar o ID-DO-ANUNCIANTE o endpoint poderá ser implementado sem este identificador.

#### Exemplos

```
https://yourdomain.com.br/grupoolx/notification
```