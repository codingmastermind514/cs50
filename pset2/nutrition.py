def main():
    # fruits dict storing fruits and their calories
    fruits = {
        "apple":130,
        "avocado":50,
        "banana":110,
        "cantaloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwifruit":90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80,
        "strawberries":50
    }
    # getting and lowercasing input
    item = input("Item: ").lower().strip()
    # if the item in fruits dict
    if item in fruits:
        # print the fruit's calories
        print(f"Calories: {fruits[item]}")

main()
