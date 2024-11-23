"""
Key Objectives for `diff_communicator.py` script:
1. Format generated differences from git operations into a readable markdown format.
2. Implement communication functionality to post formatted differences to the designated Discussion Board.
3. Create utility functions for handling API calls to the Discussion Board.
4. Ensure data validation and error handling for communication operations.
5. Include logging for debug and traceability purposes.
"""

import requests
import logging

class DiffCommunicator:
    def __init__(self, api_url, api_token):
        self.api_url = api_url
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def format_diff_to_markdown(self, diff):
        """Formats the git diff into a markdown-friendly format."""
        try:
            markdown_diff = "```diff\n" + diff + "\n```"
            logging.debug("Formatted diff to markdown.")
            return markdown_diff
        except Exception as e:
            logging.error(f"Error formatting diff: {e}")
            raise

    def post_to_discussion_board(self, title, content):
        """Posts the formatted diff to the discussion board."""
        try:
            payload = {
                "title": title,
                "content": content
            }
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            logging.info(f"Posted to discussion board: {title}")
            return response.json()
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request exception: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def validate_data(self, data):
        """Validates the data before posting."""
        if not data.get("title") or not data.get("content"):
            logging.error("Validation failed: Title and content are required.")
            raise ValueError("Title and content are required.")
        logging.debug("Data validation passed.")

# Example usage
if __name__ == "__main__":
    diff_communicator = DiffCommunicator(api_url="https://api.example.com/discussions", api_token="your_api_token")
    diff = "Example diff content"
    markdown_diff = diff_communicator.format_diff_to_markdown(diff)
    diff_communicator.validate_data({"title": "Example Diff", "content": markdown_diff})
    diff_communicator.post_to_discussion_board("Example Diff", markdown_diff)