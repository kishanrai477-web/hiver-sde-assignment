"""Prompt templates for the agent"""

from typing import Dict


class PromptTemplate:
    """Manages prompt templates"""
    
    def __init__(self):
        """
        Initialize prompt templates.
        """
        self.templates = {}
    
    def add_template(self, name: str, template: str) -> None:
        """
        Add a prompt template.
        
        Args:
            name: Template name
            template: Template string with placeholders
        """
        self.templates[name] = template
    
    def format(self, name: str, **kwargs) -> str:
        """
        Format a template with provided values.
        
        Args:
            name: Template name
            **kwargs: Values to fill placeholders
            
        Returns:
            Formatted prompt
        """
        template = self.templates.get(name, "")
        return template.format(**kwargs)


# Default prompts
DEFAULT_SYSTEM_PROMPT = """You are a helpful customer support assistant. 
Your goal is to provide accurate, helpful, and professional responses to customer inquiries.
"""

DEFAULT_USER_PROMPT = """Please respond to the following customer inquiry:

{query}

Provide a helpful and professional response.
"""
