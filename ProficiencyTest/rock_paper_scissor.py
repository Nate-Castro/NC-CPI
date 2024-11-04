#Nathaniel Castro ProfTest: Rock, Paper, Scissors

import random
#score =+ 1

game = ["rock", "paper", "scissors"]



play = input("Would you like to play rock, paper, scissors?: ")
if play == "no":
    print("Okay, bye bye")



if play == "yes":
    print("Okay")
    
    print("You go first")

while play == "yes":
     

    user1 = input("Rock, paper, or scissors?: ")
    if user1 not in ["rock", "scissor", "paper"]:
        print("Try again!!!")
    
    com1 = random.choice(game)
    print("The computer chooses", com1)
    
    if user1 == "scissors" and com1 == "rock":
        print("Computer wins!")

    elif user1 == "rock" and com1 == "scissors":
        print("User wins!")

    elif user1 == "rock" and com1 == "paper":
        print("Computer wins!")

    elif user1 == "paper" and com1 == "rock":
        print("User wins!")

    elif user1 == "paper" and com1 == "scissors":
        print("Computer wins!")

    elif user1 == "scissors" and com1 == "paper":
        print("User wins")

    else:
        print("It's a tie! go again.")