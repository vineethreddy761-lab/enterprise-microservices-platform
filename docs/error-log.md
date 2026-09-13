# Enterprise Platform Error Log & Troubleshooting Guide

| Error ID | Component | Symptom | Root Cause | Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **ERR-001** | NetworkPolicy / DNS | Upstream pods unable to communicate with PostgreSQL. | Default-deny NetworkPolicy blocking cross-namespace traffic. | Apply explicit namespace allow rules targeting port `5432`. |
| **ERR-002** | HashiCorp Vault | Database connection failing with unauthorized token. | Vault short-lived lease token expired without auto-renewal. | Verify Vault Agent sidecar annotation configurations and token TTL settings. |
| **ERR-003** | Nginx Ingress | 502 Bad Gateway during traffic spike. | Shared memory zone exhaustion (`api_limit` too small). | Increase shared memory size parameter in Nginx configuration to `64m` or higher. |
| **ERR-004** | GitHub Actions | Workflow parsing failure on push. | Invisible carriage return (`\r`) line endings or invalid YAML indentation. | Recreate workflow files using standard Unix line endings (`\n`) and validate via python3. |
| **ERR-005** | Custom Resources | `kubectl apply --dry-run` failing on unknown CRDs. | Runner environment missing CRD schema definitions for ArgoCD, Flagger, or KEDA. | Separate native Kubernetes object validation from custom YAML syntax checks in CI pipeline. |
