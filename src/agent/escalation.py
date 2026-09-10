"""Escalation logic for complex queries"""

from typing import Dict, List


class EscalationManager:
    """Manages escalation of complex queries"""
    
    def __init__(self):
        """
        Initialize escalation manager.
        """
        self.escalation_rules = []
    
    def should_escalate(self, message: str, intent: str, confidence: float) -> bool:
        """
        Determine if a message should be escalated.
        
        Args:
            message: The message text
            intent: The classified intent
            confidence: Confidence score of the classification
            
        Returns:
            Boolean indicating if escalation is needed
        """
        # Low confidence should be escalated
        if confidence < 0.5:
            return True
        
        # Complex intents might need escalation
        complex_intents = ['billing', 'legal', 'complaint']
        if intent in complex_intents:
            return True
        
        return False
