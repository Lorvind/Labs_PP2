class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num

    def withdraw(self, num):
        if self.balance < num:
            raise ValueError("Insufficient Funds")

        self.balance -= num

    def show_balance(self):
        print(self.balance)

initial_balance, amount_to_withdraw = list(map(int, input().split()))

George = Account("Geaorge", initial_balance)

try:
    George.withdraw(amount_to_withdraw)
    George.show_balance()

except ValueError as error:
    print(error)