# ----------------------------------------
# 🎬 Movie Ratings & Year Correlation Analysis
# ----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(path)

# ---- Basic Data Overview ----
print("Columns in dataset:\n", df.columns, "\n")
print(f"Total Records: {len(df)}\n")

# ---- Statistical Insights ----
avg_rating = df["rating"].mean()
print(f"⭐ Average Movie Rating: {avg_rating:.2f}")

# Top 5 highest-rated movies
top_movies = df.nlargest(5, "rating")[["title", "rating", "year"]]
print("\n🎥 Top 5 Highest Rated Movies:\n", top_movies.to_string(index=False))

# Correlation between movie rating and release year
correlation = df["rating"].corr(df["year"])
print(f"\n📊 Correlation between Year and Rating: {correlation:.3f}")

# ---- Visualization ----
plt.figure(figsize=(7, 5))
plt.scatter(df["year"], df["rating"], alpha=0.7, edgecolors='k')
plt.title("Movie Ratings Over the Years")
plt.xlabel("Release Year")
plt.ylabel("Rating")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
