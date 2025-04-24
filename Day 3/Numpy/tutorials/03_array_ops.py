# -----------------------------------------------------------------------------
# NUMPY ARRAY OPERATIONS
# -----------------------------------------------------------------------------

import numpy as np

# 1. Basic Arithmetic Operations
print("1. BASIC ARITHMETIC")
print("-" * 50)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(b / a)

x = np.array([0, 30, 45, 60, 90])
print(np.cos(x * np.pi / 180))

# sigmoid - 1/1*e^(-x)
x_1 = np.random.randn(196, 55, 55)
sigmoid_x = 1 / (1 + np.exp(-x_1))
# print(sigmoid_x)

# comparing

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 3, 3, 2, 5])

print(all(a < b))

# RELU
a = np.array([-1, 2, -3, 4, 5])
a[a < 0] = 0
print(a)

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])

print(A @ B)

print(A * B)

print("#"*50)
# Aggregation
arr = np.array([[1, 2, 3],
                [4, 35, 6],
                [7, -8, 9]])


print(arr.sum())
print(arr.mean())
print(arr.std())
print(arr.max())
print(arr.min())

print((arr - arr.std()) / arr.mean())

print(np.argmin(arr))
print(np.argmax(arr))