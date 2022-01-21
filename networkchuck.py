# /bin/python3

from unicodedata import name


print ("Hellow, welcome to NetworkChuck Coffie!!!!")

name = input("What is your Name?\n")

print("Hello " + name + ", Thank you so much for coming in today.\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappuchino"

print (name + " , what would you like from our mwny today? Here is what we are serving.\n" + menu)

order = input ()

print ("Sounds Good " + name + ", We'll have that " + order + " ready for you in a moment.") 
