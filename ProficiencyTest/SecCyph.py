#Nathaniel Castro ProfTest: Secret Cypher

string1 = input("Give your Shift Cypher: ")



f = ""

def decode(f):
    for x in string1:
        print(ord(x))
    
    for x in string1:
        print(chr(ord(x) + 1))
  
  
  
   #     f = ""

  #      f += x



decode(string1)

