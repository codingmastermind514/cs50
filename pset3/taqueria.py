# menu dictionary w/ price
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# make a total variable
total = 0
# keeps running until ctrl d or EOFError
while True:
    # try block
    try:
        # cleaning up and Title Casing the input
        item = input("Item: ").title().strip()
        # if the item in the dictionary
        if item in menu:
            # add to the total
            total += menu[item]
            # print total formatted to 2 dp
            print(f"Total: ${total:.2f}")
    # except EOFError
    except EOFError:
        break
