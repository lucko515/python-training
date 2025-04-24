import numpy as np

# Pitfall 1: Modifying views affects original array
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]  # Creates a view
print("Original array:", original)
print("View:", view)

view[0] = 10  # Modifies original array too!
print("\nAfter modifying view:")
print("Original array:", original)
print("View:", view)

copy = original[1:4].copy()
copy[0] = 20  # Doesn't affect original
print("\nAfter modifying copy:")
print("Original array:", original)
print("Copy:", copy)

size = 1000
data = np.random.random((size, size))

# Bad practice: Creates temporary large arrays
def inefficient_calculation(arr):
    temp1 = arr * arr  # Creates temporary
    temp2 = temp1 * arr  # Creates another temporary
    return temp2.sum()

def more_efficient(arr):
    return (arr ** 3).sum()

integers = np.array([1, 2, 3, 4])
floats = np.array([1.5, 2.5, 3.5, 4.5])
# Integer division
print("Integer division:", integers / 2)  # Converts to float
print("Floor division:", integers // 2)   # Stays integer

# Mixed type operations
mixed = integers + floats
print("\nMixed type result:", mixed)
print("Result dtype:", mixed.dtype)

data = np.array([1, 2, np.nan, 4, 5])
print("Array with NaN:", data)
print("Mean (with NaN):", data.mean())
print("Mean (ignoring NaN):", np.nanmean(data))