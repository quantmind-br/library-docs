---
title: Change Status Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/n8n/change-status
source: sitemap
fetched_at: 2026-04-12T18:48:43.538587561-03:00
rendered_js: false
word_count: 67
summary: This document details the API endpoint required to modify the status of an n8n bot, specifying the necessary path parameters and body data.
tags:
    - n8n
    - api-endpoint
    - bot-status
    - automation
    - update
    - authorization
category: reference
---

Altera o status do bot n8n

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Dados para alterar o status do bot n8n

Example:

`"5511912345678@s.whatsapp.net"`

Status a ser atribuído ao bot n8n. Os valores válidos são `opened`, `paused` e `closed`.

Available options:

`opened`,

`paused`,

`closed`

#### Response

Status do bot n8n alterado com sucesso.

Example:

`"Status do bot n8n alterado para closed com sucesso"`

[Find n8n Settings](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/find-settings)[Find Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/n8n/find-status)