# Crop Recommendation System 🌾

This project is a **Crop Recommendation System** that predicts the most suitable crop to grow based on soil and environmental parameters.

## Problem Statement
Farmers often face challenges in deciding which crop to cultivate based on their land's condition. This system uses machine learning to recommend crops based on input parameters such as:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

## Approach
1. **Dataset**: The model is trained on a dataset containing soil, weather, and crop information.
2. **Pipeline**:
   - Standardization of input features using `StandardScaler`.
   - Model training using **Gradient Boosting Classifier** for high accuracy.
3. **Deployment**:
   - A Flask web application with a user-friendly interface.
   - Users can input parameters to get crop recommendations.

## Features
- Accepts soil and environmental parameters as inputs.
- Provides precise crop recommendations based on trained machine learning models.
- Deployed using Flask with an intuitive UI.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/crop-recommendation.git
