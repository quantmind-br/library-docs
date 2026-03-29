---
title: Beta Libraries
url: https://docs.mistral.ai/api/endpoint/beta/libraries
source: crawler
fetched_at: 2026-01-29T07:33:21.276652779-03:00
rendered_js: false
word_count: 114
summary: This document details the REST API endpoints available for managing library resources, including functionality for creating, listing, updating, and deleting libraries.
tags:
    - rest-api
    - libraries-api
    - crud-operations
    - endpoint-reference
    - resource-management
category: api
---

*List all libraries you have access to.*

## **GET** /v1/libraries

List all libraries that you have created or have been shared with you.

## **POST** /v1/libraries

Create a new Library, you will be marked as the owner and only you will have the possibility to share it with others. When first created this will only be accessible by you.

*Detailed information about a specific Library.*

## **GET** /v1/libraries/{library\_id}

Given a library id, details information about that Library.

## **PUT** /v1/libraries/{library\_id}

Given a library id, you can update the name and description.

*Delete a library and all of it's document.*

## **DELETE** /v1/libraries/{library\_id}

Given a library id, deletes it together with all documents that have been uploaded to that library.