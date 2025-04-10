import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
data = pd.read_csv('../data/server_metrics.csv')

# Features (input) and label (output)
X = data[['CPU Usage', 'Memory', 'Response Time', 'Uptime']]
y = data['Best Server']

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the trained model
joblib.dump(model, '../backend/model.pkl')
print("✅ Model trained and saved to backend/model.pkl")
