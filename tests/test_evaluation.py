# tests/test_evaluation.py
import numpy as np
from src import evaluation

def test_rmse():
    y_true = [3, 4, 5]
    y_pred = [2.5, 4.5, 5]
    assert np.isclose(evaluation.rmse(y_true, y_pred), 0.408, atol=0.01)

def test_precision_at_k():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 1]
    assert 0 <= evaluation.precision_at_k(y_true, y_pred, k=3) <= 1

def test_recall_at_k():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 1]
    assert 0 <= evaluation.recall_at_k(y_true, y_pred, k=3) <= 1

def test_f1_at_k():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 1]
    assert 0 <= evaluation.f1_at_k(y_true, y_pred, k=3) <= 1
