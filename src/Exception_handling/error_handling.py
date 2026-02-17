

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


# Output:# Enter a number: 0
# Error: You cannot divide by zero.

#Handling Invalid Input Error
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid number.")

# Output:# Enter a number: abc
# Error: Please enter a valid number.


#Using Multiple Except Blocks

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input.")

# Output:# Enter first number: 10
# Enter second number: 0

# Using Finally Block
try:
    num = int(input("Enter a number: "))
    print("Number is:", num)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")

# Output:# Enter a number: abc
# Invalid input.


# Handling File Not Found Error
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")
