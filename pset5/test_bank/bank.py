def main():
    # taking user input for greeting
    greeting = input("Greeting: ")
    moolah = value(greeting)
    print(f"${moolah}")
    
def value(greeting):
    # if the word hello in greeting $0
    if greeting.lower().startswith("hello"):
        return 0

    # if the first letter is h $20
    elif greeting.lower().startswith("h"):
        return 20

    # anything else $100
    else:
        return 100


if __name__ == "__main__":
    main()
