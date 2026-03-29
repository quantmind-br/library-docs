---
title: Bake file reference
url: https://docs.docker.com/build/bake/reference/
source: llms
fetched_at: 2026-01-24T14:15:20.574742026-03:00
rendered_js: false
word_count: 3180
summary: This document provides a comprehensive reference for Docker Bake files, explaining their supported formats, lookup order, and merging behavior. It details the various properties and attributes available for defining complex build workflows using docker buildx bake.
tags:
    - docker-buildx
    - bake-file
    - hcl-configuration
    - build-workflow
    - target-attributes
    - docker-build
category: reference
---

The Bake file is a file for defining workflows that you run using `docker buildx bake`.

You can define your Bake file in the following file formats:

- HashiCorp Configuration Language (HCL)
- JSON
- YAML (Compose file)

By default, Bake uses the following lookup order to find the configuration file:

1. `compose.yaml`
2. `compose.yml`
3. `docker-compose.yml`
4. `docker-compose.yaml`
5. `docker-bake.json`
6. `docker-bake.hcl`
7. `docker-bake.override.json`
8. `docker-bake.override.hcl`

You can specify the file location explicitly using the `--file` flag:

If you don't specify a file explicitly, Bake searches for the file in the current working directory. If more than one Bake file is found, all files are merged into a single definition. Files are merged according to the lookup order. That means that if your project contains both a `compose.yaml` file and a `docker-bake.hcl` file, Bake loads the `compose.yaml` file first, and then the `docker-bake.hcl` file.

If merged files contain duplicate attribute definitions, those definitions are either merged or overridden by the last occurrence, depending on the attribute. The following attributes are overridden by the last occurrence:

- `target.cache-to`
- `target.dockerfile-inline`
- `target.dockerfile`
- `target.outputs`
- `target.platforms`
- `target.pull`
- `target.tags`
- `target.target`

For example, if `compose.yaml` and `docker-bake.hcl` both define the `tags` attribute, the `docker-bake.hcl` is used.

All other attributes are merged. For example, if `compose.yaml` and `docker-bake.hcl` both define unique entries for the `labels` attribute, all entries are included. Duplicate entries for the same label are overridden.

The Bake file supports the following property types:

- `target`: build targets
- `group`: collections of build targets
- `variable`: build arguments and variables
- `function`: custom Bake functions

You define properties as hierarchical blocks in the Bake file. You can assign one or more attributes to a property.

The following snippet shows a JSON representation of a simple Bake file. This Bake file defines three properties: a variable, a group, and a target.

In the JSON representation of a Bake file, properties are objects, and attributes are values assigned to those objects.

The following example shows the same Bake file in the HCL format:

HCL is the preferred format for Bake files. Aside from syntactic differences, HCL lets you use features that the JSON and YAML formats don't support.

The examples in this document use the HCL format.

A target reflects a single `docker build` invocation. Consider the following build command:

You can express this command in a Bake file as follows:

The following table shows the complete list of attributes that you can assign to a target:

