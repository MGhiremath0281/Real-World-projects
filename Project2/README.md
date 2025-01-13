# Fraud Detection Model

## Problem Statement

The goal of this project is to detect fraudulent financial transactions to prevent losses. The dataset consists of transaction details, and the challenge is to predict whether a transaction is fraudulent (`1`) or not (`0`).

## Approach

- **Data Preprocessing**: Categorical features were encoded and numerical features were scaled to improve the model's performance.
- **Model**: After evaluating different models, **Random Forest** was selected as the final model for prediction.
- **Handling Imbalanced Data**: The dataset was imbalanced, so **under-sampling** was used to balance it. Further improvements will be made in future versions.

## Challenges

- The dataset was imbalanced, with more non-fraudulent transactions than fraudulent ones, leading to biases in predictions.
- Consistent preprocessing of features (encoding and scaling) was crucial for making predictions on new data.

## Future Work

- Handling class imbalance better using techniques like **SMOTE**.
- Further model improvements and better handling of real-time predictions.


