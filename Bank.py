# Object-Oriented-Bank-Account-Management-System

import random
from datetime import datetime

class BasicAccount:
    acNum = 0

    def __init__(self,acName,openingBalance):
        self.name = acName
        self.balance = openingBalance
        BasicAccount.acNum = BasicAccount.acNum + 1
        self.acNum = BasicAccount.acNum
        self.cardNum = "".join([str(random.randint(0,9))for _ in range(16)])
        self.cardExp = (datetime.now().month,int(str(datetime.now().year)[2:])+3)

    def __str__(self):
        return f"This account belongs to {self.name} and has the available balance of £{self.balance}"

    def deposit(self,amount:float):
        if amount<=0:
            print("You can only deposit the amount greater than 0")
            return
        else:
            self.balance = self.balance+amount

    def withdraw(self, amount:float):
        if amount <= 0:
            print("Cannot withdraw £",str(amount))
        if amount > self.balance:
            print("Cannot withdraw £",str(amount))
        else:
            self.balance -= amount
            print(self.name,"has withdrawn £",str(amount), "New balance is £",str(self.balance))

    def getAvailableBalance(self):
        return self.balance

    def getBalance(self):
        return self.balance

    def printBalance(self):
        print("Balance amount in your account is",str(self.balance))

    def getName(self):
        return self.name

    def getAcNum(self):
        return str(self.acNum)

    def issueNewCard(self):
        self.cardNum = "".join([str(random.randint(0,9))for _ in range(16)])
        self.cardExp = (datetime.now().month,int(str(datetime.now().year)[2:])+3)

    def closeAccount(self):
        self.withdraw(self.balance)
        return True

class PremiumAccount(BasicAccount):
    def __init__(self,acName:str,openingBalance:float,initialOverdraft:float):
        super().__init__(acName,openingBalance)
        self.overdraft = True
        self.overdraftLimit = initialOverdraft

    def str(self):
        return super().__str__() + f"\nOverdraft Limit: {self.overdraftLimit}"

    def setOverdraftLimit(self,newLimit:float):
        self.overdraftLimit = newLimit

    def getAvailableBalance(self):
        return self.balance + self.overdraftLimit

    def withdraw(self, amount: float):
        if amount <= 0:
            print('Cannot withdraw £',str(amount))
        if amount > self.balance + self.overdraftLimit:
            print('Cannot withdraw £',str(amount))
        else:
            self.balance -= amount
            print(self.name,'has withdrawn £', str(amount), 'New balance is £', str(self.balance))
            
    def printBalance(self):
        if self.balance < 0:
            limit = self.overdraftLimit + self.balance
            print(f"Current balance: {self.balance}\nOverdraft limit:", limit)
        else:
            print(f"Current balance: {self.balance}\nOverdraft limit:{self.overdraftLimit}.")

    def closeAccount(self):
        if self.overdraft > self.balance:
            print('Can not close account due to customer being overdrawn by £', self.overdraft)
            return False
        if self.overdraft < self.balance:
            super().closeAccount()
            self.withdraw(self.balance - self.overdraft)
            return True