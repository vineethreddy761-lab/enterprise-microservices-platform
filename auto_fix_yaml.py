import os
import yaml

def fix_manifests():
    print("Starting automated YAML repair across k8s/...")
    fixed_count = 0

    for root, dirs, files in os.walk("k8s"):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        raw_docs = list(yaml.safe_load_all(f))
                    
                    # Filter out None / empty documents
                    valid_docs = [doc for doc in raw_docs if doc is not None and isinstance(doc, dict)]
                    if not valid_docs:
                        continue
                    
                    modified = False
                    base_name = os.path.splitext(file)[0].replace("_", "-")
                    
                    for idx, doc in enumerate(valid_docs):
                        # Ensure metadata exists
                        if "metadata" not in doc or not isinstance(doc["metadata"], dict):
                            doc["metadata"] = {}
                            modified = True
                        
                        # Assign name if missing
                        if not doc["metadata"].get("name"):
                            kind = doc.get("kind", "resource").lower()
                            suffix = f"-{idx+1}" if len(valid_docs) > 1 else ""
                            doc["metadata"]["name"] = f"{base_name}-{kind}{suffix}"
                            modified = True

                    # Rewrite the file cleanly if modified or to strip out None documents
                    with open(path, "w", encoding="utf-8") as f:
                        yaml.safe_dump_all(valid_docs, f, sort_keys=False)
                    
                    fixed_count += 1
                except Exception as e:
                    print(f"[!] Error fixing {path}: {e}")

    print(f"\nSuccessfully repaired and normalized {fixed_count} YAML files!")

if __name__ == "__main__":
    fix_manifests()
