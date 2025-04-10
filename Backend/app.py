from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime
import json

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")

# History file to log predictions
HISTORY_FILE = "history.json"

# Function to log prediction history
def save_to_history(entry):
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# API Endpoint: Predict best server
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        features = np.array([
            [
                data["cpu"],       # % CPU Usage
                data["memory"],    # % Memory Usage
                data["latency"],   # Response Time
                data["uptime"]     # Uptime
            ]
        ])
    except KeyError:
        return jsonify({"error": "Missing input values"}), 400

    prediction = model.predict(features)[0]

    # Save to history
    entry = {
        "timestamp": datetime.now().isoformat(),
        "input": data,
        "prediction": prediction
    }
    save_to_history(entry)

    return jsonify({"best_server": prediction})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

