---
title: Expressions
url: https://docs.docker.com/build/bake/expressions/
source: llms
fetched_at: 2026-01-24T14:15:08.921703608-03:00
rendered_js: false
word_count: 201
summary: This document explains how to use expression evaluation in Docker Bake files for performing arithmetic operations and conditional logic using ternary operators and variables.
tags:
    - docker-buildx
    - bake
    - hcl
    - expressions
    - ternary-operators
    - arithmetic-operations
category: guide
---

## Expression evaluation in Bake

Bake files in the HCL format support expression evaluation, which lets you perform arithmetic operations, conditionally set values, and more.

## [Arithmetic operations](#arithmetic-operations)

You can perform arithmetic operations in expressions. The following example shows how to multiply two numbers.

```
sum = 7*6
target "default" {
  args = {
    answer = sum
  }
}
```

Printing the Bake file with the `--print` flag shows the evaluated value for the `answer` build argument.

```
$ docker buildx bake --print
```

```
{
  "target": {
    "default": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "answer": "42"
      }
    }
  }
}
```

## [Ternary operators](#ternary-operators)

You can use ternary operators to conditionally register a value.

The following example adds a tag only when a variable is not empty, using the built-in `notequal` [function](https://docs.docker.com/build/bake/funcs/).

```
variable "TAG" {}
target "default" {
  context="."
  dockerfile="Dockerfile"
  tags = [
    "my-image:latest",
    notequal("",TAG) ? "my-image:${TAG}": ""
  ]
}
```

In this case, `TAG` is an empty string, so the resulting build configuration only contains the hard-coded `my-image:latest` tag.

```
$ docker buildx bake --print
```

```
{
  "target": {
    "default": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "tags": ["my-image:latest"]
    }
  }
}
```

## [Expressions with variables](#expressions-with-variables)

You can use expressions with [variables](https://docs.docker.com/build/bake/variables/) to conditionally set values, or to perform arithmetic operations.

The following example uses expressions to set values based on the value of variables. The `v1` build argument is set to "higher" if the variable `FOO` is greater than 5, otherwise it is set to "lower". The `v2` build argument is set to "yes" if the `IS_FOO` variable is true, otherwise it is set to "no".

```
variable "FOO" {
  default = 3
}
variable "IS_FOO" {
  default = true
}
target "app" {
  args = {
    v1 = FOO > 5 ? "higher" : "lower"
    v2 = IS_FOO ? "yes" : "no"
  }
}
```

Printing the Bake file with the `--print` flag shows the evaluated values for the `v1` and `v2` build arguments.

```
$ docker buildx bake --print app
```

```
{
  "group": {
    "default": {
      "targets": ["app"]
    }
  },
  "target": {
    "app": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "v1": "lower",
        "v2": "yes"
      }
    }
  }
}
```