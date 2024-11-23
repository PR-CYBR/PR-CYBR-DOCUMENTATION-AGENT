"""
Key Objectives for `git_operations.py` script: 
 
1. Implement functionality to clone remote repositories using `git clone`.
2. Develop a method to fetch and compare the differences between specified commits.
3. Create utility functions for handling git commands and output parsing.
4. Ensure error handling for common Git operations (e.g., repository not found, authentication issues).
5. Include documentation to explain usage and examples for end users.
"""

import subprocess
import os

class GitOperations:
    def __init__(self, repo_url=None, local_path=None):
        self.repo_url = repo_url
        self.local_path = local_path or os.path.basename(repo_url)

    def clone_repository(self):
        """Clones a remote repository to the local path."""
        try:
            if not self.repo_url:
                raise ValueError("Repository URL must be provided.")
            subprocess.run(["git", "clone", self.repo_url, self.local_path], check=True)
            print(f"Repository cloned to {self.local_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def fetch_commit_diff(self, commit1, commit2):
        """Fetches and returns the differences between two commits."""
        try:
            if not os.path.exists(self.local_path):
                raise FileNotFoundError(f"Local path {self.local_path} does not exist.")
            os.chdir(self.local_path)
            result = subprocess.run(
                ["git", "diff", commit1, commit2],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error fetching commit diff: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            os.chdir("..")  # Ensure we return to the original directory

    def execute_git_command(self, command):
        """Executes a generic git command and returns the output."""
        try:
            result = subprocess.run(
                ["git"] + command.split(),
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing git command '{command}': {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    git_ops = GitOperations(repo_url="https://github.com/example/repo.git")
    git_ops.clone_repository()
    diff = git_ops.fetch_commit_diff("commit1_hash", "commit2_hash")
    print(diff)