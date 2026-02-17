
# Simple Generator

def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)

# Output:
# 1

#Generator using loop

def count(n):
    for i in range(1, n+1):
        yield i

for value in count(5):
    print(value)

# Output:
# 1

