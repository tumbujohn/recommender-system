# Data Source:
# This project uses the MovieLens dataset, which can be downloaded from:
# https://grouplens.org/datasets/movielens/latest/
# MovieLens is a widely used public dataset for recommender system research, provided by GroupLens Research.

# src/models.py
"""
Collaborative filtering models for the recommender system.
"""
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.metrics.pairwise import cosine_similarity
from typing import Optional

class UserBasedCF:
    def __init__(self, ratings: DataFrame):
        self.ratings = ratings
        self.user_similarity: Optional[np.ndarray] = None
        self.user_item_matrix: Optional[DataFrame] = None

    def fit(self) -> None:
        user_item_matrix = self.ratings.pivot(index='user_id', columns='item_id', values='rating').fillna(0)
        self.user_similarity = cosine_similarity(user_item_matrix)
        self.user_item_matrix = user_item_matrix

    def recommend(self, user_id: int, top_n: int = 5) -> list:
        if self.user_similarity is None or self.user_item_matrix is None:
            self.fit()
        user_idx = self.user_item_matrix.index.get_loc(user_id)
        sim_scores = self.user_similarity[user_idx]
        scores = np.dot(sim_scores, self.user_item_matrix.values)
        scores = scores / (sim_scores.sum() + 1e-8)
        user_rated = self.user_item_matrix.loc[user_id] > 0
        scores[user_rated.values] = -np.inf
        top_items = np.argsort(scores)[-top_n:][::-1]
        return self.user_item_matrix.columns[top_items].tolist()

class ItemBasedCF:
    def __init__(self, ratings: DataFrame):
        self.ratings = ratings
        self.item_similarity: Optional[np.ndarray] = None
        self.item_user_matrix: Optional[DataFrame] = None

    def fit(self) -> None:
        item_user_matrix = self.ratings.pivot(index='item_id', columns='user_id', values='rating').fillna(0)
        self.item_similarity = cosine_similarity(item_user_matrix)
        self.item_user_matrix = item_user_matrix

    def recommend(self, user_id: int, top_n: int = 5) -> list:
        if self.item_similarity is None or self.item_user_matrix is None:
            self.fit()
        user_ratings = self.item_user_matrix.loc[:, user_id]
        scores = np.dot(self.item_similarity, user_ratings)
        user_rated = user_ratings > 0
        scores[user_rated.values] = -np.inf
        top_items = np.argsort(scores)[-top_n:][::-1]
        return self.item_user_matrix.index[top_items].tolist()
