# -----------------------------------------------------------------------------
# CONVERTING PYTHON FUNCTIONS TO NUMPY
# -----------------------------------------------------------------------------

import numpy as np
from numpy import frompyfunc
import time


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Single value conversion:")
print(f"0°C = {celsius_to_fahrenheit(0)}°F")

temperatures = np.array([-40, 0, 37, 100])
print("\nTemperatures in Celsius:", temperatures)

vec_celsius_to_fahrenheit = np.vectorize(celsius_to_fahrenheit)
print(vec_celsius_to_fahrenheit(temperatures))

# Using frompyfunc
celsius_to_fahrenheit_ufunc = frompyfunc(celsius_to_fahrenheit, 1, 1)
print(celsius_to_fahrenheit_ufunc(temperatures))

def circle_area_python(radius):
    return 3.14159 * radius * radius

def circle_area_numpy(radius_array):
    return np.pi * np.square(radius_array)

radii = np.array([1, 2, 3, 4, 5])
print("Circle areas:")
print("Using vectorize:", np.vectorize(circle_area_python)(radii))
print("Using NumPy:", circle_area_numpy(radii))

def assign_grade_python(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'
    
def assign_grade_numpy(scores):
    grades = scores.copy()
    grades = np.where(scores < 70, 'F', grades)
    grades = np.where(scores >= 70, 'C', grades)
    grades = np.where(scores >= 80, 'B', grades)
    grades = np.where(scores >= 90, 'A', grades)
    return grades

scores = np.array([85, 95, 65, 75, 90])
print("\nGrades:")
vectorized_grade = np.vectorize(assign_grade_python)
print("Using vectorize:", vectorized_grade(scores))
print("Using NumPy:", assign_grade_numpy(scores))


def sigmoid_numpy(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_python(x):
    return 1 / (1 + np.exp(-x))

# Convert to ufunc
sigmoid_ufunc = frompyfunc(sigmoid_python, 1, 1)

x = np.array([-2, -1, 0, 1, 2])
print("Sigmoid function results:")
print("Using ufunc:", sigmoid_ufunc(x))
print("Using NumPy:", sigmoid_numpy(x))


size = 1_000_000
data = np.random.random(size) * 10 - 5  # Values between -5 and 5

# Test different implementations
def measure_time(func, data):
    start = time.time()
    result = func(data)
    return time.time() - start

# Regular Python (using list comprehension)
start = time.time()
python_result = [sigmoid_python(x) for x in data]
python_time = time.time() - start

# Vectorized function
vectorized_time = measure_time(np.vectorize(sigmoid_python), data)

# Universal function
ufunc_time = measure_time(sigmoid_ufunc, data)

# NumPy optimized
numpy_time = measure_time(sigmoid_numpy, data)

print("Time comparison for sigmoid calculation:")
print(f"Python list comprehension: {python_time:.6f} seconds")
print(f"Vectorized function: {vectorized_time:.6f} seconds")
print(f"Universal function: {ufunc_time:.6f} seconds")
print(f"NumPy optimized: {numpy_time:.6f} seconds")