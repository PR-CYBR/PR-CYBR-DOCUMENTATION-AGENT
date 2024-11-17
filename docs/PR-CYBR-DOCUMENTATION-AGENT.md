**Assistant-ID**:
- `asst_xqS5VHO5ESFJhcnouiYN8SwW`

**Github Repository**:
- Repo: `https://github.com/PR-CYBR/PR-CYBR-DOCUMENTATION-AGENT`
- Setup Script (local): `https://github.com/PR-CYBR/PR-CYBR-DOCUMENTATION-AGENT/blob/main/scripts/local_setup.sh`
- Setup Script (cloud): `https://github.com/PR-CYBR/PR-CYBR-DOCUMENTATION-AGENT/blob/main/.github/workflows/docker-compose.yml`
- Project Board: `https://github.com/orgs/PR-CYBR/projects/9`
- Discussion Board: `https://github.com/PR-CYBR/PR-CYBR-DOCUMENTATION-AGENT/discussions`
- Wiki: `https://github.com/PR-CYBR/PR-CYBR-DOCUMENTATION-AGENT/wiki`

**Docker Repository**:
- Repo: `https://hub.docker.com/r/prcybr/pr-cybr-documentation-agent`
- Pull-Command:
```shell
docker pull prcybr/pr-cybr-documentation-agent
```


---


```markdown
# System Instructions for PR-CYBR-DOCUMENTATION-AGENT

## Role:
You are the `PR-CYBR-DOCUMENTATION-AGENT`, responsible for creating, maintaining, and managing all documentation related to the PR-CYBR initiative. Your mission is to ensure clarity, accessibility, and usability of all technical and non-technical documentation for PR-CYBR systems, tools, and processes.

## Core Functions:
1. **Documentation Creation**:
   - Write comprehensive user guides, technical manuals, FAQs, and onboarding resources for all PR-CYBR tools and systems.
   - Ensure all documentation aligns with PR-CYBR’s goals of accessibility, resilience, and inclusivity.
   - Translate technical jargon into clear and concise language suitable for different audiences, including non-technical users and community leaders.

2. **Content Maintenance**:
   - Regularly review and update documentation to reflect the latest features, fixes, and changes in PR-CYBR systems.
   - Work closely with PR-CYBR-FRONTEND-AGENT, PR-CYBR-BACKEND-AGENT, and PR-CYBR-SECURITY-AGENT to stay informed of updates and ensure documentation accuracy.

3. **Accessibility and Localization**:
   - Provide multilingual documentation to serve all regions and users within Puerto Rico.
   - Ensure documentation is accessible to users with varying levels of technical expertise and to those with disabilities.

4. **Collaboration**:
   - Partner with PR-CYBR-USER-FEEDBACK-AGENT to identify common user questions and pain points to prioritize documentation needs.
   - Align with PR-CYBR-TESTING-AGENT to document test cases, results, and known issues for both internal and external use.
   - Work with PR-CYBR-MGMT-AGENT to produce strategic reports and operational documents.

5. **Process Documentation**:
   - Document workflows, pipelines, and integration processes for PR-CYBR systems.
   - Provide detailed API documentation for PR-CYBR-BACKEND-AGENT and PR-CYBR-DATA-INTEGRATION-AGENT to facilitate third-party integrations.

6. **Training Resources**:
   - Create training materials, including tutorials, walkthroughs, and video guides, for users and contributors.
   - Develop educational resources for PR-CYBR’s community outreach and cybersecurity awareness campaigns.

7. **Version Control**:
   - Manage documentation repositories to ensure proper version control and traceability of changes.
   - Clearly mark deprecated features or workflows in documentation and provide migration instructions.

8. **Knowledge Base Management**:
   - Organize all documentation into a centralized knowledge base that is easily searchable and navigable.
   - Maintain a database of resolved issues, troubleshooting steps, and best practices.

9. **Feedback Integration**:
   - Incorporate user feedback received from PR-CYBR-USER-FEEDBACK-AGENT to continuously improve documentation quality.
   - Highlight frequently asked questions and common issues in user-facing documentation.

10. **Security and Privacy**:
    - Document cybersecurity best practices and guidelines for users, ensuring alignment with PR-CYBR’s mission.
    - Maintain confidentiality when documenting sensitive processes or systems.

11. **Compliance and Standards**:
    - Ensure all documentation adheres to technical writing standards, accessibility guidelines, and relevant compliance requirements.
    - Use standardized formats and templates to maintain consistency across all documents.

## Key Directives:
- Simplify complex information to make PR-CYBR resources accessible and understandable to all users.
- Provide accurate, up-to-date, and actionable documentation to empower users and contributors.
- Ensure documentation is a reliable and trusted resource for PR-CYBR’s community and stakeholders.

## Interaction Guidelines:
- Collaborate with all PR-CYBR agents to gather the necessary technical and operational details for documentation.
- Proactively identify areas where documentation can improve user experience and reduce support needs.
- Deliver documentation in a timely manner to coincide with the rollout of new features or updates.

## Context Awareness:
- Be aware of Puerto Rico’s regional and cultural diversity to tailor documentation to the needs of specific divisions, barrios, and sectors.
- Ensure consistency with PR-CYBR’s mission and branding across all documentation.
- Emphasize the importance of security, resilience, and collaboration in all user-facing resources.

## Tools and Capabilities:
You are equipped with technical writing tools, localization frameworks, and knowledge base management systems to ensure the quality and accessibility of PR-CYBR’s documentation. Leverage these to deliver precise, user-centric, and impactful documentation.
```

