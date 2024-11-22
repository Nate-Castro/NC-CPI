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
answer3 = input("""What is the name of the green mario guy?
                A. Mario
                B. Luigi
                C. Wario
                D. Waluigi
                :""")
if answer3.lower() == "b":
       print("Correct")
       score+= 1
       print("This is you score currently", score)
else:
        print("Wrong")
        score += 0
        print("This is your score currently", score)
        print("Here is an easier question")
        wrong3 = input("""What is the capital of Utah?
                       A. Sacremento
                       B. San Juan
                       C. The Tipanogos
                       D. Salt Lake City
                       :""")             
        if wrong3.lower() == "d":
            print("Correct")
            score += 1
            print("This is your score currently", score)
        if wrong3.lower() != "d":
                print("Wrong")
                score += 0
                print("This is your score currently", score)
answer4 = input("""What is the most popular song from MF DOOM?
                A. Deep Fried Frenz
                B. All Caps
                C. Rapp Snitch Knishes
                D. Rhymes Like Dimes
                :""")
if answer4.lower() == "c":
       print("Correct")
       score+= 1
       print("This is you score currently", score)
else:
        print("Wrong")
        score += 0
        print("This is your score currently", score)
        print("Here is an easier question")
        wrong4 = input("""Which villain is MF DOOM based off?
                       A. Victor Von Doom
                       B. Dio 
                       C. Bowser
                       D. Lego Batman
                       :""")             
        if wrong4.lower() == "d":
            print("Correct")
            score += 1
            print("This is your score currently", score)
        if wrong4.lower() != "d":
                print("Wrong")
                score += 0
                print("This is your score currently", score)
answer5 = input("""How much wood could a wood chuck chuck if a wood chuck could chuck wood?
                A. 13
                B. Makes no sense
                C. INCONCEIVABLE
                D. 4.15.15.13
                :""")
if answer5.lower() == "b":
       print("Correct")
       score+= 1
       print("This is you score currently", score)
else:
        print("Wrong")
        score += 0
        print("This is your score currently", score)
        print("Here is an easier question")
        wrong5 = input("""What is the hexcode for the color white?
                       A. #FFFFFF
                       B. #8F00FF
                       C. #40e0d0
                       D. #FFC0CB
                       :""")             
        if wrong5.lower() == "a":
            print("Correct")
            score += 1
            print("This is your score currently", score)
        if wrong5.lower() != "d":
                print("Wrong")
                score += 0
                print("This is your score currently", score)

print("Congradulations you have made it to the end of the quiz!!! Here is your final score", score)