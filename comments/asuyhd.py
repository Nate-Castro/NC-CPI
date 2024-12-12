#Nathaniel Castro ProfTest: Tic-Tac-Toe Game
import random
print("Welcome to you tic-tac-toe game! You are X and the computer is O, Here is the board.")


grid = [["1","2","3"],
["4","5","6"],
["7","8","9"]]

com1 = ["1","2","3","4","5","6","7","8","9"]

user_choices = ["1","2","3","4","5","6","7","8","9"]


if [0] == "x" and grid[0] == grid[1] and grid[1] == grid[2]:
    print("You win")


start = input("Would you like to play?: ")
if start.lower == "yes":

    while start == "yes":
        print("Here is the board")
        for row in grid:
            print(row)


        while True:
            user = str(input("Where do you want to put your X? (Use number placement in table): "))
            if user not in user_choices:
                 print("You cannot place here.")
                 continue
            else:
                grid[(int(user)) - 1] = "x"
                user_choices.pop([int(user) - 1])
                com1.pop([(int(user)) - 1])



            for rownum, row in enumerate(grid):
                for placenum, place in enumerate(row):
                    if user == place:
                        grid[rownum][placenum] = "x"
                        
                     
            print("Here is the board")
            for row in grid:
                print(row)

            if user_choices[0] == user_choices[1] and user_choices[1] == user_choices[2]:
                print("You win")
                break

            com_choice = random.choice(com1)
            if com_choice in user_choices:
                user_choices.pop([(int(com_choice)) - 1])
                com1.pop([(int(com_choice)) - 1])

            for rownum, row in enumerate(grid):
                for placenum, place in enumerate(row):
                    if com_choice == place:
                        grid[rownum][placenum] = "o"
            print("Here is the board after the Computer places")
            for row in grid:
                print(row)

else:print("bye bye")
board = [None,None,None,None,None,None,None,None,None]
if board[5-1] != None:
    print("NOOOOOOO YOU IDIOT")