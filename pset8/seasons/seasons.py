# imports
from datetime import date
import inflect
import sys

# take the date as YYYY-MM-DD and return it as a date() object
def parse(bd):
    try:
        # split
        y, m, d = bd.split("-")
        # int
        y, m, d = int(y), int(m), int(d)
        # date object
        return date(y, m, d)

    except:
        sys.exit("Invalid Date") # system exit

# convert mins to words
def convert(dob):
    p = inflect.engine() # inflect engine
    # print num of mins if dtae was efore today
    if  parse(dob) < date.today():
        print(f"{p.number_to_words((date.today() - parse(dob)).days * 24 * 60, andword="").capitalize()} minutes")
    # else system exit
    else:
        sys.exit("Invalid Date")
#nmain
def main():
    # get bday
    dob = input("Date of Birth: ").strip()
    convert(dob) # convert
# run main
if __name__ == "__main__":
    main()
