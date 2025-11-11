
import pandas as pd
import matplotlib.pyplot as plt

# --- Settings ---
input_file = "summary10.dat"  # change if needed
col_names = ["Cluster", "Frames", "Frac", "AvgDist", "Stdev", "Centroid", "AvgCDist"]

# --- Load ---
df = pd.read_csv(input_file, delim_whitespace=True, comment="#", names=col_names)
df = df.dropna(subset=["Cluster", "Frames", "Frac", "AvgDist", "Stdev"]).copy()
df["Cluster"] = pd.to_numeric(df["Cluster"], errors="coerce").astype(int)
for c in ["Frames", "Frac", "AvgDist", "Stdev", "Centroid", "AvgCDist"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.dropna(subset=["Frames", "Frac", "AvgDist", "Stdev"])

# --- 1) Fractions ---
df_sorted = df.sort_values("Frac", ascending=False).reset_index(drop=True)
plt.figure(figsize=(12, 6))
plt.bar(df_sorted["Cluster"].astype(str), df_sorted["Frac"])
plt.xlabel("Cluster ID")
plt.ylabel("Fraction of Population")
plt.title("Cluster Population Fractions (sorted)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()

# --- 2) AvgDist ± Stdev ---
plt.figure(figsize=(12, 6))
plt.errorbar(df["Cluster"], df["AvgDist"], yerr=df["Stdev"], fmt="o", capsize=3)
plt.xlabel("Cluster ID")
plt.ylabel("Average Distance (± Stdev)")
plt.title("Cluster Average Distances with Variability")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# --- 3) Frames vs Frac ---
plt.figure(figsize=(12, 6))
sc = plt.scatter(df["Frames"], df["Frac"], c=df["Cluster"])
plt.xlabel("Frames")
plt.ylabel("Fraction")
plt.title("Cluster Frames vs Fraction")
cbar = plt.colorbar(sc)
cbar.set_label("Cluster ID")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
