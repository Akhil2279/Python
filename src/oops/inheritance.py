#inheritance

# Parent class
class parent:
    def speak(self):
        print("Parent speaks")

# Child class
class child(parent):
    def listen(self):
        print("Child listens")

# Create object
d = child()

d.speak()  # inherited method
d.listen()   # own method


#Multiple Inheritance

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skill1()
obj.skill2()


#Multilevel Inheritance 

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skill1()
obj.skill2()

#Hierarchical Inheritance

# Parent class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

# Child class 1
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Child class 2
class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


# Creating objects
c = Car()
b = Bike()

# Calling parent class method
c.start()
b.start()

# Calling child class methods
c.drive()
b.ride()



