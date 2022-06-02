#movieInfo = {"Sean Connery": "From Russia With Love", "Roger Moore": "Live and Let Die", "Pierce Brosnan": "Die Another Day", "Daniel Craig": "Skyfall"}
#name1 = input("Name of first actor")
score = 0
for i in range(0,4):
    name1 = input("Name of the actor")
    if name1 == "Sean Connery":
        print("From Russia with Love")
        score = score +1
    elif name1 == "Roger Moore":
        print("Live and let Die")
        score = score +1
    elif name1 == "Pierce Brosnon":
        print("Die another Day")
        score = score +1
    elif name1 == "Daniel Craig":
        print("Skyfall")
        score = score +1
    else:
        print("That is not a Bond actor")
print("Final score is",score)

