# Platform Troubleshooting & Error Log

## 1. Bash Syntax Error When Executing Python Code Directly
- **Symptom:** Pasting Python code directly into the active bash terminal caused syntax errors on keywords like `import`, `def`, and `print()`.
- **Resolution:** Saved the script into `deploy_platform.py` and executed it properly using `python3 deploy_platform.py`.

## 2. Namespace Creation Piping Hang
- **Symptom:** `kubectl create namespace ... --dry-run=client -o yaml | kubectl apply -f -` hung in certain local environments.
- **Resolution:** Replaced the piped command with a robust, non-blocking check: `kubectl get namespace enterprise-backend || kubectl create namespace enterprise-backend`.

## 3. Missing Root Manifest Files
- **Symptom:** The deployment script initially looked for flat YAML files in the root directory.
- **Resolution:** Updated `deploy_platform.py` to point directly to the modular manifest structure under the `k8s/` tiers (e.g., `k8s/tier3-data/database-statefulset.yaml`).
