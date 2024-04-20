class BankAccount:
    instances = []
    def __init__(self, int_rate=0.2, balance=500): 
        self.int_rate = int_rate
        self.balance = balance 
        BankAccount.instances.append(self)

    def deposit(self, amount): 
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient funds.")
        else:
            self.balance = self.balance - amount
            print(self.balance)
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        

    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance * self.int_rate
        print(self.balance)
        return self
    
    @classmethod
    def all_instances(cls):
        for name in cls.instances:
            print(name)
    def __repr__(self):
        instance_number = BankAccount.instances.index(self) + 1
        return f"Instance: user{instance_number}"

user1 = BankAccount().deposit(50).deposit(150).deposit(20).withdraw(500).yield_interest()

user2=BankAccount().deposit(20).deposit(40).withdraw(50).withdraw(80).withdraw(70).yield_interest().display_account_info()

BankAccount.all_instances()
