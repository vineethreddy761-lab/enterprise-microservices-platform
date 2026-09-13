# Enterprise Microservices Platform

A robust, scalable, and observable microservices platform running on a Kind Kubernetes cluster.

## Architecture & Components
- **Cluster**: Kind (Kubernetes-in-Docker) on Ubuntu.
- **Ingress**: NGINX Ingress Controller (`enterprise.local`).
- **Backend**: Node.js microservice connected to PostgreSQL.
- **Database**: PostgreSQL StatefulSet with `enterprise` database schema.
- **Autoscaling**: KEDA (Kubernetes Event-driven Autoscaling) targeting CPU utilization.
- **Monitoring**: Prometheus and Grafana stack via Helm.

## Quick Start / Deployment
1. Deploy NGINX Ingress Controller.
2. Deploy PostgreSQL and create the database (`CREATE DATABASE enterprise;`).
3. Deploy the Node.js backend.
4. Install KEDA and apply the backend `ScaledObject`.
5. Deploy the Prometheus and Grafana monitoring stack via Helm.