**Directory Structure**:

```shell
PR-CYBR-DOCUMENTATION-AGENT/
	.github/
		workflows/
			ci-cd.yml
			docker-compose.yml
			openai-function.yml
	config/
		docker-compose.yml
		secrets.example.yml
		settings.yml
	docs/
		OPORD/
		README.md
	scripts/
		deploy_agent.sh
		local_setup.sh
		provision_agent.sh
	src/
		agent_logic/
			__init__.py
			core_functions.py
		shared/
			__init__.py
			utils.py
	tests/
		test_core_functions.py
	web/
		README.md
		index.html
	.gitignore
	LICENSE
	README.md
	requirements.txt
	setup.py
```

## Agent Core Functionality Overview

```markdown
# PR-CYBR-DOCUMENTATION-AGENT Core Functionality Technical Outline

## Introduction

The **PR-CYBR-DOCUMENTATION-AGENT** is responsible for generating, maintaining, and organizing all documentation related to the PR-CYBR initiative. Its primary goal is to ensure that all technical and user-facing documentation is up-to-date, accessible, and accurately reflects the functionalities and processes of the various agents and systems within the initiative. This agent facilitates knowledge sharing among team members and provides comprehensive guides for users and contributors.
```

```markdown
### Directory Structure

PR-CYBR-DOCUMENTATION-AGENT/
├── config/
│   ├── settings.yml
│   ├── secrets.example.yml
├── docs/
│   ├── api/
│   │   ├── agent1_api.md
│   │   ├── agent2_api.md
│   │   └── ...
│   ├── user_guides/
│   │   ├── installation_guide.md
│   │   ├── usage_guide.md
│   │   └── ...
│   ├── developer_guides/
│   │   ├── contributing.md
│   │   ├── coding_standards.md
│   │   └── ...
│   ├── release_notes/
│   │   ├── v1.0.0.md
│   │   ├── v1.1.0.md
│   │   └── ...
│   ├── README.md
├── scripts/
│   ├── generate_docs.sh
│   ├── deploy_docs.sh
│   └── update_docs.sh
├── src/
│   ├── agent_logic/
│   │   ├── __init__.py
│   │   └── core_functions.py
│   ├── doc_generation/
│   │   ├── __init__.py
│   │   ├── doc_parser.py
│   │   ├── doc_formatter.py
│   │   └── doc_publisher.py
│   ├── shared/
│   │   ├── __init__.py
│   │   └── utils.py
├── tests/
│   ├── test_core_functions.py
│   ├── test_doc_generation.py
│   └── ...
└── web/
    ├── static/
    ├── templates/
    └── app.py
```

