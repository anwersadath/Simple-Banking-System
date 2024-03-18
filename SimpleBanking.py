class BankAccount:
    def __init__(self, account_number, account_holder, password, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.password = password
        self.balance = balance

    def login(self, account_number, username, password):
        return (self.account_number == account_number and
                self.account_holder == username and
                self.password == password)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount} deposited. New balance is {self.balance}.")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn. New balance is {self.balance}.")
        else:
            print("Invalid transaction. Please check the amount and try again.")

    def check_balance(self):
        print(f"Your current balance is {self.balance}.")

#Usage
# Creating an account
account = BankAccount("123456", "Bob", "password123")

# Account login
account_number_input = input("Enter account number: ")
username_input = input("Enter username: ")
password_input = input("Enter password: ")
if account.login(account_number_input, username_input, password_input):
    print("Login successful!")
    # Check balance
    account.check_balance()

    # Deposit
    amount_to_deposit = float(input("Enter amount to deposit: "))
    account.deposit(amount_to_deposit)

    # Withdrawal
    amount_to_withdraw = float(input("Enter amount to withdraw: "))
    account.withdraw(amount_to_withdraw)
else:
    print("Invalid login credentials. Process terminated.")
