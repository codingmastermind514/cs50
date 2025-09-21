def main():
    # prompt user for time and convert to float
    time = input("What time is it? ")
    time = convert(time)

    # check against special meal times
    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")

    else:
        print("")


# time comes as a string in the format x:xx or xx:xx
def convert(time):
    # floating time
    new = time.split(':')
    return float(int(new[1])/60 + int(new[0]))


if __name__ == "__main__":
    main()
