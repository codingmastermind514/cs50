# imports
import random
import sys

# while loop
while True:
    # try block
    try:
        # level
        n = int(input("Level: "))
        break
    # except value error
    except ValueError:
        # reprompt
        continue

# randomly generates num between 1 and n
num = random.randint(1,n)

# while loop
while True:
    # try block
    try:
        # input
        g = int(input("Guess: "))

        # if guess is negative reprompt
        if g <= 0:
            continue
        # if guess is too big reprompt
        if g > num:
            print("Too large!")
            continue
        # if guess is too small reprompt
        elif g < num:
            print("Too small!")
            continue
        # if guess is correct
        elif g == num:
            print("Just right!")
            # exit
            sys.exit()
    # except value error reprompt
    except ValueError:
        continue

