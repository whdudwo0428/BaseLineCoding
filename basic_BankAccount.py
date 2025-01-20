class BankAcount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def Deposit(self,amount):
        self.balance = self.balance + amount

    def Withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance = amount
        else:
            print("잔액부족")
    def display_balance(self):
        print("Balance : ", self.balance)

gongjea = BankAcount("Gongjae", 1570000)
gongjea.display_balance()
gongjea.Deposit(30000)
gongjea.display_balance()
gongjea.Withdraw(17000000)
gongjea.display_balance()
gongjea.Withdraw(1500000)
gongjea.display_balance()