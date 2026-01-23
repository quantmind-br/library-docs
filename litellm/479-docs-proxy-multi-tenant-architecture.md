---
title: Multi-Tenant Architecture with LiteLLM | liteLLM
url: https://docs.litellm.ai/docs/proxy/multi_tenant_architecture
source: sitemap
fetched_at: 2026-01-21T19:53:05.648992145-03:00
rendered_js: false
word_count: 2051
summary: This document explains LiteLLM's hierarchical multi-tenant architecture for managing LLM access, cost attribution, and isolation across organizations, teams, and users.
tags:
    - multi-tenancy
    - litellm
    - access-control
    - rbac
    - cost-tracking
    - organizational-hierarchy
category: concept
---

## Overview[​](#overview "Direct link to Overview")

LiteLLM provides a centralized solution that scales across multiple tenants, enabling organizations to:

- **Centrally manage** LLM access for multiple tenants (organizations, teams, departments)
- **Isolate spend and usage** across different organizational units
- **Delegate administration** without compromising security
- **Track costs** at granular levels (organization → team → user → key)
- **Scale seamlessly** as new teams and users are added

Open Source vs. Enterprise

- **Teams + Virtual Keys**: ✅ Available in open source
- **Organizations + Org Admins**: ✨ Enterprise feature ([Get a 7 day trial](https://www.litellm.ai/#trial))

You can implement multi-tenancy using **Teams** alone in the open source version, or add **Organizations** on top for additional hierarchy in the enterprise version.

## The Multi-Tenant Challenge[​](#the-multi-tenant-challenge "Direct link to The Multi-Tenant Challenge")

Organizations with multi-tenant architectures face several challenges when deploying LLM solutions:

1. **Centralized vs. Decentralized**: Need a single unified gateway while maintaining tenant isolation
2. **Cost Attribution**: Tracking spend across different business units, departments, or customers
3. **Access Control**: Different teams need different models, budgets, and rate limits
4. **Delegation**: Team leads should manage their teams without platform-wide admin access
5. **Scalability**: Solution must scale from 10 to 10,000+ users without architectural changes

## How LiteLLM Solves Multi-Tenancy[​](#how-litellm-solves-multi-tenancy "Direct link to How LiteLLM Solves Multi-Tenancy")

LiteLLM implements a hierarchical multi-tenant architecture with four levels:

### 1. Organizations (Top-Level Tenants) ✨ Enterprise Feature[​](#1-organizations-top-level-tenants--enterprise-feature "Direct link to 1. Organizations (Top-Level Tenants) ✨ Enterprise Feature")

**Organizations** represent the highest level of tenant isolation - typically different business units, departments, or customers.

- Each organization has its own:
  
  - Budget limits
  - Allowed models
  - Admin users (org admins)
  - Teams
  - Spend tracking

**Use Cases:**

- **Enterprise Departments**: Separate organizations for Engineering, Marketing, Sales
- **Multi-Customer SaaS**: Each customer is an organization with full isolation
- **Geographic Regions**: EMEA, APAC, Americas as separate organizations

**Key Features:**

- Organizations cannot see each other's data
- Each organization can have multiple teams
- Organization admins manage teams within their organization only
- Spend and usage tracked at organization level

[API Reference for Organizations](https://litellm-api.up.railway.app/#/organization%20management)

* * *

### 2. Teams (Mid-Level Grouping) ✅ Open Source[​](#2-teams-mid-level-grouping--open-source "Direct link to 2. Teams (Mid-Level Grouping) ✅ Open Source")

**Teams** can work independently or sit within organizations, representing logical groupings of users working together.

tip

Teams are available in **open source** and can be used as your primary multi-tenant boundary without needing Organizations. Organizations provide an additional layer of hierarchy for enterprise deployments.

- Each team has:
  
  - Team-specific budgets and rate limits
  - Team admins who manage members
  - Service account keys for shared resources
  - Model access controls
  - Granular team member permissions

**Use Cases:**

- **Project Teams**: ML Research team, Product team, Data Science team
- **Customer Sub-Groups**: Different divisions within a customer organization
- **Environment Separation**: Development, Staging, Production teams

**Key Features:**

- Teams inherit organization constraints (can't exceed org budget/models)
- Team admins can manage their team without affecting others
- Service account keys survive team member changes
- Per-team spend tracking and billing

[API Reference for Teams](https://litellm-api.up.railway.app/#/team%20management)

* * *

### 3. Users (Individual Members) ✅ Open Source[​](#3-users-individual-members--open-source "Direct link to 3. Users (Individual Members) ✅ Open Source")

**Users** are individuals who belong to teams and create/use API keys.

- Each user can:
  
  - Belong to multiple teams
  - Have their own budget limits
  - Create personal API keys
  - Track individual spend

**User Types:**

- **Internal Users**: Employees, developers, data scientists
- **Team Admins**: Lead their teams, manage members
- **Org Admins**: Manage multiple teams within their organization
- **Proxy Admins**: Platform-wide administrators

**Key Features:**

- User spend tracked individually
- Users can be on multiple teams simultaneously
- Role-based permissions control what users can do
- User keys deleted when user is removed

[API Reference for Users](https://litellm-api.up.railway.app/#/user%20management)

* * *

### 4. Virtual Keys (Authentication Layer) ✅ Open Source[​](#4-virtual-keys-authentication-layer--open-source "Direct link to 4. Virtual Keys (Authentication Layer) ✅ Open Source")

**Virtual Keys** are the API keys used to authenticate requests and track spend.

Each key can be one of three types:

Key TypeConfigurationUse CaseSpend TrackingLifecycle**User-only**`user_id` onlyDeveloper personal keysUser levelDeleted with user**Team Service Account**`team_id` onlyProduction apps, CI/CDTeam levelSurvives member changes**User + Team**Both `user_id` and `team_id`User within team contextUser AND TeamDeleted with user

**Example Scenarios:**

- Use **user-only keys** for developers testing locally
- Use **team service account keys** for your production application that shouldn't break when employees leave
- Use **user + team keys** when you want individual accountability within a team budget

[API Reference for Keys](https://litellm-api.up.railway.app/#/key%20management)

* * *

## Role-Based Access Control (RBAC)[​](#role-based-access-control-rbac "Direct link to Role-Based Access Control (RBAC)")

LiteLLM provides granular RBAC across the hierarchy:

### Global Proxy Roles (Platform-Wide)[​](#global-proxy-roles-platform-wide "Direct link to Global Proxy Roles (Platform-Wide)")

RoleScopePermissions**Proxy Admin**Entire platformCreate orgs, teams, users. View all spend. Full control.**Proxy Admin Viewer**Entire platformView-only access to all data. Cannot make changes.**Internal User**Own resourcesCreate/delete own keys. View own spend.

### Organization/Team Roles (Scoped)[​](#organizationteam-roles-scoped "Direct link to Organization/Team Roles (Scoped)")

RoleScopePermissions**Org Admin** ✨Specific organizationCreate teams, add users, view org spend within their org only.**Team Admin** ✨Specific teamManage team members, budgets, keys within their team only.

✨ = Premium Feature

### Team Member Permissions[​](#team-member-permissions "Direct link to Team Member Permissions")

Team admins can configure granular permissions for regular team members:

**Read-only** (default):

```
["/key/info","/key/health"]
```

**Allow key creation**:

```
["/key/info","/key/health","/key/generate","/key/update"]
```

**Full key management**:

```
["/key/info","/key/health","/key/generate","/key/update","/key/delete","/key/regenerate","/key/block","/key/unblock"]
```

[Learn more about RBAC](https://docs.litellm.ai/docs/proxy/access_control)

* * *

## Spend Tracking & Cost Attribution[​](#spend-tracking--cost-attribution "Direct link to Spend Tracking & Cost Attribution")

LiteLLM provides multi-level spend tracking that flows through the hierarchy:

### Hierarchical Spend Flow[​](#hierarchical-spend-flow "Direct link to Hierarchical Spend Flow")

```
Organization Spend
    ├── Team 1 Spend
    │   ├── User A Spend
    │   │   ├── Key 1 Spend
    │   │   └── Key 2 Spend
    │   └── Service Account Spend
    │       └── Key 3 Spend
    └── Team 2 Spend
        └── User B Spend
            └── Key 4 Spend
```

### Budget Enforcement[​](#budget-enforcement "Direct link to Budget Enforcement")

Budgets can be set at every level with inheritance:

1. **Organization Budget**: `$10,000/month`
   
   - Team 1: `$6,000/month` (within org limit)
     
     - User A: `$3,000/month` (within team limit)
     - User B: `$3,000/month` (within team limit)
   - Team 2: `$4,000/month` (within org limit)

**Enforcement Rules:**

- Team budgets cannot exceed organization budget
- User budgets cannot exceed team budget
- Requests blocked when any level exceeds budget
- Real-time tracking prevents overruns

[Learn more about Budgets](https://docs.litellm.ai/docs/proxy/team_budgets)

* * *

## Common Multi-Tenant Patterns[​](#common-multi-tenant-patterns "Direct link to Common Multi-Tenant Patterns")

### Pattern 1: Enterprise Departments[​](#pattern-1-enterprise-departments "Direct link to Pattern 1: Enterprise Departments")

**Scenario**: Large enterprise with multiple departments needing centralized LLM access

**Enterprise Setup** (with Organizations):

```
Platform (LiteLLM Instance)
├── Engineering Organization ✨
│   ├── Backend Team
│   ├── Frontend Team
│   └── ML Team
├── Marketing Organization ✨
│   ├── Content Team
│   └── Analytics Team
└── Sales Organization ✨
    ├── Sales Ops Team
    └── Customer Success Team
```

**Open Source Alternative** (Teams only):

```
Platform (LiteLLM Instance)
├── Engineering Backend Team
├── Engineering Frontend Team
├── Engineering ML Team
├── Marketing Content Team
├── Marketing Analytics Team
├── Sales Ops Team
└── Customer Success Team
```

**Benefits:**

- Each department/team manages their own budget
- Department leads (org/team admins) control their teams
- Centralized billing and model access
- Cross-department cost visibility for finance

* * *

### Pattern 2: Multi-Customer SaaS[​](#pattern-2-multi-customer-saas "Direct link to Pattern 2: Multi-Customer SaaS")

**Scenario**: SaaS provider offering LLM-powered features to multiple customers

**Enterprise Setup** (with Organizations):

```
Platform (LiteLLM Instance)
├── Customer A Organization ✨
│   ├── Production Team (Service Accounts)
│   ├── Development Team
│   └── QA Team
├── Customer B Organization ✨
│   ├── Production Team (Service Accounts)
│   └── Development Team
└── Customer C Organization ✨
    └── Production Team (Service Accounts)
```

**Open Source Alternative** (Teams only):

```
Platform (LiteLLM Instance)
├── Customer A Production Team (Service Accounts)
├── Customer A Development Team
├── Customer A QA Team
├── Customer B Production Team (Service Accounts)
├── Customer B Development Team
└── Customer C Production Team (Service Accounts)
```

**Benefits:**

- Complete isolation between customers/teams
- Per-customer/team billing and usage tracking
- Customer/team admins can self-serve
- Production service account keys survive employee turnover

* * *

### Pattern 3: Environment Separation[​](#pattern-3-environment-separation "Direct link to Pattern 3: Environment Separation")

**Scenario**: Single organization with multiple environments

```
Platform (LiteLLM Instance)
└── Company Organization
    ├── Production Team
    │   └── Service Account Keys (strict rate limits)
    ├── Staging Team
    │   └── Service Account Keys (moderate limits)
    └── Development Team
        └── User Keys (generous limits for testing)
```

**Benefits:**

- Separate budgets for each environment
- Different model access (production vs. development)
- Prevent development usage from affecting production budget
- Easy cost attribution by environment

* * *

## Delegation & Self-Service[​](#delegation--self-service "Direct link to Delegation & Self-Service")

One of LiteLLM's key advantages is delegated administration:

### Without LiteLLM[​](#without-litellm "Direct link to Without LiteLLM")

```
Every team → Requests platform admin → Admin makes changes
```

❌ Bottleneck on platform team  
❌ Slow onboarding  
❌ Poor scalability

### With LiteLLM[​](#with-litellm "Direct link to With LiteLLM")

```
Proxy Admin → Creates org + org admin
Org Admin → Creates teams + team admins  
Team Admin → Manages their team independently
```

✅ Decentralized management  
✅ Fast onboarding  
✅ Scales to thousands of users

### Self-Service Capabilities[​](#self-service-capabilities "Direct link to Self-Service Capabilities")

**Team Admins Can:**

- Add/remove team members
- Create API keys for team members
- Update team budgets (within org limits)
- Configure team member permissions
- View team usage and spend

**Org Admins Can:**

- Create new teams within their organization
- Assign team admins
- View organization-wide spend
- Manage users across their teams

**Platform Admins Can:**

- Create organizations
- Assign org admins
- Set organization-level policies
- View platform-wide analytics

* * *

## Scalability[​](#scalability "Direct link to Scalability")

LiteLLM's architecture scales from small teams to enterprise deployments:

### Small Team (10-100 users)[​](#small-team-10-100-users "Direct link to Small Team (10-100 users)")

- Single organization
- Few teams (5-10)
- Proxy admins manage everything

### Mid-Size (100-1,000 users)[​](#mid-size-100-1000-users "Direct link to Mid-Size (100-1,000 users)")

- Multiple organizations
- Many teams (50+)
- Org admins delegate to team admins

### Enterprise (1,000+ users)[​](#enterprise-1000-users "Direct link to Enterprise (1,000+ users)")

- Many organizations (departments/regions)
- Hundreds of teams
- Fully delegated admin structure
- Centralized observability and billing

**Key Scalability Features:**

- No architectural changes needed as you grow
- Database-backed (PostgreSQL) for reliability
- Horizontal scaling support
- Efficient spend tracking and logging

* * *

## Security & Isolation[​](#security--isolation "Direct link to Security & Isolation")

### Tenant Isolation[​](#tenant-isolation "Direct link to Tenant Isolation")

Each tenant (organization) is isolated:

- ✅ Cannot view other organizations' data
- ✅ Cannot access other organizations' keys
- ✅ Cannot exceed their budget limits
- ✅ Cannot access models not in their allowed list

### Authentication Security[​](#authentication-security "Direct link to Authentication Security")

- Master key for platform admins
- Virtual keys with scoped permissions
- SSO integration support
- JWT authentication
- IP allowlisting

### Audit & Compliance[​](#audit--compliance "Direct link to Audit & Compliance")

- All API calls logged with user/team/org context
- Spend tracking for chargeback/showback
- Admin actions audited
- Integration with observability tools

[Learn more about Security](https://docs.litellm.ai/docs/data_security)

* * *

## Getting Started[​](#getting-started "Direct link to Getting Started")

Enterprise vs. Open Source Setup

The steps below show the **full enterprise hierarchy** with Organizations.

For **open source**, skip Steps 1-2 and start directly with **Step 3** (creating teams). Teams can function as your top-level tenant boundary without Organizations.

### Step 1: Set Up Organizations ✨ Enterprise[​](#step-1-set-up-organizations--enterprise "Direct link to Step 1: Set Up Organizations ✨ Enterprise")

Create your first organization:

```
curl --location 'http://0.0.0.0:4000/organization/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        "organization_alias": "engineering_department",
        "models": ["gpt-4", "gpt-4o", "claude-3-5-sonnet"],
        "max_budget": 10000
    }'
```

### Step 2: Add an Organization Admin ✨ Enterprise[​](#step-2-add-an-organization-admin--enterprise "Direct link to Step 2: Add an Organization Admin ✨ Enterprise")

```
curl -X POST 'http://0.0.0.0:4000/organization/member_add' \
    -H 'Authorization: Bearer sk-1234' \
    -H 'Content-Type: application/json' \
    -d '{
        "organization_id": "org-123",
        "member": {
            "role": "org_admin",
            "user_id": "admin@company.com"
        }
    }'
```

### Step 3: Create Teams ✅ Open Source[​](#step-3-create-teams--open-source "Direct link to Step 3: Create Teams ✅ Open Source")

**For Enterprise:** Organization admin creates team within their organization  
**For Open Source:** Proxy admin creates team directly (no `organization_id` needed)

```
# Enterprise: Org admin creates team in their organization
curl --location 'http://0.0.0.0:4000/team/new' \
    --header 'Authorization: Bearer sk-org-admin-key' \
    --header 'Content-Type: application/json' \
    --data '{
        "team_alias": "ml_team",
        "organization_id": "org-123",
        "max_budget": 5000
    }'

# Open Source: Proxy admin creates team directly
curl --location 'http://0.0.0.0:4000/team/new' \
    --header 'Authorization: Bearer sk-1234' \
    --header 'Content-Type: application/json' \
    --data '{
        "team_alias": "ml_team",
        "max_budget": 5000
    }'
```

### Step 4: Add Team Admin[​](#step-4-add-team-admin "Direct link to Step 4: Add Team Admin")

```
curl -X POST 'http://0.0.0.0:4000/team/member_add' \
    -H 'Authorization: Bearer sk-org-admin-key' \
    -H 'Content-Type: application/json' \
    -d '{
        "team_id": "team-456",
        "member": {
            "role": "admin",
            "user_id": "team-lead@company.com"
        }
    }'
```

### Step 5: Team Admin Manages Their Team[​](#step-5-team-admin-manages-their-team "Direct link to Step 5: Team Admin Manages Their Team")

```
# Team admin adds members
curl -X POST 'http://0.0.0.0:4000/team/member_add' \
    -H 'Authorization: Bearer sk-team-admin-key' \
    -H 'Content-Type: application/json' \
    -d '{
        "team_id": "team-456",
        "member": {
            "role": "user",
            "user_id": "developer@company.com"
        }
    }'

# Team admin creates keys for members
curl --location 'http://0.0.0.0:4000/key/generate' \
    --header 'Authorization: Bearer sk-team-admin-key' \
    --header 'Content-Type: application/json' \
    --data '{
        "user_id": "developer@company.com",
        "team_id": "team-456"
    }'
```

* * *

## Use Case Examples[​](#use-case-examples "Direct link to Use Case Examples")

### Example 1: Chargeback Model[​](#example-1-chargeback-model "Direct link to Example 1: Chargeback Model")

**Goal**: Each business unit pays for their own LLM usage

**Setup:**

1. Create organization per business unit
2. Set budgets based on allocated budgets
3. Track spend per organization
4. Generate monthly reports for finance

**Result**: Finance can charge back costs to respective departments with accurate attribution.

* * *

### Example 2: Customer-Facing AI Product[​](#example-2-customer-facing-ai-product "Direct link to Example 2: Customer-Facing AI Product")

**Goal**: Provide LLM capabilities to customers with isolation and cost tracking

**Setup:**

1. Create organization per customer
2. Use service account keys for production workloads
3. Track spend per customer organization
4. Set rate limits per customer tier

**Result**: Bill customers accurately, prevent noisy neighbors, maintain isolation.

* * *

### Example 3: Development vs. Production[​](#example-3-development-vs-production "Direct link to Example 3: Development vs. Production")

**Goal**: Separate development and production environments with different policies

**Setup:**

1. Create "Development" and "Production" teams
2. Development: Generous budgets, all models, user keys
3. Production: Strict budgets, approved models only, service account keys
4. Different rate limits per environment

**Result**: Developers can experiment freely without impacting production budget or reliability.

* * *

## Best Practices[​](#best-practices "Direct link to Best Practices")

### 1. Organization Design[​](#1-organization-design "Direct link to 1. Organization Design")

- ✅ Map organizations to cost centers or customers
- ✅ Set realistic budgets with buffer for growth
- ✅ Assign 1-2 org admins per organization
- ❌ Don't create too many organizations (adds management overhead)

### 2. Team Structure[​](#2-team-structure "Direct link to 2. Team Structure")

- ✅ Keep teams aligned with actual working groups
- ✅ Use service account keys for production
- ✅ Give team admins enough permissions to self-serve
- ❌ Don't create single-user teams (use user-only keys instead)

### 3. Key Management[​](#3-key-management "Direct link to 3. Key Management")

- ✅ Use descriptive key names
- ✅ Rotate keys regularly
- ✅ Delete unused keys
- ✅ Use appropriate key type for use case
- ❌ Don't share keys across users/teams

### 4. Budget Management[​](#4-budget-management "Direct link to 4. Budget Management")

- ✅ Set budgets at multiple levels (org → team → user)
- ✅ Monitor spend regularly
- ✅ Alert before budget exhaustion
- ❌ Don't set budgets too tight (may block legitimate usage)

### 5. Delegation[​](#5-delegation "Direct link to 5. Delegation")

- ✅ Assign org admins for large organizations
- ✅ Assign team admins for active teams
- ✅ Configure team member permissions appropriately
- ❌ Don't make everyone a proxy admin

* * *

## Monitoring & Observability[​](#monitoring--observability "Direct link to Monitoring & Observability")

LiteLLM provides comprehensive monitoring:

- **Spend Tracking**: Real-time spend by org/team/user/key
- **Usage Analytics**: Request counts, token usage, model usage
- **Admin UI**: Visual dashboard for all metrics
- **Logging**: Detailed logs with tenant context
- **Alerting**: Budget alerts, rate limit alerts, error alerts

[Learn more about Logging](https://docs.litellm.ai/docs/proxy/logging)

* * *

## Comparison with Other Approaches[​](#comparison-with-other-approaches "Direct link to Comparison with Other Approaches")

ApproachProsConsLiteLLM Advantage**Separate instances per tenant**Strong isolationHigh operational overhead, cost inefficientSingle instance, same isolation, 90% cost reduction**Single shared pool**Simple setupNo cost attribution, no access controlFull attribution, granular access control**API key prefixes**Basic separationManual tracking, no hierarchy, no RBACAutomatic tracking, hierarchical, full RBAC**External auth layer**FlexibleComplex integration, no built-in budgetsNative integration, built-in budgets

* * *

## FAQ[​](#faq "Direct link to FAQ")

**Q: Can users belong to multiple teams?**  
A: Yes, users can be members of multiple teams and have different keys for each team.

**Q: What happens when a user leaves?**  
A: User-specific keys are deleted, but team service account keys remain active.

**Q: Can team budgets exceed organization budget?**  
A: No, the system enforces that team budgets cannot exceed their organization's budget.

**Q: How granular is the cost tracking?**  
A: Every API call is tracked with organization, team, user, and key context.

**Q: Can I have teams without organizations?**  
A: Yes! Teams work independently in **open source** without needing Organizations. Organizations are an **enterprise feature** that adds an additional hierarchy layer on top of teams.

**Q: Is there a limit to hierarchy depth?**  
A: The hierarchy is: Organization → Team → User → Key (4 levels). This covers most use cases.

**Q: How do I migrate from flat structure to hierarchical?**  
A: You can gradually create organizations and teams, then move existing users/keys into them.

* * *

- [User Management Hierarchy](https://docs.litellm.ai/docs/proxy/user_management_heirarchy) - Visual hierarchy overview
- [Access Control (RBAC)](https://docs.litellm.ai/docs/proxy/access_control) - Detailed role permissions
- [Team Budgets](https://docs.litellm.ai/docs/proxy/team_budgets) - Budget management guide
- [Virtual Keys](https://docs.litellm.ai/docs/proxy/virtual_keys) - API key management
- [Admin UI](https://docs.litellm.ai/docs/proxy/ui) - Visual dashboard for management

* * *

## Summary[​](#summary "Direct link to Summary")

LiteLLM solves multi-tenant architecture challenges through:

1. **Hierarchical Structure**: Organizations → Teams → Users → Keys
2. **Granular RBAC**: Platform-wide and tenant-scoped roles
3. **Cost Attribution**: Spend tracking at every level
4. **Delegation**: Org admins and team admins self-manage
5. **Isolation**: Strong tenant boundaries
6. **Scalability**: Handles 10 to 10,000+ users with same architecture

### Open Source vs. Enterprise[​](#open-source-vs-enterprise "Direct link to Open Source vs. Enterprise")

**Open Source** (Teams + Users + Keys):

- ✅ Teams as primary tenant boundary
- ✅ Team admins manage their teams
- ✅ Virtual keys with team/user tracking
- ✅ Budget and rate limits per team
- ✅ Spend tracking and logging

**Enterprise** (Adds Organizations layer):

- ✨ Organizations for top-level tenant isolation
- ✨ Organization admins manage multiple teams
- ✨ Organization-level budgets and model access
- ✨ Hierarchical delegation and reporting

This makes LiteLLM ideal for:

- ✅ Enterprises with multiple departments
- ✅ SaaS providers with multiple customers
- ✅ Organizations needing cost chargeback/showback
- ✅ Teams requiring self-service LLM access
- ✅ Any multi-tenant LLM deployment

[Start with LiteLLM Proxy →](https://docs.litellm.ai/docs/proxy/quick_start)