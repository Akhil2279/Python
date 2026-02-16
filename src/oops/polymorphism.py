
class Developer:
    def work(self):
        print("Developer writes code")

class Manager:
    def work(self):
        print("Manager manages the team")

class Tester:
    def work(self):
        print("Tester tests the software")


# Polymorphism
employees = [Developer(), Manager(), Tester()]

for emp in employees:
    emp.work()
