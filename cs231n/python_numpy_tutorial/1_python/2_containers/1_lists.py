xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')    # Add a new element to the end of the list
print(xs)
x = xs.pop()        # Remove and return the last element of the list
print(x, xs)
# Slicing
print("\nSlicing:")
nums = list(range(5))   # range is a built-in function that creates a list of int
print(nums)
print(nums[2:4])    # Get a slice from index 2 to 4 (exclusive)
print(nums[2:])     # Get a slice from index 2 to the end
print(nums[:2])     # Get a slice from the start to index 2 (exclusive)
print(nums[:])
print(nums[:-1])    # Slice indices can be negative
nums[2:4] = [8, 9]
print(nums)
# Loops
print("\nLoops:")
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# List comprehensions
print("\nList comprehensions:")
nums = list(range(5))
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)
squares = [x ** 2 for x in nums]
print(squares)
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)