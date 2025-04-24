import pandas as pd
import numpy as np

# Create a larger dataset for meaningful aggregation
np.random.seed(42)
n_records = 1000

data = {
    'application_date': pd.date_range('2024-01-01', periods=n_records),
    'loan_type': np.random.choice(['Home', 'Business', 'Education', 'Car'], n_records),
    'loan_amount': np.random.normal(100000, 50000, n_records),
    'credit_score': np.random.normal(700, 50, n_records),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
    'status': np.random.choice(['Approved', 'Pending', 'Rejected'], n_records, p=[0.6, 0.3, 0.1])
}

df = pd.DataFrame(data)

# 1. Basic grouping
print("Average Loan Amount by Type:")
print(df.groupby('loan_type')['loan_amount'].mean())

# 2. Multiple aggregations
print("\nMultiple Metrics by Region:")
agg_metrics = df.groupby('region').agg({
    'loan_amount': ['count', 'mean', 'sum'],
    'credit_score': ['mean', 'min', 'max']
})
print(agg_metrics)

# 3. Pivot table
print("\nPivot Table - Average Loan Amount by Region and Type:")
pivot_table = pd.pivot_table(
    df,
    values='loan_amount',
    index='region',
    columns='loan_type',
    aggfunc='mean'
)
print(pivot_table)

# 4. Time-based analysis
df['month'] = df['application_date'].dt.month
monthly_stats = df.groupby('month').agg({
    'loan_amount': 'sum',
    'application_date': 'count'
}).rename(columns={'application_date': 'num_applications'})

monthly_stats['avg_loan_size'] = monthly_stats['loan_amount'] / monthly_stats['num_applications']

print("\nMonthly Application Statistics:")
print(monthly_stats)