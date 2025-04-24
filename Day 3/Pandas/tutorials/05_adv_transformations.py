import pandas as pd
import numpy as np


# Create sample data with monthly loan performance
dates = pd.date_range('2024-01-01', '2024-12-31', freq='M')
loan_ids = ['L001', 'L002', 'L003']

# Create wide format data (each month as a column)
wide_data = pd.DataFrame(
    np.random.normal(1000, 100, (len(loan_ids), len(dates))),
    index=loan_ids,
    columns=dates
)
wide_data.index.name = 'loan_id'

print("Wide Format Data:")
print(wide_data)

# 1. Melting (wide to long)
long_data = wide_data.reset_index().melt(
    id_vars=['loan_id'],
    var_name='payment_date',
    value_name='payment_amount'
)
print("\nLong Format Data:")
print(long_data)

# 2. Window functions
long_data['cumulative_payment'] = long_data.groupby('loan_id')['payment_amount'].cumsum()
long_data['payment_rank'] = long_data.groupby('loan_id')['payment_amount'].rank(method='dense')
long_data['3_month_avg'] = long_data.groupby('loan_id')['payment_amount'].rolling(3).mean().reset_index(0, drop=True)

print("\nData with Window Functions:")
print(long_data)

# 3. Custom transformation
def calculate_metrics(group):
    return pd.Series({
        'total_payments': group['payment_amount'].sum(),
        'avg_payment': group['payment_amount'].mean(),
        'payment_volatility': group['payment_amount'].std() / group['payment_amount'].mean(),
        'num_payments': len(group)
    })

loan_metrics = long_data.groupby('loan_id').apply(calculate_metrics)
print("\nCustom Aggregation Metrics:")
print(loan_metrics)
