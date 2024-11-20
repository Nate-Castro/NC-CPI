#Nathaniel Castro ProfTest: Simple Quiz Game
score = 0
print("Welcome to The Quiz!\n", "Lets see how much you know about Math")

answer1 = input("""What is the answer to 25 X 2?(Please use the letter for answer)
                A. 27
                B. 50
                C. 94
                D. 81
                :""")
if answer1.lower() == "b":
    print("Correct")
    score += 1
    print("This is your score currently", score)
if answer1 != "b":
    print("Wrong")
    score +=0 
    print("This is your score currently", score)
    while answer1 != "b":
        wrong1 = input("""What is the name of the final boss in Hollow Knight?
                       A. Moss Kight
                       B. Bee Kinght
                       C. The Hollow Knight""")

