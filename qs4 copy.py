class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}. New balance is {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}, Balance: {self.__balance}")


# Search from ai
class SavingsAccount(BankAccount): # Inherited instances of class BankAccount
    def __init__(self, account_number, balance = 0, interest_rate = 0.2):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}. New balance is {self.get_balance()}")


# Search from ai
class CheckingAccount(BankAccount): # Inherited instances of class BankAccount
    def __init__(self, account_number, balance = 0, overdraft_limit = 500):
        super().__init__(account_number, balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.__overdraft_limit:
            self._BankAccount__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.get_balance()}")
        else:
            print("Insufficient balance or invalid amount.")


savings = SavingsAccount("SA021", 1000)
savings.display_account_info()
savings.add_interest()
savings.display_account_info()

checking = CheckingAccount("CA123", 500)
checking.display_account_info()
checking.withdraw(800)
checking.display_account_info()
# Little bit calculation wrong will do it later