from user import User
from bankAccount import BankAccounts 
jeni = User("Jeni", "Ukperaj")
leo = User("Leo" , "Messi")
jon = User ("Jon", "Jones")

jeni.display_accounts_info()
jon.transfer_money(1000,'checking', jeni, 'savings')

jeni.display_accounts_info()

leo.display_accounts_info()
