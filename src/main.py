# src/main.py
"""
Main script to run the recommender system pipeline.
"""
import pandas as pd
from src import data_loader, preprocess, models, evaluation

def main() -> None:
    # Load data
    ratings = data_loader.load_ratings()
    # Preprocess data
    ratings = preprocess.clean_data(ratings)
    ratings = preprocess.normalize_ratings(ratings)
    # Train model (example: user-based CF)
    model = models.UserBasedCF(ratings)
    model.fit()
    # Example: recommend for user_id=1
    recommendations = model.recommend(user_id=1, top_n=5)
    print(f"Recommendations for user 1: {recommendations}")

if __name__ == "__main__":
    main()
