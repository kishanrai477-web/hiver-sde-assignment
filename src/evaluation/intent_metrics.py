"""Intent classification metrics"""

from typing import List
from sklearn.metrics import precision_recall_fscore_support, accuracy_score, confusion_matrix


def calculate_metrics(y_true: List[str], y_pred: List[str]) -> dict:
    """
    Calculate classification metrics.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        
    Returns:
        Dictionary of metrics
    """
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true, y_pred, average='weighted'
    )
    accuracy = accuracy_score(y_true, y_pred)
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }
