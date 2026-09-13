import subprocess

def run_cmd(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing: {command}")
        exit(1)

print("--- Starting Enterprise Microservices Deployment ---")

# 1. Ensure Namespace exists
run_cmd("kubectl get namespace enterprise-backend || kubectl create namespace enterprise-backend")

# 2. Deploy Database (Tier 3)
print("Deploying Database...")
run_cmd("kubectl apply -f k8s/tier3-data/database-statefulset.yaml")

# 3. Deploy Redis Cache (Tier 3)
print("Deploying Redis...")
run_cmd("kubectl apply -f k8s/tier3-data/redis-cache.yaml")

# 4. Deploy Backend (Tier 2)
print("Deploying Express Backend...")
run_cmd("kubectl apply -f k8s/tier2-backend/backend-deployment.yaml")

print("--- Platform Deployment Successfully Completed ---")
