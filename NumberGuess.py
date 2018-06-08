# This is guess the number game

import random
print("What is your name? ")
lName = input()

secretNumber = random.randint(1,20)

print(lName + ", I am thinking of a number between 1 and 20.")

for i in range(1, 6):
    print("Take a guess")
    guessNumber = int(input())

    if guessNumber < secretNumber:
        print("That is low " + lName)
    elif guessNumber > secretNumber:
        print("That is high " + lName)
    else:
        break

if guessNumber == secretNumber:
    print("Good job " + lName + "! You got the number " + str(secretNumber))
else:
    print("Nope. The number I was thinking was " + str(secretNumber))
