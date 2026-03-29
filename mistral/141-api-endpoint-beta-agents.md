---
title: Beta Agents
url: https://docs.mistral.ai/api/endpoint/beta/agents
source: crawler
fetched_at: 2026-01-29T07:33:20.16806759-03:00
rendered_js: false
word_count: 98
---

## **GET** /v1/agents

Retrieve a list of agent entities sorted by creation time.

*Create a agent that can be used within a conversation.*

## **POST** /v1/agents

Create a new agent giving it instructions, tools, description. The agent is then available to be used as a regular assistant in a conversation or as part of an agent pool from which it can be used.

*Retrieve an agent entity.*

## **GET** /v1/agents/{agent\_id}

Given an agent retrieve an agent entity with its attributes.

## **DELETE** /v1/agents/{agent\_id}

## **PATCH** /v1/agents/{agent\_id}

Update an agent attributes and create a new version.

## **PATCH** /v1/agents/{agent\_id}/version

Switch the version of an agent.