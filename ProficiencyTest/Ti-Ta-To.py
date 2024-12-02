#Nathaniel Castro ProfTest: Tic-Tac-Toe Game
import random
print("Welcome to you tic-tac-toe game! You are X and the computer is O, Here is the board.")



column1 = ["    |      |", "    |      |", "    |      |"]
row1 = ["_________________"] 
b = 2
q = 2
f = 2
while b < 3:
    b += 1
    for x in column1:
        print(x)
for a in row1:
    print(a)
while q < 3:
    q += 1
    for x in column1:
        print(x)
for a in row1:
    print(a)
while f < 3:
    f += 1
    for x in column1:
        print(x)
user = input("""Where do you want to place?
             A. Top right
             B. Top middle
             C. Top left
             D. Middle left
             E. Middle
             F. Middle righ5t
             G. Bottom left
             H. Bottom middle
             I. Bottom right
             : """)
