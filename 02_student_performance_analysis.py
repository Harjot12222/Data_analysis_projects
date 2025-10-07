# ----------------------------
# 📘 Student Performance Analysis
# ----------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(path)

# Display column names for reference
print("Columns in dataset:\n", df.columns, "\n")

# ---- Descriptive Statistics ----
print("📈 Statistical Summary for Math Scores:")
print(df["math_score"].describe(), "\n")

# ---- Mean Values Across Subjects ----
mean_reading = df["reading_score"].mean()
mean_writing = df["writing_score"].mean()
mean_science = df["science_score"].mean()

print(f"Average Reading Score: {mean_reading:.2f}")
print(f"Average Writing Score: {mean_writing:.2f}")
print(f"Average Science Score: {mean_science:.2f}\n")

# ---- Correlation Analysis ----
if "total_score" in df.columns and "test_preparation_course" in df.columns:
    corr_value = df["total_score"].corr(df["test_preparation_course"])
    print(f"Correlation between Total Score and Test Preparation Course: {corr_value:.3f}")
else:
    print("⚠️ Columns for correlation ('total_score' or 'test_preparation_course') not found.\n")

# ---- Visualization ----
plt.figure(figsize=(7, 5))
plt.scatter(df["science_score"], df["writing_score"], alpha=0.7, edgecolors='k')
plt.title("Science vs Writing Scores")
plt.xlabel("Science Score")
plt.ylabel("Writing Score")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
