weight=int(input("Enter your weight in (kg)"))
height=float(input("enter your height in (m)"))
BMI=weight/(height*height)
print("Your BMI is ", BMI)
if (BMI <18.5):
    print("You come in underweight category")
elif (BMI >18.5 and BMI < 25):
    print("You come in the normal category")
elif (BMI >25 and BMI < 30):
    print("You come in the overweight category")
else:
    print("You come in the obese category")
