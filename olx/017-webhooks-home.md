---
title: Notificação via Webhooks
url: https://developers.olx.com.br/webhooks/home.html
source: crawler
fetched_at: 2026-02-07T15:17:09.034687949-03:00
rendered_js: false
word_count: 137
summary: This document explains how to integrate and receive automated notifications about ad statuses and other events through a webhook system using HTTP POST requests.
tags:
    - webhooks
    - api-integration
    - notifications
    - ad-status
    - http-post
category: guide
---

## Notificação via Webhooks

Webhook é um método de comunicação entre diferentes aplicações, facilitando e agilizando a troca de informações em entre elas.

Isso permite configurar o envio de notificações automáticas, assim que um evento relevante acontece em um sistema, bastando definir para qual URL cada webhook deve ser enviado quando os eventos ocorrerem.

Este documento contém as informações para que seja possível realizar integrações com nossa API. Assim, o integrador poderá receber as notificações referente aos anúncios dos nossos anunciantes e/ou outras informações que estejam disponíveis e configuradas.

Nosso sistema notificará os integradores sobre o status dos anúncios importados nas URLs (endpoints) configuradas. Esta requisição será realizada via protocolo HTTP no verbo POST, no endpoint especificado passando um JSON como corpo do request.

- [Modelo de notificações](https://developers.olx.com.br/webhooks/notifications_model.html);
- [Configuração de Notificações](https://developers.olx.com.br/webhooks/notifications_configuration.html);
- [Notificação de Status de Anúncios](https://developers.olx.com.br/webhooks/notifications_ad_status.html);
- [Codificação de URL](https://developers.olx.com.br/webhooks/url_encoding.html).