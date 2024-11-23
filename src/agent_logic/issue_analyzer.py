"""
Key Objectives for `issue_analyzer.py` script:
1. Implement functionality to fetch open issues from specified repositories.
2. Analyze issues for trends, commonalities, and potential solutions.
3. Create reports summarizing findings and propose actionable solutions based on results.
4. Develop a mechanism to present analyses in a clear and concise manner for team discussions.
5. Include unit tests to ensure the reliability of the analysis functions.
"""

import requests
import logging

class IssueAnalyzer:
    def __init__(self, repo_owner, repo_name, api_token):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.api_token = api_token
        self.api_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def fetch_open_issues(self):
        """Fetches open issues from the specified repository."""
        try:
            response = requests.get(self.api_url, headers=self.headers, params={"state": "open"})
            response.raise_for_status()
            issues = response.json()
            logging.info(f"Fetched {len(issues)} open issues.")
            return issues
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request exception: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def analyze_issues(self, issues):
        """Analyzes issues for trends and commonalities."""
        try:
            analysis = {
                "total_issues": len(issues),
                "labels": {},
                "assignees": {}
            }
            for issue in issues:
                for label in issue.get("labels", []):
                    label_name = label["name"]
                    analysis["labels"][label_name] = analysis["labels"].get(label_name, 0) + 1
                for assignee in issue.get("assignees", []):
                    assignee_login = assignee["login"]
                    analysis["assignees"][assignee_login] = analysis["assignees"].get(assignee_login, 0) + 1
            logging.debug("Issues analyzed for trends and commonalities.")
            return analysis
        except Exception as e:
            logging.error(f"Error analyzing issues: {e}")

    def create_report(self, analysis):
        """Creates a report summarizing the analysis."""
        try:
            report = f"Total Issues: {analysis['total_issues']}\n"
            report += "Labels:\n"
            for label, count in analysis["labels"].items():
                report += f"  - {label}: {count}\n"
            report += "Assignees:\n"
            for assignee, count in analysis["assignees"].items():
                report += f"  - {assignee}: {count}\n"
            logging.info("Report created summarizing the analysis.")
            return report
        except Exception as e:
            logging.error(f"Error creating report: {e}")

# Example usage
if __name__ == "__main__":
    issue_analyzer = IssueAnalyzer(repo_owner="example", repo_name="repo", api_token="your_api_token")
    issues = issue_analyzer.fetch_open_issues()
    if issues:
        analysis = issue_analyzer.analyze_issues(issues)
        report = issue_analyzer.create_report(analysis)
        print(report)