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
#if answer1 != "b":
else: 
    print("Wrong")
    score += 0 
    print("This is your score currently", score)
    print("Here is an easier question")
 #   while answer1 != "b":
    wrong1 = input("""What is the name of the final boss in Hollow Knight?
                       A. Watcher Knight
                       B. Hive Kinght
                       C. The Hollow Knight
                       D. False Kinght
                       :""")             
    if wrong1.lower() == "c":
            print("Correct")
            score += 1
            print("This is your score currently", score)
    if wrong1.lower() != "c":
                print("Wrong")
                score += 0
                print("This is your score currently", score)
answer2 = input("""How many episodes of One Piece are there?
                A. 12
                B. 4
                C. Over 9000
                D. 1122
                :""")
if answer2.lower() == "d":
       print("Correct")
       score+= 1
       print("This is you score currently", score)
else:
        print("Wrong")
        score += 0
        print("This is your score currently", score)
        print("Here is an easier question")
        wrong2 = input("""What year did the War of 1812 happen?
                       A. 2024
                       B. 2077
                       C. 1812
                       D. Y2K
                       :""")             
        if wrong2.lower() == "c":
            print("Correct")
            score += 1
            print("This is your score currently", score)
        if wrong2.lower() != "c":
                print("Wrong")
                score += 0
                print("This is your score currently", score)
answer3