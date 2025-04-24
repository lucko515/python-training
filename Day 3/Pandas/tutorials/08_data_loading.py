# -----------------------------------------------------------------------------
# PANDAS DATA LOADING AND EXPORTING
# -----------------------------------------------------------------------------

"""
INSTRUCTOR NOTES:

Duration: ~45 minutes

This tutorial covers:
1. Reading and writing various file formats
2. Handling different data types and formats
3. Working with dates and times
4. Dealing with missing data
5. Best practices for data I/O
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

# Create a data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)

# -----------------------------------------------------------------------------
# 1. CSV Files
# -----------------------------------------------------------------------------
print("1. CSV FILES")
print("-" * 50)

# Create sample sales data
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=5),
    'product_id': ['P001', 'P002', 'P001', 'P003', 'P002'],
    'quantity': [10, 5, 8, 12, 6],
    'unit_price': [99.99, 149.99, 99.99, 79.99, 149.99],
    'total': lambda x: x['quantity'] * x['unit_price']
})

# Save to CSV
sales_data.to_csv(data_dir / 'sales.csv', index=False)
print("Original sales data:")
print(sales_data)

# Read from CSV with type specification
sales_from_csv = pd.read_csv(
    data_dir / 'sales.csv',
    parse_dates=['date'],
    dtype={
        'product_id': str,
        'quantity': int,
        'unit_price': float
    }
)
print("\nData loaded from CSV:")
print(sales_from_csv.dtypes)

# -----------------------------------------------------------------------------
# 2. Excel Files
# -----------------------------------------------------------------------------
print("\n2. EXCEL FILES")
print("-" * 50)

# Create multiple dataframes for different sheets
products = pd.DataFrame({
    'product_id': ['P001', 'P002', 'P003'],
    'name': ['Widget', 'Gadget', 'Tool'],
    'category': ['Electronics', 'Electronics', 'Hardware'],
    'in_stock': [True, False, True]
})

categories = pd.DataFrame({
    'category': ['Electronics', 'Hardware', 'Software'],
    'tax_rate': [0.20, 0.15, 0.10],
    'department': ['Tech', 'Operations', 'Tech']
})

# Save multiple sheets to Excel
with pd.ExcelWriter(data_dir / 'inventory.xlsx') as writer:
    sales_data.to_excel(writer, sheet_name='Sales', index=False)
    products.to_excel(writer, sheet_name='Products', index=False)
    categories.to_excel(writer, sheet_name='Categories', index=False)

# Read specific sheet from Excel
products_from_excel = pd.read_excel(
    data_dir / 'inventory.xlsx',
    sheet_name='Products'
)
print("Products from Excel:")
print(products_from_excel)

# -----------------------------------------------------------------------------
# 3. JSON Files
# -----------------------------------------------------------------------------
print("\n3. JSON FILES")
print("-" * 50)

# Create nested data structure
customer_data = {
    'customers': [
        {
            'id': 'C001',
            'name': 'John Doe',
            'orders': [
                {'order_id': 'O001', 'amount': 150.0},
                {'order_id': 'O002', 'amount': 75.5}
            ]
        },
        {
            'id': 'C002',
            'name': 'Jane Smith',
            'orders': [
                {'order_id': 'O003', 'amount': 225.0}
            ]
        }
    ]
}

# Save to JSON
with open(data_dir / 'customers.json', 'w') as f:
    json.dump(customer_data, f, indent=2)

# Read JSON with normalization
with open(data_dir / 'customers.json', 'r') as f:
    json_data = json.load(f)
    
customers_df = pd.json_normalize(
    json_data['customers'],
    record_path='orders',
    meta=['id', 'name']
)
print("Normalized customer data:")
print(customers_df)

# -----------------------------------------------------------------------------
# 4. SQL Database (SQLite example)
# -----------------------------------------------------------------------------
print("\n4. SQL DATABASE")
print("-" * 50)

import sqlite3

# Create SQLite database and save data
conn = sqlite3.connect(data_dir / 'sales.db')
sales_data.to_sql('sales', conn, index=False, if_exists='replace')
products.to_sql('products', conn, index=False, if_exists='replace')

# Read from SQL with query
sql_query = """
SELECT s.date, s.product_id, p.name, s.quantity, s.unit_price
FROM sales s
JOIN products p ON s.product_id = p.product_id
WHERE s.quantity > 5
"""
sql_results = pd.read_sql(sql_query, conn)
print("SQL query results:")
print(sql_results)
conn.close()

# -----------------------------------------------------------------------------
# 5. Handling Different Date Formats
# -----------------------------------------------------------------------------
print("\n5. DATE FORMATS")
print("-" * 50)

dates_df = pd.DataFrame({
    'date_str': [
        '2024-01-01',
        '01/15/2024',
        '2024.02.01',
        'March 1, 2024'
    ]
})

# Convert to datetime using different formats
dates_df['date_iso'] = pd.to_datetime(dates_df['date_str'])
dates_df['date_custom'] = pd.to_datetime(
    dates_df['date_str'],
    format='mixed',  # Auto-detect format
    dayfirst=False  # Use US date format (month first)
)

print("Parsed dates:")
print(dates_df)

# -----------------------------------------------------------------------------
# 6. Handling Missing Data
# -----------------------------------------------------------------------------
print("\n6. MISSING DATA")
print("-" * 50)

# Create data with missing values
missing_data = pd.DataFrame({
    'A': [1, np.nan, 3, None, 5],
    'B': ['a', 'b', None, 'd', np.nan],
    'C': [1.0, 2.0, 3.0, np.nan, 5.0]
})

# Save with different missing value representations
missing_data.to_csv(data_dir / 'missing.csv', na_rep='NULL')
missing_data.to_excel(data_dir / 'missing.xlsx', na_rep='N/A')

# Read with missing value handling
from_csv = pd.read_csv(
    data_dir / 'missing.csv',
    na_values=['NULL', 'N/A', ''],
    keep_default_na=True
)
print("Data with missing values:")
print(from_csv)

"""
Key Takeaways:
1. Pandas supports multiple file formats (CSV, Excel, JSON, SQL)
2. Data type specification improves data integrity
3. Date parsing can handle various formats
4. Missing data can be represented differently
5. Excel files can contain multiple sheets
6. JSON data can be normalized into flat DataFrames
""" 