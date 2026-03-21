# End-to-End-Book-Recommender-System
    This project is an end-to-end Machine Learning based Book Recommender System that suggests similar books using a K-Nearest Neighbors(KNN) model based on user ratings-USING COLLABORATIVE FILTERING METHOD

    The system is built with a modular pipeline architecture and deployed using Streamlit cloud

# APP LINK

#  Features

-  Book recommendation based on similar taste users
-  Search and select books easily
-  KNN-based recommendation engine
-  Cosine similarity for accurate matching
-  Interactive UI using Streamlit
-  Modular ML pipeline (ingestion → transformation → training)

# Project Structure

├── app.py
├── config.yaml
├── requirements.txt
├── books_recommender/
│   ├── components/
│   ├── pipeline/
│   ├── utils/
│   ├── config/
│   ├── entity/
│   ├── logger/
│   └── exception/

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- YAML (for configuration)

# Model Details

- Algorithm: K-Nearest Neighbors (KNN)
- Similarity Metric: Cosine Similarity
- Approach: Collaborative Filtering
- Input: User-book rating matrix
- Output: Top similar books

# Pipeline Overview

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Recommendation Generation

# WORKFLOW
UPDATE modules in this order
- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py
