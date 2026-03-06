import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

base_dir = Path(__file__).parent
csv_path = base_dir / "sales.csv"

df = pd.read_csv(csv_path)

df["unit_revenue"] = df["quantity"] * df["unit_price"]
df["date"] = pd.to_datetime(df["date"])

print(df)

highest_revenue_product = df.groupby("product")["unit_revenue"].sum().idxmax()
total_sales_per_product = df.groupby("product")["quantity"].sum()

print("\nThe product with the highest revenue was", highest_revenue_product,
      "\n\nTotal sales per product:\n", total_sales_per_product)

monthly_total_revenue = df.groupby(df["date"].dt.to_period("M"))["unit_revenue"].sum()
highest_monthly_revenue = monthly_total_revenue.idxmax()

print("\nRevenue per month:")
print(monthly_total_revenue)

print("\nMonth with the highest revenue was:", highest_monthly_revenue,
      "with revenue of", monthly_total_revenue[highest_monthly_revenue])

highest_revenue_customer = df.groupby("customer")["unit_revenue"].sum().idxmax()

print("\nCustomer with the highest total revenue:", highest_revenue_customer,
      "with revenue of",
      df.groupby("customer")["unit_revenue"].sum()[highest_revenue_customer],
      "(in this economy? :o)")

sales_by_region = df.groupby("region")["quantity"].sum()
revenue_by_region = df.groupby("region")["unit_revenue"].sum()
top_region = revenue_by_region.idxmax()

print("\nTotal sales by region:\n", sales_by_region,
      "\n\nTotal revenue by region:\n", revenue_by_region,
      "\n\nRegion with highest revenue:", top_region,
      "with revenue of", revenue_by_region[top_region])

print("\nThe most important product for the company is",
      df.groupby("product")["unit_revenue"].sum().idxmax(),
      "with the most important investment region being",
      revenue_by_region.idxmax())

revenue_by_product = df.groupby("product")["unit_revenue"].sum()
revenue_by_product.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

monthly_revenue = df.groupby(df["date"].dt.to_period("M"))["unit_revenue"].sum()
monthly_revenue.plot(kind="line")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()