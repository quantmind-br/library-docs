---
title: List machine templates
url: https://docs.factory.ai/api-reference/machine-templates/list-machine-templates.md
source: llms
fetched_at: 2026-03-03T01:12:17.555131-03:00
rendered_js: false
word_count: 63
summary: This document provides the API specification for listing machine templates, detailing request parameters, pagination, and the schema for template metadata.
tags:
    - factory-api
    - machine-templates
    - pagination
    - openapi-spec
    - rest-api
    - infrastructure
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List machine templates

> Returns a paginated list of machine templates for the authenticated organization.



## OpenAPI

````yaml https://api.factory.ai/api/v0/openapi.json get /api/v0/machines/templates
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
  /api/v0/machines/templates:
    get:
      tags:
        - Machine Templates
      summary: List machine templates
      description: >-
        Returns a paginated list of machine templates for the authenticated
        organization.
      operationId: listMachineTemplates
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
                $ref: '#/components/schemas/ListMachineTemplates200ResponseBody'
        '401':
          description: Response for status 401
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMachineTemplates401ResponseBody'
        '403':
          description: Response for status 403
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMachineTemplates403ResponseBody'
        '500':
          description: Response for status 500
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListMachineTemplates500ResponseBody'
components:
  schemas:
    ListMachineTemplates200ResponseBody:
      type: object
      properties:
        templates:
          type: array
          items:
            type: object
            properties:
              templateId:
                type: string
                description: Template ID
              repoUrl:
                anyOf:
                  - type: string
                    format: uri
                  - type: string
                    enum:
                      - ''
                description: Repository URL
              templateName:
                type: string
                description: Human-readable template name
              defaultBranch:
                type: string
                description: Default branch name
              createdBy:
                type: string
                description: User ID of creator
              createdAt:
                type: integer
                description: Creation timestamp (ms)
              buildStatus:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - building
                      - success
                      - failed
                    description: Current build status
                  failureReason:
                    type: string
                    enum:
                      - setup_script_error
                      - system_error
                    description: >-
                      Reason for build failure (only present when status is
                      failed)
                  buildStartedAt:
                    type: integer
                    description: Build start timestamp (ms)
                  builtAt:
                    type: integer
                    description: Build completion timestamp (ms)
                  logs:
                    type: string
                    description: Build logs
                required:
                  - status
                additionalProperties: false
                description: Build status
              lastUpdatedAt:
                type: integer
                nullable: true
                description: Last update timestamp (ms)
              environmentVariables:
                type: array
                items:
                  type: object
                  properties:
                    key:
                      type: string
                      description: Environment variable name
                    value:
                      type: string
                      description: Environment variable value
                  required:
                    - key
                    - value
                  additionalProperties: false
                description: Shared environment variables
              userEnvironmentVariablesByUser:
                type: array
                items:
                  type: object
                  properties:
                    key:
                      type: string
                      description: Environment variable name
                    value:
                      type: string
                      description: Environment variable value
                  required:
                    - key
                    - value
                  additionalProperties: false
                description: User-specific environment variables
              setupScript:
                type: string
                description: Setup script to run after cloning
            required:
              - templateId
              - repoUrl
              - templateName
              - defaultBranch
              - createdBy
            additionalProperties: false
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
        - templates
        - pagination
      additionalProperties: false
    ListMachineTemplates401ResponseBody:
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
    ListMachineTemplates403ResponseBody:
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
    ListMachineTemplates500ResponseBody:
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