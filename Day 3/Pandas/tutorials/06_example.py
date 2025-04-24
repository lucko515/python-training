import pandas as pd
import numpy as np


# Create sample Salesforce-like data
opportunities = pd.DataFrame({
    'opportunity_id': ['OPP001', 'OPP002', 'OPP003', 'OPP004', 'OPP005'],
    'account_id': ['ACC001', 'ACC002', 'ACC001', 'ACC003', 'ACC002'],
    'stage': ['Closed Won', 'Negotiation', 'Closed Lost', 'Closed Won', 'Closed Won'],
    'amount': [100000, 150000, 75000, 200000, 125000],
    'close_date': pd.date_range('2024-01-01', periods=5)
})

accounts = pd.DataFrame({
    'account_id': ['ACC001', 'ACC002', 'ACC003'],
    'name': ['Acme Corp', 'Beta Inc', 'Gamma LLC'],
    'industry': ['Technology', 'Healthcare', 'Finance'],
    'created_date': pd.date_range('2023-01-01', periods=3)
})

activities = pd.DataFrame({
    'activity_id': ['ACT001', 'ACT002', 'ACT003', 'ACT004', 'ACT005'],
    'opportunity_id': ['OPP001', 'OPP001', 'OPP002', 'OPP003', 'OPP005'],
    'type': ['Call', 'Email', 'Meeting', 'Call', 'Email'],
    'date': pd.date_range('2024-01-01', periods=5)
})

# 1. Pipeline Analysis
pipeline_summary = opportunities.groupby('stage').agg({
    'opportunity_id': 'count',
    'amount': ['sum', 'mean']
})
print("Pipeline Summary:")
print(pipeline_summary)

# 2. Account Performance
account_performance = opportunities.merge(accounts, on='account_id').groupby(
    ['name', 'industry']
).agg({
    'amount': ['sum', 'count'],
    'opportunity_id': 'nunique'
})
print("\nAccount Performance:")
print(account_performance)

# 3. Activity Analysis
activity_summary = activities.merge(
    opportunities[['opportunity_id', 'account_id', 'amount']],
    on='opportunity_id'
).groupby('account_id').agg({
    'activity_id': 'count',
    'amount': 'sum'
})
activity_summary['activities_per_dollar'] = activity_summary['activity_id'] / activity_summary['amount']
print("\nActivity Analysis:")
print(activity_summary)

# 4. Time-based Analysis
opportunities['month'] = opportunities['close_date'].dt.month
monthly_trends = opportunities.groupby('month').agg({
    'amount': ['sum', 'count'],
    'opportunity_id': 'nunique'
})
print("\nMonthly Trends:")
print(monthly_trends)
