"""
Key Objectives for `opord_analysis.py` script:
1. Parse new OPORD documents to extract relevant information for analysis.
2. Summarize actionable tasks and assignments based on the OPORD content.
3. Create a user-friendly templating system for briefing posts derived from OPORD analysis.
4. Implement documentation of the OPORD analysis process for user understanding.
5. Ensure integration with existing documentation and communication systems.
"""

import logging
import re

class OpordAnalysis:
    def __init__(self, opord_path):
        self.opord_path = opord_path
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def parse_opord(self):
        """Parses the OPORD document to extract relevant information."""
        try:
            with open(self.opord_path, 'r') as file:
                content = file.read()
            logging.info("OPORD document parsed successfully.")
            return content
        except FileNotFoundError:
            logging.error(f"OPORD file not found: {self.opord_path}")
        except Exception as e:
            logging.error(f"Error parsing OPORD: {e}")

    def summarize_tasks(self, content):
        """Summarizes actionable tasks and assignments from the OPORD content."""
        try:
            tasks = re.findall(r"## Task Organization:(.*?)##", content, re.DOTALL)
            tasks_summary = tasks[0].strip() if tasks else "No tasks found."
            logging.debug("Tasks summarized from OPORD content.")
            return tasks_summary
        except Exception as e:
            logging.error(f"Error summarizing tasks: {e}")

    def create_briefing_template(self, tasks_summary):
        """Creates a user-friendly template for briefing posts."""
        try:
            template = f"### OPORD Briefing\n\n**Tasks and Assignments:**\n\n{tasks_summary}\n"
            logging.info("Briefing template created.")
            return template
        except Exception as e:
            logging.error(f"Error creating briefing template: {e}")

    def document_analysis_process(self):
        """Documents the OPORD analysis process for user understanding."""
        try:
            documentation = (
                "### OPORD Analysis Process\n\n"
                "1. **Parse OPORD**: Extracts content from the OPORD document.\n"
                "2. **Summarize Tasks**: Identifies and summarizes actionable tasks.\n"
                "3. **Create Briefing Template**: Formats the summary into a briefing template.\n"
            )
            logging.info("OPORD analysis process documented.")
            return documentation
        except Exception as e:
            logging.error(f"Error documenting analysis process: {e}")

# Example usage
if __name__ == "__main__":
    opord_analysis = OpordAnalysis(opord_path="docs/OPORD/OPORD-PR-CYBR-DOC-10.md")
    content = opord_analysis.parse_opord()
    if content:
        tasks_summary = opord_analysis.summarize_tasks(content)
        briefing_template = opord_analysis.create_briefing_template(tasks_summary)
        print(briefing_template)
        documentation = opord_analysis.document_analysis_process()
        print(documentation)