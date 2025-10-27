#############################################
# PR-CYBR Agent Terraform Entry Point
#
# This file configures baseline Terraform
# settings and exposes a normalized view of
# all workspace variables. Actual secrets are
# supplied by Terraform Cloud; nothing here
# should embed credentials directly.
#############################################

terraform {
  required_version = ">= 1.6.0"
}

locals {
  workspace = {
    agent_id       = var.AGENT_ID
    notion_page_id = var.NOTION_PAGE_ID

    docker = {
      registry_user = var.PR_CYBR_DOCKER_USER
      registry_pass = var.PR_CYBR_DOCKER_PASS
      hub_user      = var.DOCKERHUB_USERNAME
      hub_token     = var.DOCKERHUB_TOKEN
    }

    domain = var.GLOBAL_DOMAIN

    automation = {
      agent_actions = var.AGENT_ACTIONS
      notion_token  = var.NOTION_TOKEN
      tfc_token     = var.TFC_TOKEN
    }

    notion_databases = {
      discussions_arc       = var.NOTION_DISCUSSIONS_ARC_DB_ID
      issues_backlog        = var.NOTION_ISSUES_BACKLOG_DB_ID
      knowledge_file        = var.NOTION_KNOWLEDGE_FILE_DB_ID
      project_board_backlog = var.NOTION_PROJECT_BOARD_BACKLOG_DB_ID
      pr_backlog            = var.NOTION_PR_BACKLOG_DB_ID
      task_backlog          = var.NOTION_TASK_BACKLOG_DB_ID
    }
  }
}

output "workspace_configuration" {
  value      = local.workspace
  sensitive  = true
  depends_on = []
}
