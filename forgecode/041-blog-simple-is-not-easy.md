---
title: 'Simple Over Easy: Architectural Constraints for Maintainable AI-Generated Code'
url: https://forgecode.dev/blog/simple-is-not-easy/
source: sitemap
fetched_at: 2026-03-29T14:48:36.00291288-03:00
rendered_js: false
word_count: 1469
summary: This document explains how to apply Rich Hickey's 'Simple Made Easy' principles to constrain AI code generation, creating architectural patterns that force maintainable code by design.
tags:
    - ai-code-generation
    - simple-made-easy
    - architectural-constraints
    - code-maintenance
    - rich-hickey
    - software-design
    - principles
category: guide
---

> **TL;DR**: AI agents can generate code that passes tests and looks familiar, but the last 10% of understanding, review, and maintenance becomes impossible. By applying Rich Hickey's principles from his talk "Simple Made Easy", Our team constrained our architecture to leave only one way to solve each problem, making AI-generated code easy to review and maintain.

Two months ago, YouTube's recommendation algorithm served me Rich Hickey's 2011 QCon talk ["Simple Made Easy"](https://www.youtube.com/watch?v=SxdOUGdseq4).

tip

If you haven't seen it, I highly recommend watching it. It's a 13-year-old talk that feels more relevant today than ever. ["Simple Made Easy"](https://www.youtube.com/watch?v=SxdOUGdseq4)

We've all experienced this with AI coding agents, what I now call **the AI 90/10 problem**: Agents can generate syntactically correct, test passing code that gets us 90% of the way there incredibly fast, but that last 10%, the part where humans have to understand, review, and maintain the code, becomes impossible.

As Hickey mentioned: "We can only hope to make reliable those things we understand." And there's usually a tradeoff: when evolving a system to make it more extensible and dynamic, it may become harder to understand and decide if it's correct.

**AI agents are optimization machines that tend to choose the path of least resistance during generation, not the path of least resistance during review.**

When AI Agents generate code, it's optimizing for:

- ✅ Syntactic correctness
- ✅ Test passage
- ✅ Familiar patterns
- ✅ Minimal prompting required

But you have to live with code that's optimized for:

- ❌ Human comprehension
- ❌ Change velocity
- ❌ Debugability
- ❌ Long term maintenance

This creates a real problem: the faster the AI agents generate code, the slower the team becomes at reviewing it.

**The root cause**: We don't constrain our AI with architecture. We give it infinite ways to solve every problem, then wonder why it chose the most complex path.

Hickey's core distinction changed how I think about Agent generated code:

**Simple**: "One fold, one braid, one twist." Things that are not interleaved or braided together. Simple is objective, you can count the braids. As Hickey explains, the roots of "simple" are "sim" and "plex", meaning "one twist" - the opposite of complex, which means "multiple twists" or "braided together."

**Easy**: "Near at hand, nearby." Things that are familiar, already in your toolkit, close to your current skill set. Easy is relative, what's easy for you might be hard for me. The Latin origin of "easy" relates to "adjacent", meaning "to lie near" and "to be nearby."

AI tends to choose easy over simple because it optimizes for generation speed, not maintenance clarity.

My Agent was generating familiar patterns (easy) that created intertwined, braided complexity (not simple). The solution isn't to make the Agent smarter, it is to make our architecture more constraining.

**Maintainable code has one defining characteristic: it's very easy to review.**

When there's only one way to solve a problem, review becomes pattern matching instead of archaeology.

From the talk, I have extracted five core principles that became architectural constraints for my software:

### Principle 1: Avoid Complecting[​](#principle-1-avoid-complecting "Direct link to Principle 1: Avoid Complecting")

> **"Complect means to interleave, to entwine, to braid. Complex means braided together, folded together. Simple means one fold, one braid, one twist."**

Complecting is when you take simple components and interweave them into complex knots. Every time you complect two concepts, you lose the ability to reason about them independently. As Hickey notes: "Complect results in bad software."

### Principle 2: Separate State from Value[​](#principle-2-separate-state-from-value "Direct link to Principle 2: Separate State from Value")

> **"State complects value and time."**

When you mix what something is (value) with when it changed (time), you create artifacts that are impossible to reason about in isolation.

### Principle 3: Data as Data, Not Objects[​](#principle-3-data-as-data-not-objects "Direct link to Principle 3: Data as Data, Not Objects")

> **"Information is simple. The only thing you can possibly do with information is ruin it."**

Objects complect state, identity, and value. They hide information behind methods and encapsulation, making it impossible to operate on data generically.

### Principle 4: Functions Over Methods[​](#principle-4-functions-over-methods "Direct link to Principle 4: Functions Over Methods")

> **"Methods complect function and state, namespaces."**

Methods hide their dependencies in the object they're attached to. Pure functions make all dependencies explicit. As Hickey explains, methods intertwine function logic with object state and namespace concerns.

### Principle 5: Composition Over Inheritance[​](#principle-5-composition-over-inheritance "Direct link to Principle 5: Composition Over Inheritance")

> **"Inheritance complects types. It says these two types are complected, that's what it means."**

When you inherit, you're saying these types are braided together. Composition lets you combine capabilities without complecting them.

The solution isn't to make AI smarter, it's to make the architecture more constraining. Instead of giving AI Agent a thousand ways to implement a feature, Our team designed systems that left exactly one obvious way.

This approach transforms the AI generation problem: when there's only one valid pattern to follow, AI naturally generates maintainable code because it has no other choice.

Here's how our team transformed each principle into architectural constraints:

### Constraint 1: Immutable Data, Zero Exceptions[​](#constraint-1-immutable-data-zero-exceptions "Direct link to Constraint 1: Immutable Data, Zero Exceptions")

Separate state from value. All domain entities are immutable. When there's only one way to change state (return a new value), AI can't generate hidden mutations that complicate review.

### Constraint 2: Data Separated from Behavior[​](#constraint-2-data-separated-from-behavior "Direct link to Constraint 2: Data Separated from Behavior")

Data as data, not objects. Data structures contain only data. Behavior lives in stateless services.

### Constraint 3: Explicit Error Context, No Exceptions[​](#constraint-3-explicit-error-context-no-exceptions "Direct link to Constraint 3: Explicit Error Context, No Exceptions")

Avoid complecting. Every error must tell the complete story of what went wrong and where. When errors are explicit and contextual, agents can't swallow failures or create generic error handling that hides problems.

### Constraint 4: Pure Functions Over Methods[​](#constraint-4-pure-functions-over-methods "Direct link to Constraint 4: Pure Functions Over Methods")

Functions over methods. Business logic must be pure functions with explicit dependencies. When all dependencies are explicit, AI can't hide complexity in object state or method chains.

### Constraint 5: Composition Over Inheritance[​](#constraint-5-composition-over-inheritance "Direct link to Constraint 5: Composition Over Inheritance")

Composition over inheritance. Capabilities compose through focused traits, never inherit. When types compose instead of inherit, AI can't create hierarchies that complect unrelated concerns.

Hickey's advice was clear: "Stick a queue in there. Queues are the way to just get rid of this problem." He emphasizes that queues help decouple components by separating the "when" from the "where" - avoiding the complexity that comes from direct connections between objects.

Coordination between services happens only through event queues. When services can't call each other directly, AI can't create temporal coupling that makes systems impossible to reason about.

What's interesting is that our architectural constraints don't just make code review faster, they actively teach our Agent to generate better code. Every time agent sees our patterns, it learns and add them in memory. In [ForgeCode](https://github.com/antinomyhq/forge) we call it [custom rules](https://forgecode.dev/docs/custom-rules/). Other agents call them memory, rules etc.

- **Separation of concerns** prevents feature entanglement
- **Explicit dependencies** make testing trivial
- **Immutable data** eliminates entire classes of bugs
- **Pure functions** compose predictably
- **Data as data** enables generic operations

The AI has internalized our constraints with custom rules/memory.

If you're experiencing the AI 90/10 problem, here's what we learned:

### 1. **Constrain Generation, Don't Guide Review**[​](#1-constrain-generation-dont-guide-review "Direct link to 1-constrain-generation-dont-guide-review")

Don't try to teach your AI to generate better code. Design architecture that makes bad code impossible to express.

### 2. **One Way to Win**[​](#2-one-way-to-win "Direct link to 2-one-way-to-win")

For every problem your AI might encounter, there should be exactly one obvious way to solve it. Multiple valid approaches create review complexity.

### 3. **Good Code = Reviewable Code**[​](#3-good-code--reviewable-code "Direct link to 3-good-code--reviewable-code")

The only metric that matters for AI-generated code is: "How quickly can a human verify this is correct?"

### 4. **Teach Through Structure**[​](#4-teach-through-structure "Direct link to 4-teach-through-structure")

Your AI learns from your code structure more than your system prompt. Make sure your architecture embodies the constraints you want replicated.

The architectural constraints we implemented had an upfront cost, but the returns have been extraordinary:

- **Review velocity increased**: What used to take hours of now takes minutes of pattern matching
- **Onboarding accelerated**: New team members could contribute immediately because there was only one way to solve each problem
- **AI learning improved**: Our agents began generating better code because our architecture taught them good patterns

The AI 90/10 problem isn't a limitation of current AI Agents, it's a failure of architectural design.

When your architecture constrains AI behavior through design, AI becomes your partner in building maintainable software rather than your adversary in creating technical debt.

**In the AI era, the teams that win won't be those with the most sophisticated AI agents, they'll be those with the most constraining architectures.**

Good code has one defining characteristic: it's very easy to review. When you design constraints that leave only one way to solve each problem, review becomes pattern matching instead of archaeology.

For teams ready to solve their own AI 90/10 problem, here's how we implemented each principle in our [ForgeCode](https://github.com/antinomyhq/forge) architecture:

### Domain Layer: Pure Information (Principles 1, 2, 3)[​](#domain-layer-pure-information-principles-1-2-3 "Direct link to Domain Layer: Pure Information (Principles 1, 2, 3)")

### Service Layer: Focused Abstractions (Principles 4, 5)[​](#service-layer-focused-abstractions-principles-4-5 "Direct link to Service Layer: Focused Abstractions (Principles 4, 5)")

### Infrastructure Layer: Simple Capabilities (Principle 5)[​](#infrastructure-layer-simple-capabilities-principle-5 "Direct link to Infrastructure Layer: Simple Capabilities (Principle 5)")

### Error Handling: Explicit Context (Principle 1)[​](#error-handling-explicit-context-principle-1 "Direct link to Error Handling: Explicit Context (Principle 1)")

### Testing: Properties Over Implementation (All Principles)[​](#testing-properties-over-implementation-all-principles "Direct link to Testing: Properties Over Implementation (All Principles)")

When [ForgeCode](https://github.com/antinomyhq/forge) generates new code, it naturally follows these structures because there's no other way to express solutions in our architecture. AI generated code that's easier to review than human written code, because our constraints make complexity impossible to express.