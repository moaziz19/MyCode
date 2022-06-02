class firstCar:
    def superClass1(self):
        print("This is the first car")

class secondCar:
    def superClass2(self):
        print("This is the second car")
        
class petrol(firstCar,secondCar):
    def gas(self):
        print("Both the super classes need me to run")

obj = petrol()
obj.gas()