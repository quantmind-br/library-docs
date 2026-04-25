---
title: Change Status Bot - Evolution API Documentation
url: https://doc.evolution-api.com/v2/api-reference/integrations/dify/change-status
source: sitemap
fetched_at: 2026-04-12T18:49:54.212205865-03:00
rendered_js: false
word_count: 67
summary: This document details the required parameters and process for updating the status of a Dify bot, specifying acceptable values such as opened, paused, or closed.
tags:
    - dify-bot
    - status-update
    - authorization-key
    - api-call
    - whatsapp-bot
category: reference
---

Altera o status do bot Dify

#### Authorizations

Your authorization key header

#### Path Parameters

#### Body

Dados para alterar o status do bot Dify

Example:

`"5511912345678@s.whatsapp.net"`

Status a ser atribuído ao bot Dify. Os valores válidos são `opened`, `paused` e `closed`.

Available options:

`opened`,

`paused`,

`closed`

#### Response

Status do bot Dify alterado com sucesso.

Example:

`"Status do bot Dify alterado para closed com sucesso"`

[Find Dify Settings](https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-settings)[Find Status Bot](https://doc.evolution-api.com/v2/api-reference/integrations/dify/find-status)