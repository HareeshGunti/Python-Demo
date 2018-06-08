# Roll of a set of Dice

import random

print("Roll the dice? Y/N")
lRollAgain = input()
while 1 == 1:
    if lRollAgain == "Y":
        print(random.randint(1, 6))
        print(random.randint(1, 6))
        print("Roll the dice? Y/N")
        lRollAgain = input()
    elif lRollAgain == "N":
        break
    else:
        print("Enter Y/N. Roll the dice? Y/N")
        lRollAgain = input()

print("Good Bye!!")
