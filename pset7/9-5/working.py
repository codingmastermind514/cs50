# imports
import re
import sys

# main function
def main():
    #input
    print(convert(input("Hours: ")))

# convert function
def convert(s):
    # regex string
    reg = r"^([1-9]|[1][0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|[1][0-2])(?::([0-5][0-9]))? (AM|PM)$"
    # matches
    matches = re.fullmatch(reg, s)
    # if there are matches
    if matches:
        hour1, min1, ap1, hour2, min2, ap2 = matches.groups()
    # raise value error
    else:
        raise ValueError
    # converting to 24 hour time
    if ap1 == "PM" and hour1 != "12":
        hour1 = int(hour1) + 12
    if ap2 == "PM" and hour2 != "12":
        hour2 = int(hour2) + 12
    if hour1 == "12" and ap1 == "AM":
        hour1 = "00"
    if hour2 == "12" and ap2 == "AM":
        hour2 = "00"
    if min1 == None:
        min1 = "00"
    if min2 == None:
        min2 = "00"
    # return new times in f string
    return f"{int(hour1):02d}:{min1} to {int(hour2):02d}:{min2}"



if __name__ == "__main__":
    main()
