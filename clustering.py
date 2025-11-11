import pandas as pd
import matplotlib.pyplot as plt

# === Parameters ===
input_file = "summary10.dat"   # replace with your file name
time_per_frame = 0.01  # ns per frame
window = 100  # number of frames per averaging window for populations

# === Load file ===
df = pd.read_csv(input_file, delim_whitespace=True, header=0, names=["Frame", "Cluster"])
df = df.dropna()
df["Time_ns"] = df["Frame"] * time_per_frame

# === Timeline plot (what you already did) ===
plt.figure(figsize=(12, 5))
plt.scatter(df["Time_ns"], df["Cluster"], s=5, c=df["Cluster"], cmap="tab20", marker="o")
plt.title("Cluster Distribution Over Simulation Time", fontsize=14)
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("Cluster ID", fontsize=12)
plt.colorbar(label="Cluster ID")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# === Population over time (stacked area plot) ===
# Bin the trajectory into windows and compute fraction of each cluster
df["bin"] = df["Frame"] // window
pop = df.groupby(["bin", "Cluster"]).size().unstack(fill_value=0)
pop = pop.div(pop.sum(axis=1), axis=0)  # normalize to fractions
pop.index = pop.index * window * time_per_frame  # convert bin → time

plt.figure(figsize=(12, 6))
plt.stackplot(pop.index, pop.T, labels=pop.columns, cmap="tab10")
plt.title("Cluster Population Distribution Over Time", fontsize=14)
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("Fraction of Population", fontsize=12)
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

