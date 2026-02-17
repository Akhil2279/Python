
# Even numbers

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
# Output:
# [2, 4, 6]


# Filter out words longer than 5 characters
words = ['apple', 'banana', 'cherry', 'date']

long_words = list(filter(lambda w: len(w) > 5, words))

print(long_words)
# Output:
# ['banana', 'cherry']


#Filter positive numbers
numbers = [-2, -1, 0, 1, 2, 3]

positive_numbers = list(filter(lambda x: x > 0, numbers))

print(positive_numbers)
# Output:
# [1, 2, 3]


# Filter names starting with A

names = ['Akhil', 'Bob', 'Charlie', 'David']

names_starting_with_a = list(filter(lambda name: name.startswith('A'), names))

print(names_starting_with_a)
# Output:
# ['Akhil']