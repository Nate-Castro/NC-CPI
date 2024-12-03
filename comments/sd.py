#Nathaniel Castro ProfTest: Tic-Tac-Toe Game
import random
print("Welcome to you tic-tac-toe game! You are X and the computer is O, Here is the board.")


#column1 = ["    |      |", "    |      |"]# "    |      |"]
#row1 = ["_________________"] 

grid = [[1,2,3],
[4,5,6],
[7,8,9]]
b = 2
q = 2
f = 2
com1 = [1,2,3,4,5,6,7,8,9]
com_choice = random.choice(com1)





for row in grid:
    print(row)

user = int(input("Where do you want to put your X? (Use number placement in table): "))

for rownum, row in enumerate(grid):
    for placenum, place in enumerate(row):
        if user == place:
            grid[rownum][placenum] = "X"
for row in grid:
    print(row)
#win()
for rownum, row in enumerate(grid):
    for placenum, place in enumerate(row):
        if com_choice == place:
            grid[rownum][placenum] = "O"
for row in grid:
    print(row)


for row in grid:
    print(row)

user = int(input("Where do you want to put your X? (Use number placement in table): "))

for rownum, row in enumerate(grid):
    for placenum, place in enumerate(row):
        if user == place:
            grid[rownum][placenum] = "X"

for row in grid:
    print(row)
#win()
for rownum, row in enumerate(grid):
    for placenum, place in enumerate(row):
        if com_choice == place:
            grid[rownum][placenum] = "O"

for row in grid:
    print(row)




