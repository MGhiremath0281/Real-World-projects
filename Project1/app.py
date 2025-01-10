from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the pre-trained scaler and model
with open('scaler.pkl', 'rb') as f:
    loaded_scaler = pickle.load(f)

with open('gradient_boosting_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    age = float(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']
    
    # Manually encode categorical features using the specified mappings
    sex_map = {'male': 0, 'female': 1}
    smoker_map = {'yes': 0, 'no': 1}
    region_map = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}

    # Encode the input values
    new_data = pd.DataFrame({
        'age': [age],
        'sex': [sex_map[sex]],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker_map[smoker]],
        'region': [region_map[region]]
    })

    # Scale the new data using the previously loaded scaler
    new_data_scaled = loaded_scaler.transform(new_data)

    # Use the loaded model to make predictions
    prediction = loaded_model.predict(new_data_scaled)

    # Return the prediction as the output on the webpage
    return render_template('index.html', prediction_text=f'Predicted Charges: ${prediction[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
