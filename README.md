# End-to-End-Book-Recommender-System

    This project is an end-to-end Machine Learning based Book Recommender System that suggests books to users who has similar tastes using a K-Nearest Neighbors (KNN) model based on user ratings.

    The system is built with a modular pipeline architecture and deployed using Streamlit Cloud.

# 🚀 Live Demo

🔗 https://keerthana893-end-to-end-book-recommender-system-app-qrecor.streamlit.app/

# 📌 Features

- 📖 Book recommendation based on similarity
- 🔍 Search and select books easily
- 🤖 KNN-based recommendation engine
- 🧠 Cosine similarity for accurate matching
- 🌐 Interactive UI using Streamlit
- ⚙️ Modular ML pipeline (ingestion → transformation → training)

# 🏗️ Project Structure

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

# ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- YAML (for configuration)

# 🧠 Model Details

- Algorithm: K-Nearest Neighbors (KNN)
- Similarity Metric: Cosine Similarity
- Approach: Collaborative Filtering
- Input: User-book rating matrix
- Output: Top similar books

# 🔄 Pipeline Overview

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Recommendation Generation

# 📸 Screenshots
<img width="1316" height="810" alt="Screenshot 2026-03-21 162700" src="https://github.com/user-attachments/assets/ba584116-361e-4118-9cc9-03e3f8b5dd9c" />



# WORKFLOW
UPDATE modules in this order
- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py