```markdown
## Key Files and Modules

- **`src/agent_logic/core_functions.py`**: Orchestrates the documentation processes, including generation, updating, and publishing.
- **`src/doc_generation/doc_parser.py`**: Parses source code and documentation files to extract relevant information.
- **`src/doc_generation/doc_formatter.py`**: Formats extracted information into structured documentation.
- **`src/doc_generation/doc_publisher.py`**: Publishes the documentation to designated platforms or repositories.
- **`src/shared/utils.py`**: Contains utility functions for file handling, configuration loading, and logging.
- **`scripts/generate_docs.sh`**: Automates the process of generating documentation from source code.
- **`scripts/deploy_docs.sh`**: Handles the deployment of documentation to web servers or repositories.
- **`docs/`**: Directory containing all generated and maintained documentation.

## Core Functionalities

### 1. Documentation Generation (`doc_parser.py` and `doc_formatter.py`)

#### Modules and Functions:

- **`parse_source_code()`** (`doc_parser.py`)
  - Scans source code files to extract comments and docstrings.
  - Inputs: Source code directories of all agents.
  - Outputs: Extracted documentation data.

- **`parse_existing_docs()`** (`doc_parser.py`)
  - Reads existing documentation files to include in the generation process.
  - Inputs: Documentation files in `docs/` directory.
  - Outputs: Parsed content for updating.

- **`format_documentation()`** (`doc_formatter.py`)
  - Converts parsed data into structured markdown or HTML formats.
  - Inputs: Extracted documentation data.
  - Outputs: Formatted documentation files.

#### Interaction with Other Agents:

- **Code Integration**: Accesses source code from agents like `PR-CYBR-BACKEND-AGENT`, `PR-CYBR-FRONTEND-AGENT`, etc.
- **Version Control**: Pulls the latest code from repositories to ensure documentation is up-to-date.

### 2. Documentation Updating and Maintenance (`core_functions.py` and `update_docs.sh`)

#### Modules and Functions:

- **`check_for_updates()`** (`core_functions.py`)
  - Monitors code repositories for changes that affect documentation.
  - Inputs: Git commit logs, code diffs.
  - Outputs: Triggers documentation regeneration when necessary.

- **`update_documentation()`** (`core_functions.py`)
  - Calls documentation generation modules to update docs.
  - Inputs: Notification of changes from `check_for_updates()`.
  - Outputs: Updated documentation files.

- **`update_docs.sh`**
  - Shell script that automates the update process.
  - Inputs: Execution trigger (manual or scheduled).
  - Outputs: Updated documentation in the `docs/` directory.

#### Interaction with Other Agents:

- **CI/CD Agent**: Integrates with `PR-CYBR-CI-CD-AGENT` to automate documentation updates during deployment pipelines.
- **Developer Agent**: Coordinates with `PR-CYBR-DEVELOPER-AGENT` to ensure developers document code changes.

### 3. Documentation Publishing (`doc_publisher.py` and `deploy_docs.sh`)

#### Modules and Functions:

- **`publish_to_web()`** (`doc_publisher.py`)
  - Deploys documentation to web servers or static site generators.
  - Inputs: Formatted documentation files.
  - Outputs: Published documentation accessible via web URLs.

- **`publish_to_repositories()`** (`doc_publisher.py`)
  - Pushes documentation to repositories like GitHub Pages or internal portals.
  - Inputs: Documentation files.
  - Outputs: Updated repositories with the latest documentation.

- **`deploy_docs.sh`**
  - Automates the deployment process.
  - Inputs: Execution trigger.
  - Outputs: Documentation deployed to specified platforms.

#### Interaction with Other Agents:

- **Frontend Agent**: May integrate with `PR-CYBR-FRONTEND-AGENT` to display documentation within user interfaces.
- **Management Agent**: Notifies `PR-CYBR-MGMT-AGENT` when new documentation is published.

### 4. Documentation Accessibility and Searchability (`web/app.py`)

#### Modules and Functions:

- **`serve_documentation()`**
  - Hosts documentation on a web server with search capabilities.
  - Inputs: Documentation files in markdown or HTML.
  - Outputs: User-friendly web interface for documentation.

- **`implement_search()`**
  - Provides search functionality to find information within documentation.
  - Inputs: User search queries.
  - Outputs: Relevant documentation sections.

#### Interaction with Other Agents:

- **User Feedback Agent**: Works with `PR-CYBR-USER-FEEDBACK-AGENT` to improve documentation based on user input.
- **Security Agent**: Ensures that published documentation does not expose sensitive information, coordinating with `PR-CYBR-SECURITY-AGENT`.

### 5. Collaboration and Contribution Management (`core_functions.py`)

#### Modules and Functions:

- **`manage_contributions()`**
  - Facilitates contributions to documentation from developers and users.
  - Inputs: Pull requests, issues, and suggestions.
  - Outputs: Updated documentation incorporating contributions.

- **`enforce_documentation_standards()`**
  - Ensures that documentation follows predefined styles and guidelines.
  - Inputs: Documentation content.
  - Outputs: Standardized documentation.

#### Interaction with Other Agents:

- **Developer Agent**: Collaborates with `PR-CYBR-DEVELOPER-AGENT` to manage contributions.
- **Testing Agent**: Works with `PR-CYBR-TESTING-AGENT` to include test cases and results in documentation.

## Inter-Agent Communication Mechanisms

### Communication Protocols

- **APIs**: Exposes endpoints for other agents to request documentation updates or access documentation data.
- **Webhooks**: Receives notifications from code repositories when changes occur.
- **Messaging Systems**: Uses internal messaging to coordinate with other agents.

### Data Formats

- **Markdown**: Primary format for writing and maintaining documentation.
- **HTML**: For web publishing and rendering documentation online.
- **YAML/JSON**: Configuration files and data exchange formats.

### Authentication and Authorization

- **Git Authentication**: Uses SSH keys or tokens to access repositories.
- **API Keys**: Secures communication with other agents.
- **User Authentication**: Manages access control for documentation contributions.

## Interaction with Specific Agents

### PR-CYBR-MGMT-AGENT

- **Documentation Requests**: Receives requests for specific documentation updates.
- **Reporting**: Provides reports on documentation coverage and updates.

### PR-CYBR-DEVELOPER-AGENT

- **Contribution Coordination**: Manages documentation contributions from developers.
- **Standards Enforcement**: Ensures code documentation aligns with coding standards.

### PR-CYBR-CI-CD-AGENT

- **Automation Integration**: Integrates documentation generation into CI/CD pipelines.
- **Deployment Synchronization**: Ensures documentation is updated alongside code deployments.

### PR-CYBR-USER-FEEDBACK-AGENT

- **Feedback Incorporation**: Updates documentation based on user feedback.
- **User Guides**: Enhances user-facing documentation to improve user experience.

## Technical Workflows

### Documentation Generation Workflow

1. **Trigger**: A code change or scheduled event triggers documentation generation.
2. **Parsing**: `parse_source_code()` extracts documentation from code.
3. **Formatting**: `format_documentation()` structures the content.
4. **Output**: Generated documentation is placed in the `docs/` directory.

### Documentation Update Workflow

1. **Monitoring**: `check_for_updates()` detects changes that affect documentation.
2. **Updating**: `update_documentation()` regenerates affected documentation sections.
3. **Publishing**: Updated documentation is published via `publish_to_web()` or `publish_to_repositories()`.

### Publishing Workflow

1. **Preparation**: Documentation files are prepared for publishing.
2. **Deployment**: `deploy_docs.sh` executes, deploying documentation to web servers or repositories.
3. **Verification**: Ensures that the published documentation is accessible and correctly rendered.

## Error Handling and Logging

- **Exception Handling**: Catches errors during parsing, formatting, and publishing.
- **Logging**: Maintains logs for generation and deployment processes.
- **Notifications**: Alerts relevant teams when errors occur in documentation workflows.

## Security Considerations

- **Access Controls**: Manages permissions for documentation editing and publishing.
- **Sensitive Information**: Scans documentation to prevent leakage of confidential data.
- **Secure Communication**: Uses encrypted channels for data transfer and repository access.

## Deployment and Scaling

- **Containerization**: The agent is containerized using Docker for consistent environments.
- **Automation**: Utilizes scripts and CI/CD integration for automated deployments.
- **Scalability**: Capable of handling documentation generation for multiple agents and large codebases.

## Conclusion

The **PR-CYBR-DOCUMENTATION-AGENT** is a critical component for maintaining clarity and knowledge sharing within the PR-CYBR initiative. By automating the generation and updating of documentation, it ensures that all stakeholders have access to accurate and up-to-date information. Its collaboration features facilitate contributions from developers and users alike, promoting a culture of transparency and continuous improvement.
```


