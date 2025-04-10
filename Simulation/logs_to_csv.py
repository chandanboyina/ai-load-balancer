import json
import pandas as pd

with open("simulation_log.json", "r") as f:
    logs = json.load(f)

df = pd.DataFrame(logs)
df.rename(columns={'predicted_server': 'best_server'}, inplace=True)
df.to_csv("data.csv", index=False)

print("✅ Log data converted to data.csv")
