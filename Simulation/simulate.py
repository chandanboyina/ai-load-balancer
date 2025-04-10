import requests
import random
import time
from datetime import datetime
import json
import os

# URL of your Flask API
API_URL = "http://127.0.0.1:5000/predict"

# File to store simulation results
LOG_FILE = "simulation_log.json"

def simulate_data():
    return {
        "cpu": random.randint(10, 100),
        "memory": random.randint(20, 90),
        "latency": random.randint(80, 300),
        "uptime": random.randint(1, 100)
    }

def append_log(entry):
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Simulate and send data every 5 seconds
while True:
    input_data = simulate_data()
    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()
    except Exception as e:
        print("❌ Error connecting to API:", e)
        break

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": input_data,
        "prediction": result.get("best_server", "error")
    }

    print(f"[{log_entry['timestamp']}] Predicted: {log_entry['prediction']}")
    append_log(log_entry)

    time.sleep(5)
    
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = json.load(f)
else:
    logs = []

# Append new prediction
log_entry = {
    "cpu": data["cpu"],
    "memory": data["memory"],
    "latency": data["latency"],
    "uptime": data["uptime"],
    "predicted_server": prediction
}

logs.append(log_entry)

# Save logs
with open(log_file, "w") as f:
    json.dump(logs, f, indent=2)
