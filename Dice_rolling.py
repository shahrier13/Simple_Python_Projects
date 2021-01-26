import random

print("Dice Rolling Stimulator 1.0")

while True:
    number = random.randint(1, 6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|    X   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| X    X |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    X   |")
        print("|    X   |")
        print("|    X   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| X    X |")
        print("|        |")
        print("| X    X |")
        print("----------")
    if number == 5:
        print("----------")
        print("| X    X |")
        print("|    X   |")
        print("| X    X |")
        print("----------")
    if number == 6:
        print("----------")
        print("| X    X |")
        print("| X    X |")
        print("| X    X |")
        print("----------")

    print(f"---YOU HAVE ROLLED {number} ---")

    ext = input("Enter Y to carry on or X to stop: ")
    ext = ext.upper()
    if ext == "Y":
        x = input("Press Enter to roll again")
    else:
        break;

