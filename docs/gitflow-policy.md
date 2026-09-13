# Enterprise GitFlow & Branching Strategy

## Branch Naming Conventions
- **`main`**: Production-ready code. All merges require passing CI/CD checks and peer review.
- **`develop`**: Integration branch for ongoing feature development.
- **`feature/**`**: New features, microservice tiers, or infrastructure updates (branched from `develop`, merged back via Pull Request).
- **`release/**`**: Release preparation, version bumping, and final testing.
- **`hotfix/**`**: Urgent production patch fixes.

## Automated Pull Request Rules
1. **Required Status Checks**: All PRs must pass the offline YAML validation and script syntax checks in GitHub Actions.
2. **Review Policy**: At least one explicit peer review approval is mandatory before merging into `main` or `develop`.
