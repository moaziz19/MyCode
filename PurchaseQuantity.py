quantity = int(input("How many items do you have"))
Total = 100*quantity
if (quantity > 10):
    newTotal = Total -(Total * 0.1)
    print("New total after discount is", newTotal)
else:
    print("Sorry no discount. Your total is", Total)