# Step 1: Checking our command-line arguments for correctness
import sys
args = sys.argv

# Too many command-line arguments
if len(args) > 2:
    sys.exit("Too many command-line arguments")

# Too few command-line arguments
if len(args) < 2:
    sys.exit("Too few command-line arguments")

# Not a Python file
if not args[1].endswith(".py"): # not python file
    sys.exit("Not a Python file") # print

# Step 2: Open the file and read the lines
try:
    file = open(args[1], "r") # open file in read mode
    lines = file.readlines() # read lines
except FileNotFoundError: # non existent file
    sys.exit("File does not exist")

# Step 3: Loop through each item in the list and check...
count = 0
# for loop...
for line in lines:
    line = line.strip() # remove whitespace
    if not line.startswith("#") and line != "": # non comment and non empty line
        count += 1 # add to count
print(count) # print
