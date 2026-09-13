#!/usr/bin/env bash
set -e

echo "=== Enterprise GitFlow Release Automation ==="

# Ensure working directory is clean
if [[ -n $(git status -s) ]]; then
echo "Error: Working directory is not clean. Commit or stash changes first."
exit 1
fi

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Current active branch: $CURRENT_BRANCH"

# Prompt for action
echo "Select release action:"
echo "1) Sync with main"
echo "2) Prepare release tag"
read -p "Enter choice [1-2]: " choice

if [ "$choice" == "1" ]; then
git checkout main
git pull origin main
echo "Successfully synchronized main branch."
elif [ "$choice" == "2" ]; then
read -p "Enter release version tag (e.g., v1.0.0): " version
git tag -a "$version" -m "Enterprise Release $version"
git push origin "$version"
echo "Successfully created and pushed release tag $version."
else
echo "Invalid selection."
exit 1
fi
