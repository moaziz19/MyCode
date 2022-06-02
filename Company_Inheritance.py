class Company:
    def companyID(self):
        print("Company Details")
    def employeeID(self):
        print("Employee Details")

class Employee(Company):
    def employeeID(self):
        print("Employee Details")
obj = Employee()
obj.employeeID()
