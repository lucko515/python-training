import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create a sample loan applications DataFrame
data = {
    'applicant_id': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'loan_amount': [50000, 75000, 100000, 25000, 150000],
    'credit_score': [720, 680, 750, 620, 800],
    'annual_income': [60000, 85000, 120000, 45000, 200000],
    'loan_purpose': ['Home', 'Business', 'Education', 'Car', 'Home']
}

df = pd.DataFrame(data)

print("Basic DataFrame Structure:")
print(df)

# Demonstrate basic attributes
print("\nDataFrame Information:")
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)

# Basic statistics
print("\nNumerical Column Statistics:")
print(df.describe())

# Accessing data
print("\nDifferent Ways to Access Data:")
print("\nSingle column (Series):")
print(df['loan_amount'])

print("\nMultiple columns:")
print(df[['applicant_id', 'loan_amount', 'credit_score']])

print("\nFiltering data (credit score > 700):")
print(df[df['credit_score'] > 700])

print("#" * 50)
print(df[df['loan_amount'] > 50000][['applicant_id', 'loan_amount', 'credit_score']])

# SQL style filtering
print("\nSQL Style Filtering:")
print(df.query('credit_score > 700 and loan_amount > 50000'))