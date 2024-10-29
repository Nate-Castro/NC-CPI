#Nathaniel Castro SkillPrac: Password Validator

password = input("Give a password: ")
x = ("@", "#", "$", "%", "*", "&")

while x not in password:
    print("Try again and it must contain", x)
    input("Give new password")
