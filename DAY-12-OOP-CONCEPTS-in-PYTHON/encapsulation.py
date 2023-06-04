class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number
    
    def set_account_number(self, new_account_number):
        self._account_number = new_account_number

    def get_balance(self):
        return self._balance
    
    def set_balance(self, new_balance):
        self._balance = new_balance

# Creating an instance of the BankAccount class
account = BankAccount("8437653927", 10000)

# Access and modify the account number and balance using the public methods
print("Account Number:", account.get_account_number())  
print("Balance:", account.get_balance())  

account.set_account_number("7386529435")
account.set_balance(50000)

print("Updated Account Number:", account.get_account_number())  
print("Updated Balance:", account.get_balance())  