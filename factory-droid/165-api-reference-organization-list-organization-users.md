---
title: List organization users
url: https://docs.factory.ai/api-reference/organization/list-organization-users.md
source: llms
fetched_at: 2026-03-03T01:12:19.158506-03:00
rendered_js: false
word_count: 62
summary: This document provides the OpenAPI specification for the Factory API endpoint used to retrieve a paginated list of organization users, detailing request parameters and response schemas.
tags:
    - factory-api
    - user-management
    - organization-users
    - pagination
    - rest-api
    - openapi-spec
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List organization users

> Returns a paginated list of users in the Factory organization.



## OpenAPI

````yaml https://api.factory.ai/api/v0/openapi.json get /api/v0/organization/users
openapi: 3.0.1
info:
  title: Factory Public API
  description: >-
    Public API for Factory platform. Requires authentication via the
    `Authorization: Bearer` header.
  version: 0.1.0
servers:
  - url: https://api.factory.ai/
    description: Production
security:
  - BearerAuth: []
paths:
  /api/v0/organization/users:
    get:
      tags:
        - Organization
      summary: List organization users
      description: Returns a paginated list of users in the Factory organization.
      operationId: listOrganizationUsers
      parameters:
        - name: limit
          in: query
          required: false
          schema:
            type: string
            default: '20'
            description: Maximum number of items to return (1-100)
        - name: cursor
          in: query
          required: false
          schema:
            type: string
            description: Cursor for pagination
      responses:
        '200':
          description: Response for status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationUsers200ResponseBody'
        '401':
          description: Response for status 401
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationUsers401ResponseBody'
        '403':
          description: Response for status 403
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationUsers403ResponseBody'
        '500':
          description: Response for status 500
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListOrganizationUsers500ResponseBody'
components:
  schemas:
    ListOrganizationUsers200ResponseBody:
      type: object
      properties:
        users:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                description: WorkOS user ID
              email:
                type: string
                format: email
                description: User email address
              firstName:
                type: string
                description: User first name
              lastName:
                type: string
                description: User last name
              createdAt:
                type: string
                description: ISO 8601 timestamp of user creation
              lastSignInAt:
                type: string
                description: ISO 8601 timestamp of last sign in
              metadata:
                type: object
                additionalProperties:
                  type: string
                description: Custom metadata for the user
            required:
              - id
              - email
              - createdAt
              - metadata
            additionalProperties: false
          description: List of users
        pagination:
          type: object
          properties:
            hasMore:
              type: boolean
              description: Whether there are more items after this page
            nextCursor:
              type: string
              nullable: true
              description: Cursor to use for the next page, null if no more pages
          required:
            - hasMore
            - nextCursor
          additionalProperties: false
      required:
        - users
        - pagination
      additionalProperties: false
    ListOrganizationUsers401ResponseBody:
      type: object
      properties:
        detail:
          type: string
          description: Human-readable error message
        status:
          type: number
          description: HTTP status code
        title:
          type: string
          description: HTTP status title
        metadata:
          type: object
          additionalProperties: {}
          description: Additional error metadata
      required:
        - detail
        - status
        - title
      additionalProperties: false
    ListOrganizationUsers403ResponseBody:
      type: object
      properties:
        detail:
          type: string
          description: Human-readable error message
        status:
          type: number
          description: HTTP status code
        title:
          type: string
          description: HTTP status title
        metadata:
          type: object
          additionalProperties: {}
          description: Additional error metadata
      required:
        - detail
        - status
        - title
      additionalProperties: false
    ListOrganizationUsers500ResponseBody:
      type: object
      properties:
        detail:
          type: string
          description: Human-readable error message
        status:
          type: number
          description: HTTP status code
        title:
          type: string
          description: HTTP status title
        metadata:
          type: object
          additionalProperties: {}
          description: Additional error metadata
      required:
        - detail
        - status
        - title
      additionalProperties: false
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Factory API key or JWT token for authentication

````