import subprocess
import time
import sys

TIERS = [
    ("tier1-ingress", "enterprise-ingress"),
    ("tier2-backend", "enterprise-backend"),
    ("tier3-data", "enterprise-data"),
    ("tier4-observability", "enterprise-observability"),
    ("tier5-gitops", "enterprise-gitops"),
    ("tier6-resilience", "enterprise-resilience"),
    ("tier7-aiml", "enterprise-aiml"),
    ("tier8-developer-portal", "enterprise-devportal"),
    ("tier9-edge-iot", "enterprise-iot"),
    ("tier10-governance", "enterprise-governance")
]

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def main():
    print("Starting Throttled Sequential Enterprise Platform Deployment...\n")
    deployment_results = {}

    for tier, namespace in TIERS:
        path = f"k8s/{tier}"
        print(f"--- Deploying {tier} to namespace {namespace} ---")
        
        # Create namespace
        code, out, err = run_cmd(f"kubectl create namespace {namespace} --dry-run=client -o yaml | kubectl apply -f -")
        if code != 0:
            print(f"[-] Status: FAILED (Namespace creation for {tier})")
            deployment_results[tier] = "FAILED"
            continue

        # Apply manifests
        code, out, err = run_cmd(f"kubectl apply -f {path}/ -n {namespace}")
        if code != 0:
            print(f"[-] Status: FAILED (Manifest apply for {tier})")
            print(err)
            deployment_results[tier] = "FAILED"
        else:
            print(f"[+] Status: SUCCESS ({tier} applied successfully)")
            deployment_results[tier] = "SUCCESS"
        
        print(f"Waiting 20 seconds for {tier} workloads to stabilize...\n")
        time.sleep(20)

    print("\n==============================")
    print("DEPLOYMENT SUMMARY REPORT")
    print("==============================")
    for tier, status in deployment_results.items():
        print(f"{tier}: {status}")
    print("==============================\n")

    print("Checking pod status across all namespaces...")
    subprocess.run("kubectl get pods -A", shell=True)

if __name__ == "__main__":
    main()
