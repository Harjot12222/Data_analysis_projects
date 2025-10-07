import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --- Load Data ---
# Replace these with your actual CSV file paths
path_main = "data/weekly_sales.csv"
path_products = "data/product_sales.csv"

df_main = pd.read_csv(path_main)
df_products = pd.read_csv(path_products)


# --- Summary Statistics ---
weekly_avg = df_main["Weekly_Sales"].mean()
weekly_sum = df_main["Weekly_Sales"].sum()
weekly_count = df_main["Weekly_Sales"].count()

print(f"Average Weekly Sales: {weekly_avg:,.2f}")
print(f"Total Weekly Sales: {weekly_sum:,.2f}")
print(f"Total Transactions Recorded: {weekly_count}")


# --- Product-Level Analysis ---
product_sums = {
    "Product 1": df_products["S-P1"].sum(),
    "Product 2": df_products["S-P2"].sum(),
    "Product 3": df_products["S-P3"].sum(),
    "Product 4": df_products["S-P4"].sum(),
}

print("\nTotal Sales by Product Category:")
for product, total in product_sums.items():
    print(f"  {product}: {total:,.2f}")

best_product = max(product_sums, key=product_sums.get)
print(f"\nBest Performing Product: {best_product}")


# --- Visualization ---
plt.figure(figsize=(8, 6))
plt.bar(product_sums.keys(), product_sums.values(), color="skyblue", edgecolor="black")
plt.title("Total Sales by Product Category")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("outputs/product_sales_comparison.png", bbox_inches="tight")
plt.show()
