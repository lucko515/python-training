# -----------------------------------------------------------------------------
# NUMPY VECTORIZATION
# -----------------------------------------------------------------------------
import numpy as np
import time

numbers = np.array([1, 2, 3, 4, 5])

print("Original array:", numbers)
print("Using vectorization:", numbers ** 2)

# python_squares = []
# for num in numbers:
#     python_squares.append(num ** 2)
# print("Using Python loop:", python_squares)

size = 1_000_000
data = np.random.random(size)


# start_time = time.time()
# python_result = []
# for x in data:
#     python_result.append(np.sin(x) * np.cos(x))
# python_time = time.time() - start_time
# print(f"Python loop time: {python_time:.4f} seconds")

start_time = time.time()
numpy_result = np.sin(data) * np.cos(data)
numpy_time = time.time() - start_time
print(f"NumPy vectorization time: {numpy_time:.4f} seconds")


data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original data:", data)

normalized = (data - data.min()) / (data.max() - data.min())
print("Normalized data:", normalized)

# Example 3: Image processing
print("\nImage processing example:")
image = np.random.randint(0, 256, (4, 4))  # Small example image
print("Original image:\n", image)

# Apply threshold
threshold = 128
binary_image = image > threshold
print("\nBinary image (threshold=128):\n", binary_image)