# creating empty dictionary
# value = 0
groceries = {}
# while loop kepps loping until ctrl d
while True:
    # try block
    try:
        # cleaning up and uppercasing empty input
        item = input("").upper().strip()
        # if the item in the dictionary
        if item in groceries:
            # add 1 to the value
            groceries[item]+=1
        # if the item not in dictionary
        if item not in groceries:
            # add item to the dictionary and set it to 1
            groceries[item] = 1
    # except for EOFError or ctrl d
    except EOFError:
        break
# converting groceries to a dict and sorting the keys
groceries = dict(sorted(groceries.items()))
# for each key in groceries
for key in groceries.keys():
    # print key
    print(f"{groceries[key]} {key}")
