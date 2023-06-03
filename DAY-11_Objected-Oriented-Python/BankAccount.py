class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print ("Deposit successful")
        else:
            print ("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print ("Withdrawal successful")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount of withdrawal.")

    def check_balance(self):
        print ("Account Balance", self.balance)

# Example Usage
account1 = BankAccount("HJ89SDP", 10000, "2023-05-30", "Hazel Museo")

account1.check_balance()  # Output: Account Balance: 10000

account1.deposit(5000)    # Output: Deposit successful.
account1.check_balance()  # Output: Account Balance: 15000

account1.withdraw(8000)   # Output: Withdrawal successful.
account1.check_balance()  # Output: Account Balance: 7000

account1.withdraw(10000)  # Output: Insufficient balance.