def main():
    # taking input for the cost of the meal and tip
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # printing how much tip to leave
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# format & convert $ amount (str) to float
def dollars_to_float(d):
    return float(d.replace("$", ""))

# format & convert % amount (str) to float
def percent_to_float(p):
    return float(p.replace("%",""))/100

main()
