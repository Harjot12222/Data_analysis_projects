# ----------------------------------------
# 🌍 Global Sales & Profit Performance Analysis
# ----------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and clean dataset
cols_to_keep = [' Profit ', 'Country', 'Date', ' Product ', '  Sales ', ' Units Sold ', 'Year']
df = pd.read_csv(path, usecols=cols_to_keep)
df.dropna(subset=cols_to_keep, inplace=True)
df.reset_index(drop=True, inplace=True)

# Standardize column names
df.columns = df.columns.str.strip()
df.rename(columns={"Sales": "Total Sales", "Profit": "Profit"}, inplace=True)

# Clean Sales column (remove currency symbols and commas)
df['Sales'] = df['Sales'].replace('[\$,]', '', regex=True).astype(float)

# Clean and convert Profit column (handle parentheses for negatives)
profit = df['Profit'].astype(str).str.strip()
profit = profit.replace({'': np.nan, '-': np.nan})
profit = profit.str.replace(r'[\$,]', '', regex=True)
mask_parens = profit.str.startswith('(') & profit.str.endswith(')')
profit_no_parens = profit.str.replace(r'[\(\)]', '', regex=True)
profit_float = pd.to_numeric(profit_no_parens, errors='coerce')
profit_float[mask_parens] *= -1
df['Profit'] = profit_float

# ---- Exploratory Insights ----
print(f"🌎 Countries in dataset: {df['Country'].nunique()} — {df['Country'].unique()[:10]}")
print(f"\nAverage Sales: ${df['Sales'].mean():,.2f}")
print(f"Total Sales: ${df['Sales'].sum():,.2f}")
print(f"Average Profit: ${df['Profit'].mean():,.2f}\n")

# ---- Best Performing Products ----
best_products = (
    df.groupby("Product")["Profit"]
    .sum()
    .reset_index()
    .sort_values(by="Profit", ascending=False)
)
print("🏆 Top 5 Products by Profit:\n", best_products.head(5), "\n")

# ---- Top Performing Regions ----
best_regions = (
    df.groupby("Country")["Sales"]
    .sum()
    .reset_index()
    .sort_values(by="Sales", ascending=False)
)
print("🌍 Top 3 Countries by Total Sales:\n", best_regions.head(3), "\n")

# ---- Correlation Analysis ----
print("📈 Correlation between Sales and Profit:", round(df["Sales"].corr(df["Profit"]), 3))

# ---- Visualizations ----
# 1. Yearly Sales Trend
plt.figure(figsize=(8, 5))
df.groupby("Year")["Sales"].sum().plot(kind="line", marker="o", color="teal")
plt.title("Annual Sales Performance")
plt.xlabel("Year")
plt.ylabel("Total Sales ($)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# 2. Product Profit Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(best_products["Product"][:10], best_products["Profit"][:10], color="royalblue")
plt.title("Top 10 Products by Profit")
plt.xlabel("Product")
plt.ylabel("Profit ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Sales vs Profit Scatter Plot
plt.figure(figsize=(7, 5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.6, color="orange", edgecolor="black")
plt.title("Sales vs Profit Correlation")
plt.xlabel("Sales ($)")
plt.ylabel("Profit ($)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
