---
title: Knowledge Graph Memory Extension | goose
url: https://block.github.io/goose/docs/mcp/knowledge-graph-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:23.622111244-03:00
rendered_js: true
word_count: 378
summary: This tutorial explains how to integrate and configure the Knowledge Graph Memory MCP Server extension in goose to enable persistent, relationship-based data analysis and pattern detection across sessions.
tags:
    - goose-ai
    - mcp-server
    - knowledge-graph
    - persistent-memory
    - configuration-guide
    - ai-extensions
category: tutorial
---

🎥Plug & Play

Watch the demo

* * *

This tutorial covers how to add the [Knowledge Graph Memory MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) as a goose extension. This enables goose to analyze relationships, detect patterns, and gain a deeper understanding of your data. The knowledge graph builds on the [memory extension](https://block.github.io/goose/docs/mcp/memory-mcp) by mapping complex relationships between concepts and providing persistent memory across goose sessions.

TLDR

- goose Desktop
- goose CLI

## Configuration[​](#configuration "Direct link to Configuration")

info

Note that you'll need [Node.js](https://nodejs.org/) installed on your system to run this command, as it uses `npx`.

- goose Desktop
- goose CLI

<!--THE END-->

1. [Launch the installer](goose://extension?cmd=npx&arg=-y&arg=%40modelcontextprotocol%2Fserver-memory&id=knowledge_graph_memory&name=Knowledge%20Graph%20Memory&description=Graph-based%20memory%20system%20for%20persistent%20knowledge%20storage)
2. Click `Yes` to confirm the installation
3. Click the button in the top-left to open the sidebar
4. Navigate to the chat

## Example Usage[​](#example-usage "Direct link to Example Usage")

In this example, I'll show you how goose can become an intelligent security reviewer by using connected knowledge patterns to detect and analyze vulnerabilities. goose will be able to understand the relationship between security issues, their impacts, and mitigations.

This means goose doesn't just spot issues - it understands how vulnerabilities connect to real world impacts and can suggest comprehensive solutions.

### Step 1: Teach goose About Security Patterns[​](#step-1-teach-goose-about-security-patterns "Direct link to Step 1: Teach goose About Security Patterns")

#### goose Prompt #1[​](#goose-prompt-1 "Direct link to goose Prompt #1")

```
goose, learn these security vulnerability patterns and their relationships:

1. SQL Injection relates to:

    - Unvalidated database inputs
    - Data theft risks
    - Parameterized query solutions

2. XSS Vulnerabilities connect to:

    - Unescaped user output
    - Session hijacking risks
    - Content sanitization fixes

3.Authentication Weaknesses link to:

    - Session management
    - Account compromise
    - JWT-based solutions
```

#### goose Output[​](#goose-output "Direct link to goose Output")

```
I'll store this security knowledge in the Knowledge Graph Memory with proper entities and relationships

[.... Create Entities .....]

Now, let's create the relationships between these security concepts:

[.... Create Relations .....]

Let me verify what's been stored:

[... Read Graph ...]

I've now stored your security knowledge in the graph with:

1. Vulnerability Entities:

    - SQL Injection (with observations about unvalidated inputs and data theft)
    - XSS Vulnerabilities (with observations about unescaped output and session risks)
    - Authentication Weaknesses (with observations about session management)

2. Solution Entities:

    - Parameterized Queries
    - Content Sanitization
    - JWT Authentication

3. Connected Relationships:

    - Vulnerabilities → their potential impacts
    - Solutions → the vulnerabilities they mitigate

The knowledge is now structured in a way that I can:

    - Trace vulnerability impact chains
    - Identify appropriate solutions for each vulnerability
    - Understand how different security issues are related
```

### Step 2: Use Connected Knowledge for Code Review[​](#step-2--use-connected-knowledge-for-code-review "Direct link to Step 2: Use Connected Knowledge for Code Review")

#### goose Prompt # 2[​](#goose-prompt--2 "Direct link to goose Prompt # 2")

```
Review this API endpoint for security issues:
```

```
app.post('/api/login',(req, res)=>{
const{ username, password }= req.body;
const query =`SELECT * FROM users WHERE username = '${username}'`;
    db.query(query,(err, result)=>{
if(err)throw err;
if(result.length>0){
        res.cookie('user', username);
        res.json({success:true});
}
});
});
```

#### goose Output[​](#goose-output-1 "Direct link to goose Output")

```
I'll analyze this code using our connected knowledge graph to trace security vulnerabilities and their implications:

[.... Search Nodes ... Open Nodes ...]

Based on our knowledge graph analysis, I've found multiple critical security issues:

1. SQL Injection Vulnerability:
    - Issue: Using string concatenation in query WHERE username = '${username}'
    - Impact Chain: SQL Injection → Data Theft
    - Risk Level: Critical
    - Solution (from parameterized_queries): Use parameterized queries instead

2. Authentication Weakness:
    - Issue: Using basic cookie-based session res.cookie('user', username)
    - Impact Chain: Auth Weakness → Account Compromise
    - Risk Level: High
    - Solution (from jwt_auth): Implement JWT with proper expiration

```

```
Here's the secure implementation based on our stored patterns:

app.post('/api/login',async(req, res)=>{
try{
// Input validation
if(!req.body.username||!req.body.password){
return res.status(400).json({
success:false,
error:'Username and password required'
});
}

// Parameterized query (prevents SQL injection)
const query ='SELECT * FROM users WHERE username = ?';
const result =await db.query(query,[req.body.username]);

if(!result.length){
return res.status(401).json({
success:false,
error:'Invalid credentials'
});
}

// Password verification would go here
// const validPassword = await bcrypt.compare(req.body.password, result[0].password);

// JWT-based session management (prevents session hijacking)
const token = jwt.sign(
{userId: result[0].id},
        process.env.JWT_SECRET,
{expiresIn:'1h'}
);

        res.json({
success:true,
token: token
});

}catch(error){
        res.status(500).json({
success:false,
error:'Internal server error'
});
}
});
```

```
 The fixes address the vulnerability chains our knowledge graph identified:

     1. SQL Injection → Data Theft: Mitigated by parameterized queries
     2. Auth Weakness → Account Compromise: Mitigated by JWT implementation

 Additional security improvements based on connected patterns:

     - Added input validation
     - Proper error handling
     - No exposure of internal errors
     - Token-based instead of cookie-based auth
     - Expiration time on authentication

 Would you like me to:

     1. Explain any of these security relationships in more detail?
     2. Show how to implement additional security patterns?
     3. Analyze another endpoint?
```