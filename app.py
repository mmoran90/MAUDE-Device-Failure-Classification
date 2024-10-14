from flask import Flask, render_template, request, jsonify, url_for
#from sklearn.feature_extraction.text import CountVectorizer
import pickle
import numpy as np
import os

app = Flask(__name__)
app.static_folder = 'static'

# Load the best model
with open("optimal_model.pkl", "rb") as plkFile:
    model = pickle.load(plkFile)

# Load the vectorizer
with open("tfidf_vectorizer.pkl", "rb") as tfidf_file:
    vectorizer = pickle.load(tfidf_file)

# Enable css modifications    
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

# Setup flask connection and methods
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get info from user
        user_input = request.form['text_bar']
        data = vectorizer.transform([user_input])

        # Predict using provided info
        prediction = model.predict(data)
        return jsonify({'prediction': prediction.tolist()})
    
    # Use index.html to show flask page on local host
    return render_template('index.html')  

# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)
