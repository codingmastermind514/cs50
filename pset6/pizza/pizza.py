# Step 1: Checking our command-line arguments for correctness
import sys
from tabulate import tabulate

args = sys.argv

# Too many command-line arguments
if len(args) > 2:
    sys.exit("Too many command-line arguments")

# Too few command-line arguments
if len(args) < 2:
    sys.exit("Too few command-line arguments")

# Not a CSV file
if not args[1].endswith(".csv"):
    sys.exit("Not a CSV file") # non csv file

# Step 2: Open the file and read the lines
try:
    file = open(args[1], "r")
    lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist") # not real file

# Step 3: Go through each item of the list and turn it into a list
table = [] # table list

for line in lines: # for loop...
    if line != "\n": # not newline
        line = line.strip().split(",") # remove whitespace and split on comma
        table.append(line) # add to list

# print in table format
print(tabulate(table, headers="firstrow", tablefmt = "grid")#)
