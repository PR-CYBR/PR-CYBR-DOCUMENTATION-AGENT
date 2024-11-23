"""
Key Objectives:
1. Update the main execution flow to integrate the new functionalities provided by the new scripts.
2. Ensure command-line arguments and input methods accept new parameters related to git operations and issue analysis.
3. Revise the user interface prompts to include options for the new features.
4. Maintain compatibility with existing functionalities while ensuring seamless integration of new features.
5. Provide informative output messages upon execution to enhance user experience.
"""

import argparse
from agent_logic.core_functions import AgentCore

def main():
    parser = argparse.ArgumentParser(description="PR-CYBR Documentation Agent")
    parser.add_argument('--repo-url', type=str, help='URL of the repository to clone')
    parser.add_argument('--commit1', type=str, help='First commit hash for diff comparison')
    parser.add_argument('--commit2', type=str, help='Second commit hash for diff comparison')
    parser.add_argument('--repo-owner', type=str, help='Owner of the repository for issue analysis')
    parser.add_argument('--repo-name', type=str, help='Name of the repository for issue analysis')
    parser.add_argument('--api-token', type=str, help='API token for accessing GitHub')
    args = parser.parse_args()

    agent = AgentCore()

    if args.repo_url:
        agent.git_operations.repo_url = args.repo_url
        agent.git_operations.clone_repository()

    if args.commit1 and args.commit2:
        diff = agent.git_operations.fetch_commit_diff(args.commit1, args.commit2)
        print("Commit Diff:\n", diff)

    if args.repo_owner and args.repo_name and args.api_token:
        agent.issue_analyzer.repo_owner = args.repo_owner
        agent.issue_analyzer.repo_name = args.repo_name
        agent.issue_analyzer.api_token = args.api_token
        issues = agent.issue_analyzer.fetch_open_issues()
        if issues:
            analysis = agent.issue_analyzer.analyze_issues(issues)
            report = agent.issue_analyzer.create_report(analysis)
            print("Issue Analysis Report:\n", report)

if __name__ == "__main__":
    main()