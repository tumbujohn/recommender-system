# Collaborative Filtering Methods and Output Properties

This document explains the two collaborative filtering (CF) methods implemented in the project web demo, and details the meaning of the output properties for each method.

---

## 1. User-Based Collaborative Filtering (User-Based CF)

**How it works:**
- Finds users who are similar to the target user (using cosine similarity of their rating vectors).
- Recommends movies that similar users have rated highly, but the target user has not seen.

**Output property:**
- `predicted_rating`: This is an estimated score for each recommended movie, calculated as the average of ratings given to that movie by similar users. A higher value means the system predicts the user will like the movie more.

---

## 2. Item-Based Collaborative Filtering (Item-Based CF)

**How it works:**
- Finds movies similar to those the user has already rated (using cosine similarity between movie rating vectors).
- For each candidate movie, computes a score by summing the similarities to all movies the user has rated, weighted by the user's ratings.

**Output property:**
- `score`: This value represents how similar a candidate movie is to the movies the user has already rated, weighted by how much the user liked them. A higher score means the movie is more similar to the user's favorites and is more likely to be a good recommendation.
- (Optionally, this score can be normalized by dividing by the sum of similarities for a more interpretable value, but ranking by score is common.)

---

## Summary Table
| Method      | Output Property     | Meaning                                                                 |
|-------------|---------------------|------------------------------------------------------------------------|
| User-Based  | predicted_rating    | Estimated rating for the user, based on similar users' ratings          |
| Item-Based  | score               | Weighted similarity to user's rated movies, higher = more recommended   |

---

Refer to this document when interpreting the results of your recommender system web demo or when explaining your project to others.


## Performance Issues
I discovered the recommendation display by streamlite in the browser is slow for iterm based filtering but should not in theory; So i researched and figured out that my dataset in /data/ folder has more iterms than users, but in reality, it is expected that iterms grow at a much more slower rate than users
------ 
In terms of performance (speed and scalability), item-based collaborative filtering is generally better than user-based collaborative filtering, especially for large datasets. Here’s why:

Item-Based Collaborative Filtering
Faster at prediction time: Item similarities can be precomputed and cached, so generating recommendations for a user only requires looking up a small set of similar items.
Scales better: The number of items is usually much smaller and more stable than the number of users, making the similarity matrix smaller and more manageable.
More stable: User preferences change more frequently than item properties, so item-based models are less sensitive to new users or user churn.
User-Based Collaborative Filtering
Slower at prediction time: Requires finding similar users for each recommendation, which can be computationally expensive as the number of users grows.
Less scalable: The user-user similarity matrix can become very large and expensive to update as new users join.
More sensitive to user activity: Recommendations can change rapidly as users rate new items.
Summary:

For most real-world applications, item-based CF is preferred for performance and scalability.
User-based CF can be useful for small datasets or when user similarity is especially important, but it is less efficient for large-scale systems.