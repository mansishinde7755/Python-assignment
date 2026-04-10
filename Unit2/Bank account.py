class BankAccount:
    
    # Constructor to initialize account number and balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    # Method to check balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating an object
account1 = BankAccount(123456, 5000)

print("Account Number:", account1.account_number)

account1.deposit(1000)
account1.withdraw(2000)
account1.check_balance()