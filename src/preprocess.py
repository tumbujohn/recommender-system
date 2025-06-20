# src/preprocess.py
"""
Data preprocessing functions for the recommender system.
"""
import pandas as pd
from pandas import DataFrame

def clean_data(df: DataFrame) -> DataFrame:
    """Clean and preprocess the input DataFrame."""
    # Drop duplicates
    df = df.drop_duplicates()
    # Handle missing values (simple example: drop rows)
    df = df.dropna()
    return df

def normalize_ratings(df: DataFrame, rating_col: str = 'rating') -> DataFrame:
    """Normalize ratings to 0-1 scale."""
    if rating_col in df.columns:
        min_rating = df[rating_col].min()
        max_rating = df[rating_col].max()
        if max_rating != min_rating:
            df[rating_col] = (df[rating_col] - min_rating) / (max_rating - min_rating)
        else:
            df[rating_col] = 0.0
    return df
