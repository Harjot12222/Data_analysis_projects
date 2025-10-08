# ----------------------------------------
# 💰 Expense Tracker & Category Spending Analysis
# ----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(path)

# ---- Basic Overview ----
print("Columns in dataset:\n", df.columns, "\n")
print(f"Total Transactions: {len(df)}\n")

# ---- Sort by Transaction Date ----
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors='coerce')
df = df.sort_values("Transaction Date")

# ---- Unique Categories ----
unique_categories = df["Category"].unique()
print(f"🛒 Unique Spending Categories ({len(unique_categories)}): {unique_categories}\n")

# ---- Category-Wise Spending ----
category_totals = (
    df.groupby("Category")["Total Spent"]
    .sum()
    .reset_index()
    .sort_values(by="Total Spent", ascending=False)
)

print("💵 Total Spending by Category:\n", category_totals.to_string(index=False), "\n")

# ---- Highest Spending Category ----
top_category = category_totals.iloc[0]
print(f"🏆 Highest Spending Category: {top_category['Category']} (${top_category['Total Spent']:.2f})\n")

# ---- Monthly Spending Trend (Optional Enhancement) ----
df["Month"] = df["Transaction Date"].dt.to_period("M")
monthly_expense = df.groupby("Month")["Total Spent"].sum().reset_index()

# ---- Visualizations ----
plt.figure(figsize=(8, 5))
plt.bar(category_totals["Category"], category_totals["Total Spent"], color="skyblue", edgecolor="black")
plt.title("Total Spending by Category")
plt.xlabel("Category")
plt.ylabel("Total Spent ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(monthly_expense["Month"].astype(str), monthly_expense["Total Spent"], marker="o", color="teal")
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Total Spent ($)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
