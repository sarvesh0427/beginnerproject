# Play Tennis - End-to-End ML System 🎾

This repository contains a full-stack Machine Learning application that predicts whether weather conditions are suitable for playing tennis. It integrates a **Random Forest** model with a modern **FastAPI** backend and an interactive **HTML/CSS/JS** frontend.

## 🚀 Features
* **Machine Learning:** Utilizes Scikit-learn with specialized categorical encoding for weather data.
* **REST API:** A high-performance backend built with FastAPI to serve real-time predictions.
* **Interactive UI:** A clean, responsive frontend for user-friendly data input and instant feedback.
* **Seamless Integration:** Configured with CORS middleware to allow communication between separate frontend and backend environments.

**📊 Dataset**
The dataset used for this project was personally created and curated to simulate realistic weather scenarios and their impact on outdoor sports.

Source: https://www.kaggle.com/datasets/sarveshchhetri/play-tennis-practice-dataset-for-classification

Attributes: 
* Outlook: Sunny, Overcast, Rain
* Temperature: Hot, Mild, Cool
* Humidity: High, Normal
* Wind: Weak, Strong

## 📂 Project Structure
```text
playtennis_full_system/
├── backend/            # FastAPI application logic & API routes
├── frontend/           # UI components (HTML, CSS, JavaScript)
├── dataset/            # CSV source data
├── models/             # Serialized .joblib model and encoders
├── model_training/     # Training script to regenerate the model
└── requirements.txt    # List of Python dependencies

