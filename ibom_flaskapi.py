# app.py
from flask import Flask, request, jsonify
import joblib

# Load the trained model
model = joblib.load('nlp_model.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    query = data.get('query')
    if query:
        prediction = model.predict([query])[0]
        return jsonify({'category': prediction})
    return jsonify({'error': 'No query provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)