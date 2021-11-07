print("welcome to the love calculator!")
name1 = str(input("what is your name? \n").lower())
name2 = str(input("what is their name? \n").lower())

name = name1 + name2

t = name.count("t")
u = name.count("u")
r = name.count("r")
e = name.count("e")

true = t+r+u+e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l+o+v+e
true_love = str(true) + str(love) 
print(true_love)