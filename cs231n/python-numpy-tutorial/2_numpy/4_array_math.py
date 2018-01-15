import numpy as np
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))
# Elementwise difference; both produce the array
print(x - y)
print(np.subtract(x, y))
# Elementwise product; both produce the array
print(x * y)
print(np.multiply(x, y))
# Elementwise division; both produce the array
print(x / y)
print(np.divide(x, y))
# Elementwise square root; produce the array
print(np.sqrt(x))

# DOT
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
print(v.dot(x))
print(np.dot(v, x))
# Matrix / vector product; both produce the rank 2 array
print(x.dot(y))
print(np.dot(x, y))

# SUM
x = np.array([[1, 2], [3, 4]])
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

# T
x = np.array([[1, 2], [3, 4]])
print(x)
print(x.T)
v = np.array([1, 2, 3])
print(v)
print(v.T)