# imports
from pyfiglet import Figlet
import sys
import random

# command line argument
args = sys.argv[1:]
fonts = Figlet().getFonts()

# check for invalid input
if len(args) != 0 and len(args) != 2:
    sys.exit("Invalid Input")

# valid input
else:
    if len(args) == 2:
        # wrong CLI arg
        if args[0] != '-f' and args[0] != '--font':
            # system exit
            sys.exit("u put in the wrong thing dont crash my program u intellectually incompetent ignoramus")
        # check for invalid fonts
        if args[1] not in fonts:
            # system exit
            sys.exit("not valid font")

        # font
        font = args[1]

    # if no font provided then random font
    elif len(args) == 0:
        font = random.choice(fonts)

# input
text = input("Input: ")
# font
f = Figlet(font=font)
# print text in nice font
print(f.renderText(text))

