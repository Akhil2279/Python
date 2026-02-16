
#simple function
def greet():
    print("Hello, welcome to Python programming!")
greet()


#functions with parameter
def greet(name):
    print("Hello", name)
greet("Akhil")


#Function to add two numbers
def add(a, b):
    result = a + b
    print("Sum:", result)

add(10, 20)

#Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_even_odd(7)

#Function to calculate the square of a number
def square(num):
    return num * num

number = int(input("Enter a number: "))
result = square(number)

print("Square is:", result)

#Function to check if a number is positive or negative

def check_number(num):
    if num >= 0:
        print("Positive")
    else:
        print("Negative")

check_number(-3)
