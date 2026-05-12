---
title: Build static physics playground for gap collision debugging
url: https://ampcode.com/threads/T-019bbcd0-1ffa-72fa-957b-91f0d01bdaa1
source: crawler
fetched_at: 2026-02-06T02:09:47.766110859-03:00
rendered_js: false
word_count: 394
summary: This document provides a technical overview of implementations for circle-point and corner collision detection in open-source physics engines like Box2D and Matter.js. It details mathematical algorithms for calculating normals, impulses, and contact points using methods like Voronoi regions and Separating Axis Theorem.
tags:
    - physics-engine
    - collision-detection
    - game-development
    - box2d
    - collision-response
    - geometry-algorithms
category: reference
---

Perfect! Now I have comprehensive information. Let me compile this into a detailed response with visual guidance.

## Open Source Physics Engine Implementations: Circle-Point Collision Detection and Response

I've analyzed the most widely-used physics engines and compiled the key implementations for handling circle-vertex/corner collisions. Here's a comprehensive guide:

### Key Implementations

#### 1. **Box2D (C/C++) - Most Robust Approach**

[Box2D's manifold.c](https://github.com/erincatto/box2d/blob/main/src/manifold.c) contains the gold standard for circle-polygon collisions, including corner cases. The `b2CollidePolygonAndCircle` function (lines 141-257) demonstrates the critical pattern:

**Circle vs Polygon Vertex Detection:**

```
// Lines 186-207 in manifold.c
if ( u1 < 0.0f && separation > FLT_EPSILON )
{
    // Circle center is closest to v1 (first vertex)
    // This is the CORNER/VERTEX case
    b2Vec2 normal = b2Normalize( b2Sub( center, v1 ) );
    separation = b2Dot( b2Sub( center, v1 ), normal );
    
    // Contact point at midpoint, accounting for both radii
    b2Vec2 cA = b2MulAdd( v1, radiusA, normal );
    b2Vec2 cB = b2MulSub( center, radiusB, normal );
    b2Vec2 contactPointA = b2Lerp( cA, cB, 0.5f );
    
    manifold.normal = b2RotateVector( xfA.q, normal );
    // ... set separation and manifold data
}
```

**Why this works for your gap-in-circle scenario:**

- **Closest point detection** uses barycentric coordinates (lines 183-184) to determine if the circle center is outside the polygon edge
- **Vertex normal is computed directly** from the vector between the vertex and circle center
- **The normal always points from the collision object outward**, ensuring proper reflection

* * *

#### 2. **Matter.js (JavaScript) - Practical Reference**

[Matter.js's Collision.js](https://github.com/liabru/matter-js/blob/master/src/collision/Collision.js) uses the Separating Axis Theorem (SAT) which automatically handles corner collisions:

**Key pattern (lines 113-127):**

```
// Ensure normal faces away from bodyA
if (normalX * deltaX + normalY * deltaY >= 0) {
    normalX = -normalX;
    normalY = -normalY;
}

normal.x = normalX;
normal.y = normalY;

// Tangent is perpendicular to normal
tangent.x = -normalY;
tangent.y = normalX;

// Penetration vector for separating bodies
penetration.x = normalX * depth;
penetration.y = normalY * depth;
```

**For velocity reflection (lines 317-318 in Resolver.js):**

```
// Raw impulse from collision
var normalImpulse = (1 + pair.restitution) * normalVelocity * share;
tangentImpulse *= share;
```

* * *

#### 3. **Simplified Algorithm for Your Use Case**

Based on [Jeff Thompson's Collision Detection](https://github.com/jeffThompson/CollisionDetection) examples, here's the clean circle-point collision pattern:

**Detection (LineCircle example - applicable to gap endpoints):**

```
// Find closest point on line segment
function lineCircle(x1, y1, x2, y2, cx, cy, r) {
    // Check if endpoints are inside circle
    if (pointCircle(x1, y1, cx, cy, r)) return true;
    if (pointCircle(x2, y2, cx, cy, r)) return true;
    
    // Find closest point on line segment
    let len = dist(x1, y1, x2, y2);
    let dot = ((cx-x1)*(x2-x1) + (cy-y1)*(y2-y1)) / (len*len);
    let closestX = x1 + dot * (x2-x1);
    let closestY = y1 + dot * (y2-y1);
    
    // Clamp to segment (critical for endpoint detection)
    if (!pointOnSegment(x1, y1, x2, y2, closestX, closestY)) {
        return false;
    }
    
    return dist(closestX, closestY, cx, cy) <= r;
}
```

* * *

### The Correct Collision Normal and Reflection Calculation

#### **For Circle vs Gap Endpoint (Corner):**

```
Given:
  - Ball center: P_ball
  - Gap endpoint (corner): V_corner
  - Ball radius: r

1. NORMAL CALCULATION (collision normal):
   normal = normalize(P_ball - V_corner)
   
2. SEPARATION (penetration depth):
   distance = length(P_ball - V_corner)
   separation = distance - r
   
3. CONTACT POINT:
   contact_point = V_corner + r * normal
   // or midpoint between surfaces:
   contact_point = (V_corner + (P_ball - r * normal)) / 2
   
4. VELOCITY REFLECTION (impulse-based):
   relative_velocity = v_ball
   
   // Component along normal
   v_normal = dot(relative_velocity, normal)
   
   // If moving toward corner, apply impulse
   if v_normal < 0:
       // Impulse magnitude (with restitution e)
       impulse = -(1 + e) * v_normal
       
       // Apply impulse
       v_ball_new = v_ball + (impulse / mass) * normal
   
   // Alternative: Direct reflection (elastic, e=1.0)
   v_reflected = v - 2 * dot(v, normal) * normal
```

* * *

### Critical Implementation Details from Box2D

**Why Box2D's approach is superior for your scenario:**

1. **Voronoi regions** (lines 186-231): The algorithm determines whether the closest feature is:
   
   - The edge (smooth curve case) → use edge normal
   - A vertex (corner case) → use vertex-to-center normal
2. **Barycentric coordinate test:**
   
   ```
   float u1 = dot(center - v1, v2 - v1);
   float u2 = dot(center - v2, v1 - v2);
   
   if (u1 < 0.0f) → closest to v1 (first vertex/corner)
   if (u2 < 0.0f) → closest to v2 (second vertex/corner)
   else → closest to edge segment
   ```
3. **Separation threshold** (line 186): The check `separation > FLT_EPSILON` prevents false positives from floating-point errors.

* * *

### Manifold/Contact Structure (What to Store)

Based on Box2D's `b2Manifold` structure (collision.h):

```
struct b2Manifold {
    b2Vec2 normal;              // Unit normal from A to B
    b2ManifoldPoint points[2];  // Up to 2 contact points
    int pointCount;             
};

struct b2ManifoldPoint {
    b2Vec2 point;               // Contact point in world space
    float separation;           // Negative if overlapping
    float normalImpulse;        // Cached for warm start
    uint16_t id;                // Feature ID for persistence
};
```

**For your circle vs gap endpoint case:**

- `normal` = direction from corner to ball center (normalized)
- `points[0].point` = the contact location
- `points[0].separation` = distance - radius (negative if penetrating)
- `pointCount` = 1 (only one contact point for corner collision)

* * *

### References

- **Box2D**: [`manifold.c` lines 141-257](https://github.com/erincatto/box2d/blob/main/src/manifold.c#L141-L257) - CirclePolygon collision with corner handling
- **Box2D Documentation**: [`docs/collision.md`](https://github.com/erincatto/box2d/blob/main/docs/collision.md) - Ghost collisions and chain segments
- **Matter.js**: [`Collision.js`](https://github.com/liabru/matter-js/blob/master/src/collision/Collision.js) - SAT-based collision detection
- **Matter.js**: [`Resolver.js`](https://github.com/liabru/matter-js/blob/master/src/collision/Resolver.js) - Impulse-based response
- **Jeff Thompson's Guide**: [`LineCircle.pde`](https://github.com/jeffThompson/CollisionDetection/blob/master/CodeExamples/LineCircle/LineCircle.pde) - Practical closest-point algorithm

The key takeaway: **Use Voronoi region detection** (determining which feature of the polygon is closest) to switch between edge collision (smooth curves) and vertex collision (corners). The normal vector should always point from the static geometry toward the dynamic body for consistent physics.