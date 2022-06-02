score = int(input("what is your score"))
if (score < 25):
    print("Grade F")
elif(score >= 25 and score <= 45):
    print("Grade E")
elif(score > 45 and score <= 50):
    print("Grade D")
elif(score > 50 and score <= 60):
    print("Grade C")
elif(score > 60 and score <= 80):
    print(("Grade B"))
elif(score > 80):
    print("Grade A")