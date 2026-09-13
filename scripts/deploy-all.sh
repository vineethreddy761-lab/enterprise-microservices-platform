#!/bin/bash
set -e

echo "=================================================="
echo "Deploying Enterprise Microservices Platform..."
echo "=================================================="

# Step 1: Create Namespaces for Micro-Segmentation
echo "[1/5] Creating isolated namespaces..."
kubectl create namespace enterprise-ingress --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace enterprise-backend --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace enterprise-data --dry-run=client -o yaml | kubectl apply -f -
kubectl create namespace enterprise-control-plane --dry-run=client -o yaml | kubectl apply -f -

# Step 2: Deploy Tier 4 Control Plane (Vault & Observability)
echo "[2/5] Deploying Tier 4 Control Plane & Observability..."
kubectl apply -f k8s/tier4-observability/vault-deployment.yaml
kubectl apply -f k8s/tier4-observability/prometheus-config.yaml
kubectl apply -f k8s/tier4-observability/grafana-dashboards.yaml

# Step 3: Deploy Tier 3 Data & Storage (StatefulSet & NetworkPolicies)
echo "[3/5] Deploying Tier 3 Data & Storage Tier (Zero-Trust Locked Down)..."
kubectl apply -f k8s/tier3-data/database-statefulset.yaml
kubectl apply -f k8s/tier3-data/network-policy.yaml

# Step 4: Deploy Tier 2 Application & Backend (Priority Classes & Services)
echo "[4/5] Deploying Tier 2 Backend & Priority Classes..."
kubectl apply -f k8s/tier2-backend/priority-classes.yaml
kubectl apply -f k8s/tier2-backend/backend-deployment.yaml

# Step 5: Deploy Tier 1 Edge & Ingress Gateway
echo "[5/5] Deploying Tier 1 Edge Ingress Gateway & WAF..."
kubectl apply -f k8s/tier1-ingress/deployment.yaml

echo "===================================================="
echo "Enterprise Architecture Deployed Successfully."
echo "===================================================="
