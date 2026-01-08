class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
    def deposit(self,ammount):
        self.balance+=ammount
        print(f"Final Balance ={self.balance}")
    
    def withdraw(self,ammount):
        print(f"Withdraw of Rs.{ammount} succesfully!!")
        self.balance-=ammount
        print(f"Remaining balance ={self.balance}")
    def check_balance(self):
        print(f"Balance is = {self.balance}")

acc1=BankAccount(12345,"Ankit",50000)
acc1.deposit(10_000)
acc1.withdraw(40_000)
acc1.check_balance()