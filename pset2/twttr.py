def main():
    # list of vowels
    vowels = ["a","e","i","o","u"]
    # taking user input
    twttr = input("Input: ")
    # for every char in twttr
    for char in twttr:
        # if character in vowel list
        if char.lower() in vowels:
            # replace the vowel with empty space
            twttr = twttr.replace(char,"")
    # print the output
    print(f"Output: {twttr}")


main()
