class Account:
    """
    A class representing details for an account object
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an Account object
        :param name: Account holders first name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit input amount
        :param amount: deposit amount
        :return: Boolean return True if transaction was successful, False if not
        """
        if amount <= 0:
            self.__account_balance += 0
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdrawl input amount
        :param amount: withdrawl amount.
        :return: Boolean return True if transaction was successful, False if not
        """
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

    def get_balance(self) -> float:
        """
        Method to access balance
        :return: account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access account holders name
        :return: account name
        """
        return self.__account_name
