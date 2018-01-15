# Arrays
print("\nArrays:")
import numpy as np
a = np.array([1, 2, 3])     # Create a rank 1 array
print(a)
print(type(a))
print(a.shape)
print(type(a.shape))
print(a[0], a[1], a[2])
a[0] = 5
print(a)
b = np.array([[1, 2, 3], [4, 5, 6]])    # Create a rank 2 array / matrix
print(b)
print(b.shape)
print(type(b))
print(b[0, 0], b[0, 1], b[1, 0])

# functions to create arrays:
a = np.zeros((2, 2))    # Create an array of all zeros
print(a)
b = np.ones((1, 2))
print(b)
c = np.full((2, 2), 7)
print(c)
d = np.eye(2)       # Create a 2x2 identity matrix
print(d)
e = np.random.random((2, 2))
print(e)