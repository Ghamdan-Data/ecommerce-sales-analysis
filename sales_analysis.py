import pandas as pd
import numpy as np

# 1. Create a realistic E-commerce sales dataset
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Laptop'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'Quantity': [1, 3, 2, 1, 4, 5, 1, 2],
    'UnitPrice': [1200, 25, 300, 1200, 45, 25, 300, 1200],
    'CustomerID': ['C101', 'C102', 'C101', 'C103', 'C102', 'C104', 'C103', 'C104']
}

df = pd.DataFrame(data)

# 2. Data Transformation: Calculate Total Sales per Order
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# 3. Key Business Metrics
total_revenue = df['TotalSales'].sum()
top_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()
revenue_by_category = df.groupby('Category')['TotalSales'].sum()

# 4. Display Results
print("--- E-COMMERCE SALES SUMMARY REPORT ---")
print(f"Total Revenue Generated: ${total_revenue:,.2f}")
print(f"Top Selling Product (by Units): {top_selling_product}")
print("\n--- Revenue Distribution by Category ---")
print(revenue_by_category)

print("\n--- Top Customers by Spending ---")
top_customers = df.groupby('CustomerID')['TotalSales'].sum().reset_index().sort_values(by='TotalSales', ascending=False)
print(top_customers)
