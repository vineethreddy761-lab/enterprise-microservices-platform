---

## Architecture Overview (10 Tiers)

1. **Tier 1: Edge & Ingress (`k8s/tier1-ingress`)** - Nginx API Gateway, SSL termination, and rate-limiting zones running on dedicated edge nodes (`worker-edge-01`).
2. **Tier 2: Backend Microservices (`k8s/tier2-backend`)** - Priority-isolated application workloads running on high-performance compute nodes (`c6i.2xlarge`).
3. **Tier 3: Locked-Down Data Layer (`k8s/tier3-data`)** - PostgreSQL StatefulSet and distributed Redis caching cluster running on storage and memory-optimized nodes with zero-trust NetworkPolicies.
4. **Tier 4: Observability & Control Plane (`k8s/tier4-observability`)** - Prometheus monitoring, Grafana dashboards, and HashiCorp Vault dynamic secret injection.
5. **Tier 5: GitOps & Progressive Delivery (`k8s/tier5-gitops`)** - ArgoCD Application syncs and Flagger Canary release policies.
6. **Tier 6: Resilience & Chaos Engineering (`k8s/tier6-resilience`)** - Chaos Mesh network latency experiments, KEDA autoscalers, and Karpenter node provisioners.
7. **Tier 7: AI/ML Inference & GPU Analytics (`k8s/tier7-aiml`)** - Dedicated GPU nodes (`g4dn.xlarge`) running high-performance inference workloads.
8. **Tier 8: Developer Portal & Governance (`k8s/tier8-developer-portal`)** - Internal developer portal and service cataloging infrastructure.
9. **Tier 9: Edge Computing & IoT Ingestion (`k8s/tier9-edge-iot`)** - Eclipse Mosquitto MQTT message brokers for distributed IoT data streams.
10. **Tier 10: Multi-Cloud Policy Governance (`k8s/tier10-governance`)** - Open Policy Agent (OPA) validation servers for compliance auditing.

---

## Infrastructure & Security Add-ons
- **Specialized Server Pools**: Edge, Compute, Storage, GPU, Security (Falco), Bastion, Cache, Backup (Velero), Portal, IoT, and Governance nodes.
- **Runtime Threat Detection**: Falco daemonset auditing kernel system calls.
- **Hardened Access**: Encrypted OpenSSH jump host bastion deployment.
- **CI/CD Pipeline**: GitHub Actions offline YAML syntax validation and deployment script verification.

## Enterprise Microservices Platform (Lightweight Local Setup)

This repository houses an enterprise microservices platform optimized for local execution using **Kind (Kubernetes in Docker)** and **Docker** on resource-constrained development environments (such as Ubuntu VMs).

### Architecture & Resource Optimization Strategy
To prevent system freezes, storage I/O saturation, and kernel deadlocks (`D` state processes), this platform adheres to strict operational guidelines:
- **Single-Replica Deployments:** All microservices default to `replicas: 1` during initial rollout to minimize concurrent container image extraction and disk contention.
- **Docker Daemon Tuning:** Configured with elevated `ulimits` and strict log rotation to manage container logging overhead safely.
- **Multi-Terminal SSH Workflow:** Operations are managed across dedicated terminal windows (e.g., separate tabs for cluster management, workload deployment, and log streaming) to ensure responsiveness if a process blocks.

### Quick Start
1. Recreate the Kind cluster:
   ```bash
   kind create cluster --name enterprise-platform
   kind export kubeconfig --name enterprise-platform
