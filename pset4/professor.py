# import random module
import random

# main function
def main():
    # call get_level
    lvl = get_level()
    score = 0
    # generate int
    for i in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)

        # track tries, repeat until 3 tries, when 3 tries, display answer ; ALSO we want to show how many they got right total
        tries = 0
        while tries < 3:
            try:
                # question
                operation = int(input(f"{x} + {y} = "))

                # if wrong ans
                if operation != x + y:
                    print("EEE")
                    tries += 1

                # if right ans...
                if operation == x + y:
                    score += 1
                    break

            except BaseException:
                print("EEE")
                tries += 1
                continue

        # if they've done 3 tries, print the correct answer as x + y = ans
        if tries == 3:
            print(f"{x} + {y} = {x+y}")

    # display the final score as Score: _
    print(f"Score: {score}")

# prompts (re-prompts) an integer 1, 2, 3 and returns it
def get_level():
    # while loop
    while True:
        # try block
        try:
            # input for level (stripped)
            level = int(input('Level: ').strip())
        # except value error
        except ValueError:
            pass
        # else
        else:
            # invalid level
            if level not in [1,2,3]:
                pass
            # else return level
            else:
                return level

# generates 1 int with level (1,2,3) digits & returns ValueError otherwise
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
