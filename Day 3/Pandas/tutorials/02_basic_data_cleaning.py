import pandas as pd
import numpy as np
# Create DataFrame with some issues to clean
data = {
    'applicant_id': ['A001', 'A002', None, 'A004', 'A005'],
    'loan_amount': [50000, np.nan, 100000, 25000, 150000],
    'credit_score': [720, 680, 750, '620', 800],
    'annual_income': ['60,000', '85,000', '120,000', '45,000', '200,000'],
    'application_date': ['2024-01-15', '2024-01-16', '2024-01-16', '2024-01-17', '2024-01-17']
}

df = pd.DataFrame(data)
print("Original DataFrame with Issues:")
print(df)

print(df.isna().sum())

# 1. Handle missing values
print("\nHandling Missing Values:")
df['applicant_id'] = df['applicant_id'].fillna('UNKNOWN')
df['loan_amount'] = df['loan_amount'].fillna(df['loan_amount'].mean())

# 2. Convert data types
print("\nConverting Data Types:")
df['credit_score'] = pd.to_numeric(df['credit_score'])
df['annual_income'] = df['annual_income'].str.replace(',', '').astype(float)
df['application_date'] = pd.to_datetime(df['application_date'])

print("\nCleaned DataFrame:")
print(df)
print("\nUpdated Data Types:")
print(df.dtypes)

# 3. Add derived columns
df['debt_to_income'] = df['loan_amount'] / df['annual_income']
df['application_month'] = df['application_date'].dt.month

print("\nDataFrame with Derived Columns:")
print(df)