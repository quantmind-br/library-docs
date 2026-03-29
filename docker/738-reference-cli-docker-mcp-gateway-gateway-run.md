---
title: docker mcp gateway run
url: https://docs.docker.com/reference/cli/docker/mcp/gateway/gateway_run/
source: llms
fetched_at: 2026-01-24T14:37:35.365661326-03:00
rendered_js: false
word_count: 242
summary: This document provides a comprehensive list of command-line flags and configuration options for managing Docker MCP servers and the associated gateway.
tags:
    - docker-mcp
    - cli-reference
    - configuration-flags
    - mcp-gateway
    - server-management
category: reference
---

OptionDefaultDescription`--additional-catalog`Additional catalog paths to append to the default catalogs`--additional-config`Additional config paths to merge with the default config.yaml`--additional-registry`Additional registry paths to merge with the default registry.yaml`--additional-tools-config`Additional tools paths to merge with the default tools.yaml`--block-network`Block tools from accessing forbidden network resources`--block-secrets``true`Block secrets from being/received sent to/from tools`--catalog``[docker-mcp.yaml]`Paths to docker catalogs (absolute or relative to ~/.docker/mcp/catalogs/)  
`--config``[config.yaml]`Paths to the config files (absolute or relative to ~/.docker/mcp/)`--cpus``1`CPUs allocated to each MCP Server (default is 1)`--debug-dns`Debug DNS resolution`--dry-run`Start the gateway but do not listen for connections (useful for testing the configuration)  
`--enable-all-servers`Enable all servers in the catalog (instead of using individual --servers options)  
`--interceptor`List of interceptors to use (format: when:type:path, e.g. 'before:exec:/bin/path')  
`--log-calls``true`Log calls to the tools`--long-lived`Containers are long-lived and will not be removed until the gateway is stopped, useful for stateful servers  
`--mcp-registry`MCP registry URLs to fetch servers from (can be repeated)`--memory``2Gb`Memory allocated to each MCP Server (default is 2Gb)`--oci-ref`OCI image references to use`--port`TCP port to listen on (default is to listen on stdio)`--registry``[registry.yaml]`Paths to the registry files (absolute or relative to ~/.docker/mcp/)  
`--secrets``docker-desktop`Colon separated paths to search for secrets. Can be `docker-desktop` or a path to a .env file (default to using Docker Desktop's secrets API)  
`--servers`Names of the servers to enable (if non empty, ignore --registry flag)  
`--static`Enable static mode (aka pre-started servers)`--tools`List of tools to enable`--tools-config``[tools.yaml]`Paths to the tools files (absolute or relative to ~/.docker/mcp/)`--transport``stdio`stdio, sse or streaming (default is stdio)`--verbose`Verbose output`--verify-signatures`Verify signatures of the server images`--watch``true`Watch for changes and reconfigure the gateway