import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

# Load simulation log
with open("simulation_log.json", "r") as f:
    logs = json.load(f)

# Convert to DataFrame
data = []
for entry in logs:
    data.append({
        "timestamp": datetime.fromisoformat(entry["timestamp"]),
        "cpu": entry["input"]["cpu"],
        "memory": entry["input"]["memory"],
        "latency": entry["input"]["latency"],
        "uptime": entry["input"]["uptime"],
        "prediction": entry["prediction"]
    })

df = pd.DataFrame(data)

# Plot settings
plt.figure(figsize=(18, 16))
sns.set(style="whitegrid")

# ✅ 1. Line Graph: CPU, Memory, Latency, Uptime over Time
plt.subplot(4, 1, 1)
plt.plot(df["timestamp"], df["cpu"], label="CPU (%)", color="red")
plt.plot(df["timestamp"], df["memory"], label="Memory (%)", color="blue")
plt.plot(df["timestamp"], df["latency"], label="Latency (ms)", color="green")
plt.plot(df["timestamp"], df["uptime"], label="Uptime (hrs)", color="purple")
plt.legend()
plt.title("Server Metrics Over Time")
plt.ylabel("Value")
plt.xticks(rotation=45)

# ✅ 2. Annotated Line: Predicted Server Over Time
plt.subplot(4, 1, 2)
plt.plot(df["timestamp"], df["prediction"], label="Predicted Server", color="orange", marker="o", linestyle='--')
for i, val in enumerate(df["prediction"]):
    plt.annotate(str(val), (df["timestamp"][i], df["prediction"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
plt.title("Load Balancer Predictions")
plt.ylabel("Server ID")
plt.xticks(rotation=45)
plt.legend()

# ✅ 3. Heatmap: Server Load Distribution (Pivot for Heatmap)
pivot_data = df.pivot_table(index="prediction", columns=df["timestamp"].dt.strftime('%H:%M:%S'), values="cpu", aggfunc='mean')
sns.heatmap(pivot_data, cmap="Reds", linewidths=0.5, annot=True, fmt=".0f", cbar_kws={'label': 'CPU Usage (%)'}, ax=plt.subplot(4, 1, 3))
plt.title("Server Load Distribution Heatmap")
plt.ylabel("Predicted Server")
plt.xlabel("Time")

# ✅ 4. Bar Graph: Server Prediction Frequency
plt.subplot(4, 1, 4)
server_counts = df["prediction"].value_counts().sort_index()
plt.bar(server_counts.index.astype(str), server_counts.values, color="teal")
plt.title("Prediction Frequency per Server")
plt.xlabel("Server ID")
plt.ylabel("Times Selected")

plt.tight_layout()
plt.savefig("detailed_visualization.png")
print("✅ Graph saved as detailed_visualization.png")

