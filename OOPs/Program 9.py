#9. Bank Account System

class Account:
    def __init__(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print("Balance:", self.balance)

class sav_acct(Account):

    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

class cur_acct(Account):

    def withdraw(self, amount):
        self.balance -= amount

        if self.balance < 500:
            self.balance -= 50
            print("Penalty imposed")

name = input("Enter name: ")
acc_no = input("Enter account number: ")
acc_type = input("Enter account type (saving/current): ")
balance = float(input("Enter balance: "))

if acc_type == "saving":
    acc = sav_acct(name, acc_no, acc_type, balance)

    deposit = float(input("Enter deposit amount: "))
    acc.deposit(deposit)

    acc.add_interest()

    withdraw = float(input("Enter withdrawal amount: "))
    acc.withdraw(withdraw)

    acc.display()

else:
    acc = cur_acct(name, acc_no, acc_type, balance)

    deposit = float(input("Enter deposit amount: "))
    acc.deposit(deposit)

    withdraw = float(input("Enter withdrawal amount: "))
    acc.withdraw(withdraw)

    acc.display()