#Nathaniel Castro ProfTest: Authorized

auth_user = ["Nate", "Devin", "Gavin", "Royal", "William", "Matthew", "Locklin", "Jude"]
user = input("What is your name: ")


if user in auth_user:
    print("You are allowed to come in")
else:
    print("No entry")