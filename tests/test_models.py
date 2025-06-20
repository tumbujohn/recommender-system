# tests/test_models.py
import pandas as pd
from src import models

def test_user_based_cf():
    ratings = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3, 3],
        'item_id': [1, 2, 2, 3, 1, 3],
        'rating': [5, 3, 4, 2, 1, 5]
    })
    model = models.UserBasedCF(ratings)
    model.fit()
    recs = model.recommend(user_id=1, top_n=2)
    assert isinstance(recs, list)
    assert len(recs) == 2

def test_item_based_cf():
    ratings = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3, 3],
        'item_id': [1, 2, 2, 3, 1, 3],
        'rating': [5, 3, 4, 2, 1, 5]
    })
    model = models.ItemBasedCF(ratings)
    model.fit()
    recs = model.recommend(user_id=1, top_n=2)
    assert isinstance(recs, list)
    assert len(recs) == 2
