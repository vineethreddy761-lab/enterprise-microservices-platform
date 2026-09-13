import os
import yaml

def validate_yaml_files():
    print("Starting comprehensive validation of all Kubernetes manifests in k8s/...")
    total_files = 0
    errors_found = 0

    for root, dirs, files in os.walk("k8s"):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                path = os.path.join(root, file)
                total_files += 1
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        docs = list(yaml.safe_load_all(f))
                    
                    for i, doc in enumerate(docs):
                        if doc is None:
                            continue
                        if not isinstance(doc, dict):
                            print(f"[!] Invalid YAML structure in {path} (Doc {i+1})")
                            errors_found += 1
                            continue
                        
                        # Check required Kubernetes base fields
                        kind = doc.get("kind")
                        name = doc.get("metadata", {}).get("name")
                        
                        if kind and not name:
                            print(f"[!] MISSING NAME: {path} -> Kind '{kind}' (Document #{i+1}) lacks metadata.name")
                            errors_found += 1
                except Exception as e:
                    print(f"[!] PARSE ERROR: {path} -> {e}")
                    errors_found += 1

    print("\n==============================")
    print("VALIDATION SUMMARY")
    print(f"Total YAML files scanned: {total_files}")
    print(f"Errors/Missing names found: {errors_found}")
    print("==============================\n")

if __name__ == "__main__":
    validate_yaml_files()
