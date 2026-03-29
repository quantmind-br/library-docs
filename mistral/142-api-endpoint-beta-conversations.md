---
title: Beta Conversations
url: https://docs.mistral.ai/api/endpoint/beta/conversations
source: crawler
fetched_at: 2026-01-29T07:33:20.649205061-03:00
rendered_js: false
word_count: 320
summary: A guide on conducting feedback discussions and user interviews during the beta testing phase of a product.
tags:
    - beta testing
    - user feedback
    - product development
    - interviews
category: guide
---

*List all created conversations.*

## **GET** /v1/conversations

Retrieve a list of conversation entities sorted by creation time.

*Create a conversation and append entries to it.*

## **POST** /v1/conversations

Create a new conversation, using a base model or an agent and append entries. Completion and tool executions are run and the response is appended to the conversation.Use the returned conversation\_id to continue the conversation.

*Retrieve a conversation information.*

## **GET** /v1/conversations/{conversation\_id}

Given a conversation\_id retrieve a conversation entity with its attributes.

*Append new entries to an existing conversation.*

## **POST** /v1/conversations/{conversation\_id}

Run completion on the history of the conversation and the user entries. Return the new created entries.

## **DELETE** /v1/conversations/{conversation\_id}

Delete a conversation given a conversation\_id.

*Retrieve all entries in a conversation.*

## **GET** /v1/conversations/{conversation\_id}/history

Given a conversation\_id retrieve all the entries belonging to that conversation. The entries are sorted in the order they were appended, those can be messages, connectors or function\_call.

*Retrieve all messages in a conversation.*

## **GET** /v1/conversations/{conversation\_id}/messages

Given a conversation\_id retrieve all the messages belonging to that conversation. This is similar to retrieving all entries except we filter the messages only.

*Restart a conversation starting from a given entry.*

## **POST** /v1/conversations/{conversation\_id}/restart

Given a conversation\_id and an id, recreate a conversation from this point and run completion. A new conversation is returned with the new entries returned.

*Create a conversation and append entries to it.*

## **POST** /v1/conversations#stream

Create a new conversation, using a base model or an agent and append entries. Completion and tool executions are run and the response is appended to the conversation.Use the returned conversation\_id to continue the conversation.

*Append new entries to an existing conversation.*

## **POST** /v1/conversations/{conversation\_id}#stream

Run completion on the history of the conversation and the user entries. Return the new created entries.

*Restart a conversation starting from a given entry.*

## **POST** /v1/conversations/{conversation\_id}/restart#stream

Given a conversation\_id and an id, recreate a conversation from this point and run completion. A new conversation is returned with the new entries returned.