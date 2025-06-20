import streamlit as st
import pandas as pd
import numpy as np
import collections

@st.cache_data
def load_data():
    ratings = pd.read_csv('data/ratings.csv')
    movies = pd.read_csv('data/movies.csv')
    return ratings, movies

@st.cache_data
def compute_user_item_matrix(ratings):
    return ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

@st.cache_data
def compute_user_similarity(user_item_matrix):
    user_norms = np.linalg.norm(user_item_matrix.values, axis=1, keepdims=True)
    user_item_normalized = user_item_matrix.values / (user_norms + 1e-8)
    user_similarity = np.dot(user_item_normalized, user_item_normalized.T)
    return pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Load and cache data and matrices
ratings, movies = load_data()
user_item_matrix = compute_user_item_matrix(ratings)
user_similarity_df = compute_user_similarity(user_item_matrix)

st.title("MovieLens Recommender Demo: User-Based CF")

user_ids = ratings['userId'].unique()
user_id = st.selectbox("Select a user ID", user_ids)

# Show user's past ratings
st.subheader("User's Past Ratings")
user_history = ratings[ratings['userId'] == user_id].merge(movies, on='movieId')[['title', 'rating']]
st.dataframe(user_history)

# User-based collaborative filtering
similar_users = user_similarity_df[user_id].drop(user_id).sort_values(ascending=False)
user_movies = set(ratings[ratings['userId'] == user_id]['movieId'])
recommendations = []
for neighbor in similar_users.index:
    neighbor_movies = ratings[ratings['userId'] == neighbor][['movieId', 'rating']]
    for _, row in neighbor_movies.iterrows():
        if row['movieId'] not in user_movies:
            recommendations.append((row['movieId'], row['rating']))
    if len(recommendations) > 100:
        break
rec_counter = collections.defaultdict(list)
for movie_id, rating in recommendations:
    rec_counter[movie_id].append(rating)
rec_list = [(movie_id, np.mean(ratings)) for movie_id, ratings in rec_counter.items()]
rec_list = sorted(rec_list, key=lambda x: x[1], reverse=True)[:5]
rec_df = pd.DataFrame(rec_list, columns=['movieId', 'predicted_rating'])
rec_df = rec_df.merge(movies, on='movieId', how='left')
st.subheader("Recommended Movies (User-Based CF)")
st.dataframe(rec_df[['title', 'predicted_rating']])
