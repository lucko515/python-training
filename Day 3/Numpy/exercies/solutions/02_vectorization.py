# -----------------------------------------------------------------------------
# VECTORIZATION EXERCISE SOLUTION: Customer Lifetime Value Calculator
# -----------------------------------------------------------------------------

import numpy as np
import time

# Sample data generation (same as exercise)
np.random.seed(42)
n_customers = 1000

# Generate sample customer data
purchase_history = np.random.randint(100, 10000, n_customers)  # Annual purchase value
loyalty_years = np.random.randint(1, 11, n_customers)         # Years as customer
industry_sectors = np.random.randint(1, 5, n_customers)       # 1=Tech, 2=Retail, 3=Manufacturing, 4=Services
company_sizes = np.random.randint(1, 4, n_customers)          # 1=Small, 2=Medium, 3=Large
geo_regions = np.random.randint(1, 4, n_customers)            # 1=NA, 2=EU, 3=APAC

def calculate_clv_python(purchase_value, years, sector, size, region):
    """Python implementation (same as exercise)"""
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
    Vectorized NumPy implementation of the CLV calculator.
    
    This implementation uses NumPy's vectorized operations and broadcasting
    to efficiently calculate CLV for multiple customers simultaneously.
    """
    # Base calculation
    base_values = purchase_values * years
    
    # Loyalty multiplier using np.where()
    loyalty_mult = np.where(
        years < 2, 1.0,
        np.where(years < 5, 1.2, 1.5)
    )
    
    # Industry sector adjustment using np.select()
    sector_conditions = [
        sectors == 1,  # Tech
        sectors == 2,  # Retail
        sectors == 3,  # Manufacturing
        sectors == 4   # Services
    ]
    sector_choices = [1.4, 1.1, 1.2, 1.3]
    sector_mult = np.select(sector_conditions, sector_choices)
    
    # Company size factor using np.select()
    size_conditions = [
        sizes == 1,  # Small
        sizes == 2,  # Medium
        sizes == 3   # Large
    ]
    size_choices = [1.0, 1.2, 1.5]
    size_mult = np.select(size_conditions, size_choices)
    
    # Geographic multiplier using np.select()
    geo_conditions = [
        regions == 1,  # NA
        regions == 2,  # EU
        regions == 3   # APAC
    ]
    geo_choices = [1.0, 0.9, 1.1]
    geo_mult = np.select(geo_conditions, geo_choices)
    
    # Calculate final CLV using broadcasting
    clv = base_values * loyalty_mult * sector_mult * size_mult * geo_mult
    
    # Apply minimum and maximum bounds using np.clip()
    return np.clip(clv, 1000, 1000000)

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

numpy_result = calculate_clv_numpy(
    np.array([test_purchase]),
    np.array([test_years]),
    np.array([test_sector]),
    np.array([test_size]),
    np.array([test_region])
)[0]
print(f"NumPy function result: {numpy_result}")

# Verify results match
assert abs(python_result - numpy_result) < 0.01, "Results don't match!"
print("✓ Results match!")

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

# NumPy implementation
start_time = time.time()
numpy_results = calculate_clv_numpy(
    purchase_history, loyalty_years, industry_sectors,
    company_sizes, geo_regions
)
numpy_time = time.time() - start_time
print(f"NumPy implementation: {numpy_time:.4f} seconds")

# Calculate speedup
speedup = python_time / numpy_time
print(f"NumPy is {speedup:.1f}x faster!")

# Verify results
assert np.allclose(python_results, numpy_results), "Batch results don't match!"
print("✓ Batch results match!")

"""
Key Vectorization Techniques Used:
1. np.where() for conditional value assignment
2. np.select() for multiple conditions
3. Broadcasting for element-wise operations
4. np.clip() for bounding values
5. Vectorized array operations instead of loops
""" 