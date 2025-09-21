# import sys and inflect
import sys
import inflect
# inflect engine
p = inflect.engine()
# empty list
names = []
# while loop
while True:
    # try block
    try:
        # input for name
        name = input("Name: ").capitalize().strip()
        # add name to names list
        names.append(name)
    # except ctrl d
    except EOFError:
        # newline
        print()
        # convert name to tuple
        names = tuple(names)
        # print adieu adieu to names
        print(f"Adieu, adieu, to {p.join(names)}")
        # exit
        sys.exit()


