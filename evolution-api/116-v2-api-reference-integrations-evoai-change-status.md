---
title: Change Status Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/evoai/change-status
source: sitemap
fetched_at: 2026-04-12T18:49:43.514080698-03:00
rendered_js: false
word_count: 67
summary: This document details the required parameters and structure for an API call designed to change the operational status of an EvoAI bot.
tags:
    - api
    - bot-control
    - status-update
    - whatsapp-bot
    - authorization
    - endpoint
category: reference
---

Altera o status do bot EvoAI

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Dados para alterar o status do bot EvoAI

Example:

`"5511912345678@s.whatsapp.net"`

Status a ser atribuído ao bot EvoAI. Os valores válidos são `opened`, `paused` e `closed`.

Available options:

`opened`,

`paused`,

`closed`

#### Response

Status do bot EvoAI alterado com sucesso.

Example:

`"Status do bot EvoAI alterado para closed com sucesso"`

[Find EvoAI Settings](https://doc.evolution-api.com/v2/api-reference/integrations/evoai/find-settings)[Find Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/evoai/find-status)