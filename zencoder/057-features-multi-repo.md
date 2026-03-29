---
title: Multi-Repository Search - Zencoder Docs
url: https://docs.zencoder.ai/features/multi-repo
source: crawler
fetched_at: 2026-01-23T09:28:14.32549948-03:00
rendered_js: false
word_count: 568
summary: This document provides instructions for setting up and utilizing Multi-Repository Search to allow Zencoder AI agents to index and search across multiple codebase repositories. It details the administrative setup process, VCS connection configuration, repository indexing, and best practices for cross-repo queries.
tags:
    - multi-repo-search
    - vcs-integration
    - repository-indexing
    - ai-agents
    - codebase-search
    - access-control
category: guide
---

If you work with multiple repositories, Multi-Repository Search allows you to add and index repositories through the web admin panel, enabling Zencoder agents to search across those indexed repositories when needed.

## Getting Started

Setting up multi-repository search involves a few steps that will give your AI agents access to your organization’s codebase.

### Prerequisites

Before setting up multi-repository search, ensure you have:

- **Active subscription** on Core, Advanced, or Max plan
- **Owner or Manager role** in your organization

### Setup Process

#### 1. Access Web Admin Panel

Navigate to [auth.zencoder.ai](https://auth.zencoder.ai) and log in to your account. Users with Owner or Manager roles will see additional options for Connections and Repositories management. ![Web admin panel showing connections and repositories options](https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/multi-repo-admin-panel.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=1af6bde7cbed25a72a611b9026f378e2)

#### 2. Add a connection to your VCS provider

Create a connection to your version control system:

1. Click on `Connections` in the admin panel
2. Select `Add`
3. Choose your VCS provider: GitHub, Bitbucket, or GitLab
4. Add your access token. Note that for multi-repo search, the token scope requires at least repo read permissions.

![Adding a new VCS connection in the admin panel](https://mintcdn.com/forgoodaiinc/pRqEaM47Xe_-nh77/images/multi-repo-add-connection.png?fit=max&auto=format&n=pRqEaM47Xe_-nh77&q=85&s=a2972e36e1e315594fd353b1bfaa4f83)

#### 3. Add Repositories

Once your connection is established, add repositories to your multi-repo index:

1. Navigate to `Repositories` in the admin panel
2. Click `Add`
3. Select a connection and then a repo name from your connected VCS provider
4. **Important**: Enable the “Indexing” flag for each repository (`Automatically reindex repository` checkbox) to allow AI agents to search its contents

![Adding repositories with indexing enabled](https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/multi-repo-add-repository.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=6eb4a4e2e38ec2c3a63ba603258f3d19)

#### 4. Configure Access Permissions

Control which users can access each repository through the multi-repo search tool:

- **Default setting** allows all users within your organization to access the repository
- **Custom access** lets you restrict access to specific users by their email addresses as needed

![Configuring repository access permissions](https://mintcdn.com/forgoodaiinc/K9DwmHqJDSAPSbZr/images/multi-repo-permissions.png?fit=max&auto=format&n=K9DwmHqJDSAPSbZr&q=85&s=eddfdd76c23f889df98bae06e5c9daf5)

## Using Multi-Repository Search

### Automatic Agent Detection

Since Multi-Repository Search is implemented as an agent tool, by default it is available for the [coding agent](https://docs.zencoder.ai/features/coding-agent), but needs to be configured manually for [custom agents](https://docs.zencoder.ai/features/ai-agents) (this functionality is coming soon). Once configured, multi-repository search tool works with your existing workflow:

- **No special commands** are needed as AI agents automatically detect when you reference other repositories
- **Zencoder context understanding** allows agents to use repository names, service names, or project references to trigger searches

### Example Interactions

```
User: "How is authentication handled in the user-service repository? 

Use the multi-repo search tool to find relevant code."

Agent: [Automatically searches user-service repository for 
authentication patterns]
Based on the user-service repository, authentication is 
handled using JWT tokens with...
```

```
User: "Use the multi-repo search tool to find and then implement 
the same error handling pattern used in the payment-api".

Agent: [Searches payment-api repository for error handling patterns]
I found the error handling pattern in payment-api. 
Here's how to implement it in your current project...
```

## Best Practices

To get the most out of Multi-Repository Search, follow these guidelines for optimal results:

### Be Specific with Repository References and Tool Usage

For optimal search behavior, avoid making vague requests as agents might use the search tool excessively. Instead, be specific when referencing repositories or services. Use exact repository names like “user-service” rather than generic terms like “the user thing” or “that authentication repo.” Also, since the Multi-repo search is a tool, you can be explicit in asking the agent to use it. This helps agents target their searches more effectively and return more relevant results.

### Consider Repository Size and Scope

Very large repositories may take longer to index initially, so consider the scope of your searches to get the most relevant results. When working with extensive codebases, provide additional context about which parts of the repository are most relevant to your current task.

### Provide Clear Context

The more context you provide about what you’re looking for across repositories, the better the search results will be. Instead of asking “How does authentication work?”, try “How is JWT token validation implemented in the auth-service repository? Use repo search tool.” This specificity helps agents understand exactly what information to retrieve.

Multi-Repository Search works with other Zencoder capabilities: