# Bengaluru House Price Prediction

This project aims to predict house prices in Bengaluru, using key features such as location, square footage, number of bathrooms, and BHK (bedroom, hall, kitchen). The objective is to build a machine learnnng model that can help buyers, sellers, and investors make informed decisions regarding real estate in Bengaluru.

## Dataset Overview

The dataset includes the following features:
- **location**: The area where the house is located.
- **total_sqft**: The total area of the house in square feet.
- **bath**: The number of bathrooms.
- **bhk**: The number of bedrooms, halls, and kitchens.
- **price**: The target variable representing the house price in lakhs.

## Model Overview.

Three regression models were implemented and evaluated:
- **Linear Regression**: A baseline model for performance comparison.
- **Lasso Regression**: A regularization technique to reduce overfitting.
- **Ridge Regression**: The final model, which performed the best with an R² score of **0.9180**.

Ridge Regression was selected as the best model due to its ability to handle multicollinearity and generalize better than the other models.

## Key Features
- **Preprocessing**: Handling missing data, encoding categorical variables, and scaling numerical features.
- **Model Training**: Utilized pipelines to streamline the workflow from preprocessing to model training.
- **Performance**: Ridge Regression achieved the highest accuracy with an R² score of 0.9180.

## Future Scope
- Add more features (e.g., property age, proximity to amenities).
- Deploy the model for real-time house price predictions.
- Experiment with advanced models like Random Forest or Gradient Boosting.

## Final Metrics

| Model               | R² Score     |
|---------------------|--------------|
| Linear Regression   | 0.8572       |
| Lasso Regression    | 0.8874       |
| Ridge Regression    | 0.9180       |

---

### Installation
Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/Bengaluru-House-Price-Prediction.git
cd Bengaluru-House-Price-Prediction
pip install -r requirements.txt
