#Nathaniel Castro SkillPrac: Palindrome

word = input("Give a word: ")
palindrome = word [::-1]


if word == palindrome:
    print("This is a palindrome")
else:
    print("This is not a palindrome")