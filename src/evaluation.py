# src/evaluation.py
"""
Evaluation metrics for recommender system models.
"""
import numpy as np
from typing import Sequence
from sklearn.metrics import mean_squared_error, precision_score, recall_score, f1_score

def rmse(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))

def precision_at_k(y_true: Sequence[int], y_pred: Sequence[int], k: int = 5) -> float:
    y_true = np.array(y_true)[:k]
    y_pred = np.array(y_pred)[:k]
    return float(precision_score(y_true, y_pred, average='binary', zero_division=0))

def recall_at_k(y_true: Sequence[int], y_pred: Sequence[int], k: int = 5) -> float:
    y_true = np.array(y_true)[:k]
    y_pred = np.array(y_pred)[:k]
    return float(recall_score(y_true, y_pred, average='binary', zero_division=0))

def f1_at_k(y_true: Sequence[int], y_pred: Sequence[int], k: int = 5) -> float:
    y_true = np.array(y_true)[:k]
    y_pred = np.array(y_pred)[:k]
    return float(f1_score(y_true, y_pred, average='binary', zero_division=0))
