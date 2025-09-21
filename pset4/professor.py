"""

https://cs50.harvard.edu/python/psets/4/professor/

In a file called professor.py, implement a program that:

    DONE: Prompts the user for a level. If the user does not input 1, 2, or 3, the program should prompt again.


    DONE: Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).


    TO DO: Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.


    TO DO: The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

Docs:
docs.python.org/3/library/random.html

"""

import random

def main():
    lvl = get_level()

    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        operation = int(input(f"{x} + {y} = "))

        if operation != x + y:
            print("EEE")

# prompts (re-prompts) an integer 1, 2, 3 and returns it
def get_level():
    while True:
        try:
            level = int(input('Level: ').strip())
        except ValueError:
            pass
        else:
            if level not in [1,2,3]:
                pass
            else:
                return level

# generates 1 int with level (1,2,3) digits & returns ValueError otherwise
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
