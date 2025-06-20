# tests/test_preprocess.py
import pandas as pd
from src import preprocess

def test_clean_data():
    df = pd.DataFrame({'a': [1, 1, None], 'b': [2, 2, 3]})
    cleaned = preprocess.clean_data(df)
    assert cleaned.isnull().sum().sum() == 0
    assert cleaned.duplicated().sum() == 0

def test_normalize_ratings():
    df = pd.DataFrame({'rating': [1, 2, 3, 4, 5]})
    normed = preprocess.normalize_ratings(df.copy())
    assert normed['rating'].min() == 0
    assert normed['rating'].max() == 1
