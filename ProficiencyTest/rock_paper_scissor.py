#Nathaniel Castro ProfTest: Rock, Paper, Scissors

import random
score = 0

game = ["rock", "paper", "scissors"]



play = input("Would you like to play rock, paper, scissors?: ")
if play == "no":
    print("Okay, bye bye!")



if play == "yes":
    print("Okay")
    
    print("You go first")

while play == "yes":
    
    user1 = input("Rock, paper, or scissors?: ")
    
    while user1 not in ["rock", "paper", "scissors"]:
        print("Try again")
        user1 = input("Rock, paper, or scissors?: ")
        if user1 == ["rock", "paper", "scissors"]:
            break

    
    com1 = random.choice(game)
    print("The computer chooses", com1)
    
    if user1 == "scissors" and com1 == "rock":
        print("Computer wins!")
        score -= 1


    elif user1 == "rock" and com1 == "scissors":
        print("User wins!")
        score += 1

    elif user1 == "rock" and com1 == "paper":
        print("Computer wins!")
        score -= 1

    elif user1 == "paper" and com1 == "rock":
        print("User wins!")
        score += 1

    elif user1 == "paper" and com1 == "scissors":
        print("Computer wins!")
        score -= 1

    elif user1 == "scissors" and com1 == "paper":
        print("User wins")
        score += 1

    else:
        print("It's a tie! Go again.")

    #if "User wins!":
     #   score =+ 1
    #elif "Computer wins!":
    #    score =- 1
    #elif "It's a tie! Go again.":
     #   score += 0
    print("This is your current score", score)

    end = input("Would you like to continue?: ")

    if end == "yes":
        print("Okay, go again")

    if end == "no":
        print("Okay!")
        break