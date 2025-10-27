# --- Terraform Variables ---
variable "AGENT_ID" {
  description = "Agent identifier for Documentation Agent (A-11)"
  type        = string
}

variable "DOCKERHUB_USERNAME" {
  description = "Docker Hub username for PR-CYBR containers"
  type        = string
}

variable "GLOBAL_DOMAIN" {
  description = "Primary domain for PR-CYBR infrastructure"
  type        = string
}

variable "PR_CYBR_DOCKER_USER" {
  description = "Docker Hub user for authenticated pushes"
  type        = string
}

variable "PR_CYBR_DOCKER_PASS" {
  description = "Sensitive Docker Hub access token"
  type        = string
}

# --- Environment Variables ---
variable "AGENT_ACTIONS" {
  description = "Sensitive variable controlling agent orchestration permissions"
  type        = string
}

variable "DOCKERHUB_TOKEN" {
  description = "Sensitive Docker Hub access token for API use"
  type        = string
}

variable "NOTION_DISCUSSIONS_ARC_DB_ID" {
  description = "Notion database ID for Discussions Archive"
  type        = string
}

variable "NOTION_ISSUES_BACKLOG_DB_ID" {
  description = "Notion database ID for Issues Backlog"
  type        = string
}

variable "NOTION_KNOWLEDGE_FILE_DB_ID" {
  description = "Notion database ID for Knowledge Files"
  type        = string
}

variable "NOTION_PAGE_ID" {
  description = "Primary Notion page ID for documentation sync"
  type        = string
}

variable "NOTION_PR_BACKLOG_DB_ID" {
  description = "Notion database ID for PR Backlog"
  type        = string
}

variable "NOTION_PROJECT_BOARD_BACKLOG_DB_ID" {
  description = "Notion database ID for Project Board Backlog"
  type        = string
}

variable "NOTION_TASK_BACKLOG_DB_ID" {
  description = "Notion database ID for Task Backlog"
  type        = string
}

variable "NOTION_TOKEN" {
  description = "Sensitive Notion integration token"
  type        = string
}

variable "TFC_TOKEN" {
  description = "Sensitive Terraform Cloud access token for sync operations"
  type        = string
}
