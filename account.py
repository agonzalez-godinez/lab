class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        if amount <= 0:
            self.__account_balance += 0
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            self.__account_balance -= 0
            return False
        elif amount > self.__account_balance:
            self.__account_balance -= 0
            return False
        self.__account_balance -= amount
        if self.__account_balance < 0:
            self.__account_balance = 0
        return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name
