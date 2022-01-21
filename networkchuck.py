# /bin/python3

from unicodedata import name
# epsode 1-2

print("Hellow, welcome to NetworkChuck Coffie!!!!")

name = input("What is your Name?\n")

print("Hello " + name + ", Thank you so much for coming in today.\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappuchino"

print(name + " , what would you like from our mwny today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your rotal is: $" + str(total))

print("Sounds Good " + name + ", We'll have your " +
      quantity + " " + order + " ready for you in a moment.")

# episode 3

# got it done
