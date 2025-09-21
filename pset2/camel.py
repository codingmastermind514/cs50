
def main():
    # get input
    camel = input("camelCase: ")
    # for each character in in camel
    for char in camel:
        # uppercase letters are dectected
        upper = char.isupper()
        # if they are uppercase
        if upper == True:
            # put underscore in front of lowered character
            camel = camel.replace(char,f"_{char.lower()}")
    # print the 'snake case'
    print(f"snake_case: {camel}")

main()
