# Nathaniel Castro ProfTest: Graded Quiz
score = 0
quest1 = int(input("What is 7 + 5?: "))
answer1 = 12
if quest1 == answer1:
        score += 1
        print("Correct, 7 + 5 is", quest1)
    

quest2 = input("What is the name of the closest planet to the sun?: ")
answer2 = "Mercury"
if quest2 == answer2:
    score += 1
    print("Correct, the closest planet to the sun is", quest2)

quest3 = input("What is the language this was written on?: ")
answer3 =  "Python"
if quest3 == answer3:
    score += 1
    print("Correct, it was written on ",quest3)

quest4 = int(input("What is 76 rounded up by ten?: "))
answer4 = 80
if quest4 == answer4:
    score += 1
    print("Correct, 76 rounded up is ",quest4)
                
quest5 = input("What is the color of UCAS logo?: ")
answer5 = "Green"
if quest5 == answer5:
    score +=1
    print("Correct, the color of it is ",quest5)
print("Your score is",score)