NameTypeDescription[`args`](#targetargs)MapBuild arguments[`annotations`](#targetannotations)ListExporter annotations[`attest`](#targetattest)ListBuild attestations[`cache-from`](#targetcache-from)ListExternal cache sources[`cache-to`](#targetcache-to)ListExternal cache destinations[`call`](#targetcall)StringSpecify the frontend method to call for the target.[`context`](#targetcontext)StringSet of files located in the specified path or URL[`contexts`](#targetcontexts)MapAdditional build contexts[`description`](#targetdescription)StringDescription of a target[`dockerfile-inline`](#targetdockerfile-inline)StringInline Dockerfile string[`dockerfile`](#targetdockerfile)StringDockerfile location[`entitlements`](#targetentitlements)ListPermissions that the build process requires to run[`extra-hosts`](#targetextra-hosts)ListCustoms host-to-IP mapping[`inherits`](#targetinherits)ListInherit attributes from other targets[`labels`](#targetlabels)MapMetadata for images[`matrix`](#targetmatrix)MapDefine a set of variables that forks a target into multiple targets.[`name`](#targetname)StringOverride the target name when using a matrix.[`no-cache-filter`](#targetno-cache-filter)ListDisable build cache for specific stages[`no-cache`](#targetno-cache)BooleanDisable build cache completely[`output`](#targetoutput)ListOutput destinations[`platforms`](#targetplatforms)ListTarget platforms[`pull`](#targetpull)BooleanAlways pull images[`secret`](#targetsecret)ListSecrets to expose to the build[`shm-size`](#targetshm-size)ListSize of `/dev/shm`[`ssh`](#targetssh)ListSSH agent sockets or keys to expose to the build[`tags`](#targettags)ListImage names and tags[`target`](#targettarget)StringTarget build stage[`ulimits`](#targetulimits)ListUlimit options

### [`target.args`](#targetargs)

Use the `args` attribute to define build arguments for the target. This has the same effect as passing a [`--build-arg`](https://docs.docker.com/reference/cli/docker/image/build/#build-arg) flag to the build command.

You can set `args` attributes to use `null` values. Doing so forces the `target` to use the `ARG` value specified in the Dockerfile.

### [`target.annotations`](#targetannotations)

The `annotations` attribute lets you add annotations to images built with bake. The key takes a list of annotations, in the format of `KEY=VALUE`.

By default, the annotation is added to image manifests. You can configure the level of the annotations by adding a prefix to the annotation, containing a comma-separated list of all the levels that you want to annotate. The following example adds annotations to both the image index and manifests.

Read about the supported levels in [Specifying annotation levels](https://docs.docker.com/build/building/annotations/#specifying-annotation-levels).

### [`target.attest`](#targetattest)

The `attest` attribute lets you apply [build attestations](https://docs.docker.com/build/attestations/) to the target. This attribute accepts the long-form CSV version of attestation parameters.

### [`target.cache-from`](#targetcache-from)

Build cache sources. The builder imports cache from the locations you specify. It uses the [Buildx cache storage backends](https://docs.docker.com/build/cache/backends/), and it works the same way as the [`--cache-from`](https://docs.docker.com/reference/cli/docker/buildx/build/#cache-from) flag. This takes a list value, so you can specify multiple cache sources.

### [`target.cache-to`](#targetcache-to)

Build cache export destinations. The builder exports its build cache to the locations you specify. It uses the [Buildx cache storage backends](https://docs.docker.com/build/cache/backends/), and it works the same way as the [`--cache-to` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#cache-to). This takes a list value, so you can specify multiple cache export targets.

### [`target.call`](#targetcall)

Specifies the frontend method to use. Frontend methods let you, for example, execute build checks only, instead of running a build. This is the same as the `--call` flag.

Supported values are:

- `build` builds the target (default)
- `check`: evaluates [build checks](https://docs.docker.com/build/checks/) for the target
- `outline`: displays the target's build arguments and their default values if available
- `targets`: lists all Bake targets in the loaded definition, along with its [description](#targetdescription).

For more information about frontend methods, refer to the CLI reference for [`docker buildx build --call`](https://docs.docker.com/reference/cli/docker/buildx/build/#call).

### [`target.context`](#targetcontext)

Specifies the location of the build context to use for this target. Accepts a URL or a directory path. This is the same as the [build context](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context) positional argument that you pass to the build command.

This resolves to the current working directory (`"."`) by default.

### [`target.contexts`](#targetcontexts)

Additional build contexts. This is the same as the [`--build-context` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#build-context). This attribute takes a map, where keys result in named contexts that you can reference in your builds.

You can specify different types of contexts, such local directories, Git URLs, and even other Bake targets. Bake automatically determines the type of a context based on the pattern of the context value.

Context typeExampleContainer image`docker-image://alpine@sha256:0123456789`Git URL`https://github.com/user/proj.git`HTTP URL`https://example.com/files`Local directory`../path/to/src`Bake target`target:base`

#### [Pin an image version](#pin-an-image-version)

#### [Use a local directory](#use-a-local-directory)

#### [Use another target as base](#use-another-target-as-base)

> You should prefer to use regular multi-stage builds over this option. You can Use this feature when you have multiple Dockerfiles that can't be easily merged into one.

### [`target.description`](#targetdescription)

Defines a human-readable description for the target, clarifying its purpose or functionality.

This attribute is useful when combined with the `docker buildx bake --list=targets` option, providing a more informative output when listing the available build targets in a Bake file.

### [`target.dockerfile-inline`](#targetdockerfile-inline)

Uses the string value as an inline Dockerfile for the build target.

The `dockerfile-inline` takes precedence over the `dockerfile` attribute. If you specify both, Bake uses the inline version.

### [`target.dockerfile`](#targetdockerfile)

Name of the Dockerfile to use for the build. This is the same as the [`--file` flag](https://docs.docker.com/reference/cli/docker/image/build/#file) for the `docker build` command.

Resolves to `"Dockerfile"` by default.

### [`target.entitlements`](#targetentitlements)

Entitlements are permissions that the build process requires to run.

Currently supported entitlements are:

- `network.host`: Allows the build to use commands that access the host network. In Dockerfile, use [`RUN --network=host`](https://docs.docker.com/reference/dockerfile/#run---networkhost) to run a command with host network enabled.
- `security.insecure`: Allows the build to run commands in privileged containers that are not limited by the default security sandbox. Such container may potentially access and modify system resources. In Dockerfile, use [`RUN --security=insecure`](https://docs.docker.com/reference/dockerfile/#run---security) to run a command in a privileged container.

Entitlements are enabled with a two-step process. First, a target must declare the entitlements it requires. Secondly, when invoking the `bake` command, the user must grant the entitlements by passing the `--allow` flag or confirming the entitlements when prompted in an interactive terminal. This is to ensure that the user is aware of the possibly insecure permissions they are granting to the build process.

Use the `extra-hosts` attribute to define customs host-to-IP mapping for the target. This has the same effect as passing a [`--add-host`](https://docs.docker.com/reference/cli/docker/buildx/build/#add-host) flag to the build command.

### [`target.inherits`](#targetinherits)

A target can inherit attributes from other targets. Use `inherits` to reference from one target to another.

In the following example, the `app-dev` target specifies an image name and tag. The `app-release` target uses `inherits` to reuse the tag name.

The `inherits` attribute is a list, meaning you can reuse attributes from multiple other targets. In the following example, the `app-release` target reuses attributes from both the `app-dev` and `_release` targets.

When inheriting attributes from multiple targets and there's a conflict, the target that appears last in the `inherits` list takes precedence. The previous example defines the `BUILDX_EXPERIMENTAL` argument twice for the `app-release` target. It resolves to `0` because the `_release` target appears last in the inheritance chain:

### [`target.labels`](#targetlabels)

Assigns image labels to the build. This is the same as the `--label` flag for `docker build`.

It's possible to use a `null` value for labels. If you do, the builder uses the label value specified in the Dockerfile.

### [`target.matrix`](#targetmatrix)

A matrix strategy lets you fork a single target into multiple different variants, based on parameters that you specify. This works in a similar way to \[Matrix strategies for GitHub Actions]. You can use this to reduce duplication in your bake definition.

The `matrix` attribute is a map of parameter names to lists of values. Bake builds each possible combination of values as a separate target.

Each generated target **must** have a unique name. To specify how target names should resolve, use the `name` attribute.

The following example resolves the `app` target to `app-foo` and `app-bar`. It also uses the matrix value to define the [target build stage](#targettarget).

#### [Multiple axes](#multiple-axes)

You can specify multiple keys in your matrix to fork a target on multiple axes. When using multiple matrix keys, Bake builds every possible variant.

The following example builds four targets:

- `app-foo-1-0`
- `app-foo-2-0`
- `app-bar-1-0`
- `app-bar-2-0`

#### [Multiple values per matrix target](#multiple-values-per-matrix-target)

If you want to differentiate the matrix on more than just a single value, you can use maps as matrix values. Bake creates a target for each map, and you can access the nested values using dot notation.

The following example builds two targets:

- `app-foo-1-0`
- `app-bar-2-0`

### [`target.name`](#targetname)

Specify name resolution for targets that use a matrix strategy. The following example resolves the `app` target to `app-foo` and `app-bar`.

### [`target.network`](#targetnetwork)

Specify the network mode for the whole build request. This will override the default network mode for all the `RUN` instructions in the Dockerfile. Accepted values are `default`, `host`, and `none`.

Usually, a better approach to set the network mode for your build steps is to instead use `RUN --network=<value>` in your Dockerfile. This way, you can set the network mode for individual build steps and everyone building the Dockerfile gets consistent behavior without needing to pass additional flags to the build command.

If you set network mode to `host` in your Bake file, you must also grant `network.host` entitlement when invoking the `bake` command. This is because `host` network mode requires elevated privileges and can be a security risk. You can pass `--allow=network.host` to the `docker buildx bake` command to grant the entitlement, or you can confirm the entitlement when prompted if you are using an interactive terminal.

### [`target.no-cache-filter`](#targetno-cache-filter)

Don't use build cache for the specified stages. This is the same as the `--no-cache-filter` flag for `docker build`. The following example avoids build cache for the `foo` build stage.

### [`target.no-cache`](#targetno-cache)

Don't use cache when building the image. This is the same as the `--no-cache` flag for `docker build`.

### [`target.output`](#targetoutput)

Configuration for exporting the build output. This is the same as the [`--output` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#output). The following example configures the target to use a cache-only output,

### [`target.platforms`](#targetplatforms)

Set target platforms for the build target. This is the same as the [`--platform` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#platform). The following example creates a multi-platform build for three architectures.

### [`target.pull`](#targetpull)

Configures whether the builder should attempt to pull images when building the target. This is the same as the `--pull` flag for `docker build`. The following example forces the builder to always pull all images referenced in the build target.

### [`target.secret`](#targetsecret)

Defines secrets to expose to the build target. This is the same as the [`--secret` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#secret).

This lets you [mount the secret](https://docs.docker.com/reference/dockerfile/#run---mounttypesecret) in your Dockerfile.

### [`target.shm-size`](#targetshm-size)

Sets the size of the shared memory allocated for build containers when using `RUN` instructions.

The format is `<number><unit>`. `number` must be greater than `0`. Unit is optional and can be `b` (bytes), `k` (kilobytes), `m` (megabytes), or `g` (gigabytes). If you omit the unit, the system uses bytes.

This is the same as the `--shm-size` flag for `docker build`.

> In most cases, it is recommended to let the builder automatically determine the appropriate configurations. Manual adjustments should only be considered when specific performance tuning is required for complex build scenarios.

### [`target.ssh`](#targetssh)

Defines SSH agent sockets or keys to expose to the build. This is the same as the [`--ssh` flag](https://docs.docker.com/reference/cli/docker/buildx/build/#ssh). This can be useful if you need to access private repositories during a build.

### [`target.tags`](#targettags)

Image names and tags to use for the build target. This is the same as the [`--tag` flag](https://docs.docker.com/reference/cli/docker/image/build/#tag).

### [`target.target`](#targettarget)

Set the target build stage to build. This is the same as the [`--target` flag](https://docs.docker.com/reference/cli/docker/image/build/#target).

### [`target.ulimits`](#targetulimits)

Ulimits overrides the default ulimits of build's containers when using `RUN` instructions and are specified with a soft and hard limit as such: `<type>=<soft limit>[:<hard limit>]`, for example:

> If you do not provide a `hard limit`, the `soft limit` is used for both values. If no `ulimits` are set, they are inherited from the default `ulimits` set on the daemon.

> In most cases, it is recommended to let the builder automatically determine the appropriate configurations. Manual adjustments should only be considered when specific performance tuning is required for complex build scenarios.

Groups allow you to invoke multiple builds (targets) at once.

Groups take precedence over targets, if both exist with the same name. The following bake file builds the `default` group. Bake ignores the `default` target.

The HCL file format supports variable block definitions. You can use variables as build arguments in your Dockerfile, or interpolate them in attribute values in your Bake file.

You can assign a default value for a variable in the Bake file, or assign a `null` value to it. If you assign a `null` value, Buildx uses the default value from the Dockerfile instead.

You can also add a description of the variable's purpose with the `description` field. This attribute is useful when combined with the `docker buildx bake --list=variables` option, providing a more informative output when listing the available variables in a Bake file.

You can override variable defaults set in the Bake file using environment variables. The following example sets the `TAG` variable to `dev`, overriding the default `latest` value shown in the previous example.

Variables can also be assigned an explicit type. If provided, it will be used to validate the default value (if set), as well as any overrides. This is particularly useful when using complex types which are intended to be overridden. The previous example could be expanded to apply an arbitrary series of tags.

This example shows how to generate three tags without changing the file or using custom functions/parsing:

### [Variable typing](#variable-typing)

The following primitive types are available:

- `string`
- `number`
- `bool`

The type is expressed like a keyword; it must be expressed as a literal:

Specifying primitive types can be valuable to show intent (especially when a default is not provided), but bake will generally behave as expected without explicit typing.

Complex types are expressed with "type constructors"; they are:

- `tuple([<type>,...])`
- `list(<type>)`
- `set(<type>)`
- `map(<type>)`
- `object({<attr>=<type>},...})`

The following are examples of each of those, as well as how the (optional) default value would be expressed:

Note that in each example, the default value would be valid even if typing was not present. If typing was omitted, the first three would all be considered `tuple`; you would be restricted to functions that operate on `tuple` and, for example, not be able to add elements. Similarly, the third and fourth would both be considered `object`, with the limits and semantics of that type. In short, in the absence of a type, any value delimited with `[]` is a `tuple` and value delimited with `{}` is an `object`. Explicit typing for complex types not only opens up the ability to use functions applicable to that specialized type, but is also a precondition for providing overrides.

> See [HCL Type Expressions](https://github.com/hashicorp/hcl/tree/main/ext/typeexpr) page for more details.

### [Overriding variables](#overriding-variables)

As mentioned in the [intro to variables](#variable), primitive types (`string`, `number`, and `bool`) can be overridden without typing and will generally behave as expected. (When explicit typing is not provided, a variable is assumed to be primitive when the default value lacks `{}` or `[]` delimiters; a variable with neither typing nor a default value is treated as `string`.) Naturally, these same overrides can be used alongside explicit typing too; they may help in edge cases where you want `VAR=true` to be a `string`, where without typing, it may be a `string` or a `bool` depending on how/where it's used. Overriding a variable with a complex type can only be done when the type is provided. This is still done via environment variables, but the values can be provided via CSV or JSON.

#### [CSV overrides](#csv-overrides)

This is considered the canonical method and is well suited to interactive usage. It is assumed that `list` and `set` will be the most common complex type, as well as the most common complex type designed to be overridden. Thus, there is full CSV support for `list` and `set` (and `tuple`; despite being considered a structural type, it is more like a collection type in this regard).

There is limited support for `map` and `object` and no support for composite types; for these advanced cases, an alternative mechanism [using JSON](#json-overrides) is available.

#### [JSON overrides](#json-overrides)

Overrides can also be provided via JSON. This is the only method available for providing some complex types and may be convenient if overrides are already JSON (for example, if they come from a JSON API). It can also be used when dealing with values are difficult or impossible to specify using CSV (e.g., values containing quotes or commas). To use JSON, simply append `_JSON` to the variable name. In this contrived example, CSV cannot handle the second value; despite being a supported CSV type, JSON must be used:

This example illustrates some precedence and usage rules:

The variable `FOO` can *only* be overridden using CSV because `FOO_JSON`, which would typically used for a JSON override, is already a defined variable. Since `FOO_JSON` is an actual variable, setting that environment variable would be expected to a CSV value. A JSON override *is* possible for this variable, using environment variable `FOO_JSON_JSON`.

### [Built-in variables](#built-in-variables)

The following variables are built-ins that you can use with Bake without having to define them.

VariableDescription`BAKE_CMD_CONTEXT`Holds the main context when building using a remote Bake file.`BAKE_LOCAL_PLATFORM`Returns the current platform’s default platform specification (e.g. `linux/amd64`).

### [Use environment variable as default](#use-environment-variable-as-default)

You can set a Bake variable to use the value of an environment variable as a default value:

### [Interpolate variables into attributes](#interpolate-variables-into-attributes)

To interpolate a variable into an attribute string value, you must use curly brackets. The following doesn't work:

Wrap the variable in curly brackets where you want to insert it:

Before you can interpolate a variable into an attribute, first you must declare it in the bake file, as demonstrated in the following example.

A [set of general-purpose functions](https://github.com/docker/buildx/blob/master/docs/bake-stdlib.md) provided by [go-cty](https://github.com/zclconf/go-cty/tree/main/cty/function/stdlib) are available for use in HCL files:

In addition, [user defined functions](https://github.com/hashicorp/hcl/tree/main/ext/userfunc) are also supported:

> See [User defined HCL functions](https://docs.docker.com/build/bake/hcl-funcs/) page for more details.