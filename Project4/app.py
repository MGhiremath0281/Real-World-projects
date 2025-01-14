from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the saved pipeline (Gradient Boosting model)
with open('gradient_boosting_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize LabelEncoder and fit it with the exact labels used during training
label_encoder = LabelEncoder()
label_encoder.fit([
    'rice', 'maize', 'jute', 'cotton', 'coconut', 'papaya', 'orange', 'apple',
    'muskmelon', 'watermelon', 'grapes', 'mango', 'banana', 'pomegranate', 'lentil',
    'blackgram', 'mungbean', 'mothbeans', 'pigeonpeas', 'kidneybeans', 'chickpea', 'coffee'
])  # Use the full list of labels here

# Route to render the prediction form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        
        # Prepare the input data for prediction
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Convert prediction back to the original label using label encoder
        crop = label_encoder.inverse_transform(prediction)

        return render_template('index.html', prediction_text=f"Recommended Crop: {crop[0]}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
