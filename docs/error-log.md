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

## [ERR-002] Vault Dynamic Token Expiration Causing Database Connection Resets
- **Symptom:** Backend microservices experienced sudden database connection drops with `pq: password authentication failed for user` errors after exactly 1 hour of continuous runtime.
- **Root Cause:** The Vault dynamic database secrets engine role was configured with a strict default TTL of `1h`, but the application connection pool cached old credentials and did not listen for secret file updates rendered by the Vault Agent sidecar.
- **Solution:** Configured Vault Agent template rendering with automated file updates (`vault.hashicorp.com/agent-inject-template`) and implemented an in-memory file watcher in the backend application to gracefully refresh connection pools upon secret rotation.
- **Prevention:** Mandate dynamic secret rotation handlers in all stateful microservice templates and define explicit lease renewal grace periods in Vault backend roles.
