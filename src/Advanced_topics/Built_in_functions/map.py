
# square numbers in a list using map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)
# Output:
# [1, 4, 9, 16, 25]


# convert list of strings to uppercase using map

strings = ['hello', 'world', 'python']
uppercase_strings = list(map(lambda s: s.upper(), strings))
print(uppercase_strings)
# Output:
# ['HELLO', 'WORLD', 'PYTHON']


# add two lists element-wise using map

list1 = [1, 2, 3]
list2 = [4, 5, 6]
added = list(map(lambda x, y: x + y, list1, list2))
print(added)
# Output:
# [5, 7, 9]


#Add 10 to each number

numbers = [1, 2, 3, 4, 5]
added_ten = list(map(lambda x: x + 10, numbers))
print(added_ten)
# Output:
# [11, 12, 13, 14, 15]


# Convert int to string

numbers = [1, 2, 3, 4, 5]
strings = list(map(lambda x: str(x), numbers))
print(strings)
# Output:
# ['1', '2', '3', '4', '5']