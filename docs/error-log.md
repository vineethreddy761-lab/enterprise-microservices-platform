# Engineering Error & Struggle Log

All configuration hurdles, unexpected failures, and system bugs encountered during development will be documented here.

## Template
[ERR-00X] Short Description of Issue
Symptom: Exact error message or observable behavior.

Root Cause: Deep-dive technical explanation of why it failed.

Solution: Step-by-step fix implemented.

Prevention: How to avoid or automate detection in the future.

## [ERR-001] Cross-Namespace DNS Resolution Failure in Tier 3 Database Connection
- **Symptom:** Backend microservices in `enterprise-backend` intermittently failed to connect to PostgreSQL in `enterprise-data` with `Name or service not known` errors.
- **Root Cause:** Kubernetes NetworkPolicy in the `enterprise-data` namespace enforced ingress restrictions, but the corresponding CoreDNS lookup was missing explicit namespace selector labels on the namespace object itself.
- **Solution:** Labeled the `enterprise-backend` namespace with `environment: enterprise-backend` and updated the NetworkPolicy namespaceSelector matchLabels accordingly.
- **Prevention:** Standardize namespace labeling conventions across all Terraform and Kubernetes manifest templates during the initial scaffolding phase.
