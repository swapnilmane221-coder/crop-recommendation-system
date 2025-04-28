# 🌾 Crop Recommendation System

![image](https://github.com/user-attachments/assets/d99745ff-1376-4c2c-98b6-87bb4ace2a45)



> **An intelligent ML-based system that recommends the best crop based on soil and weather conditions!** 🌱

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" />
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
| ![image](https://github.com/user-attachments/assets/431a7447-fddc-4f1e-81ba-78096a43f048)
 | ![image](https://github.com/user-attachments/assets/8c523fa8-c283-4d8c-8e7f-2ccb9232a14e)
 |

---

## 📂 Project Structure

```bash
├── Crop_recommendation.csv    # Dataset
├── model_training.py          # Model training script
├── crop_recommendation_model.pkl   # Saved ML model
├── label_encoder.pkl          # Saved label encoder
├── assets/                    # Images, banners
├── README.md                  # Project documentation
