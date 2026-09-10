"""Judge the quality of generated replies"""

from typing import Dict


class ReplyJudge:
    """Evaluates quality of generated replies"""
    
    def __init__(self):
        """
        Initialize reply judge.
        """
        self.criteria = {
            'relevance': 0.3,
            'completeness': 0.3,
            'clarity': 0.2,
            'tone': 0.2
        }
    
    def judge(self, query: str, reply: str, reference: str = None) -> Dict:
        """
        Judge a reply.
        
        Args:
            query: Original query
            reply: Generated reply
            reference: Reference/gold standard reply
            
        Returns:
            Dictionary with scores and feedback
        """
        scores = {
            'relevance': self._score_relevance(query, reply),
            'completeness': self._score_completeness(reply),
            'clarity': self._score_clarity(reply),
            'tone': self._score_tone(reply)
        }
        
        overall_score = sum(
            scores[k] * self.criteria[k] for k in scores
        )
        
        return {
            'scores': scores,
            'overall': overall_score
        }
    
    def _score_relevance(self, query: str, reply: str) -> float:
        """Score reply relevance to query"""
        return 0.7
    
    def _score_completeness(self, reply: str) -> float:
        """Score reply completeness"""
        return 0.8
    
    def _score_clarity(self, reply: str) -> float:
        """Score reply clarity"""
        return 0.75
    
    def _score_tone(self, reply: str) -> float:
        """Score reply tone"""
        return 0.8
