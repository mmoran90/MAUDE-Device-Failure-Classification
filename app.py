import pickle
import numpy as np
import xgboost as xgb
import pandas as pd
from flask import Flask, render_template, request, jsonify, url_for
import os
import re
import nltk
from nltk.corpus import stopwords

# Import additional requirements
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

app = Flask(__name__)
app.static_folder = 'static'

# Load the best model
with open("optimal_model.pkl", "rb") as plkFile:
    model = pickle.load(plkFile)

# Load the vectorizer
with open("tfidf_vectorizer.pkl", "rb") as tfidf_file:
    vectorizer = pickle.load(tfidf_file)

# Load encoded labels from CSV
encoded_labels_df = pd.read_csv('encoded_labels.csv')

# Function to clean and tokenize text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = text.split() 
    return tokens

# Function to remove stopwords
def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

def processInput(input):
    # Transform the input using the pre-fitted vectorizer
    pred = vectorizer.transform(input)
    
    # Create DMatrix from the sparse matrix
    dmatrix = xgb.DMatrix(pred)  
    
    # Make predictions using the DMatrix
    result = model.predict(dmatrix)  
    
    # Get the index of the highest prediction score
    most_likely_index = np.argmax(result)
    most_likely_label = encoded_labels_df.columns[most_likely_index]
    return most_likely_label

# Enable CSS modifications
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# Setup Flask connection and methods
@app.route("/", methods=['GET', 'POST'])
#@app.route("/", methods=['POST'])
def home():
    prediction = None
    if request.method == 'POST':
        # Get info from user input
        brand_name = request.form['brand_name']
        patient_problem = request.form['patient_problem']
        manufacturer_narrative = request.form['manufacturer_narrative']
        event_desc = request.form['event_desc']

        # Concatenate input into a single string
        user_input = " ".join([brand_name, patient_problem, manufacturer_narrative, event_desc])

        # Pre-process and clean user input text
        processed_text = preprocess_text(user_input)
        clean_input = remove_stopwords(processed_text)

        # Get the most likely prediction
        prediction = processInput(clean_input)
        return jsonify({'prediction': prediction})

    return render_template('index.html', prediction=prediction)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)