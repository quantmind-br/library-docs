---
title: Decorating Methods - FastMCP
url: https://gofastmcp.com/v2/patterns/decorating-methods
source: crawler
fetched_at: 2026-01-22T22:22:06.62937573-03:00
rendered_js: false
word_count: 648
summary: This guide explains the correct patterns for using FastMCP decorators with Python instance, class, and static methods to ensure proper parameter binding.
tags:
    - fastmcp
    - python-decorators
    - method-binding
    - tool-registration
    - instance-methods
    - class-methods
category: guide
---

FastMCP’s decorator system is designed to work with functions, but you may see unexpected behavior if you try to decorate an instance or class method. This guide explains the correct approach for using methods with all FastMCP decorators (`@tool`, `@resource`, and `@prompt`).

## Why Are Methods Hard?

When you apply a FastMCP decorator like `@tool`, `@resource`, or `@prompt` to a method, the decorator captures the function at decoration time. For instance methods and class methods, this poses a challenge because:

1. For instance methods: The decorator gets the unbound method before any instance exists
2. For class methods: The decorator gets the function before it’s bound to the class

This means directly decorating these methods doesn’t work as expected. In practice, the LLM would see parameters like `self` or `cls` that it cannot provide values for. Additionally, **FastMCP decorators return objects (Tool, Resource, or Prompt instances) rather than the original function**. This means that when you decorate a method directly, the method becomes the returned object and is no longer callable by your code:

This is another important reason to register methods functionally after defining the class.

## Recommended Patterns

### Instance Methods

When the decorator is applied this way, it captures the unbound method. When the LLM later tries to use this component, it will see `self` as a required parameter, but it won’t know what to provide for it, causing errors or unexpected behavior.

This approach works because:

1. You first create an instance of the class (`obj`)
2. When you access the method through the instance (`obj.add`), Python creates a bound method where `self` is already set to that instance
3. When you register this bound method, the system sees a callable that only expects the appropriate parameters, not `self`

### Class Methods

The behavior of decorating class methods depends on the order of decorators:

- If `@classmethod` comes first, then `@mcp.tool`: No error is raised, but it won’t work correctly
- If `@mcp.tool` comes first, then `@classmethod`: FastMCP will detect this and raise a helpful `ValueError` with guidance

This works because:

1. The `@classmethod` decorator is applied properly during class definition
2. When you access `MyClass.from_string`, Python provides a special method object that automatically binds the class to the `cls` parameter
3. When registered, only the appropriate parameters are exposed to the LLM, hiding the implementation detail of the `cls` parameter

### Static Methods

Static methods “work” with FastMCP decorators, but this is not recommended because the FastMCP decorator will not return a callable method. Therefore, you should register static methods the same way as other methods.

This works because `@staticmethod` converts the method to a regular function, which the FastMCP decorator can then properly process. However, this is not recommended because the FastMCP decorator will not return a callable staticmethod. Therefore, you should register static methods the same way as other methods.

## Additional Patterns

### Creating Components at Class Initialization

You can automatically register instance methods when creating an object:

```
from fastmcp import FastMCP

mcp = FastMCP()

class ComponentProvider:
    def __init__(self, mcp_instance):
        # Register methods
        mcp_instance.tool(self.tool_method)
        mcp_instance.resource("resource://data")(self.resource_method)

    def tool_method(self, x):
        return x * 2

    def resource_method(self):
        return "Resource data"

# The methods are automatically registered when creating the instance
provider = ComponentProvider(mcp)
```

This pattern is useful when:

- You want to encapsulate registration logic within the class itself
- You have multiple related components that should be registered together
- You want to ensure that methods are always properly registered when creating an instance

The class automatically registers its methods during initialization, ensuring they’re properly bound to the instance before registration.

## Summary

The current behavior of FastMCP decorators with methods is:

- **Static methods**: Can be decorated directly and work perfectly with all FastMCP decorators
- **Class methods**: Cannot be decorated directly and will raise a helpful `ValueError` with guidance
- **Instance methods**: Should be registered after creating an instance using the decorator calls

For class and instance methods, you should register them after creating the instance or class to ensure proper method binding. This ensures that the methods are properly bound before being registered. Understanding these patterns allows you to effectively organize your components into classes while maintaining proper method binding, giving you the benefits of object-oriented design without sacrificing the simplicity of FastMCP’s decorator system.