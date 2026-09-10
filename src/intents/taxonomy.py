"""Intent taxonomy management"""

from typing import Dict, List


class IntentTaxonomy:
    """Manages intent taxonomy and hierarchies"""
    
    def __init__(self):
        """
        Initialize taxonomy.
        """
        self.intents = {}
        self.hierarchy = {}
    
    def add_intent(self, intent_id: str, name: str, description: str) -> None:
        """
        Add intent to taxonomy.
        
        Args:
            intent_id: Unique intent identifier
            name: Intent name
            description: Intent description
        """
        self.intents[intent_id] = {
            'name': name,
            'description': description
        }
    
    def get_intent(self, intent_id: str) -> Dict:
        """
        Get intent details.
        
        Args:
            intent_id: Intent identifier
            
        Returns:
            Intent details dictionary
        """
        return self.intents.get(intent_id, {})
