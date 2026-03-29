---
title: MCP with Federated Auth
url: https://docs.getbifrost.ai/enterprise/mcp-with-fa.md
source: llms
fetched_at: 2026-01-21T19:43:29.916150074-03:00
rendered_js: false
word_count: 292
summary: This document explains how to transform private enterprise APIs into LLM-ready Model Context Protocol tools using federated authentication and various import methods like OpenAPI and Postman.
tags:
    - mcp
    - federated-authentication
    - api-integration
    - llm-tools
    - openapi
    - enterprise-security
    - zero-trust
category: guide
---

# MCP with Federated Auth

> Transform your existing private enterprise APIs into LLM-ready MCP tools using federated authentication without writing a single line of code

Transform your existing private enterprise APIs into LLM-ready MCP tools instantly. Add your APIs along with authentication information, and Bifrost dynamically syncs user authentication to allow these existing APIs to be used as MCP tools.

## Supported Import Methods

Add your existing APIs to Bifrost using any of these methods:

<Tabs>
  <Tab title="Postman Collection">
    Import your existing Postman collections directly into Bifrost. All request configurations, headers, and parameters are preserved.

    ```json  theme={null}
    {
      "info": {
        "name": "Enterprise API Collection",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
      },
      "item": [
        {
          "name": "Get User Profile",
          "request": {
            "method": "GET",
            "header": [
              {
                "key": "Authorization",
                "value": "{{req.header.authorization}}",
                "type": "text"
              }
            ],
            "url": {
              "raw": "https://api.company.com/users/profile",
              "host": ["api", "company", "com"],
              "path": ["users", "profile"]
            }
          }
        }
      ]
    }
    ```
  </Tab>

  <Tab title="OpenAPI Spec">
    Use your existing OpenAPI 3.0+ specifications. Bifrost automatically converts them into MCP-compatible tools.

    ```yaml  theme={null}
    openapi: 3.0.0
    info:
      title: Enterprise API
      version: 1.0.0
    paths:
      /users/profile:
        get:
          summary: Get user profile
          security:
            - BearerAuth: []
          parameters:
            - name: Authorization
              in: header
              schema:
                type: string
              example: "{{req.header.authorization}}"
    components:
      securitySchemes:
        BearerAuth:
          type: http
          scheme: bearer
    ```
  </Tab>

  <Tab title="cURL Commands">
    Convert your existing cURL commands directly into MCP tools.

    ```bash  theme={null}
    curl -X GET "https://api.company.com/users/profile" \
      -H "Authorization: {{req.header.authorization}}" \
      -H "Content-Type: application/json"
    ```
  </Tab>

  <Tab title="Built-in UI">
    Use Bifrost's intuitive UI to manually configure your API endpoints with the same ease as Postman.

    1. Set HTTP method and URL
    2. Configure headers with variable substitution
    3. Define request body (if needed)
    4. Test the endpoint
    5. Deploy as MCP tool
  </Tab>
</Tabs>

## What Happens Next

Once you upload your API specifications, Bifrost automatically:

* **Syncs authentication systems** from your existing APIs
* **Converts endpoints** into MCP-compatible tools
* **Maintains security** using your current auth infrastructure
* **Makes APIs available** to LLMs instantly

## Supported Authentication Types

Bifrost automatically handles all common authentication patterns:

* **Bearer Tokens** (JWT, OAuth)
* **API Keys** (headers, query parameters)
* **Custom Headers** (tenant IDs, user tokens)
* **Basic Auth** and other standard methods

## Real-World Use Cases

### Enterprise CRM Integration

Transform your Salesforce, HubSpot, or custom CRM APIs:

```json  theme={null}
{
  "name": "Get Customer Data",
  "method": "GET",
  "url": "https://api.company.com/crm/customers/{{req.body.customer_id}}",
  "headers": {
    "Authorization": "{{req.header.authorization}}",
    "X-Tenant-ID": "{{req.header.x-tenant-id}}"
  }
}
```

### Internal Microservices

Make your internal microservices LLM-accessible:

```yaml  theme={null}
paths:
  /internal/user-service/profile:
    get:
      parameters:
        - name: Authorization
          in: header
          schema:
            type: string
            default: "{{req.header.authorization}}"
        - name: X-Service-Token
          in: header
          schema:
            type: string
            default: "{{env.INTERNAL_SERVICE_TOKEN}}"
```

### Database APIs

Connect to your database APIs securely:

```http  theme={null}
POST https://db-api.company.com/query
Content-Type: application/json
Authorization: {{req.header.authorization}}
X-Database-Name: {{req.header.x-database}}

{
  "query": "SELECT * FROM users WHERE tenant_id = '{{req.body.tenant_id}}'",
  "limit": 100
}
```

## Security Benefits

### 1. **Zero Trust Architecture**

* Authentication happens at the edge (your existing systems)
* Bifrost never stores or caches authentication credentials
* Each request is authenticated independently

### 2. **Existing Security Policies**

* Leverage your current RBAC (Role-Based Access Control)
* Maintain existing audit trails
* No changes to security infrastructure required

### 3. **Granular Access Control**

* Different users get different API access based on their credentials
* Tenant isolation maintained through existing headers
* API rate limiting and quotas preserved

### 4. **Compliance Friendly**

* No sensitive data passes through Bifrost permanently
* Existing compliance frameworks remain intact
* Audit trails maintained in your systems


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt