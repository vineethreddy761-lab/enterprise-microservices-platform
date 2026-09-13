# Troubleshooting & Resolved Errors

## 1. NGINX Ingress Controller `fork/exec /usr/bin/nginx: input/output error`
- **Symptom**: NGINX Ingress controller pods entered `CrashLoopBackOff` with `unexpected error obtaining NGINX version`.
- **Cause**: Incompatible manifest version applied to the Kind cluster.
- **Resolution**: Uninstalled the main branch manifest and applied a stable version (`controller-v1.10.0`) designed for Kind.

## 2. Database Connection Error `database "enterprise" does not exist`
- **Symptom**: Backend traffic successfully routed through ingress but failed with a database missing error.
- **Cause**: The PostgreSQL container was running, but the specific database had not been initialized.
- **Resolution**: Executed `CREATE DATABASE enterprise;` inside the PostgreSQL StatefulSet pod.

## 3. Helm Release Name Conflict (`cannot reuse a name that is still in use`)
- **Symptom**: Helm installation failed due to an interrupted prior release.
- **Resolution**: Ran `helm uninstall monitoring-stack --namespace monitoring` before re-running the installation.

## 4. Otel Collector Block Mapping Parser Error
- **Symptom**: `yaml.parser.ParserError` encountered at line 27 of `collector.yaml`.
- **Resolution**: Separated the ConfigMap and Deployment into a clean multi-document manifest.

## 5. Grafana Dashboards ConfigMap JSON Parsing Error
- **Symptom**: Embedded JSON curly braces in `grafana-dashboards.yaml` misconstrued as block mapping keys.
- **Resolution**: Simplified the ConfigMap structure into clean key-value text pairs.

## 6. Kind Control Plane Disconnection & API Timeout
- **Symptom**: `TLS handshake timeout` and missing cluster control plane nodes.
- **Resolution**: Recreated the Kind cluster and re-exported the kubeconfig context.
