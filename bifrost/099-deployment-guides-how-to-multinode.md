---
title: Multinode Deployment
url: https://docs.getbifrost.ai/deployment-guides/how-to/multinode.md
source: llms
fetched_at: 2026-01-21T19:43:19.019846928-03:00
rendered_js: false
word_count: 720
summary: This document explains how to achieve high availability in Bifrost OSS deployments by using a shared configuration file across multiple nodes. It provides implementation strategies for Kubernetes and Docker Compose while highlighting the architectural differences between OSS and Enterprise clustering.
tags:
    - high-availability
    - multinode-deployment
    - bifrost-oss
    - kubernetes
    - docker-compose
    - deployment-strategies
category: guide
---

# Multinode Deployment

> Deploy multiple Bifrost nodes with shared configuration for high availability in OSS deployments

## Overview

Running multiple Bifrost nodes provides high availability, load distribution, and fault tolerance for your AI gateway. This guide covers the recommended approach for deploying multiple Bifrost nodes in OSS deployments.

### OSS vs Enterprise

| Aspect                   | OSS Approach                      | Enterprise Approach               |
| ------------------------ | --------------------------------- | --------------------------------- |
| **Configuration Source** | Shared `config.json` file         | Database with P2P sync            |
| **Sync Mechanism**       | File sharing (ConfigMap, volumes) | Gossip protocol (real-time)       |
| **Config Updates**       | Modify file + restart nodes       | UI/API with automatic propagation |

***

## How It Works

All configuration in Bifrost is loaded into memory at startup. For OSS multinode deployments, the recommended approach is to use `config.json` **without** `config_store` enabled.

### `config.json` as Single Source of Truth

When you deploy without `config_store`:

* **No database involved** - `config.json` is the only configuration source
* **Shared file** - All nodes read from the same `config.json` file
* **Identical configuration** - Since the source is shared, all nodes automatically have the same configuration
* **No sync needed** - The shared file itself ensures consistency

<Frame>
  <img src="https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=854f9485b56deae872055d54f50791c9" alt="OSS multi-node setup" data-og-width="1718" width="1718" data-og-height="1004" height="1004" data-path="media/oss-multinode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?w=280&fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=8dd385936e916cdefa6eb2052f813481 280w, https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?w=560&fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=d73bc52af20eb3cb94edb882278cd6ca 560w, https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?w=840&fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=bfc2d7a43d513ec9929e8e99efc9f3f7 840w, https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?w=1100&fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=c10f61e290f63e80bd369196e96fa238 1100w, https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?w=1650&fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=00945f8a2e6ee8039524da46cb510ae1 1650w, https://mintcdn.com/bifrost/Y0t6PENmoYOoYyEe/media/oss-multinode.png?w=2500&fit=max&auto=format&n=Y0t6PENmoYOoYyEe&q=85&s=9eb2acfe3e393b37d7d63428bf683d18 2500w" />
</Frame>

***

## Why not to use `config_store` for Multinode OSS?

Using `config_store` (database-backed configuration) with multiple nodes in OSS creates a **synchronization problem**:

1. **Config changes are local** - When you update configuration via the UI or API, it updates the database and the in-memory config on that specific node only
2. **No propagation mechanism** - Other nodes don't know about the change; they keep their existing in-memory configuration
3. **Nodes become out of sync** - Different nodes end up with different configurations
4. **Restart required** - You'd have to restart all nodes after every config change to bring them back in sync

This defeats the purpose of having database-backed configuration with real-time updates.

<Warning>
  Without P2P clustering (Enterprise feature), there's no mechanism to notify other nodes of configuration changes. For OSS multinode deployments, use the shared `config.json` approach instead.
</Warning>

### Enterprise Solution

Bifrost Enterprise includes **P2P clustering** with gossip protocol that automatically syncs configuration changes across all nodes in real-time. See the [Clustering documentation](/enterprise/clustering) for details.

***

## Setting Up Multinode OSS Deployment

### Example config.json

Create a `config.json` **without** `config_store` or `logs_store`:

```json  theme={null}
{
  "$schema": "https://www.getbifrost.ai/schema",
  "client": {
    "drop_excess_requests": false,
    "enable_logging": false,
    "enable_governance": false
  },
  "config_store": {
    "enabled": false
  },
  "logs_store": {
    "enabled": true,
    "type": "postgres",
    "config": {...}
  },
  "providers": {
    "openai": {
      "keys": [
        {
          "name": "openai-primary",
          "value": "env.OPENAI_API_KEY",
          "models": ["gpt-4o", "gpt-4o-mini"],
          "weight": 1.0
        }
      ]
    },
    "anthropic": {
      "keys": [
        {
          "name": "anthropic-primary",
          "value": "env.ANTHROPIC_API_KEY",
          "models": ["claude-sonnet-4-20250514", "claude-3-5-haiku-20241022"],
          "weight": 1.0
        }
      ]
    }
  }
}
```

<Note>
  Notice `config_store` is disabled. This ensures all configuration comes from the file only.
</Note>

### Kubernetes Deployment

Use a ConfigMap to share the same configuration across all pods:

