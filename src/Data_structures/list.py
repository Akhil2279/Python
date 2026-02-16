
#Creating a list
numbers = [10, 20, 30, 40, 50]
print(numbers)

# Access elements from list
numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Length of list
numbers = [1, 2, 3, 4, 5]
print("Length of list:", len(numbers))


#Add element to list
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#Insert element at specific position

numbers = [10, 20, 40]

numbers.insert(2, 30)
print(numbers)

#Remove element from list
numbers = [10, 20, 30, 40]

numbers.remove(20)
print(numbers)


#Remove duplicate values from list
num = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = set(num)

print("After removing duplicates:", unique_numbers)