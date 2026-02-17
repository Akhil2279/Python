
# Add two numbers

add = lambda a, b: a + b
print(add(4, 6))
# Output:
# 10


# Square of a number
square = lambda x: x * x
print(square(5))
# Output:
# 25


# Sort a list of tuples based on the second element
data = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
# Output:
# [(2, 'a'), (1, 'b'), (3, 'c')]


# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output:   
# [2, 4, 6]

#Find maximum of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))
# Output:
# 20

