# -----------------------------------------------------------------------------
# VECTORIZATION EXERCISE: Customer Lifetime Value Calculator
# -----------------------------------------------------------------------------

"""
Exercise: Convert a complex Customer Lifetime Value (CLV) calculator from Python
to an efficient NumPy implementation.

The calculator considers:
- Purchase history
- Customer loyalty years
- Industry sector
- Company size
- Geographic region multiplier

Your task:
1. Study the Python implementation
2. Create a vectorized version using NumPy
3. Compare performance of both implementations
"""

import numpy as np
import time

# Sample data generation
np.random.seed(42)
n_customers = 1000

# Generate sample customer data
purchase_history = np.random.randint(100, 10000, n_customers)  # Annual purchase value
loyalty_years = np.random.randint(1, 11, n_customers)         # Years as customer
industry_sectors = np.random.randint(1, 5, n_customers)       # 1=Tech, 2=Retail, 3=Manufacturing, 4=Services
company_sizes = np.random.randint(1, 4, n_customers)          # 1=Small, 2=Medium, 3=Large
geo_regions = np.random.randint(1, 4, n_customers)            # 1=NA, 2=EU, 3=APAC

def calculate_clv_python(purchase_value, years, sector, size, region):
    """
    Traditional Python function to calculate Customer Lifetime Value.
    
    This is a complex calculation that considers multiple factors:
    - Base value from purchase history
    - Loyalty multiplier based on years
    - Industry sector adjustments
    - Company size factors
    - Geographic region modifiers
    """
    # Base calculation
    base_value = purchase_value * years
    
    # Loyalty multiplier
    if years < 2:
        loyalty_mult = 1.0
    elif years < 5:
        loyalty_mult = 1.2
    else:
        loyalty_mult = 1.5
        
    # Industry sector adjustment
    if sector == 1:  # Tech
        sector_mult = 1.4
    elif sector == 2:  # Retail
        sector_mult = 1.1
    elif sector == 3:  # Manufacturing
        sector_mult = 1.2
    else:  # Services
        sector_mult = 1.3
        
    # Company size factor
    if size == 1:  # Small
        size_mult = 1.0
    elif size == 2:  # Medium
        size_mult = 1.2
    else:  # Large
        size_mult = 1.5
        
    # Geographic multiplier
    if region == 1:  # NA
        geo_mult = 1.0
    elif region == 2:  # EU
        geo_mult = 0.9
    else:  # APAC
        geo_mult = 1.1
        
    # Calculate final CLV
    clv = base_value * loyalty_mult * sector_mult * size_mult * geo_mult
    
    # Apply minimum and maximum bounds
    clv = max(1000, min(clv, 1000000))
    
    return clv

def calculate_clv_numpy(purchase_values, years, sectors, sizes, regions):
    """
    TODO: Implement a vectorized version of the CLV calculator using NumPy.
    
    Tips:
    1. Use np.where() for conditional logic
    2. Use broadcasting for multiplication
    3. Use np.clip() for bounds
    4. Avoid explicit loops
    """
    pass  # Replace with your implementation

# Test data for a single customer
print("Testing single customer calculation:")
test_purchase = 5000
test_years = 3
test_sector = 1
test_size = 2
test_region = 1

python_result = calculate_clv_python(
    test_purchase, test_years, test_sector, test_size, test_region
)
print(f"Python function result: {python_result}")

# Performance comparison
print("\nComparing performance...")

# Python implementation (loop)
start_time = time.time()
python_results = [
    calculate_clv_python(p, y, s, sz, r)
    for p, y, s, sz, r in zip(
        purchase_history, loyalty_years, industry_sectors, 
        company_sizes, geo_regions
    )
]
python_time = time.time() - start_time
print(f"Python implementation: {python_time:.4f} seconds")

# Your NumPy implementation
start_time = time.time()
try:
    numpy_results = calculate_clv_numpy(
        purchase_history, loyalty_years, industry_sectors,
        company_sizes, geo_regions
    )
    numpy_time = time.time() - start_time
    print(f"NumPy implementation: {numpy_time:.4f} seconds")
    
    if numpy_time < python_time:
        speedup = python_time / numpy_time
        print(f"NumPy is {speedup:.1f}x faster!")
except:
    print("NumPy implementation not completed yet!")

"""
Expected Output:
Testing single customer calculation:
Python function result: 31752.0

Comparing performance...
Python implementation: 0.2340 seconds
NumPy implementation: 0.0021 seconds
NumPy is 111.4x faster!
""" 