```yaml  theme={null}
apiVersion: v1
kind: ConfigMap
metadata:
  name: bifrost-config
  namespace: default
data:
  config.json: |
    {
      "$schema": "https://www.getbifrost.ai/schema",
      "client": {
        "drop_excess_requests": false,
        "enable_logging": false,
        "enable_governance": false
      },
      "config_store": {
        "enabled": false
      },
      "logs_store": {
        "enabled": true,
        "type": "postgres",
        "config": {...}
      },
      "providers": {
        "openai": {
          "keys": [
            {
              "name": "openai-primary",
              "value": "env.OPENAI_API_KEY",
              "models": ["gpt-4o", "gpt-4o-mini"],
              "weight": 1.0
            }
          ]
        }
      }
    }
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bifrost
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: bifrost
  template:
    metadata:
      labels:
        app: bifrost
    spec:
      containers:
      - name: bifrost
        image: maximhq/bifrost:latest
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: provider-secrets
              key: openai-api-key
        volumeMounts:
        - name: config
          mountPath: /app
          readOnly: true
        resources:
          requests:
            cpu: 250m
            memory: 256Mi
          limits:
            cpu: 1000m
            memory: 1Gi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
      volumes:
      - name: config
        configMap:
          name: bifrost-config
---
apiVersion: v1
kind: Service
metadata:
  name: bifrost
  namespace: default
spec:
  type: LoadBalancer
  selector:
    app: bifrost
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
    name: http
```

### Docker Compose

Share the configuration using a bind mount:

```yaml  theme={null}
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - bifrost-1
      - bifrost-2
      - bifrost-3

  bifrost-1:
    image: maximhq/bifrost:latest
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./config.json:/app/config.json:ro
    expose:
      - "8080"

  bifrost-2:
    image: maximhq/bifrost:latest
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./config.json:/app/config.json:ro
    expose:
      - "8080"

  bifrost-3:
    image: maximhq/bifrost:latest
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./config.json:/app/config.json:ro
    expose:
      - "8080"
```

**nginx.conf** for load balancing:

```nginx  theme={null}
events {
    worker_connections 1024;
}

http {
    upstream bifrost {
        least_conn;
        server bifrost-1:8080;
        server bifrost-2:8080;
        server bifrost-3:8080;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://bifrost;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }

        location /health {
            access_log off;
            return 200 "healthy\n";
        }
    }
}
```

### Bare Metal / VM Deployment

For bare metal or VM deployments, distribute the configuration file using:

* **NFS mount** - Mount a shared NFS directory containing `config.json`
* **rsync** - Sync the config file from a central location to all nodes
* **Configuration management** - Use Ansible, Chef, or Puppet to deploy identical configs

Example with rsync:

```bash  theme={null}
# On config server - push to all nodes
for node in node1 node2 node3; do
  rsync -avz /etc/bifrost/config.json $node:/etc/bifrost/config.json
done

# Restart nodes after config update
for node in node1 node2 node3; do
  ssh $node "systemctl restart bifrost"
done
```

***

## Updating Configuration

To update configuration in a multinode OSS deployment:

1. **Modify the shared `config.json` file**
   * Update the ConfigMap (Kubernetes)
   * Edit the shared file (Docker Compose / bare metal)

2. **Restart the nodes**
   * Rolling restart is supported - nodes can be restarted one at a time
   * Each node picks up the new configuration on startup

### Kubernetes Rolling Restart

```bash  theme={null}
# Update ConfigMap
kubectl apply -f configmap.yaml

# Trigger rolling restart
kubectl rollout restart deployment/bifrost

# Watch the rollout
kubectl rollout status deployment/bifrost
```

### Docker Compose Restart

```bash  theme={null}
# After updating config.json
docker-compose restart bifrost-1
docker-compose restart bifrost-2
docker-compose restart bifrost-3
```

***

## Best Practices

### Use Environment Variables for Secrets

Never put API keys directly in `config.json`. Use the `env.` prefix to reference environment variables:

```json  theme={null}
{
  "providers": {
    "openai": {
      "keys": [
        {
          "value": "env.OPENAI_API_KEY"
        }
      ]
    }
  }
}
```

Then provide the actual keys via environment variables or Kubernetes secrets.

### Load Balancer Configuration

Always put a load balancer in front of your Bifrost nodes:

* **Kubernetes**: Use a Service with `type: LoadBalancer` or an Ingress
* **Docker/VMs**: Use nginx, HAProxy, or a cloud load balancer

### Health Checks

Configure health checks to ensure traffic only goes to healthy nodes:

* **Liveness endpoint**: `GET /health`
* **Readiness endpoint**: `GET /health`

### Resource Allocation

For production deployments:

```yaml  theme={null}
resources:
  requests:
    cpu: 500m
    memory: 512Mi
  limits:
    cpu: 2000m
    memory: 2Gi
```

***

## Summary

| Scenario             | Recommendation                                  |
| -------------------- | ----------------------------------------------- |
| Single node          | Use `config_store` for UI access                |
| Multinode OSS        | Use shared `config.json` without `config_store` |
| Multinode Enterprise | Use P2P clustering with `config_store`          |

For OSS multinode deployments, the shared `config.json` approach provides a simple, reliable way to keep all nodes in sync without the complexity of database synchronization.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt