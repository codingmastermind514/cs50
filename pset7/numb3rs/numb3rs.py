# import
import re

# main function
def main():
    print(validate(input("IPv4 Address: ")))

# validate function
def validate(ip):
    # regex for first byte for IPv4 adress
    reg = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    # regex pattern for full IPv4 adress
    pattern = rf"^{reg}\.{reg}\.{reg}\.{reg}$"

    # if ip fullmatches pattern
    if re.fullmatch(pattern, ip):
        return True

    # else false
    else:
        return False

# run main
if __name__ == "__main__":
    main()
