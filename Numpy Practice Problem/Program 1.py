#Array operations using NumPy

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:")
print(arr)
print()

# a) Number of dimensions
print("Number of dimensions:", arr.ndim)

# b) Shape of array
print("Shape of array:", arr.shape)

# c) Size of array
print("Size of array:", arr.size)

# d) Type of elements
print("Type of elements:", arr.dtype)