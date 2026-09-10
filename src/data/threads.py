"""Handle conversation threads"""

from typing import List, Dict


class Thread:
    """Represents a conversation thread"""
    
    def __init__(self, thread_id: str, messages: List[Dict] = None):
        """
        Initialize a thread.
        
        Args:
            thread_id: Unique thread identifier
            messages: List of messages in the thread
        """
        self.thread_id = thread_id
        self.messages = messages or []
    
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to the thread.
        
        Args:
            role: Role of the sender (user/assistant)
            content: Message content
        """
        self.messages.append({
            'role': role,
            'content': content
        })
    
    def get_context(self) -> str:
        """
        Get full thread context.
        
        Returns:
            Formatted thread context
        """
        context = []
        for msg in self.messages:
            context.append(f"{msg['role'].upper()}: {msg['content']}")
        return "\n".join(context)
