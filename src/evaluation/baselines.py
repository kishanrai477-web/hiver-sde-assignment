"""Baseline models for comparison"""

from typing import List, Dict


class BaselineModel:
    """Base class for baseline models"""
    
    def predict(self, query: str) -> str:
        """
        Generate prediction.
        
        Args:
            query: Input query
            
        Returns:
            Predicted response
        """
        raise NotImplementedError


class SimpleBaseline(BaselineModel):
    """Simple rule-based baseline"""
    
    def predict(self, query: str) -> str:
        """
        Generate response based on simple rules.
        
        Args:
            query: Input query
            
        Returns:
            Response
        """
        query_lower = query.lower()
        
        if 'hello' in query_lower or 'hi' in query_lower:
            return "Hello! How can I help you today?"
        elif 'help' in query_lower:
            return "I'm here to help. What do you need assistance with?"
        else:
            return "Thank you for your message. I'm processing your request."
