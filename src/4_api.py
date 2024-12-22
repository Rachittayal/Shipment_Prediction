from flask import Flask, request, jsonify, send_from_directory
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

   # Load the trained model
with open('models/delay_prediction_model.pkl', 'rb') as f:
       model = pickle.load(f)

@app.route('/')
def home():
       return send_from_directory('', 'index.html')  # Serve the index.html file

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = pd.DataFrame([data])
    prediction = model.predict(features)
    result = 'Yes' if prediction[0] == 1 else 'No'
    return jsonify({'Delayed': result})

if __name__ == '__main__':
       app.run(debug=True)