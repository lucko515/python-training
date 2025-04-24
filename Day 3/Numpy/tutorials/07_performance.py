# -----------------------------------------------------------------------------
# NUMPY PERFORMANCE OPTIMIZATION
# -----------------------------------------------------------------------------
import numpy as np
import time
import sys

size = 1000
arr_c = np.zeros((size, size), order='C')  # Row-major (C-style)
arr_f = np.zeros((size, size), order='F')  # Column-major (Fortran-style)

def access_by_rows(arr):
    start = time.time()
    for i in range(arr.shape[0]):
        row_sum = arr[i, :].sum()
    return time.time() - start

def access_by_cols(arr):
    start = time.time()
    for j in range(arr.shape[1]):
        col_sum = arr[:, j].sum()
    return time.time() - start

print("Row access time (C-order):", access_by_rows(arr_c))
print("Row access time (F-order):", access_by_rows(arr_f))
print("Column access time (C-order):", access_by_cols(arr_c))
print("Column access time (F-order):", access_by_cols(arr_f))

size = 1_000_000
data_float64 = np.random.random(size)  # Default float64
data_float32 = data_float64.astype(np.float32)
data_int64 = np.random.randint(0, 100, size)
data_int32 = data_int64.astype(np.int32)


def measure_computation(arr):
    start = time.time()
    for _ in range(100):
        result = np.sin(arr) * np.cos(arr)
    return time.time() - start

print("\nComputation time:")
print(f"float64: {measure_computation(data_float64):.4f} seconds")
print(f"float32: {measure_computation(data_float32):.4f} seconds")


# Example of view vs copy
arr = np.arange(1_000_000)

# Using view
start = time.time()
view = arr[::2]  # Creates a view
view_time = time.time() - start
print(f"View creation time: {view_time:.6f} seconds")

# Using copy
start = time.time()
copy = arr[::2].copy()  # Creates a copy
copy_time = time.time() - start
print(f"Copy creation time: {copy_time:.6f} seconds")

# Check if array owns its data
print("\nMemory ownership:")
print("View owns data:", view.flags.owndata)
print("Copy owns data:", copy.flags.owndata)


# Compare different ways to calculate mean
data = np.random.random(1_000_000)

# Method 1: Python loop
start = time.time()
mean1 = sum(data) / len(data)
time1 = time.time() - start

# Method 2: NumPy mean
start = time.time()
mean2 = data.mean()
time2 = time.time() - start


print(f"Python loop time: {time1:.6f} seconds")
print(f"NumPy mean time: {time2:.6f} seconds")


size = 1000
times = []

# Bad practice: Growing array
start = time.time()
arr = np.array([])
for i in range(size):
    arr = np.append(arr, i)
times.append(time.time() - start)
print(f"Growing array time: {times[0]:.6f} seconds")

# Good practice: Pre-allocation
start = time.time()
arr = np.zeros(size, dtype=np.int32) # int[] arr = new int[size];
for i in range(size):
    arr[i] = i
times.append(time.time() - start)
print(f"Pre-allocated time: {times[1]:.6f} seconds")