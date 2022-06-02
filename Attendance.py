TotalClasses = int(input("How many total classes"))
ClassesAttended = int(input("How many classes have you attended"))
Percentage = (ClassesAttended/TotalClasses)*100
MedicalIssue = input("Do you have medical condition")
if (Percentage>75):
    print("Allowed to write exams")
elif (MedicalIssue.upper() == "Y"):
    print("Ok, you can write exams")
else:
    print("Sorry, not allowed to write exams")