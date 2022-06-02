class BankAccount:
    initialBalance = 10000
    def withdraw(self):
        newBalance = self.initialBalance - number1
        print("Your total is" ,newBalance)
    def deposit(self):
        newBalance = self.initialBalance + number1
        print("Your new total is", newBalance)
obj = BankAccount()
print("What would you like to do")
print("1. Withdraw")
print("2. Deposit")
user = int(input("Make a selection"))
if user == 1:
    print("How much would you like to withdraw")
    number1 = int(input("enter amount"))
    obj.withdraw()
elif user == 2:
    print("How much would you like to deposit")
    number1 = int(input("enter amount"))
    obj.deposit()
else:
    print("Invalid Selection")

