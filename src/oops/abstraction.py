
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child class
class Car(Vehicle):
    def start(self):
        print("Car starts with key")

# Child class
class Bike(Vehicle):
    def start(self):
        print("Bike starts with button")


# Creating objects
c = Car()
b = Bike()

c.start()
b.start()

# output:
# Car starts with key
# Bike starts with button