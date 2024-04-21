class BankAccounts:
    def __init__(self, int_rate=0.2, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def display_account_info(self):
        self.balance()

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
