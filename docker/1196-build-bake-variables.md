---
title: Variables
url: https://docs.docker.com/build/bake/variables/
source: llms
fetched_at: 2026-01-24T14:15:24.615603419-03:00
rendered_js: false
word_count: 492
summary: This document explains how to define, interpolate, and validate variables in Docker Bake files to create dynamic build configurations.
tags:
    - docker-bake
    - hcl
    - variable-interpolation
    - validation-rules
    - build-configuration
    - environment-variables
category: guide
---

## Variables in Bake

You can define and use variables in a Bake file to set attribute values, interpolate them into other values, and perform arithmetic operations. Variables can be defined with default values, and can be overridden with environment variables.

Use the `variable` block to define a variable.

The following example shows how to use the `TAG` variable in a target.

Bake supports string interpolation of variables into values. You can use the `${}` syntax to interpolate a variable into a value. The following example defines a `TAG` variable with a value of `latest`.

To interpolate the `TAG` variable into the value of an attribute, use the `${TAG}` syntax.

Printing the Bake file with the `--print` flag shows the interpolated value in the resolved build configuration.

To verify that the value of a variable conforms to an expected type, value range, or other condition, you can define custom validation rules using the `validation` block.

In the following example, validation is used to enforce a numeric constraint on a variable value; the `PORT` variable must be 1024 or greater.

If the `condition` expression evaluates to `false`, the variable value is considered invalid, whereby the build invocation fails and `error_message` is emitted. For example, if `PORT=443`, the condition evaluates to `false`, and the error is raised.

Values are coerced into the expected type before the validation is set. This ensures that any overrides set with environment variables work as expected.

### [Validate multiple conditions](#validate-multiple-conditions)

To evaluate more than one condition, define multiple `validation` blocks for the variable. All conditions must be `true`.

Here’s an example:

This example enforces:

- The variable must not be empty.
- The variable must match a specific character set.

For invalid inputs like `VAR="hello@world"`, the validation would fail.

### [Validating variable dependencies](#validating-variable-dependencies)

You can reference other Bake variables in your condition expression, enabling validations that enforce dependencies between variables. This ensures that dependent variables are set correctly before proceeding.

Here’s an example:

This configuration ensures that the `BAR` variable can only be used if `FOO` has been assigned a non-empty value. Attempting to build without setting `FOO` will trigger the validation error.

If you want to bypass variable interpolation when parsing the Bake definition, use double dollar signs (`$${VARIABLE}`).

When multiple files are specified, one file can use variables defined in another file. In the following example, the `vars.hcl` file defines a `BASE_IMAGE` variable with a default value of `docker.io/library/alpine`.

The following `docker-bake.hcl` file defines a `BASE_LATEST` variable that references the `BASE_IMAGE` variable.

When you print the resolved build configuration, using the `-f` flag to specify the `vars.hcl` and `docker-bake.hcl` files, you see that the `BASE_LATEST` variable is resolved to `docker.io/library/alpine:latest`.

Here are some additional resources that show how you can use variables in Bake:

- You can override `variable` values using environment variables. See [Overriding configurations](https://docs.docker.com/build/bake/overrides/#environment-variables) for more information.
- You can refer to and use global variables in functions. See [HCL functions](https://docs.docker.com/build/bake/funcs/#variables-in-functions)
- You can use variable values when evaluating expressions. See [Expression evaluation](https://docs.docker.com/build/bake/expressions/#expressions-with-variables)