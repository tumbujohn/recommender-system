import pandas as pd
import os

def load_movielens(path: str) -> pd.DataFrame:
    """Load MovieLens ratings data from a CSV file."""
    return pd.read_csv(path)  # type: ignore

def load_ratings(path: str | None = None) -> pd.DataFrame:
    """Load ratings data from a CSV file. Defaults to ../data/ratings.csv."""
    if path is None:
        path = os.path.join(os.path.dirname(__file__), '../data/ratings.csv')
    return pd.read_csv(path)  # type: ignore
