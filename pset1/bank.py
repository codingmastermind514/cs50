def main():
    # taking user input for greeting
    greeting = input("Greeting: ").lower().strip()

    # if the word hello in greeting $0
    if 'hello' in greeting:
        print('$0')

    # if the first letter is h $20
    elif greeting[0] == 'h':
        print("$20")
        
    # anything else $100
    else:
        print("$100")

main()
