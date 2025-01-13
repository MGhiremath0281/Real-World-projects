from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model and data
pipe = pickle.load(open("RidgeModel.pkl", "rb"))
data = pd.read_csv("Cleaned_data.csv")

@app.route("/")
def index():
    # Get unique locations for the dropdown
    locations = sorted(data['location'].unique())
    return render_template("index.html", locations=locations)

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    location = request.form.get("location")
    total_sqft = float(request.form.get("total_sqft"))
    bath = int(request.form.get("bath"))
    bhk = int(request.form.get("bhk"))

    # Prepare input DataFrame
    input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], 
                              columns=["location", "total_sqft", "bath", "bhk"])

    # Predict using the model
    prediction = pipe.predict(input_data)[0]
    price = round(prediction * 1e5, 2)  # Assuming scaling was applied during training

    return render_template("index.html", prediction=price, locations=sorted(data['location'].unique()))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
