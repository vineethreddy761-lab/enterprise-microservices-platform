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
