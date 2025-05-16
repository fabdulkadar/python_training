class BankAccount:
    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance

    def deposit(self,amount):
        self.__balance += amount
        print(f"Added ${amount}")

    def display_balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):
    def __init__(self,name,balance,interest):
        super().__init__(name,balance)
        self.interest = interest
    
    def add_interest(self):
        self.balance+=self.balance*self.interest

    def display_balance(self):
        print()
        print(f"Balance + Interest : {self.__balance}")

def display():
    print()

bnkacc = BankAccount("John",10000)
savings_account = SavingsAccount("John", 10000, 10)
bnkacc.deposit(100)
print(f"Available Balance : ${bnkacc.display_balance()}")
savings_account.display_balance()
