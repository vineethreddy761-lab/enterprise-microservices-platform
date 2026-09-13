# Enterprise Microservices Platform

A production-grade, highly scalable, and observable microservices platform running on a Kind Kubernetes cluster with multi-tier architecture, automated GitOps, runtime security, and policy governance.

## Architecture & Tiers
- **Cluster & Infrastructure**: Kind (Kubernetes-in-Docker) on Ubuntu.
- **Tier 1 (Ingress)**: NGINX Ingress Controller (`enterprise.local`).
- **Tier 2 (Backend)**: Node.js microservice integrated with Redis caching.
- **Tier 3 (Data)**: PostgreSQL StatefulSet with enterprise database schema and network policies.
- **Tier 4 (Observability)**: Prometheus, Grafana dashboards, OpenTelemetry, and Vault secret management.
- **Tier 5 (GitOps)**: ArgoCD application synchronization and canary rollout policies.
- **Tier 6 (Resilience)**: KEDA autoscaling, Velero backups, chaos engineering experiments, and circuit breakers.
- **Tier 7 (AI/ML)**: Scalable model inference deployment.
- **Tier 8 (Developer Portal)**: Internal developer portal integration.
- **Tier 9 (Edge IoT)**: MQTT-backed sensor publishers and subscribers.
- **Tier 10 (Governance & Security)**: Falco runtime security monitoring and OPA Gatekeeper policy enforcement.

## Quick Start & Deployment
1. Validate all manifests using `python3 validate_all_yaml.py`.
2. Deploy platform tiers using `python3 deploy_platform.py` or `./scripts/deploy-all.sh`.
3. Enforce security and governance policies via OPA Gatekeeper and Falco.
