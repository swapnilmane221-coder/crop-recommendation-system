# 🌾 Crop Recommendation System

![Uploading image.png…]()


> **An intelligent ML-based system that recommends the best crop based on soil and weather conditions!** 🌱

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/ML-Model-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" />
</p>

---

## 🚀 Overview

Choosing the right crop is crucial for maximizing agricultural productivity.  
This **Crop Recommendation System** suggests the best crop to plant based on **soil nutrients** and **environmental conditions** using **Machine Learning**.

---

## 🛠️ Built With

- 🐍 Python 3.10
- 📊 Pandas & NumPy
- 🎯 Scikit-learn
- 🧃 Pickle
- 🎨 (Optional) Streamlit/Flask for deployment

---

## 📊 Dataset Overview

| Feature     | Description                           |
|-------------|---------------------------------------|
| `N`         | Nitrogen content in soil              |
| `P`         | Phosphorous content in soil           |
| `K`         | Potassium content in soil             |
| `Temperature` | Air temperature (°C)                |
| `Humidity`  | Relative humidity (%)                 |
| `pH`        | Soil pH value                         |
| `Rainfall`  | Rainfall (mm)                         |
| `Label`     | Crop Name (Target output)             |

📂 Dataset: `Crop_recommendation.csv`

---

## 🌐 Workflow

<p align="center">
  <img src="assets/workflow.png" alt="Workflow Diagram" width="800px">
</p>

1. Input soil and weather data.
2. Data pre-processing and feature scaling.
3. Predict using trained Random Forest Classifier.
4. Output the most recommended crop.

---

## 📸 Screenshots

| Search Crop Feature | Prediction Output |
|:-------------------:|:-----------------:|
| ![search-page](assets/search.png) | ![prediction-page](assets/predict.png) |

---

## 📂 Project Structure

```bash
├── Crop_recommendation.csv    # Dataset
├── model_training.py          # Model training script
├── crop_recommendation_model.pkl   # Saved ML model
├── label_encoder.pkl          # Saved label encoder
├── assets/                    # Images, banners
├── README.md                  # Project documentation
