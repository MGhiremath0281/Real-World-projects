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
   - Based on evaluation metrics, **Gradient Boosting** was chosen as the final model for deployment.

3. **Model Performance**  
   - **Accuracy:** 52%  
   - **Classification Report:**  
     ```
                 precision    recall  f1-score   support

              0       0.53      0.51      0.52       102
              1       0.50      0.52      0.51        98

       accuracy                           0.52       200
      macro avg       0.52      0.52      0.51       200
   weighted avg       0.52      0.52      0.52       200
     ```
   - The **Gradient Boosting** model provided moderate performance but serves as a baseline for further optimization.

4. **Web Application**  
   - Built a Flask-based web application for easy user interaction.  
   - Integrated the model to predict attrition dynamically based on user inputs.  
   - Encoded inputs using pre-trained LabelEncoders and standardized data using a saved Scaler.

---

## Outcome

This project provides organizations with a tool to:  
- Identify employees at risk of attrition.  
- Initiate steps to improve retention strategies.  
- Build on this baseline model to further enhance prediction accuracy.
