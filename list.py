#Nathaniel Castro ProfTest: Shopping list
list = []

while True:
    action = input("""What would you like to do?
                Enter 1 to add item
                Enter 2 to remove item
                Enter 3 to leave the list:\n""")

    if action == "1":
        x = input("What would you like to add to your list?: ")
        list.append(x) 
        print("This is your list currently", list)

    elif action == "2":
        x = input("What do you want to remove?: ")
        list.remove(x)
        print("This is your list currently", list)

    else:
        print("Have a nice day!")
        break
