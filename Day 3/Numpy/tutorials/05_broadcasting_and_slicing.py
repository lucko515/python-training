# -----------------------------------------------------------------------------
# NUMPY BROADCASTING AND SLICING
# -----------------------------------------------------------------------------

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(arr[3])
# print(arr[-len(arr)])

# print(arr[-3:])

# print("->", arr[7:2:-1])

arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(arr_2d[1, 2])

print(arr_2d[1][::-1])

print(arr_2d[1, 1:3])

print(arr_2d[1:, 2:])

print(arr_2d[(arr_2d > 9) | (arr_2d < 3)])


### broadcasting
print("#" * 50)
arr = np.array([5, 3, 6, 8, 2])
print(arr + 5.5)

x = np.array([[1], [2], [3]]) # shape (3, 1)
y = np.array([4, 5, 6]) # shape (3,)

print(x + y)

a = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
b = np.array([1, 2, 3])

print(a.reshape(4, ) + b)