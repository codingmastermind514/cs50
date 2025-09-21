

months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December":"12"
}

# ask for input

while True:
    date = input("Date: ").strip().capitalize()
    # format 1: MONTH/DAY/YEAR
    # if it has slashes...
    if '/' in date:
        # try block
        try:
            month, day, year = date.split('/')
            month, day, year = int(month), int(day), int(year)
            if month in range(1,13) and day in range(1,32) and year in range(1,10000):
                # print year formatted to 4 digits, month & day 2 digits
                print(f"{year:04}-{month:02}-{day:02}")
                break
        # except value error
        except ValueError:
            continue

    # format 2: MONTH DAY, YEAR
    # elif it has commas
    elif ',' in date:
        # try block
        try:
            month, day, year = date.split(' ')
            month, day, year = int(months[month]), int(day.replace(',','')), int(year)
            # only doing if all aspects are correct
            if month in range(1,13) and day in range(1,32) and year in range(1,10000):
                # print year formatted to 4 digits, month & day 2 digits
                print(f"{year:04}-{month:02}-{day:02}")
                break
        # exception for key error w/ dictionary
        except KeyError:
            continue


