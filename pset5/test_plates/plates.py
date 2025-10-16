def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # checking the length of plate
    if len(s) in range(2,7):
        # checking first 2 chars are letters
        if s[0].isalpha() and s[1].isalpha():
            # checking if numers are in the middle
            if s.isalnum():
                flag = False
                for ch in s:
                    if flag and ch.isalpha():
                        return False

                    if ch.isdigit() and not flag and ch == "0":
                        return False

                    # update flag
                    if ch.isdigit():
                        flag = True
                    else:
                        flag = False
                return True
    return False


if __name__ == "__main__":
    main()
