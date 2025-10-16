# import
import re

# main function
def main():
    print(parse(input("HTML: ")))

# parse function
def parse(s):
    # regex
    reg = r"<iframe[^>]*src=\"https?:\/\/(?:www\.)?youtube\.com\/embed\/(.+?)\"[^>]*>"
    # search for pattern
    matches = re.search(reg, s)
    if matches:
        # grab link
        return f"https://youtu.be/{matches.group(1)}"
    # else do nothing
    else:
        return None

# run main
if __name__ == "__main__":
    main()
