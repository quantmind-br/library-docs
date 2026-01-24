---
title: Functions
url: https://docs.docker.com/build/bake/funcs/
source: llms
fetched_at: 2026-01-24T14:15:10.607835166-03:00
rendered_js: false
word_count: 134
summary: This document explains how to utilize built-in standard library functions and create user-defined functions within Docker Bake configuration files to perform complex value manipulations.
tags:
    - docker-bake
    - hcl
    - buildx
    - standard-library
    - user-defined-functions
    - configuration
category: guide
---

HCL functions are great for when you need to manipulate values in your build configuration in more complex ways than just concatenation or interpolation.

## [Standard library](#standard-library)

Bake ships with built-in support for the [standard library functions](https://docs.docker.com/build/bake/stdlib/).

The following example shows the `add` function:

```
variable "TAG" {
  default = "latest"
}
group "default" {
  targets = ["webapp"]
}
target "webapp" {
  args = {
    buildno = "${add(123, 1)}"
  }
}
```

```
$ docker buildx bake --print webapp
```

```
{
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "buildno": "124"
      }
    }
  }
}
```

## [User-defined functions](#user-defined-functions)

You can create [user-defined functions](https://github.com/hashicorp/hcl/tree/main/ext/userfunc) that do just what you want, if the built-in standard library functions don't meet your needs.

The following example defines an `increment` function.

```
function "increment" {
  params = [number]
  result = number + 1
}
group "default" {
  targets = ["webapp"]
}
target "webapp" {
  args = {
    buildno = "${increment(123)}"
  }
}
```

```
$ docker buildx bake --print webapp
```

```
{
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "args": {
        "buildno": "124"
      }
    }
  }
}
```

## [Variables in functions](#variables-in-functions)

You can make references to [variables](https://docs.docker.com/build/bake/variables/) and standard library functions inside your functions.

You can't reference user-defined functions from other functions.

The following example uses a global variable (`REPO`) in a custom function.

```
# docker-bake.hcl
variable "REPO" {
  default = "user/repo"
}
function "tag" {
  params = [tag]
  result = ["${REPO}:${tag}"]
}
target "webapp" {
  tags = tag("v1")
}
```

Printing the Bake file with the `--print` flag shows that the `tag` function uses the value of `REPO` to set the prefix of the tag.

```
$ docker buildx bake --print webapp
```

```
{
  "group": {
    "default": {
      "targets": ["webapp"]
    }
  },
  "target": {
    "webapp": {
      "context": ".",
      "dockerfile": "Dockerfile",
      "tags": ["user/repo:v1"]
    }
  }
}
```