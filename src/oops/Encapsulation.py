
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Creating object
account = BankAccount(1000)

# deposit money
account.deposit(500)

# access balance using method
print(account.get_balance())

# output:
# 1500