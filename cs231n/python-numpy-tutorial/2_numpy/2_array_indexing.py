# Slicing
print("\nSlicing:")
import numpy as np
# Create the following rank 2 array with shape (3, 4)
# [[1  2  3  4]
#  [5  6  7  8]
#  [9 10 11 12]]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# Use slicing to pull out the subarray consisting of the first 2 row
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)
# A slice of array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])
b[0, 0] = 77
print(a[0, 1])
# Create the following rank 2 array with shape (3, 4)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
row_r1 = a[1, :]        # Rank 1 view of the second row of a 降维
row_r2 = a[1:2, :]      # Rank 2 view of the second row of a 不降维
print(row_r1, row_r1.shape)     # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)     # Prints "[[5 6 7 8]] (1, 4)"
row_r1[0] = 88
print(a[1, 0])
row_r2[0, 0] = 99
print(a[1, 0])
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)     # Prints "[2 6 10] (3,)"
print(col_r2, col_r2.shape)     # Prints "[[ 2]
                                #          [ 6]
                                #          [10]] (3, 1)"
# Integer array indexing
print("\nInteger array indexing:")
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])        # Prints "[2, 2]"
print(np.array([a[0, 1], a[0, 1]]))
# Create a new array from which we will select elements
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)        # prints "[[ 1  2  3]
                #          [ 4  5  6]
                #          [ 7  8  9]
                #          [10 11 12]]"
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])   # Prints "[1 6 7 11]"
a[np.arange(4), b] += 10
print(a)        # prints "[[11,  2,  3]
                #          [ 4,  5, 16]
                #          [17,  8,  9]
                #          [10, 21, 12]]"
# Boolean array indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = a > 2        # Find the elements of a that are bigger than 2;
                        # this returns a numpy array of Booleans of the same
                        # shapes as a, where each slot of bool_idx tells
                        # whether that element of a is > 2.
print(bool_idx)
print(a[bool_idx])
print(a[a > 2])