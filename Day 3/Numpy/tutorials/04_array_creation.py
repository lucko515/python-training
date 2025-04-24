# -----------------------------------------------------------------------------
# NUMPY ARRAY CREATION METHODS
# -----------------------------------------------------------------------------

import numpy as np

# 1. Creating from Python Sequences
print("1. FROM PYTHON SEQUENCES")
print("-" * 50)

list_1d = [1, 2, 3, 4, 5]
list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr_1d = np.array(list_1d)
arr_2d = np.array(list_2d)

tuple_1d = (1, 2, 3, 4, 5)
arr_1d = np.array(tuple_1d)

print(np.arange(10))
print(np.arange(5, 10))
print(np.arange(0, 11, 2))

print(np.linspace(0, 10, 50))


print(np.zeros((5, 5)))
print(np.ones((1024, 1024)) * 255)

print(np.random.rand(5, 5))

print(np.random.randn(5, 5))

original_array = np.random.randint(0, 256, (480, 480))

shallow_copy = original_array.view()
deep_copy = original_array.copy()