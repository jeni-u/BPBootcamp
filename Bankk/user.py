from bankAccount import BankAccounts
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.checking = BankAccounts (int_rate = 0.8,balance =10000)
        self.savings = BankAccounts (int_rate = 0.5, balance = 6000)
    def make_deposit(self,account_type,amount):
        if account_type == "savings":
            self.savings.balance = self.savings.balance + amount
        else:
            self.checking.balance = self.checking.balance + amount

    def make_withdrawal(self,account_type,amount):
        if account_type == "savings":
            self.savings.balance = self.savings.balance - amount
        else:
            self.checking.balance = self.checking.balance - amount

    def display_accounts_info(self):
        print(f'User: {self.first_name} {self.last_name}, Balance on the checking account is: ${self.checking.balance}')
        print(f'User: {self.first_name} {self.last_name}, Balance on the savings account is: ${self.savings.balance}\n')
        return self
    
    def transfer_money(self,amount,self_account_type,other_user,other_user_account_type):
        if self_account_type == "savings" and other_user_account_type == "savings":
            self.savings.balance = self.savings.balance - amount
            other_user.savings.balance = other_user.savings.balance + amount

        elif self_account_type == "checking" and other_user_account_type == "checking":
            self.checking.balance = self.checking.balance - amount
            other_user.checking.balance = other_user.checking.balance + amount
        
        elif self_account_type == "savings" and other_user_account_type == "checking":
            self.savings.balance = self.savings.balance - amount
            other_user.checking.balance = other_user.checking.balance + amount
        else:
            self_account_type == "checking" and other_user_account_type == "savings"
            self.checking.balance = self.checking.balance - amount
            other_user.savings.balance = other_user.savings.balance + amount
