import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# 1. Bar Plot: Opportunity Amount by Stage
print("1. BAR PLOT: OPPORTUNITY AMOUNTS BY STAGE")
print("-" * 50)

stage_amounts = opportunities.groupby('stage')['amount'].sum()
ax = stage_amounts.plot(kind='bar', figsize=(10, 6))
plt.title('Total Opportunity Amount by Stage')
plt.xlabel('Stage')
plt.ylabel('Total Amount ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Pie Chart: Activities by Type
print("\n2. PIE CHART: ACTIVITIES BY TYPE")
print("-" * 50)

activity_counts = activities['type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Activity Types')
plt.show()

# 3. Time Series: Opportunities Over Time
print("\n3. TIME SERIES: OPPORTUNITIES OVER TIME")
print("-" * 50)

daily_amounts = opportunities.set_index('close_date')['amount']
ax = daily_amounts.plot(kind='line', marker='*', figsize=(10, 6))
plt.title('Opportunity Amounts Over Time')
plt.xlabel('Date')
plt.ylabel('Amount ($)')
plt.grid(True)
plt.show()

# 4. Box Plot: Amount Distribution by Industry
print("\n4. BOX PLOT: AMOUNT DISTRIBUTION BY INDUSTRY")
print("-" * 50)

# Merge opportunities with accounts to get industry information
opp_with_industry = opportunities.merge(accounts[['account_id', 'industry']], on='account_id')
plt.figure(figsize=(10, 6))
sns.boxplot(data=opp_with_industry, x='industry', y='amount')
plt.title('Opportunity Amount Distribution by Industry')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Stacked Bar: Activities by Type and Opportunity
print("\n5. STACKED BAR: ACTIVITIES BY TYPE AND OPPORTUNITY")
print("-" * 50)

activity_pivot = pd.crosstab(activities['opportunity_id'], activities['type'])
ax = activity_pivot.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Activities by Type for Each Opportunity')
plt.xlabel('Opportunity ID')
plt.ylabel('Number of Activities')
plt.legend(title='Activity Type')
plt.tight_layout()
plt.show()

# 6. Heatmap: Correlation Matrix
print("\n6. HEATMAP: CORRELATION MATRIX")
print("-" * 50)

# Create some additional metrics for correlation
opportunities['days_to_close'] = range(len(opportunities))  # Dummy metric
opportunities['win_probability'] = [0.8, 0.6, 0.2, 0.9, 0.85]  # Dummy probability

correlation_matrix = opportunities[['amount', 'days_to_close', 'win_probability']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix of Opportunity Metrics')
plt.tight_layout()
plt.show()

# 7. Scatter Plot with Regression Line
print("\n7. SCATTER PLOT WITH REGRESSION LINE")
print("-" * 50)

plt.figure(figsize=(10, 6))
sns.regplot(data=opportunities, x='days_to_close', y='amount')
plt.title('Opportunity Amount vs Days to Close')
plt.xlabel('Days to Close')
plt.ylabel('Amount ($)')
plt.tight_layout()
plt.show()

"""
Key Takeaways:
1. Pandas provides convenient plotting methods through .plot()
2. Different plot types serve different analytical purposes
3. Seaborn integration enhances statistical visualization
4. Time series data has specialized plotting capabilities
5. Plots can be customized using matplotlib parameters
"""

