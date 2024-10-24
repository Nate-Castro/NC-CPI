#Nathaniel Castro SkillPrac: What is My Grade

print("Hello user and welcome to your grade finder outerer!")
classnum = input("What class would you like to check grade?: ")
grade = int(input(f"What is your percent grade for {classnum} ?: "))

if grade >= 90:
    print("You have an A")

elif grade >= 80 and grade < 90:
    print("You have a B")
elif grade >= 70 and grade < 80:
    print("You have a C")
elif grade >= 60 and grade < 70:
    print("You have a D")
else:
    print("You have an F")