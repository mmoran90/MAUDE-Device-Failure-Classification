import pickle
import numpy as np
import xgboost as xgb
from flask import Flask, render_template, request, jsonify, url_for
import os

app = Flask(__name__)
app.static_folder = 'static'

# Load the best model
with open("optimal_model.pkl", "rb") as plkFile:
    model = pickle.load(plkFile)

# Load the vectorizer
with open("tfidf_vectorizer.pkl", "rb") as tfidf_file:
    vectorizer = pickle.load(tfidf_file)

# Create a mapping for numeric predictions to text labels
prediction_labels = {
    0: "No failure",
    1: "Minor failure",
    2: "Major failure",
    3: "Critical failure"
    # Adjust or expand based on your classification categories
}

# Enable CSS modifications
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# Setup Flask connection and methods
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get input from the form fields
        brand_name = request.form['brand_name']
        patient_problem = request.form['patient_problem']
        manufacturer_narrative = request.form['manufacturer_narrative']
        event_desc = request.form['event_desc']

        # Combine the input fields into a single text string
        user_input = f"{brand_name} {patient_problem} {manufacturer_narrative} {event_desc}"

        # Vectorize the input
        data = vectorizer.transform([user_input])

        # Convert the vectorized data to DMatrix for XGBoost
        dmatrix_data = xgb.DMatrix(data)

        # Predict using the loaded model
        prediction = model.predict(dmatrix_data)

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction.tolist()})

    # Render the form on GET request
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
