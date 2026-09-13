# Enterprise Microservices Platform

An enterprise-grade, multi-tier microservices platform designed for high availability, robust security, and cloud-native resilience across local Kind clusters and production environments.

## Architecture & Tiers
The platform is structured into modular enterprise tiers located under `k8s/`:
- **Tier 1 (Ingress):** NGINX Ingress controller and routing rules.
- **Tier 2 (Backend):** Express.js microservice deployment and autoscaling objects.
- **Tier 3 (Data Storage):** PostgreSQL StatefulSet and Redis cache deployments.
- **Tier 4 & 6 (Observability & Resilience):** Prometheus, Grafana, OpenTelemetry, and Chaos engineering experiments.
- **Tier 5 & 10 (Gitops & Governance):** ArgoCD applications and OPA policy validators.

## Automated Local Deployment
You can fully automate the deployment of core platform services (Namespace, PostgreSQL, Redis, and Express Backend) onto your local Kind cluster using the provided Python automation script:
## CI/CD Pipeline
The GitHub Actions pipeline (`.github/workflows/ci-cd.yaml`) automatically validates all YAML manifests, spins up a test Kind cluster, builds local container images, and executes end-to-end deployment validation on every push or pull request.
