#Nathaniel Castro ProfTest: What are these numbers

x = int(input("Give a number over 1000: "))

txt = "That number is {:,}"
print(txt.format(x))

txt2 = "That number is {:.4f}"
print(txt2.format(x))

txt3 = "That number is {:.0%}"
print(txt3.format(x))

txt4 = "That number is ${:.2f}"
print(txt4.format(x))