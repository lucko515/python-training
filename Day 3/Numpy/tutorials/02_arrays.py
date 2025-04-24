import numpy as np

# Create NumPy array from the same data
monthly_revenue = np.array([
    100000, 120000, 115000, 130000, 140000, 135000,
    145000, 150000, 160000, 165000, 175000, 180000
])

print(monthly_revenue[:-1])
print(np.diff(monthly_revenue))
growth_rate = np.diff(monthly_revenue) / monthly_revenue[:-1]
print(growth_rate)

print("Monthly Growth Rates (%) using NumPy:")
for month, rate in enumerate(growth_rate, 1):
    print(f"Month {month}: {rate:.1f}%")
