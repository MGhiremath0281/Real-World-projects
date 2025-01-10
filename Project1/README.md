# Insurance Charges Prediction

## Overview

This project aims to predict insurance charges for individuals based on various demographic and health-related features. The prediction model uses **Gradient Boosting** to estimate the insurance charges based on input features like age, sex, BMI, number of children, smoking habits, and region.

## Features

The model uses the following features to predict the insurance charges:
- **age**: Age of the individual.
- **sex**: Gender of the individual (male/female).
- **bmi**: Body Mass Index (BMI).
- **children**: Number of children or dependents.
- **smoker**: Whether the individual is a smoker (yes/no).
- **region**: Region where the individual resides (southeast, southwest, northeast, northwest).

## Approach

- **Data Preprocessing**: The categorical features (sex, smoker, region) were encoded using predefined mappings. Numerical features were scaled using **StandardScaler** to improve the performance of the Gradient Boosting model.
  
- **Model Selection**: The model chosen for this task is **Gradient Boosting**, which is an ensemble learning technique that performs well for regression tasks.

- **Performance**: The model achieved a **R2 score of 0.88** and a **Mean Squared Error (MSE) of 18,686,549.01**, indicating strong predictive accuracy.

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the `app.py` file to start the Flask web application.
4. Use the provided HTML form to input the required data and receive predictions for insurance charges.

## Files in the Repository

- **app.py**: Contains the Flask application code.
- **model/**: Contains the pre-trained Gradient Boosting model, encoder, and scaler.
- **templates/index.html**: The HTML file used for user input and display of prediction results.
- **README.md**: This file providing project details and instructions.

## Further Clarification

For a more detailed explanation of the model, approach, and results, please refer to the full report included in this repository. The report provides a deep dive into the problem statement, dataset, model selection, and evaluation metrics.
