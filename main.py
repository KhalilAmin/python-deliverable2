import math
userName = input("Welcome to the GC Fruit Market! What is your name? ")
fruits = ["Apple $2", "Grape $1", "Orange $3"]
stillShopping = "y"
appleCount = 0
grapeCount = 0
orangeCount = 0
cart = 0
taxrate = .05
total = 0

while stillShopping == "y":
    print(f"Welcome {userName}. Which Fruit would you like to buy? ")
    for x in fruits:
        print(f"{fruits.index(x) + 1}. {x}")
    fruitChoice = input("> ")

    if fruitChoice == "1":
        print("You bought 1 Apple at $2")
        appleCount += 1
        cart += 2
    elif fruitChoice == "2":
        print("You bought 1 Grape at $1")
        grapeCount += 1
        cart += 1
    elif fruitChoice == "3":
        print("You bought 1 Orange at $3")
        orangeCount += 1
        cart += 3
    else:
        print("Sorry invalid option.")
    print("Would you like to buy another piece of fruit? y/n")
    stillShopping = input("> ")


if stillShopping == "n":
    print(f"Order for {userName}")
    print(f"{appleCount} apple(s) at $2 apiece")
    print(f"{grapeCount} grape(s) at $1 apiece")
    print(f"{orangeCount} orange(s) at $3 apiece")
    print(f"Sub Total: ${cart}")
    print(f"5% Tax: ${cart * taxrate}")
    print(f"Total: ${cart + (cart * taxrate)}")
