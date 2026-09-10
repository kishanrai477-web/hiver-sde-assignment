"""Generate evaluation reports"""

from typing import Dict, List
import json


class ReportGenerator:
    """Generates evaluation reports"""
    
    def __init__(self, output_path: str = "report/report.md"):
        """
        Initialize report generator.
        
        Args:
            output_path: Path to save the report
        """
        self.output_path = output_path
        self.results = {}
    
    def add_results(self, section: str, data: Dict) -> None:
        """
        Add results to report.
        
        Args:
            section: Section name
            data: Results data
        """
        self.results[section] = data
    
    def generate(self) -> str:
        """
        Generate the report.
        
        Returns:
            Markdown report string
        """
        lines = ["# Evaluation Report\n"]
        
        for section, data in self.results.items():
            lines.append(f"## {section}\n")
            lines.append(json.dumps(data, indent=2))
            lines.append("\n")
        
        return "".join(lines)
