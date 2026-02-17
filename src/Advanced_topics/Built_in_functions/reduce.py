

# importing reduce function from functools module
from functools import reduce

# Sum of numbers
numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, numbers)
print(result)

# Output:
# 10


# Product of numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(product)
# Output:
# 24


# Find maximum in a list
numbers = [3, 1, 4, 1, 5]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)
# Output:
# 5


# Concatenate a list of strings
strings = ['Hello', ' ', 'World', '!']
concatenated = reduce(lambda a, b: a + b, strings)
print(concatenated)
# Output:
# Hello World!

# Find the longest string in a list
strings = ['apple', 'banana', 'cherry', 'date']
longest = reduce(lambda a, b: a if len(a) > len(b) else b, strings)
print(longest)
# Output:
# banana

