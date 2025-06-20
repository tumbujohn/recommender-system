# Project Requirements Explained

This document explains each dependency in `requirements.txt`, its purpose, and where it is used in the project.

---

## Core Data Science Libraries

- **numpy**: Fundamental package for numerical computations in Python. Used for matrix operations, similarity calculations, and general data manipulation.
- **pandas**: Essential for data loading, cleaning, and manipulation. Used throughout the project for handling CSV files and DataFrames.

## Visualization

- **matplotlib**: Standard plotting library for Python. Used for creating static visualizations in notebooks (e.g., rating distributions).
- **seaborn**: Built on top of matplotlib, provides advanced statistical visualizations and prettier plots. Used for EDA and data exploration.

## Machine Learning & Recommender System

- **scikit-learn**: Provides machine learning utilities, including metrics and (optionally) cosine similarity for collaborative filtering. Used in both notebook and scripts for similarity calculations and train/test splitting.
- **scipy**: Scientific computing library, sometimes required by scikit-learn and for advanced mathematical operations.
- **scikit-surprise**: Specialized library for building and evaluating recommender systems. Useful for advanced collaborative filtering models (not required for the basic workflow, but included for experimentation).

## Interactive & Notebook Environment

- **jupyter**: Required to run and edit Jupyter notebooks for EDA, prototyping, and demonstration.
- **streamlit**: Used to build a simple web demo for the recommender system, allowing interactive user selection and recommendation display.

## Testing

- **pytest**: Framework for writing and running unit tests to ensure code correctness and reliability.

---

## Where to Find More Information
- Official documentation for each package can be found on [PyPI](https://pypi.org/) or the respective project websites.
- For installation, use: `pip install -r requirements.txt`

---

This file is located in the `.docs` folder for easy reference by developers and reviewers.
