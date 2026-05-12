---
title: Create a Priority Matrix for Database Optimization | Guides | Warp
url: https://docs.warp.dev/guides/devops-and-infrastructure/how-to-create-a-priority-matrix-for-database-optimization
source: sitemap
fetched_at: 2026-04-29T15:07:07.290017023-03:00
rendered_js: false
word_count: 459
summary: A comprehensive framework for auditing, profiling, and optimizing database queries to improve application performance through systematic analysis and best practices.
tags:
    - database-optimization
    - sql-performance
    - query-tuning
    - database-profiling
    - index-optimization
    - n-plus-one-problem
category: guide
optimized: true
optimized_at: 2026-04-29T15:07:07.290017023-03:00
---
A systematic, repeatable approach for analyzing, profiling, and optimizing database performance.

## Phase 1: Query Discovery & Cataloging

### Step 1 — Identify All Queries

Scan the entire codebase for every SQL or ORM-based query:

- Raw SQL queries (including stored procedures)
- ORM-generated queries
- Dynamic query builders
- Background job queries at scale
- Admin or reporting queries that lock tables

### Step 2 — Document Key Details

For each query, record:

- File location and function name
- Frequency of execution (per request, batch job, cron)
- Typical data volume processed

## Phase 2: Performance Analysis

Generate and analyze execution plans for each query.

### Execution Plan Commands

```sql
-- PostgreSQL
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON);
-- MySQL
EXPLAIN FORMAT=JSON;
```

### Extract These Metrics

- Total execution time
- Rows examined vs. rows returned ratio
- Index usage (full table scans, index scans, seeks)
- Join methods (nested loop, hash, merge)
- Memory usage and temporary file creation
- Buffer pool hit ratio

## Phase 3: Identify Specific Problems

### 1. N+1 Query Detection

| Aspect | Value |
|--------|-------|
| **Problem** | Loading users and posts separately |
| **Found in** | `/api/users/controller.js:45` |
| **Impact** | 100 queries for 100 users instead of one batched query |

**Current Implementation:**
```js
const users = await db.query('SELECT * FROM users');
for (const user of users) {
  user.posts = await db.query('SELECT * FROM posts WHERE user_id = ?', [user.id]);
}
```

**Optimized Version:**
```js
const usersWithPosts = await db.query(`
  SELECT u.*,
         COALESCE(json_agg(p.*) FILTER (WHERE p.id IS NOT NULL), '[]') AS posts
  FROM users u
  LEFT JOIN posts p ON p.user_id = u.id
  GROUP BY u.id;
`);
```

### 2. Missing Index Analysis

| Aspect | Value |
|--------|-------|
| **Finding** | Full table scan on `orders` table (2M rows) |
| **Query** | `SELECT * FROM orders WHERE status = 'pending' AND created_at > ?;` |

**Recommendation:**
```sql
CREATE INDEX idx_orders_status_created ON orders(status, created_at);
```

**Impact:** Query time reduced from **3.2s → 0.045s**

### 3. Inefficient JOIN Patterns

Problem: Queries join through unnecessary intermediate tables.

Solution: Simplify relationships using direct joins or indexed subqueries.

### 4. Subquery Optimization

**Inefficient Query:**
```sql
SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products WHERE category_id = p.category_id);
```

**Optimized (Window Function):**
```sql
WITH product_stats AS (
  SELECT *,
         AVG(price) OVER (PARTITION BY category_id) AS avg_category_price
  FROM products
)
SELECT * FROM product_stats WHERE price > avg_category_price;
```

## Phase 4: Advanced Optimizations

### Caching Strategies

Use caching for:

- User-specific data with low update frequency
- Expensive aggregations that can be pre-computed

**Implementation:**
```js
const getCachedOrQuery = async (key, query, ttl = 3600) => {
  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);
  const result = await db.query(query);
  await redis.setex(key, ttl, JSON.stringify(result));
  return result;
};
```

### Recommended Connection Configuration

```json
{
  "connectionLimit": 50,
  "queueLimit": 100,
  "acquireTimeout": 30000,
  "waitForConnections": true,
  "idleTimeout": 300000,
  "enableKeepAlive": true,
  "keepAliveInitialDelay": 10
}
```

### Batch Operation Optimization

| Aspect | Value |
|--------|-------|
| **Problem** | Records inserted one by one |
| **Found in** | `/jobs/import-data.js` |
| **Current** | 1000 individual `INSERT` statements |

**Optimized:**
```sql
INSERT INTO users (name, email, created_at) VALUES
  ($1, $2, $3),
  ($4, $5, $6),
  ... -- batch in groups of 1000
```

### Pagination Optimization

```sql
SELECT * FROM posts
WHERE created_at < $cursor
ORDER BY created_at DESC
LIMIT 20;
```

## Phase 5: Monitoring & Maintenance

### 1. Slow Query Logging Setup

**PostgreSQL:**
```sql
ALTER SYSTEM SET log_min_duration_statement = '1000';
ALTER SYSTEM SET log_statement = 'all';
ALTER SYSTEM SET log_duration = on;
```

**MySQL:**
```sql
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1;
SET GLOBAL log_output = 'TABLE';
```

### 2. Query Performance Testing

```js
describe('Query Performance', () => {
  test('User listing should complete under 100ms', async () => {
    const start = Date.now();
    await db.query('SELECT * FROM users LIMIT 1000');
    expect(Date.now() - start).toBeLessThan(100);
  });
});
```

## Phase 6: Deliverables

- **Optimization Script:** Single SQL file with all index creations, ordered by performance impact
- **Code Changes PR:** All query optimizations with before/after comparison results
- **Performance Report:** Baseline vs. optimized metrics, expected resource savings, risk assessment
- **Monitoring Dashboard:** Recurring queries to track performance over time

## Priority Matrix

Rank optimizations by:

- **Impact:** Query frequency × time saved
- **Risk:** Low / Medium / High
- **Effort:** Quick fix / Moderate / Complex refactor

> Focus on **high-impact**, **low-risk**, **low-effort** items first.

#database-optimization #query-tuning #performance
