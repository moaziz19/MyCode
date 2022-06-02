class MainAccount:
    accountHolder = "Aziz"
    def holderName (self):
        print("This account belongs to", self.accountHolder)

class savingsAccount(MainAccount):
    def savingsAcc(self):
        print("This is the savings account")

class checkingAccount(MainAccount):
    def checkingAcc(self):
        print("This is the checking account")

class Deposits(MainAccount):
    def dep(self):
        print("These are account holders deposits")

obj = MainAccount()
obj = Deposits()
obj.holderName()
obj.dep()

