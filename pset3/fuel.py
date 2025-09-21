# def main function
def main():
    while True:
        # try to do this
        try:
            fraction = input("Fraction: ").strip()
            # splitting on /
            num, denom = fraction.split("/")
            # turning vars to ints
            num = int(num)
            denom = int(denom)

            # if num > denom reprompt
            if num > denom:
                continue
            # if num or denom < 0 reprompt
            if num < 0 or denom < 0:
                continue
            # converting fraction to percentage
            percent = num/denom
            percent = round(percent*100)
            # check for full
            if percent >= 99:
                print("F")
            # check for empty
            elif percent <= 1:
                print("E")
            # else print the percent full
            else:
               print(f"{percent}%")
            # quit
            break
        # if theres error pass
        except (ValueError, ZeroDivisionError):
            pass
# call main
main()

