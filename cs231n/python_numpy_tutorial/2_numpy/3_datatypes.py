import numpy as np

x = np.array([1, 2])    # Let numpy choose the datatype
print(x.dtype)
print(type(x))

x = np.array([1.0, 2.0])    # Let numpy choose the datatype
print(x.dtype)
print(type(x))

x = np.array([1, 2], dtype = np.int64)
print(x.dtype)
print(type(x))