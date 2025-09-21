"""
In a file called game.py, implement a program that:
Prompts the user for a level,n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random
import sys
while True:
    try:
        n = int(input("Level: "))
        break
    except ValueError:
        continue

num = random.randint(1,n)
while True:
    try:
        g = int(input("Guess: "))
        if g <= 0:
            continue
        if g > num:
            print("Too large!")
            continue
        elif g < num:
            print("Too small!")
            continue
        elif g == num:
            print("Just right!")
            sys.exit()
    except ValueError:
        continue

