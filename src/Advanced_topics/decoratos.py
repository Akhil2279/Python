
#Simple Decorator Example

# decorator function
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# using decorator
@my_decorator
def greet():
    print("Hello, welcome!")

greet()

#Output:
# Before function execution
# Hello, welcome!
# After function execution


# Decorator with user message

def login_decorator(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper

@login_decorator
def dashboard():
    print("Welcome to dashboard")

dashboard()

#Output:
# Checking login...
# Welcome to dashboard

