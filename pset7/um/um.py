# import re
import re

# main function
def main():
    print(count(input("Text: ")))

# count function which counts ums
def count(s):
    # retirns num of ums
    return len(re.findall(r"(?i)(?<!\w)um(?!\w)", s))

# run main
if __name__ == "__main__":
    main()
