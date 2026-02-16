# Conditional statements with elif
if 5 > 3:
    print("5 is greater than 3.")
elif 5 == 3:
    print("5 is equal to 3.")   
else:
    print("5 is less than 3.")


# Check if a number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 100:
    print("The number is greater than 100.")
elif num == 100:
    print("The number is equal to 100.")
else :
    print("The number should be below than 100.")


# Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is", a)
elif b > c:
    print("Largest number is", b)
else:
    print("Largest number is", c)
