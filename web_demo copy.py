# This demo uses a switcher to change from user-based CF to item-based CF, allowing users to see recommendations based on different collaborative filtering methods. 
# This code is structured to load data, compute user and item similarity matrices, and provide recommendations based on the selected method.

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

@st.cache_data
def compute_item_similarity(user_item_matrix):
    item_item_matrix = user_item_matrix.T
    item_norms = np.linalg.norm(item_item_matrix.values, axis=1, keepdims=True)
    item_item_normalized = item_item_matrix.values / (item_norms + 1e-8)
    item_similarity = np.dot(item_item_normalized, item_item_normalized.T)
    return pd.DataFrame(item_similarity, index=item_item_matrix.index, columns=item_item_matrix.index)

# Load and cache data and matrices
ratings, movies = load_data()
user_item_matrix = compute_user_item_matrix(ratings)
user_similarity_df = compute_user_similarity(user_item_matrix)
item_similarity_df = compute_item_similarity(user_item_matrix)

st.title("MovieLens Recommender Demo")

user_ids = ratings['userId'].unique()
user_id = st.selectbox("Select a user ID", user_ids)

# Show user's past ratings
st.subheader("User's Past Ratings")
user_history = ratings[ratings['userId'] == user_id].merge(movies, on='movieId')[['title', 'rating']]
st.dataframe(user_history)

# Recommendation method selection
method = st.radio("Select recommendation method", ("User-Based CF", "Item-Based CF"))

if method == "User-Based CF":
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
else:
    # Item-based collaborative filtering
    user_ratings = ratings[ratings['userId'] == user_id][['movieId', 'rating']]
    scores = {}
    for _, row in user_ratings.iterrows():
        movie_id = row['movieId']
        rating = row['rating']
        similar_scores = item_similarity_df[movie_id] * rating
        for sim_movie_id, score in similar_scores.items():
            if sim_movie_id not in user_ratings['movieId'].values:
                scores[sim_movie_id] = scores.get(sim_movie_id, 0) + score
    rec_list = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
    rec_df = pd.DataFrame(rec_list, columns=['movieId', 'score'])
    rec_df = rec_df.merge(movies, on='movieId', how='left')
    st.subheader("Recommended Movies (Item-Based CF)")
    st.dataframe(rec_df[['title', 'score']])
