# Example: Calculate revenue growth from monthly data
monthly_revenue = [
    100000, 120000, 115000, 130000, 140000, 135000,
    145000, 150000, 160000, 165000, 175000, 180000
]

# Calculate month-over-month growth rates (inefficient way)
growth_rates = []
for i in range(1, len(monthly_revenue)):
    previous = monthly_revenue[i-1]
    current = monthly_revenue[i]
    growth = ((current - previous) / previous) * 100
    growth_rates.append(growth)

print("Monthly Growth Rates (%):")
for month, rate in enumerate(growth_rates, 1):
    print(f"Month {month}: {rate:.1f}%")

# Calculate average revenue (inefficient for large datasets)
average_revenue = sum(monthly_revenue) / len(monthly_revenue)
print(f"\nAverage Monthly Revenue: ${average_revenue:,.2f}")