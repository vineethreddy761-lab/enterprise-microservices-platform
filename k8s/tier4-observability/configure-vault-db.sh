#!/bin/bash
# Enable Database Secrets Engine in Vault
vault secrets enable database

# Configure PostgreSQL connection for Vault
vault write database/config/postgresql \
plugin_name=postgresql-database-plugin \
connection_url="postgresql://{{username}}:{{password}}@postgres-internal.enterprise-data.svc.cluster.local:5432/enterprise_core?sslmode=disable" \
allowed_roles="backend-service-role" \
username="postgres" \
password="super-secret-admin-password"

# Create a dynamic role with short-lived TTL (Time-To-Live)
vault write database/roles/backend-service-role \
db_name=postgresql \
creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL 'timestamp ''now + 1 hour'''; GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO \"{{name}}@\"" \
default_ttl="1h" \
max_ttl="24h"

echo "Vault Database Secrets Engine configured successfully!"
