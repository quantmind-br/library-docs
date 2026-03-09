---
title: Delete a machine template
url: https://docs.factory.ai/api-reference/machine-templates/delete-a-machine-template.md
source: llms
fetched_at: 2026-03-03T01:12:12.518433-03:00
rendered_js: false
word_count: 62
summary: This document provides the API specification for permanently deleting a machine template and all its associated resources using the Factory Public API.
tags:
    - machine-templates
    - factory-api
    - rest-api
    - openapi
    - endpoint-reference
    - resource-deletion
category: api
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.factory.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a machine template

> Permanently deletes a machine template and all associated resources.



## OpenAPI

````yaml https://api.factory.ai/api/v0/openapi.json delete /api/v0/machines/templates/{templateId}
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
    delete:
      tags:
        - Machine Templates
      summary: Delete a machine template
      description: Permanently deletes a machine template and all associated resources.
      operationId: deleteMachineTemplate
      parameters:
        - name: templateId
          in: path
          required: true
          schema:
            type: string
            description: Template ID
      responses:
        '204':
          description: Response for status 204
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteMachineTemplate204ResponseBody'
        '401':
          description: Response for status 401
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteMachineTemplate401ResponseBody'
        '403':
          description: Response for status 403
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteMachineTemplate403ResponseBody'
        '404':
          description: Response for status 404
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteMachineTemplate404ResponseBody'
        '500':
          description: Response for status 500
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteMachineTemplate500ResponseBody'
components:
  schemas:
    DeleteMachineTemplate204ResponseBody:
      type: object
      properties: {}
      additionalProperties: false
    DeleteMachineTemplate401ResponseBody:
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
    DeleteMachineTemplate403ResponseBody:
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
    DeleteMachineTemplate404ResponseBody:
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
    DeleteMachineTemplate500ResponseBody:
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