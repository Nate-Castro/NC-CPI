#Nathaniel Castro ProfTest: Tic-Tac-Toe Game
import random
print("Welcome to you tic-tac-toe game! You are X and the computer is O, Here is the board.")


grid = [[1,2,3],
[4,5,6],
[7,8,9]]
com1 = [1,2,3,4,5,6,7,8,9]


#def win():
   # if grid()



start = input("Would you like to play?: ")
if start == "yes":

    while start == "yes":
        print("Here is the board")
        for row in grid:
            print(row)


        while True:
            user = int(input("Where do you want to put your X? (Use number placement in table): "))


            for rownum, row in enumerate(grid):
                for placenum, place in enumerate(row):
                    if user == place:
                        grid[rownum][placenum] = "x"
                    elif user != row:
                        print("you need a valid space")

                    elif user == "x":
                        print("you need to chose a empty space")
                    elif user == "o":
                        print("you need to chose a empty space")    
            print("Here is the board")
            for row in grid:
                print(row)

            com_choice = random.choice(com1)

            for rownum, row in enumerate(grid):
                for placenum, place in enumerate(row):
                    if com_choice == place:
                        grid[rownum][placenum] = "o"
            print("Here is the board after the Computer places")
            for row in grid:
                print(row)

else:print("bye bye")