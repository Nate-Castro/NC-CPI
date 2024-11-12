#Nathaniel Castro ProfTest: Secret Cypher

string1 = input("Give your Shift Cypher: ")






def decode():
    for x in string1:
        #print(ord(x),end="=")
        print(ord(x))

        
        print(chr(ord(x) + 1))


    

decode()