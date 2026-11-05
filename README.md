# E-commerce Sales Performance Analysis

## Project Overview
This repository presents an automated Python data analysis workflow tailored for E-commerce businesses. The analysis calculates essential performance metrics, including total revenue, product sales volume, category-wise revenue distribution, and high-value customer identification.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy

## Business Questions Answered
1. What is the total revenue generated from sales?
2. Which products are moving highest in volume?
3. How is revenue distributed across product categories?
4. Who are the top-spending customers (Customer Lifetime Value insight)?

## Key Code Logic
* Data structure initialization using Pandas DataFrames.
* Derived calculated metrics (`TotalSales = Quantity * UnitPrice`).
* Grouped statistical aggregations for category revenue and customer spending.

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/Ghamdan-Data/ecommerce-sales-analysis.git](https://github.com/Ghamdan-Data/ecommerce-sales-analysis.git)
   python sales_analysis.py