---

## OpenAI Functions

## Function List for PR-CYBR-DOCUMENTATION-AGENT

```markdown
## Function List for PR-CYBR-DOCUMENTATION-AGENT

1. **create_user_guide**: Generates comprehensive user guides for various PR-CYBR tools and systems, ensuring clarity and ease of use.
2. **update_documentation**: Facilitates regular updates of existing documentation to reflect the latest changes and features within PR-CYBR systems.
3. **translate_documentation**: Provides translation services for documentation to cater to users in different languages, ensuring accessibility across regions.
4. **create_troubleshooting_guide**: Develops troubleshooting guides that assist users in resolving common issues or queries related to PR-CYBR tools.
5. **compile_faqs**: Gathers frequently asked questions and answers to build a comprehensive FAQ section for user support.
6. **document_workflows**: Records workflows and integration processes for PR-CYBR systems to aid in understanding and collaboration.
7. **create_training_materials**: Produces training resources, including video tutorials and walkthroughs, to educate users and contributors on PR-CYBR systems.
8. **manage_knowledge_base**: Organizes and maintains a centralized knowledge base that is easily searchable and provides access to all documentation.
9. **collect_user_feedback**: Integrates user feedback and suggestions to continuously improve documentation quality and user experience.
10. **ensure_compliance**: Reviews and ensures all documentation adheres to compliance and accessibility standards required by PR-CYBR.
```