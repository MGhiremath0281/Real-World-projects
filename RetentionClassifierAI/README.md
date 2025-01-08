# Employee Attrition Prediction

## Problem Statement

Employee attrition is a critical challenge for organizations, impacting productivity, costs, and team morale. The goal of this project is to predict whether an employee is likely to leave or stay with the company based on various factors such as age, gender, job satisfaction, monthly working hours, and more.

---

## Approach

1. **Data Preprocessing**  
   - Cleaned and encoded categorical data using Label Encoding.  
   - Standardized numerical features to ensure uniform scaling.  

2. **Model Selection and Training**  
   - Evaluated the following machine learning models:  
     - Logistic Regression  
     - Decision Tree  
     - Random Forest  
     - Support Vector Machine (SVM)  
     - Gradient Boosting  
   - Based on accuracy and other performance metrics, **Gradient Boosting** was chosen as the final model for deployment.

3. **Model Performance**  
   - **Accuracy:** 92.3%  
   - **Precision:** 89.6%  
   - **Recall:** 91.4%  
   - **F1-Score:** 90.5%  
   - The Gradient Boosting model provided the best trade-off between precision and recall, making it highly suitable for this use case.

4. **Web Application**  
   - Built a Flask-based web application for easy user interaction.  
   - Integrated the model to predict attrition dynamically based on user inputs.  
   - Encoded inputs using pre-trained LabelEncoders and standardized data using a saved Scaler.

---

## Outcome

This project helps organizations by:  
- Identifying employees at risk of attrition.  
- Providing actionable insights to improve employee retention strategies.  
- Streamlining decision-making using data-driven predictions.
