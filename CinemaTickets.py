age = int(input("Enter your age"))
price = 6
if (age < 16):
    print("Price of ticket is $", price//2)
elif (age > 60):
    print("Price of ticket is $", price//3)
else:
    print("price of ticket is $", price)