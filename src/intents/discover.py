"""Discover intents from data"""

from typing import List, Dict, Set
from collections import Counter


def extract_intents(messages: List[str]) -> List[str]:
    """
    Extract intents from messages using keyword-based approach.
    
    Args:
        messages: List of message texts
        
    Returns:
        List of discovered intents
    """
    intent_keywords = {
        'support': ['help', 'issue', 'problem', 'error', 'fix'],
        'sales': ['buy', 'price', 'upgrade', 'plan', 'cost'],
        'billing': ['invoice', 'payment', 'charge', 'refund'],
        'feature_request': ['feature', 'add', 'implement', 'build'],
        'general': ['hello', 'hi', 'thanks', 'ok']
    }
    
    discovered_intents = []
    for message in messages:
        message_lower = message.lower()
        for intent, keywords in intent_keywords.items():
            if any(kw in message_lower for kw in keywords):
                discovered_intents.append(intent)
                break
    
    return discovered_intents


def get_intent_distribution(intents: List[str]) -> Dict[str, int]:
    """
    Get distribution of intents.
    
    Args:
        intents: List of intents
        
    Returns:
        Dictionary with intent counts
    """
    return dict(Counter(intents))
