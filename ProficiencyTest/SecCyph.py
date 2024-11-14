#Nathaniel Castro ProfTest: Secret Cypher

#string1 = input("Give your Shift Cypher: ")
def decode():
    string1 = input("Give your Shift Cypher: ")
    f = ""
    for x in string1:
        x = (ord(x)) + 1
    
    #for x in string1:
        f = f + (chr(x))
  
    print("The code you put was", string1)
    print("The new code is", f)



decode()

