import sys
import csv

# Exclude the first argument and grab cmd line args
args = sys.argv[1:]

# Too many command-line arguments
if len(args) > 2:
    sys.exit("Too many command-line arguments")

# Too few command-line arguments
if len(args) < 2:
    sys.exit("Too few command-line arguments")

# Not a CSV file
if not args[0].endswith(".csv") or not args[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# Open the file and read the lines
try:
    file = open(args[0], "r") # open file in read mode
    lines = file.readlines()[1:] # read lines
except FileNotFoundError:
    sys.exit(f"Could not read {args[0]}") # not real file

with open(f"{args[1]}", 'w') as csvfile: # open file as csvfile
    writer = csv.writer(csvfile) # writer
    hd = ["first","last","house"] # rows
    writer.writerow(hd) # write rows
    for line in lines: # for loop
        line = line.replace("\"","").replace(" ","").strip().split(",") # remove quotes
        newline =[line[1],line[0],line[2]] # rearranging order
        writer.writerow(newline) # write rows
