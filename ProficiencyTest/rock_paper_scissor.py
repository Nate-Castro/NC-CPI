#Nathaniel Castro ProfTest: Rock, Paper, Scissors

import random
#score =+ 1

com1 = ["rock", "paper", "scissors"]



play = input("Would you like to play rock, paper, scissors?: ")
if play == "no":
    print("Okay, bye bye")



if play == "yes":
    print("Okay")
    
    print("You go first")

user1 = input("Rock, paper, or scissors?: ")
print(random.choice(com1))

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