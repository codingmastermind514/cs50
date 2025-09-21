import statistics as stat
import sys

# function for testing some of the essential statistics library functions
def test_stats():
    vals = [100, 90, 99, 98, 89, 89, 89, 87, 97, 95, 97, 40, 90, 88, 100, 100]

    # find the mean/average
        # sum of vals/n vals
    print(stat.mean(vals))

    # find the median
        # middle val of sorted list
    print(stat.median(vals))

    # find the mode
        # most frequent value
    print(stat.mode(vals))


def try_sys():
    """
    Write a program that takes a name as a sys argument and says "Hello, {name}!"

        $ python notes.py Selena
        Hello, Selena!

    If the user does not provide a name, print out "Please provide name." and end the program.

    """
    try:
        args = sys.argv[1:]

        print(f"Hello, {args[0]}!")

    except IndexError:
        print("Please provide name.")


    args = sys.argv[1:]
    if len(args) != 0:
        print(f"Hello, {args[0]}!")
    else:
        sys.exit("Too few arguments.")


def my_lib():
    import labubu
    labubu.labubize("hello")


# API = tool we can use to make requests for information from companies or organizations using code
    # Application Program Interfaces
    # response - JSON format (dictionaries)

import requests
