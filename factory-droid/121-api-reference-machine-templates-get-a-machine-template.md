---
title: Get a machine template
url: https://docs.factory.ai/api-reference/machine-templates/get-a-machine-template.md
source: llms
fetched_at: 2026-02-05T21:40:12.469823592-03:00
rendered_js: false
word_count: 60
summary: Provides technical specifications for the GET /api/v0/machines/templates/{templateId} endpoint to retrieve detailed information about a machine template.
tags:
    - machine-templates
    - api-endpoint
    - factory-api
    - openapi
    - rest-api
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a machine template

> Returns details of a specific machine template.



## OpenAPI

````yaml https://api.factory.ai/api/v0/openapi.json get /api/v0/machines/templates/{templateId}
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
  /api/v0/machines/templates/{templateId}:
    get:
      tags:
        - Machine Templates
      summary: Get a machine template
      description: Returns details of a specific machine template.
      operationId: getMachineTemplate
      parameters:
        - name: templateId
          in: path
          required: true
          schema:
            type: string
            description: Template ID
      responses:
        '200':
          description: Response for status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMachineTemplate200ResponseBody'
        '400':
          description: Response for status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMachineTemplate400ResponseBody'
        '401':
          description: Response for status 401
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMachineTemplate401ResponseBody'
        '403':
          description: Response for status 403
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMachineTemplate403ResponseBody'
        '404':
          description: Response for status 404
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMachineTemplate404ResponseBody'
        '500':
          description: Response for status 500
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetMachineTemplate500ResponseBody'
components:
  schemas:
    GetMachineTemplate200ResponseBody:
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
    GetMachineTemplate400ResponseBody:
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
    GetMachineTemplate401ResponseBody:
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
    GetMachineTemplate403ResponseBody:
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
    GetMachineTemplate404ResponseBody:
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
    GetMachineTemplate500ResponseBody:
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