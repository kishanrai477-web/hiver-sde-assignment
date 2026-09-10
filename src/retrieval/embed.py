"""Embedding generation module"""

from typing import List
import numpy as np


class EmbeddingModel:
    """Generates embeddings for texts"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Initialize embedding model.
        
        Args:
            model_name: Name of the embedding model
        """
        self.model_name = model_name
        self.model = None
    
    def embed(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for texts.
        
        Args:
            texts: List of texts to embed
            
        Returns:
            Array of embeddings
        """
        # Embedding logic here
        pass
    
    def embed_single(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector
        """
        return self.embed([text])[0]
