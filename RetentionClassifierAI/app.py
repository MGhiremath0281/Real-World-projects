from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model, scaler, and label encoders
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('label_encoders.pkl', 'rb') as le_file:
    label_encoders = pickle.load(le_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        age = float(request.form['age'])
        gender = request.form['gender']  # Input as string, e.g., "Male" or "Female"
        department = request.form['department']  # Input as string, e.g., "IT", "HR"
        job_title = request.form['job_title']  # Input as string, e.g., "Junior", "Senior"
        years_at_company = float(request.form['years_at_company'])
        satisfaction_level = float(request.form['satisfaction_level'])
        avg_monthly_hours = float(request.form['avg_monthly_hours'])
        promotion_last_5years = int(request.form['promotion_last_5years'])  # 0 or 1
        salary = request.form['salary']  # Input as string, e.g., "Low", "Medium", "High"

        # Encode categorical variables using the loaded LabelEncoders
        gender_encoded = label_encoders['Gender'].transform([gender])[0]
        department_encoded = label_encoders['Department'].transform([department])[0]
        job_title_encoded = label_encoders['Job_Title'].transform([job_title])[0]
        salary_encoded = label_encoders['Salary'].transform([salary])[0]

        # Prepare the input data for prediction
        input_data = np.array([[age, gender_encoded, department_encoded, job_title_encoded, years_at_company,
                                satisfaction_level, avg_monthly_hours, promotion_last_5years, salary_encoded]])

        # Standardize the input data using the saved scaler
        input_data_scaled = scaler.transform(input_data)

        # Make prediction using the trained model
        prediction = model.predict(input_data_scaled)

        # Return the prediction result
        if prediction[0] == 1:
            result = "Employee is likely to leave (Attrition: 1)"
        else:
            result = "Employee is likely to stay (Attrition: 0)"

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
