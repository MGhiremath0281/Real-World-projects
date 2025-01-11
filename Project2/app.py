from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler

app = Flask(__name__)

# Load the trained model, scaler, and label encoders
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Initialize label encoders for categorical columns
label_encoder_type = LabelEncoder()
label_encoder_nameOrig = LabelEncoder()
label_encoder_nameDest = LabelEncoder()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values from the form
        step = int(request.form['step'])
        transaction_type = request.form['type']
        amount = float(request.form['amount'])
        nameOrig = request.form['nameOrig']
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        nameDest = request.form['nameDest']
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])
        isFlaggedFraud = int(request.form['isFlaggedFraud'])

        # Create a DataFrame from the input data
        new_data = pd.DataFrame({
            'step': [step],
            'type': [transaction_type],
            'amount': [amount],
            'nameOrig': [nameOrig],
            'oldbalanceOrg': [oldbalanceOrg],
            'newbalanceOrig': [newbalanceOrig],
            'nameDest': [nameDest],
            'oldbalanceDest': [oldbalanceDest],
            'newbalanceDest': [newbalanceDest],
            'isFlaggedFraud': [isFlaggedFraud]
        })

        # Encode categorical columns in the new data
        new_data['type'] = label_encoder_type.fit_transform(new_data['type'])
        new_data['nameOrig'] = label_encoder_nameOrig.fit_transform(new_data['nameOrig'])
        new_data['nameDest'] = label_encoder_nameDest.fit_transform(new_data['nameDest'])

        # Scale the new data using the saved scaler
        new_data_scaled = scaler.transform(new_data)

        # Predict using the loaded model
        predictions = model.predict(new_data_scaled)

        # Decode the prediction result
        result = predictions[0]

        return render_template('index.html', prediction_text='Prediction for fraud: {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)
