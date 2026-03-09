---
title: Create a machine template
url: https://docs.factory.ai/api-reference/machine-templates/create-a-machine-template.md
source: llms
fetched_at: 2026-03-03T01:12:12.438837-03:00
rendered_js: false
word_count: 64
summary: This document provides the API specification for creating machine templates, detailing the required parameters for repository URLs, environment variables, and setup scripts.
tags:
    - machine-templates
    - factory-api
    - api-reference
    - infrastructure-automation
    - openapi-specification
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a machine template

> Creates a new machine template with the specified repository and configuration.



## OpenAPI

````yaml https://api.factory.ai/api/v0/openapi.json post /api/v0/machines/templates
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
    post:
      tags:
        - Machine Templates
      summary: Create a machine template
      description: >-
        Creates a new machine template with the specified repository and
        configuration.
      operationId: createMachineTemplate
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateMachineTemplateRequestBody'
      responses:
        '201':
          description: Response for status 201
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateMachineTemplate201ResponseBody'
        '400':
          description: Response for status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateMachineTemplate400ResponseBody'
        '401':
          description: Response for status 401
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateMachineTemplate401ResponseBody'
        '403':
          description: Response for status 403
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateMachineTemplate403ResponseBody'
        '500':
          description: Response for status 500
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateMachineTemplate500ResponseBody'
components:
  schemas:
    CreateMachineTemplateRequestBody:
      type: object
      properties:
        repoUrl:
          type: string
          format: uri
          description: Repository URL to clone
        templateName:
          type: string
          minLength: 1
          maxLength: 100
          description: Human-readable template name
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
          description: Environment variables to set in the machine
        setupScript:
          type: string
          maxLength: 10000
          description: Setup script to run after cloning
      required:
        - repoUrl
        - templateName
      additionalProperties: false
    CreateMachineTemplate201ResponseBody:
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
              description: Reason for build failure (only present when status is failed)
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
    CreateMachineTemplate400ResponseBody:
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
    CreateMachineTemplate401ResponseBody:
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
    CreateMachineTemplate403ResponseBody:
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
    CreateMachineTemplate500ResponseBody:
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