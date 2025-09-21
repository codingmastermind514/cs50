"""
https://cs50.harvard.edu/python/psets/4/figlet/
https://pypi.org/project/pyfiglet/

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

    1. Expects zero or two command-line arguments:
        a. Zero if the user would like to output text in a random font.
        b. Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.

    2. Prompts the user for a str of text.

    3.Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

"""
from pyfiglet import Figlet
import sys
import random

args = sys.argv[1:]
fonts = Figlet().getFonts()

# f = Figlet(font='slant')
# print(f.renderText('text to render'))

# len(args) = 0
# if False or Truef

if len(args) != 0 and len(args) != 2:
    sys.exit("Invalid Input")
else:
    if len(args) == 2:
        if args[0] != '-f' and args[0] != '--font':
            sys.exit("u put in the wrong thing dont crash my program u intellectually incompetent ignoramus")
        if args[1] not in fonts:
            sys.exit("not valid font")
        font = args[1]

    elif len(args) == 0:
        font = random.choice(fonts)

text = input("Input: ")
f = Figlet(font=font)
print(f.renderText(text))

