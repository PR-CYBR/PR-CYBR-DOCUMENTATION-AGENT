# Overview of Agent GitHub Actions

<!--
Key Objectives for this Document:
1. Define the purpose and role of GitHub Actions in the PR-CYBR Agent ecosystem.
2. Provide a clear structure for implementing CI/CD workflows.
3. Offer examples and templates for common automation tasks.
4. Outline best practices for managing and maintaining GitHub Actions.
-->

## Introduction

- Brief description of GitHub Actions and their relevance to the PR-CYBR Agents.
- Objectives of integrating GitHub Actions in agent workflows.

## Key Components

### Workflow Files
- Explanation of workflow file structure (e.g., `.yml` format).
- Common workflow files used in PR-CYBR Agents:
  - `ci-cd.yml`
  - `docker-compose.yml`
  - `openai-function.yml`

### Environment Variables
- Overview of `.env` file usage to securely manage sensitive variables.
- Key environment variables required for workflows (e.g., `Assistant ID`, API keys).
- Repository-level variables shared across workflows (for example `TF_CLOUD_ORGANIZATION`, `TF_WORKSPACE`, `TF_CONFIG_DIRECTORY`).

## Core CI/CD Workflows

### Build and Test Pipeline
- Purpose: Automate build and testing processes for agents.
- Example Workflow:

```yaml
  name: Build and Test

  on:
    push:
      branches:
        - main

  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'
        - name: Install Dependencies
          run: pip install -r requirements.txt
        - name: Run Tests
          run: pytest
```

## Deployment Pipeline

	•	Purpose: Automate deployment to production or staging environments.
	•	Example Workflow:

```yaml
name: Deploy Agent

on:
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Docker
        uses: docker/setup-buildx-action@v1
      - name: Build and Push Docker Image
        run: |
          docker build -t prcybr/agent:latest .
          docker push prcybr/agent:latest
      - name: Notify Deployment
        run: echo "Deployment successful!"
```

### Terraform Cloud Workflow Bridge (A-11)

- **Purpose**: Ensure Terraform Cloud performs all plans and applies so secrets and provider credentials remain centralized in Terraform Cloud workspaces.
- **Workflow file**: `.github/workflows/tfc-sync.yml` (Terraform Cloud Workflow Bridge).
- **Triggers**:
  - Pull requests targeting `main` upload configuration and start speculative plans.
  - Pushes to integration branches (`codex`, `agents`) upload configuration and request apply runs.
- **Required configuration**:
  - Repository variables `TF_CLOUD_ORGANIZATION`, `TF_WORKSPACE`, and optional `TF_CONFIG_DIRECTORY` (defaults to the repository root when unset).
  - GitHub Actions secret `TFC_WORKFLOW_TOKEN` generated from Terraform Cloud's workflow bridge token; GitHub stores only this trigger credential while Terraform Cloud retains all provider secrets.
- **Feedback loop**: The workflow comments on pull requests with the Terraform plan summary and links directly to the Terraform Cloud run for review.
- **Safety rails**: Auto-apply only proceeds when Terraform Cloud marks the run confirmable; otherwise maintainers approve the run inside Terraform Cloud.

## Best Practices

	•	Use modular workflows for reusability across agents.
	•	Implement caching to reduce build times.
	•	Securely manage secrets using GitHub Actions Secrets and Terraform Cloud workspace variables.
	•	Use versioned actions to ensure stability.

## Troubleshooting and Maintenance

•	Common issues and their resolutions:
	•	Failed builds.
	•	Permission errors with secrets or Docker registry.
•	Tips for maintaining workflows:
	•	Regularly update dependencies and action versions.
	•	Monitor workflow performance using GitHub Insights.

## Advanced Features

**Custom Runners**

	•	Benefits of using custom runners for PR-CYBR Agents.
	•	Configuration steps for setting up custom runners.

**Notifications and Alerts**

	•	Integrate notifications for workflow statuses using tools like Slack or email.
	•	Example notification step:

```yaml
- name: Send Slack Notification
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    fields: repo,message
```

## Appendix

	•	Glossary of terms (e.g., “runner”, “job”, “step”).
	•	Links to GitHub Actions documentation and resources.
	•	Workflow templates for quick reference.
