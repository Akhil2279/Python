#Creating a set
numbers = {10, 20, 30, 40}
print(numbers)


#Adding elements to a set

numbers = {10, 20, 30}

numbers.add(40)
print(numbers)

#Removing elements from a set
numbers = {10, 20, 30, 40}
numbers.remove(20)
print(numbers)

#Remove duplicate values using set

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)
print(unique_numbers)


# Check element exists in set

numbers = {10, 20, 30}

if 20 in numbers:
    print("Element found")
else:
    print("Element not found")


#Find length of set

numbers = {10, 20, 30, 40}

print("Length:", len(numbers))



