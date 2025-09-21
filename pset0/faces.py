# creating a function that converts :) and :( into real emojis

def convert():
    # prompting the user with an empty string for a sentence
    sentence = input('')

    # creating a variable called new which replaces (.replace) the :) and :( characters with 🙂 and 🙁 respectively
    new = sentence.replace(':)','🙂').replace(':(','🙁')

    # printing out the variable new
    print(new)

# assigning convert to a main() function
def main():
    convert()

# calling the main function
main()
