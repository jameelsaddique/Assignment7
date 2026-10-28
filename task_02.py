class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Warning: insufficient balance.")
            return
        self.balance -= amount


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self.balance += self.balance * rate / 100


if __name__ == "__main__":
    account = SavingsAccount(1000)
    account.deposit(500)
    print(account.balance)
    account.add_interest(5)
    print(account.balance)
