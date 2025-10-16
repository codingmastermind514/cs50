def main():
    # grab the fraction, convert, and print level
    fraction = input("Fraction: ").strip()
    fraction = convert(fraction)
    print(gauge(fraction))

# takes frac string as input and outputs percentage as int
def convert(fraction):
    # repeat until valid input
    while True:
        try:
            # grab num and denom from string and convert to integer
            num, denom = fraction.split("/")
            num = int(num)
            denom = int(denom)

            # if num > denom: continue
            if num > denom:
                continue
            if num < 0 or denom < 0:
                continue

            percentage = num/denom
            percentage = round(percent*100)
            return percentage

        # catch errors for ...
        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    # if percent > 99: full
    if percentage >= 99:
        print("F")

    # if percent < 1: empty
    elif percentage <= 1:
        print("E")

    # else print percentage
    else:
        print(f"{percentage}%")

# run main
if __name__ == "__main__":
    main()
