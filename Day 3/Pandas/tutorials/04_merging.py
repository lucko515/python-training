import pandas as pd
import numpy as np

# Create main loan applications DataFrame
loans_df = pd.DataFrame({
    'application_id': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'customer_id': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'loan_amount': [50000, 75000, 100000, 25000, 150000],
    'status': ['Approved', 'Pending', 'Approved', 'Rejected', 'Approved']
})

# Create customer details DataFrame
customers_df = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C003', 'C006', 'C007'],
    'name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Charlie Davis'],
    'credit_score': [720, 680, 750, 690, 700]
})

# Create payment history DataFrame
payments_df = pd.DataFrame({
    'application_id': ['A001', 'A001', 'A003', 'A003', 'A005'],
    'payment_date': ['2024-01-15', '2024-02-15', '2024-01-15', '2024-02-15', '2024-01-15'],
    'payment_amount': [1000, 1000, 2000, 2000, 3000]
})

print("Original DataFrames:")
print("\nLoan Applications:")
print(loans_df)
print("\nCustomer Details:")
print(customers_df)
print("\nPayment History:")
print(payments_df)

# 1. Inner join
print("\nInner Join (Loans + Customers):")
inner_join = loans_df.merge(customers_df, on='customer_id', how='inner')
print(inner_join)

# 2. Left join
print("\nLeft Join (Loans + Customers):")
left_join = loans_df.merge(customers_df, on='customer_id', how='left')
print(left_join)

# 3. Multiple joins
print("\nMultiple Joins (Loans + Customers + Payments):")
# First merge loans and customers
full_data = loans_df.merge(customers_df, on='customer_id', how='left')
# Then merge with payments
full_data = full_data.merge(
    payments_df.groupby('application_id')['payment_amount'].sum().reset_index(),
    on='application_id',
    how='left'
)
print(full_data)