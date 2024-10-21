#Nathaniel Castro SkillPrac: Average Grade

grade1 = int(input("What is your %/ grade for period 1?: "))
grade2 = int(input("What is your %/ grade for period 2?: "))
grade3 = int(input("What is your %/ grade for period 3?: "))

grade6 = int(input("What is your %/ grade for period 6?: "))
grade7 = int(input("What is your %/ grade for period 7?: "))
grade8 = int(input("What is your %/ grade for period 8?: "))

total = grade1 + grade2 + grade3 + grade6 + grade7 + grade8

av = total / 6
print("Your average grade is: %", av)