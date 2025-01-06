from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load pre-trained models and other components
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('features.pkl', 'rb') as file:
    feature_names = pickle.load(file)

# Define route for home
@app.route('/')
def home():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = {
        'months_as_customer': [int(request.form['months_as_customer'])],
        'age': [int(request.form['age'])],
        'policy_state': [request.form['policy_state']],
        'policy_csl': [request.form['policy_csl']],
        'policy_deductable': [int(request.form['policy_deductable'])],
        'policy_annual_premium': [float(request.form['policy_annual_premium'])],
        'umbrella_limit': [int(request.form['umbrella_limit'])],
        'insured_sex': [request.form['insured_sex']],
        'insured_education_level': [request.form['insured_education_level']],
        'incident_date': [request.form['incident_date']],
        'incident_type': [request.form['incident_type']],
        'collision_type': [request.form['collision_type']],
        'incident_severity': [request.form['incident_severity']],
        'authorities_contacted': [request.form['authorities_contacted']],
        'incident_state': [request.form['incident_state']],
        'incident_city': [request.form['incident_city']],
        'incident_hour_of_the_day': [int(request.form['incident_hour_of_the_day'])],
        'number_of_vehicles_involved': [int(request.form['number_of_vehicles_involved'])],
        'property_damage': [request.form['property_damage']],
        'bodily_injuries': [int(request.form['bodily_injuries'])],
        'witnesses': [int(request.form['witnesses'])],
        'police_report_available': [request.form['police_report_available']],
        'total_claim_amount': [float(request.form['total_claim_amount'])],
        'injury_claim': [float(request.form['injury_claim'])],
        'property_claim': [float(request.form['property_claim'])],
        'vehicle_claim': [float(request.form['vehicle_claim'])],
        'auto_year': [int(request.form['auto_year'])],
    }

    # Create DataFrame for input data
    new_data = pd.DataFrame(data)

    # One-hot encode categorical features
    categorical_features = [
        'policy_state', 'policy_csl', 'insured_sex', 'insured_education_level',
        'incident_type', 'collision_type', 'incident_severity', 
        'authorities_contacted', 'incident_state', 'property_damage', 
        'police_report_available'
    ]
    new_data_encoded = pd.get_dummies(new_data, columns=categorical_features)

    # Align new data with training features
    new_data_encoded = new_data_encoded.reindex(columns=feature_names, fill_value=0)

    # Scale the input data
    new_data_scaled = scaler.transform(new_data_encoded)

    # Make predictions
    prediction = model.predict(new_data_scaled)[0]
    prediction_probabilities = model.predict_proba(new_data_scaled)[0]

    # Render results
    return render_template(
        'index.html',  # Same HTML form
        prediction=prediction,
        probability=prediction_probabilities[1],
    )

if __name__ == '__main__':
    app.run(debug=True)
