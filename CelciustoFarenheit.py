firstAmount = int(input("Enter the first amount in celcius:"))
secondAmount = int(input("Enter the last amount in celcius:"))

for i in range(firstAmount,secondAmount+1):
    z = (i * 9/5)+32
    print(i, end='   ')
    print(z)

