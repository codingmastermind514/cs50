def main():
    # taking user input
    twttr = input("Input: ")
    print(f"Output: {shorten(twttr)}")

def shorten(word):
    # list of vowels
    vowels = ["a","e","i","o","u"]
    # for every char in twttr
    for char in word:
        # if character in vowel list
        if char.lower() in vowels:
            # replace the vowel with empty space
            word = word.replace(char,"")
    # print the output
    return word


if __name__ == "__main__":
    main()
